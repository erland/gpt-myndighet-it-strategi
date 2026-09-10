#!/usr/bin/env python3
from pathlib import Path
import json, sys
try:
    from jsonschema import Draft202012Validator
except Exception as e:
    print(f"ERROR: jsonschema unavailable: {e}")
    sys.exit(2)
root=Path(__file__).resolve().parents[1]
schema_dir=root/'schemas'
files=sorted(schema_dir.glob('*.schema.json'))
errors=[]
for path in files:
    try:
        obj=json.loads(path.read_text(encoding='utf-8'))
        Draft202012Validator.check_schema(obj)
    except Exception as e:
        errors.append(f"{path.name}: {e}")
print(f"Schemas checked: {len(files)}")
if errors:
    for e in errors: print('ERROR:',e)
    sys.exit(1)
print('PASS: all schemas are valid Draft 2020-12 schemas')
