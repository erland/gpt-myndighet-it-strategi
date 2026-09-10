# IT-strategen för myndigheter – Custom GPT

Detta paket innehåller den Custom GPT-optimerade distributionen.

## Konfigurera

1. Skapa en Custom GPT.
2. Använd namn, beskrivning och conversation starters från `custom-gpt-config.yaml`.
3. Klistra in `instructions.md` i GPT:ns instruktioner.
4. Ladda upp samtliga sju filer i `knowledge/` som Knowledge.
5. Aktivera web browsing och data analysis. Filuppladdningar bör vara möjliga för kompletterande myndighetsunderlag.
6. Image generation och Actions krävs inte.

## Viktigt

`instructions.md` är en kompilerad runtime-version av projektets canonical instruktion och ska inte redigeras separat. Ändringar görs i canonical källan och kompileras om. Knowledge är tidsneutral metodfördjupning; aktuell myndighetsinformation och IT-omvärld ska verifieras vid runtime.
