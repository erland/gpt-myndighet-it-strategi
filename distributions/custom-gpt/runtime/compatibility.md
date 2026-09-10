# Compatibility – Custom GPT och Chat ZIP

## Gemensamt kärnbeteende

Båda distributionerna ska behålla samma identitet, 15-fasers strategiprocess, tre fasgrindar, källhierarki, evidens/spårbarhetsregler, lösningsneutralitet, mål-/vägvals-/förflyttningslogik, konsekvensanalys, färdplan och rapportkvalitetskrav.

## Nödvändiga skillnader

- **Instruktionsformat:** Chat ZIP använder hela canonical instruktionen. Custom GPT använder en kompilerad instruktion under projektets 8 000-teckensgräns.
- **Knowledge:** Chat ZIP kan bära schemas och runtime-policyer i paketet. Custom GPT använder sju kuraterade metodfiler som Knowledge; JSON Schemas är projekt-/testkontrakt och behöver inte laddas upp som Knowledge.
- **Startmekanism:** Chat ZIP har `START-HERE.md`. Custom GPT startas genom sin konfiguration och conversation starters.
- **Capabilities:** Custom GPT ska ha web browsing aktiverat och data analysis rekommenderat. Actions och image generation krävs inte.

## Kända begränsningar

Den kompilerade instruktionen innehåller mindre metodförklaring och färre detaljerade exempel än canonical-filen. Kritiska guardrails och arbetsflödet måste däremot vara bevarade. Slutlig beteendeparitet verifieras i steg 25.
