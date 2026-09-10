# Schemas och strukturerade arbetsartefakter

Dessa JSON Schema-filer formaliserar GPT:ns interna analysobjekt. De är arbetskontrakt för konsekvent struktur och spårbarhet; de är inte ett krav på att varje användarsvar ska exponera rå JSON.

## Scheman

| Fil | Objekt |
|---|---|
| `source-inventory.schema.json` | Inventerad källa och källvärdering |
| `evidence-item.schema.json` | Evidenspost med observation, källor och inferensstyrka |
| `strategic-driver.schema.json` | Strategisk drivkraft |
| `strategic-issue.schema.json` | Strategisk IT-fråga/gap/risk/möjlighet/beroende |
| `it-strategic-goal.schema.json` | IT-strategiskt mål |
| `strategic-choice.schema.json` | Vägval med alternativ och trade-offs |
| `principle.schema.json` | Strategisk princip |
| `transformation.schema.json` | Prioriterad strategisk förflyttning |
| `roadmap-item.schema.json` | Strategisk färdplanspost och indikatorer |
| `source-gap.schema.json` | Informationslucka |
| `strategy-status.schema.json` | Runtime-status och fasgrindar |

## Gemensamma designregler

- ID:n är stabila inom en strategianalys och används för länkar mellan objekt.
- Spårbarhet ska gå från källa/evidens till strategisk fråga, mål, vägval, förflyttning och färdplan.
- `solution_neutral`, `product_neutral` och `project_level_detail` används som maskinvaliderbara guardrails där de passar.
- Scheman tillåter inte godtyckliga extra fält (`additionalProperties: false`) för att upptäcka strukturdrift.
- Saknade baslinjer representeras som `to_be_established`; de får inte fabriceras.
- Scheman beskriver intern struktur. Slutrapport och ledningsversion ska fortfarande vara läsbar svensk prosa.

## Validering

I steg 19 kontrolleras att alla scheman är giltiga Draft 2020-12-scheman och att ett sammanhängande minimiscenario kan valideras mot kärnobjekten. Mer omfattande research- och härledningstester byggs i steg 20–22.
