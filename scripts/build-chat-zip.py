#!/usr/bin/env python3
from __future__ import annotations
import hashlib
import shutil
import sys
import tempfile
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RUNTIME = ROOT / "distributions" / "chat" / "runtime"
VERSION = (ROOT / "VERSION").read_text(encoding="utf-8").strip()
OUTDIR = ROOT / "dist"
OUT = OUTDIR / f"it-strategen-myndigheter-chat-{VERSION}.zip"
SHA = OUT.with_suffix(OUT.suffix + ".sha256")

REQUIRED = [
    "START-HERE.md",
    "assistant/instructions.md",
    "assistant/policies/runtime-boundary.md",
    "runtime-manifest.yaml",
    "VERSION",
]
CORE_MARKERS = [
    "Myndighetsspecifik evidens väger tyngre än generell IT-trendinformation.",
    "Observation → källa → betydelse → strategisk konsekvens → rekommendation.",
    "Bygg strategin stegvis",
]

def fail(msg: str) -> None:
    raise SystemExit(f"FAIL: {msg}")

for rel in REQUIRED:
    if not (RUNTIME / rel).is_file():
        fail(f"saknad runtimefil: {rel}")

instructions = (RUNTIME / "assistant/instructions.md").read_text(encoding="utf-8")
for marker in CORE_MARKERS:
    if marker not in instructions:
        fail(f"canonical markör saknas i paketerad instruktion: {marker}")

if (RUNTIME / "assistant/instructions.md").read_bytes() != (ROOT / "src/instructions/system.md").read_bytes():
    fail("paketerad instruktion avviker från canonical källa")

knowledge = sorted((RUNTIME / "knowledge").glob("*.md"))
schemas = sorted((RUNTIME / "schemas").glob("*.schema.json"))
if len(knowledge) != 7:
    fail(f"förväntade 7 knowledge-filer, hittade {len(knowledge)}")
if len(schemas) != 11:
    fail(f"förväntade 11 schemas, hittade {len(schemas)}")

OUTDIR.mkdir(parents=True, exist_ok=True)
with zipfile.ZipFile(OUT, "w", compression=zipfile.ZIP_DEFLATED) as zf:
    for path in sorted(p for p in RUNTIME.rglob("*") if p.is_file()):
        zf.write(path, path.relative_to(RUNTIME))

with zipfile.ZipFile(OUT) as zf:
    bad = zf.testzip()
    if bad:
        fail(f"ZIP CRC-fel i {bad}")
    names = set(zf.namelist())
    for rel in REQUIRED:
        if rel not in names:
            fail(f"saknad fil i ZIP: {rel}")

sha = hashlib.sha256(OUT.read_bytes()).hexdigest()
SHA.write_text(f"{sha}  {OUT.name}\n", encoding="utf-8")
print(f"PASS: Chat ZIP byggd: {OUT}")
print(f"PASS: knowledge={len(knowledge)}, schemas={len(schemas)}, canonical parity=yes")
print(f"SHA256: {sha}")
