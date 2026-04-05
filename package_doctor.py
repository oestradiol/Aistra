from __future__ import annotations
import json
import shutil
import sys
from pathlib import Path
import importlib.util
from authoritative_guard import verify_integrity, AuthorityError

BASE = Path(__file__).resolve().parent

SUPERSEDED_DOCS = [
    "deprecated/route1_superseded/pilot_protocol_memo_v0_1.md",
    "deprecated/route1_superseded/baseline_protocol_memo_v0_1.md",
    "deprecated/route1_superseded/pilot_review_template_v0_1.md",
    "deprecated/route1_superseded/pilot_packet_route1_v0_1.jsonl",
    "deprecated/route1_superseded/pilot_packet_route1_v0_2_redteamed.jsonl",
    "deprecated/route1_superseded/pilot_ready_status_note_v0_1.md",
    "deprecated/route1_superseded/pilot_readiness_memo_v0_1.md",
]

CURRENT_ANSWER_KEY = "core/route1/pilot_answer_key_route1_v0_4_alternate_aware.jsonl"
CURRENT_TEMPLATE = "core/route1/pilot_response_template_route1_v0_2_anchored.json"
CURRENT_PACKET = "core/route1/pilot_packet_route1_v0_3_final.jsonl"
CURRENT_START = "START_HERE_v0_7.md"
CURRENT_HUMAN_GUIDE = "docs/frontdoor/HUMAN_PILOT_PACK_GUIDE_v0_5.md"

def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod

def read_text(rel: str) -> str:
    return (BASE / rel).read_text(encoding="utf-8")

def read_json(rel: str):
    return json.loads(read_text(rel))

def jsonl_rows(rel: str):
    rows = []
    for line in read_text(rel).splitlines():
        line = line.strip()
        if line:
            rows.append(json.loads(line))
    return rows


def read_packet_config_json():
    return read_json("human_pilot_app_v0_1/packet_config.json")

def read_packet_config_js_payload():
    text = read_text("human_pilot_app_v0_1/packet_config.js").strip()
    prefix = "window.PACKET_CONFIG = "
    if not text.startswith(prefix) or not text.endswith(";"):
        raise ValueError("packet_config.js has unexpected wrapper")
    return json.loads(text[len(prefix):-1])

def load_authoritative_sources():
    cfg = read_json("governance/AUTHORITATIVE_SOURCES_v0_2.json")
    required = list(cfg["package_entrypoints"]) + list(cfg["route1_current"]["formal"]) + list(cfg["route1_current"]["ops"]) + list(cfg["route2_current"]) + list(cfg["research_current"]) + ["governance/AUTHORITATIVE_SOURCES_v0_2.json"]
    return cfg, required

def cleanup_transient_bytecode(base: Path):
    removed_dirs = []
    removed_files = []
    for pycache in sorted(base.rglob("__pycache__")):
        if pycache.is_dir():
            shutil.rmtree(pycache)
            removed_dirs.append(str(pycache.relative_to(base)))
    for pyc in sorted(base.rglob("*.pyc")):
        if pyc.is_file():
            pyc.unlink()
            removed_files.append(str(pyc.relative_to(base)))
    return removed_dirs, removed_files

def main():
    checks = []
    issues = []
    def record(name: str, ok: bool, detail: str = ""):
        checks.append({"check": name, "ok": ok, "detail": detail})
        if not ok:
            issues.append({"check": name, "detail": detail})

    auth_cfg, required_paths = load_authoritative_sources()
    for rel in required_paths:
        p = BASE / rel
        record(f"exists:{rel}", p.exists(), "present" if p.exists() else f"missing {rel}")

    try:
        integrity = verify_integrity(strict=True)
        record("integrity:manifest-pass", integrity["status"] == "PASS", f"verified_files={integrity['verified_files']}")
    except AuthorityError as e:
        record("integrity:manifest-pass", False, str(e))

    for rel in ["audits/AUDIT_INDEX.md", "examples/README.md", "verification_outputs/README.md", "deprecated/README.md"]:
        p = BASE / rel
        record(f"layout:{rel}:exists", p.exists(), "present" if p.exists() else f"missing {rel}")
    removed_dirs, removed_files = cleanup_transient_bytecode(BASE)
    remaining_pycaches = list(BASE.rglob("__pycache__"))
    remaining_pyc = list(BASE.rglob("*.pyc"))
    detail = f"removed_dirs={len(removed_dirs)} removed_pyc={len(removed_files)} remaining_dirs={len(remaining_pycaches)} remaining_pyc={len(remaining_pyc)}"
    record("layout:transient-bytecode-clean", len(remaining_pycaches) == 0 and len(remaining_pyc) == 0, detail)

    manifest = read_json("cross_route_spec_v0_1/manifest.json")
    state = read_json("governance/PACKAGE_STATE_SUMMARY_v0_1.json")
    auth_index = read_text("governance/AUTHORITATIVE_INDEX_v0_1.md")
    handoff = read_text("docs/frontdoor/HANDOFF_GUIDE_v0_1.md")
    readme = read_text("README.md")

    record("status:manifest-state-match", manifest["package_status"] == state["package_status"], f"manifest={manifest['package_status']} state={state['package_status']}")
    record("status:route1-pilot-ready", state["routes"]["route1_intero_affective"]["status"] == "pilot_ready", state["routes"]["route1_intero_affective"]["status"])
    record("status:route2-pre-human", state["routes"]["route2_visual_microstructures"]["status"] == "pre_human", state["routes"]["route2_visual_microstructures"]["status"])
    record("status:answer-key-sync", manifest["routes"][0]["authoritative_answer_key"] == state["routes"]["route1_intero_affective"]["authoritative_answer_key"] == CURRENT_ANSWER_KEY, f"manifest={manifest['routes'][0]['authoritative_answer_key']} state={state['routes']['route1_intero_affective']['authoritative_answer_key']}")

    packet = jsonl_rows(CURRENT_PACKET)
    answer = jsonl_rows(CURRENT_ANSWER_KEY)
    template = read_json(CURRENT_TEMPLATE)
    record("route1-packet:item-count", len(packet) == 10, f"count={len(packet)}")
    packet_ids = [r["id"] for r in packet]
    record("route1-packet:unique-ids", len(packet_ids) == len(set(packet_ids)), "duplicate ids" if len(packet_ids) != len(set(packet_ids)) else "ok")
    canonicals = [r["expected_canonical"] for r in packet]
    record("route1-packet:unique-canonicals", len(canonicals) == len(set(canonicals)), "overlap found" if len(canonicals) != len(set(canonicals)) else "ok")
    record("route1-answer-key:id-match", {r["id"] for r in answer} == set(packet_ids), "answer key mismatch" if {r["id"] for r in answer} != set(packet_ids) else "ok")
    record("route1-template:id-match", {r["trial_id"] for r in template} == set(packet_ids), "response template mismatch" if {r["trial_id"] for r in template} != set(packet_ids) else "ok")
    cfg_json = read_packet_config_json()
    cfg_js = read_packet_config_js_payload()
    record("route1-app:packet-config-sync", cfg_json == cfg_js, "packet_config.json and packet_config.js diverge" if cfg_json != cfg_js else "ok")
    record("route1-app:packet-source-sync", cfg_json.get("packet_source") == CURRENT_PACKET and cfg_json.get("answer_key_source") == CURRENT_ANSWER_KEY, f"packet_source={cfg_json.get('packet_source')} answer_key_source={cfg_json.get('answer_key_source')}")
    record("route1-app:packet-count-sync", len(cfg_json.get("packet", [])) == len(packet) and set(r["id"] for r in cfg_json.get("packet", [])) == set(packet_ids), "app packet mismatch")
    record("route1-app:key-id-sync", set(cfg_json.get("answer_key", {}).keys()) == set(packet_ids), "app answer key mismatch")
    record("route1-app:has-config-digests", all(cfg_json.get(k) for k in ["packet_sha256", "answer_key_sha256", "config_sha256"]), "missing config digests")

    for rel in SUPERSEDED_DOCS:
        p = BASE / rel
        if not p.exists():
            record(f"superseded:{rel}:exists", False, "missing superseded doc")
            continue
        if p.suffix == ".jsonl":
            sidecar = p.parent / f"{p.name}.WARNING.txt"
            ok = sidecar.exists()
            detail = "sidecar warning present" if ok else "missing superseded sidecar warning"
            if ok:
                content = sidecar.read_text(encoding="utf-8", errors="ignore")
                ok = ("SUPERSEDED" in content) and ("governance/AUTHORITATIVE_INDEX_v0_1.md" in content)
                detail = "sidecar warning valid" if ok else "sidecar warning missing required pointer"
            record(f"superseded:{rel}:warning", ok, detail)
        else:
            content = p.read_text(encoding="utf-8", errors="ignore")
            record(f"superseded:{rel}:warning", ("SUPERSEDED" in content) and ("governance/AUTHORITATIVE_INDEX_v0_1.md" in content), "missing superseded header / pointer")

    record("handoff:readme-points-to-start", CURRENT_START in readme and CURRENT_HUMAN_GUIDE in readme, "README missing current start path")
    record("handoff:guide-points-to-index", "governance/AUTHORITATIVE_INDEX_v0_1.md" in handoff and CURRENT_START in read_text("docs/frontdoor/CURRENT_OPERATOR_START_HERE_v0_1.md"), "handoff guide missing authoritative index pointer")
    record("handoff:index-has-superseded-section", "Superseded or traceability-only files" in auth_index, "index missing superseded section")
    record("handoff:uses-current-guide", CURRENT_HUMAN_GUIDE in readme and CURRENT_HUMAN_GUIDE in read_text("docs/frontdoor/CURRENT_OPERATOR_START_HERE_v0_1.md") and CURRENT_HUMAN_GUIDE in read_text(CURRENT_START), "current human guide not wired through front door")
    record("index:uses-current-start", CURRENT_START in auth_index and CURRENT_ANSWER_KEY in auth_index, "index still stale")
    record("handoff:mentions-authoritative-wrapper", "tools/run_route1_current_ops.py" in handoff and "tools/run_route1_current_ops.py" in auth_index and "tools/run_route1_current_ops.py" in read_text("docs/frontdoor/CURRENT_OPERATOR_START_HERE_v0_1.md"), "authoritative wrapper not wired through docs")
    record("handoff:mentions-integrity-ledger", "governance/AUTHORITATIVE_INTEGRITY_MANIFEST_v0_1.json" in handoff and "governance/AUTHORITATIVE_INTEGRITY_MANIFEST_v0_1.json" in auth_index and "governance/AUTHORITATIVE_INTEGRITY_MANIFEST_v0_1.json" in read_text("docs/frontdoor/CURRENT_OPERATOR_START_HERE_v0_1.md"), "integrity ledger not wired through docs")

    for row in template:
        record(f"route1-template:metadata:{row['trial_id']}", row.get("_response_template") == CURRENT_TEMPLATE, row.get("_response_template", "missing _response_template"))

    r1_parser = load_module("doctor_r1_parser", BASE / "core/route1/parser.py")
    r1_valid = jsonl_rows("core/route1/gold_valid.jsonl")
    r1_invalid = jsonl_rows("core/route1/gold_invalid.jsonl")
    r1v = sum(1 for rec in r1_valid if (lambda res: res.valid and res.canonical == rec["canonical"])(r1_parser.parse(rec["surface"])))
    r1i = sum(1 for rec in r1_invalid if (lambda res: (not res.valid) and res.error_type == rec["error_type"])(r1_parser.parse(rec["input"])))
    record("route1-parser:valid", r1v == len(r1_valid), f"{r1v}/{len(r1_valid)}")
    record("route1-parser:invalid", r1i == len(r1_invalid), f"{r1i}/{len(r1_invalid)}")

    r2_parser = load_module("doctor_r2_parser", BASE / "route2_visual_v0_1" / "parser.py")
    r2_valid = jsonl_rows("route2_visual_v0_1/gold_valid.jsonl")
    r2_invalid = jsonl_rows("route2_visual_v0_1/gold_invalid.jsonl")
    r2v = sum(1 for rec in r2_valid if (lambda res: res.valid and res.canonical == rec["canonical"])(r2_parser.parse(rec["surface"])))
    r2i = sum(1 for rec in r2_invalid if (lambda res: (not res.valid) and res.error_type == rec["error_type"])(r2_parser.parse(rec["input"])))
    record("route2-parser:valid", r2v == len(r2_valid), f"{r2v}/{len(r2_valid)}")
    record("route2-parser:invalid", r2i == len(r2_invalid), f"{r2i}/{len(r2_invalid)}")

    prehuman = read_json("research_grounding_v0_1/prehuman_validation_summary_v0_1.json")
    bib = read_json("research_grounding_v0_1/reference_bibliography_v0_1.json")
    record("research-grounding:summary-present", "status" in prehuman, str(prehuman))
    record("research-grounding:summary-pass", prehuman.get("status") == "PASS", f"status={prehuman.get('status')}")
    record("research-grounding:bibliography-nonempty", len(bib.get("references", [])) >= 10, f"n_refs={len(bib.get('references', []))}")

    adv = read_json("verification_outputs/adversarial_suite_v0_1/adversarial_report.json")
    record("adversarial:all-pass", adv["n_failed"] == 0, f"n_failed={adv['n_failed']}")

    status = "PASS" if not issues else "FAIL"
    summary = {
        "doctor_version": "0.8.0",
        "status": status,
        "total_checks": len(checks),
        "passed_checks": sum(1 for c in checks if c["ok"]),
        "failed_checks": sum(1 for c in checks if not c["ok"]),
        "issues": issues,
    }
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    sys.exit(0 if status == "PASS" else 1)

if __name__ == "__main__":
    main()
