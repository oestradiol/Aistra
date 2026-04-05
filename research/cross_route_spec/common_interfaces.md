# Cross-route package spec v0.1

## Purpose
This spec defines the shared interfaces across bounded routes in the SUF-shaped experiential language project.

Current routes:
- Route 1 — interoceptive-affective microstates
- Route 2 — visual phenomenological microstructures

This spec does **not** merge route ontologies. It standardizes:
- package metadata
- file conventions
- parser/scorer/runner interfaces
- experiment report shape
- route-control handoff rules

## Core package principles
1. Shared scaffold, route-local content
2. No silent ontology mixing
3. Same lifecycle state labels across routes
4. Same JSONL and report conventions
5. Route-control runs before parser selection when route is unknown

## Required route artifacts
Each route package must expose:
- `core/route1/gold_valid.jsonl`
- `core/route1/gold_invalid.jsonl`
- `core/route1/correction_pairs.jsonl`
- `core/route1/parser.py`
- `core/route1/scorer.py`
- `core/route1/experiment_runner.py`
- `README.md`

## Minimal parser interface
Each route parser should expose:
- `parse(text: str) -> ParseResult`
- `parse_surface(text: str) -> ParseResult`
- `parse_canonical(text: str) -> ParseResult`

`ParseResult` fields:
- `valid: bool`
- `canonical: str | None`
- `object: dict | None`
- `gloss: str | None`
- `error_type: str | None`
- `slot: str | None`
- `token: str | None`
- `message: str | None`

## Minimal scorer interface
Each route scorer should expose:
- `score_texts(gold_text: str, pred_text: str, weights: dict | None = None) -> dict`
- `score_predictions_file(gold_path: str, predictions_path: str, weights: dict | None = None) -> dict`

Shared scorer output keys:
- `valid`
- `gold_canonical`
- `pred_canonical`
- `gold_gloss`
- `pred_gloss`
- `score`
- `earned_weight`
- `total_weight`
- `exact_fields`
- `partial_fields`
- `missed_fields`
- `field_results`

## Minimal experiment-runner interface
Each route runner should expose:
- `make_blind_packet(gold_path, output_path, n=10, seed=42, include_gloss=False) -> dict`
- `make_blank_predictions(packet_path, output_path) -> dict`
- `score_run(gold_path, predictions_path, report_path) -> dict`

## Shared JSONL conventions

### Gold valid row
```json
{
  "id": "string",
  "surface": "string",
  "canonical": "string",
  "gloss": "string"
}
```

Optional:
- `expected`
- `expected_flags`
- `note`

### Gold invalid row
```json
{
  "id": "string",
  "input": "string",
  "mode": "surface|canonical",
  "error_type": "string",
  "message": "string"
}
```

Optional:
- `slot`
- `token`

### Correction pair row
```json
{
  "id": "string",
  "bad": "string",
  "good": "string",
  "reason": "string"
}
```

### Prediction row
```json
{
  "id": "string",
  "prediction": "string"
}
```

## Unified experiment report schema
```json
{
  "package": "aistra",
  "version": "0.1.0",
  "route_id": "route1_intero_affective",
  "n_gold": 20,
  "n_predictions": 20,
  "n_scored": 18,
  "average_score": 0.84,
  "results": [
    {
      "id": "V01",
      "valid": true,
      "gold_canonical": "...",
      "pred_canonical": "...",
      "score": 0.91,
      "exact_fields": [],
      "partial_fields": [],
      "missed_fields": [],
      "field_results": []
    }
  ]
}
```

## Shared lifecycle states
Allowed per-route `status` values:
- `design`
- `pre_human`
- `pilot_ready`
- `pilot_running`
- `pilot_review`
- `frozen`

Current package posture:
- Route 1: `pre_human`
- Route 2: `pre_human`

## Route-control handoff
When route is not already known:
1. classify via `core/common/route_control.py`
2. if confident route is returned, dispatch to that route package
3. if `defer_mixed_or_out_of_scope`, do not force parse
4. require future mixed-route layer rather than silent fallback

## Package expansion rule
A new route can be added only if:
- its domain is bounded
- its ontology is route-local
- its parser/scorer/runner implement the shared interface
- route-control policy is updated
- it does not silently reuse incompatible fields from another route

## Current non-goals
This cross-route spec does not yet define:
- mixed-route encoding
- human-subject data collection surfaces
- UI
- learned models
- route fusion scoring
- cross-route semantic translation
