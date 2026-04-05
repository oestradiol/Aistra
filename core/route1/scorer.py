from __future__ import annotations
import sys
sys.dont_write_bytecode = True
import json
from pathlib import Path
import sys
from pathlib import Path
BASE = Path(__file__).resolve().parent
sys.path.insert(0, str(BASE))
from parser import parse

FIELDS = ["mod","val","aro","int","loc","tex","con","cer","src","act"]
WEIGHTS = {"mod":1/18,"val":2/18,"aro":2/18,"int":2/18,"loc":2/18,"tex":2/18,"con":2/18,"cer":2/18,"src":2/18,"act":1/18}

def canonical_to_map(canonical: str):
    parts = canonical.split(".")
    if len(parts) != 10:
        raise ValueError("bad canonical")
    out = dict(zip(FIELDS, parts))
    out["tex"] = [t for t in out["tex"].split("+") if t]
    return out

def field_match(field, gold, pred):
    if field == "tex":
        gs, ps = set(gold), set(pred)
        if gs == ps:
            return "exact"
        if gs & ps:
            return "partial"
        return "none"
    return "exact" if gold == pred else "none"

def score_against(gold_canonical: str, pred_canonical: str):
    gold = canonical_to_map(gold_canonical)
    pred = canonical_to_map(pred_canonical)
    exact_fields, partial_fields, missed_fields, field_results = [], [], [], []
    score = 0.0
    for f in FIELDS:
        match_type = field_match(f, gold[f], pred[f])
        if match_type == "exact":
            exact_fields.append(f); score += WEIGHTS[f]
        elif match_type == "partial":
            partial_fields.append(f); score += WEIGHTS[f] / 2.0
        else:
            missed_fields.append(f)
        field_results.append({"field": f, "match_type": match_type})
    return {
        "score": round(score, 4),
        "exact_fields": exact_fields,
        "partial_fields": partial_fields,
        "missed_fields": missed_fields,
        "field_results": field_results,
    }

def score_predictions_file(gold_path: str, pred_path: str):
    gold_rows = [json.loads(line) for line in Path(gold_path).read_text(encoding="utf-8").splitlines() if line.strip()]
    pred_rows = {json.loads(line)["id"]: json.loads(line).get("prediction", "") for line in Path(pred_path).read_text(encoding="utf-8").splitlines() if line.strip()}
    results = []
    valid_scores = []
    for row in gold_rows:
        pred_text = pred_rows.get(row["id"], "") or ""
        pred_parse = parse(pred_text)
        if not pred_parse.valid:
            results.append({"id": row["id"], "valid": False, "stage": "pred_parse", "error_type": pred_parse.error_type})
            continue
        candidates = [row.get("expected_canonical") or row.get("canonical")]
        for alt in row.get("acceptable_alternates", []):
            if isinstance(alt, dict) and alt.get("expected_canonical"):
                candidates.append(alt["expected_canonical"])
        candidate_results = []
        best = None
        for cand in candidates:
            r = score_against(cand, pred_parse.canonical)
            snap = {
                "candidate": cand,
                "score": r["score"],
                "exact_fields": list(r["exact_fields"]),
                "partial_fields": list(r["partial_fields"]),
                "missed_fields": list(r["missed_fields"]),
            }
            candidate_results.append(snap)
            if best is None or snap["score"] > best["score"]:
                best = snap
                best_detail = r
        out = {
            "id": row["id"],
            "valid": True,
            "score": best_detail["score"],
            "exact_fields": best_detail["exact_fields"],
            "partial_fields": best_detail["partial_fields"],
            "missed_fields": best_detail["missed_fields"],
            "field_results": best_detail["field_results"],
            "candidate_results": candidate_results,
        }
        results.append(out)
        valid_scores.append(best_detail["score"])
    return {
        "n_gold": len(gold_rows),
        "n_scored": len(valid_scores),
        "average_score": round(sum(valid_scores)/len(valid_scores), 4) if valid_scores else 0.0,
        "results": results,
    }


def score_texts(gold_text: str, pred_text: str):
    gp = parse(gold_text)
    pp = parse(pred_text or "")
    if not gp.valid:
        return {"valid": False, "stage": "gold_parse", "error_type": gp.error_type}
    if not pp.valid:
        return {"valid": False, "stage": "pred_parse", "error_type": pp.error_type}
    res = score_against(gp.canonical, pp.canonical)
    res["valid"] = True
    return res
