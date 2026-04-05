# Handoff guide v1.10

This file explains how to hand the live package to another person without sending them into stale files.

Read in this order:
1. `../../START_HERE.md`
2. `CURRENT_OPERATOR_START_HERE.md`
3. `SCIENTIFIC_GROUNDING.md`
4. `../../governance/AUTHORITATIVE_INDEX_v0_1.md`
5. `HUMAN_PILOT_PACK_GUIDE.md`

For Route 1 pilot use:
- run `python package_doctor.py`
- run `python route1_launch_gate.py`
- use `python tools/run_route1_current_ops.py --responses <filled_response.json> --run-dir <outdir>` for scoring

For release checks:
- run `python tests/run_route1_regression_tests.py`
- run `python tools/audit_root_budget.py`
- run `python tools/audit_current_surfaces.py`
- run `python tools/audit_repository_file_registry.py`
- run `python tools/audit_current_claims.py`
- run `python tools/audit_repository_minimality.py`
- run `python adversarial_suite_v0_1/run_adversarial_suite.py`

Current truth surfaces:
- `../state/PROJECT_STATUS.md`
- `../state/CURRENT_EXECUTION_ORDER.md`
- `VERIFICATION_REPORT.md`
- `FULL_AUDIT_REPORT.md`

Historical trace lives under `../../deprecated/` and `../history/`.
