from __future__ import annotations
import sys
sys.dont_write_bytecode = True
import json
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SUBPROCESS_ENV = {**__import__("os").environ, "PYTHONDONTWRITEBYTECODE": "1"}


def assert_true(cond, msg):
    if not cond:
        raise AssertionError(msg)


def test_packet_contains_woba():
    packet = ROOT / 'core/route1/pilot_packet_route1_v0_3_final.jsonl'
    text = packet.read_text(encoding='utf-8')
    assert_true('woba' in text, 'expected woba token in packet')
    assert_true(' holo ' not in text, 'legacy holo token should not remain in packet stimuli')


def test_parser_accepts_woba():
    sys.path.insert(0, str(ROOT / 'core/route1'))
    import parser as route1_parser
    pred = route1_parser.parse_canonical('IA.POS.M.1.WH.CALM.STAT.HIGH.SELF.RST')
    assert_true(pred.valid and pred.object['loc'] == 'WH', 'canonical parse sanity failed')


def test_packet_config_sync():
    cfg_json = json.loads((ROOT / 'human_pilot_app_v0_1' / 'packet_config.json').read_text(encoding='utf-8'))
    js_text = (ROOT / 'human_pilot_app_v0_1' / 'packet_config.js').read_text(encoding='utf-8').strip()
    prefix = 'window.PACKET_CONFIG = '
    assert_true(js_text.startswith(prefix) and js_text.endswith(';'), 'packet_config.js wrapper invalid')
    cfg_js = json.loads(js_text[len(prefix):-1])
    assert_true(cfg_json == cfg_js, 'packet_config json/js mismatch')
    assert_true(bool(cfg_json.get('packet_sha256')) and bool(cfg_json.get('answer_key_sha256')) and bool(cfg_json.get('config_sha256')), 'missing config digests')


def test_export_scorer_generates_outputs():
    cfg = ROOT / 'human_pilot_app_v0_1' / 'packet_config.json'
    sample = {
        'package_name': 'test',
        'app_version': 'test_app',
        'scorer_version': 'test_scorer',
        'exported_at': '2026-04-05T00:00:00Z',
        'responses': [
            {
                'id': 'S2',
                'condition': 'structured',
                'stimulus': 'sai pos ma un woba cal stan kei sel res',
                'response': {
                    'valence': 'positive',
                    'arousal': 'medium',
                    'intensity': '1',
                    'location': 'whole body',
                    'texture1': 'calm',
                    'texture2': '',
                    'contour': 'static',
                    'certainty': 'high',
                    'source': 'self',
                    'action': 'rest',
                    'comments': '',
                },
                'prediction_canonical': 'IA.POS.M.1.WH.CALM.STAT.HIGH.SELF.RST',
            }
        ],
    }
    with tempfile.TemporaryDirectory() as td:
        sample_path = Path(td) / 'sample.json'
        sample_path.write_text(json.dumps(sample), encoding='utf-8')
        subprocess.run([sys.executable, str(ROOT / 'tools' / 'score_route1_human_pilot_export.py'), str(sample_path), str(cfg)], check=True, env=SUBPROCESS_ENV)
        scored = sample_path.with_suffix('.scored.json')
        report = sample_path.with_suffix('.report.md')
        assert_true(scored.exists(), 'scored json not created')
        assert_true(report.exists(), 'report md not created')
        scored_obj = json.loads(scored.read_text(encoding='utf-8'))
        assert_true(scored_obj['summary']['exact_matches'] == 1, 'expected exact match in scorer test')


def test_alternate_aware_scoring_prefers_best_match():
    cfg = {
        'answer_key': {
            'X1': {
                'expected_canonical': 'IA.NEG.H.3.CH.SHARP.RISE.HIGH.REACT.FRZ',
                'acceptable_alternates': ['IA.NEG.H.2.CH.TIGHT+SHARP.RISE.HIGH.REACT.FRZ'],
            }
        }
    }
    sample = {
        'package_name': 'test',
        'exported_at': '2026-04-05T00:00:00Z',
        'responses': [
            {
                'id': 'X1',
                'condition': 'baseline',
                'stimulus': 'synthetic',
                'response': {
                    'valence': 'negative',
                    'arousal': 'high',
                    'intensity': '2',
                    'location': 'chest',
                    'texture1': 'tight',
                    'texture2': 'sharp',
                    'contour': 'rising',
                    'certainty': 'high',
                    'source': 'reactive',
                    'action': 'freeze',
                    'comments': '',
                },
                'prediction_canonical': 'IA.NEG.H.2.CH.TIGHT+SHARP.RISE.HIGH.REACT.FRZ',
            }
        ],
    }
    with tempfile.TemporaryDirectory() as td:
        cfg_path = Path(td) / 'cfg.json'
        sample_path = Path(td) / 'sample.json'
        cfg_path.write_text(json.dumps(cfg), encoding='utf-8')
        sample_path.write_text(json.dumps(sample), encoding='utf-8')
        subprocess.run([sys.executable, str(ROOT / 'tools' / 'score_route1_human_pilot_export.py'), str(sample_path), str(cfg_path)], check=True, env=SUBPROCESS_ENV)
        scored = json.loads(sample_path.with_suffix('.scored.json').read_text(encoding='utf-8'))
        row = scored['responses'][0]
        assert_true(row['scoring']['matched_policy'] == 'alternate', 'expected alternate to win')
        assert_true(row['scoring']['best_match']['exact_match'] is True, 'expected exact match against alternate')




def test_repository_file_registry_audit_passes():
    subprocess.run([sys.executable, str(ROOT / 'tools' / 'audit_repository_file_registry.py')], check=True, env=SUBPROCESS_ENV)

def test_current_surfaces_audit_passes():
    subprocess.run([sys.executable, str(ROOT / 'tools' / 'audit_current_surfaces.py')], check=True, env=SUBPROCESS_ENV)


def test_frontdoor_uses_clean_names():
    readme = (ROOT / 'README.md').read_text(encoding='utf-8')
    assert_true('START_HERE.md' in readme, 'expected clean START_HERE.md reference')
    assert_true('START_HERE_v0_7.md' not in readme, 'stale start path leaked into README')

def main():
    test_packet_contains_woba()
    test_parser_accepts_woba()
    test_packet_config_sync()
    test_export_scorer_generates_outputs()
    test_alternate_aware_scoring_prefers_best_match()
    test_repository_file_registry_audit_passes()
    test_current_surfaces_audit_passes()
    test_frontdoor_uses_clean_names()
    print('route1 regression tests passed')


if __name__ == '__main__':
    main()
