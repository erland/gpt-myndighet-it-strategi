# Release notes – 0.1.0-rc.1

## Sammanfattning

Detta är den första release candidate-versionen av **IT-strategen för myndigheter**. Den är avsedd för praktisk pilotprovning på svenska myndigheter och omfattar hela arbetsflödet från myndighetsidentifiering och källinventering till fullständig IT-strategi och ledningsversion.

## Ingår i RC:n

- research-heavy arbetsflöde i 15 faser
- källmodell och källhierarki för offentlig myndighetsinformation
- evidens- och spårbarhetsmodell
- analys av uppdrag, styrning, mål, ekonomi, kapacitet, nuläge och förändringstryck
- selektiv IT-omvärldsanalys
- strategiska IT-utmaningar, mål, vägval, principer och förflyttningar
- konsekvensanalys, färdplan och uppföljning
- fullständig slutrapport och ledningsversion
- 11 JSON Schema-kontrakt
- 7 research-/källtestfall
- 10 strategiska härledningstestfall
- end-to-end-referensscenario för Tullverket
- Chat ZIP-distribution
- Custom GPT-distribution
- runtime-paritetskontroll
- GitHub Actions CI och automatiserad release-build

## Kvalitetsstatus

Inför RC:n passerar projektet release-readiness-grinden utan blockerande fel eller kända validatorvarningar. RC-builden använder release-taggen som versionskälla och producerar projekt-, Chat- och Custom GPT-artefakter med SHA-256-checksummor.

## Pilotfokus

RC:n bör framför allt provas på flera myndighetstyper för att bedöma:

- om resultatet blir tillräckligt myndighetsspecifikt
- om källinventeringen hittar och prioriterar rätt offentliga underlag
- om mål och vägval blir strategiska snarare än teknikdrivna
- om omfattningen på slutrapporten är praktiskt användbar
- om arbetssättet fungerar även när offentligt nulägesunderlag är begränsat

## Nästa steg

Efter RC följer pilotgranskning och justering enligt utvecklingsplanens steg 31.
