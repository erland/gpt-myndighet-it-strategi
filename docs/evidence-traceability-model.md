# Evidens- och spårbarhetsmodell

## Syfte

Detta dokument definierar den canonical modell som IT-strategen för myndigheter ska använda för att hålla isär belagda observationer, analytiska tolkningar och strategiska rekommendationer. Modellen ska göra det möjligt att följa en betydande strategisk slutsats bakåt till de källor och observationer som motiverar den och samtidigt synliggöra antaganden, svag evidens och osäkerhet.

## Grundmodell

För större strategiska slutsatser används följande härledningskedja:

**Observation → källa → betydelse → strategisk konsekvens → rekommendation**

Kedjan ska inte behandlas som fem fria textfält som fylls i i efterhand. Varje led ska ha en tydlig semantisk roll och nästa led ska kunna motiveras av föregående led.

## Fem påståendetyper

Allt material som används i strategisk syntes ska kunna klassificeras som en av följande typer.

### Fakta

Ett påstående som direkt stöds av en identifierad källa eller av flera källor.

Exempel: myndigheten redovisar ett visst mål, en viss kostnadsutveckling eller ett beslutat regeringsuppdrag.

Regler:
- källreferens krävs,
- fakta får inte förstärkas bortom vad källan faktiskt visar,
- datum, tidsperiod och avgränsning ska bevaras när de påverkar innebörden,
- om källan endast återger någon annans uppgift ska ursprungskällan identifieras när det är relevant.

### Analys

En tolkning eller syntes som bygger på ett eller flera fakta, observationer eller uttryckliga antaganden.

Exempel: flera dokumenterade krav på digitalt informationsutbyte innebär ett växande behov av interoperabilitet.

Regler:
- analys ska inte formuleras som om den vore citerad fakta,
- underliggande evidens ska vara identifierbar,
- inferensens styrka ska bedömas,
- alternativa rimliga tolkningar ska beaktas när de kan förändra slutsatsen väsentligt.

### Rekommendation

Ett normativt strategiskt råd om vad myndigheten bör prioritera, välja, förändra eller avstå från.

Regler:
- rekommendationen ska kopplas till minst en dokumenterad strategisk konsekvens eller ett explicit antagande,
- omfattande rekommendationer kräver starkare och normalt bredare evidens än små rekommendationer,
- trendinformation får inte ensam bära en myndighetsspecifik rekommendation,
- rekommendationen ska kunna omprövas om en central premiss visar sig felaktig.

### Antagande

En uttrycklig premiss som behövs för analysen men som inte har kunnat beläggas tillräckligt.

Regler:
- antagandet ska märkas som antagande,
- det får inte förvandlas till fakta längre fram i kedjan,
- dess betydelse för slutsatsen ska anges,
- där det är möjligt ska det anges vilket underlag som skulle kunna verifiera eller falsifiera antagandet.

### Osäkerhet / informationslucka

En dokumenterad begränsning i underlaget, källkonflikt eller svag inferens som påverkar säkerheten i analysen.

Regler:
- ange vad som är osäkert,
- ange varför det spelar roll,
- ange vilka slutsatser som påverkas,
- ange om arbetet kan fortsätta best effort eller om ett steg faktiskt blockeras.

## Evidenspost

En evidenspost representerar ett avgränsat belagt eller explicit osäkert påstående som kan återanvändas i analysen.

Fram till det formella schemasteget ska en evidenspost semantiskt kunna innehålla minst:

- `id`
- `typ`: fakta, antagande eller osäkerhet
- `observation`
- `source_ids`: en eller flera källposter när typen kräver källa
- `tidsperiod`
- `scope`: vad observationen faktiskt gäller
- `evidensstyrka`
- `direkthet`: direkt belagd eller infererad
- `konflikter`: relaterade käll- eller evidenskonflikter
- `begransningar`
- `anvands_i`: vilka analyser eller härledningskedjor som använder posten

En evidenspost ska vara tillräckligt atomär för att dess stöd kan bedömas. Ett helt stycke med flera separata sakpåståenden ska normalt delas upp.

## Evidensstyrka

Evidensstyrka bedöms kvalitativt, inte genom falsk numerisk precision.

### Stark

- direkt stöd från en auktoritativ och relevant primärkälla, eller
- samstämmigt stöd från flera oberoende och relevanta källor.

### Medel

- rimligt stöd från relevant källa men med begränsning i aktualitet, scope eller oberoende, eller
- syntes från flera indirekta signaler som tillsammans ger en stabil bild.

### Svag

- enstaka indirekt signal,
- gammal eller endast delvis relevant uppgift,
- svag inferens,
- källa med tydligt egenintresse utan oberoende stöd.

Svag evidens får användas för hypoteser och försiktiga analysindikeringar men ska normalt inte ensam bära ett stort strategiskt vägval.

## Strategisk härledningskedja

En härledningskedja binder ihop evidens med en strategisk slutsats. Den ska kunna representeras med minst:

- `id`
- `evidence_ids`
- `betydelse`
- `strategisk_konsekvens`
- `rekommendation` när kedjan leder till ett råd
- `inferensstyrka`
- `kritiska_antaganden`
- `osakerheter`
- `alternativa_tolkningar` när relevanta
- `berorda_mal_eller_vagval`

### Led 1 – Observation

Beskriv vad underlaget faktiskt visar. Undvik strategiska värdeord i detta led.

### Led 2 – Källa

Knyt observationen till de källposter som stöder den. Källans nivå och begränsningar följer källmodellen i `docs/source-model.md`.

### Led 3 – Betydelse

Förklara varför observationen är relevant för myndighetens förmåga att fullgöra uppdrag, nå mål eller hantera förändringstryck.

Detta är analys, inte fakta.

### Led 4 – Strategisk konsekvens

Beskriv vilken långsiktig IT-relaterad förmåga, begränsning, risk eller möjlighet som följer av betydelsen.

Konsekvensen ska ligga på strategisk nivå. Den ska inte omotiverat hoppa direkt till produkt eller detaljlösning.

### Led 5 – Rekommendation

Formulera endast en rekommendation när föregående led ger tillräckligt stöd. Rekommendationen ska beskriva ett strategiskt mål, vägval, princip eller prioriterad förflyttning på rätt abstraktionsnivå.

## Spårbarhetsgraf

Spårbarheten ska behandlas som en graf snarare än som en enda linjär kedja:

- en källa kan stödja flera evidensposter,
- en evidenspost kan bidra till flera analyser,
- flera evidensposter kan tillsammans motivera en strategisk konsekvens,
- ett strategiskt mål kan ha flera härledningskedjor,
- en rekommendation kan stödja flera förflyttningar,
- samma antagande kan påverka flera slutsatser och ska då kunna identifieras på alla berörda ställen.

Det innebär att duplicerad text inte ska ersätta explicita relationer mellan poster.

## Härledningsregler

### Regel 1 – Inga hopp över verksamhetsbetydelsen

En teknisk trend eller observation får inte hoppa direkt till rekommendation utan att dess betydelse för den aktuella myndigheten förklaras.

Felaktigt exempel:

> AI utvecklas snabbt → myndigheten bör införa generativ AI.

Godtagbar struktur kräver först ett belagt myndighetsbehov och en analys av varför tekniken är relevant för detta behov.

### Regel 2 – Rekommendationens styrka får inte överstiga evidensen

Svag evidens ska ge försiktigare språk, större osäkerhet eller en rekommendation om vidare analys snarare än ett kategoriskt vägval.

### Regel 3 – Strategisk betydelse kräver proportionerlig evidens

Ju större kostnad, irreversibilitet, organisatorisk påverkan eller risk ett vägval innebär, desto högre krav ställs på triangulering och kvalitet i underlaget.

### Regel 4 – Motsägande evidens ska följa med framåt

En olöst käll- eller evidenskonflikt får inte försvinna när slutsatser syntetiseras. Den ska kopplas till berörda analyser och påverka säkerhetsbedömningen.

### Regel 5 – Antaganden ärver inte evidensstatus

Att flera analyser använder samma antagande gör inte antagandet mer sant. Ett återanvänt antagande ska fortfarande märkas som obelagt tills det verifierats.

### Regel 6 – Frånvaro av evidens är normalt inte evidens för frånvaro

Om GPT:n inte hittar offentlig information om exempelvis teknisk skuld, plattformsproblem eller kompetensbrist får den inte dra slutsatsen att problemet saknas. Den ska i stället registrera en informationslucka när frågan är strategiskt relevant.

## Inferensstyrka

Analytiska led och härledningskedjor ska kunna klassificeras kvalitativt som:

- **hög** – slutsatsen följer direkt eller mycket starkt av relevant evidens och få rimliga alternativa tolkningar finns,
- **medel** – slutsatsen är väl motiverad men innehåller viss inferens, avgränsning eller osäkerhet,
- **låg** – slutsatsen är en plausibel hypotes eller svag syntes och ska inte presenteras som säker.

Inferensstyrka är skild från källans auktoritet. En mycket auktoritativ källa kan fortfarande ge svagt stöd för en slutsats som ligger långt utanför det den faktiskt beskriver.

## Alternativa tolkningar och motbevis

För strategiskt betydande slutsatser ska GPT:n aktivt kontrollera om:

- samma observation rimligen kan förklaras på annat sätt,
- det finns källor som motsäger slutsatsen,
- senare utveckling har gjort evidensen inaktuell,
- rekommendationen bygger på ett implicit antagande,
- den rekommenderade åtgärden är en lösning på symptom snarare än bakomliggande behov.

Alternativa tolkningar behöver inte alltid presenteras i slutrapporten, men ska påverka säkerhetsbedömningen och redovisas när de är materiella.

## Strategiska objekt och minsta spårbarhet

### Strategisk IT-utmaning

Ska kunna spåras till minst en evidenspost och en förklarad verksamhetsbetydelse.

### IT-strategiskt mål

Ska kunna spåras till en eller flera strategiska utmaningar, behov eller möjligheter med belagd myndighetsrelevans.

### Strategiskt vägval

Ska kunna spåras till mål och relevanta härledningskedjor. Stora vägval ska normalt ha triangulerad evidens.

### Princip

Ska kunna motiveras av mål, vägval eller återkommande dokumenterade behov. Generella best practices får inte införas utan myndighetsrelevans.

### Prioriterad förflyttning

Ska kunna spåras till minst ett mål eller vägval och beskriva vilken strategisk effekt den ska bidra till.

### Färdplanspost

Ska kunna spåras till en prioriterad förflyttning och dess beroenden.

## Spårbarhetsmatris

Inför strategisk syntes och i slutlig kvalitetsgranskning ska GPT:n kunna skapa eller internt kontrollera en matris med minst:

- strategiskt objekt
- typ av objekt
- stödjande evidens/härledningskedjor
- källor
- kritiska antaganden
- osäkerheter
- inferensstyrka

Målet är inte att belasta användaren med intern administration. Matrisen används för kvalitetssäkring och kan visas på begäran eller sammanfattas i slutrapportens metod-/spårbarhetsdel.

## Säkerhets- och språkregler för slutsatser

- Använd inte ord som “visar”, “bevisar” eller “kräver” om evidensen endast stödjer en möjlig tolkning.
- Använd formuleringar som “indikerar”, “talar för” eller “bör analyseras vidare” när inferensen är svagare.
- Separera “myndigheten anger …” från “analysen bedömer …”.
- Ange när en rekommendation är villkorad av ett antagande.
- Vid låg säkerhet ska rekommendationen kunna vara att inhämta visst internt underlag innan beslut.

## Kvalitetsgrind för strategisk härledning

En större strategisk slutsats är redo för syntes när:

1. den har minst en identifierad evidenspost,
2. evidensposten har källstöd eller är uttryckligen klassificerad som antagande/osäkerhet,
3. verksamhetsbetydelsen är förklarad,
4. den strategiska konsekvensen följer utan omotiverat teknik- eller lösningshopp,
5. inferensstyrkan är bedömd,
6. kritiska antaganden och motsägande evidens är synliga,
7. rekommendationens styrka är proportionerlig mot evidensen.

För stora eller svårreversibla vägval krävs normalt triangulering eller en uttrycklig rekommendation om vidare beslutsunderlag.

## Exempel på komplett kedja

### Evidens

- Myndighetens styrning och strategiska dokument innehåller återkommande behov av digitalt informationsutbyte med externa aktörer.
- Flera oberoende källor visar att informationsutbyte är centralt för verksamhetens måluppfyllelse.

### Betydelse

Myndighetens resultat blir i ökande grad beroende av att information kan delas korrekt, säkert och tillräckligt snabbt över organisatoriska gränser.

### Strategisk konsekvens

Interoperabilitet och styrd informationshantering blir långsiktiga IT-förmågor som behöver behandlas sammanhållet snarare än som enskilda integrationsprojekt.

### Rekommendation

Etablera interoperabilitet som ett strategiskt målområde och prioritera en förflyttning mot gemensamma informationsprinciper, standardiserade gränssnitt och återanvändbara mekanismer för digitalt informationsutbyte.

### Spårbarhetsbedömning

Rekommendationen är inte motiverad av att “API-first” är en branschtrend. Den är motiverad av myndighetens dokumenterade verksamhetsbehov; tekniska principer väljs senare som medel för att stödja detta behov.

## Relation till senare schemasteg

Detta dokument etablerar det semantiska kontraktet. Formella maskinläsbara schemas för evidensposter, strategiska objekt och spårbarhetsrelationer skapas senare enligt utvecklingsplanen. De får precisera syntax men inte bryta de semantiska reglerna ovan utan ett uttryckligt metodbeslut.
