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
# Pilot-readiness memo v0.1

## Purpose
This memo states the current readiness level of the SUF-shaped experiential language package and defines the minimum conditions for initiating the first human pilot.

It is a control document, not a claim of scientific success.

Current package scope:
- Route 1 — interoceptive-affective microstates
- Route 2 — visual phenomenological microstructures

Current posture:
- pre-human
- bounded
- formally testable
- not yet pilot-running

---

## 1. What is complete now

### 1.1 Route 1 formal package
Complete:
- bounded ontology
- fixed-slot canonical notation
- surface token system
- parser
- scorer
- experiment runner
- valid corpus
- invalid corpus
- correction pairs

### 1.2 Route 2 formal package
Complete:
- bounded ontology
- fixed-slot canonical notation
- surface token system
- parser
- scorer
- experiment runner
- valid corpus
- invalid corpus
- correction pairs

### 1.3 Cross-route governance
Complete:
- route-control layer
- defer path for mixed/out-of-scope cases
- cross-route manifest
- common interface spec
- unified report template
- package tree

### 1.4 Formal hardening
Complete:
- scoring rationale memo
- adversarial suite
- repaired adversarial case
- current adversarial pass state: full pass

---

## 2. What is strong enough already

The package is now strong enough for:

- parser/validator testing
- scorer behavior inspection
- route-boundary enforcement
- synthetic and desk simulations
- adversarial pre-human review
- protocol drafting for a first small pilot

This means the system is no longer just a loose concept. It is a bounded formal prototype.

---

## 3. What remains provisional

The following are still provisional and should be treated that way:

### 3.1 Ontology adequacy
Unknowns remain about whether the chosen fields and values match lived distinctions well enough.

### 3.2 Token usability
The token systems are deliberately rigid and may be harder or easier for humans than expected.

### 3.3 Weight calibration
The weights are engineering priors, not empirically justified final values.

### 3.4 Gloss adequacy
Deterministic glosses are useful for formal work, but may be awkward for real participants.

### 3.5 Score interpretation
A numerical reconstruction score is useful, but its human meaning is not yet validated.

### 3.6 Route adequacy
It is still not known whether Route 1 and Route 2 are the best first bounded routes for actual user performance.

---

## 4. What is still missing before pilot

These are the remaining blockers before a useful human run.

### 4.1 Pilot protocol memo
Still needed:
- participant task instructions
- whether they see gloss or encoded form
- whether the task is encode, decode, or both
- number of trials
- route assignment procedure
- stopping conditions

### 4.2 Baseline protocol
Still needed:
- plain-language baseline task
- checklist baseline task
- scoring alignment with those baselines

### 4.3 Trial packet design
Still needed:
- exact first pilot packet
- difficulty balance
- route balance
- whether mixed-route items are excluded entirely

### 4.4 Pilot review template
Still needed:
- field confusion template
- participant difficulty notes
- token usability notes
- ontology mismatch notes

These are moderate blockers, not deep architecture blockers.

---

## 5. What is explicitly not required before pilot

The following do **not** need to be completed before first human pilot:

- mixed-route layer
- UI
- learned model support
- narrative grammar
- additional routes beyond 1 and 2
- perfect weights
- large-scale corpus expansion
- philosophical closure

Those can wait.

---

## 6. Pilot trigger condition

The first human pilot should begin when all of the following are true:

1. a pilot protocol memo exists
2. a baseline protocol exists
3. a small fixed packet exists for each chosen route
4. review templates exist for post-trial analysis
5. the team accepts that ontology and weights are provisional

That is the minimum trigger.

Until then, stay in `pre_human`.

Once those are met, move to `pilot_ready`.

---

## 7. Recommended first pilot shape

The first pilot should be small.

### Recommended size
- 1 to 3 participants
- 1 route at a time
- 8 to 12 items per route
- no mixed-route items
- both structured and plain-language comparison tasks

### Recommended order
1. Route 1 pilot first
2. review failures
3. small revisions if needed
4. Route 2 pilot second

This is safer than piloting both routes simultaneously.

---

## 8. Why Route 1 should pilot first

Route 1 is likely the better first human route because:
- bodily-affective states are often easier to introspect than brief visual microstructures
- the route already includes action tendency and source, which may expose useful human confusions
- it is closer to the original motivation of structured experiential encoding

Route 2 is still valuable, but slightly more fragile.

---

## 9. Failure conditions for first pilot

The first pilot should be considered a redesign signal if any of these happen:

- participants cannot learn the token system at all
- route assignment is frequently confusing
- plain language consistently outperforms the structured system
- token errors overwhelm semantic errors
- participants report that major felt distinctions have no place in the ontology
- scores look high but participants say decoded outputs still feel wrong
- the task burden is too high for the information gained

These are not “project death” signals. They are design feedback signals.

---

## 10. Current status recommendation

Current status should remain:

`pre_human`

Not because the system is weak, but because the remaining blockers are protocol blockers rather than architecture blockers.

The correct next move is not more ontology expansion.
The correct next move is pilot preparation.

---

## 11. Immediate next documents to write

Write these next, in this order:

1. `pilot_protocol_memo_v0_1.md`
2. `baseline_protocol_memo_v0_1.md`
3. `pilot_packet_route1_v0_1.jsonl`
4. `pilot_review_template_v0_1.md`

Once those exist, the first Route 1 pilot is justified.

---

## 12. Safe current claim

> The package is now formally pilot-preparable but not yet pilot-ready.

That is the cleanest current posture.

---

## 13. Compression

### 1–2 line summary
The architecture is now solid enough for a first small human pilot, but protocol materials are still missing. The package should remain `pre_human` until pilot instructions, baselines, packets, and review templates are written.

### Key patterns
- architecture done
- protocol not done
- no more big formal expansion required before pilot
- Route 1 should go first
- weights and ontology remain explicitly provisional

### Memory anchor
**Formally ready to prepare a pilot, not yet ready to run one.**
