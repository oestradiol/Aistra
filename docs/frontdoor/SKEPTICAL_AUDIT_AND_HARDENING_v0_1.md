# Skeptical audit and hardening v0.1

## Purpose
This document plays the internal critic. It lists the strongest remaining package weaknesses, states whether they are fixed in v0.5, and points to the control surface that now addresses them.

## Weakness map

### 1. Front-door clutter could cause stale-file drift
Risk:
- multiple old guides and reports at top level make it too easy to open the wrong file first.

Fix in v0.5:
- historical handoff guides and old reports were moved to `deprecated/handoff_history_v0_1/`.
- `../START_HERE_v0_7.md` is now the canonical front door.
- `README.md`, `CURRENT_OPERATOR_START_HERE_v0_1.md`, and `HANDOFF_GUIDE_v0_1.md` were updated to point to the same minimal path.

### 2. App config duplication could silently drift
Risk:
- `packet_config.json` and `packet_config.js` can diverge.

Fix in v0.5:
- `tools/generate_route1_packet_config.py` now generates both from the authoritative packet and key.
- the config now carries `packet_sha256`, `answer_key_sha256`, and `config_sha256`.
- `package_doctor.py` now fails if the JSON and JS configs diverge.

### 3. Alternate-aware scoring was named but not actually enforced end-to-end
Risk:
- the answer key format allowed alternates, but both the browser app and local scorer only scored the primary canonical.

Fix in v0.5:
- browser scoring now evaluates the primary canonical plus any acceptable alternates.
- local scorer now does the same.
- regression tests now cover alternate-aware scoring behavior.

### 4. Human-testing status was stale in package-level docs
Risk:
- several package-level docs still said Route 1 had not been human-tested.

Fix in v0.5:
- package state docs now say Route 1 has undergone an initial single-participant pilot and remains pilot-ready rather than validated.

### 5. Baseline prompts could be mistaken for naturalistic evaluation
Risk:
- scored calibration prompts can be overread as a claim about natural language phenomenology.

Fix in v0.5:
- front-door docs now state clearly that the main packet is explicit calibration mode.
- naturalistic baseline remains a future separate packet.

### 6. Top-level version references were stale or inconsistent
Risk:
- README and start docs still named older handoff versions.

Fix in v0.5:
- top-level front-door docs now point to v0.5 materials.
- historical versions remain archived for traceability.

### 7. Hidden quality-of-life risk: exported runs did not prove which packet/key generated them
Risk:
- a returned results file could be hard to tie to a specific packet state.

Fix in v0.5:
- app exports now include packet, answer-key, and config digests.
- human-readable reports include those digests too.

## Remaining real weaknesses after v0.5
These are not packaging bugs; they are project-level limits.

- external validity across naive users remains unknown.
- the ontology may still need revision after broader pilot data.
- source and certainty remain the most interpretation-sensitive fields.
- Route 2 is still pre-human.
- scientific usefulness is still provisional, not psychometrically established.

## Conclusion
v0.5 addresses the strongest package-integrity and operator-drift weaknesses that could be fixed without collecting new human data.
