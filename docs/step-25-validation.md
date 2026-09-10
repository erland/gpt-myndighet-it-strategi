# Steg 25 – validering

**Resultat:** PASS

- Chat ZIP-instruktionen är byte-identisk med canonical instruktion.
- Custom GPT-instruktionen håller sig inom 8 000 tecken.
- 24/24 kritiska beteendekontraktsgrupper verifieras i Custom GPT-kompileringen.
- Knowledge-paritet: 7/7 filer, byte-identiska mellan Chat och Custom GPT.
- Web browsing är aktiverat och markerat som required i Custom GPT-konfigurationen.
- Data analysis är aktiverat/rekommenderat.
- Actions krävs inte.
- Accepterade plattformsskillnader är dokumenterade i `docs/runtime-parity-report.md`.
- Blockerande runtime-avvikelser: 0.

## Kvar för steg 26

Project hygiene och dokumentationsgranskning över hela projektet.
