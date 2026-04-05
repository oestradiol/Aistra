from __future__ import annotations
import sys
sys.dont_write_bytecode = True
import json
from typing import Dict, Any, List
from parser import parse

DEFAULT_WEIGHTS = {
    "mod": 0.5,
    "val": 0.5,
    "viv": 1.0,
    "bri": 1.0,
    "loc": 1.0,
    "col": 1.0,
    "tex": 1.5,
    "con": 1.0,
    "stb": 0.75,
    "cer": 0.5,
}
FIELDS = ["mod", "val", "viv", "bri", "loc", "col", "tex", "con", "stb", "cer"]

def _norm(v: Any) -> List[str]:
    return v if isinstance(v, list) else [v]

def _field_score(field: str, gold: Any, pred: Any, weight: float) -> Dict[str, Any]:
    g = _norm(gold); p = _norm(pred)
    if field == "tex":
        gs, ps = set(g), set(p)
        if gs == ps:
            raw, mt = 1.0, "exact"
        else:
            inter, union = len(gs & ps), len(gs | ps)
            raw = inter / union if union else 0.0
            mt = "partial" if raw > 0 else "none"
    else:
        gs, ps = set(g), set(p)
        if gs == ps:
            raw, mt = 1.0, "exact"
        elif gs & ps:
            raw, mt = 0.5, "partial"
        else:
            raw, mt = 0.0, "none"
    return {"field": field, "gold": gold, "pred": pred, "match_type": mt, "raw_score": raw, "weight": weight, "weighted_score": raw * weight}

def compare_objects(gold_obj: Dict[str, Any], pred_obj: Dict[str, Any], weights: Dict[str, float] | None = None) -> Dict[str, Any]:
    weights = weights or DEFAULT_WEIGHTS
    field_results = []
    total = 0.0
    earned = 0.0
    for field in FIELDS:
        w = weights.get(field, 1.0)
        total += w
        fr = _field_score(field, gold_obj[field], pred_obj[field], w)
        earned += fr["weighted_score"]
        field_results.append(fr)
    return {
        "score": round(earned / total if total else 0.0, 4),
        "earned_weight": round(earned, 4),
        "total_weight": round(total, 4),
        "exact_fields": [r["field"] for r in field_results if r["match_type"] == "exact"],
        "partial_fields": [r["field"] for r in field_results if r["match_type"] == "partial"],
        "missed_fields": [r["field"] for r in field_results if r["match_type"] == "none"],
        "field_results": field_results,
    }

def score_texts(gold_text: str, pred_text: str, weights: Dict[str, float] | None = None) -> Dict[str, Any]:
    gold = parse(gold_text)
    pred = parse(pred_text)
    if not gold.valid:
        return {"valid": False, "stage": "gold_parse", "error": {"error_type": gold.error_type, "slot": gold.slot, "token": gold.token, "message": gold.message}}
    if not pred.valid:
        return {"valid": False, "stage": "pred_parse", "error": {"error_type": pred.error_type, "slot": pred.slot, "token": pred.token, "message": pred.message}, "gold_canonical": gold.canonical}
    comp = compare_objects(gold.object, pred.object, weights=weights)
    return {"valid": True, "gold_canonical": gold.canonical, "pred_canonical": pred.canonical, "gold_gloss": gold.gloss, "pred_gloss": pred.gloss, **comp}

def load_jsonl(path: str):
    rows = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            rows.append(json.loads(line))
    return rows

def score_predictions_file(gold_path: str, predictions_path: str, weights: Dict[str, float] | None = None) -> Dict[str, Any]:
    gold_rows = load_jsonl(gold_path)
    pred_rows = load_jsonl(predictions_path)
    gold_by_id = {r["id"]: r for r in gold_rows}
    pred_by_id = {r["id"]: r for r in pred_rows}
    results = []
    scores = []
    for rid, grow in gold_by_id.items():
        prow = pred_by_id.get(rid)
        if prow is None:
            results.append({"id": rid, "valid": False, "stage": "lookup", "error": {"message": "Missing prediction for id"}})
            continue
        res = score_texts(grow.get("surface") or grow.get("canonical"), prow.get("prediction") or prow.get("surface") or prow.get("canonical"), weights=weights)
        res["id"] = rid
        results.append(res)
        if res.get("valid"):
            scores.append(res["score"])
    return {"n_gold": len(gold_rows), "n_predictions": len(pred_rows), "n_scored": len(scores), "average_score": round(sum(scores)/len(scores), 4) if scores else 0.0, "results": results}
