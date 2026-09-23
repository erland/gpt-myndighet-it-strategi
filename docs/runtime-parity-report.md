# Runtime-paritetsrapport – GPT Byggaren 1.5

## Slutsats

**Resultat: PASS för aktiva runtimes.** Chat ZIP och Custom GPT representerar samma GPT på beteendenivå. Alla fem registrerade runtimes är nu explicit bedömda enligt GPT Byggaren 1.5.

Chat ZIP är den fullständiga runtime-representationen och använder canonical instruktion byte-identiskt. Custom GPT är en kompilerad representation som behåller kritiska beteendekontrakt inom plattformens instruktionsgräns.

## Paritetsmodell

Paritet bedöms inte som textuell identitet mellan runtime-formaten. GPT Byggaren 1.5 jämför fem kontraktskategorier: **behavior, capability, artifact, workspace_state och tool**. För de två aktiva runtimes används dessutom följande konkreta kontrollager:

1. **Identitet och uppdrag** – samma roll, målgrupp och slutprodukt.
2. **Kritiskt beteende** – samma research-, käll-, evidens-, fasgrinds-, härlednings-, guardrail- och rapportregler.
3. **Stödjande kunskap** – samma sju tidsneutrala Knowledge-filer med identiskt innehåll.
4. **Capabilities** – Custom GPT har de funktioner som krävs för att motsvara Chat-runtimens arbetsmetod, framför allt web browsing.

## Verifierade beteendekontrakt

Följande kontraktsgrupper verifieras maskinellt i `scripts/validate-runtime-parity.py`:

- identitet och scope
- källprioritering och källauktoritet
- separation mellan fakta, analys, rekommendation, antagande och lucka
- evidens- och spårbarhetskedja
- proportionalitet mellan evidens och rekommendationsstyrka
- trendguardrails
- produkt-/detaljlösningsguardrails
- förbud mot fabricerade sakuppgifter och falsk precision
- aktuell webbresearch och aktualitetskontroll
- 15-fasers workflow
- nästa-steg-beteende
- tre fasgrindar
- verksamhets-/styrningsanalys före lösning
- ekonomisk och organisatorisk genomförbarhet
- explicit hantering av infererat nuläge och osäkerhet
- selektiv IT-omvärldsanalys
- lösningsneutrala strategiska mål
- alternativ- och trade-off-analys
- förflyttningskontrakt
- dubbelriktad konsekvensanalys
- färdplan och uppföljningsindikatorer
- fullrapport/ledningsversion-paritet
- slutlig kvalitetsgrind
- Knowledge/runtime-gräns

## Knowledge-paritet

Chat ZIP och Custom GPT använder samma sju Markdown-filer som metodstöd. Validatorn kräver både samma filuppsättning och byte-identiskt innehåll.

JSON Schemas inkluderas endast i Chat ZIP. Detta är **inte** en beteendedrift: schemas är strukturerade projekt-/testkontrakt och kritiska runtime-regler som de skyddar finns redan i instruktionen.

## Accepterade plattformsskillnader

| Område | Chat ZIP | Custom GPT | Bedömning |
|---|---|---|---|
| Instruktion | Full canonical instruktion | Kompilerad instruktion | Accepterad; kritiska kontrakt verifieras |
| Start | `START-HERE.md` | GPT-konfiguration + starters | Accepterad |
| Knowledge | 7 metodfiler + schemas i paket | 7 metodfiler | Accepterad |
| Schemas | 11 runtime-tillgängliga filer | Inte Knowledge | Accepterad; test/projektkontrakt |
| Runtime-policy | Separat policyfil möjlig | Kritiska regler direkt i instruktion | Accepterad |
| Webbresearch | Tillgängligt i Chat-miljön | Web browsing måste vara aktiverat | Krav verifierat i config |
| Dataanalys | Miljöberoende | Aktiverad/rekommenderad | Accepterad |
| Actions | Ej nödvändigt | Ej nödvändigt | Paritet |
| Bildgenerering | Ej nödvändigt | Ej nödvändigt | Paritet |

## Risker som kvarstår

Custom GPT-instruktionen har mindre metodförklaring och färre exempel än canonical instruktion. Det kan ge mindre pedagogisk redundans i svåra fall, men inte en avsiktlig skillnad i beslutskriterier. De sju gemensamma Knowledge-filerna reducerar denna risk.

Faktiskt modellbeteende kan ändå variera mellan körningar och modellkonfigurationer. Projektets paritetskontroll verifierar därför **kontrakt och distribution**, inte deterministiskt identiska formuleringar.

## Avvikelselista

### Blockerande avvikelser

Inga.

### Accepterade avvikelser

1. Full kontra kompilerad instruktion.
2. Schemas finns i Chat ZIP men inte som Custom GPT Knowledge.
3. Olika startmekanism.
4. Separata runtime-policyfiler kan bäras av Chat ZIP men inte behövs i Custom GPT.

Ingen av dessa avvikelser ändrar GPT:ns avsedda strategimetod eller guardrails.

## Kvalitetsbedömning

Runtime-pariteten bedöms som tillräcklig för nästa fas. Projektet kan gå vidare till project hygiene och dokumentationsgranskning utan korrigerande runtime-arbete.


## GPT Byggaren 1.5 – registrerade runtimes

| Runtime | Suitability | Aktiv som standard | Bedömning |
| --- | --- | --- | --- |
| ChatGPT Chat | ready | Ja | Fullt stöd för webbresearch, filer och portabelt tillstånd. |
| ChatGPT Custom | reduced | Ja | Kärnflödet stöds; research- och filfunktioner beror på aktiverade plattformsverktyg. |
| Claude Projects | reduced | Nej | Instruktion/Knowledge kan paketeras men workspace och deterministisk verifiering är begränsad. |
| OpenCode | reduced | Nej | Workspace/lokal exekvering är starkt, men webbresearch och källparitet är ännu inte verifierad. |
| OpenAI Plugin | reduced | Nej | Skills/referenser kan paketeras men hela research-/stateflödet realiseras inte av Plugin v1. |

De tre reducerade runtimes får inte aktiveras enbart för att en teknisk distribution går att bygga. För IT-strategen krävs verifierad **research- och källparitet** innan de kan bli aktiva peer runtimes.

## Release gate

`scripts/validate-runtime-parity.py` verifierar nu både den befintliga Chat/Custom-beteendepariteten och 1.5-registreringen för alla fem runtimes. `scripts/validate-release-readiness.py` behandlar samma runtimebeslut och de aktiva runtime-kontrakten som blockerande releasekrav.
