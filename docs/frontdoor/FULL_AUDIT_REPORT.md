# Full audit report v1.11

Current package version: **1.11.0**.

## Main release-cleaning actions
- strengthened current-surface governance so live docs are checked separately from historical trace files
- removed historical handoff guides and audit memos whose useful content had already been extracted into current docs
- removed shipped generated verification artifacts that can be reproduced on demand
- removed stored pilot run outputs that were not needed for operation or release verification
- consolidated the useful development story into `../history/DEVELOPMENT_HISTORY.md`
- moved generated report outputs to `../../archive/reports/generated/`
- simplified several current front-door docs to reduce over-produced or compliance-heavy tone
- added a front-door scientific grounding summary so the research layer is visible without digging
- enforced a repository-wide file registry so every shipped file keeps an explicit role and justification

## Release judgment
This is a cleaner package than the previous release line because it keeps the current logic, specs, and research layer while dropping extra historical clutter.

## Remaining honest limits
- the package is still a prototype package, not finished science
- Route 1 still needs broader multi-user validation
- Route 2 is still pre-human
- future edits can still create new failure modes that current checks do not yet encode


Latest hardening additions:
- `tools/audit_current_claims.py` checks current-package claim shape and bounded scientific posture on key live files.
- `tools/audit_repository_minimality.py` keeps historical and generated zones under explicit size pressure so governance cannot justify endless growth.
