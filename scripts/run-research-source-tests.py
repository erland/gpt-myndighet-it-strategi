#!/usr/bin/env python3
from pathlib import Path
import json, sys

root = Path(__file__).resolve().parents[1]
cases_path = root / "tests" / "research-source-handling" / "cases.json"
source_model = (root / "docs" / "source-model.md").read_text(encoding="utf-8")
system = (root / "src" / "instructions" / "system.md").read_text(encoding="utf-8")
cases = json.loads(cases_path.read_text(encoding="utf-8"))

errors = []
required_ids = {
    "RS01_WELL_DOCUMENTED_AGENCY",
    "RS02_SMALL_AGENCY_FEW_DOCUMENTS",
    "RS03_CONFLICTING_SOURCES",
    "RS04_OLD_STRATEGY_NEW_STEERING",
    "RS05_MISSING_BUDGET_BASIS",
    "RS06_WEAK_THIRD_PARTY_SOURCE",
    "RS07_FAST_MOVING_IT_TREND",
}
ids = {c.get("id") for c in cases}
missing = required_ids - ids
if missing:
    errors.append("Missing required cases: " + ", ".join(sorted(missing)))
if len(ids) != len(cases):
    errors.append("Duplicate test case ids")
for c in cases:
    for key in ("id", "title", "scenario", "expect"):
        if key not in c:
            errors.append(f"{c.get('id','<unknown>')}: missing {key}")
    if not isinstance(c.get("expect"), dict) or not c.get("expect"):
        errors.append(f"{c.get('id','<unknown>')}: expect must be a non-empty object")

required_source_markers = [
    "Auktoritet", "Aktualitet", "Direkt relevans", "Oberoende",
    "Informationsluckor", "Triangulering", "Konfliktmodell"
]
for marker in required_source_markers:
    if marker not in source_model:
        errors.append(f"source model missing marker: {marker}")

runtime_markers = [
    "Myndighetsspecifik evidens väger tyngre än generell IT-trendinformation.",
    "best effort",
]
for marker in runtime_markers:
    if marker.lower() not in system.lower():
        errors.append(f"canonical runtime missing marker: {marker}")

print(f"Research/source cases checked: {len(cases)}")
if errors:
    for e in errors:
        print("ERROR:", e)
    sys.exit(1)
print("PASS: research and source-handling test suite is complete and contract-aligned")
