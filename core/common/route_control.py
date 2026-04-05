from __future__ import annotations
import json
from typing import Dict, Any, List, Optional

# Route identities
ROUTE_1 = "route1_intero_affective"
ROUTE_2 = "route2_visual_microstructures"
DEFER = "defer_mixed_or_out_of_scope"

# Canonical prefix cues
ROUTE_PREFIXES = {
    ROUTE_1: {"I", "A", "IA"},
    ROUTE_2: {"V", "VI", "VM"},
}

# Surface token cues
ROUTE1_SURFACE_MODS = {"si", "sa", "sai"}
ROUTE2_SURFACE_MODS = {"va", "vai", "vam"}

# Heuristic vocab anchors by route
ROUTE1_ANCHORS = {
    "loc": {"chet", "thal", "abdo", "heda", "skan", "woba", "difa"},
    "tex": {"tak", "war", "sha", "grav", "hol", "buz", "pres", "opa", "cal", "rawa"},
}
ROUTE2_ANCHORS = {
    "loc": {"cen", "per", "allo", "dist", "difa"},
    "col": {"rel", "blu", "gre", "yel", "wha", "blk", "mixc", "nonc"},
    "tex": {"sha", "dif", "gra", "haz", "edg", "smr", "clr", "rav"},
}

def detect_mode(text: str) -> str:
    text = text.strip()
    if "." in text and " " not in text:
        return "canonical"
    return "surface"

def classify_text(text: str) -> Dict[str, Any]:
    text = text.strip()
    mode = detect_mode(text)

    if mode == "canonical":
        slots = text.split(".")
        if not slots:
            return {"route": DEFER, "confidence": 0.0, "reason": "empty"}
        prefix = slots[0]
        if prefix in ROUTE_PREFIXES[ROUTE_1]:
            return {"route": ROUTE_1, "confidence": 1.0, "reason": "canonical_prefix"}
        if prefix in ROUTE_PREFIXES[ROUTE_2]:
            return {"route": ROUTE_2, "confidence": 1.0, "reason": "canonical_prefix"}
        return {"route": DEFER, "confidence": 0.0, "reason": "unknown_canonical_prefix"}

    tokens = text.split()
    if not tokens:
        return {"route": DEFER, "confidence": 0.0, "reason": "empty"}

    first = tokens[0]
    if first in ROUTE1_SURFACE_MODS:
        return {"route": ROUTE_1, "confidence": 1.0, "reason": "surface_modality_token"}
    if first in ROUTE2_SURFACE_MODS:
        return {"route": ROUTE_2, "confidence": 1.0, "reason": "surface_modality_token"}

    # fallback heuristic from anchors
    r1_hits = 0
    r2_hits = 0
    for tok in tokens:
        if tok in ROUTE1_ANCHORS["loc"] or tok in ROUTE1_ANCHORS["tex"]:
            r1_hits += 1
        if tok in ROUTE2_ANCHORS["loc"] or tok in ROUTE2_ANCHORS["col"] or tok in ROUTE2_ANCHORS["tex"]:
            r2_hits += 1

    if r1_hits > r2_hits and r1_hits > 0:
        conf = min(0.8, 0.4 + 0.1 * r1_hits)
        return {"route": ROUTE_1, "confidence": round(conf, 2), "reason": "surface_anchor_heuristic", "r1_hits": r1_hits, "r2_hits": r2_hits}
    if r2_hits > r1_hits and r2_hits > 0:
        conf = min(0.8, 0.4 + 0.1 * r2_hits)
        return {"route": ROUTE_2, "confidence": round(conf, 2), "reason": "surface_anchor_heuristic", "r1_hits": r1_hits, "r2_hits": r2_hits}

    return {"route": DEFER, "confidence": 0.0, "reason": "insufficient_route_signal", "r1_hits": r1_hits, "r2_hits": r2_hits}

def detect_mixed_route_features(features: Dict[str, Any]) -> Dict[str, Any]:
    """Simple route-control check on high-level semantic features, for future structured pipelines."""
    has_body = any(k in features for k in ["action_tendency", "source", "arousal", "valence", "bodily_locus"])
    has_visual = any(k in features for k in ["color", "brightness", "vividness", "visual_locus", "stability"])
    if has_body and has_visual:
        return {"mixed": True, "decision": DEFER, "reason": "cross_route_semantic_mix"}
    if has_body:
        return {"mixed": False, "decision": ROUTE_1, "reason": "body_affect_semantic_profile"}
    if has_visual:
        return {"mixed": False, "decision": ROUTE_2, "reason": "visual_semantic_profile"}
    return {"mixed": False, "decision": DEFER, "reason": "insufficient_semantic_profile"}

def validate_route_assignment(text: str, claimed_route: str) -> Dict[str, Any]:
    detected = classify_text(text)
    if detected["route"] == DEFER:
        return {
            "ok": False,
            "claimed_route": claimed_route,
            "detected_route": detected["route"],
            "reason": detected["reason"],
            "message": "State should be deferred rather than forced into a route."
        }
    if detected["route"] != claimed_route:
        return {
            "ok": False,
            "claimed_route": claimed_route,
            "detected_route": detected["route"],
            "reason": detected["reason"],
            "message": "Route mismatch: encoded form appears to belong to a different route."
        }
    return {
        "ok": True,
        "claimed_route": claimed_route,
        "detected_route": detected["route"],
        "reason": detected["reason"],
        "message": "Route assignment accepted."
    }

def explain_route_policy() -> Dict[str, Any]:
    return {
        "routes": {
            ROUTE_1: "Interoceptive-affective microstates; bodily-affective primary burden.",
            ROUTE_2: "Visual phenomenological microstructures; visual primary burden.",
            DEFER: "Mixed-route, underspecified, or out-of-scope states."
        },
        "control_rules": [
            "Do not force mixed bodily-affective and visual states into one route.",
            "Use modality/prefix first; use anchor heuristics only as fallback.",
            "If route signal is weak, defer.",
            "If a future state genuinely needs both routes, create an explicit mixed-route control layer rather than silently merging."
        ]
    }

if __name__ == "__main__":
    examples = [
        "sai neg ha du chet tak-sha ras kei ren faz",
        "va neu hii du cen rel sha pul meda hiq",
        "unknown token stream",
        "IA.NEG.H.2.CH.TIGHT+SHARP.RISE.HIGH.REACT.FRZ",
        "V.NEU.H.2.CTR.RED.SHARP.PULSE.MED.HIGH",
    ]
    for ex in examples:
        print(json.dumps({"input": ex, "classification": classify_text(ex)}, ensure_ascii=False, indent=2))
