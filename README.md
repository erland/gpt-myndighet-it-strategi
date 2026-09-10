# IT-strategen för myndigheter

GPT-projekt för att ta fram **källspårbara och myndighetsanpassade IT-strategier för svenska myndigheter**. Strategin härleds stegvis från formell styrning, verksamhetsmål, ekonomiska förutsättningar, dokumenterat nuläge och förändringstryck. Aktuell IT-omvärld används som kompletterande underlag och får inte ensam styra myndighetsspecifika rekommendationer.

## Projektprofil

`workflow_research_heavy`

## Canonical beteende

`src/instructions/system.md` är projektets canonical runtime-kontrakt. Kritiska beteenden ligger där och är inte beroende av att Knowledge-filer läses. Fördjupande och tidsneutral metodkunskap finns i `knowledge/`.

Den strategiska huvudkedjan är:

**styrning och uppdrag → verksamhetsmål → evidens och nuläge → förändringstryck → strategiska IT-frågor → mål → vägval och principer → förflyttningar → konsekvenser → färdplan och uppföljning**

## Distributioner

Projektet har två verifierade runtime-format från samma canonical kontrakt:

- **Chat ZIP** – full canonical instruktion, Knowledge och JSON Schemas.
- **Custom GPT** – kompilerad instruktion och kuraterad Knowledge inom plattformsgränserna.

Runtime-pariteten är verifierad utan blockerande avvikelser. Källorna för distributionerna finns under `distributions/`; genererade ZIP-filer byggs med skripten i `scripts/` och ska inte lagras i projektets `dist/`.

## Tester och validering

Projektet innehåller:

- 11 JSON Schemas för strukturerade arbetsartefakter,
- 7 research- och källhanteringsscenarier,
- 15 strategiska härledningstester,
- ett komplett end-to-end-referensscenario för Tullverket,
- runtime-paritetsvalidering mellan Chat ZIP och Custom GPT.

Kör relevanta validatorer från projektroten, exempelvis:

```bash
python3 scripts/validate-schemas.py
python3 scripts/run-research-source-tests.py
python3 scripts/run-strategic-derivation-tests.py
python3 scripts/run-end-to-end-tests.py
python3 scripts/validate-runtime-parity.py
```


## Continuous integration

`.github/workflows/ci.yml` kör projektlint, schemas, research-/källtester, strategisk härledning, end-to-end, runtime-paritet och source hygiene. Därefter byggs Chat ZIP och Custom GPT ZIP, vars CRC och SHA-256 verifieras innan de laddas upp som GitHub Actions-artifacts. Samma validatorer och build-skript kan köras lokalt.

## Build

```bash
python3 scripts/build-chat-zip.py
python3 scripts/build-custom-gpt.py
```

Byggartefakter skapas under `dist/`, som är genererad och ignorerad.

## Utvecklingsstatus

**Steg 1–32 är klara. Version 0.1.0 är stabil release.** Pilotgranskningen från `0.1.0-rc.2` är införlivad och hela kvalitetsgrinden passerar utan blockerande fel eller varningar. Se:

- `project-status.yaml` för maskinläsbar status,
- `STATUS.md` för kort mänsklig status,
- `docs/stable-release-report-0.1.0.md` för stabil releasegrind,
- `docs/development-plan.md` för hela planen.

**Nästa utvecklingsområde:** 0.2.x, baserat på verklig användningsfeedback och eventuell rapportexport.

## Release-build

GitHub Release-workflowet i `.github/workflows/release.yml` använder release-taggen som versionskälla och kör `scripts/build-release.py`. Det producerar projekt-ZIP, Chat ZIP, Custom GPT ZIP, individuella `.sha256`-filer och `SHA256SUMS.txt`. Vid en publicerad GitHub Release bifogas artefakterna automatiskt till releasen. Workflowet kan även köras manuellt för en befintlig tagg.


## Stabil release

Första stabila versionen är **0.1.0**, byggd från den pilotjusterade kandidaten **0.1.0-rc.2**. Se `docs/release-notes-0.1.0.md`, `docs/stable-release-report-0.1.0.md` och `distributions/custom-gpt/runtime/compatibility.md`.

## Pilotgranskning steg 31

RC-metoden är pilotgranskad mot fyra olika myndighetstyper. Riktade guardrails för mognadsanpassning, relativ researchmättnad, teknikrollseparation och offentlig evidensgräns har införts. Se `docs/pilot-review-step-31.md`.
