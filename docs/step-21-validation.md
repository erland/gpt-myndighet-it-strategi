# Steg 21 – validering

## Omfattning

Steg 21 etablerar kontraktstester för strategisk härledning från evidens till mål, vägval och förflyttningar.

## Leveranser

- `tests/strategic-derivation/cases.json`
- `tests/strategic-derivation/README.md`
- `scripts/run-strategic-derivation-tests.py`
- uppdaterad testöversikt och projektstatus

## Scenarier

1. Irrelevant IT-trend väljs bort.
2. Verksamhetsbehov kan härledas till lösningsneutralt IT-strategiskt mål.
3. Specifik produkt rekommenderas inte utan separat evidens/analys.
4. Mål blandas inte ihop med initiativ eller teknisk lösning.
5. Observation kan följas genom en komplett spårbarhetskedja till vägval.
6. Osäkerhet i nuläget förs vidare och sänker slutsatsens säkerhet.
7. Symptom konsolideras till bakomliggande strategiskt gap.
8. Större vägval kräver meningsfull alternativ- och trade-off-analys.
9. Befintliga initiativ återuppfinns inte; kvarstående gap identifieras.
10. Kapacitetsbegränsningar får påverka omfattning, sekvensering eller tidshorisont.

## Resultat

- Strategic derivation test suite: **PASS, 10/10 scenarier**.
- JSON Schema validation: **PASS, 11/11 schemas**.
- Steg 21-validering: **PASS**.
