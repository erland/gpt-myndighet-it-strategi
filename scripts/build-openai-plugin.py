#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import re
import zipfile
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
SEMVER=re.compile(r"^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)(?:-[0-9A-Za-z.-]+)?(?:\+[0-9A-Za-z.-]+)?$")

def sha(data: bytes)->str:
    return hashlib.sha256(data).hexdigest()

def write_zip(files: dict[str,bytes], out: Path)->None:
    out.parent.mkdir(parents=True,exist_ok=True)
    if out.exists(): out.unlink()
    with zipfile.ZipFile(out,"w",zipfile.ZIP_DEFLATED,compresslevel=9) as z:
        for name in sorted(files):
            info=zipfile.ZipInfo(name,date_time=(1980,1,1,0,0,0))
            info.compress_type=zipfile.ZIP_DEFLATED
            info.create_system=3
            info.external_attr=(0o100644<<16)
            z.writestr(info,files[name],compress_type=zipfile.ZIP_DEFLATED,compresslevel=9)

def main()->int:
    ap=argparse.ArgumentParser()
    ap.add_argument("--version")
    ap.add_argument("--output-dir",default=str(ROOT/"dist"))
    a=ap.parse_args()
    version=(a.version or (ROOT/"VERSION").read_text(encoding="utf-8")).strip()
    if not SEMVER.fullmatch(version):
        raise SystemExit(f"Ogiltig version: {version}")
    outdir=Path(a.output_dir)
    files: dict[str,bytes]={}

    canonical=(ROOT/"src/instructions/system.md").read_text(encoding="utf-8").strip()
    knowledge=sorted((ROOT/"knowledge").glob("*.md"))
    schemas=sorted((ROOT/"schemas").glob("*.schema.json"))
    policy=ROOT/"src/runtime-policy/operational-execution-policy.md"

    skill=(
        "---\n"
        "name: it-strategen-myndigheter\n"
        "description: Källspårbar och myndighetsanpassad IT-strategi med aktuell webbresearch, stegvis evidensbaserad analys och persistent arbetsstatus.\n"
        "---\n\n"
        "# IT-strategen för myndigheter\n\n"
        "## Plugin-runtime\n\n"
        "- Aktuell myndighetsstrategi kräver faktisk webbresearch från hosten. Utan webbförmåga får pluginen endast arbeta med explicit tillgängligt material och ska tydligt markera att aktuell offentlig styrning och omvärld inte har verifierats.\n"
        "- Workspace/file read och persistent state krävs för robust resumable flerstegsarbete. project-status.yaml i arbetsytan är auktoritativ status när den finns; chattminne är inte fallback.\n"
        "- File write krävs för att påstå att persistent status, strategi- eller projektartefakter har skapats eller uppdaterats.\n"
        "- Code execution är valfri hostförmåga för deterministisk analys av strukturerade data; pluginen innehåller inga runtime-skript.\n"
        "- Strategimetodik och analys av uppladdat material får fortsätta best effort när full hostkapacitet saknas, men slutsatser och leveransstatus ska begränsas proportionerligt.\n"
        "- Ingen MCP-wrapper genereras.\n\n"
        "## Canonical behavior\n\n"
        + canonical
        + "\n\n## References\n\n"
        + "\n".join(f"- references/knowledge/{p.name}" for p in knowledge)
        + "\n- references/policies/operational-execution-policy.md\n"
        + "\n## Structured contracts\n\n"
        + "\n".join(f"- references/schemas/{p.name}" for p in schemas)
        + "\n"
    ).encode()
    files["skills/it-strategen-myndigheter/SKILL.md"]=skill
    for p in knowledge:
        files[f"skills/it-strategen-myndigheter/references/knowledge/{p.name}"]=p.read_bytes()
    files["skills/it-strategen-myndigheter/references/policies/operational-execution-policy.md"]=policy.read_bytes()
    for p in schemas:
        files[f"skills/it-strategen-myndigheter/references/schemas/{p.name}"]=p.read_bytes()

    plugin={
        "$schema":"https://agent-plugins.org/schemas/1.0.0/plugin.schema.json",
        "name":"it-strategen-myndigheter",
        "version":version,
        "description":"Källspårbar IT-strategi för svenska myndigheter med aktuell research och persistent arbetsstatus.",
    }
    contract={
        "schema_version":1,
        "runtime_id":"openai_plugin",
        "version":version,
        "adapter":{
            "mode":"skills_first",
            "compatibility":"ready_runtime_dependent",
            "web_research":"required_host_runtime",
            "filesystem_read":"required_host_runtime",
            "filesystem_write":"required_host_runtime",
            "persistent_state":"required_host_runtime",
            "code_execution":"optional_host_runtime",
            "state_authority":"workspace_file",
            "state_path":"project-status.yaml",
            "conversation_fallback":False,
            "mcp_generated":False,
            "script_resources":[],
            "fallback_policy":{
                "without_web":"limit_to_explicit_material_and_do_not_claim_current_public_research_verified",
                "without_persistent_state":"allow_bounded_step_but_do_not_claim_robust_resume_or_status_update",
                "without_file_write":"do_not_claim_persistent_status_or_strategy_artifacts_created",
            },
        },
    }
    files["plugin.json"]=(json.dumps(plugin,ensure_ascii=False,indent=2)+"\n").encode()
    files["runtime-contract.json"]=(json.dumps(contract,ensure_ascii=False,indent=2)+"\n").encode()
    files["README.md"]=(
        "# IT-strategen för myndigheter – OpenAI Plugin\n\n"
        "Skills-first peer-runtime enligt GPT Byggaren 1.5.1. Aktuell webbresearch, workspace/file access och persistent state är hostberoenden. "
        "Knowledge, operational policy och strukturerade JSON Schemas paketeras som references. Inga runtime-skript eller MCP-wrapper ingår.\n"
    ).encode()
    files["VERSION"]=(version+"\n").encode()

    manifest={
        "schema_version":1,
        "runtime_id":"openai_plugin",
        "version":version,
        "entrypoint":"plugin.json",
        "files":[{"path":name,"sha256":sha(data),"bytes":len(data)} for name,data in sorted(files.items())],
    }
    files["MANIFEST.json"]=(json.dumps(manifest,ensure_ascii=False,indent=2)+"\n").encode()

    out=outdir/f"it-strategen-myndigheter-openai-plugin-{version}.zip"
    write_zip(files,out)
    digest=hashlib.sha256(out.read_bytes()).hexdigest()
    out.with_suffix(out.suffix+".sha256").write_text(f"{digest}  {out.name}\n",encoding="utf-8")
    print(out)
    print(digest)
    return 0

if __name__=="__main__":
    raise SystemExit(main())
