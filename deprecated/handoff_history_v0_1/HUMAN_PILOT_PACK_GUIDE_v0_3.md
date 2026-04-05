# Route 1 human pilot pack v0.3

## What changed in v0.3
- Preserved the v0.2 `hol` → `woba` collision fix for the whole-body token.
- Rewrote the baseline prompts so all 9 scored fields are directly supported by the wording.
- Rewrote the practice baseline prompt (`PR2`) for the same reason.
- Added built-in scoring to the local interface export. The exported JSON now contains item-level exact-field scores and field-by-field matches.
- Added a corrected copy of the April 4, 2026 pilot response export with the `PR2` valence misclick fixed from `negative` to `positive`.
- Added a verification report and a thread summary for handoff.

## Recommended entry point
1. Open `human_pilot_app_v0_1/index.html` in a browser.
2. Complete the packet exactly as shown.
3. Click **Export Results**.
4. Send the exported JSON back.

## Important rules
- Answer from the stimulus, not from your current feeling.
- Fill the 9 scored fields only.
- Texture can contain one or two values.
- For baseline items, do not infer extra cause, source, certainty, or contour beyond what the text explicitly gives you.
- This build is designed to remove both operator paraphrase drift and baseline underspecification.

## Open method
This build embeds the packet config directly into the page, so you should be able to open `human_pilot_app_v0_1/index.html` directly in a browser.

If your system still refuses local file execution, use:

### Python 3
```bash
python -m http.server 8000
```
Then open:
```text
http://localhost:8000/human_pilot_app_v0_1/
```

## Files you will likely use
- `human_pilot_app_v0_1/index.html` — local interface
- `human_pilot_app_v0_1/packet_config.json` — exact packet and answer key source used by the UI
- `../core/route1/pilot_packet_route1_v0_3_final.jsonl` — current verbatim packet items
- `../core/route1/pilot_answer_key_route1_v0_4_alternate_aware.jsonl` — current answer key
- `../core/route1/token_legend_route1_v0_1.md` — token legend
- `tools/score_route1_human_pilot_export.py` — local scorer for exported JSON files
- `pilot_runs/route1_human_pilot_results_2026-04-04T23-14-29-409Z.corrected.json` — corrected legacy pilot export
- `THREAD_LOSSLESS_COMPRESSION_v0_1.md` — full thread compression and conclusions
- `VERIFICATION_REPORT_v0_3.md` — change verification and safety checks

## Result format
The exported JSON contains:
- item id
- condition
- verbatim stimulus
- structured response
- canonical prediction string
- field-level scoring against the current answer key

## Current baseline wording policy
The v0.3 baseline prompts are deliberately explicit. They are less naturalistic than v0.2, but more valid for scored administration.
