# AUTHORITATIVE INDEX v0.8

## Purpose
This document prevents accidental use of outdated package materials and defines the minimal current handoff surface.

## Current authoritative files

### Package-level
- `../README.md`
- `../START_HERE_v0_7.md`
- `../docs/frontdoor/CURRENT_OPERATOR_START_HERE_v0_1.md`
- `../docs/frontdoor/HANDOFF_GUIDE_v0_1.md`
- `AUTHORITATIVE_INDEX_v0_1.md`
- `AUTHORITATIVE_SOURCES_v0_2.json`
- `AUTHORITATIVE_INTEGRITY_MANIFEST_v0_1.json`
- `PACKAGE_STATE_SUMMARY_v0_1.json`
- `../docs/ops/CORRECTION_CYCLE_PROTOCOL_v0_1.md`
- `../docs/ops/PACKAGE_ENFORCEMENT_LAYER_v0_1.md`
- `../cross_route_spec_v0_1/manifest.json`
- `../cross_route_spec_v0_1/common_interfaces.md`
- `../core/common/route_control.py`
- `../core/common/route_control_memo.md`
- `../docs/ops/weight_calibration_memo_v0_1.md`

### Route 1 authoritative files
- `../core/route1/gold_valid.jsonl`
- `../core/route1/gold_invalid.jsonl`
- `../core/route1/correction_pairs.jsonl`
- `../core/route1/parser.py`
- `../core/route1/scorer.py`
- `../core/route1/experiment_runner.py`
- `../authoritative_guard.py`
- `../docs/ops/pilot_protocol_memo_v0_2_redteamed.md`
- `../docs/ops/baseline_protocol_memo_v0_2_redteamed.md`
- `../docs/ops/pilot_review_template_v0_2_redteamed.md`
- `../core/route1/pilot_packet_route1_v0_3_final.jsonl`
- `../core/route1/pilot_answer_key_route1_v0_4_alternate_aware.jsonl`
- `../docs/ops/participant_instructions_route1_pilot_v0_2_anchored.md`
- `../core/route1/token_legend_route1_v0_1.md`
- `../docs/ops/allowed_values_response_form_route1_v0_2_anchored.md`
- `../core/route1/pilot_response_template_route1_v0_2_anchored.json`
- `../docs/ops/route1_calibration_examples_v0_1.md`
- `../docs/ops/route1_pilot_clarification_layer_v0_1.md`
- `../docs/ops/operator_checklist_route1_pilot_v0_1_1.md`
- `../docs/ops/NEXT_STEP_PREP_route1_pilot_ops_v0_1_1.md`
- `../docs/ops/final_correction_pass_note_v0_1.md`
- `../tools/run_route1_current_ops.py`
- `../tools/convert_route1_responses_to_predictions.py`

### Route 2 authoritative files
- `../route2_visual_v0_1/README.md`
- `../route2_visual_v0_1/gold_valid.jsonl`
- `../route2_visual_v0_1/gold_invalid.jsonl`
- `../route2_visual_v0_1/correction_pairs.jsonl`
- `../route2_visual_v0_1/parser.py`
- `../route2_visual_v0_1/scorer.py`
- `../route2_visual_v0_1/experiment_runner.py`

## Rule
If a file is not listed in the authoritative sections above, do not assume it is the correct entrypoint.

## Enforcement files
- `../package_doctor.py`
- `../route1_launch_gate.py`
- `../tools/audit_root_budget.py`

## Superseded or traceability-only files
- `../deprecated/route1_superseded/`
- `../deprecated/handoff_history_v0_1/`

Reference path: `governance/AUTHORITATIVE_INTEGRITY_MANIFEST_v0_1.json`
