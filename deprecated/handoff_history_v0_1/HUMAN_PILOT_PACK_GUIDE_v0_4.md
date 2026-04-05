# Route 1 human pilot pack v0.4

## What changed in v0.4
- Keeps the v0.3 `woba` token fix and explicit baseline packet unchanged.
- Adds package-level design/spec docs so the project can be handed off without thread context.
- Adds a field-rationale review and a baseline design decision note.
- Adds local regression tests.
- App export now produces both:
  - results JSON
  - human-readable report Markdown
- Local scorer now also produces both:
  - `.scored.json`
  - `.report.md`

## Recommended entry point
1. Open `human_pilot_app_v0_1/index.html` in a browser.
2. Complete the packet exactly as shown.
3. Click **Export Results**.
4. Return both exported files if possible.

## Important rules
- Answer from the stimulus, not from your current feeling.
- Fill the 9 scored fields only.
- Texture can contain one or two values.
- For baseline-explicit items, do not infer extra cause, source, certainty, or contour beyond what the text explicitly gives you.
- The current main packet is **baseline-explicit calibration mode**, not naturalistic baseline mode.

## Files you will likely use
- `human_pilot_app_v0_1/index.html` — local interface
- `human_pilot_app_v0_1/packet_config.json` — exact packet and answer key source used by the UI
- `../core/route1/pilot_packet_route1_v0_3_final.jsonl` — current verbatim packet items
- `../core/route1/pilot_answer_key_route1_v0_4_alternate_aware.jsonl` — current answer key
- `tools/score_route1_human_pilot_export.py` — local scorer for exported JSON files
- `../../docs/specs/DESIGN_DECISION_NOTE_v0_1.md` — why the package currently uses explicit baseline prompts
- `../../docs/specs/FIELD_RATIONALE_REVIEW_v0_1.md` — why the 9 fields are currently retained
- `../../docs/specs/SCORING_SPEC_v0_1.md` — scoring policy
- `../../docs/specs/BASELINE_FIELD_SUPPORT_MATRIX_v0_1.md` — field-by-field textual support for baseline prompts
- `../../docs/specs/VALIDITY_AND_LIMITS_v0_1.md` — current claim boundary
- `CHANGELOG_v0_4.md` — what changed in this release
- `VERIFICATION_REPORT_v0_4.md` — integrity and drift verification
- `THREAD_LOSSLESS_COMPRESSION_v0_2.md` — thread summary through v0.4

## Running local checks
### Core checks
```bash
python package_doctor.py
python route1_launch_gate.py
python tests/run_route1_regression_tests.py
```

### Score an exported run locally
```bash
python tools/score_route1_human_pilot_export.py /path/to/results.json human_pilot_app_v0_1/packet_config.json
```

## Current design stance
- main packet = explicit calibration
- naturalistic baseline = future optional separate packet
- do not merge scores from those two modes
