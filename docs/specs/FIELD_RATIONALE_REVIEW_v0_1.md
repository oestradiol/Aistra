# Field rationale review v0.1

## Purpose
Audit whether the Route 1 9-field ontology is conceptually justified before further expansion.

Fields:
- valence
- arousal
- intensity
- location
- texture
- contour
- certainty
- source
- action

## Summary judgment
Keep all 9 fields for now, but clarify semantics and status:
- **core-retain**: valence, arousal, location, texture, source, action
- **retain-with-watchlist**: intensity, contour, certainty

## Field-by-field review

### 1. Valence
**Status:** retain

**Why:** indispensable. Distinguishes negative / neutral / positive / mixed orientation.

**Risk:** mixed vs neutral-negative drift in ambiguous prose.

**Conclusion:** keep unchanged.

### 2. Arousal
**Status:** retain

**Why:** captures activation level separate from pleasantness and action.

**Risk:** can be confused with intensity in high-salience language.

**Conclusion:** keep, but anchor examples should keep arousal and intensity explicitly separable.

### 3. Intensity
**Status:** retain-with-watchlist

**Question:** is it redundant with arousal?

**Assessment:** not fully redundant.
- high arousal can be moderate intensity in brief sharp states
- low arousal can still be strong in heavy, depressive, or diffuse states
- user data so far shows occasional inflation, but not proof of redundancy

**Conclusion:** keep for now. Reassess after more pilots using field-confusion matrices.

### 4. Location
**Status:** retain

**Why:** highly discriminative and learnable. One of the strongest fields in pilot behavior.

**Risk:** token-level collisions (`hol`/`holo`) were lexical, not conceptual.

**Conclusion:** keep. Already strengthened by `woba` fix.

### 5. Texture
**Status:** retain

**Why:** carries much of the embodied descriptive power. Also one of the most human-useful fields.

**Risk:** dual-texture compression into one token when reading quickly.

**Conclusion:** keep. Consider later whether one vs two textures should be explicitly marked.

### 6. Contour
**Status:** retain-with-watchlist

**Question:** is contour really discriminative?

**Assessment:** yes, but weaker than location/texture.
Contour adds temporal-shape information: static, rising, falling, pulsing, wave-like, oscillating.
This helps distinguish states that share valence/arousal/location.

**Risk:** in baseline prose, contour is often inferred if not stated.

**Conclusion:** keep, but require explicit support in scored prose. Contour is useful, but fragile.

### 7. Certainty
**Status:** retain-with-watchlist and clarify

**Question:** should certainty refer to state certainty or report certainty?

**Assessment:** it should refer to **report certainty**: how confidently the state can be identified from the available signal.
It should **not** mean metaphysical certainty about cause or truth.

**Risk:** vividness gets misread as certainty.

**Conclusion:** keep, but redefine explicitly in docs as **report-level identification confidence**.

### 8. Source
**Status:** retain

**Question:** is source too ambiguous?

**Assessment:** source is difficult, but still valuable.
The distinction between self / reactive / memory / unclear is meaningful and repeatedly exposed baseline weaknesses.
That means it is not useless; it is diagnostically important.

**Risk:** baseline prose underdetermines source unless named directly.

**Conclusion:** keep, but only score it when clearly supported.

### 9. Action
**Status:** retain

**Question:** should action be optional?

**Assessment:** not yet.
Action tendency is one of the best bridges from felt state to behavioral implication. It also made hidden interpretive drift visible in the pilot.

**Risk:** some states genuinely have no strong action pull.

**Conclusion:** keep required, with `none` as the explicit no-pull option.

## Semantic clarifications to adopt
1. **Certainty = report certainty**, not ground truth certainty.
2. **Source** should be scored conservatively. If not textually supported in baseline-explicit mode, use `unclear`.
3. **Intensity** and **arousal** should be documented with contrast examples.
4. **Contour** should only be scored from explicit support in prose packets.

## Provisional ontology stance
The ontology is currently **minimal-enough to continue**.
No field should be removed before additional multi-user evidence.

## What would justify future revision
- repeated multi-user confusion showing intensity and arousal collapse into one dimension
- contour failing across explicit packets despite direct wording
- certainty showing poor interpretability even after report-level clarification
- source failing even when explicitly stated

## Current recommendation
Freeze the 9-field ontology for the next pilot cycle.
Do not add or remove fields until field-level confusion data from multiple users exists.
