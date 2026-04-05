from __future__ import annotations
import sys
sys.dont_write_bytecode = True
import json
import re
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
EXPECT_PATH = BASE / 'governance' / 'CURRENT_CLAIM_EXPECTATIONS_v0_1.json'
REPORT_PATH = BASE / 'archive' / 'reports' / 'generated' / 'current_claim_audit_report_v0_1.json'


def _search_pattern(pattern: str, text: str, *, ignore_case: bool = True):
    flags = re.IGNORECASE if ignore_case else 0
    try:
        compiled = re.compile(pattern, flags=flags)
    except re.error as e:
        return None, f'invalid regex {pattern!r}: {e}'
    return compiled.search(text), ''


def run_audit() -> dict:
    data = json.loads(EXPECT_PATH.read_text(encoding='utf-8'))
    issues = []
    checks = []

    def record(name, ok, detail=''):
        checks.append({'check': name, 'ok': ok, 'detail': detail})
        if not ok:
            issues.append({'check': name, 'detail': detail})

    for rel, rules in data['expectations'].items():
        p = BASE / rel
        record(f'exists:{rel}', p.exists(), 'present' if p.exists() else 'missing')
        if not p.exists():
            continue
        text = p.read_text(encoding='utf-8', errors='ignore')
        text_ci = text.casefold()
        for s in rules.get('must_contain_all', []):
            record(f'must-contain:{rel}:{s}', s in text, f'missing required phrase {s!r}' if s not in text else 'ok')
        for s in rules.get('must_not_contain_any', []):
            record(f'must-not-contain:{rel}:{s}', s not in text, f'found forbidden phrase {s!r}' if s in text else 'ok')
        for s in rules.get('must_not_contain_any_ci', []):
            s_ci = s.casefold()
            record(
                f'must-not-contain-ci:{rel}:{s}',
                s_ci not in text_ci,
                f'found forbidden phrase {s!r} (case-insensitive)' if s_ci in text_ci else 'ok',
            )
        for idx, rule in enumerate(rules.get('must_satisfy_any_regex', []), start=1):
            patterns = rule.get('patterns', []) if isinstance(rule, dict) else [str(rule)]
            ignore_case = rule.get('ignore_case', True) if isinstance(rule, dict) else True
            matched = False
            invalid_errors = []
            for pattern in patterns:
                match, error = _search_pattern(pattern, text, ignore_case=ignore_case)
                if error:
                    invalid_errors.append(error)
                    continue
                if match is not None:
                    matched = True
                    break
            if invalid_errors:
                detail = '; '.join(invalid_errors)
            elif matched:
                detail = 'ok'
            else:
                detail = (
                    rule.get('description') if isinstance(rule, dict) and rule.get('description') else f'none of the required regex patterns matched: {patterns!r}'
                )
            record(
                f'must-satisfy-any-regex:{rel}:{idx}',
                matched and not invalid_errors,
                detail,
            )
        for idx, rule in enumerate(rules.get('must_not_match_regex_any', []), start=1):
            pattern = rule['pattern'] if isinstance(rule, dict) else str(rule)
            ignore_case = rule.get('ignore_case', True) if isinstance(rule, dict) else True
            match, error = _search_pattern(pattern, text, ignore_case=ignore_case)
            if error:
                record(
                    f'must-not-match-regex:{rel}:{idx}',
                    False,
                    error,
                )
                continue
            matched = match is not None
            record(
                f'must-not-match-regex:{rel}:{idx}',
                not matched,
                f'regex matched forbidden content: {pattern!r}' if matched else 'ok',
            )

    report = {
        'status': 'PASS' if not issues else 'FAIL',
        'total_checks': len(checks),
        'failed_checks': len(issues),
        'issues': issues,
        'checks': checks,
    }
    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    REPORT_PATH.write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    return report


if __name__ == '__main__':
    r = run_audit()
    print(json.dumps({k: r[k] for k in ['status', 'total_checks', 'failed_checks', 'issues']}, ensure_ascii=False, indent=2))
    raise SystemExit(0 if r['status'] == 'PASS' else 1)
