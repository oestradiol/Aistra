# Thread lossless compression v0.3

## Thread map
1. human pilot administration began manually.
2. early testing exposed operator drift and one real lexical collision: `hol` vs `holo`.
3. the package was patched to use `woba` for whole body.
4. a local browser app replaced manual operator administration.
5. exported pilot results showed structured items were strong and baseline prompts were the main ambiguity source.
6. baseline prompts were rewritten into explicit calibration form.
7. scoring, reports, specs, tests, and handoff materials were added through v0.4.
8. skeptical review in v0.5 found remaining package-level weaknesses: stale front-door clutter, config duplication drift risk, app/scorer alternate-awareness gap, stale human-testing status, and weak run provenance.
9. v0.5 fixed those package-integrity weaknesses without changing Route 1 semantics.

## Global signal compression
- SUF helped because it factorized subjective-state reports into inspectable slots.
- the biggest empirical gain came from making error sources visible.
- the biggest package failures were not conceptual; they were lexical collision, operator dependence, and ambiguous baseline stimuli.
- the project is now a handoff-ready prototype instrument, not a validated scientific measure.

## Conclusions
- Route 1 structured language is usable.
- baseline-explicit calibration is the correct current scored mode.
- naturalistic baseline should remain a separate future packet.
- the next true frontier is multi-user validation, not more foundational packaging cleanup.
