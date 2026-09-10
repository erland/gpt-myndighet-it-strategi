# Chat ZIP

Den portabla Chat-runtime-distributionen byggs från projektets canonical instruktion och tidsneutrala Knowledge.

## Struktur

Källan för paketet finns under `distributions/chat/runtime/` och innehåller:

- `START-HERE.md`
- `assistant/instructions.md`
- `assistant/policies/runtime-boundary.md`
- `knowledge/`
- `schemas/`
- `runtime-manifest.yaml`
- `VERSION`

## Bygg

Kör:

```bash
python3 scripts/build-chat-zip.py
```

Standardartefakt: `dist/it-strategen-myndigheter-chat-<version>.zip`.
