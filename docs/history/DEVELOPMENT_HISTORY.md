# Development history

This file keeps the useful parts of the package hardening history without shipping every intermediate memo and generated artifact.

## What changed over the course of development
- The project moved from a loose handoff bundle into a bounded package with a defined front door, route split, scoring path, and governance layer.
- The largest lexical bug in Route 1 was fixed by replacing the whole-body token `holo` with `woba`, leaving `hol` for hollow.
- Human testing showed that the structured route was learnable but the original baseline wording was too ambiguous, especially for source, certainty, and sometimes contour.
- A local pilot app replaced manual operator paraphrase, which reduced administration drift and made exports reproducible.
- Alternate-aware scoring was implemented end to end in both the app and the local scorer.
- Repo governance expanded from root-only cleanliness to current-surface truth checks and then to a full repository file registry.

## Design decisions worth retaining
- Route 1 is an explicit-calibration route, not a naturalistic phenomenology route.
- Baseline-explicit prompts are kept separate from any future baseline-natural prompts.
- Route 1 remains pilot-ready but not broadly validated.
- Route 2 remains pre-human.
- Integrity checks prove alignment and reproducibility, not scientific truth by themselves.

## What was removed from the shipped package
The following classes of material were removed once their useful content had been extracted here or into current docs:
- historical handoff guides that no longer define current behavior
- generated verification artifacts that can be reproduced on demand
- old audit memos whose still-useful points are now summarized in current front-door or spec documents
- stored pilot run outputs that are no longer required to operate or verify the package

## Why this is enough
The package now keeps:
- the current front door
- the current governance and specs
- the current route assets and app
- the research-grounding layer
- the superseded Route 1 materials needed for traceability

It no longer keeps extra historical clutter just because it once existed.
