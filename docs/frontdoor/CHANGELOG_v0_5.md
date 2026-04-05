# Changelog v0.5

## Added
- `../START_HERE_v0_7.md`
- `SKEPTICAL_AUDIT_AND_HARDENING_v0_1.md`
- `HUMAN_PILOT_PACK_GUIDE_v0_5.md`
- `THREAD_LOSSLESS_COMPRESSION_v0_3.md`
- `tools/generate_route1_packet_config.py`

## Changed
- cleaned the top-level front door and archived older handoff/history docs under `deprecated/handoff_history_v0_1/`
- updated README and package-level handoff docs to current status
- packet config now includes source digests and is generated reproducibly
- browser app scoring now supports acceptable alternates and exports provenance digests
- local scorer now supports acceptable alternates and writes richer report metadata
- package doctor now checks packet-config sync and front-door entrypoint presence
- regression tests expanded to cover alternate-aware scoring and config sync

## Not changed
- Route 1 structured packet semantics
- Route 1 baseline-explicit packet semantics
- Route 2 status


## v0.6

Front-door and status-surface hardening inspired by review of `oestradiol/Research` public repo organization:
- added `../state/PROJECT_STATUS_v0_1.md` as the canonical current-state surface
- added `../state/CURRENT_EXECUTION_ORDER_v0_1.md` as the shortest live next-step surface
- updated `README.md`, `../START_HERE_v0_7.md`, and `CURRENT_OPERATOR_START_HERE_v0_1.md` to use an explicit status-surface rule

No Route 1 ontology, packet, scoring, app behavior, or verification semantics changed in v0.6.


## v0.7

- added explicit package minimization policy
- added root allowlist and file justification registry
- added root budget audit tool and wired it into regression tests
- updated front-door docs to state the file-budget rule
- removed transient `__pycache__` from handoff package

## v0.8
- performed a deep file-tree refactor to collapse root-folder clutter
- moved operational docs under `docs/ops/`, state docs under `docs/state/`, front-door docs under `docs/frontdoor/`, Route 1 formal assets under `core/route1/`, and shared route-control files under `core/common/`
- rewired validators, launch gate, scorer, config generator, integrity manifest generation, and regression tests to the new tree
- reduced root to five justified files and made the root-budget audit pass under the new structure
- preserved Route 1 task semantics while changing package layout


## v0.9 addendum

- added front-door purpose/use-case surface
- added single-file coherence and control surface
- added project naming decision (`Aistra`) without mass path rename
- added anti-slop trust/style policy for front-door language
- updated README and START_HERE sequencing to surface purpose, controls, and trust policy earlier
