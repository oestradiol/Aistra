# Start Here v1.1

This package was refactored to reduce root-folder sprawl. Use these files in order:

1. `README.md`
2. `docs/frontdoor/PROJECT_PURPOSE_AND_USE_CASES_v0_1.md`
3. `docs/frontdoor/COHERENCE_AND_CONTROL_SURFACE_v0_1.md`
4. `docs/state/PROJECT_STATUS_v0_1.md`
5. `docs/state/CURRENT_EXECUTION_ORDER_v0_1.md`
6. `docs/frontdoor/CURRENT_OPERATOR_START_HERE_v0_1.md`
7. `docs/frontdoor/HUMAN_PILOT_PACK_GUIDE_v0_5.md`
8. `governance/AUTHORITATIVE_INDEX_v0_1.md`
9. `docs/frontdoor/SKEPTICAL_AUDIT_AND_HARDENING_v0_1.md`
10. `docs/frontdoor/ANTI_SLOP_TRUST_AND_STYLE_POLICY_v0_1.md`

Name: **Aistra**

Structure summary:
- `docs/frontdoor/` = operator and handoff entry surfaces
- `docs/state/` = current package posture and execution order
- `docs/specs/` = ontology, scoring, validity, and design docs
- `docs/ops/` = operational memos, checklists, and protocol details
- `core/route1/` = Route 1 formal artifacts and core code
- `core/common/` = shared route-control assets
- `human_pilot_app_v0_1/` = local app
- `governance/` = authoritative maps, integrity ledger, minimization rules

Run before pilot use:
- `python package_doctor.py`
- `python route1_launch_gate.py`
