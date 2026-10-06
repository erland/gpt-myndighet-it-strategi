# OpenAI Plugin runtime

IT-strategen för myndigheter distribueras som en skills-first peer-runtime enligt GPT Byggaren 1.5.1.

## Hostberoenden

Fullt research- och statebeteende kräver:

- aktuell webbresearch,
- läsbar filyta/workspace,
- skrivbar filyta för persistent status och artefakter,
- persistent state.

Code execution är valfri och används vid behov för deterministisk analys av strukturerade data. Pluginen paketerar inga runtime-skript och genererar ingen MCP-wrapper.

## State

`project-status.yaml` i arbetsytan är auktoritativ status när den finns. Chattminne är inte fallback för persistent projektstatus.

## Fallbacks

- Utan webbförmåga får pluginen arbeta med explicit tillgängligt material, men får inte påstå att aktuell offentlig styrning eller omvärld har verifierats.
- Utan persistent state får ett avgränsat analyssteg genomföras, men robust resume eller statusuppdatering får inte påstås.
- Utan filskrivning får persistent strategi-/projektartefakter inte påstås vara skapade.

## Paket

Pluginpaketet innehåller canonical beteende, Knowledge, operational policy och relevanta JSON Schemas som references. Projektets Python-skript är build/test-infrastruktur och ingår inte i runtimepaketet.
