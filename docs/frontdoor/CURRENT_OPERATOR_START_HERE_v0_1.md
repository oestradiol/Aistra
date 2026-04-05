Use `PROJECT_PURPOSE_AND_USE_CASES_v0_1.md` for project point/usefulness and `COHERENCE_AND_CONTROL_SURFACE_v0_1.md` for the shortest control map before operator launch work.

# Current operator start here v0.6

Read in this order:
1. `../../START_HERE_v0_7.md`
2. `../state/PROJECT_STATUS_v0_1.md`
3. `../state/CURRENT_EXECUTION_ORDER_v0_1.md`
4. `HUMAN_PILOT_PACK_GUIDE_v0_5.md`
5. `../../governance/AUTHORITATIVE_INDEX_v0_1.md`
6. `../../governance/AUTHORITATIVE_SOURCES_v0_2.json`
7. `SKEPTICAL_AUDIT_AND_HARDENING_v0_1.md`
8. `../ops/operator_checklist_route1_pilot_v0_1_1.md` if you are operating Route 1
9. `../../research_grounding_v0_1/reference_bibliography_v0_1.md` if you are auditing scientific grounding

Fast truth:
- Route 1 has completed an initial single-participant pilot and remains pilot-ready, not validated.
- Route 1 current human-facing materials are the v0.5 human pilot guide, local app, and alternate-aware v0.4 answer key.
- Route 2 remains pre-human.
- `package_doctor.py` and `route1_launch_gate.py` resolve current required files from `../../governance/AUTHORITATIVE_SOURCES_v0_2.json`.
- The root is intentionally minimized; historical materials live under `../../deprecated/`.

Strict execution rule:
- Do not score Route 1 by calling lower-level scripts with ad hoc gold paths.
- Run Route 1 through `python tools/run_route1_current_ops.py --responses <filled_response.json> --run-dir <outdir>` so the current launch gate and authoritative answer key are enforced.

Integrity ledger:
- `../../governance/AUTHORITATIVE_INTEGRITY_MANIFEST_v0_1.json` records current authoritative file digests.
- Verify it with `python research_grounding_v0_1/scripts/verify_integrity_manifest.py --strict`.

Current guide path: `docs/frontdoor/HUMAN_PILOT_PACK_GUIDE_v0_5.md`
