# Aistra package v1.10

Aistra is a small prototype language for describing human felt states in a more structured and testable way. Instead of treating a feeling as one vague blob, it breaks it into parts like valence, arousal, intensity, location, texture, contour, certainty, source, and action tendency. It is already real enough to run as a serious prototype, but it is still a prototype and not finished science.

## What this is for
Read `docs/frontdoor/PROJECT_PURPOSE_AND_USE_CASES.md` for the shortest honest summary of what the project is trying to do, what it is useful for right now, and what it does not claim.

## Why you should trust it at all
Read `docs/frontdoor/COHERENCE_AND_CONTROL_SURFACE.md` for the shortest map of the package safeguards, checks, and limits.
Read `docs/frontdoor/SCIENTIFIC_GROUNDING.md` for the shortest map of the research layer.

## Project name
The project and language name is **Aistra**. See `docs/frontdoor/NAME_DECISION.md`.

Current package posture:
- **Route 1**: `pilot_ready`, one initial human pilot completed, not broadly validated
- **Route 2**: `pre_human`

## Front door
Read in this order:
1. `START_HERE.md`
2. `docs/frontdoor/PROJECT_PURPOSE_AND_USE_CASES.md`
3. `docs/frontdoor/COHERENCE_AND_CONTROL_SURFACE.md`
4. `docs/frontdoor/SCIENTIFIC_GROUNDING.md`
5. `docs/state/PROJECT_STATUS.md`
6. `docs/state/CURRENT_EXECUTION_ORDER.md`
7. `docs/frontdoor/CURRENT_OPERATOR_START_HERE.md`
8. `docs/frontdoor/HUMAN_PILOT_PACK_GUIDE.md`
9. `governance/AUTHORITATIVE_INDEX_v0_1.md`
10. `docs/frontdoor/SKEPTICAL_AUDIT_AND_HARDENING.md`
11. `docs/frontdoor/TRUST_AND_STYLE_POLICY.md`

## Layout
- `docs/frontdoor/` = the shortest honest explanations, verification, and operator guidance
- `docs/state/` = current project posture and next-step sequencing
- `docs/specs/` = ontology, scoring, validity, and design docs
- `docs/ops/` = operator memos, instructions, checklists, and templates
- `docs/history/` = condensed development history worth keeping
- `core/route1/` = Route 1 assets and code
- `core/common/` = shared route-control code
- `human_pilot_app_v0_1/` = local Route 1 app
- `research_grounding_v0_1/` = literature-linked grounding and prehuman justification
- `governance/` = authoritative maps, integrity, and file-governance rules
- `reports/generated/` = regenerated check outputs and run reports

## Boundaries
- `examples/` are examples, not launch artifacts.
- `deprecated/` contains superseded material retained for traceability.
- `reports/generated/` contains generated reports, not canonical definitions.

## Minimum checks before use
- `python package_doctor.py`
- `python route1_launch_gate.py`

## Important
Use `START_HERE.md`, `governance/AUTHORITATIVE_INDEX_v0_1.md`, and `governance/AUTHORITATIVE_SOURCES_v0_2.json` to find the live files.


This is still not yet broadly validated science.
