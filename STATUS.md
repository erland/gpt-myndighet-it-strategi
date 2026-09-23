# STATUS – IT-strategen för myndigheter

## Aktuell status

**PÅGÅR – migrering till GPT Byggaren 1.5.0, steg 35.**

Den stabila domänversionen **0.1.0** är fortsatt baslinje. Steg 33–34 är verifierade utan regression i research-, härlednings- eller end-to-end-flödet.

## Verifierat i steg 34

- Custom GPT innehåller nu `Operativ kärna` och `Auktoritativ status`
- Custom GPT-instruktion: **7 990 / 8 000 tecken**
- befintliga semantiska kontraktsmarkörer bevarade
- Chat och Custom GPT har explicita 1.5-runtime-kontrakt
- buildscript kräver runtime-kontrakten
- parity-test blockerar om den nya 1.5-kärnan tappas
- full CI-kedja: PASS

## Nästa rekommenderade steg

**35 – Generaliserad runtime parity och release readiness.**

Alla fem registrerade runtimes ska bedömas i 1.5-paritetsmodellen. Chat och Custom GPT är aktiva; Claude Projects, OpenCode och OpenAI Plugin ska fortsatt vara explicit bedömda och inte aktiveras utan verifierad research- och källparitet.
