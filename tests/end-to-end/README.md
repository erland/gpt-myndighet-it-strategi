# End-to-end-scenario – Tullverket

Detta scenario verifierar hela arbetsflödet med en verklig svensk myndighet och verkliga offentliga källor. Det är ett **regressionstest och referensexempel**, inte en beslutad eller komplett IT-strategi för Tullverket.

Scenariot använder offentliga källor för att bygga en sammanhängande spårbarhetskedja:

`source → evidence → driver → strategic issue → goal → choice/principle → transformation → roadmap`

## Viktiga testegenskaper

- Bindande instruktion används som uppdragsankare.
- Årsredovisning och budgetunderlag används för nuläge, utvecklingsbehov och kapacitet.
- Aktuell regeländring används för att verifiera förändringstryck.
- Strategiska mål och vägval hålls produktneutrala.
- Ett materiellt informationsgap om intern arkitektur/systemportfölj bevaras i slutläget.
- Färdplanen använder horisonter och beroenden snarare än fabricerade kalenderdatum.

Kör:

```bash
python3 scripts/run-end-to-end-tests.py
```
