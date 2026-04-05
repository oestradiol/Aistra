# Verification report v0.4

## Goal
Prove that the v0.4 handoff package preserves the original package outside the intended update surface, keeps the v0.3 Route 1 semantics intact, and remains launch-gate clean.

## Source package compared
- Original upload: `suf_lang_v0_3_minimal_handoff_ready_neg_fixed.zip`
- Previous handoff layer: `suf_lang_route1_human_pilot_pack_v0_3.zip`
- Final package target: `suf_lang_route1_human_pilot_pack_v0_4.zip`

## Integrity and launch checks
- `python package_doctor.py` → PASS
- `python route1_launch_gate.py` → PASS
- `python tests/run_route1_regression_tests.py` → PASS
- `node --check human_pilot_app_v0_1/app.js` → PASS
- `python tools/score_route1_human_pilot_export.py pilot_runs/route1_human_pilot_results_2026-04-04T23-14-29-409Z.corrected.json human_pilot_app_v0_1/packet_config.json` → PASS

## File diff against the original uploaded zip
- Unchanged files: 109
- Changed files: 11
- Added files: 27
- Removed files: 0

### Changed files
- `governance/AUTHORITATIVE_INTEGRITY_MANIFEST_v0_1.json`
- `README.md`
- `../core/route1/correction_pairs.jsonl`
- `examples/route1/sample_predictions_filled.jsonl`
- `../core/route1/gold_valid.jsonl`
- `../core/route1/parser.py`
- `../core/route1/pilot_answer_key_route1_v0_4_alternate_aware.jsonl`
- `../core/route1/pilot_packet_route1_v0_3_final.jsonl`
- `../core/route1/pilot_response_template_route1_v0_2_anchored.json`
- `../core/common/route_control.py`
- `../core/route1/token_legend_route1_v0_1.md`

### Added files
- `../../docs/specs/BASELINE_FIELD_SUPPORT_MATRIX_v0_1.md`
- `CHANGELOG_v0_4.md`
- `../../docs/specs/DESIGN_DECISION_NOTE_v0_1.md`
- `../../docs/specs/FIELD_RATIONALE_REVIEW_v0_1.md`
- `../docs/ops/HANDOFF_PROTOCOL_v0_1.md`
- `HUMAN_PILOT_PACK_GUIDE_v0_2.md`
- `HUMAN_PILOT_PACK_GUIDE_v0_3.md`
- `HUMAN_PILOT_PACK_GUIDE_v0_4.md`
- `../../docs/specs/ONTOLOGY_AUDIT_v0_1.md`
- `../../docs/specs/PROJECT_SPEC_v0_1.md`
- `../../docs/specs/SCORING_SPEC_v0_1.md`
- `THREAD_LOSSLESS_COMPRESSION_v0_1.md`
- `THREAD_LOSSLESS_COMPRESSION_v0_2.md`
- `../../docs/specs/VALIDITY_AND_LIMITS_v0_1.md`
- `VERIFICATION_REPORT_v0_3.md`
- `../docs/ops/baseline_protocol_memo_v0_3_clarity.md`
- `human_pilot_app_v0_1/app.js`
- `human_pilot_app_v0_1/index.html`
- `human_pilot_app_v0_1/packet_config.js`
- `human_pilot_app_v0_1/packet_config.json`
- `human_pilot_app_v0_1/styles.css`
- `pilot_runs/route1_human_pilot_results_2026-04-04T23-14-29-409Z.corrected.json`
- `pilot_runs/route1_human_pilot_results_2026-04-04T23-14-29-409Z.corrected.report.md`
- `pilot_runs/route1_human_pilot_results_2026-04-04T23-14-29-409Z.corrected.scored.json`
- `pilot_runs/route1_human_pilot_results_2026-04-04T23-14-29-409Z.corrected.scored_legacy_v0_2.json`
- `tests/run_route1_regression_tests.py`
- `tools/score_route1_human_pilot_export.py`

### Removed files
- none

## v0.3 → v0.4 delta
v0.4 does **not** change the live Route 1 semantics introduced in v0.3.

### Semantically unchanged from v0.3
- `../core/route1/parser.py`
- `../core/common/route_control.py`
- `../core/route1/pilot_packet_route1_v0_3_final.jsonl`
- `../core/route1/pilot_answer_key_route1_v0_4_alternate_aware.jsonl`
- `../core/route1/token_legend_route1_v0_1.md`
- all baseline-explicit prompts
- all structured prompts

### Changed in v0.4
- app export/reporting layer
- scorer output/reporting layer
- package-level design/spec docs
- regression tests
- integrity manifest refresh

## Intended change surface in v0.4
- `human_pilot_app_v0_1/app.js` for richer export summaries and report generation
- `human_pilot_app_v0_1/packet_config.{json,js}` for package version metadata only
- `tools/score_route1_human_pilot_export.py` for report generation and summary metrics
- documentation and test additions only for the remaining new files

## Accuracy claim
- No original file was removed.
- No Route 1 surface token semantics changed in v0.4.
- No baseline-explicit prompt semantics changed in v0.4.
- The package remains doctor-clean and launch-gate clean.
- The final bundle is a documentation/tooling hardening release on top of the v0.3 semantic state.
