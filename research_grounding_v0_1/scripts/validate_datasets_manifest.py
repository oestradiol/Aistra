from __future__ import annotations
import sys
sys.dont_write_bytecode = True
import json, sys
from pathlib import Path

ROOT = Path(sys.argv[sys.argv.index("--root")+1]) if "--root" in sys.argv else Path(".")
manifest = json.loads((ROOT/"research_grounding_v0_1"/"datasets_manifest_v0_1.json").read_text(encoding="utf-8"))
issues = []
for ds in manifest.get("datasets", []):
    if ds["access"] == "restricted_academic" and ds.get("required_for") == "route1_scientific_grounding_prehuman":
        issues.append({"dataset":ds["dataset_id"],"kind":"restricted_cannot_be_required"})
status = "PASS" if not issues else "FAIL"
print(json.dumps({"status":status,"issues":issues}, ensure_ascii=False, indent=2))
sys.exit(0 if status=="PASS" else 1)
