#!/usr/bin/env python3
from pathlib import Path
import json, sys

root = Path(__file__).resolve().parents[1]
cases_path = root / "tests" / "strategic-derivation" / "cases.json"
system_path = root / "src" / "instructions" / "system.md"

cases = json.loads(cases_path.read_text(encoding="utf-8"))
system = system_path.read_text(encoding="utf-8")
errors = []

required_ids = {
    "SD01_IRRELEVANT_TREND_REJECTED",
    "SD02_BUSINESS_NEED_TO_IT_GOAL",
    "SD03_NO_PRODUCT_WITHOUT_EVIDENCE",
    "SD04_GOAL_NOT_INITIATIVE",
    "SD05_TRACE_OBSERVATION_TO_RECOMMENDATION",
    "SD06_UNCERTAINTY_PROPAGATES",
    "SD07_SYMPTOM_TO_ROOT_GAP",
    "SD08_CHOICE_REQUIRES_ALTERNATIVES",
    "SD09_EXISTING_INITIATIVE_NOT_REINVENTED",
    "SD10_CAPACITY_CONSTRAINS_AMBITION",
    "SD11_MATURE_CAPABILITY_NOT_REINTRODUCED",
    "SD12_SMALL_AGENCY_PUBLIC_EVIDENCE_CEILING",
    "SD13_DOMAIN_TECH_NOT_INTERNAL_ADOPTION",
    "SD14_EXTERNAL_INTEROPERABILITY_AS_DRIVER",
    "SD15_SECURITY_PUBLIC_EVIDENCE_CEILING",
}
ids = [c.get("id") for c in cases]
missing = required_ids - set(ids)
if missing:
    errors.append("Missing required cases: " + ", ".join(sorted(missing)))
if len(ids) != len(set(ids)):
    errors.append("Duplicate test case ids")

for c in cases:
    for key in ("id", "title", "scenario", "expect"):
        if key not in c:
            errors.append(f"{c.get('id','<unknown>')}: missing {key}")
    if not isinstance(c.get("expect"), dict) or not c.get("expect"):
        errors.append(f"{c.get('id','<unknown>')}: expect must be a non-empty object")

runtime_markers = [
    "Myndighetsspecifik evidens väger tyngre än generell IT-trendinformation.",
    "lösningsneutral",
    "produkt",
    "spårbar",
    "osäker",
    "alternativ",
    "kapacitet",
    "public evidence ceiling",
    "sakuppdrag",
]
for marker in runtime_markers:
    if marker.lower() not in system.lower():
        errors.append(f"canonical runtime missing marker: {marker}")

required_schema_files = [
    "evidence-item.schema.json",
    "strategic-issue.schema.json",
    "it-strategic-goal.schema.json",
    "strategic-choice.schema.json",
    "transformation.schema.json",
]
for name in required_schema_files:
    if not (root / "schemas" / name).exists():
        errors.append(f"required traceability schema missing: {name}")

trace_case = next((c for c in cases if c.get("id") == "SD05_TRACE_OBSERVATION_TO_RECOMMENDATION"), None)
if trace_case:
    required_chain = trace_case.get("expect", {}).get("required_chain", [])
    expected_chain = ["source", "evidence", "strategic_issue", "it_strategic_goal", "strategic_choice"]
    if required_chain != expected_chain:
        errors.append("SD05 required_chain does not match canonical derivation chain")

print(f"Strategic derivation cases checked: {len(cases)}")
if errors:
    for e in errors:
        print("ERROR:", e)
    sys.exit(1)
print("PASS: strategic derivation test suite is complete and contract-aligned")
