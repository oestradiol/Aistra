# Pilot protocol memo v0.2 (red-teamed)

## Status
This version replaces the v0.1 pilot plan as the recommended first human pilot.

Reason:
v0.1 had several avoidable threats to interpretability:
- same underlying targets appeared in both structured and baseline conditions
- condition order was fixed
- the baseline descriptions were too close to direct canonical paraphrases
- the main packet included high-complexity uncertainty/remainder items too early
- no explicit practice phase materials were defined

## Pilot purpose
This is still a **small bounded design pilot**, not a full study.

Primary questions:
1. Can participants learn Route 1 well enough to complete bounded decode tasks?
2. Where do confusions cluster: token lookup, ontology mapping, or field extraction?
3. Does the structured format produce different error structure from plain language?
4. Are the most complex schema features usable at all, or should they be deferred?

This pilot is for usability and error topology first.
It is **not** a superiority test.

## Route
- Route 1 only
- Route 2 remains deferred until Route 1 review is complete

## Recommended participant count
- minimum informative pilot: 2
- preferred first pass: 3

One participant can still reveal catastrophic usability failure, but not enough comparison structure.

## Design
Use a **within-participant blocked design with non-overlapping item sets**.

Each participant completes:
- structured block
- baseline block

But:
- the underlying targets in the two blocks must be different
- block order should be counterbalanced across participants if possible

## Conditions

### Condition S — structured decode
Participant sees a Route 1 encoded string and reconstructs the intended state in a controlled feature form.

### Condition B — baseline decode
Participant sees a plain-language description and reconstructs the intended state in the same controlled feature form.

This keeps the response format constant while changing the input format.

## Critical control rule
Do **not** show the same underlying target in both conditions to the same participant.

That was the main flaw in v0.1.

## Item complexity policy
For the first pilot:
- main scored items should avoid uncertainty markers and remainder markers
- use only simple single-locus or clearly diffuse cases
- use at most two-texture combinations
- defer the most complex items (`?`, `Ø`) to practice or later pilot phases

Rationale:
if the first pilot fails, it should fail on core usability, not on advanced notation edge cases.

## Trial counts
Recommended:
- 2 practice items
- 4 structured scored items
- 4 baseline scored items

Total viewed items:
- 10

This is smaller than v0.1 but more interpretable.

## Practice phase
Practice should include:
- 1 simple structured item
- 1 simple baseline item

Practice items must:
- not appear in scored trials
- allow questions
- allow one corrective explanation pass

No corrective feedback once scored trials begin.

## Materials allowed
Participants may see:
- a short Route 1 token legend
- a Route 1 allowed-values sheet
- a fixed response form

Participants should **not** see:
- the answer key
- full theory explanation
- current scorer logic
- item difficulty labels

## Response format
Use controlled feature-form responses only.

Required fields:
- valence
- arousal
- intensity
- locus
- texture
- contour
- certainty
- source
- action tendency

Optional comments box:
- "what was hard?"
- "what felt missing?"

Do not use free encoded-string production in the first pilot.
That adds token production difficulty too early.

## Timing
Capture:
- start time
- end time
- optional per-item time if easy to collect

But do not make timing itself the main criterion in pilot 1.

## Counterbalancing
If 2+ participants:
- Participant A: structured first, baseline second
- Participant B: baseline first, structured second
- Participant C: structured first, baseline second

If only 1 participant:
- structured first is acceptable, but note order bias in review

## Scoring posture
Use the existing Route 1 field-wise scorer as a **descriptive aid**, not as a final truth metric.

Review must also inspect:
- malformed responses
- participant confusion comments
- whether high scores actually feel semantically right
- whether low scores reflect token failure or ontology mismatch

## Immediate redesign triggers
Pause and revise before additional participants if:
- participant cannot complete practice after one explanation
- malformed responses dominate main trials
- participant consistently says the available categories do not fit the states
- the structured condition appears to test memorization only
- the baseline condition is obviously easier or harder for wording reasons unrelated to the ontology

## Output after pilot
Produce:
- scored report
- field confusion summary
- participant comments summary
- token usability summary
- ontology adequacy summary
- recommendation: keep / revise / redesign
