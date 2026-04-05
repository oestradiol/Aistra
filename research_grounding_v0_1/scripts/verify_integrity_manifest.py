from __future__ import annotations
import json
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(BASE))
from authoritative_guard import verify_integrity, AuthorityError  # noqa

def main() -> None:
    strict = "--strict" in sys.argv
    try:
        payload = verify_integrity(strict=strict)
    except AuthorityError as e:
        print(json.dumps({"status": "FAIL", "error": str(e)}, ensure_ascii=False, indent=2))
        sys.exit(1)
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    sys.exit(0 if payload["status"] == "PASS" else 1)

if __name__ == "__main__":
    main()
