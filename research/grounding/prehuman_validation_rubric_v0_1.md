# Pre-human validation rubric v0.1

## Status labels
- design_only
- scientifically_grounded_prehuman
- pilot_ready_operational
- pilot_running
- pilot_review

## Scientifically grounded prehuman
A route qualifies only if all are true:
- field registry exists
- evidence table exists and covers every field
- route scientific grounding memo exists
- datasets manifest exists
- weight priors memo exists
- prehuman validation report exists
- no missing required columns in evidence tables
- no missing field-to-evidence mappings
- enforcement layer recognizes these artifacts

## Important
`scientifically_grounded_prehuman` is not the same as human-validated.
It means:
- theory-grounded
- research-grounded
- internally checked
- ready for empirical pilot work

## Failure conditions
Do not assign `scientifically_grounded_prehuman` if:
- any field lacks grounding
- evidence rows are partial
- weight memo is out of sync
- route fields changed without evidence update
- prehuman validation summary is missing
