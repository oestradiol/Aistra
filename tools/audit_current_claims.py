from __future__ import annotations
import sys
sys.dont_write_bytecode = True
import json
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
EXPECT_PATH = BASE / 'governance' / 'CURRENT_CLAIM_EXPECTATIONS_v0_1.json'
REPORT_PATH = BASE / 'reports' / 'generated' / 'current_claim_audit_report_v0_1.json'

def run_audit() -> dict:
    data = json.loads(EXPECT_PATH.read_text(encoding='utf-8'))
    issues=[]; checks=[]
    def record(name, ok, detail=''):
        checks.append({'check':name,'ok':ok,'detail':detail})
        if not ok:
            issues.append({'check':name,'detail':detail})
    for rel, rules in data['expectations'].items():
        p = BASE / rel
        record(f'exists:{rel}', p.exists(), 'present' if p.exists() else 'missing')
        if not p.exists():
            continue
        text = p.read_text(encoding='utf-8', errors='ignore')
        for s in rules.get('must_contain_all', []):
            record(f'must-contain:{rel}:{s}', s in text, f'missing required phrase {s!r}' if s not in text else 'ok')
        for s in rules.get('must_not_contain_any', []):
            record(f'must-not-contain:{rel}:{s}', s not in text, f'found forbidden phrase {s!r}' if s in text else 'ok')
    report={'status':'PASS' if not issues else 'FAIL','total_checks':len(checks),'failed_checks':len(issues),'issues':issues,'checks':checks}
    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    REPORT_PATH.write_text(json.dumps(report, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
    return report

if __name__ == '__main__':
    r=run_audit()
    print(json.dumps({k:r[k] for k in ['status','total_checks','failed_checks','issues']}, ensure_ascii=False, indent=2))
    raise SystemExit(0 if r['status']=='PASS' else 1)
