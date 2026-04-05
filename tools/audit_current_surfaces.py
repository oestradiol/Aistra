from __future__ import annotations
import sys
sys.dont_write_bytecode = True
import json
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
REGISTRY_PATH = BASE / 'governance' / 'CURRENT_SURFACES_REGISTRY_v0_1.json'
REPORT_PATH = BASE / 'archive' / 'reports' / 'generated' / 'current_surface_audit_report_v0_1.json'
TEXT_SUFFIXES = {'.md', '.txt', '.json', '.js', '.py', '.html', '.css'}


def load_json(path: Path):
    return json.loads(path.read_text(encoding='utf-8'))


def run_audit() -> dict:
    registry = load_json(REGISTRY_PATH)
    issues = []
    checks = []

    def record(name: str, ok: bool, detail: str = ''):
        checks.append({'check': name, 'ok': ok, 'detail': detail})
        if not ok:
            issues.append({'check': name, 'detail': detail})

    current = registry['current_truth_surfaces'] + registry.get('current_supporting_surfaces', [])
    forbidden = registry.get('forbidden_in_current_surfaces', [])
    package_name = registry['package_name']
    package_version = registry['package_version']

    for rel in current:
        p = BASE / rel
        record(f'exists:{rel}', p.exists(), 'present' if p.exists() else 'missing')
        if not p.exists() or p.suffix not in TEXT_SUFFIXES:
            continue
        text = p.read_text(encoding='utf-8', errors='ignore')
        if rel not in {'governance/CURRENT_SURFACES_REGISTRY_v0_1.json', 'governance/CURRENT_CLAIM_EXPECTATIONS_v0_1.json'}:
            for bad in forbidden:
                record(f'forbidden:{rel}:{bad}', bad not in text, f'found forbidden marker {bad!r}' if bad in text else 'ok')
        if p.suffix == '.md':
            record(
                f'current-name:{rel}',
                package_name.lower() in text.lower() or 'route 1' in text.lower() or 'current' in text.lower(),
                'current surface too generic',
            )

    state = load_json(BASE / 'governance' / 'PACKAGE_STATE_SUMMARY_v0_1.json')
    record('state:package-name', state.get('package_name') == package_name, f"package_name={state.get('package_name')}")
    record('state:version', state.get('version') == package_version, f"version={state.get('version')}")

    readme = (BASE / 'README.md').read_text(encoding='utf-8')
    start = (BASE / 'START_HERE.md').read_text(encoding='utf-8')
    operator = (BASE / 'docs/frontdoor/CURRENT_OPERATOR_START_HERE.md').read_text(encoding='utf-8')
    guide = (BASE / 'docs/frontdoor/HUMAN_PILOT_PACK_GUIDE.md').read_text(encoding='utf-8')
    handoff = (BASE / 'docs/frontdoor/HANDOFF_GUIDE.md').read_text(encoding='utf-8')
    record('link:readme-start', 'START_HERE.md' in readme, 'README missing START_HERE.md')
    record('link:start-guide', 'HUMAN_PILOT_PACK_GUIDE.md' in start, 'START_HERE missing guide')
    record('link:start-grounding', 'SCIENTIFIC_GROUNDING.md' in start, 'START_HERE missing scientific grounding')
    record('link:operator-guide', 'HUMAN_PILOT_PACK_GUIDE.md' in operator, 'operator guide path stale')
    record('link:guide-start', 'START_HERE.md' in guide, 'human guide start path stale')
    record('link:handoff-current', 'CURRENT_OPERATOR_START_HERE.md' in handoff and 'HUMAN_PILOT_PACK_GUIDE.md' in handoff, 'handoff guide paths stale')

    report = {
        'status': 'PASS' if not issues else 'FAIL',
        'package_name': package_name,
        'package_version': package_version,
        'total_checks': len(checks),
        'failed_checks': len(issues),
        'issues': issues,
        'checks': checks,
    }
    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    REPORT_PATH.write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    return report


def main():
    report = run_audit()
    print(json.dumps({k: report[k] for k in ['status', 'package_name', 'package_version', 'total_checks', 'failed_checks', 'issues']}, ensure_ascii=False, indent=2))
    raise SystemExit(0 if report['status'] == 'PASS' else 1)


if __name__ == '__main__':
    main()
