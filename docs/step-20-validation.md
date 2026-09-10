# Steg 20 – validering

## Omfattning

Steg 20 etablerar tester för research och källhantering.

## Leveranser

- `tests/research-source-handling/cases.json`
- `tests/research-source-handling/README.md`
- `scripts/run-research-source-tests.py`
- uppdaterad testöversikt och projektstatus

## Scenarier

1. Väl dokumenterad större myndighet.
2. Mindre myndighet med få offentliga dokument.
3. Motstridiga källor.
4. Äldre strategi kontra nyare bindande styrning.
5. Saknat budgetunderlag.
6. Osäker tredjeparts-/leverantörskälla.
7. Snabbt föränderlig IT-trend.

## Kontroller

- källauktoritet och aktualitet behandlas separat,
- nyare källa antas inte automatiskt vara starkare,
- bindande aktuell styrning kan övertrumfa äldre intern riktning,
- informationsluckor registreras och påverkar säkerheten,
- icke-blockerande luckor tillåter best effort,
- konflikter klassificeras och bevaras om de inte kan lösas,
- strategiskt viktiga påståenden trianguleras när rimligt,
- tredjeparts- och trendkällor får inte ensamma skapa myndighetsspecifika strategiska mål.

## Resultat

- Research/source test suite: PASS, 7/7 obligatoriska scenarier finns.
- JSON Schema validation: PASS, 11/11 schemas giltiga.
- Steg 20-validering: PASS.
