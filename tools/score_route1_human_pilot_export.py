from __future__ import annotations
import sys
sys.dont_write_bytecode = True
import json
import sys
from pathlib import Path

FIELDS = ["valence", "arousal", "intensity", "location", "texture", "contour", "certainty", "source", "action"]
CANON_TO_LABEL = {
    "valence": {"NEG": "negative", "NEU": "neutral", "POS": "positive", "MIX": "mixed"},
    "arousal": {"L": "low", "M": "medium", "H": "high"},
    "intensity": {"1": "1", "2": "2", "3": "3"},
    "location": {"CH": "chest", "TH": "throat", "AB": "abdomen", "HD": "head", "SK": "skin", "WH": "whole body", "DF": "diffuse"},
    "texture": {"TIGHT": "tight", "WARM": "warm", "SHARP": "sharp", "HEAVY": "heavy", "HOLLOW": "hollow", "BUZZ": "buzz", "PRESS": "pressure", "OPEN": "open", "CALM": "calm", "RAW": "raw"},
    "contour": {"STAT": "static", "RISE": "rising", "FALL": "falling", "PULSE": "pulsing", "WAVE": "wave-like", "OSC": "oscillating"},
    "certainty": {"LOW": "low", "MED": "medium", "HIGH": "high"},
    "source": {"SELF": "self", "REACT": "reactive", "MEM": "memory", "UNC": "unclear"},
    "action": {"APP": "approach", "AVO": "avoid", "FRZ": "freeze", "RST": "rest", "DIS": "discharge", "NON": "none"},
}


def normalize(field: str, value: str) -> str:
    v = str(value).strip().lower()
    if field == "source" and v == "unknown":
        return "unclear"
    if field == "contour" and v == "wavy":
        return "wave-like"
    return v


def parse(canonical: str):
    mod, val, aro, intensity, loc, tex, contour, certainty, source, action = canonical.split('.')
    return {
        "modality": mod,
        "valence": CANON_TO_LABEL["valence"][val],
        "arousal": CANON_TO_LABEL["arousal"][aro],
        "intensity": CANON_TO_LABEL["intensity"][intensity],
        "location": CANON_TO_LABEL["location"][loc],
        "texture": sorted([CANON_TO_LABEL["texture"][t] for t in tex.split('+') if t]),
        "contour": CANON_TO_LABEL["contour"][contour],
        "certainty": CANON_TO_LABEL["certainty"][certainty],
        "source": CANON_TO_LABEL["source"][source],
        "action": CANON_TO_LABEL["action"][action],
    }


def score_against_expected(resp, expected):
    predicted = {
        "valence": normalize("valence", resp["valence"]),
        "arousal": normalize("arousal", resp["arousal"]),
        "intensity": normalize("intensity", resp["intensity"]),
        "location": normalize("location", resp["location"]),
        "texture": sorted([normalize("texture", t) for t in [resp.get("texture1", ""), resp.get("texture2", "")] if t]),
        "contour": normalize("contour", resp["contour"]),
        "certainty": normalize("certainty", resp["certainty"]),
        "source": normalize("source", resp["source"]),
        "action": normalize("action", resp["action"]),
    }
    fields = {f: predicted[f] == expected[f] for f in FIELDS}
    return {
        "predicted_fields": predicted,
        "expected_fields": expected,
        "field_matches": fields,
        "exact_9_score": sum(fields.values()),
        "exact_match": all(fields.values()),
    }


def score_response(resp, key_row):
    candidates = [key_row["expected_canonical"], *key_row.get("acceptable_alternates", [])]
    scored = []
    for idx, canonical in enumerate(candidates):
        expected = parse(canonical)
        scored.append({
            "canonical": canonical,
            "is_primary": idx == 0,
            "result": score_against_expected(resp, expected),
        })
    scored.sort(key=lambda x: (-x["result"]["exact_9_score"], 0 if x["is_primary"] else 1))
    best = scored[0]
    return {
        "predicted_canonical": None,
        "expected_canonical": key_row["expected_canonical"],
        "acceptable_alternates": key_row.get("acceptable_alternates", []),
        "matched_policy": "primary" if best["is_primary"] else "alternate",
        "best_match": {
            "matched_canonical": best["canonical"],
            **best["result"],
        },
        "status": "exact" if best["result"]["exact_match"] else "scored",
    }


def summarize(rows):
    by_field = {f: {"hits": 0, "total": 0} for f in FIELDS}
    by_condition = {}
    completed = 0
    exact_matches = 0
    total_hits = 0
    for row in rows:
        cond = row["condition"]
        by_condition.setdefault(cond, {"items": 0, "completed": 0, "exact_matches": 0, "exact_field_hits": 0})
        by_condition[cond]["items"] += 1
        scoring = row.get("scoring", {})
        if scoring.get("status") == "missing":
            continue
        completed += 1
        by_condition[cond]["completed"] += 1
        best = scoring["best_match"]
        total_hits += best["exact_9_score"]
        by_condition[cond]["exact_field_hits"] += best["exact_9_score"]
        if best["exact_match"]:
            exact_matches += 1
            by_condition[cond]["exact_matches"] += 1
        for f in FIELDS:
            by_field[f]["total"] += 1
            if best["field_matches"][f]:
                by_field[f]["hits"] += 1
    return {
        "items_total": len(rows),
        "items_completed": completed,
        "exact_matches": exact_matches,
        "total_exact_field_hits": total_hits,
        "field_accuracy": {
            f: {
                "hits": stats["hits"],
                "total": stats["total"],
                "rate": round(stats["hits"] / stats["total"], 4) if stats["total"] else None,
            } for f, stats in by_field.items()
        },
        "condition_breakdown": by_condition,
    }


def build_report(out):
    lines = [
        "# Route 1 human pilot report",
        "",
        f"- package: {out.get('package_name', 'unknown')}",
        f"- app_version: {out.get('app_version', 'unknown')}",
        f"- scorer_version: {out.get('scorer_version', 'unknown')}",
        f"- exported_at: {out.get('exported_at', 'unknown')}",
        f"- packet_source: {out.get('packet_source', 'unknown')}",
        f"- answer_key_source: {out.get('answer_key_source', 'unknown')}",
        f"- packet_sha256: {out.get('packet_sha256', 'unknown')}",
        f"- answer_key_sha256: {out.get('answer_key_sha256', 'unknown')}",
        f"- config_sha256: {out.get('config_sha256', 'unknown')}",
        "",
        "## Summary",
        f"- items_total: {out['summary']['items_total']}",
        f"- items_completed: {out['summary']['items_completed']}",
        f"- exact_matches: {out['summary']['exact_matches']}",
        f"- total_exact_field_hits: {out['summary']['total_exact_field_hits']}",
        "",
        "## Field accuracy",
    ]
    for field, stats in out["summary"]["field_accuracy"].items():
        lines.append(f"- {field}: {stats['hits']}/{stats['total']} ({stats['rate']})")
    lines.extend(["", "## Condition breakdown"])
    for cond, stats in out["summary"]["condition_breakdown"].items():
        lines.append(f"- {cond}: items={stats['items']}, completed={stats['completed']}, exact_matches={stats['exact_matches']}, exact_field_hits={stats['exact_field_hits']}")
    lines.extend(["", "## Item results"])
    for row in out["responses"]:
        lines.append(f"### {row['id']} ({row['condition']})")
        lines.append(f"- stimulus: {row['stimulus']}")
        scoring = row.get("scoring", {})
        if scoring.get("status") == "missing":
            lines.append("- status: missing")
            lines.append("")
            continue
        best = scoring['best_match']
        lines.append(f"- predicted_canonical: {row.get('prediction_canonical')}")
        lines.append(f"- expected_canonical: {scoring['expected_canonical']}")
        lines.append(f"- matched_policy: {scoring['matched_policy']}")
        lines.append(f"- matched_canonical: {best['matched_canonical']}")
        lines.append(f"- exact_9_score: {best['exact_9_score']}")
        lines.append(f"- exact_match: {best['exact_match']}")
        lines.append(f"- field_matches: {json.dumps(best['field_matches'])}")
        lines.append("")
    return "\n".join(lines) + "\n"


def main():
    if len(sys.argv) != 3:
        print("usage: python tools/score_route1_human_pilot_export.py <results.json> <packet_config.json>")
        raise SystemExit(2)
    results_path = Path(sys.argv[1])
    cfg_path = Path(sys.argv[2])
    results = json.loads(results_path.read_text(encoding='utf-8'))
    cfg = json.loads(cfg_path.read_text(encoding='utf-8'))
    key = cfg["answer_key"]
    scored = []
    for row in results["responses"]:
        resp = row["response"]
        if resp is None:
            scored.append({**row, "scoring": {"status": "missing"}})
            continue
        score = score_response(resp, key[row["id"]])
        score["predicted_canonical"] = row.get("prediction_canonical")
        scored.append({**row, "scoring": score})
    out = {**results, "responses": scored}
    out["summary"] = summarize(scored)
    out_path = results_path.with_suffix('.scored.json')
    out_path.write_text(json.dumps(out, ensure_ascii=False, indent=2) + "\n", encoding='utf-8')
    report_path = results_path.with_suffix('.report.md')
    report_path.write_text(build_report(out), encoding='utf-8')
    print(out_path)
    print(report_path)


if __name__ == '__main__':
    main()
