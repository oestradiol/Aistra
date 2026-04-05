# Pilot review template v0.2 (red-teamed)

## Pilot metadata
- date:
- route:
- participant ids:
- block order by participant:
- practice items used:
- scored structured items:
- scored baseline items:
- were any items familiar from a previous packet? yes/no
- were any items explicitly treated as holdout items? yes/no

## Sanity checks
- any repeated underlying targets across conditions for same participant? yes/no
- any practice items leaked into scored block? yes/no
- any participant received corrective feedback during scored trials? yes/no

## Outcome summary
- structured average score:
- baseline average score:
- malformed response rate:
- major failure mode:
- overall recommendation: keep / revise / redesign

## Error source diagnosis
For each participant, estimate which source dominated:
- token lookup difficulty
- ontology mismatch
- field extraction difficulty
- wording ambiguity
- fatigue
- interface-shaping / instruction dependence
- other

## Field confusion summary
For each field:
- exact match rate
- partial match rate
- miss rate
- common substitutions
- did this feel like a real semantic miss or a format miss?
- did the miss look packet-specific, interface-shaped, or ontology-level?

Fields:
- val
- aro
- int
- loc
- tex
- con
- cer
- src
- act

## Condition comparison
- Was structured clearly harder because of token lookup?
- Was baseline clearly easier because wording was too explicit?
- Did one condition produce better qualitative comments even when scores were similar?
- Did familiar items behave differently from holdout items?

## Token usability notes
- which tokens caused recurrent confusion?
- were there legend-dependent lookups?
- did participants stop reasoning and start decoding mechanically?

## Interface and human-factors notes
- where did participants hesitate?
- where did they ask for clarification?
- did examples or layout seem to steer answers?
- did fatigue, overload, or demand characteristics seem to shape responses?

## Ontology adequacy notes
- which distinctions felt natural?
- which felt forced?
- what missing distinctions were reported?
- did any field seem unnecessary in pilot 1?
- did any weird-but-valid state fail because the schema could not represent it cleanly?

## Scoring reality check
- did high-scoring trials actually feel like good reconstructions?
- did low-scoring trials reflect meaningful misses?
- did the current weights distort the apparent outcome?

## Redesign decision
Choose one:
- keep v0.2 as-is
- simplify token system
- simplify ontology
- simplify baseline wording
- reduce field count
- redesign pilot before continuing

## Next action
- one change to make immediately
- one thing to keep unchanged
- one question for the next pilot
