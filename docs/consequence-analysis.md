# Konsekvensanalys

## Syfte

Konsekvensanalysen prövar vad de föreslagna strategiska målen, vägvalen, principerna och förflyttningarna faktiskt innebär för myndighetens styrning, arkitektur, organisation, kompetens, sourcing, säkerhet, finansiering och samverkan. Den ska göra genomförandekrav, målkonflikter och dolda beroenden synliga innan färdplanen fastställs.

Analysen är **dubbelriktad**: den bedömer både vilka konsekvenser strategin skapar och om identifierade begränsningar kräver att mål, vägval eller förflyttningar justeras.

## Grundregel

För varje större strategiskt objekt ska GPT:n fråga:

> **Vad måste förändras eller säkras för att detta ska vara genomförbart, och finns det någon konsekvens som gör att den strategiska riktningen bör omprövas?**

Konsekvensanalysen får inte reduceras till en generell checklista. Endast materiella konsekvenser ska lyftas, men alla obligatoriska analysdomäner ska övervägas.

## Indata

Använd i första hand:

- prioriterade `it_strategic_goal`,
- `strategic_choice` och `strategic_principle`,
- `strategic_transformation` och tillhörande initiativområden,
- ekonomisk och kapacitetsmässig analys,
- nuläge och förändringstryck,
- strategiska IT-utmaningar och gap,
- viktiga beroenden, målkonflikter, risker och informationsluckor,
- relevanta styr-, säkerhets-, juridik- och samverkanskrav.

## Obligatoriska analysdomäner

Överväg konsekvenser inom minst följande domäner:

1. **Verksamhetsstyrning** – ansvar, prioritering, verksamhetsägarskap, nyttorealisering och beslutsforum.
2. **IT-styrning** – portföljstyrning, produkt-/tjänsteägarskap, investeringsbeslut, livscykelstyrning och uppföljning.
3. **Enterprise architecture** – principer, målarkitekturbehov, standardisering, undantag, teknisk skuld och arkitekturstyrning.
4. **Information och data** – informationsägarskap, datakvalitet, informationsmodellering, metadata, delning och livscykel.
5. **Organisation och arbetssätt** – ansvarsfördelning, centralisering/decentralisering, tvärfunktionellt arbete, produkt-/plattformsteam och förändringsledning.
6. **Kompetens och kapacitet** – nya kompetensbehov, kompetensförsörjning, ledningsförmåga, arkitektur, säkerhet, data och leveranskapacitet.
7. **Sourcing och leverantörer** – make/buy-gränser, upphandling, avtalsstruktur, leverantörsberoenden, exit, portabilitet och intern beställarförmåga.
8. **Säkerhet och robusthet** – informationssäkerhet, cyberresiliens, kontinuitet, beredskap, identitet/behörighet, tredjepartsrisk och återställningsförmåga.
9. **Finansiering och ekonomi** – investeringsbehov, löpande kostnad, finansieringsmodell, flerårighet, dubbelkostnader under migration och kostnad för kompetens/livscykel.
10. **Samverkan och externa beroenden** – andra myndigheter, gemensamma offentliga tjänster, EU-aktörer, informationsutbyte, gemensamma standarder och beroenden till externa beslut.

Juridiska eller regulatoriska konsekvenser ska synliggöras där de är materiella, men GPT:n ska inte låtsas ge rättsligt bindande rådgivning utan särskilt underlag.

## Arbetsordning

Arbeta i följande ordning:

1. **Välj analysobjekt.** Identifiera de mål, vägval och förflyttningar som är tillräckligt betydande för konsekvensanalys.
2. **Identifiera direkt påverkan.** Beskriv vad objektet kräver eller förändrar inom relevanta domäner.
3. **Identifiera möjliggörare.** Ange vilka förutsättningar som måste finnas eller etableras.
4. **Identifiera negativa bieffekter och trade-offs.** Synliggör kostnad, komplexitet, inlåsning, styrspänningar och andra nackdelar.
5. **Identifiera övergångskonsekvenser.** Bedöm migrationsperiod, dubbel drift, temporär komplexitet och förändringsbelastning när relevant.
6. **Bedöm genomförbarhet.** Jämför konsekvenserna med dokumenterad ekonomi, kompetens och förändringskapacitet.
7. **Pröva externa beroenden.** Identifiera sådant myndigheten inte kontrollerar själv.
8. **Bedöm konsekvensens materialitet.** Skilj kritiska konsekvenser från hanterbara eller marginella.
9. **Återkoppla till strategin.** Markera om mål, vägval, principer, prioritet, sekvensering eller förflyttning behöver justeras.
10. **Registrera öppna frågor.** Ange informationsluckor som måste verifieras före beslut eller genomförande.

## Konsekvenstyper

Varje betydande konsekvens ska klassificeras som en eller flera av:

- **krav** – något som måste vara uppfyllt för att strategin ska fungera,
- **möjliggörare** – något som ökar sannolikheten eller tempot i genomförandet,
- **kostnad/belastning** – resurs-, komplexitets- eller förändringsbelastning,
- **risk** – osäker händelse eller exponering som kan försämra utfallet,
- **beroende** – något som kräver annan part, annat beslut eller annan förflyttning,
- **trade-off** – en tydlig avvägning där förbättring i en dimension försämrar en annan,
- **övergångseffekt** – temporär konsekvens under migration eller etablering,
- **strategisk återkoppling** – konsekvens som motiverar justering av den föreslagna strategin.

## Materialitetsbedömning

Bedöm varje viktig konsekvens kvalitativt efter:

- påverkan på uppdrag och måluppfyllelse,
- påverkan på genomförbarhet,
- kostnads- eller kapacitetsbelastning,
- säkerhets-/robusthetspåverkan,
- reversibilitet,
- beroende av extern part,
- tid till effekt,
- evidensstyrka.

Samlad materialitet kan uttryckas som **kritisk**, **hög**, **måttlig** eller **låg**, alltid med kort motivering. Hitta inte på numeriska sannolikheter eller kostnader utan underlag.

## Dubbelriktad strategiprövning

Konsekvensanalysen ska kunna ändra strategin. Om en konsekvens är kritisk ska GPT:n pröva minst följande alternativ:

- behåll riktningen men lägg till möjliggörare eller guardrail,
- dela upp förflyttningen i etapper,
- ändra sekvensering,
- sänk eller flytta tidshorisonten,
- justera omfattningen,
- välj ett mer reversibelt alternativ,
- ompröva vägvalet,
- markera beslutet som villkorat tills informationsluckan är stängd.

Ett tidigare formulerat mål eller vägval ska alltså inte skyddas från omprövning bara för att det ligger tidigare i arbetsflödet.

## Övergångs- kontra målbildskonsekvenser

Skilj mellan:

- **målbildskonsekvenser** – permanenta eller långsiktiga egenskaper hos den framtida modellen,
- **övergångskonsekvenser** – tillfälliga kostnader, risker eller organisatoriska belastningar för att nå målbilden.

Exempel på övergångskonsekvenser är dubbel drift, parallella kompetensbehov, migreringsrisk, tillfälligt högre kostnader, dataflytt, avtalsöverlapp och förändringströtthet. Dessa får inte misstolkas som permanenta nackdelar, men de kan påverka sekvensering och genomförbarhet kraftigt.

## Samlade tvärgående konsekvenser

Efter analys per mål/vägval/förflyttning ska GPT:n konsolidera tvärgående mönster, exempelvis:

- många förflyttningar kräver samma knappa kompetens,
- flera vägval kräver starkare gemensam arkitekturstyrning,
- flera initiativ skapar samtidiga migrationskostnader,
- många mål är beroende av informationsägarskap eller datakvalitet,
- flera strategiska effekter kräver extern samverkan,
- samma leverantörs- eller plattformsberoende återkommer,
- säkerhets- eller beredskapskrav påverkar flera områden samtidigt.

Dessa tvärgående konsekvenser ska föras vidare till färdplanen och kan skapa egna möjliggörande förflyttningar om de inte redan finns.

## Semantiskt kontrakt: `strategic_consequence`

Ett framtida strukturerat objekt bör minst kunna bära:

- `id`
- `title`
- `domain`
- `consequence_type`
- `description`
- `affected_object_ids`
- `requirement_or_change`
- `positive_effects`
- `negative_effects`
- `dependencies`
- `risks`
- `transition_effects`
- `materiality`
- `evidence_refs`
- `assumptions`
- `uncertainties`
- `strategic_feedback`
- `recommended_handling`

Detta är ett semantiskt kontrakt; JSON/YAML-schema implementeras senare enligt utvecklingsplanen.

## Spårbarhetskrav

Varje kritisk eller hög materiell konsekvens ska kunna kopplas till:

- det strategiska objekt som orsakar eller påverkas av konsekvensen,
- relevant evidens eller uttryckligt antagande,
- den föreslagna hanteringen,
- eventuell återkoppling till mål, vägval eller förflyttning.

Konsekvenser som bygger på inferens ska markeras som analys, inte fakta.

## Guardrails

GPT:n får inte:

- anta en specifik organisationsmodell enbart för att den är modern,
- rekommendera outsourcing eller insourcing som standardreaktion på kompetensbrist,
- göra exakta budget- eller bemanningsestimat utan data,
- anta att en teknisk standard automatiskt löser styrningsproblem,
- behandla säkerhet som en separat efterhandskontroll när den påverkar strategiskt val,
- dölja negativa konsekvenser för att ett vägval redan har rekommenderats,
- låta låg offentlig transparens om intern organisation bli bevis för att förmågan saknas.

## Kvalitetsgrind

Konsekvensanalysen är tillräckligt genomförd när:

- alla obligatoriska domäner har övervägts,
- kritiska och höga konsekvenser är synliga och spårbara,
- permanenta och övergångsrelaterade konsekvenser hålls isär,
- ekonomi och kapacitet har prövats mot strategins ambitionsnivå,
- tvärgående flaskhalsar och beroenden har konsoliderats,
- negativa trade-offs redovisas öppet,
- konsekvenser kan återkoppla och ändra tidigare strategiska objekt,
- informationsluckor och verifieringsbehov är tydliga,
- resultatet ger konkreta indata till färdplan och uppföljning.

## Utdata

Leverera normalt:

1. en kort samlad konsekvensbild,
2. en tabell eller strukturerad lista över kritiska/höga konsekvenser,
3. analys per relevant domän,
4. tvärgående möjliggörare och flaskhalsar,
5. föreslagna justeringar av mål/vägval/förflyttningar,
6. öppna frågor och informationsluckor som behöver verifieras.
