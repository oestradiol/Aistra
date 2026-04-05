from __future__ import annotations
import sys
sys.dont_write_bytecode = True
import json
from dataclasses import dataclass, asdict
from typing import Dict, List, Optional, Any

CANONICAL_ORDER = ["mod", "val", "viv", "bri", "loc", "col", "tex", "con", "stb", "cer"]

CANONICAL_VALUES = {
    "mod": {"V", "VI", "VM"},
    "val": {"NEG", "NEU", "POS", "MIX", "_"},
    "viv": {"L", "M", "H"},
    "bri": {"1", "2", "3"},
    "loc": {"CTR", "PER", "ALL", "DST", "DF"},
    "col": {"RED", "BLU", "GRN", "YLW", "WHT", "BLK", "MIXC", "NONE", "_"},
    "tex": {"SHARP", "DIFF", "GRAIN", "HAZE", "EDGE", "SMEAR", "CLEAR", "RAWV", "Ø"},
    "con": {"STAT", "PULSE", "FLICK", "WAVE", "EXP", "CONTR", "OSC"},
    "stb": {"LOW", "MED", "HIGH"},
    "cer": {"LOW", "MED", "HIGH"},
}

SURFACE_TO_CANONICAL = {
    "mod": {"va": "V", "vai": "VI", "vam": "VM"},
    "val": {"neg": "NEG", "neu": "NEU", "pos": "POS", "mix": "MIX", "_": "_"},
    "viv": {"lii": "L", "mii": "M", "hii": "H"},
    "bri": {"un": "1", "du": "2", "tri": "3"},
    "loc": {"cen": "CTR", "per": "PER", "allo": "ALL", "dist": "DST", "difa": "DF"},
    "col": {"rel": "RED", "blu": "BLU", "gre": "GRN", "yel": "YLW", "wha": "WHT", "blk": "BLK", "mixc": "MIXC", "nonc": "NONE", "_": "_"},
    "tex": {"sha": "SHARP", "dif": "DIFF", "gra": "GRAIN", "haz": "HAZE", "edg": "EDGE", "smr": "SMEAR", "clr": "CLEAR", "rav": "RAWV", "ø": "Ø"},
    "con": {"sta": "STAT", "pul": "PULSE", "fli": "FLICK", "wav": "WAVE", "exp": "EXP", "con": "CONTR", "osc": "OSC"},
    "stb": {"low": "LOW", "meda": "MED", "kei": "HIGH"},
    "cer": {"loq": "LOW", "meq": "MED", "hiq": "HIGH"},
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
        if slot == "bri":
            _raise("illegal_operator_use", "Approximate brightness not supported in v1 syntax.", slot, raw)
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
        "mod": {"V":"visual","VI":"visual-imaginal","VM":"visual-memory trace"},
        "val": {"NEG":"negative","NEU":"neutral","POS":"positive","MIX":"mixed-valence","_":"unknown valence"},
        "viv": {"L":"low-vividness","M":"medium-vividness","H":"high-vividness"},
        "bri": {"1":"dim","2":"medium-bright","3":"bright"},
        "loc": {"CTR":"central","PER":"peripheral","ALL":"field-wide","DST":"distant","DF":"diffuse"},
        "col": {"RED":"red","BLU":"blue","GRN":"green","YLW":"yellow","WHT":"white","BLK":"black","MIXC":"mixed-color","NONE":"colorless","_":"unknown-color"},
        "tex": {"SHARP":"sharp","DIFF":"diffuse","GRAIN":"grainy","HAZE":"hazy","EDGE":"edged","SMEAR":"smeared","CLEAR":"clear","RAWV":"raw-visual","Ø":"uncoded remainder"},
        "con": {"STAT":"static","PULSE":"pulsing","FLICK":"flickering","WAVE":"wave-like","EXP":"expanding","CONTR":"contracting","OSC":"oscillating"},
        "stb": {"LOW":"low stability","MED":"medium stability","HIGH":"high stability"},
        "cer": {"LOW":"low certainty","MED":"medium certainty","HIGH":"high certainty"},
    }
    if isinstance(obj["loc"], list):
        loc = " or ".join(d["loc"][x] for x in obj["loc"])
        loc = "uncertain " + loc
    else:
        loc = d["loc"][obj["loc"]]
    if "loc" in flags.approx:
        loc = "approximately " + loc
    tex = "-".join(d["tex"][x] for x in obj["tex"])
    return f'{d["val"][obj["val"]]}, {d["viv"][obj["viv"]]}, {d["bri"][obj["bri"]]} {loc} {d["col"][obj["col"]]} {tex} {d["con"][obj["con"]]} {d["mod"][obj["mod"]]} state; {d["stb"][obj["stb"]]}; {d["cer"][obj["cer"]]}.'

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
    examples = [
        "va neu hii du cen rel sha pul meda hiq",
        "V.NEU.M.2.~CTR.BLU.SHARP.STAT.MED.HIGH",
        "va neu hii du cen rel pul pul meda hiq",
    ]
    for ex in examples:
        print(json.dumps(parse(ex).__dict__, ensure_ascii=False, indent=2))
