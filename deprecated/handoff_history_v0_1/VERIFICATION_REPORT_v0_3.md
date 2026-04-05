# Verification report v0.3

## Goal
Prove that the v0.3 handoff package preserves the original package outside the intended update surface, and that the updated package remains launch-gate clean.

## Source package compared
- Original upload: `suf_lang_v0_3_minimal_handoff_ready_neg_fixed.zip`
- Working base: extracted `suf_lang_v0_1/`
- Final package target: `suf_lang_route1_human_pilot_pack_v0_3.zip`

## Integrity and launch checks
- `python package_doctor.py` → return code 0
- `python route1_launch_gate.py` → return code 0
- `python tools/score_route1_human_pilot_export.py pilot_runs/...corrected.json human_pilot_app_v0_1/packet_config.json` → return code 0

## File diff against the original uploaded zip
- Unchanged files: 109
- Changed files: 11
- Added files: 15
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
- `HUMAN_PILOT_PACK_GUIDE_v0_2.md`
- `HUMAN_PILOT_PACK_GUIDE_v0_3.md`
- `THREAD_LOSSLESS_COMPRESSION_v0_1.md`
- `__pycache__/parser.cpython-313.pyc`
- `../docs/ops/baseline_protocol_memo_v0_3_clarity.md`
- `human_pilot_app_v0_1/app.js`
- `human_pilot_app_v0_1/index.html`
- `human_pilot_app_v0_1/packet_config.js`
- `human_pilot_app_v0_1/packet_config.json`
- `human_pilot_app_v0_1/styles.css`
- `pilot_runs/route1_human_pilot_results_2026-04-04T23-14-29-409Z.corrected.json`
- `pilot_runs/route1_human_pilot_results_2026-04-04T23-14-29-409Z.corrected.scored.json`
- `pilot_runs/route1_human_pilot_results_2026-04-04T23-14-29-409Z.corrected.scored_legacy_v0_2.json`
- `route2_visual_v0_1/__pycache__/parser.cpython-313.pyc`
- `tools/score_route1_human_pilot_export.py`

### Removed files
- none

## Intended change surface
- `../core/route1/parser.py`, `../core/common/route_control.py`, `../core/route1/token_legend_route1_v0_1.md`, `../core/route1/correction_pairs.jsonl`, `../core/route1/gold_valid.jsonl`, and `examples/route1/sample_predictions_filled.jsonl` for the `woba` whole-body token fix inherited from v0.2.
- `../core/route1/pilot_packet_route1_v0_3_final.jsonl`, `../core/route1/pilot_answer_key_route1_v0_4_alternate_aware.jsonl`, `../core/route1/pilot_response_template_route1_v0_2_anchored.json`, and `human_pilot_app_v0_1/packet_config.{json,js}` for the baseline clarity rewrite.
- `human_pilot_app_v0_1/app.js` and `human_pilot_app_v0_1/index.html` for built-in local scoring.
- Documentation and handoff additions only for the remaining files listed above.

## Accuracy claim
- No original file was removed.
- All structured Route 1 items remain semantically unchanged except for the already-intended `holo` → `woba` whole-body token normalization.
- Baseline items were intentionally rewritten for explicit field support.
- Package doctor and route launch gate pass on the final tree.
