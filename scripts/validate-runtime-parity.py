#!/usr/bin/env python3
from __future__ import annotations
from pathlib import Path
import hashlib, json, sys, yaml

ROOT = Path(__file__).resolve().parents[1]
CANON = ROOT/'src/instructions/system.md'
CHAT = ROOT/'distributions/chat/runtime/assistant/instructions.md'
CUSTOM = ROOT/'distributions/custom-gpt/runtime/instructions.md'
CFG = ROOT/'distributions/custom-gpt/runtime/custom-gpt-config.yaml'

errors=[]
notes=[]

def check(cond,msg):
    if not cond: errors.append(msg)

canon=CANON.read_text(encoding='utf-8')
chat=CHAT.read_text(encoding='utf-8')
custom=CUSTOM.read_text(encoding='utf-8')
config=yaml.safe_load(CFG.read_text(encoding='utf-8'))

check(canon==chat,'Chat-instruktionen är inte byte-identisk med canonical instruktion')
check(len(custom)<=8000,f'Custom GPT-instruktionen överskrider gränsen: {len(custom)}')

# Semantiska kontraktsmarkörer som måste finnas i den kompilerade Custom GPT-instruktionen.
contract_markers = {
  'identity_scope': ['IT-strateg för svenska myndigheter','källspårbar, myndighetsanpassad IT-strategi'],
  'source_priority': ['Myndighetsspecifik evidens väger tyngre','Nyare betyder inte automatiskt starkare'],
  'claim_separation': ['Skilj fakta, analys, rekommendation, antagande och informationslucka'],
  'traceability': ['Observation → källa → betydelse → strategisk konsekvens → rekommendation'],
  'evidence_strength': ['Rekommendationens styrka får inte överstiga evidensen'],
  'trend_guardrail': ['Låt inte AI, moln, zero trust, plattformar, API-first'],
  'product_guardrail': ['Rekommendera inte specifika produkter eller detaljlösningar'],
  'no_fabrication': ['Hitta aldrig på baslinjer, målvärden, intern arkitektur, kostnader, kapacitet'],
  'web_research': ['Använd aktuell webbresearch','Kontrollera publiceringsdatum, giltighet'],
  'workflow': ['1. Identifiera myndigheten.','15. Skapa full strategi och ledningsversion.'],
  'next_step': ['När användaren säger ”fortsätt” eller ”gör nästa steg”'],
  'phase_gates': ['Strategisk syntes får inte börja','Mål och vägval får inte fastställas','Slutrapporten är inte färdig'],
  'business_first': ['innan IT-lösningar diskuteras'],
  'capacity_realism': ['Skilj finansiering från faktisk genomförandekapacitet'],
  'state_uncertainty': ['skilj dokumenterat nuläge, beslutad förändring, observerad förändring och infererat nuläge'],
  'environment_selectivity': ['För relevanta signaler bedöm mognad, tidshorisont, myndighetskoppling'],
  'solution_neutral_goals': ['formulera önskad framtida effekt eller förmåga, inte aktivitet eller teknikval'],
  'alternatives_tradeoffs': ['jämför meningsfulla alternativ och trade-offs'],
  'transformation_contract': ['nuläge → önskat läge → strategisk förflyttning → effekt → beroenden → risker → prioritet → tidshorisont'],
  'bidirectional_consequence': ['Låt konsekvensanalysen kunna ändra mål, vägval, omfattning, sekvensering eller tidshorisont'],
  'roadmap_followup': ['Skilj effekt-, förmåge/mognads-, genomförande- och riskindikatorer'],
  'report_parity': ['Ledningsversionen ska vara en kort beslutsorienterad destillation','får aldrig introducera nya eller starkare fakta'],
  'quality_gate': ['myndighetsspecifik, styrningsförankrad, källspårbar'],
  'knowledge_boundary': ['Kritiska regler finns här och får inte göras beroende av att en viss Knowledge-fil läses'],
}
for cid, markers in contract_markers.items():
    missing=[m for m in markers if m not in custom]
    check(not missing, f'Custom GPT saknar kontrakt {cid}: {missing}')

# Knowledge-paritet: samma sju filer och identiskt innehåll.
chat_k={p.name:p for p in (ROOT/'distributions/chat/runtime/knowledge').glob('*.md')}
custom_k={p.name:p for p in (ROOT/'distributions/custom-gpt/runtime/knowledge').glob('*.md')}
check(set(chat_k)==set(custom_k),f'Knowledge-filuppsättningen skiljer sig: chat={sorted(chat_k)} custom={sorted(custom_k)}')
for name in sorted(set(chat_k)&set(custom_k)):
    check(chat_k[name].read_bytes()==custom_k[name].read_bytes(),f'Knowledge skiljer sig för {name}')

# Capability-paritet där runtime-metoden kräver funktionalitet.
caps=config.get('capabilities',{})
check(caps.get('web_browsing',{}).get('enabled') is True,'Custom GPT web browsing är inte aktiverad')
check(caps.get('web_browsing',{}).get('required') is True,'Custom GPT web browsing är inte markerad required')
check(caps.get('data_analysis',{}).get('enabled') is True,'Custom GPT data analysis är inte aktiverad')
check(config.get('actions',{}).get('required') is False,'Custom GPT kräver oväntat Actions')

# Dokumenterade, accepterade plattformsskillnader.
notes.extend([
  'Chat ZIP använder full canonical instruktion; Custom GPT använder kompilerad instruktion <= 8 000 tecken.',
  'Chat ZIP inkluderar 11 JSON Schemas; Custom GPT Knowledge utelämnar dem eftersom de är projekt-/testkontrakt.',
  'Chat ZIP startar via START-HERE.md; Custom GPT via konfiguration och conversation starters.',
  'Chat ZIP kan bära runtime-policyfiler; Custom GPT håller kritiska regler direkt i den kompilerade instruktionen.',
])

result={
  'result':'FAIL' if errors else 'PASS',
  'canonical_chat_byte_parity': canon==chat,
  'custom_instruction_characters': len(custom),
  'custom_instruction_limit':8000,
  'behavior_contracts_total':len(contract_markers),
  'behavior_contracts_passed':len(contract_markers)-sum(1 for cid,ms in contract_markers.items() if any(m not in custom for m in ms)),
  'knowledge_files_chat':len(chat_k),
  'knowledge_files_custom':len(custom_k),
  'errors':errors,
  'accepted_platform_differences':notes,
}
print(json.dumps(result,ensure_ascii=False,indent=2))
sys.exit(1 if errors else 0)
