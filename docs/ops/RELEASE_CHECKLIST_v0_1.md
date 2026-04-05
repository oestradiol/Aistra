# Release checklist

Use this before tagging or shipping a new bounded release.

Required checks:
- `python package_doctor.py`
- `python route1_launch_gate.py`
- `python tests/run_route1_regression_tests.py`
- `python tools/audit_root_budget.py`
- `python tools/audit_current_surfaces.py`
- `python tools/audit_repository_file_registry.py`
- `python tools/audit_current_claims.py`
- `python tools/audit_repository_minimality.py`
- `python adversarial_suite_v0_1/run_adversarial_suite.py`

Manual checks:
- read `README.md` and `START_HERE.md` cold
- confirm the front door still sounds plain, bounded, and edited rather than inflated
- confirm current docs do not point to historical files
- confirm current verification and audit reports describe the live package state
- confirm current docs still match the research-grounding layer in spirit and boundary
- confirm any renamed current files are reflected in `governance/CURRENT_SURFACES_REGISTRY_v0_1.json` and `governance/AUTHORITATIVE_INDEX_v0_1.md`

Release rule:
Do not call the package release-clean unless both the automated checks and the manual current-surface pass succeed.

Additional release posture rule:
- do not ship extra generated reports, cached bytecode, or retained local run outputs
- if deprecated or history zones grow, rerun a pruning pass before release
