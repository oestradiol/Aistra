from __future__ import annotations
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
    print("Route 1 current pilot package is present, verified, and research grounding is in passing state.")
    sys.exit(0)

if __name__ == "__main__":
    main()
