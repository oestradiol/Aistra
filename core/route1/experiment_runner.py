from __future__ import annotations
import argparse
import json
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parent
ROOT = BASE.parents[1]
sys.path.insert(0, str(BASE))
sys.path.insert(0, str(ROOT))
from scorer import score_predictions_file  # noqa
from authoritative_guard import current_route1_answer_key, assert_current_route1_artifact, AuthorityError  # noqa

def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    score = sub.add_parser("score")
    score.add_argument("--gold", required=True)
    score.add_argument("--predictions", required=True)
    score.add_argument("--out", required=True)
    score.add_argument("--allow-noncurrent", action="store_true")
    args = ap.parse_args()

    if args.cmd == "score":
        gold_rel = str(Path(args.gold).resolve().relative_to(ROOT.resolve())).replace('\\','/') if Path(args.gold).is_absolute() else args.gold
        current = current_route1_answer_key()
        if not args.allow_noncurrent:
            assert_current_route1_artifact(gold_rel, allowed=[current], label="Route 1 answer key")
        payload = score_predictions_file(args.gold, args.predictions)
        Path(args.out).write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

if __name__ == "__main__":
    main()
