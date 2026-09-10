# Scripts

Reproducerbara build- och valideringsskript för projektet. Kör dem från projektroten.

## Validering

- `validate-schemas.py` – validerar projektets 11 JSON Schemas och minimala spårbarhetsexempel.
- `run-research-source-tests.py` – verifierar 7 kontraktsscenarier för research och källhantering.
- `run-strategic-derivation-tests.py` – verifierar 10 scenarier för strategisk härledning och guardrails.
- `run-end-to-end-tests.py` – validerar end-to-end-scenariot och referensintegritet genom strategikedjan.
- `validate-runtime-parity.py` – jämför Chat ZIP- och Custom GPT-runtime mot canonical beteende och Knowledge.

## Build

- `build-chat-zip.py` – bygger portabel Chat ZIP under `dist/`.
- `build-custom-gpt.py` – bygger Custom GPT-distribution under `dist/`.

`dist/` är genererad, ignorerad och ska inte följa med källprojektets ZIP.

## CI-stöd

- `validate-project.py` – lätt projektlint: obligatoriska filer, YAML/JSON, Python-syntax, UTF-8 och trailing whitespace.
- `validate-hygiene.py` – verifierar att genererade build-, cache-, OS- och temporärfiler inte ligger i källträdet.
- `../requirements-ci.txt` – minimala Python-beroenden för CI (`jsonschema`, `PyYAML`).

GitHub Actions kör samma skript som lokalt används för validering och build. Workflowet finns i `.github/workflows/ci.yml`.

- `build-release.py` – bygger en komplett versionssatt release från `--tag`/`GITHUB_REF_NAME`, validerar en staged kopia och skapar projekt-, Chat- och Custom GPT-ZIP samt checksummor under `release-dist/`.
