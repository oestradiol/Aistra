# Ontology audit v0.1

## Scope
Audit Route 1 token surfaces, field names, and likely confusion sources without changing the ontology itself.

## Findings

### Resolved
- `hol` (hollow) vs `holo` (whole body) was a real near-collision.
- Whole-body token has been changed to `woba` in the active Route 1 surface.

### Remaining lexical risk
- `sha` vs `shallow`-like private reinterpretations are possible, but there is no active surface collision.
- `grav` may be misread as gravity/grave rather than heavy.
- `meda` and `kei` are learnable but not mnemonic to naive users.
- `faz` and `dis` can be confused by first-time users because both imply high activation outcomes.

## Recommendations
1. Keep `woba` as the stable whole-body token.
2. Add token-level memory anchors in participant/operator docs:
   - `grav = heavy`
   - `meda = medium certainty`
   - `kei = high certainty`
   - `faz = freeze`
   - `dis = discharge`
3. Avoid introducing any new token that differs by a single added vowel from an existing token.
4. Keep modality tokens out of scored response forms.

## Structural audit
- Slot order is strong and learnable.
- Dual texture is expressive, but increases speed-error risk.
- Baseline-explicit prose currently works as a bridge into the same ontology.

## Current ontology status
Stable enough for the next pilot cycle.
