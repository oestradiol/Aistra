# Design decision note v0.1

## Decision
Keep **two baseline modes** and separate their purpose.

1. **Baseline-explicit** = scored calibration mode
2. **Baseline-natural** = exploratory ecological mode

Do **not** mix them into a single score stream.

## Why this is optimal
The project has two partially conflicting goals:
- preserve something recognizably human and natural in plain-language state description
- obtain valid, field-by-field scored administration

A single baseline mode cannot optimize both at once.

Natural prompts feel more human, but they underdetermine source, certainty, contour, and sometimes intensity. That makes participant inference indistinguishable from measurement error.

Explicit prompts are less natural, but they make the 9-field target legible and scorable. That is the correct choice for calibration, training, and handoff-grade verification.

Therefore:
- use **explicit baseline** whenever the goal is reliability, calibration, regression testing, or package validation
- use **natural baseline** only when the goal is ecological realism, qualitative observation, or later-stage construct stress testing

## Operational rule
- The current shipped packet remains **baseline-explicit**.
- Any future **baseline-natural** packet must be versioned separately and must not be merged into the same accuracy summary as explicit items.

## Human-factor reasoning
What it means to feel human here is not “use the loosest possible language.” Human feeling is usually richer than the words available for it. When language is underspecified, people fill gaps with context, memory, and coherence-making.

That is a real human behavior, but in this project it confounds scoring.

So the optimal structure is:
- first, calibrate with explicit prompts to prove the schema is learnable and administrable
- later, test natural prompts as a separate challenge layer

This respects both:
- the human tendency to interpret meaningfully
- the measurement need to distinguish perception from inference

## Near-term implication
For the next validation phase:
- keep the current explicit baseline in the main packet
- do not widen the ontology yet
- add a later optional `baseline_natural_packet_v0_1` only after explicit-mode performance stabilizes across multiple users

## Success criterion for this decision
This fork was the right choice if:
- explicit-mode multi-user pilots produce clear field-level error maps
- natural-mode later shows where real-world prose breaks the schema, without corrupting calibration results
