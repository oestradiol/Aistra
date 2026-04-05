from __future__ import annotations
import sys
sys.dont_write_bytecode = True
import json, random, sys
from pathlib import Path

out_dir = Path(sys.argv[sys.argv.index("--out-dir")+1]) if "--out-dir" in sys.argv else Path("data/synthetic_visual")
n = int(sys.argv[sys.argv.index("--n")+1]) if "--n" in sys.argv else 120
out_dir.mkdir(parents=True, exist_ok=True)
rng = random.Random(42)

colors = ["RED","BLU","GRN","YLW","WHT","BLK","MIXC","NONE"]
textures = ["SHARP","DIFF","GRAIN","HAZE","EDGE","SMEAR","CLEAR","RAWV"]
contours = ["STAT","PULSE","FLICK","WAVE","EXP","CONTR","OSC"]
locs = ["CTR","PER","ALL","DST","DF"]
rows = []
for i in range(n):
    rows.append({
        "id": f"SYN{i+1:03d}",
        "col": rng.choice(colors),
        "tex": rng.choice(textures),
        "con": rng.choice(contours),
        "loc": rng.choice(locs),
        "bri": rng.choice(["1","2","3"]),
        "viv": rng.choice(["L","M","H"]),
        "stb": rng.choice(["LOW","MED","HIGH"]),
    })
(out_dir/"route2_synthetic_gold_v0_1.jsonl").write_text("\n".join(json.dumps(r) for r in rows)+"\n", encoding="utf-8")
print(json.dumps({"status":"PASS","generated":len(rows),"path":str(out_dir/'route2_synthetic_gold_v0_1.jsonl')}, indent=2))
