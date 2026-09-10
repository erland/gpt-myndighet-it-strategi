# Steg 19 – validering

**Resultat: PASS**

## Leverans

- 11 JSON Schema Draft 2020-12-kontrakt.
- Gemensam ID- och spårbarhetsmodell mellan arbetsobjekt.
- Maskinvaliderbara guardrails för lösningsneutralitet och projektnivå.
- Minimalt spårbarhetsexempel.
- `scripts/validate-schemas.py` för schemavalidering.

## Kontroller

- Alla schemafiler parsar som JSON.
- Alla schemafiler godkänns av Draft 2020-12 meta-schema-validering.
- Obligatoriska kärnfält finns för källor, evidens, strategiska frågor, mål, vägval, förflyttningar, färdplan, informationsluckor och status.
- Länkar mellan arbetsobjekt uttrycks med stabila ID:n.
- Scheman används som intern struktur och tvingar inte rå JSON i användarens slutrapport.
- Tidskänslig sakinformation har inte hårdkodats i schemana.

Nästa steg: **Steg 20 – Skapa tester för research och källhantering**.
