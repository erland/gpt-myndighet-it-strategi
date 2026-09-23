# Utvecklingsplan – IT-strategi för myndigheter

## Projektöversikt

**Arbetsnamn:** IT-strategen för myndigheter
**Projektprofil:** `workflow_research_heavy`
**Mål:** Skapa en GPT som utifrån en vald svensk myndighet samlar in, värderar och analyserar offentlig information samt tar fram en källspårbar och myndighetsanpassad IT-strategi.

GPT:n ska normalt byggas för både **Chat ZIP** och **Custom GPT** från samma canonical instruktion.

## Grundprinciper

- Myndighetsspecifik evidens väger tyngre än generella IT-trender.
- Formell styrning väger tyngre än informella eller sekundära källor.
- Fakta, analys och rekommendation ska hållas tydligt åtskilda.
- Strategiska rekommendationer ska kunna härledas till identifierade behov.
- GPT:n ska uttryckligen redovisa osäkerhet och informationsluckor.
- Aktuella modeord eller tekniker ska inte automatiskt bli strategiska mål.
- Slutprodukten ska vara en IT-strategi, inte en teknisk målarkitektur eller produktlista.
- Webbresearch ska vara en integrerad del av huvudflödet.
- Källor ska vara aktuella, relevanta och spårbara.

---

## Steg 1 – Skapa projektgrund

### Mål
Skapa den första kompletta projektstrukturen och etablera canonical projektmetadata.

### Leveranser
- `README.md`
- `gpt-project.yaml`
- `PROJECT.md`
- `STATUS.md`
- `project-status.yaml`
- `docs/development-plan.md`
- grundstruktur för canonical instruktion, knowledge, schemas, tester, scripts och distributioner
- första kompletta projekt-ZIP

### Validering
- Projektstrukturen följer GPT Byggarens standard.
- Projektprofilen är `workflow_research_heavy`.
- Både Chat ZIP och Custom GPT är definierade som distributionsmål.

### Klart när
- Projektet kan återupptas enbart från projekt-ZIP:en.
- Utvecklingsplanen finns i projektet.
- Projektstatus pekar ut steg 2 som nästa planerade steg.
- En komplett projekt-ZIP kan byggas.

---

## Steg 2 – Definiera användarflöde och strategiprocess

### Mål
Formalisera hur GPT:n går från myndighetsnamn till färdig IT-strategi.

### Leveranser
- canonical workflow för:
  - identifiering av myndighet
  - källinventering
  - analys av uppdrag och styrning
  - analys av mål och strategisk riktning
  - ekonomisk analys
  - nuläges- och förändringstrycksanalys
  - IT-omvärldsanalys
  - identifiering av strategiska IT-frågor
  - formulering av mål
  - vägval och principer
  - prioriterade förflyttningar
  - konsekvensanalys
  - färdplan
  - uppföljning
  - slutlig kvalitetssäkring
  - framtagning av fullständig strategi och ledningsversion

### Validering
- Flödet bygger inte strategin innan underlaget analyserats.
- Det går att fortsätta stegvis med kommandon som “fortsätt” eller “gör nästa steg”.
- GPT:n kan redovisa aktuell fas och vad som återstår.

### Klart när
- Arbetsflödet är entydigt definierat.
- Varje fas har tydliga in- och utdata.
- Nästa steg kan rekommenderas utifrån faktisk status.

---

## Steg 3 – Definiera källmodell och källhierarki

### Mål
Bestäm vilka typer av källor GPT:n ska söka efter, hur de prioriteras och hur motstridiga uppgifter hanteras.

### Leveranser
Källmodell med minst följande grupper:

1. **Formell styrning**
   - myndighetsinstruktion
   - regleringsbrev
   - regeringsuppdrag
   - relevanta förordningar och andra bindande styrdokument

2. **Myndighetens strategiska information**
   - uppdrag
   - mål
   - vision
   - verksamhetsstrategi
   - strategiska planer
   - verksamhetsplaner
   - budgetunderlag
   - årsredovisningar
   - organisations- och arbetsordning
   - befintlig IT- eller digitaliseringsstrategi

3. **Observationer om nuläge och förändringsbehov**
   - större program och initiativ
   - offentliga upphandlingar
   - Riksrevisionen och andra granskningar
   - relevanta tillsynsbeslut
   - uttalade kompetens- eller moderniseringsbehov
   - samverkansinitiativ

4. **Extern styrning och beroenden**
   - EU-krav
   - nationella digitaliseringsinitiativ
   - DIGG
   - MSB
   - Riksarkivet
   - eSam
   - sektorsspecifika aktörer och regelverk

5. **IT-omvärld**
   - AI
   - cybersäkerhet
   - moln och plattformar
   - data och informationshantering
   - integration och interoperabilitet
   - DevSecOps och automation
   - legacy och teknisk skuld
   - kompetens
   - sourcing
   - digital suveränitet och leverantörsberoenden

### Validering
- Primärkällor prioriteras framför sekundärkällor.
- Officiella myndighetskällor prioriteras framför leverantörsmaterial.
- GPT:n kan hantera att vissa källtyper saknas.

### Klart när
- Källhierarkin finns i canonical instruktion.
- Regler för aktualitet, kvalitet och konflikt mellan källor är definierade.
- Informationsluckor redovisas explicit.

---

## Steg 4 – Definiera evidens- och spårbarhetsmodell

### Mål
Säkerställa att strategiska slutsatser kan härledas från konkreta observationer.

### Leveranser
En intern analysmodell motsvarande:

**Observation → källa → betydelse → strategisk konsekvens → rekommendation**

Varje större strategiskt påstående ska kunna klassificeras som:
- fakta
- analys
- rekommendation
- antagande
- osäkerhet/informationslucka

### Validering
- GPT:n presenterar inte analys som om den vore källa.
- Rekommendationer kan spåras till minst en relevant observation eller tydligt angivet antagande.
- Branschtrender får inte ensamma motivera myndighetsspecifika strategiska mål.

### Klart när
- Spårbarhetsmodellen är definierad.
- Ett exempel på hela kedjan från källa till rekommendation passerar test.

---

## Steg 5 – Definiera analys av uppdrag, styrning och verksamhetsmål

### Mål
Bygga den del av GPT:n som identifierar vad myndigheten faktiskt ska åstadkomma och vilka förändringar styrningen kräver.

### Leveranser
Analysram för:
- kärnuppdrag
- målgrupper
- lagstadgade uppgifter
- politiska mål och regeringsuppdrag
- återrapporteringskrav
- strategiska mål
- målkonflikter
- beroenden till andra aktörer
- krav på informationsutbyte
- verksamhetskritiska förändringar

### Klart när
- GPT:n kan skapa en strukturerad strategisk kontext från myndighetens styrdokument.
- IT-frågor introduceras först efter att verksamhetsbehovet identifierats.

---

## Steg 6 – Definiera ekonomisk och kapacitetsmässig analys

### Mål
Ge strategin realistiska ekonomiska och organisatoriska förutsättningar.

### Leveranser
Analysram för:
- anslagsutveckling
- kostnadsutveckling
- personalutveckling
- investeringar
- större åtaganden
- besparingskrav
- finansierade respektive ofinansierade initiativ
- kompetens- och genomförandekapacitet
- flerårsutveckling när data finns

### Validering
- Enskilda års siffror övertolkas inte.
- Ekonomiska slutsatser skiljer mellan redovisade fakta och analys.

### Klart när
- Ekonomiska förutsättningar kan kopplas till strategiska ambitioner och prioriteringar.

---

## Steg 7 – Definiera nuläges- och förändringstrycksanalys

### Mål
Identifiera dokumenterade problem, möjligheter och pågående förflyttningar som påverkar IT-strategin.

### Leveranser
Analysram för:
- stora förändringsprogram
- digitalisering
- teknisk modernisering
- informationsutbyte
- data
- automatisering
- cybersäkerhet
- kompetens
- sourcing
- samverkan
- revisions- och granskningsiakttagelser
- teknisk skuld när den kan beläggas

### Klart när
- GPT:n kan skilja mellan dokumenterat nuläge och infererat nuläge.
- Osäkra slutsatser markeras som sådana.

---

## Steg 8 – Definiera IT-omvärldsanalys

### Mål
Skapa en aktuell men selektiv omvärldsanalys som bara lyfter trender med strategisk relevans för myndigheten.

### Leveranser
Metod för att:
- söka aktuell information
- bedöma trendens mognad
- bedöma relevans för myndighetens uppdrag
- bedöma möjligheter och risker
- skilja strukturella förändringar från kortlivade trender

Minimiområden:
- AI
- cybersäkerhet
- moln och plattformar
- data
- integration/interoperabilitet
- DevSecOps/automation
- legacy/teknisk skuld
- kompetens
- sourcing
- digital suveränitet

### Validering
- Trendspaning blir inte automatiskt rekommendation.
- Aktuell research används för snabbt föränderliga områden.
- Källor anges.

### Klart när
- GPT:n kan rangordna trender efter faktisk strategisk relevans.

---

## Steg 9 – Definiera strategiska IT-utmaningar och gap

### Mål
Knyta ihop myndighetens behov, nuläge och omvärld till ett begränsat antal strategiska IT-frågor.

### Leveranser
Metod för att formulera:
- strategiska problem
- förmågegap
- möjlighetsområden
- risker
- beroenden
- prioriteringsgrund

### Validering
- Varje strategisk IT-fråga kan spåras till underlaget.
- Dubbletter och symptom konsolideras till bakomliggande strategiska frågor.

### Klart när
- GPT:n kan producera en prioriterad lista över strategiska IT-utmaningar utan att hoppa direkt till lösning.

---

## Steg 10 – Definiera IT-strategiska mål

### Mål
Formulera ett litet antal tydliga mål som beskriver önskad framtida förmåga eller effekt.

### Leveranser
Regler för:
- målformulering
- spårbarhet till verksamhetsmål
- mätbarhet
- avgränsning
- prioritering
- tidshorisont

### Validering
- Tekniknamn används normalt inte som mål.
- Målen uttrycker effekt eller förmåga.
- Mål kan motiveras av analyserade behov.

### Klart när
- GPT:n kan formulera ett sammanhängande och begränsat målramverk.

---

## Steg 11 – Definiera strategiska vägval och principer

### Mål
Beskriva hur myndigheten bör agera för att nå målen utan att gå ner på onödig produktnivå.

### Leveranser
Metod för:
- strategiska vägval
- styrande IT-principer
- alternativ och trade-offs
- konsekvenser av val
- explicita icke-val där relevant

Möjliga områden:
- standardisering kontra lokal frihet
- bygga kontra köpa
- gemensamma plattformar
- API-first
- informationsorientering
- cloud-smart
- automation
- säkerhet och robusthet
- återanvändning
- leverantörsberoenden

### Validering
- Vägvalen är förankrade i myndighetens behov.
- Specifika produkter rekommenderas endast om analysen verkligen kräver det.

### Klart när
- Mål och vägval bildar en logiskt sammanhängande kedja.

---

## Steg 12 – Definiera prioriterade förflyttningar och initiativområden

### Mål
Översätta strategin till genomförbara förändringsområden utan att bli en detaljerad projektportfölj.

### Leveranser
Metod för att beskriva:
- nuläge
- önskat läge
- strategisk förflyttning
- förväntad effekt
- beroenden
- risker
- ungefärlig prioritet
- möjlig tidshorisont

### Klart när
- GPT:n kan identifiera ett hanterbart antal strategiska förflyttningar.
- Varje förflyttning är kopplad till mål och vägval.

---

## Steg 13 – Definiera konsekvensanalys

### Mål
Visa vad strategin innebär utanför själva tekniken.

### Leveranser
Konsekvensanalys för minst:
- verksamhetsstyrning
- IT-styrning
- enterprise architecture
- informations- och datahantering
- organisation
- kompetens
- sourcing och leverantörer
- säkerhet
- finansiering
- samverkan

### Klart när
- Strategin tydligt visar organisatoriska och styrningsmässiga konsekvenser.

---

## Steg 14 – Definiera färdplan och uppföljning

### Mål
Göra strategin användbar för styrning över tid.

### Leveranser
Metod för:
- kort, medellång och längre tidshorisont
- beroenden
- prioriteringsordning
- strategiska milstolpar
- indikatorer
- effektmått
- uppföljningscykel
- omprövning av strategin

### Validering
- Färdplanen är strategisk, inte en detaljerad projektplan.
- Mått kan kopplas till strategiska mål.

### Klart när
- GPT:n kan skapa en begriplig genomföranderiktning och modell för uppföljning.

---

## Steg 15 – Definiera slutrapporten

### Mål
Fastställa struktur och kvalitetskrav för den fullständiga IT-strategin.

### Leveranser
Rapportstruktur:

1. Sammanfattning
2. Strategisk kontext
3. Uppdrag och styrning
4. Nuläge och förändringstryck
5. Ekonomiska och organisatoriska förutsättningar
6. Relevant IT-omvärld
7. Strategiska IT-utmaningar
8. IT-strategiska mål
9. Strategiska vägval
10. IT-principer
11. Prioriterade förflyttningar
12. Konsekvenser
13. Färdplan
14. Uppföljning
15. Metod, antaganden och informationsluckor
16. Källor

### Klart när
- Rapportmallen är definierad.
- Spårbarheten bevaras i slutrapporten.
- Strategin tydligt skiljer fakta, analys och rekommendation.

---

## Steg 16 – Definiera ledningsversion

### Mål
Skapa en kortare version som går att använda för ledningsdialog och beslut.

### Leveranser
Ledningsversion med exempelvis:
- strategisk situation
- 5–8 viktigaste slutsatser
- strategiska mål
- viktigaste vägval
- prioriterade förflyttningar
- kritiska risker och beroenden
- rekommenderade beslut

### Klart när
- Ledningsversionen kan förstås utan att läsa hela rapporten.
- Innehållet är konsistent med fullversionen.

---

## Steg 17 – Implementera canonical instruktion

### Mål
Omsätta de tidigare designstegen till GPT:ns faktiska kärninstruktion.

### Leveranser
- canonical `instructions.md`
- tydliga beteenderegler
- workflow
- källregler
- researchregler
- analysregler
- spårbarhetskrav
- status- och nästa-steg-logik
- rapporteringsregler

### Validering
- Kritiska beteenden ligger i canonical instruktion och inte enbart i knowledge.
- Kärnflödet har få obligatoriska runtime-beroenden.
- Instruktionen fungerar för både Chat ZIP och Custom GPT.

### Klart när
- Canonical instruktion är komplett och lintbar.

---

## Steg 18 – Skapa Knowledge-arkitektur

### Mål
Lägga stabil metod- och domänkunskap utanför kärninstruktionen utan att göra den nödvändig för kritiskt beteende.

### Leveranser
Möjliga knowledge-filer:
- metod för IT-strategi
- svensk myndighetsstyrning – orientering
- källvärdering
- strategiska mål och vägval
- omvärldsanalys
- rapportstruktur och kvalitetskriterier

### Validering
- Knowledge duplicerar inte canonical instruktion i onödan.
- Tidskänslig information hårdkodas inte som permanent knowledge.

### Klart när
- Knowledge-strukturen är lätt att underhålla och understöder huvudflödet.

---

## Steg 19 – Skapa schemas och strukturerade arbetsartefakter

### Mål
Ge GPT:n stabila interna format för komplexa analyser.

### Leveranser
Schemas där de tillför värde, exempelvis för:
- source inventory
- evidence item
- strategic driver
- strategic issue
- IT strategic goal
- strategic choice
- principle
- transformation
- roadmap item
- source gap
- strategy status

### Validering
- Scheman är inte mer komplexa än nödvändigt.
- De stödjer spårbarhet mellan analysstegen.

### Klart när
- De centrala analysobjekten har stabil struktur.

---

## Steg 20 – Skapa tester för research och källhantering

### Mål
Verifiera att GPT:n hittar rätt källor och värderar dem rimligt.

### Testfall
- väl dokumenterad större myndighet
- mindre myndighet med få offentliga dokument
- motstridiga källor
- gammal strategi kontra nyare regleringsbrev
- saknat budgetunderlag
- osäker tredjepartskälla
- aktuell snabbt föränderlig IT-trend

### Klart när
- Testerna fångar felaktig källprioritering och ogrundade antaganden.

---

## Steg 21 – Skapa tester för strategisk härledning

### Mål
Verifiera att strategin verkligen härleds från underlaget.

### Testfall
- trend som inte är relevant ska väljas bort
- verksamhetskrav ska kunna skapa ett strategiskt IT-mål
- produktnamn ska inte uppstå utan motivering
- mål ska inte blandas ihop med initiativ
- observation ska kunna spåras till rekommendation
- osäkerhet ska föras vidare till slutsatsen

### Klart när
- GPT:n klarar positiva och negativa härledningstester.

---

## Steg 22 – Skapa end-to-end-scenario

### Mål
Testa hela flödet från myndighetsnamn till färdig strategi.

### Leveranser
Minst ett komplett referensscenario med en verklig svensk myndighet och offentliga källor.

### Validering
- källinventering
- samtliga analysfaser
- strategiska mål
- vägval
- förflyttningar
- färdplan
- full rapport
- ledningsversion
- källspårbarhet

### Klart när
- Ett komplett scenario kan genomföras utan att workflow bryts.

---

## Steg 23 – Optimera för Chat ZIP

### Mål
Skapa en portabel Chat-runtime med samma canonical beteende.

### Leveranser
- Chat ZIP-struktur
- `START-HERE.md`
- runtime-manifest
- instruktion
- knowledge
- schemas
- relevanta scripts
- versionsmetadata

### Validering
- ZIP kan bifogas i en ny konversation och användas utan projektrepot.
- Kärnflödet fungerar i Chat-läge.

### Klart när
- Chat ZIP passerar distributionsvalidering.

---

## Steg 24 – Optimera för Custom GPT

### Mål
Kompilera projektet till en praktiskt användbar Custom GPT inom plattformens begränsningar.

### Leveranser
- Custom GPT-instruktion
- knowledge-paket
- capability-inställningar
- rekommenderad konfiguration
- compatibility-dokumentation

### Validering
- Kritiska regler har inte fallit bort vid kompilering.
- Instruktionen håller sig inom plattformens begränsningar.
- Funktionsskillnader mot Chat ZIP dokumenteras.

### Klart när
- Custom GPT-distributionen passerar validering.

---

## Steg 25 – Runtime-paritet och kvalitetsgranskning

### Mål
Verifiera att Chat ZIP och Custom GPT representerar samma GPT trots tekniska skillnader.

### Leveranser
- runtime parity report
- avvikelselista
- korrigeringar vid behov

### Klart när
- Inga blockerande beteendeskillnader finns.
- Nödvändiga plattformsskillnader är dokumenterade.

---

## Steg 26 – Project hygiene och dokumentationsgranskning

### Mål
Rensa projektet och säkerställa att endast relevanta filer finns kvar.

### Leveranser
- hygiene report
- rensning av temporära filer
- uppdaterad README
- uppdaterad PROJECT
- uppdaterad STATUS
- uppdaterad project-status

### Klart när
- Projektet är rent, begripligt och reproducerbart.
- Inga temporära arbetsartefakter ligger kvar utan syfte.

---

## Steg 27 – GitHub Actions CI

### Mål
Automatisera lint, tester och distributionsvalidering.

### Leveranser
GitHub Actions för:
- lint
- schemas
- tester
- build
- distributionsvalidering
- project hygiene-kontroll där lämpligt

### Klart när
- CI kan köras från ett rent checkout och passerar.

---

## Steg 28 – GitHub Release-build

### Mål
Automatiskt bygga versionssatta distributionsartefakter från GitHub Release-taggen.

### Leveranser
Release-workflow som producerar minst:
- projekt-ZIP
- Chat ZIP
- Custom GPT-distribution
- relevanta rapporter/checksummor om projektstandarden kräver det

### Validering
- Versionsnumret kommer från release-taggen.
- Artefakterna kan reproduceras från releasen.

### Klart när
- Ett release candidate-build kan genomföras utan manuella korrigeringar.

---

## Steg 29 – Release readiness

### Mål
Samla alla kvalitetskontroller inför första release.

### Kontroller
- project status
- lint
- schemas
- tester
- end-to-end
- build
- Chat ZIP-validering
- Custom GPT-validering
- runtime-paritet
- hygiene
- dokumentation
- release-workflow

### Klart när
- Inga blockerande fel finns.
- Eventuella kvarvarande varningar är dokumenterade och accepterade.

---

## Steg 30 – Första release candidate

### Mål
Bygga en komplett RC som kan provas praktiskt.

### Leveranser
- versionssatt projekt-ZIP
- versionssatt Chat ZIP
- Custom GPT-paket
- release notes
- kända begränsningar
- testinstruktion

### Klart när
- RC:n går att använda i ett verkligt strategiarbete.

---

## Steg 31 – Pilotgranskning och justering

### Mål
Prova GPT:n på flera typer av myndigheter och korrigera metodproblem.

### Rekommenderade pilotfall
- stor IT-tung myndighet
- mindre myndighet
- myndighet med omfattande EU-styrning
- myndighet med stor informationsutbytesproblematik

### Klart när
- Samma metod ger användbara men tydligt myndighetsspecifika strategier.
- Generiska standardrekommendationer har reducerats till acceptabel nivå.

---

## Steg 32 – Stabil release

### Mål
Publicera första stabila versionen.

### Leveranser
- slutlig projekt-ZIP
- Chat ZIP
- Custom GPT-paket
- README och användarinstruktion
- compatibility
- release notes

### Klart när
- Stable release-valideringen passerar.
- Projektstatus visar aktuell stabil version och rekommenderat nästa utvecklingsområde.

---

## Planstatus

**Alla 32 planerade steg är klara.** Version 0.1.0 är stabil release. Fortsatt utveckling sker som nya 0.2.x-steg baserat på verklig användningsfeedback.


---

## Steg 33 – GPT Byggaren 1.5-kontrakt och modellrobust kärna

### Mål
Migrera projektets canonical kontrakt till GPT Byggaren 1.5.0 utan att ändra strategimetoden.

### Leveranser
- plattformsneutrala capability-, artifact-, workspace/state- och tool-kontrakt
- stateful modellrobust workflow
- explicit operativ kärna och auktoritativ status
- fyra modellkompatibilitetsscenarier
- bedömning av samtliga fem registrerade runtimes

### Klart när
- befintlig CI är grön
- domänbeteendet är oförändrat
- 1.5-kontrakten är lintbara och spårbara

---

## Steg 34 – Anpassa distributionsmotorn till 1.5

### Mål
Låta Chat ZIP och Custom GPT byggas från samma 1.5-kontrakt utan att förlora den research-heavy metodiken.

### Leveranser
- runtime-kontrakt i distributionerna
- verifierad Custom GPT-kompilering som bevarar kärnmarkörer
- tydlig separation mellan canonical instruktion och kompilerad runtime-instruktion
- bedömning om OpenCode kan aktiveras efter research-paritetstest

### Klart när
- Chat och Custom GPT passerar distributionsvalidering
- inga kärnregler tappas i Custom GPT-kompileringen

---

## Steg 35 – Generaliserad runtime parity och release readiness

### Mål
Utöka paritetsgrinden från två distributionsformat till 1.5-modellens fem registrerade runtimes.

### Leveranser
- parity-bedömning för behavior, capability, artifact, workspace/state och tool
- explicit status för Claude Projects, OpenCode och OpenAI Plugin
- release readiness som blockerar vid oavsiktlig runtime-drift

### Klart när
- aktiva runtimes är verifierade
- reducerade/inaktiva runtimes har explicit motivering

---

## Steg 36 – Slutvalidera migreringen och releasekedjan

### Mål
Verifiera hela migreringen från rent checkout till releaseartefakter.

### Leveranser
- full regression
- CI/release-paritet
- migrationsnoter
- uppdaterad projektstatus

### Klart när
- samtliga aktiva distributioner och gates passerar
- projektet är redo att mergeas och releasas

---

## Migrationsstatus

Migrering till GPT Byggaren 1.5.0 pågår från den stabila basen 0.1.0. Steg 33 är aktuellt.
