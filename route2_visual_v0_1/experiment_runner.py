from __future__ import annotations
import json, random, argparse
from pathlib import Path
from typing import Dict, Any, List
from scorer import score_predictions_file

def load_jsonl(path: str) -> List[Dict[str, Any]]:
    rows = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            rows.append(json.loads(line))
    return rows

def write_jsonl(path: str, rows: List[Dict[str, Any]]) -> None:
    with open(path, "w", encoding="utf-8") as f:
        for row in rows:
            f.write(json.dumps(row, ensure_ascii=False) + "\n")

def make_blind_packet(gold_path: str, output_path: str, n: int = 10, seed: int = 42, include_gloss: bool = False) -> Dict[str, Any]:
    gold_rows = load_jsonl(gold_path)
    rng = random.Random(seed)
    chosen = rng.sample(gold_rows, min(n, len(gold_rows)))
    packet = []
    answers = []
    for row in chosen:
        packet.append({"id": row["id"], "prompt": row["gloss"] if include_gloss else row["surface"]})
        answers.append({"id": row["id"], "surface": row["surface"], "canonical": row["canonical"], "gloss": row["gloss"]})
    packet_path = Path(output_path)
    answer_path = packet_path.with_name(packet_path.stem + "_answer_key.jsonl")
    write_jsonl(str(packet_path), packet)
    write_jsonl(str(answer_path), answers)
    return {"packet_path": str(packet_path), "answer_key_path": str(answer_path), "n_items": len(packet)}

def make_blank_predictions(packet_path: str, output_path: str) -> Dict[str, Any]:
    packet = load_jsonl(packet_path)
    rows = [{"id": r["id"], "prediction": ""} for r in packet]
    write_jsonl(output_path, rows)
    return {"predictions_template_path": output_path, "n_items": len(rows)}

def score_run(gold_path: str, predictions_path: str, report_path: str) -> Dict[str, Any]:
    report = score_predictions_file(gold_path, predictions_path)
    with open(report_path, "w", encoding="utf-8") as f:
        json.dump(report, f, ensure_ascii=False, indent=2)
    return {"report_path": report_path, "average_score": report["average_score"], "n_scored": report["n_scored"]}
