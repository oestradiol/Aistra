# Route 1 human pilot pack v0.5

## What changed in v0.5
- keeps Route 1 semantics from v0.4 unchanged
- cleans the front door so current materials are obvious
- archives historical handoff guides and old verification reports under `../../deprecated/handoff_history_v0_1/`
- makes packet config generation reproducible and hash-traceable
- upgrades browser scoring and local scorer to truly respect acceptable alternates
- includes stronger export provenance via packet, answer-key, and config digests
- adds a skeptical audit document that maps remaining project-level weaknesses separately from package bugs

## Recommended entry point
1. Read `../../START_HERE_v0_7.md`.
2. Open `../../human_pilot_app_v0_1/index.html` in a browser.
3. Complete the packet exactly as shown.
4. Click **Export Results**.
5. Return both exported files if possible.

## Important rules
- Answer from the stimulus, not from your current feeling.
- Fill the 9 scored fields only.
- Texture can contain one or two values.
- For baseline-explicit items, do not infer extra cause, source, certainty, or contour beyond what the text explicitly gives you.
- The current main packet is **baseline-explicit calibration mode**, not naturalistic baseline mode.

## Files you will likely use
- `../../START_HERE_v0_7.md`
- `../../human_pilot_app_v0_1/index.html`
- `../../human_pilot_app_v0_1/packet_config.json`
- `../../core/route1/pilot_packet_route1_v0_3_final.jsonl`
- `../../core/route1/pilot_answer_key_route1_v0_4_alternate_aware.jsonl`
- `../../tools/score_route1_human_pilot_export.py`
- `../../tools/generate_route1_packet_config.py`
- `../specs/SCORING_SPEC_v0_1.md`
- `SKEPTICAL_AUDIT_AND_HARDENING_v0_1.md`
- `VERIFICATION_REPORT_v0_5.md`
- `THREAD_LOSSLESS_COMPRESSION_v0_3.md`

## Running local checks
```bash
python package_doctor.py
python route1_launch_gate.py
python tests/run_route1_regression_tests.py
```

## Score an exported run locally
```bash
python tools/score_route1_human_pilot_export.py /path/to/results.json human_pilot_app_v0_1/packet_config.json
```
