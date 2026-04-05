# Route 1 next-step prep

## Current working files
- `../../core/route1/pilot_response_template_route1_v0_2_anchored.json`
- `../../core/route1/pilot_answer_key_route1_v0_4_alternate_aware.jsonl`
- `tools/convert_route1_responses_to_predictions.py`
- `tools/run_route1_current_ops.py`

## Recommended operator loop
1. Duplicate `../../core/route1/pilot_response_template_route1_v0_2_anchored.json` into a participant-specific response file.
2. Fill `response_fields` only.
3. Run the authoritative wrapper:
   `python tools/run_route1_current_ops.py --responses <filled_response.json> --run-dir <outdir>`
4. Store generated outputs under `reports/generated/route1_runs/` or another dedicated run-evidence directory.
5. Keep notes separate from canonical source files.
