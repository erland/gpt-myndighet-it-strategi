# Strategiska vägval och principer

## Syfte

Detta steg översätter det spårbara målramverket till **strategiska vägval** och **styrande principer**. Ett vägval beskriver hur myndigheten på strategisk nivå väljer att agera för att nå ett eller flera mål. En princip beskriver en återkommande beslutsregel som ska styra framtida beslut i linje med dessa vägval.

Steget ska skapa strategisk riktning utan att i onödan låsa myndigheten till en specifik produkt, leverantör, teknisk implementation eller detaljerad målarkitektur.

## Grundregel

Ett strategiskt vägval ska svara på frågan:

> **Vilken övergripande riktning behöver myndigheten välja för att nå sina IT-strategiska mål, givet målkonflikter, risker, beroenden och faktisk genomförandekapacitet?**

En princip ska svara på frågan:

> **Vilken återkommande beslutsregel behöver tillämpas för att framtida beslut ska stödja den valda strategiska riktningen?**

Vägval är alltså **val mellan meningsfulla alternativ**. Principer är **regler för återkommande beslut**. Varken vägval eller principer är i sig projekt, aktiviteter eller produktval.

## Indata

Använd i första hand:

- prioriterade `it_strategic_goal`-objekt,
- målspänningar och beroenden,
- prioriterade `strategic_issue`-objekt,
- ekonomiska och kapacitetsmässiga begränsningar,
- relevanta `environment_signal`-objekt,
- styrkrav och verksamhetsberoenden,
- kända informationsluckor och osäkerheter.

## Arbetsordning

Arbeta i följande ordning:

1. **Identifiera beslutsteman.** Gruppera mål och utmaningar som kräver samma strategiska typ av val.
2. **Formulera verkliga alternativ.** Beskriv minst två meningsfulla handlingsriktningar när ett faktiskt vägval finns.
3. **Synliggör trade-offs.** Beskriv vad varje alternativ vinner, kostar, riskerar eller begränsar.
4. **Pröva mot mål och styrning.** Bedöm vilket alternativ som bäst stödjer målen och myndighetens uppdrag.
5. **Pröva genomförbarhet.** Väg in ekonomi, kompetens, förändringskapacitet, leverantörsberoenden och tidshorisont.
6. **Välj strategisk riktning.** Rekommendera ett alternativ med explicit motivering och säkerhetsnivå.
7. **Definiera guardrails.** Ange viktiga villkor, undantag eller situationer där valet inte bör tillämpas mekaniskt.
8. **Härled principer.** Formulera de återkommande beslutsregler som behövs för att operationalisera vägvalet.
9. **Pröva portföljen.** Kontrollera att vägvalen inte motsäger varandra och att principerna inte är redundanta eller för detaljerade.

## Vad som räknas som ett vägval

Ett vägval ska uttrycka **strategisk riktning i en verklig avvägning**. Exempel på legitima teman är:

- gemensam standardisering kontra lokal variation,
- återanvändning kontra nyutveckling,
- köpa kontra bygga kontra samverka,
- centraliserade gemensamma plattformar kontra distribuerade lokala lösningar,
- egen drift kontra extern molntjänst kontra hybrid lösning,
- snabb förändring kontra hög kontroll och förändringsdisciplin,
- konsolidering kontra bibehållen diversitet,
- långsiktig flexibilitet kontra kortsiktig leveranshastighet,
- hög redundans/robusthet kontra kostnadsoptimering,
- leverantörseffektivitet kontra exitförmåga och minskat beroende.

Vägvalet ska beskriva **riktningen och avvägningen**, inte bara återge ett populärt branschbegrepp.

## Exempel: från mål till vägval

Antag ett mål om snabbare, säkrare och mer standardiserat informationsutbyte.

Ett rimligt vägval kan vara:

> Myndigheten prioriterar gemensamma integrationsmönster, standardiserade gränssnitt och återanvändbara informationskontrakt framför punkt-till-punkt-integrationer, utom när särskilda verksamhets- eller säkerhetskrav motiverar avsteg.

Detta är bättre än:

> Myndigheten ska införa produkt X för API management.

Det första är en strategisk riktning. Det andra är ett lösnings- eller upphandlingsbeslut som kräver separat analys.

## Alternativanalys och trade-offs

Ett vägval ska inte presenteras som självklart när det finns rimliga alternativ. För varje betydande vägval ska GPT:n så långt underlaget medger beskriva:

- **alternativ A**, inklusive styrkor, svagheter, risker och förutsättningar,
- **alternativ B**, inklusive styrkor, svagheter, risker och förutsättningar,
- eventuellt **alternativ C** när det tillför en verklig strategisk möjlighet,
- **rekommenderad riktning**,
- **varför den rekommenderas för just denna myndighet**,
- **viktigaste nackdel eller alternativkostnad**,
- **förutsättningar för att valet ska fungera**,
- **situationer där undantag kan vara motiverade**.

Undvik skenalternativ. Två formuleringar som i praktiken innebär samma sak räknas inte som en verklig alternativanalys.

## Beslutskriterier

Bedöm vägval kvalitativt utifrån minst:

- bidrag till strategiska mål,
- överensstämmelse med formell styrning,
- verksamhetsnytta och uppdragsrelevans,
- genomförbarhet och kapacitet,
- säkerhet och robusthet,
- flexibilitet och framtida handlingsfrihet,
- kostnad och ekonomisk hållbarhet,
- tid till effekt,
- beroenden och leverantörsinlåsning,
- reversibilitet och exitförmåga,
- evidensstyrka och osäkerhet.

Kriterierna ska inte automatiskt viktas lika. Bedömningen ska spegla myndighetens faktiska situation och styrning.

## Reversibilitet och bindning

Vägval med hög kostnad, lång tidshorisont, stor leverantörsbindning eller låg reversibilitet kräver starkare evidens och tydligare alternativanalys än lätt reversibla beslut.

För stora eller svårreversibla val ska GPT:n särskilt beskriva:

- hur lätt valet kan ändras senare,
- vilka exitkostnader som kan uppstå,
- vilka nya beroenden som skapas,
- om stegvis eller experimentell införandeväg kan minska risken,
- vilken information som bör verifieras före definitivt beslut.

## Strategiska principer

En princip ska vara:

- kort och lätt att återanvända,
- normativ snarare än beskrivande,
- stabil över flera år,
- tillämpbar på många beslut,
- tydligt kopplad till minst ett vägval eller strategiskt mål,
- tillräckligt konkret för att kunna påverka beslut,
- tillräckligt generell för att inte vara en enskild lösningsregel.

Exempel:

> **Återanvänd före nyutveckling.** Befintliga gemensamma förmågor, tjänster och komponenter ska utvärderas innan nya lokala lösningar skapas.

> **Standardisera där variation inte skapar verksamhetsvärde.** Gemensamma mönster och standarder ska vara förstahandsval när lokala skillnader inte är nödvändiga för uppdraget.

> **Designa för exit och portabilitet.** Kritiska externa beroenden ska utformas så att data, integrationer och centrala funktioner kan flyttas eller ersättas till rimlig kostnad och risk.

## Princip kontra standard eller teknisk regel

Principer ska inte bli detaljerade standarder. Formuleringar som “alla tjänster ska använda Kubernetes”, “all integration ska använda produkt X” eller “alla system ska använda databas Y” är normalt tekniska standarder eller lösningsbeslut, inte strategiska principer.

En mer strategisk princip kan vara:

> Plattformar ska standardiseras där gemensam drift, säkerhet och utvecklingsförmåga ger tydlig skalfördel, samtidigt som undantag tillåts när verksamhetskrav eller riskbild motiverar det.

Tekniska standarder kan senare härledas från principerna genom arkitektur- och styrningsarbete.

## Cloud-smart i stället för reflexmässig cloud-first

Moln ska behandlas som ett vägval med flera alternativ och konsekvenser, inte som en universell destination. Bedöm bland annat:

- informationsklassning och regelkrav,
- kontinuitet och robusthet,
- kompetens och operativ förmåga,
- kostnadsmodell och volymprofil,
- leverantörsberoende och exit,
- tillgång till standardiserade plattformstjänster,
- förändringshastighet och skalbarhetsbehov.

När moln är lämpligt kan strategisk riktning uttryckas som **cloud-smart**: välj molnbaserade tjänster där de ger tydlig strategisk nytta och kan användas med acceptabel risk, kostnad och handlingsfrihet. Detta får inte användas som automatisk standardformulering; valet måste härledas från myndighetens kontext.

## Bygga, köpa eller samverka

För större förmågor ska GPT:n vid behov pröva minst tre strategiska anskaffningsvägar:

- **bygga/äga själv**,
- **köpa som produkt eller tjänst**,
- **samverka/återanvända gemensam offentlig förmåga**.

Bedöm särskilt strategisk differentiering, marknadsmognad, livscykelkostnad, kompetensbehov, kontrollbehov, leverantörsrisk, förändringstakt och möjlighet till gemensam offentlig lösning.

“Buy before build” eller “build before buy” får inte införas som generell princip utan myndighetsspecifik motivering. En mer robust princip är att välja anskaffningsform efter strategisk betydelse, marknadsmognad, kontrollbehov och total livscykelkonsekvens.

## Standardisering och variation

Standardisering kan ge lägre kostnad, högre säkerhet, snabbare leverans och enklare kompetensförsörjning men kan samtidigt minska lokal flexibilitet. Vägvalet ska därför beskriva **var standardisering är strategiskt värdefull** och **när kontrollerad variation behöver vara tillåten**.

Undvik absoluta formuleringar om att “allt ska standardiseras”. Fokusera i stället på standardisering av sådant som inte skapar särskilt verksamhetsvärde genom variation.

## Gemensamma plattformar

Plattformsorientering får rekommenderas när gemensamma behov, skalfördelar, säkerhetskrav, utvecklingshastighet eller återanvändning motiverar det. Men “plattform” är inte ett mål i sig.

Ett strategiskt vägval kan exempelvis vara att samla återkommande tekniska förmågor i gemensamt styrda plattformstjänster för att minska duplicering och höja leveranstakt och säkerhet. Valet ska samtidigt hantera risken för flaskhalsar, övercentralisering och en plattformsorganisation som inte svarar mot verksamhetens behov.

## API-first, informationsorientering och interoperabilitet

API-first eller liknande begrepp får endast användas när de beskriver en tydlig strategisk riktning. Fokus ska ligga på interoperabilitet, tydliga informationskontrakt, lös koppling och kontrollerad exponering – inte på en specifik API-teknik.

När informationsutbyte är centralt bör principerna även beakta semantik, informationsansvar, standarder och livscykelhantering av informationskontrakt.

## Automation och DevSecOps

Automation och DevSecOps kan vara vägval när myndighetens mål kräver kortare ledtider, högre kvalitet, säkrare förändringar eller effektivare drift. Rekommendationen ska beskriva önskad strategisk förflyttning i arbetssätt och styrning, inte bara införande av verktyg.

## Säkerhet och robusthet

Säkerhet ska integreras i vägval och principer snarare än läggas på i efterhand. Vid målkonflikter mellan leveranshastighet, kostnad och robusthet ska avvägningen synliggöras.

Principer kan exempelvis uttrycka att säkerhets- och kontinuitetskrav ska byggas in i arkitektur och utvecklingsflöden från början och vara proportionerliga mot informationens och tjänstens kritikalitet.

## Leverantörsberoenden och digital suveränitet

Digital suveränitet ska inte reduceras till egen drift eller nationella produkter. Analysera i stället handlingsfrihet och kritiska beroenden.

Relevanta vägval kan omfatta:

- krav på portabilitet och exit,
- öppna eller etablerade standarder,
- separering av data från leverantörsspecifik logik när det är strategiskt relevant,
- flera leverantörer där redundans motiverar kostnaden,
- tydlig kontroll över identitet, data, loggning och nyckelmaterial,
- förmåga att fortsätta kritisk verksamhet vid leverantörsstörning.

## Explicit icke-val

Det kan vara strategiskt värdefullt att dokumentera vad myndigheten **inte** väljer, särskilt när ett populärt eller tidigare dominerande alternativ avvisas.

Ett icke-val ska innehålla:

- avvisat alternativ,
- varför det inte är lämpligt i aktuell strategiperiod,
- vilka omständigheter som skulle kunna motivera omprövning.

Exempelvis kan myndigheten avstå från ett generellt “cloud-first”-krav men samtidigt använda molntjänster selektivt där analysen visar nytta.

## Vägval kontra genomförande

Ett vägval ska inte beskriva en detaljerad implementationssekvens. Formuleringar som “upphandla X”, “migrera system A före system B”, “införa produkt Y under 2027” eller “bygga tre plattformsteam” hör hemma i senare förflyttnings-, färdplans- eller genomförandeanalys.

Vägvalet ska vara tillräckligt stabilt för att flera olika genomföranden ska kunna vara förenliga med strategin.

## Spårbarhet

Varje strategiskt vägval ska kunna följas bakåt till:

1. minst ett IT-strategiskt mål,
2. de strategiska utmaningar eller målspänningar som gör valet relevant,
3. relevanta evidensposter, styrsignaler och omvärldssignaler,
4. analyserade alternativ och trade-offs,
5. motivering till rekommenderad riktning.

Varje princip ska i sin tur kunna kopplas till minst ett vägval eller mål. En princip utan strategisk motivering ska tas bort eller behandlas som generell metodrekommendation utanför kärnstrategin.

## Säkerhet i rekommendationen

Klassificera rekommendationens säkerhet som **låg**, **måttlig** eller **hög**. Säkerheten ska påverkas av:

- evidensstyrka,
- inferensstyrka,
- hur tydligt alternativen skiljer sig,
- osäkerhet om kostnad eller kapacitet,
- externa beroenden,
- beslutets reversibilitet.

Ett svagt underlag får inte döljas bakom tvärsäker språkdräkt. Vid låg säkerhet ska verifieringsbehov eller stegvis prövning rekommenderas.

## Semantiskt kontrakt: strategic_choice

Inför schemasteget ska följande betydelse bevaras:

```yaml
strategic_choice:
  id: C-001
  title: string
  decision_theme: string
  goal_refs: [id]
  strategic_issue_refs: [id]
  governance_refs: [id]
  evidence_refs: [id]
  environment_signal_refs: [id]
  alternatives:
    - id: ALT-1
      name: string
      description: string
      advantages: [string]
      disadvantages: [string]
      risks: [string]
      prerequisites: [string]
      reversibility: low | moderate | high
  recommended_alternative_ref: id
  rationale: string
  primary_tradeoff: string
  guardrails: [string]
  exceptions: [string]
  rejected_alternatives: [id]
  verification_needs: [string]
  confidence: low | moderate | high
  horizon: short | medium | long | persistent
```

Detta är ett semantiskt kontrakt; formellt schema skapas senare.

## Semantiskt kontrakt: strategic_principle

```yaml
strategic_principle:
  id: P-001
  title: string
  statement: string
  rationale: string
  strategic_choice_refs: [id]
  goal_refs: [id]
  implications: [string]
  guardrails: [string]
  exceptions: [string]
  decision_questions: [string]
  confidence: low | moderate | high
```

Detta är ett semantiskt kontrakt; formellt schema skapas senare.

## Guardrails

- Formulera inte ett vägval utan att först identifiera vilken faktisk avvägning eller riktning som behöver beslutas.
- Presentera inte populär branschpraxis som myndighetsspecifikt vägval utan spårbar motivering.
- Rekommendera inte specifik produkt, leverantör eller molnplattform i detta steg om inte ett uttryckligt styrkrav eller ovanligt stark evidens gör produktnivån strategiskt nödvändig.
- Gör inte “cloud-first”, “AI-first”, “zero trust”, “API-first”, “plattform först”, “buy before build” eller liknande till generella defaultprinciper.
- Dölj inte betydande nackdelar eller alternativkostnader för det rekommenderade valet.
- Låt inte principer bli tekniska standarder eller detaljarkitektur.
- Hitta inte på kostnader, risknivåer eller organisatorisk kapacitet som saknar underlag.
- Låt inte låg reversibilitet kombineras med svagt underlag utan tydligt verifieringsbehov eller stegvis angreppssätt.
- Behåll målkonflikter synliga när vägvalet innebär en faktisk avvägning.

## Utdata

Fasen ska producera:

1. **Vägvalskarta** – vilka beslutsteman som behöver strategisk riktning och vilka mål de stödjer.
2. **Alternativanalys** – meningsfulla alternativ, trade-offs och förutsättningar för varje större vägval.
3. **Rekommenderade strategiska vägval** – med spårbarhet, motivering, säkerhet, guardrails och undantag.
4. **Styrande principer** – ett begränsat antal återanvändbara beslutsregler kopplade till mål och vägval.
5. **Explicita icke-val** – när det är strategiskt relevant.
6. **Öppna verifieringsbehov** – sådant som måste klarläggas innan svårreversibla val eller senare genomförande.

## Kvalitetsgrind

Steget är tillräckligt genomfört när:

- varje större vägval beskriver en verklig strategisk avvägning eller riktning,
- rekommenderade val är spårbara till mål och underlag,
- rimliga alternativ och viktigaste trade-offs är synliga,
- genomförbarhet, beroenden och reversibilitet har vägts in,
- inga produktval har smugit sig in utan explicit strategisk motivering,
- principerna är normativa, återanvändbara och inte tekniska standarder,
- principerna kan kopplas till mål eller vägval,
- målkonflikter och undantag är synliga,
- svag evidens ger lägre säkerhet och tydliga verifieringsbehov,
- vägvals- och principportföljen är tillräckligt sammanhängande för att styra nästa fas.

När grinden är passerad får nästa fas definiera **prioriterade förflyttningar och initiativområden** som översätter vägvalen till större genomförbara förändringsområden.
