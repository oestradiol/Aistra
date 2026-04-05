from __future__ import annotations
import sys
sys.dont_write_bytecode = True
import json
import importlib.util
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent

def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod

def run():
    suite_path = Path(__file__).resolve().parent / "adversarial_cases.json"
    suite = json.loads(suite_path.read_text(encoding="utf-8"))

    r1_dir = BASE / "core/route1"
    r2_dir = BASE / "route2_visual_v0_1"

    r1_parser = load_module("adv_r1_parser", r1_dir / "parser.py")
    sys.modules["parser"] = r1_parser
    r1_scorer = load_module("adv_r1_scorer", r1_dir / "scorer.py")

    r2_parser = load_module("adv_r2_parser", r2_dir / "parser.py")
    sys.modules["parser"] = r2_parser
    r2_scorer = load_module("adv_r2_scorer", r2_dir / "scorer.py")

    route_control = load_module("adv_route_control", BASE / "core/common/route_control.py")

    results = {"route1": [], "route2": [], "route_control": []}

    for case in suite["route1"]["parse_should_fail"]:
        res = r1_parser.parse(case["text"])
        ok = (not res.valid) and res.error_type == case["expect"]
        results["route1"].append({"id": case["id"], "kind": "parse_should_fail", "ok": ok, "got": res.error_type, "expect": case["expect"]})

    for case in suite["route1"]["score_adversarial_pairs"]:
        res = r1_scorer.score_texts(case["gold"], case["pred"])
        score = res["score"] if res.get("valid") else None
        ok = res.get("valid") and case["expect_min"] <= score <= case["expect_max"]
        results["route1"].append({"id": case["id"], "kind": "score_adversarial_pairs", "ok": ok, "score": score, "expect_min": case["expect_min"], "expect_max": case["expect_max"]})

    for case in suite["route2"]["parse_should_fail"]:
        res = r2_parser.parse(case["text"])
        ok = (not res.valid) and res.error_type == case["expect"]
        results["route2"].append({"id": case["id"], "kind": "parse_should_fail", "ok": ok, "got": res.error_type, "expect": case["expect"]})

    for case in suite["route2"]["score_adversarial_pairs"]:
        res = r2_scorer.score_texts(case["gold"], case["pred"])
        score = res["score"] if res.get("valid") else None
        ok = res.get("valid") and case["expect_min"] <= score <= case["expect_max"]
        results["route2"].append({"id": case["id"], "kind": "score_adversarial_pairs", "ok": ok, "score": score, "expect_min": case["expect_min"], "expect_max": case["expect_max"]})

    for case in suite["route_control"]["classification_checks"]:
        res = route_control.classify_text(case["text"])
        ok = res["route"] == case["expect"]
        results["route_control"].append({"id": case["id"], "kind": "classification_checks", "ok": ok, "got": res["route"], "expect": case["expect"]})

    for case in suite["route_control"]["assignment_checks"]:
        res = route_control.validate_route_assignment(case["text"], case["claimed"])
        ok = res["ok"] == case["expect_ok"]
        results["route_control"].append({"id": case["id"], "kind": "assignment_checks", "ok": ok, "got": res["ok"], "expect": case["expect_ok"]})

    flat = results["route1"] + results["route2"] + results["route_control"]
    summary = {
        "n_checks": len(flat),
        "n_passed": sum(1 for x in flat if x["ok"]),
        "n_failed": sum(1 for x in flat if not x["ok"]),
        "results": results,
    }
    out = Path(__file__).resolve().parents[1] / "reports" / "generated" / "adversarial_suite_v0_1" / "adversarial_report.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    return summary

if __name__ == "__main__":
    print(json.dumps(run(), ensure_ascii=False, indent=2))
