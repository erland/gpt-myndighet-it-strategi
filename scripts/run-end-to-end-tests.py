#!/usr/bin/env python3
import json
from pathlib import Path
from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]
SCENARIO = ROOT / "tests" / "end-to-end" / "scenario-tullverket.json"
SCHEMAS = ROOT / "schemas"

with SCENARIO.open(encoding="utf-8") as f:
    data = json.load(f)

schema_map = {
    "sources": "source-inventory.schema.json",
    "evidence": "evidence-item.schema.json",
    "drivers": "strategic-driver.schema.json",
    "issues": "strategic-issue.schema.json",
    "goals": "it-strategic-goal.schema.json",
    "choices": "strategic-choice.schema.json",
    "principles": "principle.schema.json",
    "transformations": "transformation.schema.json",
    "roadmap": "roadmap-item.schema.json",
    "source_gaps": "source-gap.schema.json",
}

errors = []
for collection, schema_name in schema_map.items():
    schema = json.loads((SCHEMAS / schema_name).read_text(encoding="utf-8"))
    validator = Draft202012Validator(schema)
    for idx, item in enumerate(data[collection]):
        for err in validator.iter_errors(item):
            errors.append(f"{collection}[{idx}] {err.message}")

status_schema = json.loads((SCHEMAS / "strategy-status.schema.json").read_text(encoding="utf-8"))
for err in Draft202012Validator(status_schema).iter_errors(data["status"]):
    errors.append(f"status {err.message}")

ids = {}
for key in ["sources", "evidence", "drivers", "issues", "goals", "choices", "principles", "transformations", "roadmap", "source_gaps"]:
    ids[key] = {x["id"] for x in data[key]}

for ev in data["evidence"]:
    if not set(ev["source_ids"]).issubset(ids["sources"]):
        errors.append(f"{ev['id']} references unknown source")
for dr in data["drivers"]:
    if not set(dr["evidence_ids"]).issubset(ids["evidence"]):
        errors.append(f"{dr['id']} references unknown evidence")
for issue in data["issues"]:
    if not set(issue["evidence_ids"]).issubset(ids["evidence"]):
        errors.append(f"{issue['id']} references unknown evidence")
    if issue.get("driver_ids") and not set(issue["driver_ids"]).issubset(ids["drivers"]):
        errors.append(f"{issue['id']} references unknown driver")
for goal in data["goals"]:
    if not set(goal["strategic_issue_ids"]).issubset(ids["issues"]):
        errors.append(f"{goal['id']} references unknown strategic issue")
    if not set(goal["evidence_ids"]).issubset(ids["evidence"]):
        errors.append(f"{goal['id']} references unknown evidence")
    if goal["solution_neutral"] is not True:
        errors.append(f"{goal['id']} is not solution neutral")
for choice in data["choices"]:
    if not set(choice["goal_ids"]).issubset(ids["goals"]):
        errors.append(f"{choice['id']} references unknown goal")
    if len(choice["alternatives"]) < 2:
        errors.append(f"{choice['id']} lacks alternatives")
    if choice["product_neutral"] is not True:
        errors.append(f"{choice['id']} is not product neutral")
for tr in data["transformations"]:
    if not set(tr["goal_ids"]).issubset(ids["goals"]):
        errors.append(f"{tr['id']} references unknown goal")
    if tr["project_level_detail"] is not False:
        errors.append(f"{tr['id']} contains project-level detail")
for rm in data["roadmap"]:
    if not set(rm["goal_ids"]).issubset(ids["goals"]):
        errors.append(f"{rm['id']} references unknown goal")
    if rm.get("transformation_ids") and not set(rm["transformation_ids"]).issubset(ids["transformations"]):
        errors.append(f"{rm['id']} references unknown transformation")
    if rm.get("depends_on") and not set(rm["depends_on"]).issubset(ids["roadmap"]):
        errors.append(f"{rm['id']} references unknown roadmap dependency")

if set(data["status"]["open_source_gap_ids"]) - ids["source_gaps"]:
    errors.append("status references unknown source gap")

if len(data["sources"]) < 4 or len(data["goals"]) < 2 or len(data["transformations"]) < 2:
    errors.append("scenario is too small to be an end-to-end fixture")

if errors:
    print("END-TO-END: FAIL")
    for e in errors:
        print(" -", e)
    raise SystemExit(1)

print("END-TO-END: PASS")
print(f"sources={len(data['sources'])}, evidence={len(data['evidence'])}, issues={len(data['issues'])}, goals={len(data['goals'])}, choices={len(data['choices'])}, transformations={len(data['transformations'])}, roadmap={len(data['roadmap'])}")
