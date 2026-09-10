# Steg 28 – validering

## Resultat

PASS.

## Kontrakt

- GitHub Release-taggen är enda versionskälla för release-builden.
- Build sker i temporär staged kopia och muterar inte utvecklingskällans VERSION.
- Projekt-ZIP, Chat ZIP och Custom GPT ZIP produceras.
- Individuella SHA-256-filer och SHA256SUMS.txt produceras.
- Samma lint-, schema-, research-, härlednings-, end-to-end-, runtime-paritets- och hygiene-kontroller körs före build.
- Publicerad GitHub Release får artefakterna bifogade via GitHub CLI.
- Workflow_dispatch kan verifiera en befintlig tagg utan att kräva en ny release.
