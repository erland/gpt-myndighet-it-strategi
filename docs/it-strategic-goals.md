# IT-strategiska mål

## Syfte

Detta steg översätter de prioriterade strategiska IT-utmaningarna till ett begränsat, sammanhängande och spårbart målramverk. Målen ska beskriva **önskad framtida effekt eller förmåga** för myndigheten. De ska inte beskriva projekt, aktiviteter, produkter eller tekniska lösningar.

## Grundregel

Ett IT-strategiskt mål ska svara på frågan **vilket strategiskt tillstånd eller vilken förmåga behöver myndigheten uppnå för att bättre kunna fullgöra sitt uppdrag och möta de prioriterade utmaningarna?**

Målet ska därför härledas från verksamhetsmål, styrning och prioriterade strategiska IT-utmaningar. Det får inte skapas enbart för att en tekniktrend är aktuell.

## Indata

Använd i första hand:

- prioriterade `strategic_issue`-objekt,
- berörda verksamhetsmål och styrkrav,
- strategiska konsekvenser från tidigare analyser,
- dokumenterade målkonflikter och beroenden,
- ekonomiska och kapacitetsmässiga begränsningar,
- informationsluckor som påverkar målets säkerhet.

## Från utmaning till mål

Arbeta i följande ordning:

1. **Identifiera önskad effekt eller förmåga.** Formulera vilket tillstånd som skulle minska gapet eller förbättra myndighetens handlingsförmåga.
2. **Kontrollera verksamhetskopplingen.** Målet ska kunna kopplas till minst ett relevant verksamhetsmål, styrkrav eller kärnuppdrag.
3. **Konsolidera när lämpligt.** Flera utmaningar får stödja samma mål om de kräver samma strategiska effekt eller förmåga.
4. **Undvik lösningsspråk.** Formulera inte målet som införande av teknik, produkt, plattform eller metod.
5. **Pröva mätbarhet.** Definiera hur utvecklingen mot målet kan följas utan att låsa målet till ett visst genomförande.
6. **Sätt tidshorisont.** Ange när det önskade tillståndet behöver vara väsentligt uppnått eller när tydlig förflyttning ska kunna visas.
7. **Pröva realism.** Kontrollera ekonomiska, kompetensmässiga och organisatoriska begränsningar.
8. **Pröva portföljen.** Kontrollera att målramverket som helhet är begränsat, balanserat och utan onödig överlappning.

## Målformulering

Bra strategiska mål uttrycker normalt:

- en förbättrad verksamhets- eller IT-förmåga,
- en önskad effekt,
- en styrbar kvalitativ förflyttning,
- eller ett strategiskt tillstånd som ger bättre handlingsförmåga, robusthet eller effektivitet.

Exempel på målform:

> Myndigheten ska kunna utbyta verksamhetskritisk information digitalt, säkert och standardiserat med relevanta externa aktörer med kortare ledtid för nya eller ändrade informationsflöden.

Detta är bättre än:

> Myndigheten ska införa en API-plattform.

Det första uttrycker önskad förmåga och effekt. Det andra är ett möjligt vägval eller initiativ och hör hemma i senare steg.

## Mål kontra vägval, princip och initiativ

Håll objekttyperna isär:

- **Mål:** vilket tillstånd eller vilken effekt som ska uppnås.
- **Vägval:** hur myndigheten på strategisk nivå väljer att nå målen.
- **Princip:** återkommande beslutsregel som styr val.
- **Förflyttning:** större förändringsområde från nuläge mot önskat läge.
- **Initiativ/projekt:** konkret genomförandeaktivitet.

Om ett mål innehåller ord som *införa*, *migrera till*, *standardisera på*, *upphandla*, *bygga* eller ett specifikt teknik-/produktnamn ska formuleringen normalt omprövas.

## Teknikneutralitet

Tekniknamn används normalt inte i strategiska mål. AI, moln, zero trust, Kubernetes, OpenShift, Azure, API management, data mesh och liknande är inte mål i sig.

Ett teknikbegrepp får endast förekomma i ett mål när det är en uttrycklig del av bindande styrning eller när själva tekniska förmågan är det strategiskt efterfrågade resultatet och detta kan motiveras tydligt. Även då ska målet i första hand uttrycka verksamhetsvärde eller förmåga.

## Spårbarhet

Varje mål ska kunna följas bakåt till:

1. minst en prioriterad strategisk IT-utmaning,
2. relevanta verksamhetsmål eller styrkrav,
3. evidens och observationer bakom dessa,
4. förklaring till varför målet reducerar ett viktigt gap eller skapar nödvändig handlingsförmåga.

Ett mål utan spårbar koppling ska tas bort, omformuleras eller märkas som hypotes i stället för att ingå i kärnstrategin.

## Mätbarhet

Mätbarhet ska stödja styrning utan skenprecision. Varje mål ska ha minst en uppföljningsidé. Använd när möjligt en kombination av:

- effektindikatorer,
- förmågeindikatorer,
- kvalitetsindikatorer,
- ledtidsindikatorer,
- risk-/robusthetsindikatorer,
- användnings- eller täckningsindikatorer.

Undvik att göra genomförandeaktivitet till mått på måluppfyllelse. Exempelvis är “antal migrerade system” främst ett genomförandemått; det visar inte i sig om flexibilitet, kostnad, säkerhet eller verksamhetseffekt har förbättrats.

När baslinje saknas ska GPT:n ange att indikatorn behöver baslinjemätas i stället för att hitta på ett numeriskt målvärde.

## Tidshorisont

Klassificera mål med en strategiskt begriplig tidshorisont, exempelvis:

- **kort sikt** – tydlig förflyttning inom 0–2 år,
- **medellång sikt** – väsentlig effekt inom 2–4 år,
- **lång sikt** – strukturell förflyttning över 4 år.

Anpassa intervallet efter myndighetens strategiperiod och bindande deadlines. Exakta årtal ska användas när styrningen kräver det.

## Prioritering och målportfölj

Mål ska inte automatiskt skapas ett-för-ett från varje strategisk utmaning. Flera utmaningar kan stödja samma mål, och en utmaning kan kräva mer än ett mål om konsekvenserna är tydligt olika.

Sikta normalt på ett litet antal kärnmål, ofta ungefär **4–7**, när underlaget stödjer det. Antalet är vägledande och får inte tvinga fram sammanslagningar eller extra mål.

Bedöm målportföljen efter:

- täckning av kritiska/högprioriterade utmaningar,
- koppling till uppdrag och verksamhetsmål,
- begränsad överlappning,
- balans mellan effekt, robusthet och genomförbarhet,
- realistisk ambitionsnivå,
- tydlig prioritering.

Om två mål är så lika att samma indikatorer och vägval skulle användas för båda bör de normalt konsolideras.

## Målkonflikter och avvägningar

Mål kan stå i spänning med varandra eller med verksamhetsmål, exempelvis snabbare förändring kontra kontroll, standardisering kontra lokal flexibilitet eller kostnadseffektivitet kontra redundans.

Sådana konflikter ska inte döljas. Registrera dem som explicita målspänningar som senare vägval måste hantera.

## Semantiskt kontrakt: it_strategic_goal

Inför schemasteget ska följande betydelse bevaras:

```yaml
it_strategic_goal:
  id: G-001
  title: string
  statement: string
  desired_effect_or_capability: string
  strategic_issue_refs: [id]
  business_goal_refs: [id]
  governance_refs: [id]
  evidence_refs: [id]
  rationale: string
  indicators:
    - name: string
      indicator_type: effect | capability | quality | lead_time | risk | coverage | other
      direction: increase | decrease | maintain | threshold | qualitative
      baseline: string | null
      target: string | null
      note: string | null
  horizon: short | medium | long | deadline_driven
  deadline: date | null
  dependencies: [id]
  tensions: [id]
  uncertainties: [id]
  confidence: low | moderate | high
  priority: critical | high | moderate
```

Detta är ett semantiskt kontrakt; formellt schema skapas senare.

## Guardrails

- Skapa inte mål direkt från trendlistan.
- Använd inte specifik produkt eller plattform som mål utan exceptionell och explicit motivering.
- Gör inte aktiviteter till mål.
- Hitta inte på baslinjer eller numeriska målvärden.
- Skapa inte fler mål bara för att täcka varje analysområde.
- Låt inte ett mål bli bredare än att det går att följa upp och härleda.
- Låt inte svag evidens bära ett högsäkerhetsmål utan att osäkerheten syns.

## Utdata

Fasen ska producera:

1. **Kandidatlista över IT-strategiska mål** med spårbarhet till utmaningar och verksamhetsmål.
2. **Konsoliderat målramverk** med prioriterade kärnmål.
3. **Mål–utmaningsmatris** som visar vilka strategiska frågor varje mål adresserar.
4. **Preliminära indikatorer och tidshorisont** för varje mål.
5. **Målspänningar, beroenden och informationsluckor** som nästa steg behöver hantera.

## Kvalitetsgrind

Steget är tillräckligt genomfört när:

- varje kärnmål uttrycker effekt eller förmåga snarare än aktivitet eller teknikval,
- varje mål är spårbart till minst en prioriterad strategisk utmaning och relevant verksamhetskontext,
- kritiska och högprioriterade utmaningar är rimligt täckta eller uttryckligen undantagna med motivering,
- målen har preliminära indikatorer utan påhittade baslinjer,
- tidshorisont och prioritet är tydliga,
- överlappande mål har konsoliderats,
- målkonflikter och beroenden är synliga,
- målramverket är tillräckligt begränsat för att kunna styra senare vägval.

När grinden är passerad får nästa fas formulera **strategiska vägval och principer** som beskriver hur myndigheten bör agera för att nå målen.
