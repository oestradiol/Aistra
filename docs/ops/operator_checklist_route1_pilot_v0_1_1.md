# Route 1 pilot operator checklist

## Pre-run gate
1. Run `python package_doctor.py`
2. Run `python route1_launch_gate.py`
3. Verify `../../governance/AUTHORITATIVE_INTEGRITY_MANIFEST_v0_1.json` with `python research_grounding_v0_1/scripts/verify_integrity_manifest.py --strict`

Do not proceed unless all pass.

## Required current materials
- `pilot_protocol_memo_v0_2_redteamed.md`
- `baseline_protocol_memo_v0_2_redteamed.md`
- `pilot_review_template_v0_2_redteamed.md`
- `../../core/route1/pilot_packet_route1_v0_3_final.jsonl`
- `participant_instructions_route1_pilot_v0_2_anchored.md`
- `allowed_values_response_form_route1_v0_2_anchored.md`
- `../../core/route1/pilot_response_template_route1_v0_2_anchored.json`
- `route1_calibration_examples_v0_1.md`
- `route1_pilot_clarification_layer_v0_1.md`
- `../../core/route1/pilot_answer_key_route1_v0_4_alternate_aware.jsonl`

## Session structure
1. Deliver anchored instructions.
2. Deliver calibration examples.
3. Run the current packet.
4. Capture responses in the current response template.
5. Keep operator notes separate from participant response content.

## Execution path
Use the authoritative wrapper, not ad hoc low-level scoring:
```bash
python tools/run_route1_current_ops.py --responses <filled_response.json> --run-dir <outdir>
```

## Required outputs
The wrapper writes:
- converted predictions
- scored report
- run manifest

Store generated outputs under `verification_outputs/` or another run-evidence directory, not in the canonical top level.

## Stop conditions
Stop and mark the run if:
- launch gate fails
- integrity verification fails
- participant response file does not use the current template metadata
- any current authoritative file appears to conflict with `../../governance/AUTHORITATIVE_INDEX_v0_1.md`
