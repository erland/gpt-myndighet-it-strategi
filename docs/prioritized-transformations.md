# Prioriterade förflyttningar och initiativområden

## Syfte

Detta steg översätter IT-strategiska mål, strategiska vägval och principer till ett **begränsat antal större strategiska förflyttningar** som beskriver hur myndigheten behöver förändras över tid. Förflyttningarna ska vara konkreta nog för att kunna styra portfölj, arkitektur och verksamhetsplanering men tillräckligt övergripande för att inte bli en detaljerad projektlista.

En förflyttning beskriver en riktad förändring från ett relevant nuläge till ett önskat läge och ska kunna kopplas till strategisk effekt, beroenden, risker och ungefärlig tidshorisont.

## Grundregel

En strategisk förflyttning ska svara på frågan:

> **Vilken större förändring behöver myndigheten genomföra för att omsätta de valda strategiska målen och vägvalen i faktisk förmåga och effekt?**

Ett initiativområde ska svara på:

> **Vilket sammanhållet arbetsområde kan bära eller möjliggöra denna förflyttning utan att vi ännu låser den till ett specifikt projekt, system eller produktval?**

Förflyttningar ska alltså ligga mellan strategi och genomförande. De är mer konkreta än mål och vägval men mindre detaljerade än projekt, program, epics, upphandlingar eller tekniska implementationer.

## Indata

Använd i första hand:

- prioriterade `it_strategic_goal`-objekt,
- `strategic_choice` och `strategic_principle`,
- prioriterade `strategic_issue`-objekt,
- relevanta nulägesobservationer och förändringstryck,
- ekonomiska och kapacitetsmässiga begränsningar,
- befintliga initiativ och tillgångar,
- viktiga beroenden och målkonflikter,
- evidens och uttryckliga informationsluckor.

## Arbetsordning

Arbeta i följande ordning:

1. **Identifiera förändringsbehov.** Härled vilka större tillståndsförändringar som krävs för att nå målen och realisera vägvalen.
2. **Beskriv relevant nuläge.** Sammanfatta endast det nuläge som behövs för att förstå förflyttningen och markera osäkerhet där offentlig evidens saknas.
3. **Formulera önskat läge.** Beskriv vilket framtida förmåge- eller arbetssättsläge myndigheten ska ha uppnått.
4. **Formulera själva förflyttningen.** Skriv den som en riktning från nuläge till önskat läge, inte som en aktivitet eller produktinstallation.
5. **Koppla strategisk effekt.** Ange vilka mål, vägval och strategiska frågor som förflyttningen adresserar.
6. **Identifiera möjliggörande initiativområden.** Beskriv större arbetsområden som kan realisera förflyttningen utan att göra en detaljerad portfölj.
7. **Identifiera beroenden.** Synliggör organisatoriska, informationsmässiga, arkitekturella, kompetensmässiga, juridiska, säkerhetsmässiga och externa beroenden.
8. **Identifiera risker och hinder.** Beskriv vad som kan försvåra eller fördröja förflyttningen.
9. **Bedöm genomförbarhet och prioritet.** Väg strategisk betydelse mot kapacitet, tidskritikalitet och beroenden.
10. **Placera i tid.** Ange ungefärlig strategisk tidshorisont, inte exakta projektplaner när underlag saknas.
11. **Pröva portföljen.** Konsolidera överlapp, synliggör sekvensering och kontrollera att antalet förflyttningar är styrbart.

## Från nuläge till önskat läge

Varje större förflyttning ska så långt underlaget medger beskrivas i formen:

**Nuläge → önskat läge → strategisk förflyttning → effekt → beroenden → risker → prioritet → tidshorisont**

Exempel på rätt abstraktionsnivå:

> **Nuläge:** Informationsutbyte realiseras genom flera lokala integrationsmönster och återkommande specialanpassningar.
> **Önskat läge:** Myndigheten kan etablera och ändra informationsutbyte genom gemensamma, säkra och återanvändbara kontrakt och integrationsförmågor.
> **Förflyttning:** Från lokalt och punktvis integrationsarbete till gemensamt styrd interoperabilitet och återanvändbara informations- och integrationsmönster.

Detta är bättre än:

> Inför en API management-produkt och migrera 40 integrationer.

Den senare formuleringen är ett möjligt initiativ eller en genomförandeplan och kräver separat lösningsanalys.

## Typer av förflyttningar

Förflyttningar kan bland annat avse:

- styrning och beslutsförmåga,
- arkitektur och standardisering,
- informations- och dataförmåga,
- interoperabilitet och informationsutbyte,
- utvecklings- och leveransförmåga,
- gemensamma plattformstjänster,
- säkerhet och robusthet,
- livscykelhantering och teknisk skuld,
- kompetens och arbetsformer,
- sourcing och leverantörsstyrning,
- automatisering och AI-förmåga,
- samverkan och gemensamma offentliga förmågor.

Kategorierna är analysstöd och ska inte tvinga fram förflyttningar där underlaget inte visar ett relevant behov.

## Initiativområden

Ett initiativområde är ett **sammanhållet genomförandeområde**, inte automatiskt ett beslutat projekt. Det kan innehålla flera framtida initiativ och kan behöva brytas ned i ordinarie portfölj- eller verksamhetsplanering.

Bra exempel:

- etablera gemensam informations- och integrationsstyrning,
- stärka plattforms- och produktorienterad leveransförmåga där den strategiska analysen motiverar det,
- skapa systematisk livscykel- och teknikskuldshantering,
- utveckla myndighetsgemensam dataförmåga,
- etablera kontrollerad AI-förmåga för prioriterade användningsområden,
- förstärka kontinuitets- och robusthetsförmåga för kritiska digitala tjänster.

Mindre lämpligt på denna nivå:

- köp produkt X,
- inför Kubernetes-kluster Y,
- rekrytera exakt 12 utvecklare,
- migrera system A under kvartal 2,
- skapa projekt Z med specificerad budget.

Sådana beslut kan senare följa av strategin men kräver eget besluts- och planeringsunderlag.

## Strategisk effekt

Varje förflyttning ska beskriva **varför förändringen spelar roll**. Effekten ska kunna kopplas till minst ett IT-strategiskt mål och helst även till relevanta verksamhetsmål eller styrkrav.

Effekt kan exempelvis uttryckas som:

- kortare ledtid för verksamhetsförändring,
- högre kvalitet eller tillgänglighet,
- förbättrad informationsdelning,
- lägre strategisk risk,
- bättre säkerhet eller robusthet,
- minskad duplicering,
- bättre kostnadskontroll,
- ökad handlingsfrihet,
- bättre förmåga att möta nya regelkrav,
- ökad återanvändning och skalfördel.

Påhittade numeriska effekter får inte användas. Om mätbar effekt är viktig men baslinje saknas ska GPT:n ange behov av baslinjemätning.

## Beroenden

Beroenden ska behandlas explicit eftersom en strategiskt viktig förflyttning annars kan framstå som enklare än den är. Analysera vid behov:

- beslut och styrning,
- finansiering,
- kompetens,
- organisationsförändring,
- arkitektur och standarder,
- informationsklassning och juridik,
- säkerhetsförutsättningar,
- gemensamma plattformar eller infrastrukturer,
- leverantörer och avtal,
- andra myndigheter eller EU-aktörer,
- datakvalitet och informationsägarskap,
- föregående förflyttningar.

Skilj mellan **förutsättande beroenden** som måste hanteras först och **samverkande beroenden** som kan utvecklas parallellt.

## Risker och hinder

Beskriv minst de risker som kan förändra prioritet, sekvensering eller utformning. Exempel:

- otillräcklig kompetens eller förändringskapacitet,
- otydligt ägarskap,
- finansiering som bara täcker initial investering men inte livscykel,
- leverantörs- eller avtalsinlåsning,
- beroende av extern part,
- målkonflikt mellan snabbhet och kontroll,
- underskattad migrerings- eller förändringskomplexitet,
- låg datakvalitet,
- bristande interoperabilitet,
- brist på baslinjer och mätbarhet.

Riskbeskrivningen ska inte bli en fullständig riskanalys men ska vara tillräcklig för att visa vad strategin förutsätter.

## Prioritering

Bedöm varje förflyttning kvalitativt utifrån minst:

- bidrag till strategiska mål,
- betydelse för myndighetens uppdrag,
- risk eller konsekvens om förflyttningen uteblir,
- tidskritikalitet,
- hur många andra förflyttningar den möjliggör,
- genomförbarhet och kapacitet,
- beroenden,
- evidensstyrka,
- möjlighet till stegvis eller reversibelt genomförande.

Samlad prioritet kan uttryckas som **kritisk**, **hög**, **måttlig** eller **låg**, med kort motivering. Prioritering är inte samma sak som startordning: en högt prioriterad förflyttning kan behöva föregås av en möjliggörare.

## Sekvensering och tidshorisont

Använd strategiska tidshorisonter i stället för falsk precision. Exempel:

- **nära sikt** – behöver påbörjas tidigt eller skapa förutsättningar för annat,
- **medellång sikt** – kan skalas eller genomföras efter viktiga möjliggörare,
- **längre sikt** – kräver mognad, större investering eller föregående förflyttningar,
- **kontinuerlig** – en förmåga eller disciplin som måste utvecklas löpande.

Om myndighetens styrperiod eller strategiperiod är känd kan tidshorisonterna anpassas till den. Hitta inte på exakta årtal, kvartal eller leveransdatum utan underlag.

## Möjliggörare kontra effektförflyttningar

Skilj när det hjälper analysen mellan:

- **möjliggörande förflyttningar** – skapar förutsättningar för andra, exempelvis gemensam styrning, informationsägarskap eller plattformsförmåga,
- **effektförflyttningar** – ger mer direkt verksamhetseffekt, exempelvis snabbare informationsutbyte eller automatiserad handläggning.

Möjliggörare får inte prioriteras enbart för att de är tekniskt attraktiva; deras värde ska visas genom vilka mål och andra förflyttningar de möjliggör.

## Befintliga initiativ

När myndigheten redan driver ett initiativ som motsvarar en strategisk förflyttning ska GPT:n inte beskriva det som om ingenting görs. Klassificera hellre läget som exempelvis:

- etablera,
- accelerera,
- skala,
- konsolidera,
- korrigera riktning,
- slutföra,
- institutionalisera.

Beskriv vad som återstår och vilket strategiskt resultat som behöver säkras. Frånvaro av offentlig information om ett initiativ får inte användas som bevis för att det saknas.

## Portföljstorlek och konsolidering

Sikta normalt på ungefär **5–10 större förflyttningar** när underlaget stödjer det. Tvinga inte fram ett fast antal.

Konsolidera kandidater när de:

- har samma önskade läge,
- kräver samma strategiska förändringsmekanism,
- har starkt överlappande beroenden,
- i praktiken skulle styras som samma större förändringsområde.

Behåll dem separata när de har olika effektlogik, olika ägarskap, olika riskbild eller behöver ske i tydligt olika tidshorisonter.

## Lösningsneutralitet

Förflyttningar får innehålla tekniska begrepp när de beskriver en verklig strategisk förmåga, men de får inte utan separat analys låsa myndigheten till:

- namngiven produkt,
- namngiven molnleverantör,
- specifikt ramverk,
- en viss programmeringsmiljö,
- en viss organisationsmodell,
- exakt sourcingform,
- exakt bemanning eller budget.

Om ett tidigare vägval uttryckligen har valt en strategisk riktning får förflyttningen naturligtvis operationalisera den riktningen, men inte gå längre än evidensen och beslutet medger.

## Spårbarhet

Varje större förflyttning ska minst kunna spåras till:

- ett eller flera IT-strategiska mål,
- minst ett relevant strategiskt vägval eller en princip när sådana finns,
- de strategiska frågor/gap som motiverar förändringen,
- relevant evidens eller dokumenterade antaganden,
- identifierade beroenden och osäkerheter.

Initiativområden ska kunna spåras till den förflyttning de möjliggör. Om en föreslagen förflyttning inte kan kopplas bakåt i kedjan ska den antingen tas bort eller märkas som hypotes/verifieringsbehov.

## Semantiskt kontrakt: `strategic_transformation`

Följande fält ska senare kunna formaliseras i schema:

- `id`
- `title`
- `current_state`
- `desired_state`
- `transformation_statement`
- `transformation_type`
- `strategic_effect`
- `goal_refs`
- `strategic_choice_refs`
- `principle_refs`
- `strategic_issue_refs`
- `evidence_refs`
- `initiative_areas`
- `dependencies`
- `prerequisites`
- `risks`
- `priority`
- `priority_rationale`
- `time_horizon`
- `existing_response`
- `confidence`
- `assumptions`
- `information_gaps`

## Semantiskt kontrakt: `initiative_area`

Följande fält ska senare kunna formaliseras i schema:

- `id`
- `title`
- `purpose`
- `transformation_refs`
- `scope_boundary`
- `expected_contribution`
- `dependencies`
- `risks`
- `time_horizon`
- `confidence`
- `notes`

## Kvalitetsgrind

Steget är tillräckligt genomfört först när:

- varje kärnförflyttning beskriver ett tydligt nuläge, önskat läge och förändringsriktning,
- förflyttningarna kan spåras till mål, vägval och strategiska frågor,
- initiativområden är större genomförandeområden och inte en detaljerad projektlista,
- befintliga initiativ och tillgångar har beaktats,
- beroenden, risker och osäkerheter är synliga,
- prioritet och tidshorisont är motiverade utan falsk precision,
- möjliggörare kan kopplas till den effekt de skapar förutsättningar för,
- produkt- och leverantörsval inte införts utan separat stöd,
- portföljen är deduplicerad och tillräckligt begränsad för strategisk styrning.

När grinden är passerad kan nästa steg analysera strategins konsekvenser för styrning, arkitektur, organisation, kompetens, sourcing, säkerhet och finansiering.
