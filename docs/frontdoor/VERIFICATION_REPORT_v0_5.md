# Verification report v0.5

## Scope
- compares current package tree against the original uploaded zip
- confirms current doctor, launch gate, regression tests, and adversarial suite state
- notes external reference limitations

## External reference note
- requested SUF GitHub repo review could not be performed because no matching connected repository was accessible during this session.
- no repository-derived changes were made; all fixes were based on the package itself and the observed pilot workflow.

## Core check status
- `python package_doctor.py` → PASS
- `python route1_launch_gate.py` → PASS
- `python tests/run_route1_regression_tests.py` → PASS
- adversarial suite report indicates `n_failed = 0`

## Diff against original uploaded zip
- added files: 36
- removed files: 0
- changed files: 18
- unchanged files: 102

### Major intentional changes in v0.5
- cleaned front door and archived historical handoff docs under `deprecated/handoff_history_v0_1/`
- added `../START_HERE_v0_7.md` and skeptical audit doc
- made packet config generation reproducible with digests
- fixed alternate-aware scoring path in both browser app and local scorer
- updated package-level state docs to reflect that Route 1 has had an initial pilot

### No semantic Route 1 packet drift in v0.5
- structured packet remains `../core/route1/pilot_packet_route1_v0_3_final.jsonl`
- answer key remains `../core/route1/pilot_answer_key_route1_v0_4_alternate_aware.jsonl`
- v0.5 hardens packaging, scoring, provenance, and front-door clarity rather than changing task semantics

## Machine-readable diff summary
- `verification_outputs/integrity/v0_5_diff_against_original_summary.json`


## v0.6 addendum

This release adds front-door status surfaces only. No packet, answer key, parser, scorer, app logic, or regression semantics changed relative to v0.5. Existing integrity and regression results therefore remain applicable.


## v0.7 addendum

- `tools/audit_root_budget.py` added and intended to fail on unregistered root growth
- root allowlist and justification registry added under `governance/`
- transient `__pycache__` removed from package root

## v0.8 addendum

This release performs a structural file-tree refactor rather than a semantic Route 1 change. The following were revalidated after the move:
- `python package_doctor.py`
- `python route1_launch_gate.py`
- `python tests/run_route1_regression_tests.py`
- `python tools/audit_root_budget.py`

Root file count after refactor: **5**.

No Route 1 packet or answer-key semantics were intentionally changed by the refactor.


## v0.9 addendum

- added front-door purpose/use-case surface
- added single-file coherence and control surface
- added project naming decision (`Aistra`) without mass path rename
- added anti-slop trust/style policy for front-door language
- updated README and START_HERE sequencing to surface purpose, controls, and trust policy earlier
