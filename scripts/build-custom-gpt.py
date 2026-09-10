#!/usr/bin/env python3
from pathlib import Path
import zipfile, hashlib
ROOT=Path(__file__).resolve().parents[1]
VERSION=(ROOT/'VERSION').read_text(encoding='utf-8').strip()
RUNTIME=ROOT/'distributions/custom-gpt/runtime'
OUT=ROOT/'dist'/f'it-strategen-myndigheter-custom-gpt-{VERSION}.zip'
OUT.parent.mkdir(exist_ok=True)
required=['README.md','instructions.md','custom-gpt-config.yaml','compatibility.md','VERSION']
for f in required:
    if not (RUNTIME/f).exists(): raise SystemExit(f'Missing {f}')
instr=(RUNTIME/'instructions.md').read_text(encoding='utf-8')
if len(instr)>8000: raise SystemExit(f'Instructions exceed 8000 characters: {len(instr)}')
knowledge=list((RUNTIME/'knowledge').glob('*'))
if len([p for p in knowledge if p.is_file()])>20: raise SystemExit('Knowledge exceeds 20 files')
with zipfile.ZipFile(OUT,'w',zipfile.ZIP_DEFLATED) as z:
    for p in sorted(RUNTIME.rglob('*')):
        if p.is_file(): z.write(p,p.relative_to(RUNTIME))
h=hashlib.sha256(OUT.read_bytes()).hexdigest()
sha=OUT.with_suffix(OUT.suffix+'.sha256')
sha.write_text(f'{h}  {OUT.name}\n',encoding='utf-8')
print(OUT)
print(f'instruction_chars={len(instr)} knowledge_files={len([p for p in knowledge if p.is_file()])}')
print(h)
