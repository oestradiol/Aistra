# Weight calibration memo v0.1

## Purpose
This memo records the current justification for field weights in Route 1 and Route 2 scoring.

The current weights are provisional and pre-human. They are designed to support:
- bounded reconstruction experiments
- partial-match analysis
- adversarial stress tests
- later revision after pilot evidence

They do **not** claim objective final importance or universal measurement.

## General principles
1. Core structural discriminators get higher weight than metadata-like fields.
2. Fields likely to carry most of the reconstructive burden should matter more.
3. Fields that are secondary, supportive, or more weakly reportable should matter less.
4. Texture-like fields can take partial credit because they are richer and more confusable.
5. Weight choice should remain explicitly revisable after pilot evidence.

## Route 1 current weights
- mod: 0.5
- val: 1.0
- aro: 1.0
- int: 1.0
- loc: 1.0
- tex: 1.5
- con: 1.0
- cer: 0.5
- src: 0.5
- act: 1.0

### Route 1 rationale
- `tex` gets 1.5 because tactile/affective texture carries a large share of felt-structure distinction and supports useful partial matches.
- `val`, `aro`, `int`, `loc`, `con`, and `act` get 1.0 because they each change the state profile materially.
- `mod` gets 0.5 because within Route 1 it is usually constrained already.
- `cer` and `src` get 0.5 because they are important but secondary to core reconstruction.
- `src` is kept because it may matter in memory-triggered vs reactive cases, but it is not yet central enough to outweigh the state form itself.

## Route 2 current weights
- mod: 0.5
- val: 0.5
- viv: 1.0
- bri: 1.0
- loc: 1.0
- col: 1.0
- tex: 1.5
- con: 1.0
- stb: 0.75
- cer: 0.5

### Route 2 rationale
- `tex` gets 1.5 because visual clarity/texture carries major structural discrimination and often partially overlaps in informative ways.
- `viv`, `bri`, `loc`, `col`, and `con` get 1.0 because each materially changes the percept structure.
- `stb` gets 0.75 because it matters more than metadata, but less than direct appearance structure.
- `val` gets 0.5 because visual valence is often weaker and more derivative in this route.
- `mod` gets 0.5 because route identity constrains the domain already.
- `cer` gets 0.5 because it is about encoding confidence, not the percept itself.

## Why texture gets partial-credit handling
Texture fields are richer and more confusable than simple categorical fields.
Examples:
- Route 1: `TIGHT+SHARP` vs `TIGHT+PRESS`
- Route 2: `SHARP` vs `EDGE+SHARP`

Exact match should not be the only meaningful outcome. Jaccard-style overlap is acceptable at this stage.

## Why not make all weights equal
Equal weights would imply:
- certainty is as important as locus
- route-local metadata is as important as core content
- weak fields matter as much as structurally central fields

That would flatten the reconstruction problem too much.

## Why not make one or two fields dominant
Overweighting a few fields would allow high scores from partial caricatures:
- color-only success in Route 2
- valence-only success in Route 1

The current weighting tries to avoid that.

## Current risks
These weights may still be wrong because:
- they are pre-human
- they reflect design judgment
- field importance may differ by subtask
- some fields may be easier/harder than expected
- partial-credit behavior may overreward near-misses

## What will justify later revision
Revise weights after:
- pilot confusion matrices
- field-wise miss rates
- user feedback on which distinctions feel central
- adversarial score inflation tests
- baseline comparison results

## Explicit non-claim
The current weights are route-local engineering priors. They are not objective truths about experience.
