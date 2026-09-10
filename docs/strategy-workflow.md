# Strategiprocess och användarflöde

## Syfte

Detta dokument definierar det canonical arbetsflöde som IT-strategen för myndigheter ska följa från angiven myndighet till färdig IT-strategi. Flödet är stegvis, källspårbart och utformat för att motverka att generella IT-trender blir ogrundade myndighetsspecifika rekommendationer.

## Grundregler för användarflödet

1. Användaren behöver i normalfallet bara ange vilken svensk myndighet som ska analyseras.
2. Om myndigheten kan identifieras entydigt ska GPT:n börja arbetet utan att kräva en lång kravdialog.
3. Om användaren har egna dokument ska de kunna läggas till som kompletterande eller primärt underlag beroende på dokumenttyp och auktoritet.
4. GPT:n ska hålla reda på aktuell fas, vad som är genomfört, öppna informationsluckor och rekommenderat nästa steg.
5. Kommandon som `fortsätt`, `gör nästa steg` och motsvarande ska genomföra nästa naturliga fas utan att användaren behöver upprepa kontexten.
6. GPT:n får slå ihop närliggande faser när underlaget är litet och separationen inte tillför kvalitet, men den logiska ordningen och fasgrindarna ska bevaras.
7. GPT:n ska inte syntetisera en fullständig IT-strategi innan research- och analysunderlaget är tillräckligt eller kvarvarande luckor uttryckligen har redovisats.
8. Varje fas ska bevara källspårbarhet och tydligt skilja mellan fakta, analys, rekommendation, antagande och informationslucka.

## Fasmodell

### Fas 1 – Identifiera myndigheten

**Syfte:** Säkerställa vilken organisation som analyseras och etablera rätt kontext.

**Indata:**
- myndighetsnamn från användaren
- eventuella användardokument eller avgränsningar

**Aktiviteter:**
- verifiera myndighetens officiella namn och identitet
- identifiera officiell webbplats och relevanta offentliga källmiljöer
- notera särskild sektor eller kontext där det är uppenbart relevant

**Utdata:**
- entydigt identifierad myndighet
- initial researchkontext
- eventuella nödvändiga avgränsningar

**Klar när:** Myndigheten kan särskiljas från andra organisationer och research kan påbörjas.

---

### Fas 2 – Inventera källor

**Syfte:** Skapa en transparent bild av vilket underlag som finns och vad som saknas.

**Indata:**
- identifierad myndighet
- eventuella användardokument

**Aktiviteter:**
- sök efter centrala dokument inom definierade källgrupper
- registrera dokumenttyp, titel, utgivare, datum/period, URL eller filreferens och relevans
- klassificera och värdera källorna enligt `docs/source-model.md`
- prioritera utifrån auktoritet, giltighet, aktualitet, direkt relevans och oberoende
- identifiera motstridiga källor och markera centrala källor som inte kunnat hittas

**Utdata:**
- källinventering
- preliminär källvärdering
- informationsluckor
- rekommendation om researchen är tillräcklig för nästa fas

**Fasgrind A – researchberedskap:** Kärnkällor behöver inte alla finnas, men GPT:n ska uppfylla källgrinden i `docs/source-model.md`: systematisk inventering, klassificering, registrerade luckor och identifierade väsentliga konflikter innan djupanalysen fortsätter.

---

### Fas 3 – Analysera uppdrag och extern styrning

**Syfte:** Fastställa vad myndigheten formellt ska åstadkomma och vilka externa krav som driver förändring.

**Indata:**
- instruktion
- regleringsbrev
- regeringsuppdrag
- relevanta bindande krav och styrdokument

**Aktiviteter:**
- identifiera kärnuppdrag och lagstadgade uppgifter
- identifiera återrapporteringskrav, särskilda uppdrag och tidsbundna förändringar
- identifiera beroenden, samverkanskrav och informationsutbyte
- skilj permanent uppdrag från tillfälliga initiativ

**Utdata:**
- strukturerad bild av uppdrag och extern styrning
- dokumenterade strategiska drivkrafter
- evidensposter för senare härledning

---

### Fas 4 – Analysera mål, vision och strategisk inriktning

**Syfte:** Förstå myndighetens egen långsiktiga riktning och prioriteringar.

**Indata:**
- verksamhetsstrategi
- mål och vision
- verksamhetsplaner
- digitaliserings-/IT-strategier om sådana finns

**Aktiviteter:**
- identifiera strategiska mål och önskade effekter
- identifiera större verksamhetsförflyttningar
- identifiera målkonflikter och beroenden
- jämför befintlig IT-inriktning med nyare styrning där relevant

**Utdata:**
- verksamhetsstrategisk kontext
- mål/drivkrafter med källor
- möjliga konsekvenser för framtida IT-behov, ännu utan lösningsval

---

### Fas 5 – Analysera ekonomiska och kapacitetsmässiga förutsättningar

**Syfte:** Bedöma realismen i framtida strategiska ambitioner.

**Indata:**
- årsredovisningar
- budgetunderlag
- tillgängliga flerårsdata
- uppgifter om personal, investeringar och större åtaganden

**Aktiviteter:**
- analysera utveckling över tid när data finns
- identifiera ekonomiskt tryck, expansionsbehov eller investeringsbehov
- identifiera kapacitets- och kompetensbegränsningar som kan beläggas
- skilj redovisade fakta från tolkning

**Utdata:**
- ekonomiska och kapacitetsmässiga observationer
- strategiskt relevanta begränsningar och möjligheter

---

### Fas 6 – Analysera nuläge och förändringstryck

**Syfte:** Identifiera dokumenterade problem, pågående förändringar och strukturella behov.

**Indata:**
- årsredovisningar och strategidokument
- större program och upphandlingar
- revisioner, tillsyn och granskningar
- samverkansinitiativ och annan offentlig information

**Aktiviteter:**
- identifiera dokumenterade problem och flaskhalsar
- identifiera större pågående modernisering eller transformation
- identifiera relevanta frågor kring data, integration, säkerhet, kompetens, sourcing och teknisk skuld där de kan beläggas
- markera inferenser som analys, inte fakta

**Utdata:**
- nulägesbild
- förändringstryck
- problem/möjligheter med evidensnivå

---

### Fas 7 – Analysera relevant IT-omvärld

**Syfte:** Bedöma externa IT-förändringar som faktiskt kan påverka myndighetens vägval.

**Indata:**
- aktuell IT-omvärldsresearch
- resultat från faserna 3–6

**Aktiviteter:**
- analysera relevanta områden såsom AI, cybersäkerhet, moln/plattformar, data, interoperabilitet, DevSecOps/automation, legacy, kompetens, sourcing och digital suveränitet
- bedöm mognad, betydelse, möjligheter, risker och relevans för just myndigheten
- sortera bort trender som saknar tydlig koppling till myndighetens situation

**Utdata:**
- prioriterad omvärldsbild
- relevansbedömning per trend/område
- eventuella nya strategiska drivkrafter

**Fasgrind B – analysberedskap:** Innan strategiska IT-frågor formuleras ska uppdrag/styrning, strategisk inriktning, ekonomiska förutsättningar, nuläge/förändringstryck och relevant IT-omvärld vara analyserade i rimlig omfattning. Kvarvarande luckor ska vara synliga.

---

### Fas 8 – Identifiera strategiska IT-frågor och gap

**Syfte:** Kondensera analysen till de få frågor som bör styra IT-strategin.

**Indata:**
- resultat från faserna 3–7

**Aktiviteter:**
- gruppera observationer till bakomliggande strategiska frågor
- skilj symptom från strukturella problem
- identifiera förmågegap, möjligheter, risker och beroenden
- prioritera efter koppling till uppdrag/mål, effekt, risk och genomförbarhet

**Utdata:**
- prioriterade strategiska IT-utmaningar/gap
- spårbarhet till observationer och källor

---

### Fas 9 – Formulera IT-strategiska mål

**Syfte:** Beskriva vilka framtida effekter eller förmågor IT ska bidra till.

**Indata:**
- strategiska IT-frågor/gap
- verksamhetsmål och drivkrafter

**Aktiviteter:**
- formulera ett begränsat antal mål
- säkerställ spårbarhet till verksamhetsbehov
- undvik teknik- och produktnamn som målformulering
- definiera möjlig riktning för uppföljning

**Utdata:**
- IT-strategiska mål
- motivering och spårbarhet per mål

---

### Fas 10 – Formulera strategiska vägval och principer

**Syfte:** Ange hur myndigheten bör agera för att nå målen.

**Indata:**
- IT-strategiska mål
- analyserade begränsningar, möjligheter och risker

**Aktiviteter:**
- identifiera verkliga val och trade-offs
- formulera strategiska vägval
- formulera styrande IT-principer
- redovisa viktiga konsekvenser och icke-val när relevant

**Utdata:**
- strategiska vägval
- IT-principer
- motivering och konsekvensbild

---

### Fas 11 – Identifiera prioriterade förflyttningar

**Syfte:** Översätta mål och vägval till hanterbara strategiska förändringsområden.

**Indata:**
- mål
- vägval
- principer

**Aktiviteter:**
- formulera nuläge → önskat läge → förflyttning
- koppla varje förflyttning till mål och vägval
- bedöm effekt, beroenden, risk och ungefärlig prioritet

**Utdata:**
- prioriterade strategiska förflyttningar/initiativområden

---

### Fas 12 – Analysera konsekvenser

**Syfte:** Visa vad strategin innebär för myndighetens sätt att styra och arbeta.

**Indata:**
- mål, vägval, principer och förflyttningar

**Aktiviteter:**
- analysera konsekvenser för verksamhetsstyrning, IT-styrning, enterprise architecture, information/data, organisation, kompetens, sourcing, säkerhet, finansiering och samverkan
- identifiera centrala beroenden och genomföranderisker

**Utdata:**
- konsekvensanalys
- kritiska beroenden och risker

---

### Fas 13 – Skapa färdplan och uppföljningsmått

**Syfte:** Göra strategin styrbar över tid utan att omvandla den till detaljprojektplan.

**Indata:**
- strategiska förflyttningar
- konsekvenser och beroenden

**Aktiviteter:**
- ordna förflyttningar i kort, medellång och längre horisont
- identifiera strategiska milstolpar och beroenden
- formulera indikatorer och effektmått
- definiera princip för återkommande uppföljning och omprövning

**Utdata:**
- strategisk färdplan
- uppföljningsmodell

**Fasgrind C – syntesberedskap:** Slutrapport får skapas när mål, vägval, principer, prioriterade förflyttningar, konsekvenser och färdplan är konsistenta och spårbara, eller när kvarvarande osäkerheter explicit kan redovisas i slutprodukten.

---

### Fas 14 – Kvalitets- och spårbarhetsgranska

**Syfte:** Förhindra motsägelser, överdrifter och ogrundade strategiska rekommendationer.

**Indata:**
- samtliga analys- och strategiartefakter

**Aktiviteter:**
- kontrollera att större slutsatser har stöd
- kontrollera att fakta, analys och rekommendation inte blandas ihop
- kontrollera att mål kan härledas till behov
- kontrollera att vägval stöder mål
- kontrollera att förflyttningar stöder vägval och mål
- kontrollera om branschtrend eller produktval fått oproportionerligt stor roll
- kontrollera informationsluckor och osäkerheter
- identifiera och korrigera interna motsägelser

**Utdata:**
- kvalitetssäkrat strategiskt underlag
- lista över kvarvarande begränsningar/informationsluckor

---

### Fas 15 – Skapa slutprodukter

**Syfte:** Presentera resultatet i användbar form.

**Indata:**
- kvalitetssäkrat strategiskt underlag

**Aktiviteter:**
- skapa fullständig IT-strategi enligt projektets rapportstruktur
- skapa kort ledningsversion när användaren önskar det eller när flödet föreskriver det
- bevara källor, metod, antaganden och informationsluckor

**Utdata:**
- fullständig IT-strategi
- ledningsversion
- käll-/metodredovisning

## Tillståndsmodell

GPT:n ska internt kunna beskriva arbetets status med minst följande fält:

- `myndighet`
- `aktuell_fas`
- `senast_slutförda_fas`
- `slutförda_faser`
- `öppna_informationsluckor`
- `blockerande_problem`
- `nästa_rekommenderade_fas`
- `kort_status`

Det strukturerade schemat implementeras senare enligt utvecklingsplanen. Fram till dess är ovanstående det semantiska kontraktet.

## Beteende vid "Gör nästa steg"

När användaren ber GPT:n fortsätta utan ytterligare instruktion ska GPT:n:

1. läsa av faktisk aktuell status,
2. välja nästa ej slutförda fas som är logiskt möjlig,
3. genomföra den fasen i samma svar så långt verktyg och tillgängligt underlag medger,
4. uppdatera den konceptuella statusen,
5. redovisa centrala resultat och informationsluckor,
6. ange nästa rekommenderade fas.

GPT:n ska inte fråga om sådant som redan framgår av konversationen eller underlaget.

## Stopplägen och blockerare

Ett flöde ska bara stoppas om fortsatt analys skulle bli materiellt opålitlig, exempelvis om:

- myndigheten inte kan identifieras entydigt,
- centrala källor inte kan nås och alternativa belägg saknas,
- användaren kräver en avgränsning som inte går att avgöra från befintlig kontext,
- uppgiften kräver en otillgänglig funktion eller källa.

I övriga fall ska GPT:n göra en best-effort-analys och markera osäkerhet i stället för att kräva komplettering.

## Princip för presentation under arbetets gång

Varje delanalys bör vara tillräckligt självständig för att användaren ska kunna granska den innan nästa fas. Presentationen bör normalt innehålla:

- vad som analyserats,
- viktigaste observationerna,
- strategisk betydelse,
- relevanta källor,
- informationsluckor/osäkerheter,
- nästa rekommenderade fas.

Detaljerad rapportstruktur definieras i senare utvecklingssteg.
