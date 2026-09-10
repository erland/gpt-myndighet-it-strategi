# Steg 22 – validering

**Resultat:** PASS

## Leveranser

- `tests/end-to-end/scenario-tullverket.json` – komplett strukturerat scenario.
- `tests/end-to-end/reference-output.md` – exempel på full strategisk syntes och ledningsversion.
- `tests/end-to-end/README.md` – scenariobeskrivning och avgränsningar.
- `scripts/run-end-to-end-tests.py` – schema- och spårbarhetsvalidator.

## Kontroller

- Verklig svensk myndighet och offentliga källor används.
- Källa → evidens → drivkraft → strategisk fråga → mål → vägval → förflyttning → färdplan är sammanhängande.
- Samtliga strukturerade objekt passerar sina JSON Schemas.
- Strategiska mål och vägval är lösnings-/produktneutrala.
- Alternativanalys finns för vägval.
- Materiell informationslucka om intern arkitektur/systemportfölj finns kvar och begränsar slutsatsstyrkan.
- Slutsyntes och ledningsversion introducerar inte produktspecifika rekommendationer.

**Steg 22:** PASS.
