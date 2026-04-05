from __future__ import annotations
import argparse
import json
import subprocess
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(BASE))
from authoritative_guard import current_route1_answer_key  # noqa

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--responses", required=True)
    ap.add_argument("--run-dir", required=True)
    args = ap.parse_args()

    run_dir = Path(args.run_dir)
    run_dir.mkdir(parents=True, exist_ok=True)

    subprocess.run([sys.executable, str(BASE / "route1_launch_gate.py")], check=True)
    pred_path = run_dir / "predictions.jsonl"
    subprocess.run([sys.executable, str(BASE / "tools" / "convert_route1_responses_to_predictions.py"), args.responses, str(pred_path)], check=True)
    scored_path = run_dir / "scored_report.json"
    subprocess.run([
        sys.executable, str(BASE / "core/route1/experiment_runner.py"), "score",
        "--gold", str(BASE / current_route1_answer_key()),
        "--predictions", str(pred_path),
        "--out", str(scored_path)
    ], check=True)
    manifest = {
        "responses": args.responses,
        "predictions": str(pred_path),
        "scored_report": str(scored_path),
        "answer_key": current_route1_answer_key(),
    }
    (run_dir / "run_manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

if __name__ == "__main__":
    main()
