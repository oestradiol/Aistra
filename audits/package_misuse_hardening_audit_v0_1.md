# Package misuse hardening audit

## Purpose
This memo records the misuse modes that were explicitly reduced during package cleanup.

## Main misuse modes addressed
- Confusing examples with launch artifacts.
- Confusing generated verification outputs with source-of-truth definitions.
- Reaching into deprecated Route 1 pilot files because they remained visible.
- Running low-level scoring scripts with stale or ad hoc gold paths.
- Treating Route 2 as pilot-ready despite its documented pre-human status.

## Controls now present
- Directory separation makes non-canonical materials visibly distinct.
- Top-level handoff docs point to current authoritative files only.
- The Route 1 wrapper enforces the launch gate before scoring.
- State summaries and authoritative indices agree on Route 1 pilot-ready and Route 2 pre-human.

## Residual boundary
A determined operator can still bypass documentation and call low-level code manually. The package is hardened against common misuse, not against arbitrary hostile execution outside the documented path.

## Current status
Retained for audit history. Not a launch instruction file.
