# SUPERSEDED DOCUMENT WARNING

This file is retained for traceability only.
Do **not** use it as the current package source of truth.

Current authoritative state is defined in:
- `governance/AUTHORITATIVE_INDEX_v0_1.md`
- `../docs/frontdoor/HANDOFF_GUIDE_v0_1.md`
- `governance/PACKAGE_STATE_SUMMARY_v0_1.json`

For the current Route 1 pilot packet, use:
- `../core/route1/pilot_packet_route1_v0_3_final.jsonl`

---
# Pilot protocol memo v0.1

## Purpose
This memo defines the first human pilot for the SUF-shaped experiential language package.

This is a **small bounded pilot**, not a full study.

Initial pilot scope:
- Route 1 only
- 1 to 3 participants
- 8 to 12 items
- decode-first design
- structured system vs plain-language baseline

## Current pilot posture
Status transition intended:
- from `pre_human`
- to `pilot_ready`

This pilot is designed to answer:
1. Can a participant learn the Route 1 token system enough to perform bounded decode tasks?
2. Does the structured system support useful reconstruction?
3. Where do confusions cluster?
4. Are token errors more common than semantic errors?

## Route used
- Route 1: interoceptive-affective microstates

Route 2 is deferred until after Route 1 pilot review.

## Participant profile
Minimum:
- 1 participant can already be informative for usability failure
Preferred:
- 2 to 3 participants

No specialized background is required, but participants must:
- read English comfortably
- tolerate short structured decoding tasks
- understand that the system is provisional

## Task type
This pilot uses **decode-first** tasks.

Participants are shown:
- either a structured encoded state
- or a plain-language description
and must reconstruct the state in the requested target format.

Do not mix encode and decode in the same first pilot block.

## Pilot blocks

### Block A — structured decode
Participant sees a Route 1 encoded form and writes:
- a plain-language gloss
- or selects target features from a controlled form

### Block B — plain-language baseline
Participant sees a plain-language description and reconstructs:
- target features in the Route 1 schema

This lets the pilot compare:
- structure → reconstruction
- plain language → reconstruction

## Number of trials
Recommended first run:
- 10 trials total
- 5 structured decode
- 5 plain-language baseline

Optional simpler first run:
- 8 trials total
- 4 structured
- 4 baseline

## Trial order
Recommended:
1. brief orientation
2. 2 practice items
3. 5 structured trials
4. short break
5. 5 baseline trials
6. post-task feedback

Practice items should not be included in main scoring.

## Materials shown to participants
Allowed:
- short Route 1 token legend
- allowed value cheatsheet
- response template

Not allowed in main scored trials:
- answer key
- full ontology explanation beyond what is needed
- live corrective feedback during scoring

## Response format
Participant response should be captured as either:

### Option A — structured feature form
- valence
- arousal
- intensity
- locus
- texture
- contour
- certainty
- source
- action tendency

### Option B — predicted surface encoding
If using this option, participant must produce a Route 1 encoded string.

For first pilot, Option A is safer.

## Scoring
Primary scoring:
- field-by-field reconstruction score using existing scorer logic
- confusion by field
- exact vs partial vs missed fields

Secondary scoring:
- token errors
- malformed responses
- latency per item if practical
- self-reported difficulty

## Success criteria
This pilot is successful if:
- participants can complete the task
- structured trials are interpretable
- main confusion points are identifiable
- the system produces meaningful error structure

This pilot does **not** need to prove superiority yet.

## Failure / redesign signals
Redesign is indicated if:
- participants cannot understand the token system enough to respond
- malformed responses dominate
- ontology fields feel unusable
- route logic is confusing
- all items collapse into low-information guesses
- participants report major missing distinctions

## Data to capture
Per trial:
- participant id
- trial id
- route id
- condition (structured / baseline)
- stimulus text
- response text
- parsed response if applicable
- score
- field-level errors
- time taken if available
- participant comments if any

## Ethics / posture
This is a bounded design pilot, not a clinical or diagnostic tool.
Do not overinterpret individual responses.

## Output artifacts from pilot
After the pilot, produce:
- scored report
- field confusion summary
- usability notes
- ontology mismatch notes
- recommendation: keep / revise / redesign
