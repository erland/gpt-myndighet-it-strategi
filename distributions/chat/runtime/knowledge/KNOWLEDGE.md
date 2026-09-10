# Knowledge-arkitektur

Den här katalogen innehåller **stabil, tidsneutral metod- och domänkunskap** som fördjupar GPT:ns analys. Kritiska runtime-regler finns alltid i `src/instructions/system.md` och får inte vara beroende av att någon knowledge-fil läses.

## Principer

- Knowledge förklarar **hur man tänker**, inte vad dagens läge råkar vara.
- Tidskänsliga fakta, aktuella regleringsbrev, årsredovisningar, budgetunderlag, tekniktrender och myndighetsspecifika sakuppgifter ska hämtas och verifieras i den aktuella analysen.
- Knowledge får innehålla stabila begrepp, analysramar, kvalitetskriterier, exempel och kontrollfrågor.
- Vid konflikt gäller canonical runtime-instruktionen före Knowledge.
- Knowledge ska kunna uppdateras fil för fil utan att kärnflödet ändras.

## Filer

- `it-strategy-method.md` – metod för att härleda en IT-strategi från uppdrag, behov och evidens.
- `swedish-agency-governance.md` – orientering om svensk myndighetsstyrning och hur olika styrsignaler bör förstås.
- `source-evaluation.md` – metodstöd för källvärdering, aktualitet, konflikt och triangulering.
- `strategic-goals-and-choices.md` – stöd för mål, vägval, principer och strategiska förflyttningar.
- `environment-analysis.md` – metod för selektiv IT-omvärldsanalys.
- `report-quality.md` – struktur- och kvalitetskriterier för fullrapport och ledningsversion.

## Runtime-gräns

Följande ska **inte** flyttas från canonical instruktion hit: identitet, arbetsflöde, fasgrindar, källprioritering, evidenskrav, lösningsneutralitet, blockeringsregler, nästa-steg-beteende eller obligatoriska kvalitetsgrindar.
