#!/usr/bin/env python3
from __future__ import annotations
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FORBIDDEN_DIRS = {"dist", "build", "__pycache__", ".pytest_cache", ".mypy_cache", ".ruff_cache"}
FORBIDDEN_NAMES = {".DS_Store"}
FORBIDDEN_SUFFIXES = {".tmp", ".temp", ".pyc", ".pyo"}
errors: list[str] = []

for path in ROOT.rglob("*"):
    rel = path.relative_to(ROOT)
    # .git is not part of source artifacts and may exist in a real checkout.
    if ".git" in rel.parts:
        continue
    if path.is_dir() and path.name in FORBIDDEN_DIRS:
        errors.append(f"genererad/temporär katalog finns i källträdet: {rel}")
    if path.is_file():
        if path.name in FORBIDDEN_NAMES or path.suffix in FORBIDDEN_SUFFIXES:
            errors.append(f"temporär fil finns i källträdet: {rel}")

if errors:
    for error in errors:
        print(f"FAIL: {error}")
    raise SystemExit(1)

print("PASS: project hygiene")
print("PASS: inga förbjudna build-, cache-, OS- eller temporärfiler i källträdet")
