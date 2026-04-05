# Current operator start here v1.10

Read these before operating the live Route 1 package:
1. `../../START_HERE.md`
2. `../state/PROJECT_STATUS.md`
3. `../state/CURRENT_EXECUTION_ORDER.md`
4. `SCIENTIFIC_GROUNDING.md`
5. `HUMAN_PILOT_PACK_GUIDE.md`
6. `../../governance/AUTHORITATIVE_INDEX_v0_1.md`
7. `../../governance/AUTHORITATIVE_SOURCES_v0_2.json`
8. `../../governance/CURRENT_SURFACES_REGISTRY_v0_1.json`
9. `SKEPTICAL_AUDIT_AND_HARDENING.md`
10. `../ops/operator_checklist_route1_pilot_v0_1_1.md` if you are operating Route 1

Fast truth:
- Route 1 has completed one initial single-participant pilot and remains pilot-ready, not validated.
- Route 2 remains pre-human.
- `package_doctor.py` and `route1_launch_gate.py` are the minimum checks before live use.
- The package has a research-grounding layer, but broader human validation is still future work.

Strict execution rule:
- Do not score Route 1 with ad hoc paths.
- Use `python tools/run_route1_current_ops.py --responses <filled_response.json> --run-dir <outdir>` so the current launch gate and answer key are enforced.
