# Baseline protocol memo v0.2 (red-teamed)

## Why v0.1 baseline needed revision
The v0.1 baseline descriptions were too close to direct canonical paraphrases.
That made the baseline a near-explicit feature list rather than a natural plain-language comparison.

That would reduce interpretability:
- if baseline performed well, it might just reflect direct cueing
- if structured performed badly, it might reflect unfair baseline explicitness

## Goal of the baseline
The baseline should remain:
- ordinary enough to feel like normal language
- clear enough to support reconstruction
- bounded enough to remain scoreable

## Revised baseline rule
A baseline description may express most of the target state, but it should not mechanically enumerate every field in slot order.

Good baseline style:
- compact
- readable
- one or two natural omissions or compressions allowed
- still anchored in the target state

Example better style:
> "A sharp, rising negative feeling in the chest that seems reactive and pushes toward freezing."

This still supports reconstruction, but does not spell out every field with equal explicitness.

## What baseline should avoid
Avoid:
- exact slot-by-slot translations
- excessive jargon
- poetic overinterpretation
- narrative context not present in the target

## Scoring note
Because baseline wording is intentionally less slot-explicit than v0.1, review should interpret baseline scores as:
- reconstruction from ordinary language
not:
- direct extraction from an English-coded answer key

## Recommended baseline use in pilot 1
Use 4 baseline items, each paired to a different underlying target than the structured block for the same participant.
