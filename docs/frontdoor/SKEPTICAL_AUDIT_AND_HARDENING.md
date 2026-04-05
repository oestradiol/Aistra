# Skeptical audit and hardening

This file is the package speaking to its own strongest critics.

## Main risks that still matter
1. A current file can still be misleading in a subtle way even if it passes lexical stale-name checks.
2. File governance can prove that every file has a stated job without proving that the package is globally minimal.
3. Integrity checks prove alignment with the declared package state, not that the declared state is scientifically correct.
4. Route 1 engineering reliability is much stronger than broad human validity.
5. AI-assisted editing can still produce coherent but conceptually weak changes.

## What is already in place against those risks
- current-vs-historical file roles are explicit
- repo-wide file existence and justification are audited
- packet, key, config, and scorer are checked for alignment
- current front-door files are checked for stale names and stale links
- research-grounding and validity docs keep the scientific claims bounded

## What is still true even after all that
- Route 1 is still a prototype route, not finished science
- external validity across naive users is still unproven
- source and certainty remain the most interpretation-sensitive fields
- future changes can still introduce new failure modes that current checks do not yet know about

## Bottom line
The package is much harder to drift by accident than before. It is not a zero-risk system.


Latest hardening additions:
- `tools/audit_current_claims.py` checks current-package claim shape and bounded scientific posture on key live files.
- `tools/audit_repository_minimality.py` keeps historical and generated zones under explicit size pressure so governance cannot justify endless growth.
