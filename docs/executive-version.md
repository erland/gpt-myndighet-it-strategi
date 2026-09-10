# Ledningsversion – kontrakt

## Syfte

Ledningsversionen är en kort, beslutsinriktad destillation av den fullständiga IT-strategin. Den ska kunna läsas fristående av myndighetsledning och andra beslutsfattare, men får inte innehålla nya strategiska slutsatser, nya evidenspåståenden eller starkare rekommendationer än fullversionen.

Den ska hjälpa läsaren att snabbt förstå:

1. varför IT-strategin behöver en viss riktning,
2. vilka strategiska mål som är viktigast,
3. vilka vägval och förflyttningar som kräver ledningens ställningstagande,
4. vilka risker, beroenden och kapacitetsfrågor som kan påverka genomförandet,
5. vilka beslut eller uppdrag som bör följa.

## Normal omfattning

Ledningsversionen ska vara kort nog för ledningsdialog. Som riktmärke bör den normalt motsvara cirka 3–6 textsidor eller en likvärdig kompakt digital presentation, men omfattningen får anpassas efter myndighetens komplexitet och användarens uttryckliga önskemål.

Koncis form får aldrig uppnås genom att viktiga osäkerheter, målkonflikter eller blockerande beroenden döljs.

## Rekommenderad struktur

### 1. Strategisk situation

Sammanfatta myndighetens strategiska utgångsläge i ett fåtal stycken:

- centrala uppdrag och styrsignaler,
- viktigaste verksamhetsförändringar,
- ekonomiska eller kapacitetsmässiga förutsättningar,
- de mest relevanta IT-relaterade förändringstrycken.

Undvik generell myndighetsbeskrivning. Ta endast med sådant som behövs för att förstå strategins riktning.

### 2. Viktigaste slutsatser

Lyft normalt cirka 5–8 bärande slutsatser när underlaget stödjer det. Varje slutsats ska vara myndighetsspecifik och kunna spåras till fullrapportens analys.

En slutsats ska uttrycka vad analysen betyder strategiskt, inte bara återge ett faktum eller en trend.

### 3. IT-strategiska mål

Presentera kärnmålen i kort form. För varje mål bör ledningsversionen visa:

- önskad effekt eller förmåga,
- varför målet är viktigt för uppdraget,
- hur målet förhåller sig till de viktigaste strategiska utmaningarna.

Hitta inte på nya mål för att göra ledningsversionen mer slagkraftig.

### 4. Viktigaste strategiska vägval

Visa de vägval som har störst betydelse för ledningens styrning och resursfördelning. För varje större vägval bör det framgå:

- rekommenderad riktning,
- viktigaste alternativ eller trade-off,
- huvudsaklig motivering,
- kritisk konsekvens eller villkor när det är relevant.

Detaljerade teknik- och produktval ska normalt inte ingå.

### 5. Prioriterade förflyttningar

Visa den strategiska kärnportföljen av förflyttningar i koncentrerad form. Fokusera på:

- nuläge → önskat läge,
- strategisk betydelse,
- prioritet,
- viktigaste beroenden,
- ungefärlig tidshorisont när den är motiverad.

Ledningsversionen ska inte bli en detaljerad projektlista.

### 6. Kritiska risker och beroenden

Lyft endast de risker, beroenden, kapacitetsbegränsningar och informationsluckor som kan påverka beslut, ambitionsnivå, sekvensering eller genomförbarhet.

Skilj mellan:

- dokumenterade risker,
- analytiskt identifierade risker,
- kritiska antaganden,
- externa beroenden,
- osäkerheter som kräver kompletterande analys.

### 7. Rekommenderade beslut och uppdrag

Avsluta med de ställningstaganden som ledningen faktiskt behöver göra. Ett rekommenderat beslut eller uppdrag ska kunna härledas till fullrapportens mål, vägval, förflyttningar eller kritiska konsekvenser.

Exempel på beslutsformer:

- fastställa strategisk riktning,
- ge uppdrag att etablera en möjliggörande förmåga,
- prioritera eller sekvensera en strategisk förflyttning,
- initiera kompletterande analys där evidensen är otillräcklig,
- fastställa styr- eller uppföljningsmodell,
- besluta om princip eller vägval som kräver ledningsmandat.

Formulera inte detaljerade genomförandebeslut som underlaget inte stödjer.

## Paritetsregler mot fullversionen

Ledningsversionen är en vy över samma strategi och måste därför uppfylla följande:

1. inga nya strategiska mål,
2. inga nya vägval,
3. inga nya prioriterade förflyttningar,
4. inga starkare rekommendationer än fullrapporten,
5. inga borttagna kritiska förbehåll som ändrar innebörden,
6. inga nya faktapåståenden utan stöd i fullrapportens evidens,
7. samma prioriteringslogik och huvudsakliga beroenden som i fullversionen.

Om innehållet behöver ändras därför att ledningsversionen avslöjar en inkonsistens ska fullrapporten först korrigeras och därefter destilleras på nytt.

## Spårbarhet

Ledningsversionen behöver inte återge hela evidensgrafen, men bärande slutsatser och rekommendationer ska kunna kopplas till fullrapportens motsvarande avsnitt eller strategiska objekt.

När användargränssnittet eller dokumentformatet tillåter det bör korta källhänvisningar eller referenser till fullrapporten finnas nära särskilt viktiga faktapåståenden.

## Beslutsrelevans

Varje del ska prövas mot frågan: **Behöver ledningen detta för att förstå, välja, prioritera, mandatlägga eller följa upp strategin?**

Material som främst är metodbeskrivning, detaljerad omvärldsresearch, full källförteckning, teknisk bakgrund eller utförlig analys ska normalt stanna i fullrapporten.

## Kvalitetsgrind

Ledningsversionen är klar först när följande kontroller passerar:

- `executive_version_standalone_contract`: versionen kan förstås utan att fullrapporten läses parallellt.
- `executive_version_parity_contract`: inga mål, vägval, förflyttningar eller rekommendationer avviker materiellt från fullversionen.
- `executive_version_decision_focus_contract`: innehållet fokuserar på beslut, prioriteringar och strategisk styrning.
- `executive_version_uncertainty_contract`: kritiska osäkerheter, antaganden och beroenden är inte bortredigerade.
- `executive_version_traceability_contract`: bärande slutsatser kan spåras tillbaka till fullrapportens analys och evidens.
- `executive_version_scope_contract`: detaljnivån är strategisk och ledningsanpassad, inte projekt- eller produktorienterad.

Om någon kritisk kontroll fallerar ska ledningsversionen revideras innan den levereras som färdig.

## Semantiskt kontrakt: `executive_strategy_version`

En framtida schemaimplementation bör minst kunna representera:

- myndighet,
- versions-/datumkontext,
- strategisk situation,
- viktigaste slutsatser,
- strategiska mål,
- strategiska vägval,
- prioriterade förflyttningar,
- kritiska risker och beroenden,
- rekommenderade beslut/uppdrag,
- osäkerheter och antaganden,
- referenser till fullrapportens objekt/avsnitt,
- kvalitetsgrindens resultat.
