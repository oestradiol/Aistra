# Project spec v0.1

## What SUF Route 1 is
A compact structured language and pilot instrument for representing subjective felt-state reports across 9 fields:
valence, arousal, intensity, location, texture, contour, certainty, source, and action.

## What it is trying to do
1. define a small compositional ontology for state description
2. test whether humans can reliably map both tokenized and plain-language stimuli into that ontology

## Current status
- prototype instrument
- handoff-ready local pilot package
- not yet a validated scientific measurement tool

## Intended uses
- structured annotation of subjective-state descriptions
- calibration/training for embodied-state labeling
- interface layer between natural language and structured state representation
- pilot research on human learnability and field-level error patterns

## Non-goals
- diagnosis
- clinical decision support
- claims of validated psychometric measurement
- claims that the ontology fully captures all human feeling

## Route split
- structured route: tokenized, fixed-slot prompts
- baseline-explicit route: plain-language prompts that explicitly encode all scored fields
- future optional baseline-natural route: exploratory only, unmerged with calibration metrics

## Evidence stance
Current evidence supports:
- learnability
- practical administrability
- usefulness for structured error localization

Current evidence does not yet support:
- strong external validity claims
- robust psychometric reliability claims across populations
- field reduction or ontology finality
