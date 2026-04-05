# CORRECTION CYCLE PROTOCOL v0.1

## Purpose
This protocol defines how to prevent drift, catch mistakes, and update the package safely.

## Core rule
Do not silently patch meaning-bearing artifacts.

If a correction affects:
- route status
- packet choice
- pilot protocol
- scoring interpretation
- authoritative file choice

then also update:
- `../../governance/AUTHORITATIVE_INDEX_v0_1.md`
- `research/cross_route_spec/manifest.json`
- `../../governance/PACKAGE_STATE_SUMMARY_v0_1.json`
- a correction note or pass note

## Correction cycle
1. detect issue
2. classify issue type
3. patch affected file
4. update authoritative docs
5. record what changed
6. rerun relevant validation if code/data changed
7. do not claim finality if uncertainty remains

## Issue types
- reference drift
- route contamination
- ontology mismatch
- token mismatch
- parser bug
- scorer inflation/distortion
- protocol contamination
- packet overlap
- documentation conflict
- outdated authoritative state

## Minimum required actions by issue type

### If code changes
Also rerun:
- parser checks
- scorer checks
- adversarial suite if relevant

### If packet/protocol changes
Also update:
- handoff docs
- authoritative index
- final correction note

### If route status changes
Also update:
- manifest
- package state summary
- README
- handoff guide

## Drift-prevention rules
- preserve route separation
- do not promote superseded docs back into use
- prefer latest correction-pass note over older readiness note
- do not force mixed-route states into one route
- if uncertain, defer rather than silently choose

## Handoff rule
A future operator should be able to reconstruct current truth by reading:
1. `README.md`
2. `../frontdoor/HANDOFF_GUIDE.md`
3. `../../governance/AUTHORITATIVE_INDEX_v0_1.md`
4. `../../governance/PACKAGE_STATE_SUMMARY_v0_1.json`

If that is not enough, the package is not handoff-clean yet.

## Current correction status
As of this version:
- the package has undergone multiple correction passes
- the final Route 1 pilot packet is `../../core/route1/pilot_packet_route1_v0_3_final.jsonl`
- Route 1 is `pilot_ready`
- Route 2 remains `pre_human`
