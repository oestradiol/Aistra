# Route-control memo v0.1

Purpose:
- decide whether an encoded state belongs to Route 1, Route 2, or should be deferred
- block silent route mixing
- keep bounded-route discipline intact before human testing

Routes:
- route1_intero_affective
- route2_visual_microstructures
- defer_mixed_or_out_of_scope

Decision rule:
1. Use explicit modality/prefix first.
2. If absent, use bounded anchor heuristics.
3. If still unclear, defer.
4. If a state combines primary burdens from both routes, defer rather than force-fit.

Why this matters:
- Route 1 and Route 2 share the scaffold, not the content.
- Silent mixing would corrupt evaluation, scoring, and future human tests.
- A later mixed-route control layer can be added explicitly if needed.
