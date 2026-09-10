# PROJECT – IT-strategen för myndigheter

## Syfte

Skapa en GPT som kan ta fram en IT-strategi för den svenska myndighet som användaren anger.

## Målbild

GPT:n ska självständigt samla in, värdera och analysera offentligt tillgänglig information om myndigheten och kombinera detta med aktuell och relevant IT-omvärldsanalys. Slutresultatet ska vara en spårbar IT-strategi som härleds från myndighetens faktiska uppdrag, styrning, mål, ekonomi, nuläge och förändringstryck.

## Grundläggande analyskedja

Uppdrag och styrning → verksamhetsmål → förändringstryck → nuläge/problem → strategiska IT-behov → IT-strategiska mål → strategiska vägval → principer → prioriterade förflyttningar → färdplan och uppföljning.

## Centrala källgrupper

1. Formell styrning: instruktion, regleringsbrev, regeringsuppdrag och relevanta bindande krav.
2. Myndighetens strategiska information: mål, vision, strategier, planer, budgetunderlag, årsredovisningar, organisation och arbetsordning.
3. Nuläge och förändringsbehov: program, upphandlingar, revisioner, tillsyn, samverkan, kompetens- och moderniseringsbehov.
4. Extern styrning och beroenden: EU, nationella initiativ samt relevanta myndigheter och samverkansorgan.
5. IT-omvärld: bland annat AI, cybersäkerhet, moln/plattformar, data, interoperabilitet, automation, legacy, kompetens, sourcing och digital suveränitet.

## Evidensprincip

Myndighetsspecifik och formell evidens väger tyngre än generell IT-trendinformation. Strategiska rekommendationer ska så långt möjligt följa kedjan:

Observation → källa → betydelse → strategisk konsekvens → rekommendation.

Fakta, analys, rekommendation, antagande och informationslucka ska hållas åtskilda.

## Avgränsning

GPT:n tar i första hand fram strategisk inriktning. Den ska inte utan särskild analys välja specifika produkter, plattformar eller detaljlösningar. AI, moln, zero trust eller andra aktuella teknikområden får inte automatiskt bli strategiska mål.

## Distributioner

- Chat ZIP
- Custom GPT
- Projekt-ZIP

Alla distributioner ska härledas från samma canonical beteendekontrakt.


## Runtime-paritet

Chat ZIP och Custom GPT ska ha samma strategiska beslutslogik trots olika distributionsformat. Steg 25 verifierar detta genom beteendekontrakt, Knowledge-paritet och capability-kontroller. Accepterade plattformsskillnader dokumenteras i `docs/runtime-parity-report.md`; blockerande beteendedrift är inte tillåten.


## Steg 26 – Project hygiene och dokumentationsgranskning

**Status:** Klar

- Full hygiene-granskning genomförd och dokumenterad i `docs/project-hygiene-report.md`.
- Genererad `dist/` borttagen ur källprojektet; Chat- och Custom GPT-artefakter byggs reproducerbart och levereras separat.
- Temporära/cache-/OS-filer kontrollerade och frånvarande.
- README, PROJECT, STATUS, `gpt-project.yaml`, `project-status.yaml` och scripts-dokumentation synkroniserade.
- Test-, revisions- och runtime-källfiler behållna eftersom de har tydliga reproducerbarhets- och spårbarhetsroller.
- Project hygiene: PASS.

## Steg 27 – GitHub Actions CI

**Status:** Klar

- CI-workflow finns i `.github/workflows/ci.yml`.
- Workflowet kör project lint, schemas, samtliga testsviter, runtime-paritet och source hygiene.
- Chat ZIP och Custom GPT ZIP byggs från källträdet och integritetskontrolleras.
- Runtime-artefakter publiceras som GitHub Actions-artifacts.
- Workflowet använder endast minimala Python-beroenden från `requirements-ci.txt` och kan reproduceras lokalt med samma scripts.

## Steg 28 – GitHub Release-build

**Status:** Klar

- Release-versionen kommer från GitHub Release-taggen.
- Projekt-, Chat- och Custom GPT-ZIP byggs i staged kopia.
- SHA-256-checksummor skapas och verifieras.

## Steg 29 – Release readiness

**Status:** Klar

- Samlad kvalitetsgrind dokumenterad i `docs/release-readiness-report.md`.
- Full test- och runtime-validering passerar.
- RC-simulering med `v0.1.0-rc.1` passerar.
- Blockerande fel: 0.
- Varningar: 0.

## Nästa rekommenderade steg

Den ursprungliga 32-stegsplanen är slutförd. Nästa utvecklingsområde är **0.2.x – verklig användningsutvärdering och rapportexport**, styrt av feedback från praktisk användning.
## Aktuell releasefas

Version **0.1.0** är stabil release. Den bygger på den pilotjusterade kandidaten **0.1.0-rc.2** och har passerat full stabil releasegrind.
## Pilotgranskning

Steg 31 har verifierat metoden mot Skatteverket, Mediemyndigheten, Läkemedelsverket och Polismyndigheten. Se `docs/pilot-review-step-31.md`. Projektet är därefter redo för stabil release efter full regression.


## Steg 32 – Stabil release

**Status:** Klar

- Version `0.1.0` är första stabila release.
- Alla 32 planerade steg är slutförda.
- Full regression, runtime-paritet, hygiene och releaseartefaktintegritet passerar.
- Stable release-dokumentation finns i `docs/stable-release-report-0.1.0.md` och `docs/release-notes-0.1.0.md`.
