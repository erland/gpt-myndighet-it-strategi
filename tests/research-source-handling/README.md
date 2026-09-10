# Tester – research och källhantering

Detta testpaket verifierar metodkontraktet för steg 20. Testerna är avsiktligt teknikoberoende: de beskriver vilket beteende en runtime/eval ska kräva, medan `scripts/run-research-source-tests.py` kontrollerar att testsviten själv är komplett och konsistent med källmodellen.

## Testfall

1. `RS01_WELL_DOCUMENTED_AGENCY` – väl dokumenterad större myndighet.
2. `RS02_SMALL_AGENCY_FEW_DOCUMENTS` – mindre myndighet med få offentliga dokument.
3. `RS03_CONFLICTING_SOURCES` – motstridiga källor.
4. `RS04_OLD_STRATEGY_NEW_STEERING` – äldre strategi kontra nyare regleringsbrev.
5. `RS05_MISSING_BUDGET_BASIS` – saknat budgetunderlag.
6. `RS06_WEAK_THIRD_PARTY_SOURCE` – osäker tredjepartskälla.
7. `RS07_FAST_MOVING_IT_TREND` – snabbt föränderlig IT-trend.

## Passkriterier

Testsviten ska säkerställa att GPT:n:

- prioriterar formell och myndighetsspecifik evidens korrekt,
- inte använder aktualitet som enda rangordningsregel,
- registrerar materiella informationsluckor,
- fortsätter best effort när luckan inte är blockerande,
- klassificerar och redovisar olösta källkonflikter,
- triangulerar strategiskt viktiga slutsatser när rimligt,
- behandlar leverantörs- och branschkällor som kompletterande,
- använder aktuella källor för snabbt föränderliga IT-frågor,
- aldrig låter en trend ensam skapa ett myndighetsspecifikt strategiskt mål eller vägval.

## Runtime-eval senare

I steg 22 kan dessa scenarier användas som grund för verkliga end-to-end-evals mot en faktisk myndighet. Steg 20 testar själva research- och källhanteringskontraktet, inte webbsökningens kvalitet hos en enskild runtime.
