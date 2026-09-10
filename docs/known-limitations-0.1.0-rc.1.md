# Kända begränsningar – 0.1.0-rc.1

Den första release candidate-versionen har följande medvetna begränsningar.

## Offentligt underlag sätter gränsen

GPT:n kan endast dra säkra slutsatser om sådant som går att belägga i offentliga eller av användaren tillhandahållna källor. Intern systemportfölj, teknisk arkitektur, kontrakt, bemanning, kostnadsstruktur och faktisk leveranskapacitet är ofta endast delvis offentliga. Sådana luckor ska markeras i stället för fyllas med antaganden.

## Strategi, inte detaljerad målarkitektur

RC:n är byggd för IT-strategi. Den kan rekommendera strategiska riktningar men ska normalt inte välja specifika produkter, molnplattformar, integrationsprodukter eller detaljerad lösningsarkitektur utan särskilt analysunderlag.

## Researchkvalitet beror på tillgänglighet

Webbpublicerade dokument kan vara svåra att hitta, gamla, ompublicerade eller maskinellt svårlästa. GPT:n ska redovisa informationsluckor och källosäkerhet, men pilotprovningen behöver visa hur väl detta fungerar praktiskt på olika myndigheter.

## Custom GPT är komprimerad

Custom GPT-varianten använder en kompilerad instruktion inom plattformens instruktionsgräns. Kritiska beteendekontrakt har paritetsvaliderats, men Chat ZIP innehåller den fullständiga canonical instruktionen och JSON Schemas och är därför den rikare referensruntime-miljön.

## Ingen automatisk intern datainsamling

GPT:n har inga särskilda Actions för att hämta interna myndighetssystem. Interna dokument behöver tillhandahållas av användaren eller göras tillgängliga genom den runtime där GPT:n används.

## Pilot krävs före stabil release

RC:n är metod- och testvaliderad men ännu inte brett pilotprövad på flera myndighetstyper. Stabil release bör därför vänta tills steg 31 har genomförts.
