# Verification report v1.10

Current package version: **1.10.0**.

## What was checked
- package integrity and authoritative digests
- Route 1 launch readiness
- Route 1 regression tests
- root-budget audit
- current-surface audit
- repository file registry audit
- current-claim audit
- repository minimality audit
- adversarial suite

## What passed in the current release build
- `python package_doctor.py`
- `python route1_launch_gate.py`
- `python tests/run_route1_regression_tests.py`
- `python tools/audit_root_budget.py`
- `python tools/audit_current_surfaces.py`
- `python tools/audit_repository_file_registry.py`
- `python tools/audit_current_claims.py`
- `python tools/audit_repository_minimality.py`
- `python adversarial_suite_v0_1/run_adversarial_suite.py`

## What this means
The package is internally consistent, aligned to its declared current files, and protected against several known drift classes.

## What this does not mean
It does not mean the ontology is final.
It does not mean the science is finished.
It does not mean future edits cannot introduce new mistakes.


Latest hardening additions:
- `tools/audit_current_claims.py` checks current-package claim shape and bounded scientific posture on key live files.
- `tools/audit_repository_minimality.py` keeps historical and generated zones under explicit size pressure so governance cannot justify endless growth.
