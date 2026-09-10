# Steg 27 – validering

**Resultat:** PASS

Leveranser:

- `.github/workflows/ci.yml`
- `requirements-ci.txt`
- `scripts/validate-project.py`
- `scripts/validate-hygiene.py`

CI-flödet kör från ett rent checkout:

1. installation av minimala valideringsberoenden,
2. projektlint,
3. JSON Schema-validering,
4. research-/källtester,
5. strategiska härledningstester,
6. end-to-end-test,
7. runtime-paritetsvalidering,
8. source hygiene före build,
9. build av Chat ZIP och Custom GPT ZIP,
10. ZIP CRC- och SHA-256-verifiering,
11. uppladdning av runtime-artefakterna som GitHub Actions-artifact.

Lokalt verifierat i en kopia av källträdet utan `dist/`. Genererade runtime-artefakter ingår inte i projektkällan.
