# Package enforcement layer v0.3

This package uses four enforcement layers:

1. **Authoritative source config**
   - `../../governance/AUTHORITATIVE_SOURCES_v0_2.json`
   - machine-readable source of truth for current authoritative files

2. **Current-file integrity ledger**
   - `../../governance/AUTHORITATIVE_INTEGRITY_MANIFEST_v0_1.json`
   - byte-level drift detection for authoritative files

3. **Doctor and launch gate**
   - `package_doctor.py`
   - `route1_launch_gate.py`

4. **Strict current Route 1 wrapper**
   - `tools/run_route1_current_ops.py`

## Boundary rule
The package separates:
- canonical source files
- examples
- generated verification outputs
- deprecated traceability files
- audit history

Only the canonical source files are authoritative.
4. Repo-wide existence control:
   - `../../governance/REPOSITORY_FILE_REGISTRY_v0_1.json`
   - `../../tools/audit_repository_file_registry.py`


## Added semantic-currentness pressure

The package now runs `tools/audit_current_claims.py` to check that key current files still carry the bounded project posture and current release identity, and `tools/audit_repository_minimality.py` to keep historical and generated zones under explicit size pressure.
