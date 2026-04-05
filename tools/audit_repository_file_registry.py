from __future__ import annotations
import sys
sys.dont_write_bytecode = True
import json
import shutil
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
REGISTRY_PATH = BASE / 'governance' / 'REPOSITORY_FILE_REGISTRY_v0_1.json'
CURRENT_SURFACES_PATH = BASE / 'governance' / 'CURRENT_SURFACES_REGISTRY_v0_1.json'
ROOT_ALLOWLIST_PATH = BASE / 'governance' / 'ROOT_ALLOWLIST_v0_1.json'
REPORT_PATH = BASE / 'reports' / 'generated' / 'repository_file_registry_audit_report_v0_1.json'
VALID_ROLES = {
    'current_truth',
    'current_support',
    'governance_current',
    'governance_support',
    'authoritative_asset',
    'tooling_current',
    'test_asset',
    'generated_output',
    'historical_trace',
    'example_asset',
    'research_support',
}


def load_json(path: Path):
    return json.loads(path.read_text(encoding='utf-8'))


def cleanup_transient_bytecode(base: Path):
    removed_dirs = []
    removed_files = []
    for pycache in sorted(base.rglob("__pycache__")):
        if pycache.is_dir():
            shutil.rmtree(pycache)
            removed_dirs.append(str(pycache.relative_to(base)))
    for pyc in sorted(base.rglob("*.pyc")):
        if pyc.is_file():
            pyc.unlink()
            removed_files.append(str(pyc.relative_to(base)))
    return removed_dirs, removed_files


def all_files(base: Path) -> list[str]:
    files = []
    for p in base.rglob('*'):
        if not p.is_file():
            continue
        rel = str(p.relative_to(base)).replace('\\', '/')
        if rel.startswith('reports/generated/') and rel != 'reports/generated/README.md':
            continue
        files.append(rel)
    return sorted(files)


def run_audit() -> dict:
    removed_dirs, removed_files = cleanup_transient_bytecode(BASE)
    registry = load_json(REGISTRY_PATH)
    current = load_json(CURRENT_SURFACES_PATH)
    root_allow = load_json(ROOT_ALLOWLIST_PATH)
    actual_files = all_files(BASE)
    entries = registry.get('entries', [])
    issues = []
    checks = []

    def record(name: str, ok: bool, detail: str = ''):
        checks.append({'check': name, 'ok': ok, 'detail': detail})
        if not ok:
            issues.append({'check': name, 'detail': detail})

    by_path: dict[str, dict] = {}
    dups = []
    for entry in entries:
        path = entry.get('path')
        if path in by_path:
            dups.append(path)
        else:
            by_path[path] = entry
    record('registry:no-duplicate-paths', not dups, f'duplicates={dups}')
    record('layout:transient-bytecode-clean', len(removed_dirs) == 0 and len(removed_files) == 0, f"removed_dirs={len(removed_dirs)} removed_pyc={len(removed_files)}")

    missing_from_registry = [p for p in actual_files if p not in by_path]
    extra_in_registry = [p for p in by_path if p not in actual_files]
    record('registry:covers-all-files', not missing_from_registry, f'missing_from_registry={missing_from_registry[:20]} count={len(missing_from_registry)}')
    record('registry:no-phantom-files', not extra_in_registry, f'extra_in_registry={extra_in_registry[:20]} count={len(extra_in_registry)}')

    for path, entry in sorted(by_path.items()):
        role = entry.get('role')
        just = str(entry.get('justification', '')).strip()
        record(f'entry:{path}:valid-role', role in VALID_ROLES, f'role={role}')
        record(f'entry:{path}:justified', bool(just), 'empty justification')
        if role == 'historical_trace':
            allowed_hist = path.startswith(('deprecated/', 'docs/history/'))
            record(f'entry:{path}:historical-placement', allowed_hist, 'historical file outside approved historical zones')
        if role in {'current_truth', 'current_support'}:
            record(f'entry:{path}:not-in-historical-zones', not path.startswith(('deprecated/', 'docs/history/')), 'current file placed in historical zone')
        if path.count('/') == 0:
            allowed_root = path in {row.get('path') for row in root_allow.get('allowed_root_files', [])}
            record(f'entry:{path}:root-allowlisted', allowed_root, 'root file not allowlisted')

    current_paths = set(current.get('current_truth_surfaces', []) + current.get('current_supporting_surfaces', []))
    for path in current_paths:
        entry = by_path.get(path)
        record(f'current-surface:{path}:registered', entry is not None, 'missing registry entry')
        if entry is not None:
            record(f'current-surface:{path}:role-valid', entry.get('role') in {'current_truth', 'current_support', 'governance_current', 'governance_support'}, f"role={entry.get('role')}")

    report = {
        'status': 'PASS' if not issues else 'FAIL',
        'package_name': registry.get('package_name'),
        'package_version': registry.get('package_version'),
        'total_files': len(actual_files),
        'registered_files': len(by_path),
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
    print(json.dumps({k: report[k] for k in ['status', 'package_name', 'package_version', 'total_files', 'registered_files', 'total_checks', 'failed_checks', 'issues']}, ensure_ascii=False, indent=2))
    raise SystemExit(0 if report['status'] == 'PASS' else 1)


if __name__ == '__main__':
    main()
