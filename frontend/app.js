/* ── Note mapping: English ↔ German (API uses German) ────────── */
const NOTES_EN  = ['C','C#','D','Eb','E','F','F#','G','Ab','A','Bb','B'];
const NOTES_API = ['C','Cis','D','Es','E','F','Fis','G','As','A','B','H'];

const toApi = en => NOTES_API[NOTES_EN.indexOf(en)];
const toEn  = api => NOTES_EN[NOTES_API.indexOf(api)] ?? api;

/* Degree labels */
const DEGREES = ['1','2','3','4','5','6','7'];
const ROMAN   = ['I','II','III','IV','V','VI','VII'];

/* ── Chord quality options ───────────────────────────────────── */
const TRIAD_QUALITIES   = ['major','minor','diminished','augmented'];
const SEVENTH_QUALITIES = ['major7','dominant7','minor7','half_diminished','diminished7'];
const qualityLabel = q => ({
  major:'Major', minor:'Minor', diminished:'Diminished', augmented:'Augmented',
  major7:'Major 7th', dominant7:'Dominant 7th', minor7:'Minor 7th',
  half_diminished:'Half-diminished', diminished7:'Diminished 7th'
}[q] ?? q);

/* ── Populate note dropdowns ─────────────────────────────────── */
function populateNotes(selectId) {
  const sel = document.getElementById(selectId);
  NOTES_EN.forEach(n => {
    const opt = document.createElement('option');
    opt.value = n;
    opt.textContent = n;
    sel.appendChild(opt);
  });
}
['scale-tonic','interval-note1','interval-note2','chord-root','diatonic-tonic']
  .forEach(populateNotes);

/* ── Populate chord quality dropdown ─────────────────────────── */
let currentChordType = 'triad';

function populateQualities(type) {
  const sel = document.getElementById('chord-quality');
  sel.innerHTML = '';
  const list = type === 'triad' ? TRIAD_QUALITIES : SEVENTH_QUALITIES;
  list.forEach(q => {
    const opt = document.createElement('option');
    opt.value = q;
    opt.textContent = qualityLabel(q);
    sel.appendChild(opt);
  });
  // Show/hide 3rd inversion option
  const inv3 = document.querySelector('#chord-inversion option[value="3"]');
  inv3.style.display = type === 'seventh' ? '' : 'none';
}
populateQualities('triad');

/* ── Tab navigation ─────────────────────────────────────────── */
document.querySelectorAll('.nav-btn').forEach(btn => {
  btn.addEventListener('click', () => {
    document.querySelectorAll('.nav-btn').forEach(b => b.classList.remove('active'));
    document.querySelectorAll('.section').forEach(s => s.classList.remove('active'));
    btn.classList.add('active');
    document.getElementById(btn.dataset.section).classList.add('active');
  });
});

/* ── Triad / Seventh toggle ─────────────────────────────────── */
document.querySelectorAll('.toggle-btn').forEach(btn => {
  btn.addEventListener('click', () => {
    document.querySelectorAll('.toggle-btn').forEach(b => b.classList.remove('active'));
    btn.classList.add('active');
    currentChordType = btn.dataset.type;
    populateQualities(currentChordType);
  });
});

/* ── API base URL ───────────────────────────────────────────── */
const API = '/api';

/* ── Helper: show API url ────────────────────────────────────── */
function showUrl(elId, url) {
  const el = document.getElementById(elId);
  el.textContent = '↗ ' + url;
  el.classList.add('visible');
}

/* ── Helper: show / hide result box ─────────────────────────── */
function showResult(elId, html) {
  const el = document.getElementById(elId);
  el.innerHTML = html;
  el.classList.add('visible');
}

/* ── SCALES ─────────────────────────────────────────────────── */
document.getElementById('scale-btn').addEventListener('click', async () => {
  const tonic = document.getElementById('scale-tonic').value;
  const mode  = document.getElementById('scale-mode').value;
  const url   = `${API}/scales/${toApi(tonic)}/${mode}`;
  showUrl('scale-url', url);

  try {
    const data = await fetch(url).then(r => r.json());
    if (data.error) { showResult('scale-result', `<p class="error">${data.error}</p>`); return; }

    const pills = data.notes
      .map((n, i) => `
        <div class="note-pill">
          <span class="degree">${DEGREES[i]}</span>
          <span class="note-name">${toEn(n)}</span>
        </div>`)
      .join('');
    showResult('scale-result', `<div class="scale-notes">${pills}</div>`);
  } catch (e) {
    showResult('scale-result', `<p class="error">Could not reach the API. Is Flask running?</p>`);
  }
});

/* ── INTERVALS ───────────────────────────────────────────────── */
document.getElementById('interval-btn').addEventListener('click', async () => {
  const note1 = document.getElementById('interval-note1').value;
  const note2 = document.getElementById('interval-note2').value;
  const url   = `${API}/interval?note1=${toApi(note1)}&note2=${toApi(note2)}`;
  showUrl('interval-url', url);

  try {
    const data = await fetch(url).then(r => r.json());
    if (data.error) { showResult('interval-result', `<p class="error">${data.error}</p>`); return; }

    showResult('interval-result', `
      <div class="interval-name">${data.name}</div>
      <div class="interval-meta">
        <span>Quality: ${data.quality}</span>
        <span>Inversion: ${data.inversion}</span>
      </div>`);
  } catch (e) {
    showResult('interval-result', `<p class="error">Could not reach the API.</p>`);
  }
});

/* ── CHORDS ──────────────────────────────────────────────────── */
document.getElementById('chord-btn').addEventListener('click', async () => {
  const root      = document.getElementById('chord-root').value;
  const quality   = document.getElementById('chord-quality').value;
  const inversion = document.getElementById('chord-inversion').value;
  const endpoint  = currentChordType === 'triad' ? 'chord' : 'seventh';
  const url       = `${API}/${endpoint}?root=${toApi(root)}&quality=${quality}&inversion=${inversion}`;
  showUrl('chord-url', url);

  try {
    const data = await fetch(url).then(r => r.json());
    if (data.error) { showResult('chord-result', `<p class="error">${data.error}</p>`); return; }

    const bassNote = toEn(data.bass_note);
    const notePills = data.notes.map(n => {
      const en = toEn(n);
      return `<span class="chord-note${en === bassNote ? ' bass' : ''}">${en}</span>`;
    }).join('');

    showResult('chord-result', `
      <div class="chord-name">${data.name}</div>
      <div class="chord-notes">${notePills}</div>
      <div class="chord-intervals">Intervals above bass: ${data.intervals_above_bass?.join(', ') ?? '—'}</div>`);
  } catch (e) {
    showResult('chord-result', `<p class="error">Could not reach the API.</p>`);
  }
});

/* ── DIATONIC CHORDS ─────────────────────────────────────────── */
document.getElementById('diatonic-btn').addEventListener('click', async () => {
  const tonic = document.getElementById('diatonic-tonic').value;
  const mode  = document.getElementById('diatonic-mode').value;
  const url   = `${API}/diatonic?tonic=${toApi(tonic)}&mode=${mode}`;
  showUrl('diatonic-url', url);

  try {
    const data = await fetch(url).then(r => r.json());
    if (data.error) { showResult('diatonic-result', `<p class="error">${data.error}</p>`); return; }

    const buildTable = chords => `
      <table>
        <thead><tr><th>#</th><th>Root</th><th>Quality</th><th>Notes</th></tr></thead>
        <tbody>
          ${chords.map((c, i) => `
            <tr>
              <td>${ROMAN[i]}</td>
              <td>${toEn(c.root)}</td>
              <td>${qualityLabel(c.quality)}</td>
              <td>${c.notes.map(toEn).join(' – ')}</td>
            </tr>`).join('')}
        </tbody>
      </table>`;

    showResult('diatonic-result', `
      <div class="diatonic-tables">
        <div><h3>Triads</h3>${buildTable(data.triads)}</div>
        <div><h3>Seventh chords</h3>${buildTable(data.sevenths)}</div>
      </div>`);
  } catch (e) {
    showResult('diatonic-result', `<p class="error">Could not reach the API.</p>`);
  }
});