# Ekonomisk och kapacitetsmässig analys

## Syfte

Den ekonomiska och kapacitetsmässiga analysen ska bedöma vilka strategiska ambitionsnivåer som är realistiska utifrån myndighetens finansiering, kostnadsutveckling, personal, investeringsförmåga och genomförandekapacitet. Analysen ska stödja prioritering och sekvensering, inte fungera som en detaljerad budgetmodell.

## Grundprinciper

- Analysera flerårig utveckling när jämförbara data finns. Enskilda år får inte ensamma bära strukturella slutsatser.
- Skilj mellan redovisade fakta, beräknade förändringar och analytiska tolkningar.
- Beakta förändringar i uppdrag, redovisningsprinciper och organisationsstruktur innan tidsserier jämförs.
- Nominella belopp ska inte automatiskt tolkas som real resursförstärkning. Inflation, löneutveckling och prisökningar kan behöva vägas in kvalitativt när de är materiella.
- Budgetutrymme och genomförandekapacitet är olika saker. Finansiering utan tillräcklig kompetens, styrning eller leveranskapacitet kan fortfarande vara en begränsning.
- Frånvaro av offentlig kostnadsdata ska redovisas som informationslucka, inte ersättas med antagna IT-kostnader.
- Dra inte slutsatsen att en myndighet är ineffektiv enbart från kostnadsökningar. Koppla alltid utvecklingen till uppdrag, volymer, kvalitet, säkerhet och förändringskrav när sådana data finns.

## Analysområden

### 1. Finansiering och anslagsutveckling

Identifiera när möjligt:

- anslag och andra väsentliga finansieringskällor,
- flerårig utveckling i tilldelade och förbrukade medel,
- tillfälliga respektive varaktiga förstärkningar,
- särskilt finansierade regeringsuppdrag eller program,
- ofinansierade eller delvis finansierade uppdrag,
- anslagssparande, anslagskredit eller andra relevanta budgetsignaler.

Bedöm vilka delar som faktiskt påverkar handlingsutrymmet för strategiska IT-förflyttningar.

### 2. Kostnadsutveckling

Analysera relevanta kostnadsslag när de är offentligt tillgängliga, exempelvis:

- personalkostnader,
- lokaler och övrig drift,
- konsult- och tjänsteköp,
- IT-drift och utveckling när de särredovisas,
- avskrivningar och investeringar,
- större program eller transformationskostnader.

Identifiera trendbrott och möjliga förklaringar men skilj uttryckligen mellan belagda orsaker och hypoteser.

### 3. Personal och kompetens

Analysera när data finns:

- antal årsarbetskrafter eller anställda över tid,
- tillväxt eller minskning i relevanta kompetensgrupper,
- pensionsavgångar och rekryteringssvårigheter,
- beroende av konsulter eller leverantörer,
- dokumenterade kompetensgap,
- förmåga att attrahera, utveckla och behålla digital kompetens.

Det är inte tillräckligt att räkna personer. Bedöm även om kompetensmixen stödjer de strategiska förflyttningarna.

### 4. Investeringar och förändringsportfölj

Identifiera större investeringar, moderniseringsprogram och utvecklingsinitiativ. Bedöm:

- hur stor förändringsbörda myndigheten redan bär,
- om flera initiativ konkurrerar om samma kompetens eller styrkapacitet,
- om investeringar skapar framtida drift- och förvaltningskostnader,
- om finansieringen är engångsbaserad eller långsiktigt hållbar.

Undvik att behandla investeringsutgift och varaktig förmåga som samma sak.

### 5. Besparings- och effektiviseringskrav

Identifiera uttryckliga eller indirekta effektiviseringskrav, exempelvis minskad finansiering, nya uppdrag utan motsvarande resurstillskott eller krav på högre produktivitet.

Analysera hur dessa krav påverkar:

- möjlighet till parallella initiativ,
- behov av standardisering och återanvändning,
- tolerans för teknisk skuld,
- sourcing och kompetensförsörjning,
- prioritering mellan stabilitet, modernisering och ny funktionalitet.

Effektivisering får inte automatiskt översättas till personalminskning eller outsourcing. Sådana vägval kräver separat evidens.

### 6. Genomförandekapacitet

Bedöm den samlade förmågan att omsätta strategi i förändring. Minst följande dimensioner ska beaktas när underlag finns:

- finansiering,
- tillgänglig intern kompetens,
- lednings- och styrkapacitet,
- arkitektur- och portföljstyrning,
- upphandlings- och leverantörskapacitet,
- förändringsledning,
- beroenden till andra myndigheter eller gemensamma infrastrukturer,
- mängden samtidiga större initiativ.

Klassificera kapacitetsbegränsningar som exempelvis **låg**, **måttlig** eller **hög påverkan** och motivera bedömningen kvalitativt.

## Analys över tid

När minst tre jämförbara år finns bör GPT:n normalt söka efter riktning snarare än enskilda differenser:

- stabil,
- gradvis ökande,
- gradvis minskande,
- volatil,
- tydligt trendbrott.

Förklara alltid om jämförbarheten är svag. Belopp från olika dokument ska inte kombineras som om definitionerna vore identiska utan kontroll.

## Koppling till strategi

Resultatet ska inte vara en lista av ekonomiska nyckeltal. Varje materiell observation ska vid behov kopplas till en strategisk konsekvens, exempelvis:

- begränsat varaktigt finansieringsutrymme → behov av hårdare prioritering och återanvändning,
- hög förändringsbelastning → sekvensering och färre samtidiga strategiska initiativ,
- dokumenterade kompetensgap → kompetensförsörjning blir en strategisk möjliggörare,
- stort konsultberoende i kritiska områden → behov av analys av långsiktig intern beställar- och ägarförmåga,
- stora engångsinvesteringar → krav på plan för långsiktig förvaltning och driftsfinansiering.

Dessa är exempel på härledningsmönster, inte förhandsbestämda slutsatser.

## Semantiskt kontrakt – economic_capacity_observation

Varje betydande ekonomisk eller kapacitetsmässig observation bör kunna representeras med:

- `id`
- `category`
- `statement`
- `period`
- `value_or_direction`
- `source_refs`
- `comparability`
- `fact_or_analysis`
- `strategic_relevance`
- `capacity_impact`
- `uncertainty`

Detta är ett semantiskt kontrakt. Formellt schema införs i senare schemasteg.

## Kvalitetsgrind

Fasen är tillräckligt genomförd när:

1. väsentlig finansierings- och kostnadsutveckling är analyserad i den utsträckning data finns,
2. personal- och kompetensförutsättningar är bedömda,
3. större investeringar och samtidiga förändringsåtaganden är identifierade,
4. besparings- eller effektiviseringstryck är synliggjort,
5. strategiska ambitionsnivåer har prövats mot genomförandekapacitet,
6. fleråriga slutsatser bygger på jämförbara data eller har tydlig reservation,
7. fakta, beräkningar, tolkningar och informationsluckor är åtskilda,
8. inga specifika teknik- eller sourcingval har smugit sig in utan separat analysunderlag.

Om offentlig ekonomisk information är begränsad ska GPT:n fortsätta best effort och ange vilka slutsatser som därför har låg säkerhet.
