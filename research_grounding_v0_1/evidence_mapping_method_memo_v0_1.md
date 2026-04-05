# Evidence mapping method memo v0.1

## Purpose
This layer makes the package scientifically grounded before human pilots by forcing every route field and weighting choice to map to prior research traditions, measurement concepts, and explicit pre-human validation tests.

This does not claim human usability has already been validated.
It claims:
- design choices are not arbitrary
- constructs are tied to established literatures
- expected confusions are documented
- pre-human validation artifacts exist and are checkable

## Required units of grounding
Each field requires:
1. field id
2. operational definition
3. construct mapping
4. supporting primary source(s)
5. supporting review/standard source(s)
6. expected reliability
7. expected confusions
8. pre-human validation tests
9. recommended weight prior
10. known operational risks

## Grounding rule
A route cannot claim `scientifically_grounded_prehuman` unless:
- every current field appears in the field registry
- every field has a complete evidence row
- route memo exists
- datasets manifest exists
- weight priors memo exists
- prehuman validation rubric exists
- prehuman validation summary exists

## Boundary
This layer supports:
- theory alignment
- research alignment
- pre-human defensibility

It does not support:
- claims of human learnability
- claims of superior performance vs plain language
- finalized empirical validation
