from __future__ import annotations
import sys
sys.dont_write_bytecode = True
import json, sys
from pathlib import Path

ROOT = Path(sys.argv[sys.argv.index("--root")+1]) if "--root" in sys.argv else Path(".")
RG = ROOT / "research_grounding_v0_1"
required = [
    "field_registry_route1_v0_1.json",
    "field_registry_route2_v0_1.json",
    "route1_field_evidence_v0_1.jsonl",
    "route2_field_evidence_v0_1.jsonl",
]
missing = [r for r in required if not (RG / r).exists()]
if missing:
    print(json.dumps({"status":"FAIL","missing":missing}, indent=2))
    sys.exit(1)

def rows(path):
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]

r1_registry = json.loads((RG/"field_registry_route1_v0_1.json").read_text(encoding="utf-8"))
r2_registry = json.loads((RG/"field_registry_route2_v0_1.json").read_text(encoding="utf-8"))
r1_rows = rows(RG/"route1_field_evidence_v0_1.jsonl")
r2_rows = rows(RG/"route2_field_evidence_v0_1.jsonl")

required_cols = {"field_id","name","research_domains","primary_support","review_or_standard_support","expected_reliability","known_confusions","prehuman_validation_tests","recommended_weight_prior","operational_risks"}

issues = []
for label, reg, ev in [("route1", r1_registry["fields"], r1_rows), ("route2", r2_registry["fields"], r2_rows)]:
    reg_ids = {f["field_id"] for f in reg}
    ev_ids = {r["field_id"] for r in ev}
    if reg_ids != ev_ids:
        issues.append({"route":label,"kind":"registry_evidence_mismatch","registry_only":sorted(reg_ids-ev_ids),"evidence_only":sorted(ev_ids-reg_ids)})
    for row in ev:
        missing_cols = sorted(required_cols - set(row.keys()))
        if missing_cols:
            issues.append({"route":label,"kind":"missing_columns","field_id":row.get("field_id"),"missing":missing_cols})
        for col in required_cols:
            if not str(row.get(col,"")).strip():
                issues.append({"route":label,"kind":"empty_value","field_id":row.get("field_id"),"column":col})

status = "PASS" if not issues else "FAIL"
print(json.dumps({"status":status,"issues":issues}, ensure_ascii=False, indent=2))
sys.exit(0 if status=="PASS" else 1)
