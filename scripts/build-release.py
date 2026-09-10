#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import os
import re
import shutil
import subprocess
import sys
import tempfile
import zipfile
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
TAG_RE = re.compile(r"^v?(?P<version>\d+\.\d+\.\d+(?:-(?:rc\.\d+|[0-9A-Za-z.-]+))?)$")


def fail(msg: str) -> None:
    raise SystemExit(f"FAIL: {msg}")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def run(cmd: list[str], cwd: Path) -> None:
    print("+", " ".join(cmd))
    subprocess.run(cmd, cwd=cwd, check=True)


def copy_source(src: Path, dst: Path) -> None:
    ignored = shutil.ignore_patterns(".git", "dist", "release-dist", "__pycache__", ".pytest_cache", ".mypy_cache", ".ruff_cache", "*.pyc")
    shutil.copytree(src, dst, ignore=ignored)


def sync_version(root: Path, version: str) -> None:
    (root / "VERSION").write_text(version + "\n", encoding="utf-8")
    (root / "distributions/chat/runtime/VERSION").write_text(version + "\n", encoding="utf-8")
    (root / "distributions/custom-gpt/runtime/VERSION").write_text(version + "\n", encoding="utf-8")

    gp_path = root / "gpt-project.yaml"
    gp = yaml.safe_load(gp_path.read_text(encoding="utf-8"))
    gp["project"]["version"] = version
    gp["runtime"]["chat_zip"]["artifact"] = f"dist/it-strategen-myndigheter-chat-{version}.zip"
    gp["runtime"]["custom_gpt"]["artifact"] = f"dist/it-strategen-myndigheter-custom-gpt-{version}.zip"
    gp["release"]["github"]["enabled"] = True
    gp["release"]["github"]["status"] = "implemented"
    gp_path.write_text(yaml.safe_dump(gp, allow_unicode=True, sort_keys=False), encoding="utf-8")

    manifest_path = root / "distributions/chat/runtime/runtime-manifest.yaml"
    manifest = yaml.safe_load(manifest_path.read_text(encoding="utf-8"))
    manifest["runtime"]["version"] = version
    manifest_path.write_text(yaml.safe_dump(manifest, allow_unicode=True, sort_keys=False), encoding="utf-8")

    cfg_path = root / "distributions/custom-gpt/runtime/custom-gpt-config.yaml"
    cfg = yaml.safe_load(cfg_path.read_text(encoding="utf-8"))
    cfg["custom_gpt"]["version"] = version
    cfg_path.write_text(yaml.safe_dump(cfg, allow_unicode=True, sort_keys=False), encoding="utf-8")

    start_path = root / "distributions/chat/runtime/START-HERE.md"
    start = start_path.read_text(encoding="utf-8")
    start = re.sub(r"(?m)^Version:\s*.*$", f"Version: {version}", start)
    start_path.write_text(start, encoding="utf-8")


def build_project_zip(staged_root: Path, out: Path) -> None:
    with zipfile.ZipFile(out, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        for path in sorted(p for p in staged_root.rglob("*") if p.is_file()):
            if any(part in {".git", "dist", "release-dist", "__pycache__"} for part in path.parts):
                continue
            zf.write(path, Path(staged_root.name) / path.relative_to(staged_root))
    with zipfile.ZipFile(out) as zf:
        bad = zf.testzip()
        if bad:
            fail(f"projekt-ZIP CRC-fel i {bad}")


def write_checksum(path: Path) -> Path:
    target = path.with_suffix(path.suffix + ".sha256")
    target.write_text(f"{sha256(path)}  {path.name}\n", encoding="utf-8")
    return target


def main() -> None:
    parser = argparse.ArgumentParser(description="Build versioned release artifacts from a GitHub Release tag")
    parser.add_argument("--tag", default=os.environ.get("GITHUB_REF_NAME"), help="Release tag, e.g. v0.1.0-rc.1")
    parser.add_argument("--output-dir", default=str(ROOT / "release-dist"))
    args = parser.parse_args()

    if not args.tag:
        fail("release tag saknas; använd --tag eller GITHUB_REF_NAME")
    match = TAG_RE.fullmatch(args.tag)
    if not match:
        fail(f"ogiltig release-tag: {args.tag}")
    version = match.group("version")

    output_dir = Path(args.output_dir).resolve()
    output_dir.mkdir(parents=True, exist_ok=True)
    for p in output_dir.glob("it-strategen-myndigheter-*"):
        if p.is_file():
            p.unlink()

    with tempfile.TemporaryDirectory(prefix="it-strategen-release-") as td:
        stage = Path(td) / "it-strategen-myndigheter"
        copy_source(ROOT, stage)
        sync_version(stage, version)

        # Samma valideringskedja som CI, nu på den versionssatta staged källan.
        checks = [
            "scripts/validate-project.py",
            "scripts/validate-schemas.py",
            "scripts/run-research-source-tests.py",
            "scripts/run-strategic-derivation-tests.py",
            "scripts/run-end-to-end-tests.py",
            "scripts/validate-runtime-parity.py",
            "scripts/validate-hygiene.py",
        ]
        for script in checks:
            run([sys.executable, script], stage)
        run([sys.executable, "scripts/build-chat-zip.py"], stage)
        run([sys.executable, "scripts/build-custom-gpt.py"], stage)

        chat = stage / "dist" / f"it-strategen-myndigheter-chat-{version}.zip"
        custom = stage / "dist" / f"it-strategen-myndigheter-custom-gpt-{version}.zip"
        if not chat.is_file() or not custom.is_file():
            fail("runtime-build saknar förväntad artefakt")

        out_chat = output_dir / chat.name
        out_custom = output_dir / custom.name
        shutil.copy2(chat, out_chat)
        shutil.copy2(custom, out_custom)

        project = output_dir / f"it-strategen-myndigheter-project-{version}.zip"
        build_project_zip(stage, project)

        artifacts = [project, out_chat, out_custom]
        checksum_files = [write_checksum(p) for p in artifacts]
        sums = output_dir / "SHA256SUMS.txt"
        sums.write_text("".join(f"{sha256(p)}  {p.name}\n" for p in artifacts), encoding="utf-8")

        for p in artifacts:
            with zipfile.ZipFile(p) as zf:
                bad = zf.testzip()
                if bad:
                    fail(f"ZIP CRC-fel i {p.name}: {bad}")

    print(f"PASS: release build för tag {args.tag} -> version {version}")
    for p in sorted(output_dir.iterdir()):
        if p.is_file():
            print(p)


if __name__ == "__main__":
    main()
