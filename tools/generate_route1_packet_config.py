from __future__ import annotations
import sys
sys.dont_write_bytecode = True
import hashlib
import json
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
PACKET = BASE / 'core/route1/pilot_packet_route1_v0_3_final.jsonl'
ANSWER = BASE / 'core/route1/pilot_answer_key_route1_v0_4_alternate_aware.jsonl'
OUT_JSON = BASE / 'apps/human_pilot' / 'packet_config.json'
OUT_JS = BASE / 'apps/human_pilot' / 'packet_config.js'

FIELDS = {
    'valence': ['negative', 'neutral', 'positive', 'mixed'],
    'arousal': ['low', 'medium', 'high'],
    'intensity': ['1', '2', '3'],
    'location': ['chest', 'throat', 'abdomen', 'head', 'skin', 'whole body', 'diffuse'],
    'texture': ['tight', 'warm', 'sharp', 'heavy', 'hollow', 'buzz', 'pressure', 'open', 'calm', 'raw'],
    'contour': ['static', 'rising', 'falling', 'pulsing', 'wave-like', 'oscillating'],
    'certainty': ['low', 'medium', 'high'],
    'source': ['self', 'reactive', 'memory', 'unclear'],
    'action': ['approach', 'avoid', 'freeze', 'rest', 'discharge', 'none'],
}

def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode('utf-8')).hexdigest()

def load_jsonl(path: Path):
    return [json.loads(line) for line in path.read_text(encoding='utf-8').splitlines() if line.strip()]

def main():
    packet_text = PACKET.read_text(encoding='utf-8')
    answer_text = ANSWER.read_text(encoding='utf-8')
    packet_rows = load_jsonl(PACKET)
    answer_rows = load_jsonl(ANSWER)
    config = {
        'package_name': 'aistra_route1_human_pilot_pack_v1_11',
        'token_change': {
            'whole_body_surface_token_old': 'holo',
            'whole_body_surface_token_new': 'woba',
        },
        'surface_slot_order': ['MOD', 'VAL', 'ARO', 'INT', 'LOC', 'TEX', 'CON', 'CER', 'SRC', 'ACT'],
        'packet_source': 'core/route1/pilot_packet_route1_v0_3_final.jsonl',
        'answer_key_source': 'core/route1/pilot_answer_key_route1_v0_4_alternate_aware.jsonl',
        'packet_sha256': sha256_text(packet_text),
        'answer_key_sha256': sha256_text(answer_text),
        'packet': [{'id': r['id'], 'condition': r['condition'], 'stimulus': r['stimulus']} for r in packet_rows],
        'answer_key': {r['id']: {'expected_canonical': r['expected_canonical'], 'acceptable_alternates': r.get('acceptable_alternates', [])} for r in answer_rows},
        'fields': FIELDS,
        'design_mode': 'baseline_explicit_calibration',
        'scorer_version': 'route1_human_export_scorer_v1_0',
    }
    bare_json = json.dumps(config, ensure_ascii=False, indent=2) + '\n'
    config['config_sha256'] = sha256_text(bare_json)
    final_json = json.dumps(config, ensure_ascii=False, indent=2) + '\n'
    OUT_JSON.write_text(final_json, encoding='utf-8')
    OUT_JS.write_text('window.PACKET_CONFIG = ' + final_json.rstrip() + ';\n', encoding='utf-8')
    print(OUT_JSON)
    print(OUT_JS)

if __name__ == '__main__':
    main()
