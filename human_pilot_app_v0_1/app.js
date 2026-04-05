const state = {
  config: null,
  packet: [],
  index: 0,
  responses: {},
};

const APP_VERSION = 'human_pilot_app_v0_6';
const SCORER_VERSION = 'route1_human_scorer_v0_8';

const el = id => document.getElementById(id);

const LABEL_TO_CANON = {
  valence: {negative: 'NEG', neutral: 'NEU', positive: 'POS', mixed: 'MIX'},
  arousal: {low: 'L', medium: 'M', high: 'H'},
  intensity: {'1': '1', '2': '2', '3': '3'},
  location: {'chest': 'CH', 'throat': 'TH', 'abdomen': 'AB', 'head': 'HD', 'skin': 'SK', 'whole body': 'WH', 'diffuse': 'DF'},
  texture: {tight: 'TIGHT', warm: 'WARM', sharp: 'SHARP', heavy: 'HEAVY', hollow: 'HOLLOW', buzz: 'BUZZ', pressure: 'PRESS', open: 'OPEN', calm: 'CALM', raw: 'RAW'},
  contour: {'static': 'STAT', 'rising': 'RISE', 'falling': 'FALL', 'pulsing': 'PULSE', 'wave-like': 'WAVE', 'oscillating': 'OSC'},
  certainty: {low: 'LOW', medium: 'MED', high: 'HIGH'},
  source: {self: 'SELF', reactive: 'REACT', memory: 'MEM', unclear: 'UNC'},
  action: {approach: 'APP', avoid: 'AVO', freeze: 'FRZ', rest: 'RST', discharge: 'DIS', none: 'NON'},
};

const CANON_TO_LABEL = {
  valence: {NEG: 'negative', NEU: 'neutral', POS: 'positive', MIX: 'mixed'},
  arousal: {L: 'low', M: 'medium', H: 'high'},
  intensity: {'1': '1', '2': '2', '3': '3'},
  location: {CH: 'chest', TH: 'throat', AB: 'abdomen', HD: 'head', SK: 'skin', WH: 'whole body', DF: 'diffuse'},
  texture: {TIGHT: 'tight', WARM: 'warm', SHARP: 'sharp', HEAVY: 'heavy', HOLLOW: 'hollow', BUZZ: 'buzz', PRESS: 'pressure', OPEN: 'open', CALM: 'calm', RAW: 'raw'},
  contour: {STAT: 'static', RISE: 'rising', FALL: 'falling', PULSE: 'pulsing', WAVE: 'wave-like', OSC: 'oscillating'},
  certainty: {LOW: 'low', MED: 'medium', HIGH: 'high'},
  source: {SELF: 'self', REACT: 'reactive', MEM: 'memory', UNC: 'unclear'},
  action: {APP: 'approach', AVO: 'avoid', FRZ: 'freeze', RST: 'rest', DIS: 'discharge', NON: 'none'},
};


function normalizeLabel(field, value) {
  if (!value) return value;
  const v = String(value).trim().toLowerCase();
  if (field === 'source' && v === 'unknown') return 'unclear';
  if (field === 'contour' && v === 'wavy') return 'wave-like';
  return v;
}

function summarizeRows(rows) {
  const fieldNames = ['valence','arousal','intensity','location','texture','contour','certainty','source','action'];
  const completed = rows.filter(r => r.response);
  const byField = Object.fromEntries(fieldNames.map(f => [f, {hits: 0, total: 0}]));
  const byCondition = {};
  for (const row of rows) {
    const cond = row.condition;
    byCondition[cond] ||= {items: 0, completed: 0, exact_matches: 0, exact_field_hits: 0};
    byCondition[cond].items += 1;
    if (!row.response || !row.scoring.best_match) continue;
    byCondition[cond].completed += 1;
    byCondition[cond].exact_field_hits += row.scoring.best_match.exact_9_score;
    if (row.scoring.best_match.exact_match) byCondition[cond].exact_matches += 1;
    for (const field of fieldNames) {
      byField[field].total += 1;
      if (row.scoring.best_match.field_matches[field]) byField[field].hits += 1;
    }
  }
  return {
    items_total: rows.length,
    items_completed: completed.length,
    exact_matches: completed.filter(r => r.scoring.best_match && r.scoring.best_match.exact_match).length,
    total_exact_field_hits: completed.reduce((n, r) => n + ((r.scoring.best_match && r.scoring.best_match.exact_9_score) || 0), 0),
    field_accuracy: Object.fromEntries(fieldNames.map(f => [f, {
      hits: byField[f].hits,
      total: byField[f].total,
      rate: byField[f].total ? Number((byField[f].hits / byField[f].total).toFixed(4)) : null,
    }])),
    condition_breakdown: byCondition,
  };
}

function buildMarkdownReport(payload) {
  const lines = [];
  lines.push(`# Route 1 human pilot report`);
  lines.push('');
  lines.push(`- package: ${payload.package_name}`);
  lines.push(`- app_version: ${payload.app_version}`);
  lines.push(`- scorer_version: ${payload.scorer_version}`);
  lines.push(`- exported_at: ${payload.exported_at}`);
  lines.push(`- packet_source: ${payload.packet_source}`);
  lines.push(`- answer_key_source: ${payload.answer_key_source}`);
  lines.push(`- packet_sha256: ${payload.packet_sha256}`);
  lines.push(`- answer_key_sha256: ${payload.answer_key_sha256}`);
  lines.push(`- config_sha256: ${payload.config_sha256}`);
  lines.push('');
  lines.push('## Summary');
  lines.push(`- items_total: ${payload.summary.items_total}`);
  lines.push(`- items_completed: ${payload.summary.items_completed}`);
  lines.push(`- exact_matches: ${payload.summary.exact_matches}`);
  lines.push(`- total_exact_field_hits: ${payload.summary.total_exact_field_hits}`);
  lines.push('');
  lines.push('## Field accuracy');
  for (const [field, stats] of Object.entries(payload.summary.field_accuracy)) {
    lines.push(`- ${field}: ${stats.hits}/${stats.total} (${stats.rate})`);
  }
  lines.push('');
  lines.push('## Condition breakdown');
  for (const [cond, stats] of Object.entries(payload.summary.condition_breakdown)) {
    lines.push(`- ${cond}: items=${stats.items}, completed=${stats.completed}, exact_matches=${stats.exact_matches}, exact_field_hits=${stats.exact_field_hits}`);
  }
  lines.push('');
  lines.push('## Item results');
  for (const row of payload.responses) {
    const s = row.scoring.best_match;
    lines.push(`### ${row.id} (${row.condition})`);
    lines.push(`- stimulus: ${row.stimulus}`);
    if (!row.response) {
      lines.push(`- status: missing`);
      lines.push('');
      continue;
    }
    lines.push(`- predicted_canonical: ${row.prediction_canonical}`);
    lines.push(`- expected_canonical: ${row.scoring.expected_canonical}`);
    lines.push(`- matched_policy: ${row.scoring.matched_policy}`);
    lines.push(`- matched_canonical: ${s.matched_canonical}`);
    lines.push(`- exact_9_score: ${s.exact_9_score}`);
    lines.push(`- exact_match: ${s.exact_match}`);
    lines.push(`- field_matches: ${JSON.stringify(s.field_matches)}`);
    lines.push('');
  }
  return lines.join('\n');
}

function downloadText(filename, text, type) {
  const blob = new Blob([text], {type});
  const url = URL.createObjectURL(blob);
  const a = document.createElement('a');
  a.href = url;
  a.download = filename;
  document.body.appendChild(a);
  a.click();
  a.remove();
  URL.revokeObjectURL(url);
}

function populateSelect(id, options, allowBlank=false) {
  const select = el(id);
  select.innerHTML = '';
  if (allowBlank) {
    const opt = document.createElement('option');
    opt.value = '';
    opt.textContent = '—';
    select.appendChild(opt);
  }
  options.forEach(value => {
    const opt = document.createElement('option');
    opt.value = value;
    opt.textContent = value;
    select.appendChild(opt);
  });
}

function inferModalityHint(stimulus) {
  const first = stimulus.split(/\s+/)[0];
  if (first === 'si') return 'Modality shown: interoceptive.';
  if (first === 'sa') return 'Modality shown: affective.';
  if (first === 'sai') return 'Modality shown: mixed interoceptive-affective.';
  return 'Baseline prompt: modality is not separately scored.';
}

function currentItem() {
  return state.packet[state.index];
}

function render() {
  const item = currentItem();
  el('itemId').textContent = item.id;
  el('itemCondition').textContent = item.condition;
  el('stimulusText').textContent = item.stimulus;
  el('modalityHint').textContent = inferModalityHint(item.stimulus);
  el('progressPill').textContent = `Item ${state.index + 1} / ${state.packet.length}`;

  const saved = state.responses[item.id] || {};
  for (const field of ['valence','arousal','intensity','location','texture1','texture2','contour','certainty','source','action','comments']) {
    const node = el(field);
    node.value = saved[field] || '';
  }
  refreshSavedPreview();
}

function getFormResponse() {
  return {
    valence: el('valence').value,
    arousal: el('arousal').value,
    intensity: el('intensity').value,
    location: el('location').value,
    texture1: el('texture1').value,
    texture2: el('texture2').value,
    contour: el('contour').value,
    certainty: el('certainty').value,
    source: el('source').value,
    action: el('action').value,
    comments: el('comments').value.trim(),
  };
}

function validateResponse(resp) {
  const required = ['valence','arousal','intensity','location','texture1','contour','certainty','source','action'];
  for (const key of required) {
    if (!resp[key]) return `Missing ${key}.`;
  }
  if (resp.texture2 && resp.texture1 === resp.texture2) return 'Texture 2 must differ from Texture 1.';
  return null;
}

function saveCurrent() {
  const item = currentItem();
  const resp = getFormResponse();
  const problem = validateResponse(resp);
  if (problem) {
    alert(problem);
    return false;
  }
  state.responses[item.id] = resp;
  refreshSavedPreview();
  return true;
}

function responseToCanonical(resp, item) {
  const firstToken = item.stimulus.split(/\s+/)[0];
  const mod = firstToken === 'si' ? 'I' : firstToken === 'sa' ? 'A' : 'IA';
  const tex = [resp.texture1, resp.texture2].filter(Boolean).map(t => LABEL_TO_CANON.texture[t]).join('+');
  return [
    mod,
    LABEL_TO_CANON.valence[resp.valence],
    LABEL_TO_CANON.arousal[resp.arousal],
    LABEL_TO_CANON.intensity[resp.intensity],
    LABEL_TO_CANON.location[resp.location],
    tex,
    LABEL_TO_CANON.contour[resp.contour],
    LABEL_TO_CANON.certainty[resp.certainty],
    LABEL_TO_CANON.source[resp.source],
    LABEL_TO_CANON.action[resp.action],
  ].join('.');
}

function canonicalToFields(canonical) {
  const parts = canonical.split('.');
  if (parts.length !== 10) return null;
  const [mod, val, aro, intensity, loc, tex, contour, certainty, source, action] = parts;
  return {
    modality: mod,
    valence: CANON_TO_LABEL.valence[val],
    arousal: CANON_TO_LABEL.arousal[aro],
    intensity: CANON_TO_LABEL.intensity[intensity],
    location: CANON_TO_LABEL.location[loc],
    textures: tex ? tex.split('+').map(t => CANON_TO_LABEL.texture[t]).filter(Boolean).sort() : [],
    contour: CANON_TO_LABEL.contour[contour],
    certainty: CANON_TO_LABEL.certainty[certainty],
    source: CANON_TO_LABEL.source[source],
    action: CANON_TO_LABEL.action[action],
  };
}

function compareResponseToCanonical(resp, canonical) {
  const expected = canonicalToFields(canonical);
  if (!expected) return null;
  const predictedTextures = [resp.texture1, resp.texture2].filter(Boolean).map(t => normalizeLabel('texture', t)).sort();
  const fields = {
    valence: normalizeLabel('valence', resp.valence) === expected.valence,
    arousal: normalizeLabel('arousal', resp.arousal) === expected.arousal,
    intensity: normalizeLabel('intensity', resp.intensity) === expected.intensity,
    location: normalizeLabel('location', resp.location) === expected.location,
    texture: JSON.stringify(predictedTextures) === JSON.stringify(expected.textures),
    contour: normalizeLabel('contour', resp.contour) === expected.contour,
    certainty: normalizeLabel('certainty', resp.certainty) === expected.certainty,
    source: normalizeLabel('source', resp.source) === expected.source,
    action: normalizeLabel('action', resp.action) === expected.action,
  };
  const exact9 = Object.values(fields).filter(Boolean).length;
  return {
    expected_fields: expected,
    predicted_fields: {
      valence: normalizeLabel('valence', resp.valence),
      arousal: normalizeLabel('arousal', resp.arousal),
      intensity: normalizeLabel('intensity', resp.intensity),
      location: normalizeLabel('location', resp.location),
      textures: predictedTextures,
      contour: normalizeLabel('contour', resp.contour),
      certainty: normalizeLabel('certainty', resp.certainty),
      source: normalizeLabel('source', resp.source),
      action: normalizeLabel('action', resp.action),
    },
    field_matches: fields,
    exact_9_score: exact9,
    exact_match: exact9 === 9,
  };
}

function scoreItem(item, resp) {
  const keyRow = state.config.answer_key[item.id] || {};
  if (!resp) {
    return {
      status: 'missing',
      expected_canonical: keyRow.expected_canonical || null,
      acceptable_alternates: keyRow.acceptable_alternates || [],
    };
  }
  const candidates = [keyRow.expected_canonical, ...(keyRow.acceptable_alternates || [])].filter(Boolean);
  const scoredCandidates = candidates.map((canonical, idx) => ({
    canonical,
    is_primary: idx === 0,
    result: compareResponseToCanonical(resp, canonical),
  })).filter(x => x.result);
  scoredCandidates.sort((a, b) => {
    if (b.result.exact_9_score !== a.result.exact_9_score) return b.result.exact_9_score - a.result.exact_9_score;
    if (a.is_primary !== b.is_primary) return a.is_primary ? -1 : 1;
    return 0;
  });
  const best = scoredCandidates[0];
  return {
    status: best.result.exact_match ? 'exact' : 'scored',
    expected_canonical: keyRow.expected_canonical,
    acceptable_alternates: keyRow.acceptable_alternates || [],
    predicted_canonical: responseToCanonical(resp, item),
    matched_policy: best.is_primary ? 'primary' : 'alternate',
    best_match: {
      matched_canonical: best.canonical,
      exact_match: best.result.exact_match,
      exact_9_score: best.result.exact_9_score,
      field_matches: best.result.field_matches,
      expected_fields: best.result.expected_fields,
      predicted_fields: best.result.predicted_fields,
    },
  };
}

function exportResults() {
  const rows = state.packet.map(item => {
    const resp = state.responses[item.id] || null;
    return {
      id: item.id,
      condition: item.condition,
      stimulus: item.stimulus,
      response: resp,
      prediction_canonical: resp ? responseToCanonical(resp, item) : null,
      scoring: scoreItem(item, resp),
    };
  });
  const stamp = new Date().toISOString().replace(/[:.]/g, '-');
  const payload = {
    package_name: state.config.package_name,
    app_version: APP_VERSION,
    scorer_version: SCORER_VERSION,
    exported_at: new Date().toISOString(),
    packet_source: state.config.packet_source,
    answer_key_source: state.config.answer_key_source,
    packet_sha256: state.config.packet_sha256,
    answer_key_sha256: state.config.answer_key_sha256,
    config_sha256: state.config.config_sha256,
    token_change: state.config.token_change,
    scoring_note: 'exact_9_score compares the 9 scored fields. texture order is ignored during scoring. unknown normalizes to unclear.',
    summary: summarizeRows(rows),
    responses: rows,
  };
  downloadText(`route1_human_pilot_results_${stamp}.json`, JSON.stringify(payload, null, 2), 'application/json');
  downloadText(`route1_human_pilot_report_${stamp}.md`, buildMarkdownReport(payload), 'text/markdown');
}

function refreshSavedPreview() {
  const count = Object.keys(state.responses).length;
  el('savedStatus').textContent = `${count} items saved.`;
  const item = currentItem();
  const resp = state.responses[item.id];
  if (!resp) {
    el('savedPreview').textContent = 'No saved response for this item yet.';
    return;
  }
  el('savedPreview').textContent = JSON.stringify({id: item.id, response: resp}, null, 2);
}

function init() {
  state.config = window.PACKET_CONFIG;
  state.packet = state.config.packet;

  populateSelect('valence', state.config.fields.valence);
  populateSelect('arousal', state.config.fields.arousal);
  populateSelect('intensity', state.config.fields.intensity);
  populateSelect('location', state.config.fields.location);
  populateSelect('texture1', state.config.fields.texture);
  populateSelect('texture2', state.config.fields.texture, true);
  populateSelect('contour', state.config.fields.contour);
  populateSelect('certainty', state.config.fields.certainty);
  populateSelect('source', state.config.fields.source);
  populateSelect('action', state.config.fields.action);

  el('saveBtn').addEventListener('click', saveCurrent);
  el('prevBtn').addEventListener('click', () => {
    if (state.index > 0) state.index -= 1;
    render();
  });
  el('nextBtn').addEventListener('click', () => {
    if (!saveCurrent()) return;
    if (state.index < state.packet.length - 1) state.index += 1;
    render();
  });
  el('exportBtn').addEventListener('click', () => {
    if (!saveCurrent()) return;
    exportResults();
  });

  render();
}

init();
