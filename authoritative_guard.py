from __future__ import annotations
import sys
sys.dont_write_bytecode = True
import json
import hashlib
from pathlib import Path
from typing import Dict, List

BASE = Path(__file__).resolve().parent
CONFIG_PATH = BASE / "governance/AUTHORITATIVE_SOURCES_v0_2.json"
INTEGRITY_MANIFEST_PATH = BASE / "governance/AUTHORITATIVE_INTEGRITY_MANIFEST_v0_1.json"

class AuthorityError(RuntimeError):
    pass

def load_authoritative_sources() -> Dict:
    return json.loads(CONFIG_PATH.read_text(encoding="utf-8"))

def current_route1_ops() -> List[str]:
    return list(load_authoritative_sources()["route1_current"]["ops"])

def current_route1_formal() -> List[str]:
    return list(load_authoritative_sources()["route1_current"]["formal"])

def _find_by_name(prefix: str, suffix: str, bucket: str) -> str:
    for rel in load_authoritative_sources()["route1_current"][bucket]:
        name = Path(rel).name
        if name.startswith(prefix) and name.endswith(suffix):
            return rel
    raise AuthorityError(f"No current Route 1 artifact matching {prefix}*{suffix} declared.")

def current_route1_answer_key() -> str:
    return _find_by_name("pilot_answer_key_", ".jsonl", "ops")

def current_route1_response_template() -> str:
    return _find_by_name("pilot_response_template_", ".json", "ops")

def current_route1_packet() -> str:
    return _find_by_name("pilot_packet_route1_", ".jsonl", "ops")

def resolve_rel(path_like: str | Path) -> str:
    p = Path(path_like)
    if p.is_absolute():
        try:
            return str(p.resolve().relative_to(BASE.resolve())).replace('\\','/')
        except ValueError:
            return str(p.resolve())
    return str(p).replace('\\','/')

def assert_current_route1_artifact(path_like: str | Path, *, allowed: List[str], label: str) -> str:
    rel = resolve_rel(path_like)
    if rel not in allowed:
        raise AuthorityError(
            f"Non-current {label}: {rel}. Use one of: {', '.join(allowed)}. "
            f"Resolve current artifacts via governance/AUTHORITATIVE_INDEX_v0_1.md or docs/frontdoor/CURRENT_OPERATOR_START_HERE.md."
        )
    return rel

def load_integrity_manifest() -> Dict:
    return json.loads(INTEGRITY_MANIFEST_PATH.read_text(encoding="utf-8"))

def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()

def verify_integrity(*, strict: bool = True) -> Dict:
    manifest = load_integrity_manifest()
    results = []
    mismatches = []
    missing = []
    for rel, meta in manifest.get("files", {}).items():
        p = BASE / rel
        if not p.exists():
            missing.append(rel)
            results.append({"path": rel, "ok": False, "reason": "missing"})
            continue
        digest = sha256_file(p)
        ok = digest == meta["sha256"]
        results.append({"path": rel, "ok": ok, "sha256": digest})
        if not ok:
            mismatches.append({"path": rel, "expected": meta["sha256"], "observed": digest})
    payload = {
        "manifest_version": manifest.get("manifest_version"),
        "verified_files": len(results),
        "missing": missing,
        "mismatches": mismatches,
        "status": "PASS" if not missing and not mismatches else "FAIL",
        "results": results,
    }
    if strict and payload["status"] != "PASS":
        raise AuthorityError(
            "Integrity verification failed. Missing: " + ", ".join(missing or ["none"]) + "; mismatches: " + ", ".join(m["path"] for m in mismatches or [])
        )
    return payload
