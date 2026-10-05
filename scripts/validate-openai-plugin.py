#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json, re, zipfile
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
SEMVER=re.compile(r"^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)(?:-[0-9A-Za-z.-]+)?(?:\+[0-9A-Za-z.-]+)?$")

def main()->int:
    ap=argparse.ArgumentParser(); ap.add_argument("path",type=Path); a=ap.parse_args()
    path=a.path
    m=re.fullmatch(r"it-strategen-myndigheter-openai-plugin-(.+)\.zip",path.name)
    if not m or not SEMVER.fullmatch(m.group(1)): raise SystemExit("Fel pluginfilnamn/version")
    version=m.group(1)
    with zipfile.ZipFile(path) as z:
        bad=z.testzip()
        if bad: raise SystemExit(f"Skadad ZIP-post: {bad}")
        names=set(z.namelist())
        required={"plugin.json","README.md","VERSION","MANIFEST.json","runtime-contract.json","skills/it-strategen-myndigheter/SKILL.md"}
        missing=required-names
        if missing: raise SystemExit("Saknade pluginfiler: "+", ".join(sorted(missing)))
        if any(n.startswith("it-strategen-myndigheter/") for n in names): raise SystemExit("Plugin får inte ha wrapper-katalog")
        if any(n.endswith(".py") for n in names): raise SystemExit("Plugin får inte paketera runtime-Python")
        if z.read("VERSION").decode().strip()!=version: raise SystemExit("Plugin VERSION mismatch")
        plugin=json.loads(z.read("plugin.json"))
        if plugin.get("$schema")!="https://agent-plugins.org/schemas/1.0.0/plugin.schema.json": raise SystemExit("Plugin schema mismatch")
        if plugin.get("name")!="it-strategen-myndigheter" or plugin.get("version")!=version: raise SystemExit("Plugin metadata mismatch")
        contract=json.loads(z.read("runtime-contract.json"))
        if contract.get("runtime_id")!="openai_plugin": raise SystemExit("runtime_id mismatch")
        a=contract.get("adapter",{})
        if a.get("mode")!="skills_first" or a.get("compatibility")!="ready_runtime_dependent": raise SystemExit("adapter mismatch")
        for key in ("web_research","filesystem_read","filesystem_write","persistent_state"):
            if a.get(key)!="required_host_runtime": raise SystemExit(f"Host dependency mismatch: {key}")
        if a.get("code_execution")!="optional_host_runtime": raise SystemExit("code_execution mismatch")
        if a.get("state_authority")!="workspace_file" or a.get("state_path")!="project-status.yaml" or a.get("conversation_fallback") is not False: raise SystemExit("state contract mismatch")
        if a.get("mcp_generated") is not False or a.get("script_resources")!=[]: raise SystemExit("Plugin får inte paketera MCP/scripts")
        skill=z.read("skills/it-strategen-myndigheter/SKILL.md").decode()
        canonical=(ROOT/"src/instructions/system.md").read_text(encoding="utf-8").strip()
        if canonical not in skill: raise SystemExit("SKILL saknar canonical behavior")
        for marker in ("faktisk webbresearch","project-status.yaml","chattminne är inte fallback","Inga runtime-skript","Ingen MCP-wrapper"):
            if marker not in skill: raise SystemExit(f"SKILL saknar runtime marker: {marker}")
        for p in sorted((ROOT/"knowledge").glob("*.md")):
            target=f"skills/it-strategen-myndigheter/references/knowledge/{p.name}"
            if target not in names or z.read(target)!=p.read_bytes(): raise SystemExit(f"Knowledge drift: {p.name}")
        for p in sorted((ROOT/"schemas").glob("*.schema.json")):
            target=f"skills/it-strategen-myndigheter/references/schemas/{p.name}"
            if target not in names or z.read(target)!=p.read_bytes(): raise SystemExit(f"Schema drift: {p.name}")
        pol="skills/it-strategen-myndigheter/references/policies/operational-execution-policy.md"
        if z.read(pol)!=(ROOT/"src/runtime-policy/operational-execution-policy.md").read_bytes(): raise SystemExit("Policy drift")
        manifest=json.loads(z.read("MANIFEST.json"))
        for item in manifest.get("files",[]):
            n=item["path"]
            if n not in names or hashlib.sha256(z.read(n)).hexdigest()!=item["sha256"]: raise SystemExit(f"Manifest SHA mismatch: {n}")
    print("PASS: OpenAI Plugin distribution")
    return 0
if __name__=="__main__": raise SystemExit(main())
