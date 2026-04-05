from __future__ import annotations
import json
from dataclasses import dataclass, asdict
from typing import Dict, List, Optional, Any

CANONICAL_ORDER = ["mod", "val", "aro", "int", "loc", "tex", "con", "cer", "src", "act"]

CANONICAL_VALUES = {
    "mod": {"I", "A", "IA"},
    "val": {"NEG", "NEU", "POS", "MIX", "_"},
    "aro": {"L", "M", "H"},
    "int": {"1", "2", "3"},
    "loc": {"CH", "TH", "AB", "HD", "SK", "WH", "DF"},
    "tex": {"TIGHT", "WARM", "SHARP", "HEAVY", "HOLLOW", "BUZZ", "PRESS", "OPEN", "CALM", "RAW", "Ø"},
    "con": {"STAT", "RISE", "FALL", "PULSE", "WAVE", "OSC"},
    "cer": {"LOW", "MED", "HIGH"},
    "src": {"SELF", "REACT", "MEM", "UNC"},
    "act": {"APP", "AVO", "FRZ", "RST", "DIS", "NON"},
}

SURFACE_TO_CANONICAL = {
    "mod": {"si": "I", "sa": "A", "sai": "IA"},
    "val": {"neg": "NEG", "neu": "NEU", "pos": "POS", "mix": "MIX", "_": "_"},
    "aro": {"lo": "L", "ma": "M", "ha": "H"},
    "int": {"un": "1", "du": "2", "tri": "3"},
    "loc": {"chet": "CH", "thal": "TH", "abdo": "AB", "heda": "HD", "skan": "SK", "woba": "WH", "difa": "DF"},
    "tex": {"tak": "TIGHT", "war": "WARM", "sha": "SHARP", "grav": "HEAVY", "hol": "HOLLOW", "buz": "BUZZ", "pres": "PRESS", "opa": "OPEN", "cal": "CALM", "rawa": "RAW", "ø": "Ø"},
    "con": {"stan": "STAT", "ras": "RISE", "fal": "FALL", "pul": "PULSE", "wav": "WAVE", "osc": "OSC"},
    "cer": {"li": "LOW", "meda": "MED", "kei": "HIGH"},
    "src": {"sel": "SELF", "ren": "REACT", "mem": "MEM", "unu": "UNC"},
    "act": {"apo": "APP", "avo": "AVO", "faz": "FRZ", "res": "RST", "dis": "DIS", "non": "NON"},
}

@dataclass
class ParseFlags:
    approx: List[str]
    uncertain: List[str]
    remainder: bool
    unknown: List[str]

@dataclass
class ParseResult:
    valid: bool
    canonical: Optional[str] = None
    object: Optional[Dict[str, Any]] = None
    gloss: Optional[str] = None
    error_type: Optional[str] = None
    slot: Optional[str] = None
    token: Optional[str] = None
    message: Optional[str] = None

def _error(error_type: str, message: str, slot: Optional[str] = None, token: Optional[str] = None) -> ParseResult:
    return ParseResult(valid=False, error_type=error_type, slot=slot, token=token, message=message)

def _raise(error_type: str, message: str, slot: Optional[str] = None, token: Optional[str] = None):
    raise ValueError(json.dumps({"error_type": error_type, "message": message, "slot": slot, "token": token}))

def _resolve_token(slot: str, token: str, mode: str) -> str:
    token = token.strip()
    if mode == "canonical":
        if token not in CANONICAL_VALUES[slot]:
            for fam, vals in CANONICAL_VALUES.items():
                if fam != slot and token in vals:
                    _raise("slot_family_mismatch", f"{token} belongs to {fam}, not {slot}.", slot, token)
            _raise("invalid_token", f"{token} not in allowed {slot} set.", slot, token)
        return token
    mapping = SURFACE_TO_CANONICAL[slot]
    if token not in mapping:
        for fam, fammap in SURFACE_TO_CANONICAL.items():
            if fam != slot and token in fammap:
                _raise("slot_family_mismatch", f"{token} is {fam} token, not {slot} token.", slot, token)
        _raise("invalid_token", f"Token not in allowed {slot} lexicon", slot, token)
    return mapping[token]

def _parse_field(slot: str, raw: str, mode: str, flags: ParseFlags):
    if raw == "_":
        flags.unknown.append(slot)
        return "_"

    if raw.startswith("~"):
        if slot == "int":
            _raise("illegal_operator_use", "Approximate intensity not supported in v1 syntax.", slot, raw)
        raw = raw[1:]
        flags.approx.append(slot)

    uncertain = False
    if raw.startswith("(") and raw.endswith(")") and "?" in raw:
        uncertain = True
        raw = raw[1:-1]
    elif "?" in raw:
        uncertain = True

    if slot == "tex":
        if "?" in raw and ("+" in raw or "-" in raw):
            _raise("illegal_operator_use", "Mixed ? and + operator structure not allowed in v1 texture field.", slot, raw)
        atoms = raw.split("+") if mode == "canonical" else raw.split("-")
        if len(atoms) > 2:
            _raise("too_many_textures", "v1 allows at most 2 texture atoms.", slot, raw)
        out = []
        for atom in atoms:
            val = _resolve_token(slot, atom, mode)
            if val == "Ø":
                flags.remainder = True
            out.append(val)
        return out

    if uncertain:
        atoms = raw.split("?")
        vals = [_resolve_token(slot, atom, mode) for atom in atoms]
        flags.uncertain.append(slot)
        return vals

    return _resolve_token(slot, raw, mode)

def _canonicalize(obj: Dict[str, Any], flags: ParseFlags) -> str:
    parts = []
    for slot in CANONICAL_ORDER:
        val = obj[slot]
        prefix = "~" if slot in flags.approx else ""
        if slot == "tex":
            raw = "+".join(val)
        elif slot in flags.uncertain:
            raw = "(" + "?".join(val) + ")"
        else:
            raw = val
        parts.append(prefix + raw)
    return ".".join(parts)

def _gloss(obj: Dict[str, Any], flags: ParseFlags) -> str:
    d = {
        "mod": {"I":"Interoceptive","A":"Affective","IA":"Mixed interoceptive-affective"},
        "val": {"NEG":"negative","NEU":"neutral","POS":"positive","MIX":"mixed-valence","_":"unknown valence"},
        "aro": {"L":"low-arousal","M":"medium-arousal","H":"high-arousal"},
        "int": {"1":"low-intensity","2":"medium-intensity","3":"high-intensity"},
        "loc": {"CH":"chest","TH":"throat","AB":"abdomen","HD":"head","SK":"skin-surface","WH":"whole-body","DF":"diffuse"},
        "con": {"STAT":"static","RISE":"rising","FALL":"fading","PULSE":"pulsing","WAVE":"wave-like","OSC":"oscillating"},
        "cer": {"LOW":"low certainty","MED":"medium certainty","HIGH":"high certainty"},
        "src": {"SELF":"self-generated","REACT":"reactive source","MEM":"memory-triggered","UNC":"unclear source"},
        "act": {"APP":"approach tendency","AVO":"avoid tendency","FRZ":"freeze tendency","RST":"rest tendency","DIS":"discharge tendency","NON":"no clear action tendency"},
        "tex": {"TIGHT":"tight","WARM":"warm","SHARP":"sharp","HEAVY":"heavy","HOLLOW":"hollow","BUZZ":"buzz","PRESS":"pressure","OPEN":"open","CALM":"calm","RAW":"raw","Ø":"uncoded remainder"},
    }
    if isinstance(obj["loc"], list):
        loc = " or ".join(d["loc"][x] for x in obj["loc"])
        loc = "uncertain " + loc
    else:
        loc = d["loc"][obj["loc"]]
    if "loc" in flags.approx:
        loc = "approximately " + loc
    tex = "-".join(d["tex"][x] for x in obj["tex"])
    return f'{d["mod"][obj["mod"]]}, {d["val"][obj["val"]]}, {d["aro"][obj["aro"]]}, {d["int"][obj["int"]]} {loc} {tex} {d["con"][obj["con"]]} state; {d["cer"][obj["cer"]]}; {d["src"][obj["src"]]}; {d["act"][obj["act"]]}.'

def parse_canonical(text: str) -> ParseResult:
    slots = text.strip().split(".")
    if len(slots) != 10:
        return _error("wrong_slot_count", f"Expected 10 slots, got {len(slots)}.")
    if slots[0] not in CANONICAL_VALUES["mod"]:
        return _error("field_order_violation", "Slot 1 must be modality.")
    flags = ParseFlags(approx=[], uncertain=[], remainder=False, unknown=[])
    obj = {}
    try:
        for slot_name, raw in zip(CANONICAL_ORDER, slots):
            obj[slot_name] = _parse_field(slot_name, raw, "canonical", flags)
    except ValueError as e:
        info = json.loads(str(e))
        return _error(info["error_type"], info["message"], info.get("slot"), info.get("token"))
    canonical = _canonicalize(obj, flags)
    return ParseResult(valid=True, canonical=canonical, object={**obj, "flags": asdict(flags)}, gloss=_gloss(obj, flags))

def parse_surface(text: str) -> ParseResult:
    slots = text.strip().split()
    if len(slots) != 10:
        return _error("wrong_slot_count", f"Expected 10 slots, got {len(slots)}.")
    flags = ParseFlags(approx=[], uncertain=[], remainder=False, unknown=[])
    obj = {}
    try:
        for slot_name, raw in zip(CANONICAL_ORDER, slots):
            obj[slot_name] = _parse_field(slot_name, raw, "surface", flags)
    except ValueError as e:
        info = json.loads(str(e))
        return _error(info["error_type"], info["message"], info.get("slot"), info.get("token"))
    canonical = _canonicalize(obj, flags)
    return ParseResult(valid=True, canonical=canonical, object={**obj, "flags": asdict(flags)}, gloss=_gloss(obj, flags))

def parse(text: str) -> ParseResult:
    if "." in text and " " not in text.strip():
        return parse_canonical(text)
    return parse_surface(text)

if __name__ == "__main__":
    for ex in [
        "sai neg ha du chet tak-sha ras kei ren faz",
        "IA.POS.L.2.~AB.WARM.FALL.HIGH.REACT.RST",
        "sai neg ma du chet wav ras kei ren faz",
    ]:
        print(json.dumps(asdict(parse(ex)), ensure_ascii=False, indent=2))
