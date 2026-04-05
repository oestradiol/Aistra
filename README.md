# Aistra package v1.1

This package is a bounded, route-based prototype for structured experiential encoding.

Aistra is a small, carefully structured prototype language for describing human felt states in a clearer and more testable way. Instead of treating a feeling as one vague blob, it breaks it into parts like valence, arousal, intensity, location, texture, contour, certainty, source, and action tendency. The project is already real enough to run and hand off as a serious testable system, but it is still a prototype and not yet broadly validated science.


## What this is for
Read `docs/frontdoor/PROJECT_PURPOSE_AND_USE_CASES_v0_1.md` for the shortest explanation of the project point, current usefulness, and boundaries.

## Coherence and safeguards
Read `docs/frontdoor/COHERENCE_AND_CONTROL_SURFACE_v0_1.md` for the shortest map of constraints, methods, safeguards, validation surfaces, and handoff controls that keep the package stable.

## Project name
The project and language name is **Aistra**. See `docs/frontdoor/NAME_DECISION_v0_1.md`.

Current package posture:
- **Route 1**: `pilot_ready`, initial human pilot completed, not yet broadly validated
- **Route 2**: `pre_human`

## Clean front door
Read in this order:
1. `START_HERE_v0_7.md`
2. `docs/frontdoor/PROJECT_PURPOSE_AND_USE_CASES_v0_1.md`
3. `docs/frontdoor/COHERENCE_AND_CONTROL_SURFACE_v0_1.md`
4. `docs/state/PROJECT_STATUS_v0_1.md`
5. `docs/state/CURRENT_EXECUTION_ORDER_v0_1.md`
6. `docs/frontdoor/CURRENT_OPERATOR_START_HERE_v0_1.md`
7. `docs/frontdoor/HUMAN_PILOT_PACK_GUIDE_v0_5.md`
8. `governance/AUTHORITATIVE_INDEX_v0_1.md`
9. `docs/frontdoor/SKEPTICAL_AUDIT_AND_HARDENING_v0_1.md`
10. `docs/frontdoor/ANTI_SLOP_TRUST_AND_STYLE_POLICY_v0_1.md`

## Layout
- `docs/frontdoor/` = front-door guides, verification, handoff, skeptical audit
- `docs/state/` = current posture and live execution order
- `docs/specs/` = ontology, scoring, validity, design, and field rationale
- `docs/ops/` = route operation memos, instructions, checklists, templates
- `core/route1/` = Route 1 packet, answer key, parser, scorer, examples, gold data
- `core/common/` = shared route-control assets
- `human_pilot_app_v0_1/` = local app
- `governance/` = authoritative maps, integrity ledger, minimization policy

## Current routes
- **Route 1 — interoceptive-affective microstates**
  - status: `pilot_ready`
  - authoritative pilot packet: `core/route1/pilot_packet_route1_v0_3_final.jsonl`
  - authoritative answer key: `core/route1/pilot_answer_key_route1_v0_4_alternate_aware.jsonl`
  - local app: `human_pilot_app_v0_1/index.html`

- **Route 2 — visual phenomenological microstructures**
  - status: `pre_human`
  - citation-traceable pre-human grounding present

## Package boundaries
- `audits/` contains review history, not the operator path.
- `examples/` contains examples, not launch artifacts.
- `verification_outputs/` contains generated evidence, not canonical definitions.
- `deprecated/` contains superseded files retained for traceability.

## Enforcement layer
Before Route 1 pilot use, run:
- `python package_doctor.py`
- `python route1_launch_gate.py`

## Important
Do not assume older flattened root paths are current.
Use `START_HERE_v0_7.md`, `governance/AUTHORITATIVE_INDEX_v0_1.md`, and `governance/AUTHORITATIVE_SOURCES_v0_2.json` to identify current files.

## File governance
This package uses a file-budget rule to resist root-folder sprawl. See `governance/PACKAGE_MINIMIZATION_POLICY_v0_1.md` and run `tools/audit_root_budget.py` when changing package structure.
