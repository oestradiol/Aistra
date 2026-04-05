# Skeptical audit and hardening

This file is the package speaking to its own strongest critics.

## Main risks that still matter
1. A current file can still be misleading in a subtle way even if it passes lexical stale-name checks.
2. File governance can prove that every file has a stated job without proving that the package is globally minimal.
3. Integrity checks prove alignment with the declared package state, not that the declared state is scientifically correct.
4. Route 1 engineering reliability is much stronger than broad human validity.
5. AI-assisted editing can still produce coherent but conceptually weak changes.
6. Current Route 1 performance can still overfit the shipped packet if familiar and holdout performance are not separated.
7. The 9-field ontology can still be wrong in structure even if the package around it is coherent.
8. The local interface can reduce paraphrase drift while still shaping responses through examples, instruction load, or fatigue.
9. The adversarial suite is strong on known failure classes, not yet complete for open-world human weirdness.
10. Anti-drift governance can make deep ontology revision expensive if change and migration rules stay implicit.

## What is already in place against those risks
- current-vs-historical file roles are explicit
- repo-wide file existence and justification are audited
- packet, key, config, and scorer are checked for alignment
- current front-door files are checked for stale names and stale links
- research-grounding and validity docs keep the scientific claims bounded
- current execution order now treats holdout packet review, interface-effect logging, and failure harvesting as live next-step work rather than vague future concerns
- field rationale docs now state revision triggers and require migration planning before ontology changes
- pilot review already has a place to record fatigue, wording ambiguity, ontology mismatch, and token usability

## What is still true even after all that
- Route 1 is still a prototype route, not finished science
- external validity across naive users is still unproven
- source and certainty remain the most interpretation-sensitive fields
- future changes can still introduce new failure modes that current checks do not yet know about
- familiar-vs-holdout generalization has to be measured, not inferred from clean pilot behavior
- interface distortion and weird-but-valid cases still need more real human evidence

## Bottom line
The package is much harder to drift by accident than before. It is not a zero-risk system.


Latest hardening additions:
- `tools/audit_current_claims.py` checks current-package claim shape and bounded scientific posture on key live files.
- `tools/audit_repository_minimality.py` keeps historical and generated zones under explicit size pressure so governance cannot justify endless growth.
- current docs now explicitly bind ontology revision to evidence plus migration planning rather than informal future judgment.
