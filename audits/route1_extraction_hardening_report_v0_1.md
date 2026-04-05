# Route 1 extraction hardening report

## Scope
This report preserves the extraction-layer hardening judgment for the Route 1 pilot package.

## Hardening points retained
- Participant-facing response capture is anchored to a field form rather than left to freeform interpretation.
- Conversion from filled response form to scoring predictions is handled by `tools/convert_route1_responses_to_predictions.py`.
- The launch path reduces extraction drift by routing operators through `tools/run_route1_current_ops.py`.
- Clarification and calibration materials are included so operators do not improvise hidden interpretation rules.

## Residual limitation
Extraction remains dependent on participant comprehension and operator compliance with the documented path. This package reduces extraction drift; it does not eliminate it.

## Current status
Retained as review history. Not the active instructions file.
