# Route 1 human pilot pack v0.2

## What changed
- Fixed the `hol` / `holo` collision by renaming the whole-body surface token from `holo` to `woba`.
- Added a minimal local interface in `human_pilot_app_v0_1/`.
- The interface runs only verbatim packet items from the source files and exports a JSON result file.

## What you do
1. Open `human_pilot_app_v0_1/index.html` in a browser.
2. Read each stimulus exactly as shown.
3. Fill the 9 scored fields.
4. Save each answer.
5. At the end, click **Export Results**.
6. Send the exported JSON file back here.

## Important rules
- Answer from the stimulus, not from your current feeling.
- Modality is shown for reference. The scored fields are: valence, arousal, intensity, location, texture, contour, certainty, source, action.
- Texture can contain one or two values.
- This build is designed to remove operator paraphrase risk.

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
- `../core/route1/pilot_packet_route1_v0_3_final.jsonl` — verbatim packet items
- `../core/route1/pilot_answer_key_route1_v0_4_alternate_aware.jsonl` — answer key
- `../core/route1/token_legend_route1_v0_1.md` — token legend

## Result format
The exported JSON contains:
- item id
- condition
- verbatim stimulus
- your structured response
- a canonical prediction string

Send that exported file back here and I can score it directly.
