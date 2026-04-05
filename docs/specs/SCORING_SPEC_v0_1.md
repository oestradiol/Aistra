# Scoring spec v0.1

## Goal
Define exact, near, and miss policy for Route 1 human pilot scoring.

## Primary scoring unit
A response is scored across 9 fields:
- valence
- arousal
- intensity
- location
- texture
- contour
- certainty
- source
- action

## Exact field match
A field is exact when the response equals the answer key label after normalization.

Normalization rules:
- `unknown` = `unclear`
- texture order is ignored
- modality is ignored and unscored
- numeric intensity must normalize to `1`, `2`, or `3`

## Exact item match
An item is an exact match when all 9 scored fields match.

## Near match
A near match is not the same as exact and must be reported separately.
Suggested near classes:
- **texture_partial**: one of two expected textures present, the other omitted
- **contour_neighbor**: only if explicitly predeclared in the answer key alternates
- **wording_alias**: only if predeclared, e.g. `unknown` → `unclear`

Near matches must never be silently counted as exact.

## Miss
Any field not exact and not covered by a declared alternate or near class is a miss.

## Alternates
Only answer-key-declared alternates are allowed to affect exact scoring.
No freehand semantic alternates during review.

## Baseline policy
For baseline-explicit prompts, score only against the written key.
Do not infer generosity from prose naturalness.

## Reporting requirements
Every scored export should include:
- exact 9-field score per item
- field-by-field matches
- exact item count
- per-field exact rate
- condition breakdown (practice / structured / baseline)
- package/scorer version

## Current implementation status
- exact field scoring: implemented
- item exact scoring: implemented
- human-readable report: added in v0.4
- near-match taxonomy: documented here, not yet fully automated
