#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
errors: list[str] = []

ci = (ROOT / ".github/workflows/ci.yml").read_text(encoding="utf-8")
release = (ROOT / ".github/workflows/release.yml").read_text(encoding="utf-8")
build_release = (ROOT / "scripts/build-release.py").read_text(encoding="utf-8")

required_ci_commands = [
    "python scripts/validate-project.py",
    "python scripts/validate-schemas.py",
    "python scripts/run-research-source-tests.py",
    "python scripts/run-strategic-derivation-tests.py",
    "python scripts/run-end-to-end-tests.py",
    "python scripts/validate-runtime-parity.py",
    "python scripts/validate-hygiene.py",
    "python scripts/build-chat-zip.py",
    "python scripts/build-custom-gpt.py",
    "python scripts/validate-release-readiness.py",
]
for command in required_ci_commands:
    if command not in ci:
        errors.append(f"CI missing command: {command}")

for script in [
    "scripts/validate-project.py",
    "scripts/validate-schemas.py",
    "scripts/run-research-source-tests.py",
    "scripts/run-strategic-derivation-tests.py",
    "scripts/run-end-to-end-tests.py",
    "scripts/validate-runtime-parity.py",
    "scripts/validate-hygiene.py",
    "scripts/build-chat-zip.py",
    "scripts/build-custom-gpt.py",
]:
    if script not in build_release:
        errors.append(f"release builder missing script: {script}")

if "github.event.release.tag_name" not in release:
    errors.append("release workflow does not derive from GitHub Release tag")
if "python scripts/build-release.py" not in release:
    errors.append("release workflow does not invoke build-release.py")
if "SHA256SUMS.txt" not in release:
    errors.append("release workflow does not verify/publish checksum manifest")

if errors:
    for error in errors:
        print(f"FAIL: {error}")
    raise SystemExit(1)

print("PASS: CI/release workflow parity")
print("PASS: active runtime targets and release gates are aligned")
