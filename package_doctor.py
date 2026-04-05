from __future__ import annotations
import sys
sys.dont_write_bytecode = True
import json
import shutil
from pathlib import Path
import importlib.util
from authoritative_guard import verify_integrity, AuthorityError

BASE = Path(__file__).resolve().parent
CURRENT_ANSWER_KEY = "core/route1/pilot_answer_key_route1_v0_4_alternate_aware.jsonl"
CURRENT_TEMPLATE = "core/route1/pilot_response_template_route1_v0_2_anchored.json"
CURRENT_PACKET = "core/route1/pilot_packet_route1_v0_3_final.jsonl"
CURRENT_START = "START_HERE.md"
CURRENT_HUMAN_GUIDE = "docs/frontdoor/HUMAN_PILOT_PACK_GUIDE.md"
CURRENT_HANDOFF = "docs/frontdoor/HANDOFF_GUIDE.md"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    assert spec.loader is not None
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
    return read_json("apps/human_pilot/packet_config.json")


def read_packet_config_js_payload():
    text = read_text("apps/human_pilot/packet_config.js").strip()
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

    for rel in ["docs/history/DEVELOPMENT_HISTORY.md", "research/examples/README.md", "archive/reports/generated/README.md", "archive/deprecated/README.md"]:
        p = BASE / rel
        record(f"layout:{rel}:exists", p.exists(), "present" if p.exists() else f"missing {rel}")

    removed_dirs, removed_files = cleanup_transient_bytecode(BASE)
    remaining_pycaches = list(BASE.rglob("__pycache__"))
    remaining_pyc = list(BASE.rglob("*.pyc"))
    found_transient = len(removed_dirs) > 0 or len(removed_files) > 0
    detail = f"removed_dirs={len(removed_dirs)} removed_pyc={len(removed_files)} remaining_dirs={len(remaining_pycaches)} remaining_pyc={len(remaining_pyc)}"
    record("layout:transient-bytecode-clean", (not found_transient) and len(remaining_pycaches) == 0 and len(remaining_pyc) == 0, detail)

    manifest = read_json("research/cross_route_spec/manifest.json")
    state = read_json("governance/PACKAGE_STATE_SUMMARY_v0_1.json")
    auth_index = read_text("governance/AUTHORITATIVE_INDEX_v0_1.md")
    handoff = read_text(CURRENT_HANDOFF)
    readme = read_text("README.md")

    record("status:manifest-state-match", manifest["package_status"] == state["package_status"], f"manifest={manifest['package_status']} state={state['package_status']}")
    record("status:state-package-name-current", state.get("package_name") == "aistra", f"package_name={state.get('package_name')}")
    record("status:state-version-current", state.get("version") == "1.11.0", f"version={state.get('version')}")
    expected_entrypoints = [
        "README.md",
        "START_HERE.md",
        "docs/frontdoor/CURRENT_OPERATOR_START_HERE.md",
        "docs/frontdoor/HANDOFF_GUIDE.md",
        "docs/frontdoor/SCIENTIFIC_GROUNDING.md",
        "governance/AUTHORITATIVE_INDEX_v0_1.md",
        "governance/AUTHORITATIVE_SOURCES_v0_2.json",
        "governance/CURRENT_SURFACES_REGISTRY_v0_1.json",
        "governance/CURRENT_CLAIM_EXPECTATIONS_v0_1.json",
        "governance/AUTHORITATIVE_INTEGRITY_MANIFEST_v0_1.json",
        "governance/PACKAGE_STATE_SUMMARY_v0_1.json",
        "governance/MINIMALITY_POLICY_v0_1.json",
        "docs/ops/CORRECTION_CYCLE_PROTOCOL_v0_1.md",
        "docs/ops/PACKAGE_ENFORCEMENT_LAYER_v0_1.md",
        "docs/ops/RELEASE_CHECKLIST_v0_1.md",
        "governance/REPOSITORY_FILE_REGISTRY_v0_1.json",
    ]
    record("status:state-entrypoints-current", state.get("current_authoritative_entrypoints") == expected_entrypoints, "entrypoints stale" if state.get("current_authoritative_entrypoints") != expected_entrypoints else "ok")
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
    record("route1-app:package-name-current", cfg_json.get("package_name") == "aistra_route1_human_pilot_pack_v1_11", f"package_name={cfg_json.get('package_name')}")
    record("route1-app:packet-count-sync", len(cfg_json.get("packet", [])) == len(packet) and set(r["id"] for r in cfg_json.get("packet", [])) == set(packet_ids), "app packet mismatch")
    record("route1-app:key-id-sync", set(cfg_json.get("answer_key", {}).keys()) == set(packet_ids), "app answer key mismatch")
    record("route1-app:has-config-digests", all(cfg_json.get(k) for k in ["packet_sha256", "answer_key_sha256", "config_sha256"]), "missing config digests")

    record("handoff:readme-points-to-start", CURRENT_START in readme and CURRENT_HUMAN_GUIDE in readme, "README missing current start path")
    record("handoff:guide-points-to-index", "governance/AUTHORITATIVE_INDEX_v0_1.md" in handoff and CURRENT_START in read_text("docs/frontdoor/CURRENT_OPERATOR_START_HERE.md"), "handoff / operator start mismatch")
    record("authoritative:index-points-current-start", CURRENT_START in auth_index and CURRENT_HUMAN_GUIDE in auth_index, "authoritative index stale")

    current_mod = load_module("audit_current_surfaces_mod", BASE / "tools" / "audit_current_surfaces.py")
    current_report = current_mod.run_audit()
    record("current-surfaces:audit-pass", current_report.get("status") == "PASS", f"failed_checks={current_report.get('failed_checks')}")

    repo_mod = load_module("audit_repository_file_registry_mod", BASE / "tools" / "audit_repository_file_registry.py")
    repo_report = repo_mod.run_audit()
    record("repository-file-registry:audit-pass", repo_report.get("status") == "PASS", f"failed_checks={repo_report.get('failed_checks')}")

    claims_mod = load_module("audit_current_claims_mod", BASE / "tools" / "audit_current_claims.py")
    claims_report = claims_mod.run_audit()
    record("current-claims:audit-pass", claims_report.get("status") == "PASS", f"failed_checks={claims_report.get('failed_checks')}")

    minimality_mod = load_module("audit_repository_minimality_mod", BASE / "tools" / "audit_repository_minimality.py")
    minimality_report = minimality_mod.run_audit()
    record("repository-minimality:audit-pass", minimality_report.get("status") == "PASS", f"failed_checks={minimality_report.get('failed_checks')}")

    adv_mod = load_module("adversarial_suite_mod", BASE / "tests/adversarial_suite" / "run_adversarial_suite.py")
    adv = adv_mod.run()
    record("adversarial-suite:pass", adv.get("n_failed") == 0, f"n_failed={adv.get('n_failed')}")

    status = "PASS" if not issues else "FAIL"
    summary = {
        "doctor_version": "1.3.0",
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
