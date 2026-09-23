#!/usr/bin/env python3
from __future__ import annotations
import hashlib, json, os, shutil, subprocess, sys, tempfile, zipfile
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]

checks = []
warnings = []
errors = []

def run(name: str, cmd: list[str], cwd: Path = ROOT):
    p = subprocess.run(cmd, cwd=cwd, text=True, capture_output=True)
    ok = p.returncode == 0
    checks.append({"name": name, "result": "PASS" if ok else "FAIL", "stdout": p.stdout.strip(), "stderr": p.stderr.strip()})
    if not ok:
        errors.append(f"{name} failed")
    return ok

def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open('rb') as f:
        for chunk in iter(lambda: f.read(1024*1024), b''):
            h.update(chunk)
    return h.hexdigest()

# Readiness must be repeatable even when CI has already built runtime artifacts.
# dist/ is generated output and is removed before source hygiene checks.
shutil.rmtree(ROOT / 'dist', ignore_errors=True)

# Static/runtime/test gates
run('project_lint', [sys.executable, 'scripts/validate-project.py'])
run('schemas', [sys.executable, 'scripts/validate-schemas.py'])
run('research_source_tests', [sys.executable, 'scripts/run-research-source-tests.py'])
run('strategic_derivation_tests', [sys.executable, 'scripts/run-strategic-derivation-tests.py'])
run('end_to_end', [sys.executable, 'scripts/run-end-to-end-tests.py'])
run('runtime_parity', [sys.executable, 'scripts/validate-runtime-parity.py'])
run('hygiene', [sys.executable, 'scripts/validate-hygiene.py'])

# GPT Byggaren 1.5 runtime registration and activation gate
project_cfg = yaml.safe_load((ROOT/'gpt-project.yaml').read_text(encoding='utf-8'))
registered_expected = {'chatgpt_chat','chatgpt_custom','claude_project','opencode','openai_plugin'}
categories_expected = {'behavior','capability','artifact','workspace_state','tool'}
registered = set(project_cfg.get('runtime_parity',{}).get('registered_runtimes',[]))
categories = set(project_cfg.get('runtime_parity',{}).get('compared_categories',[]))
candidates = {
    item.get('runtime_id'): item
    for item in project_cfg.get('analysis',{}).get('runtime',{}).get('candidates',[])
    if isinstance(item,dict) and item.get('runtime_id')
}
runtime_gate_errors = []
if registered != registered_expected:
    runtime_gate_errors.append('registered runtimes differ from GPT Byggaren 1.5 set')
if categories != categories_expected:
    runtime_gate_errors.append('runtime parity categories differ from GPT Byggaren 1.5 set')
if set(candidates) != registered_expected:
    runtime_gate_errors.append('not all registered runtimes have an assessment')
for runtime_id in ('chatgpt_chat','chatgpt_custom'):
    if candidates.get(runtime_id,{}).get('activate_by_default') is not True:
        runtime_gate_errors.append(f'{runtime_id} must be active by default')
for runtime_id in ('claude_project','opencode','openai_plugin'):
    item = candidates.get(runtime_id,{})
    if item.get('activate_by_default') is not False:
        runtime_gate_errors.append(f'{runtime_id} must remain inactive')
    if item.get('suitability') != 'reduced':
        runtime_gate_errors.append(f'{runtime_id} must be assessed as reduced')
for path, runtime_id in (
    ('distributions/chat/runtime/runtime-contract.json','chatgpt_chat'),
    ('distributions/custom-gpt/runtime/runtime-contract.json','chatgpt_custom'),
):
    target = ROOT/path
    if not target.is_file():
        runtime_gate_errors.append(f'missing {path}')
    else:
        try:
            payload = json.loads(target.read_text(encoding='utf-8'))
            if payload.get('runtime_id') != runtime_id:
                runtime_gate_errors.append(f'wrong runtime_id in {path}')
        except json.JSONDecodeError:
            runtime_gate_errors.append(f'invalid JSON in {path}')
checks.append({
    "name":"gpt_builder_1_5_runtime_registration",
    "result":"PASS" if not runtime_gate_errors else "FAIL",
    "details":runtime_gate_errors or {
        "registered":sorted(registered),
        "active":["chatgpt_chat","chatgpt_custom"],
        "assessed_inactive":["claude_project","opencode","openai_plugin"],
        "categories":sorted(categories),
    },
})
if runtime_gate_errors:
    errors.append('GPT Byggaren 1.5 runtime registration/activation gate failed')

# Runtime builds
run('chat_zip_build', [sys.executable, 'scripts/build-chat-zip.py'])
run('custom_gpt_build', [sys.executable, 'scripts/build-custom-gpt.py'])

# Release workflow simulation from a release tag.
with tempfile.TemporaryDirectory(prefix='release-readiness-') as td:
    out = Path(td) / 'release'
    ok = run('release_build_rc_simulation', [sys.executable, 'scripts/build-release.py', '--tag', 'v0.1.0-rc.1', '--output-dir', str(out)])
    if ok:
        expected = [
            out/'it-strategen-myndigheter-project-0.1.0-rc.1.zip',
            out/'it-strategen-myndigheter-chat-0.1.0-rc.1.zip',
            out/'it-strategen-myndigheter-custom-gpt-0.1.0-rc.1.zip',
            out/'SHA256SUMS.txt',
        ]
        missing = [str(p.name) for p in expected if not p.exists()]
        if missing:
            errors.append('release artifacts missing: ' + ', '.join(missing))
            checks.append({"name":"release_artifacts","result":"FAIL","details":missing})
        else:
            checks.append({"name":"release_artifacts","result":"PASS","details":[p.name for p in expected]})
            sums = {}
            for line in (out/'SHA256SUMS.txt').read_text(encoding='utf-8').splitlines():
                if not line.strip(): continue
                digest, filename = line.split(None, 1)
                sums[filename.strip()] = digest
            bad=[]
            for p in expected[:3]:
                if sums.get(p.name) != sha256(p): bad.append(p.name)
            checks.append({"name":"release_checksums","result":"PASS" if not bad else "FAIL","details":bad})
            if bad: errors.append('release checksum mismatch')

# Build scripts intentionally emit dist/ in the source tree; remove it after validation
# so the readiness check is repeatable and preserves source hygiene.
shutil.rmtree(ROOT / 'dist', ignore_errors=True)

# Documentation/readiness assets
required_docs = [
    ROOT/'README.md', ROOT/'PROJECT.md', ROOT/'STATUS.md', ROOT/'docs/development-plan.md',
    ROOT/'docs/project-hygiene-report.md', ROOT/'docs/runtime-parity-report.md',
    ROOT/'.github/workflows/ci.yml', ROOT/'.github/workflows/release.yml'
]
missing_docs=[str(p.relative_to(ROOT)) for p in required_docs if not p.exists()]
checks.append({"name":"documentation_and_workflows","result":"PASS" if not missing_docs else "FAIL","details":missing_docs})
if missing_docs: errors.append('required documentation/workflow files missing')

result = {
    "result": "PASS" if not errors else "FAIL",
    "blocking_errors": errors,
    "warnings": warnings,
    "checks_total": len(checks),
    "checks_passed": sum(1 for c in checks if c['result']=='PASS'),
    "checks": checks,
}
print(json.dumps(result, ensure_ascii=False, indent=2))
sys.exit(0 if not errors else 1)
