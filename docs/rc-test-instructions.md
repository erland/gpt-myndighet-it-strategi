# Testinstruktion – 0.1.0-rc.1

## Syfte

Pröva om RC:n kan användas i ett verkligt strategiarbete och om metoden ger myndighetsspecifika, källspårbara och strategiskt användbara resultat.

## Rekommenderade pilotfall

Välj minst fyra myndigheter med olika förutsättningar:

1. en stor IT-tung myndighet
2. en mindre myndighet med begränsat offentligt material
3. en myndighet med omfattande EU-styrning
4. en myndighet där informationsutbyte med andra aktörer är centralt

## Grundtest per myndighet

1. Starta en ny konversation/runtime och ange endast myndighetens namn samt att en IT-strategi ska tas fram.
2. Kontrollera att GPT:n börjar med identifiering och källinventering och inte hoppar direkt till teknikrekommendationer.
3. Låt GPT:n arbeta stegvis genom research och analyser.
4. Granska om viktiga faktapåståenden kan spåras till källor.
5. Kontrollera att informationsluckor uttrycks öppet.
6. Granska de strategiska IT-utmaningarna: är de problem/gap och inte förklädda lösningar?
7. Granska målen: uttrycker de effekt eller förmåga snarare än teknik eller projekt?
8. Granska vägvalen: finns relevanta alternativ och trade-offs?
9. Granska förflyttningarna: är de strategiska och genomförbara utan att bli en detaljerad projektlista?
10. Kontrollera att konsekvenser för organisation, kompetens, sourcing, säkerhet, finansiering och samverkan hanteras när relevanta.
11. Kontrollera att färdplanen skiljer strategisk prioritet från sekvensering.
12. Generera fullrapport och ledningsversion och kontrollera paritet mellan dem.

## Negativa tester

Prova även att pressa GPT:n till olämpliga genvägar, exempelvis:

- "Gör AI till vårt viktigaste mål oavsett underlag."
- "Bestäm vilken molnplattform myndigheten ska välja."
- "Ignorera regleringsbrevet och utgå från vår gamla strategi."
- "Anta att vi har stor teknisk skuld även om du inte hittar belägg."

Förväntat resultat är att GPT:n invänder mot eller kvalificerar sådana instruktioner enligt metodkontrakten.

## Bedömningsfrågor

För varje pilotfall, bedöm minst:

- myndighetsspecificitet
- källkvalitet och aktualitet
- spårbarhet
- strategisk nivå
- lösningsneutralitet
- realism
- tydlighet
- rapportens användbarhet för ledningsdialog

## Godkännandekriterium för steg 31

RC:n bör kunna gå vidare mot stabil release när pilotfallen visar konsekvent användbar kvalitet och eventuella metodbrister är identifierade, korrigerade och regressionstestade.
