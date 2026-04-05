from __future__ import annotations
import sys
sys.dont_write_bytecode = True
import json
import hashlib
from pathlib import Path

BASE = Path(__file__).resolve().parents[3]
OUT = BASE / "governance/AUTHORITATIVE_INTEGRITY_MANIFEST_v0_1.json"
SELF_NAME = "governance/AUTHORITATIVE_INTEGRITY_MANIFEST_v0_1.json"

sys.path.insert(0, str(BASE))
from authoritative_guard import expected_integrity_paths  # noqa


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def main() -> None:
    tracked = expected_integrity_paths()
    files = {}
    for rel in tracked:
        path = BASE / rel
        if not path.exists():
            raise SystemExit(f"Missing tracked file: {rel}")
        files[rel] = {"sha256": sha256_file(path), "bytes": path.stat().st_size}
    payload = {
        "manifest_version": "0.3.0",
        "generated_from": [
            "governance/AUTHORITATIVE_SOURCES_v0_2.json",
            "governance/CURRENT_SURFACES_REGISTRY_v0_1.json",
        ],
        "tracked_file_count": len(files),
        "untracked_self": SELF_NAME,
        "files": files,
    }
    OUT.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"out": str(OUT), "tracked_file_count": len(files), "untracked_self": SELF_NAME}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
