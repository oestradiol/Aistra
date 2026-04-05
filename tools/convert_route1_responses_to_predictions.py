from __future__ import annotations
import json
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(BASE))
from authoritative_guard import current_route1_response_template, AuthorityError  # noqa

FIELD_ORDER = ["mod", "val", "aro", "int", "loc", "tex", "con", "cer", "src", "act"]

def response_row_to_prediction(row):
    fields = row.get("response_fields", {})
    tex = fields.get("tex", [])
    if isinstance(tex, str):
        tex = [t for t in tex.split("+") if t]
    canonical = ".".join([
        "STATE",
        fields.get("val", ""),
        fields.get("aro", ""),
        fields.get("int", ""),
        fields.get("loc", ""),
        "+".join(tex),
        fields.get("con", ""),
        fields.get("cer", ""),
        fields.get("src", ""),
        fields.get("act", ""),
    ])
    return {"id": row["trial_id"], "prediction": canonical}

def main():
    if len(sys.argv) != 3:
        raise SystemExit("Usage: python tools/convert_route1_responses_to_predictions.py <response.json> <out.jsonl>")
    in_path = Path(sys.argv[1])
    out_path = Path(sys.argv[2])
    rows = json.loads(in_path.read_text(encoding="utf-8"))
    current_template = current_route1_response_template()
    for row in rows:
        declared = row.get("_response_template")
        if declared is not None and declared != current_template:
            raise AuthorityError(f"Non-current response template declared: {declared}; expected {current_template}")
    preds = [response_row_to_prediction(r) for r in rows]
    out_path.write_text("\n".join(json.dumps(p, ensure_ascii=False) for p in preds) + "\n", encoding="utf-8")

if __name__ == "__main__":
    main()
