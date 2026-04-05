# Baseline protocol memo v0.3 clarity rewrite

## Purpose
This memo records the v0.3 rewrite of the Route 1 baseline prompts after human pilot testing showed that plain-language items were underdetermined on source, certainty, and sometimes contour.

## Findings that triggered the rewrite
- The structured route became stable after the `hol` → `woba` whole-body token fix.
- Remaining misses concentrated in the baseline prompts, especially source (`reactive` vs `self`) and certainty (`low` vs `high`).
- When the text left these fields implicit, participants filled them in by coherent interpretation rather than by direct textual support.

## Design rule adopted in v0.3
Each baseline prompt now explicitly supports all 9 scored fields:
- valence
- arousal
- intensity
- location
- texture
- contour
- certainty
- source
- action

## Current v0.3 baseline prompts
- PR2: A clearly reactive positive state: low arousal, low intensity, warm on the skin, static, high certainty, and gently inviting approach.
- B1: A clearly reactive negative state in the chest: high arousal, moderate intensity, tight and sharp, rising, high certainty, and pushing toward freeze.
- B2: A clearly reactive positive state in the abdomen: low arousal, moderate intensity, warm and open, falling/easing, high certainty, and settling toward rest.
- B3: A mixed state spread diffusely: low arousal, low intensity, hollow, mostly static, low certainty, unclear source, and no clear action pull.
- B4: A clearly reactive negative whole-body state: high arousal, high intensity, buzz and pressure, oscillating, low certainty, and tending toward discharge.

## Consequence
The v0.3 baseline route is less naturalistic but more valid as a scored stimulus set. The package now favors field-identifiability over prose naturalness.
