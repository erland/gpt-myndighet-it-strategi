#!/usr/bin/env python3
from __future__ import annotations

import ast
import json
from pathlib import Path
import sys
import yaml

ROOT = Path(__file__).resolve().parents[1]
ERRORS: list[str] = []

REQUIRED_FILES = [
    "README.md", "PROJECT.md", "STATUS.md", "VERSION", ".gitignore",
    "gpt-project.yaml", "project-status.yaml", "architecture.yaml",
    "src/instructions/system.md", "docs/development-plan.md",
]

for rel in REQUIRED_FILES:
    if not (ROOT / rel).is_file():
        ERRORS.append(f"saknad obligatorisk fil: {rel}")

for path in sorted(ROOT.rglob("*.yaml")) + sorted(ROOT.rglob("*.yml")):
    if any(part in {"dist", ".git"} for part in path.parts):
        continue
    try:
        yaml.safe_load(path.read_text(encoding="utf-8"))
    except Exception as exc:
        ERRORS.append(f"ogiltig YAML {path.relative_to(ROOT)}: {exc}")

for path in sorted(ROOT.rglob("*.json")):
    if any(part in {"dist", ".git"} for part in path.parts):
        continue
    try:
        json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        ERRORS.append(f"ogiltig JSON {path.relative_to(ROOT)}: {exc}")

for path in sorted((ROOT / "scripts").glob("*.py")):
    try:
        ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    except SyntaxError as exc:
        ERRORS.append(f"ogiltig Python-syntax {path.relative_to(ROOT)}:{exc.lineno}: {exc.msg}")

# Lätta textkontroller som fångar vanliga repo-/CI-fel utan att framtvinga stilverktyg.
for path in sorted(p for p in ROOT.rglob("*") if p.is_file()):
    if any(part in {"dist", ".git", "__pycache__"} for part in path.parts):
        continue
    if path.suffix.lower() not in {".md", ".yaml", ".yml", ".json", ".py", ".txt"} and path.name not in {"VERSION", ".gitignore"}:
        continue
    try:
        text = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        ERRORS.append(f"textfil är inte UTF-8: {path.relative_to(ROOT)}")
        continue
    if "\r\n" in text:
        ERRORS.append(f"CRLF upptäckt: {path.relative_to(ROOT)}")
    for idx, line in enumerate(text.splitlines(), start=1):
        if line.endswith(" ") or line.endswith("\t"):
            ERRORS.append(f"trailing whitespace: {path.relative_to(ROOT)}:{idx}")
            break

if ERRORS:
    for error in ERRORS:
        print(f"FAIL: {error}")
    raise SystemExit(1)

print("PASS: project lint")
print("PASS: required files, YAML, JSON, Python syntax, UTF-8 and whitespace checks")
