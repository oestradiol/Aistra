# Changelog v0.4

## Added
- `../../docs/specs/DESIGN_DECISION_NOTE_v0_1.md`
- `../../docs/specs/FIELD_RATIONALE_REVIEW_v0_1.md`
- `../../docs/specs/ONTOLOGY_AUDIT_v0_1.md`
- `../../docs/specs/BASELINE_FIELD_SUPPORT_MATRIX_v0_1.md`
- `../../docs/specs/SCORING_SPEC_v0_1.md`
- `../../docs/specs/PROJECT_SPEC_v0_1.md`
- `../../docs/specs/VALIDITY_AND_LIMITS_v0_1.md`
- `../docs/ops/HANDOFF_PROTOCOL_v0_1.md`
- `tests/run_route1_regression_tests.py`
- human-readable report generation from both the browser app and local scorer
- `pilot_runs/route1_human_pilot_results_2026-04-04T23-14-29-409Z.corrected.report.md`

## Changed
- `human_pilot_app_v0_1/app.js` now exports both JSON and Markdown report files, includes field accuracy summaries, condition breakdowns, and light normalization aliases.
- `human_pilot_app_v0_1/packet_config.{json,js}` now identify the package as v0.4 and record the explicit calibration mode.
- `tools/score_route1_human_pilot_export.py` now writes both `.scored.json` and `.report.md`, plus normalized summary metrics.
- handoff documentation updated to point to the new v0.4 entry points and spec files.

## Preserved from v0.3
- `woba` whole-body token fix
- baseline-explicit packet wording
- corrected April 4, 2026 pilot JSON
- launch-gate and doctor compatibility

## No semantic route changes in v0.4
- structured Route 1 stimuli unchanged from v0.3
- baseline-explicit prompts unchanged from v0.3
- answer key unchanged from v0.3
- parser token semantics unchanged from v0.3
