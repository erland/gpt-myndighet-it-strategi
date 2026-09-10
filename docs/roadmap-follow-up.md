# Färdplan och uppföljning

## Syfte

Färdplanen omsätter IT-strategins mål, vägval, principer, prioriterade förflyttningar och konsekvensanalys till en begriplig genomföranderiktning över tid. Den ska visa **vad som behöver ske först, vad som kan ske parallellt, vilka beroenden som styr ordningen och hur strategisk effekt ska följas upp**, utan att förvandlas till en detaljerad projektplan.

Uppföljningen ska både visa om strategins förflyttningar faktiskt genomförs och om de leder till avsedd verksamhets- och IT-effekt. Den ska också skapa en explicit mekanism för att ompröva strategin när förutsättningarna ändras.

## Grundregel

För varje prioriterad förflyttning ska GPT:n kunna svara på:

> **När behöver förflyttningen huvudsakligen ske, vad måste vara på plats före eller samtidigt, vilken strategisk milstolpe visar att förflyttningen har nått ett meningsfullt läge och hur kan vi följa både genomförande och effekt?**

Färdplanen ska vara tillräckligt konkret för ledning och styrning men inte låtsas vara en beslutad projektplan när sådant underlag saknas.

## Indata

Använd i första hand:

- prioriterade `it_strategic_goal`,
- `strategic_choice` och `strategic_principle`,
- prioriterade `strategic_transformation`,
- möjliggörande och effektorienterade förflyttningar,
- `strategic_consequence`, särskilt kritiska/höga konsekvenser,
- kända beroenden och externa beslut,
- ekonomisk och kapacitetsmässig analys,
- risker, informationsluckor och verifieringsbehov,
- befintliga program och initiativ som påverkar sekvenseringen.

## Strategiska tidshorisonter

Använd normalt tre strategiska horisonter när exakt planeringsunderlag saknas:

1. **Nära sikt** – etablera kritiska förutsättningar, hantera tidskritiska krav och påbörja högprioriterade förflyttningar.
2. **Medellång sikt** – skala, konsolidera och realisera större delar av målbilden när möjliggörare finns på plats.
3. **Längre sikt** – fullfölja strukturella förflyttningar, optimera målbilden och hantera beroenden med längre ledtid.

Använd **kontinuerlig** för sådant som inte har ett naturligt slutläge, exempelvis kompetensförsörjning, säkerhetsförbättring, arkitekturstyrning eller omvärldsbevakning när det är relevant.

Exakta kalenderår, kvartal eller leveransdatum får bara anges när de kan härledas från beslutade deadlines, kända program eller annat tillförlitligt planeringsunderlag. Hitta inte på precision för att göra färdplanen visuellt komplett.

## Sekvensering och beroenden

Sekvenseringen ska härledas, inte bara följa prioriteringsordningen. Bedöm minst:

- **hårda beroenden** – en förflyttning kan inte rimligen genomföras före en annan,
- **mjuka beroenden** – en föregående förflyttning förbättrar sannolikheten, kvaliteten eller tempot,
- **externa beroenden** – annan myndighet, regeringsbeslut, EU-tidslinje, gemensam tjänst eller leverantör,
- **kapacitetsberoenden** – samma knappa kompetens eller styrkapacitet behövs på flera ställen,
- **informations-/databeroenden** – dataägarskap, informationsmodell eller datakvalitet måste etableras,
- **arkitektur-/plattformsberoenden** – gemensamma förutsättningar som måste finnas innan flera effekter kan realiseras,
- **finansieringsberoenden** – investering eller flerårig finansiering krävs före nästa steg,
- **övergångsberoenden** – migration, dubbel drift, avtal eller livscykel skapar ordningskrav.

Skilj mellan **strategisk prioritet** och **sekvenseringsordning**. En förflyttning kan vara högst prioriterad men ändå ligga senare i genomförandet därför att en möjliggörande förflyttning måste ske först.

## Parallellisering och kapacitetsrealism

Identifiera vilka förflyttningar som kan ske parallellt, men kontrollera att parallellisering inte överskrider dokumenterad eller rimligt bedömd kapacitet.

Var särskilt vaksam på:

- samma nyckelkompetens i flera samtidiga förflyttningar,
- många samtidiga migrations- eller förändringsbelastningar,
- samma beslutsforum eller arkitekturfunktion som flaskhals,
- upphandlings- och leverantörskapacitet,
- verksamhetens mottagningsförmåga,
- säkerhets- och informationsklassningsarbete som måste hinna med.

Om kapaciteten är osäker ska färdplanen uttrycka antagandet och föreslå verifiering i stället för att anta obegränsad parallellitet.

## Strategiska milstolpar

Milstolpar ska beskriva **meningsfulla strategiska tillstånd**, inte administrativa aktiviteter. En bra milstolpe visar att en förmåga, styrmodell, standardiserad arbetssätt eller annan central förutsättning faktiskt är etablerad eller uppnådd.

Exempel på rätt abstraktionsnivå:

- gemensam styrmodell för ett tvärgående område är etablerad och används,
- prioriterade informationsutbyten följer beslutad gemensam modell,
- en kritisk legacy-beroendekategori har en beslutad och finansierad livscykelstrategi,
- en gemensam plattformsförmåga kan användas av flera verksamhetsområden,
- effektuppföljning för ett strategiskt mål är etablerad med verifierad baslinje.

Undvik milstolpar som bara säger att ett dokument är skrivet, ett projekt är startat eller en produkt är installerad, om det inte i sig representerar den strategiska effekten.

## Uppföljningsmodell

Uppföljningen ska skilja minst mellan fyra typer av mått:

### 1. Effektindikatorer

Visar om strategiska mål och önskade verksamhets-/IT-effekter närmar sig uppfyllelse. De ska så långt möjligt kopplas direkt till `it_strategic_goal`.

### 2. Förmåge-/mognadsindikatorer

Visar om den avsedda framtida förmågan etableras, exempelvis standardisering, återanvändning, dataförmåga, leveransförmåga eller robusthet.

### 3. Genomförandeindikatorer

Visar om prioriterade förflyttningar och strategiska milstolpar går framåt. Dessa är ledande indikatorer men får inte ersätta effektmått.

### 4. Risk- och beroendeindikatorer

Visar om kritiska risker, informationsluckor, externa beroenden eller kapacitetsbegränsningar förändras på ett sätt som kräver styrning eller omprövning.

Undvik aktivitetsmått som saknar tydlig koppling till effekt. Antal projekt, antal workshops, antal AI-piloter eller antal migrerade system är inte automatiskt bra strategimått.

## Baslinjer och målvärden

Hitta inte på baslinjer, procentsatser eller målärden. Om underlaget saknar baslinje ska GPT:n:

1. föreslå vad som bör mätas,
2. markera att baslinje saknas,
3. rekommendera att baslinjen fastställs i första uppföljningscykeln,
4. avstå från falskt precisa målvärden tills data finns.

När beslutade mål eller lagkrav innehåller verkliga trösklar eller deadlines får dessa naturligtvis användas och källspåras.

## Ledande och släpande indikatorer

För strategiskt viktiga mål bör GPT:n när möjligt kombinera:

- **ledande indikatorer** – visar om förutsättningar och beteenden förändras i rätt riktning,
- **släpande indikatorer** – visar om faktisk effekt har uppstått.

Exempel: etablerad gemensam leveransförmåga kan vara en ledande indikator, medan kortare verifierad ledtid från behov till produktionssatt förändring kan vara en släpande effektindikator. Båda kräver dock relevant underlag och korrekt definition.

## Uppföljningscykel

Rekommendera en återkommande styrningscykel med tre nivåer:

1. **Löpande operativ uppföljning** av risker, beroenden och genomförandesignaler i ordinarie styrning.
2. **Periodisk strategisk uppföljning** där mål, indikatorer, milstolpar, förflyttningar och konsekvenser bedöms samlat.
3. **Strategisk omprövning** när större förändringar i styrning, ekonomi, uppdrag, tekniklandskap, säkerhetsläge eller externa beroenden gör den tidigare riktningen osäker.

Ange inte en exakt mötesfrekvens som universell regel. Anpassa periodiciteten till myndighetens styrmodell och förändringstakt. Som princip ska uppföljningen vara tillräckligt tät för att upptäcka avvikelser innan de blir strukturella men inte skapa separat rapporteringsbyråkrati utan nytta.

## Omprövningstriggers

Strategin ska inte behandlas som statisk fram till ett kalenderbestämt slutdatum. Definiera triggers som kan motivera tidigare omprövning, exempelvis:

- ändrad instruktion, regleringsbrev eller större regeringsuppdrag,
- väsentligt ändrad finansiering eller besparingskrav,
- större säkerhets- eller beredskapsförändring,
- ny lagstiftning eller EU-reglering med betydande IT-påverkan,
- strategiskt teknikskifte vars relevans för myndigheten har förändrats,
- väsentlig försening eller utebliven effekt i kritisk förflyttning,
- nytt beroende eller leverantörsrisk,
- organisationsförändring eller kraftigt ändrad kompetens-/kapacitetsbild,
- evidens som visar att ett centralt antagande varit fel.

Vid trigger ska GPT:n inte automatiskt kasta hela strategin. Bedöm vilket lager som påverkas: mål, vägval, princip, förflyttning, sekvensering, indikator eller antagande.

## Semantiskt kontrakt: `roadmap_item`

Ett framtida strukturerat objekt bör minst kunna bära:

- `id`
- `title`
- `transformation_refs`
- `goal_refs`
- `horizon`
- `strategic_priority`
- `sequence_position`
- `hard_dependencies`
- `soft_dependencies`
- `external_dependencies`
- `capacity_constraints`
- `milestones`
- `risks`
- `assumptions`
- `uncertainties`
- `evidence_refs`
- `readiness_conditions`

## Semantiskt kontrakt: `strategy_indicator`

Ett framtida strukturerat objekt bör minst kunna bära:

- `id`
- `title`
- `indicator_type`
- `goal_refs`
- `transformation_refs`
- `definition`
- `strategic_rationale`
- `direction_of_improvement`
- `baseline`
- `target`
- `measurement_source`
- `cadence`
- `owner_role`
- `evidence_refs`
- `assumptions`
- `uncertainties`

`baseline` och `target` får uttryckligen vara `unknown`/saknas tills verifierad data finns.

## Semantiskt kontrakt: `strategy_review_trigger`

Ett framtida strukturerat objekt bör minst kunna bära:

- `id`
- `trigger_type`
- `description`
- `affected_goal_refs`
- `affected_choice_refs`
- `affected_transformation_refs`
- `evidence_refs`
- `recommended_review_scope`

## Spårbarhetskrav

Varje större färdplanspost ska kunna kopplas till:

- minst en prioriterad förflyttning,
- relevant strategiskt mål,
- de beroenden eller konsekvenser som motiverar horisont och sekvensering,
- underliggande evidens eller explicit antagande där ordningen inte är direkt belagd.

Varje effektindikator ska kunna kopplas till minst ett strategiskt mål. Varje genomförandeindikator ska kunna kopplas till en förflyttning eller strategisk milstolpe. Risk-/beroendeindikatorer ska kopplas till identifierad risk, konsekvens eller informationslucka.

## Guardrails

GPT:n får inte:

- göra färdplanen till en detaljerad projektplan utan beslutsunderlag,
- hitta på kvartal, datum, budget, bemanning eller projektnamn,
- anta att strategisk prioritet automatiskt anger startordning,
- använda aktivitetsmått som ersättning för effektmått,
- hitta på baslinjer, procentmål eller nyckeltal,
- föreslå en stor mängd indikatorer bara för att allt går att mäta,
- anta att en förflyttning är klar bara för att ett system är installerat eller ett dokument beslutat,
- låsa uppföljningen till en ny separat styrmodell om ordinarie styrning kan användas,
- behandla strategin som statisk när kritiska antaganden eller förutsättningar förändras.

## Kvalitetsgrind

Färdplan och uppföljning är tillräckligt definierade när:

- alla prioriterade förflyttningar har en motiverad strategisk horisont eller kontinuerlig behandling,
- hårda, mjuka, externa och kapacitetsmässiga beroenden är synliga där de är materiella,
- prioritet och sekvensering hålls isär,
- parallellisering är prövad mot kapacitet,
- strategiska milstolpar beskriver meningsfulla tillstånd snarare än enbart aktiviteter,
- varje strategiskt mål har minst en rimlig uppföljningsväg eller ett tydligt mätgap,
- effekt-, förmåge-, genomförande- och riskindikatorer hålls isär,
- baslinjer och målvärden inte är fabricerade,
- en periodisk uppföljningscykel och relevanta omprövningstriggers är definierade,
- roadmap och indikatorer är spårbara till strategi och evidens,
- resultatet kan användas som indata till slutrapporten utan att ge sken av detaljplanering.

## Utdata

Leverera normalt:

1. en kort beskrivning av genomförandelogiken,
2. en strategisk färdplan per tidshorisont,
3. en beroende- och sekvenseringsbild,
4. strategiska milstolpar,
5. ett begränsat uppföljningsramverk per mål,
6. kritiska risk-/beroendeindikatorer,
7. uppföljningscykel och ansvar på rollnivå när det kan motiveras,
8. omprövningstriggers,
9. öppna baslinje- och informationsluckor.
