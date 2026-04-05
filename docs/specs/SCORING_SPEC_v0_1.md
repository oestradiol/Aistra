# Scoring spec v0.1

## Goal
Define the Route 1 scoring family and the exact, near, and miss policy for Route 1 human pilot scoring.

## Scoring family
Route 1 now uses one explicit scoring family with two coordinated layers, each with a different job.

### Layer A: canonical scorer
- owner: `core/route1/scorer.py`
- layer: `canonical_10_field`
- scorer_version: `route1_canonical_scorer_v0_1`
- purpose: score canonical Route 1 predictions against canonical gold targets
- scored fields: modality, valence, arousal, intensity, location, texture, contour, certainty, source, action

### Layer B: human export scorer
- owner: `apps/human_pilot/app.js` and `tools/score_route1_human_pilot_export.py`
- layer: `human_export_9_field`
- scorer_version: `route1_human_export_scorer_v1_0`
- purpose: score participant form exports against the Route 1 answer key in the local human pilot workflow
- scored fields: valence, arousal, intensity, location, texture, contour, certainty, source, action
- modality is preserved in canonicalization but unscored in the human export layer because it is fixed by prompt family rather than separately chosen in the participant form

The two layers are coordinated, not interchangeable. The canonical scorer owns formal canonical evaluation. The human export scorer owns participant-form export scoring. Both belong to the same Route 1 scoring family and both must keep normalization, alternate handling, and field semantics aligned.

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
- canonical scorer: implemented for formal 10-field canonical comparisons
- human export exact field scoring: implemented
- human export weighted secondary scoring: implemented
- item exact scoring: implemented
- human-readable report: added in v0.4
- near-match taxonomy: partly automated for descriptive export scoring (currently texture_partial only); other near classes remain documented and reviewable

## Reporting and interpretation guardrail
When a Route 1 export is reviewed, read the metrics in this order:
1. `exact_9_score` and `exact_match` = primary human-export decision surface
2. `weighted_9_score` = secondary descriptive surface for bounded partial overlap
3. `matched_policy` and `candidate_results` = alternate-handling trace

Do not treat the human export scorer as a substitute for the canonical scorer, and do not treat weighted export similarity as validation evidence.
