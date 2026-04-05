from __future__ import annotations
import sys
sys.dont_write_bytecode = True
import json
import subprocess
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parent

def main():
    doctor = subprocess.run([sys.executable, str(BASE / "package_doctor.py")], capture_output=True, text=True)
    print(doctor.stdout)
    if doctor.returncode != 0:
        print("LAUNCH GATE: FAIL")
        print("Do not run the Route 1 pilot until package_doctor.py passes.")
        sys.exit(1)
    cfg = json.loads((BASE / "governance/AUTHORITATIVE_SOURCES_v0_2.json").read_text(encoding="utf-8"))
    required = [BASE / rel for rel in cfg["route1_current"]["ops"]]
    missing = [str(p.name) for p in required if not p.exists()]
    if missing:
        print("LAUNCH GATE: FAIL")
        print("Missing current Route 1 artifacts:", ", ".join(missing))
        sys.exit(1)
    print("LAUNCH GATE: PASS")
    print("Route 1 current pilot package is present. package_doctor.py passed, required current Route 1 artifacts exist, and current claim audits plus grounding-surface consistency checks passed through package_doctor.py.")
    print("This launch gate demonstrates bounded package coherence and current operational readiness for the shipped Route 1 workflow. It does not by itself validate research claims, psychometric adequacy, or broad human generalization.")
    sys.exit(0)

if __name__ == "__main__":
    main()
