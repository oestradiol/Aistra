from __future__ import annotations
import json, subprocess, sys
from pathlib import Path

ROOT = Path(sys.argv[sys.argv.index("--package-root")+1]) if "--package-root" in sys.argv else Path(".")
RG = ROOT / "research_grounding_v0_1"
scripts = RG / "scripts"

runs = []
for script, args in [
    ("validate_evidence_tables.py", ["--root", str(ROOT)]),
    ("validate_datasets_manifest.py", ["--root", str(ROOT)]),
]:
    proc = subprocess.run([sys.executable, str(scripts/script), *args], capture_output=True, text=True)
    runs.append({"script":script,"returncode":proc.returncode,"stdout":proc.stdout})

summary = {
    "version":"0.1.0",
    "status":"PASS" if all(r["returncode"]==0 for r in runs) else "FAIL",
    "runs": runs,
}
(RG/"prehuman_validation_summary_v0_1.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
print(json.dumps(summary, ensure_ascii=False, indent=2))
sys.exit(0 if summary["status"]=="PASS" else 1)
