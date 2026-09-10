# IT-strategen för myndigheter – Chat ZIP

Detta är den portabla Chat-runtime-distributionen för **IT-strategen för myndigheter**.

## Användning

1. Bifoga denna ZIP i en ny ChatGPT-konversation.
2. Skriv exempelvis: **”Använd denna zip som GPT i den här konversationen.”**
3. Ange därefter vilken svensk myndighet IT-strategin ska tas fram för.

GPT:n arbetar stegvis från källinventering och myndighetsanalys till strategiska mål, vägval, förflyttningar, färdplan, fullständig IT-strategi och ledningsversion.

## Runtime-principer

- `assistant/instructions.md` är den canonical runtime-instruktion som styr beteendet.
- `knowledge/` innehåller tidsneutral metod- och domänkunskap. Kritiska regler kräver inte att knowledge-filer läses först.
- `schemas/` innehåller strukturerade arbetskontrakt för spårbar analys.
- Aktuell myndighetsinformation och IT-omvärld ska hämtas och verifieras vid runtime; den är inte hårdkodad i paketet.
- Myndighetsspecifik evidens väger tyngre än generell IT-trendinformation.

## Viktiga delar

- `assistant/instructions.md` – komplett runtime-instruktion
- `assistant/policies/runtime-boundary.md` – portabilitets- och kunskapsgräns
- `knowledge/` – metod- och domänstöd
- `schemas/` – JSON Schema-kontrakt
- `runtime-manifest.yaml` – maskinläsbar runtime-beskrivning
- `VERSION` – distributionsversion

## Version

0.1.0-dev

## Entry point

Detta dokument är den mänskliga entrypointen. `runtime-manifest.yaml` beskriver den maskinläsbara strukturen.
