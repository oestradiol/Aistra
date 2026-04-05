#!/usr/bin/env python3
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
ALLOWLIST = ROOT / 'governance' / 'ROOT_ALLOWLIST_v0_1.json'
REGISTRY = ROOT / 'governance' / 'FILE_JUSTIFICATION_REGISTRY_v0_1.json'


def main() -> int:
    allow = json.loads(ALLOWLIST.read_text(encoding='utf-8'))
    reg = json.loads(REGISTRY.read_text(encoding='utf-8'))
    allowed = {e['path'] for e in allow['allowed_root_files']}
    actual_files = {p.name for p in ROOT.iterdir() if p.is_file()}
    unallowed = sorted(actual_files - allowed)
    missing = sorted(allowed - actual_files)
    reg_paths = {e['path'] for e in reg['entries'] if e['type'] == 'file'}
    unjustified = sorted(actual_files - reg_paths)

    ok = not unallowed and not unjustified
    print('ROOT_BUDGET_OK=' + ('1' if ok else '0'))
    print('actual_root_files=' + str(len(actual_files)))
    print('allowed_root_files=' + str(len(allowed)))
    if unallowed:
        print('unallowed_root_files:')
        for x in unallowed:
            print(' - ' + x)
    if unjustified:
        print('unjustified_root_files:')
        for x in unjustified:
            print(' - ' + x)
    if missing:
        print('allowlisted_but_missing:')
        for x in missing:
            print(' - ' + x)
    return 0 if ok else 1


if __name__ == '__main__':
    raise SystemExit(main())
