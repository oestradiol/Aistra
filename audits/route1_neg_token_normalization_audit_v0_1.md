# Route 1 NEG token normalization audit v0.1

## Scope
Package-wide normalization of Route 1 negative valence token from `ner` to `neg`.

## Why
`ner` was not self-evident for human operators and created immediate decoding friction. The active parser, validation fixtures, examples, pilot materials, and adversarial assets encoded `ner` as canonical surface form.

## Changes applied
- Replaced package-wide surface token `ner` with `neg` in active Route 1 assets.
- Updated correction pairs so `neg` is canonical rather than invalid.
- Updated parser lexicon mapping from `neg -> NEG`.
- Regenerated `../governance/AUTHORITATIVE_INTEGRITY_MANIFEST_v0_1.json`.

## Verification
- `package_doctor.py`: PASS 111/111
- `route1_launch_gate.py`: PASS
- `core/route1/parser.py`: PASS on built-in smoke tests after normalization

## Result
Canonical negative valence surface token for Route 1 is now `neg`.
