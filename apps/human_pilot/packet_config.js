window.PACKET_CONFIG = {
  "package_name": "aistra_route1_human_pilot_pack_v1_11",
  "token_change": {
    "whole_body_surface_token_old": "holo",
    "whole_body_surface_token_new": "woba"
  },
  "surface_slot_order": [
    "MOD",
    "VAL",
    "ARO",
    "INT",
    "LOC",
    "TEX",
    "CON",
    "CER",
    "SRC",
    "ACT"
  ],
  "packet_source": "core/route1/pilot_packet_route1_v0_3_final.jsonl",
  "answer_key_source": "core/route1/pilot_answer_key_route1_v0_4_alternate_aware.jsonl",
  "packet_sha256": "eac35859d952bb0ed45bed50286b9d270cdc73c0942e5110d19fd7d75b303e83",
  "answer_key_sha256": "af2c2994de0fb81ed11206665cc582eed2deadfed8a30d6d0f55c339d3b14176",
  "packet": [
    {
      "id": "PR1",
      "condition": "practice_structured",
      "stimulus": "sai neu ma du chet pres stan meda ren non"
    },
    {
      "id": "PR2",
      "condition": "practice_baseline",
      "stimulus": "A clearly reactive positive state: low arousal, low intensity, warm on the skin, static, high certainty, and gently inviting approach."
    },
    {
      "id": "S1",
      "condition": "structured",
      "stimulus": "sai neu lo du heda grav-pres stan meda unu res"
    },
    {
      "id": "S2",
      "condition": "structured",
      "stimulus": "sai pos ma un woba cal stan kei sel res"
    },
    {
      "id": "S3",
      "condition": "structured",
      "stimulus": "sai neg ha tri abdo tak-pres pul meda mem dis"
    },
    {
      "id": "S4",
      "condition": "structured",
      "stimulus": "sai mix ha du difa hol-rawa osc meda unu faz"
    },
    {
      "id": "B1",
      "condition": "baseline",
      "stimulus": "A clearly reactive negative state in the chest: high arousal, moderate intensity, tight and sharp, rising, high certainty, and pushing toward freeze."
    },
    {
      "id": "B2",
      "condition": "baseline",
      "stimulus": "A clearly reactive positive state in the abdomen: low arousal, moderate intensity, warm and open, falling/easing, high certainty, and settling toward rest."
    },
    {
      "id": "B3",
      "condition": "baseline",
      "stimulus": "A mixed state spread diffusely: low arousal, low intensity, hollow, mostly static, low certainty, unclear source, and no clear action pull."
    },
    {
      "id": "B4",
      "condition": "baseline",
      "stimulus": "A clearly reactive negative whole-body state: high arousal, high intensity, buzz and pressure, oscillating, low certainty, and tending toward discharge."
    }
  ],
  "answer_key": {
    "PR1": {
      "expected_canonical": "IA.NEU.M.2.CH.PRESS.STAT.MED.REACT.NON",
      "acceptable_alternates": []
    },
    "PR2": {
      "expected_canonical": "IA.POS.L.1.SK.WARM.STAT.HIGH.REACT.APP",
      "acceptable_alternates": []
    },
    "S1": {
      "expected_canonical": "IA.NEU.L.2.HD.HEAVY+PRESS.STAT.MED.UNC.RST",
      "acceptable_alternates": []
    },
    "S2": {
      "expected_canonical": "IA.POS.M.1.WH.CALM.STAT.HIGH.SELF.RST",
      "acceptable_alternates": []
    },
    "S3": {
      "expected_canonical": "IA.NEG.H.3.AB.TIGHT+PRESS.PULSE.MED.MEM.DIS",
      "acceptable_alternates": []
    },
    "S4": {
      "expected_canonical": "IA.MIX.H.2.DF.HOLLOW+RAW.OSC.MED.UNC.FRZ",
      "acceptable_alternates": []
    },
    "B1": {
      "expected_canonical": "IA.NEG.H.2.CH.TIGHT+SHARP.RISE.HIGH.REACT.FRZ",
      "acceptable_alternates": []
    },
    "B2": {
      "expected_canonical": "IA.POS.L.2.AB.WARM+OPEN.FALL.HIGH.REACT.RST",
      "acceptable_alternates": []
    },
    "B3": {
      "expected_canonical": "IA.MIX.L.1.DF.HOLLOW.STAT.LOW.UNC.NON",
      "acceptable_alternates": []
    },
    "B4": {
      "expected_canonical": "IA.NEG.H.3.WH.BUZZ+PRESS.OSC.LOW.REACT.DIS",
      "acceptable_alternates": []
    }
  },
  "fields": {
    "valence": [
      "negative",
      "neutral",
      "positive",
      "mixed"
    ],
    "arousal": [
      "low",
      "medium",
      "high"
    ],
    "intensity": [
      "1",
      "2",
      "3"
    ],
    "location": [
      "chest",
      "throat",
      "abdomen",
      "head",
      "skin",
      "whole body",
      "diffuse"
    ],
    "texture": [
      "tight",
      "warm",
      "sharp",
      "heavy",
      "hollow",
      "buzz",
      "pressure",
      "open",
      "calm",
      "raw"
    ],
    "contour": [
      "static",
      "rising",
      "falling",
      "pulsing",
      "wave-like",
      "oscillating"
    ],
    "certainty": [
      "low",
      "medium",
      "high"
    ],
    "source": [
      "self",
      "reactive",
      "memory",
      "unclear"
    ],
    "action": [
      "approach",
      "avoid",
      "freeze",
      "rest",
      "discharge",
      "none"
    ]
  },
  "design_mode": "baseline_explicit_calibration",
  "scorer_version": "route1_human_export_scorer_v1_0",
  "config_sha256": "8a989722b2fbf99e289f19e4a1d0045976cb66c8e9b9e51c62a2d5e0cf2ce292"
};
