# Route 1 human pilot guide

This guide is for running the current Route 1 local packet without manual operator paraphrase.

## Current package state
- live package line: `v1.11`
- Route 1 status: `pilot_ready` in package state, meaning operationally runnable under current controls
- Route 1 is the explicit-calibration route, not a naturalistic phenomenology route

## Recommended path
1. Read `../../START_HERE.md`.
2. Open `../../apps/human_pilot/index.html` in a browser.
3. Complete the packet exactly as shown.
4. Click **Export Results**.
5. Keep the exported files and, if needed, score them locally.

## Important rules
- Answer from the stimulus, not from your current feeling.
- Fill the 9 scored fields only.
- Texture can contain one or two values.
- For baseline-explicit items, do not infer extra cause, source, certainty, or contour beyond what the text gives you.

## Current files you may use
- `../../apps/human_pilot/index.html`
- `../../apps/human_pilot/packet_config.json`
- `../../core/route1/pilot_packet_route1_v0_3_final.jsonl`
- `../../core/route1/pilot_answer_key_route1_v0_4_alternate_aware.jsonl`
- `../../tools/score_route1_human_pilot_export.py`
- `../specs/SCORING_SPEC_v0_1.md`
- `VERIFICATION_REPORT.md`
- `FULL_AUDIT_REPORT.md`

## Minimum local checks
```bash
python package_doctor.py
python route1_launch_gate.py
python tests/run_route1_regression_tests.py
python tools/audit_current_surfaces.py
python tools/audit_repository_file_registry.py
```
