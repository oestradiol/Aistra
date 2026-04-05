# Coherence and control surface

This is the shortest map of how the package tries to stay honest, stable, and hard to accidentally break.

## Core rule
No package claim should be stronger than the evidence and checks currently present in the package.

## How the package stays on the right files
Use these to see what is current and authoritative:
- `../../governance/AUTHORITATIVE_INDEX_v0_1.md`
- `../../governance/AUTHORITATIVE_SOURCES_v0_2.json`
- `../../governance/AUTHORITATIVE_INTEGRITY_MANIFEST_v0_1.json`
- `../../governance/CURRENT_SURFACES_REGISTRY_v0_1.json`

## How the package checks itself before use
Before Route 1 use:
- `python package_doctor.py`
- `python route1_launch_gate.py`

Before release:
- `python package_doctor.py`
- `python tests/run_route1_regression_tests.py`
- `python tools/audit_root_budget.py`
- `python tools/audit_current_surfaces.py`
- `python tools/audit_repository_file_registry.py`
- `python tools/audit_current_claims.py`
- `python tools/audit_repository_minimality.py`

## How the package resists file sprawl
- `../../governance/PACKAGE_MINIMIZATION_POLICY_v0_1.md`
- `../../governance/ROOT_ALLOWLIST_v0_1.json`
- `../../governance/FILE_JUSTIFICATION_REGISTRY_v0_1.json`
- `../../governance/REPOSITORY_FILE_REGISTRY_v0_1.json`

Rule: no file without a job, and no root file without explicit permission.

## How the package resists stale live docs
- `../../governance/CURRENT_SURFACES_REGISTRY_v0_1.json`
- `../../tools/audit_current_surfaces.py`
- `VERIFICATION_REPORT.md`
- `FULL_AUDIT_REPORT.md`

Rule: old files may stay old, but current files may not quietly drift.

## How the package stays scientifically aligned
- `SCIENTIFIC_GROUNDING.md`
- `../specs/VALIDITY_AND_LIMITS_v0_1.md`
- `../specs/FIELD_RATIONALE_REVIEW_v0_1.md`
- `../../research_grounding_v0_1/`

## How the route logic stays aligned
- `../specs/SCORING_SPEC_v0_1.md`
- `../../core/route1/pilot_answer_key_route1_v0_4_alternate_aware.jsonl`
- `../../tools/score_route1_human_pilot_export.py`
- `../../tests/run_route1_regression_tests.py`
- `../../adversarial_suite_v0_1/run_adversarial_suite.py`

## Honest limit
These controls are strong against many known mistakes. They do not guarantee perfection and they do not replace human judgment.
