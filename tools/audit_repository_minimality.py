from __future__ import annotations
import sys
sys.dont_write_bytecode = True
import json
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
POLICY = BASE / 'governance' / 'MINIMALITY_POLICY_v0_1.json'
REPORT = BASE / 'reports' / 'generated' / 'repository_minimality_report_v0_1.json'

def run_audit() -> dict:
    policy = json.loads(POLICY.read_text(encoding='utf-8'))
    issues=[]; checks=[]
    def record(name, ok, detail=''):
        checks.append({'check':name,'ok':ok,'detail':detail})
        if not ok:
            issues.append({'check':name,'detail':detail})
    root_files = [p for p in BASE.iterdir() if p.is_file()]
    history_files = [p for p in (BASE/'docs'/'history').rglob('*') if p.is_file()]
    deprecated_files = [p for p in (BASE/'deprecated').rglob('*') if p.is_file()]
    generated_files = [p for p in (BASE/'reports'/'generated').rglob('*') if p.is_file() and p.name == 'README.md']
    lim = policy['limits']
    record('limit:root-files', len(root_files) <= lim['max_root_files'], f'count={len(root_files)} limit={lim["max_root_files"]}')
    record('limit:history-files', len(history_files) <= lim['max_docs_history_files'], f'count={len(history_files)} limit={lim["max_docs_history_files"]}')
    record('limit:deprecated-files', len(deprecated_files) <= lim['max_deprecated_files'], f'count={len(deprecated_files)} limit={lim["max_deprecated_files"]}')
    record('limit:generated-files-shipped', len(generated_files) <= lim['max_reports_generated_files_shipped'], f'count={len(generated_files)} limit={lim["max_reports_generated_files_shipped"]}')
    report={'status':'PASS' if not issues else 'FAIL','counts':{'root_files':len(root_files),'history_files':len(history_files),'deprecated_files':len(deprecated_files),'generated_files':len(generated_files)},'total_checks':len(checks),'failed_checks':len(issues),'issues':issues,'checks':checks}
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.write_text(json.dumps(report, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
    return report

if __name__ == '__main__':
    r=run_audit()
    print(json.dumps({k:r[k] for k in ['status','counts','total_checks','failed_checks','issues']}, ensure_ascii=False, indent=2))
    raise SystemExit(0 if r['status']=='PASS' else 1)
