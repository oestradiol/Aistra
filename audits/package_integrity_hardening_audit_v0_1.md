# Package integrity hardening audit

## Purpose
This memo records the integrity-hardening decisions preserved in the cleaned handoff build.

## Hardening outcomes preserved here
- The package has an authoritative file ledger in `../governance/AUTHORITATIVE_INTEGRITY_MANIFEST_v0_1.json`.
- Strict verification is available through `research_grounding_v0_1/scripts/verify_integrity_manifest.py --strict`.
- The operator path is narrowed through `../governance/AUTHORITATIVE_SOURCES_v0_2.json`, `../governance/AUTHORITATIVE_INDEX_v0_1.md`, and `tools/run_route1_current_ops.py`.
- Non-canonical material is separated into `deprecated/`, `examples/`, `verification_outputs/`, and `audits/`.
- `package_doctor.py` now clears transient Python bytecode artifacts before evaluating package cleanliness so routine execution does not create false failures.

## Residual boundary
Integrity verification establishes file identity and package consistency. It does not establish scientific truth, human readiness beyond the documented state, or immunity to operator misuse outside the enforced path.

## Current status
Retained as historical hardening evidence. Not the primary operator document.
