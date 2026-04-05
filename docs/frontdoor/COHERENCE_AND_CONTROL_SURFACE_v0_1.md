# Coherence and Control Surface v0.1

This file is the shortest single-place summary of how the package stays coherent, stable, grounded, and self-audited.

## 1. Core control rule

No package claim should outrun the strongest evidence and validation surface currently present in the package.

## 2. Authoritative-source control

Use these files to identify what is canonical:

- `governance/AUTHORITATIVE_INDEX_v0_1.md`
- `governance/AUTHORITATIVE_SOURCES_v0_2.json`
- `governance/AUTHORITATIVE_INTEGRITY_MANIFEST_v0_1.json`

## 3. Launch control

Before Route 1 use, run:

- `python package_doctor.py`
- `python route1_launch_gate.py`

These are the front-door integrity checks.

## 4. Structural minimization control

To resist file sprawl and root-folder drift, the package uses:

- `governance/PACKAGE_MINIMIZATION_POLICY_v0_1.md`
- `governance/ROOT_ALLOWLIST_v0_1.json`
- `governance/FILE_JUSTIFICATION_REGISTRY_v0_1.json`
- `tools/audit_root_budget.py`

Rule: no file without a job; no root file without explicit permission.

## 5. Ontology control

The ontology is bounded and audited through:

- `docs/specs/ONTOLOGY_AUDIT_v0_1.md`
- `docs/specs/FIELD_RATIONALE_REVIEW_v0_1.md`
- `docs/specs/DESIGN_DECISION_NOTE_v0_1.md`

## 6. Scoring control

Scoring policy is formalized in:

- `docs/specs/SCORING_SPEC_v0_1.md`
- `core/route1/pilot_answer_key_route1_v0_4_alternate_aware.jsonl`
- `tools/score_route1_human_pilot_export.py`

## 7. Prompt-specification control

Baseline prompts are constrained through explicit field support:

- `docs/specs/BASELINE_FIELD_SUPPORT_MATRIX_v0_1.md`

## 8. Scientific-boundary control

The package states its limits in:

- `docs/specs/VALIDITY_AND_LIMITS_v0_1.md`
- `docs/state/PROJECT_STATUS_v0_1.md`

## 9. Regression control

Route 1 regression protection currently uses:

- `tests/run_route1_regression_tests.py`
- `adversarial_suite_v0_1/run_adversarial_suite.py`

## 10. Handoff control

Multi-user handoff is constrained through:

- `docs/ops/HANDOFF_PROTOCOL_v0_1.md`
- `docs/frontdoor/HUMAN_PILOT_PACK_GUIDE_v0_5.md`
- `docs/frontdoor/CURRENT_OPERATOR_START_HERE_v0_1.md`

## 11. Provenance control

The local app embeds packet and key provenance metadata. Exported pilot files can be checked against the authoritative packet/key/config lineage.

## 12. Status control

For current package posture and next-step sequencing, use:

- `docs/state/PROJECT_STATUS_v0_1.md`
- `docs/state/CURRENT_EXECUTION_ORDER_v0_1.md`

## 13. Honest posture rule

This package should read as:

- bounded
- explicit
- accountable
- testable
- revisable

It should not read as:

- universal proof
- complete science
- final ontology
- authority by verbosity
