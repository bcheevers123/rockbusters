// Rockbusters — daily phonetic quiz frontend

// ---------------------------------------------------------------------------
// Constants
// ---------------------------------------------------------------------------
const EPOCH = new Date(Date.UTC(2026, 0, 2));
const TIMEZONE = 'Europe/London';
const API_URL_ATTR = 'api-url';

// ---------------------------------------------------------------------------
// Wrong-answer responses — Karl Pilkington voice
// ---------------------------------------------------------------------------
const WRONG_RESPONSES = [
  "Nope. Not having that.",
  "That's not it, is it.",
  "No. Have a think.",
  "Wrong. But points for confidence, I suppose.",
  "I don't know what that is, but it's not right.",
  "No. Try again.",
  "You've gone wrong somewhere.",
  "That answer smells a bit off, to be honest.",
  "I've heard better guesses from a chimp.",
  "That's not a word that's ever helped anyone.",
  "No. Say it out loud.",
  "Nah. Not even close.",
  "That's not it.",
  "Have another go.",
  "Wrong. Say the clue out loud again.",
  "Not right, that.",
  "I don't think so, no.",
  "That's not the one.",
  "No. Keep going.",
  "Wrong answer. Back to the drawing board.",
  "That's a no from me.",
  "Not quite. Try again.",
  "I don't think that's a place.",
  "That's just a noise, that is.",
  "No. You're overthinking it.",
  "That's not right. Say it slower.",
  "Nope. Have another go.",
  "That's not a thing.",
  "Wrong. Your ears are letting you down.",
  "No. Start from the beginning.",
  "That doesn't sound right to me.",
  "I wouldn't put that in as an answer, personally.",
  "No. Try saying the clue out loud.",
  "Wrong. A chimp would've got that.",
  "That's not it. Not by a long way.",
  "No, that's just a sound, that is.",
  "Nope. That's not what I was after.",
  "That's not right. Have another think.",
  "I don't know where you got that from.",
  "Wrong. The answer's in the clue somewhere.",
  "That's not a country. Or a place. Or a word.",
  "No. Read the clue again.",
  "Nope. That's not even nearly right.",
  "That's a different thing entirely.",
  "Wrong. Have a biscuit and try again.",
  "That's not the answer. Just putting that out there.",
  "No. But fair play for trying.",
  "That sounds wrong even before I check.",
  "Not that. Try something else.",
  "No. What even is a word, really.",
  "Wrong. Have another go, go on.",
  "That's not it. You've got the wrong end.",
  "Nope. Say the clue slowly this time.",
  "I wouldn't put that on a quiz show.",
  "No. That's not what the sounds add up to.",
  "Wrong. Try it out loud.",
  "That's the wrong answer, and I'm fairly sure of it.",
  "No. The answer's phonetic. Say it out loud.",
  "That's not right. Your ears aren't working properly.",
  "Nope. That's a guess and not a great one.",
  "Wrong. Have a think about the sounds.",
  "That's not it. Have another go.",
  "No. The clue's telling you what to say.",
  "That's not the one I'm looking for.",
  "Wrong. Simple as that.",
  "Nope. Back to it.",
  "Not right. Not wrong in an interesting way, just wrong.",
  "No. Your brain's gone somewhere else with that.",
  "Wrong. A round head wouldn't help you here.",
  "That's not a real answer, that.",
  "Nope. That's not even a country.",
  "No. The sounds don't make that.",
  "Wrong. Try listening to yourself.",
  "That's not it. Not even a bit.",
  "Nope. That's the wrong side of wrong.",
  "No. Have a sit down and try again.",
  "Wrong. The clue was doing all the work.",
  "That's not it. The sounds were right there.",
  "I don't think anyone's ever said that out loud.",
  "Nope. Close but no biscuit.",
  "That's not right and never will be.",
  "No. Have a rethink.",
  "Wrong. You're not listening to yourself.",
  "That's not a guess, that's just letters.",
  "Nope. Didn't even land near it.",
  "No. Try a different syllable.",
  "Wrong. The clue gave it all away.",
  "That's not right. Chimps would've had it by now.",
  "No. That doesn't mean anything.",
  "Nope. Have one more go.",
  "Wrong. Say it out loud and start again.",
  "That's not it. Not today.",
  "No. Beans have been more helpful than that answer.",
  "That's not the word I'm after.",
  "Nope. The sound's in the clue.",
  "Wrong. A bit resigned now, to be honest.",
  "That's not even a phonetic thing.",
  "No. Try the other syllable.",
  "Wrong. That answer went nowhere.",
  "Nope. You've wandered off somewhere.",
  "That's not it. The clue was right there.",
  "No. That answer doesn't work.",
  "Wrong. Start with the sounds.",
  "That's not a word that leads anywhere useful.",
  "Nope. Even a spaceman could've got that.",
  "No. Read the clue one more time.",
  "Wrong. Very wrong, actually.",
  "That's not right. Not even a bit.",
  "Nope. Try saying it slow.",
  "No. That's a different kind of wrong.",
  "Wrong. The sounds don't add up to that.",
  "That's not it and I'll tell you why. Because it's wrong.",
  "Nope. Your ears have gone on holiday.",
  "No. The clue's begging you to listen.",
  "Wrong. That was a bold attempt.",
  "That's not the answer. The sounds are hiding something else.",
  "No. Have another go. You're nearly somewhere.",
  "That's not it. Not the sounds, not the place, none of it.",
  "Nope. That's a noise, not an answer.",
  "Wrong. You've missed the hidden bit.",
  "That's not right. But you're still trying, which is good.",
  "No. The answer's simpler than that.",
  "Wrong. Your brain's overcooking it.",
  "That's not it. A chimp would've cracked that clue.",
  "Nope. That's not even a real place.",
  "No. You're not saying the clue out loud are you.",
  "Wrong. Try making the sound with your mouth.",
  "That's not right. The syllables are right there.",
  "Nope. That answer doesn't make sense to anyone.",
  "No. Have another go, go on then.",
  "Wrong. That's not what the sounds are doing.",
  "That's not it. Have you tried saying it out loud.",
  "Nope. That answer's taken a wrong turn.",
  "No. The clue's a sound. Listen to it.",
  "Wrong. That's not the sound the clue's making.",
  "That's not it. The phonetics don't match that.",
  "Nope. The sounds were pointing somewhere else entirely.",
  "No. Wrong. Have another think.",
  "Wrong. Very committed to the wrong answer, fair enough.",
  "That's not it. Not by any reading of the clue.",
  "Nope. Wandered off from the sounds.",
  "No. That doesn't fit what the clue's saying.",
  "Wrong. Someone put that answer in a box and it got lost.",
  "That's not it. Try again.",
  "Nope. That's not the hidden word.",
  "No. The answer's phonetic, remember.",
  "Wrong. Socks have done more for people than that answer.",
  "That's not right. The sounds go somewhere else.",
  "Nope. That's not where the clue points.",
  "No. The word's in there. Keep going.",
  "Wrong. Close only counts in horseshoes, apparently.",
  "That's not it. There's a hidden sound you've missed.",
  "Nope. That's not it and it never will be.",
  "No. Say the clue out loud again.",
  "Wrong. Your brain's gone on a walk.",
  "That's not right. The clue's louder than that.",
  "Nope. That doesn't match the sounds at all.",
  "No. Have a go at the phonetics.",
  "Wrong. Someone somewhere is baffled by that answer.",
  "That's not it. The hidden word is different.",
  "Nope. That's the wrong direction entirely.",
  "No. Start from the first syllable.",
  "Wrong. A biscuit tin's worth more as a hint than that.",
  "That's not the answer I'm looking for.",
  "Nope. That's not what the clue's doing.",
  "No. The sounds are doing the work. Let them.",
  "Wrong. That answer landed very far away.",
  "That's not it. Have a think about the vowels.",
  "Nope. Not the right sounds.",
  "No. The word was hiding in plain sound.",
  "Wrong. You've picked the wrong thing to land on.",
  "That's not right. A bit mysterious, that answer.",
  "Nope. Not even a half-right.",
  "No. The phonetics are going somewhere else.",
  "Wrong. That's not the word the sounds make.",
  "That's not it. Not the one. Not today.",
  "Nope. That's a guess with no direction.",
  "No. The clue was right there doing everything.",
  "Wrong. Have a go with fresh ears.",
  "That's not it. Close only in the sense that you used letters.",
  "Nope. That's not it at all.",
  "No. The clue's phonetic. Go at it again.",
  "Wrong. That answer doesn't fit in the clue.",
  "That's not the one. But keep at it.",
  "Nope. That's not the hidden place.",
  "No. Have another go. You've got the sounds to work with.",
  "Wrong. That's not even the right shape of word.",
  "That's not it. The answer's easier than you think.",
  "Nope. The clue's doing the work. Let it.",
  "No. That answer's gone off on its own.",
  "Wrong. The syllables are right there.",
  "That's not right. Simple as that.",
  "Nope. That's not the sound the clue makes.",
  "No. Wrong. Go again.",
  "Wrong. That was a very confident wrong answer.",
  "That's not it. Try the other way round.",
  "Nope. Have another crack at it.",
  "No. That answer doesn't match what the clue's saying.",
  "Wrong. The sounds were very clear.",
  "That's not right. Go back to the clue.",
];

function randomWrongResponse() {
  return WRONG_RESPONSES[Math.floor(Math.random() * WRONG_RESPONSES.length)];
}

// ---------------------------------------------------------------------------
// Text normalisation
// ---------------------------------------------------------------------------
function normalize(text) {
  return text
    .toLowerCase()
    .trim()
    .replace(/[^a-z0-9 ]/g, '')
    .replace(/ +/g, ' ');
}

// ---------------------------------------------------------------------------
// Answer checking
// ---------------------------------------------------------------------------
function checkAnswer(aliases, userInput) {
  const normInput = normalize(userInput);
  return aliases.some(alias => normalize(alias) === normInput);
}

// ---------------------------------------------------------------------------
// Date helpers
// ---------------------------------------------------------------------------
function getTodayLondon() {
  const now = new Date();
  const parts = new Intl.DateTimeFormat('en-GB', {
    timeZone: TIMEZONE,
    year: 'numeric',
    month: '2-digit',
    day: '2-digit',
  }).formatToParts(now);
  const get = type => parseInt(parts.find(p => p.type === type).value, 10);
  return new Date(Date.UTC(get('year'), get('month') - 1, get('day')));
}

function getTodaysIndex(totalSets) {
  const today = getTodayLondon();
  const diffMs = today.getTime() - EPOCH.getTime();
  const diffDays = Math.floor(diffMs / (1000 * 60 * 60 * 24));
  const offset = devIsUnlocked() ? devGetOffset() : 0;
  return (((diffDays + offset) % totalSets) + totalSets) % totalSets;
}

// ---------------------------------------------------------------------------
// Holiday detection — returns null or { holiday, setPrefix, theme }
// ---------------------------------------------------------------------------
function getEasterSunday(year) {
  // Computus algorithm
  const a = year % 19;
  const b = Math.floor(year / 100);
  const c = year % 100;
  const d = Math.floor(b / 4);
  const e = b % 4;
  const f = Math.floor((b + 8) / 25);
  const g = Math.floor((b - f + 1) / 3);
  const h = (19 * a + b - d - g + 15) % 30;
  const i = Math.floor(c / 4);
  const k = c % 4;
  const l = (32 + 2 * e + 2 * i - h - k) % 7;
  const m = Math.floor((a + 11 * h + 22 * l) / 451);
  const month = Math.floor((h + l - 7 * m + 114) / 31); // 1-based
  const day = ((h + l - 7 * m + 114) % 31) + 1;
  return new Date(Date.UTC(year, month - 1, day));
}

function getHolidayForDate(date) {
  const m = date.getUTCMonth() + 1; // 1-based
  const d = date.getUTCDate();
  const y = date.getUTCFullYear();

  // Christmas: Dec 23–25
  if (m === 12 && d >= 23 && d <= 25) {
    return { holiday: 'christmas', setPrefix: 'christmasbusters', theme: 'christmas' };
  }

  // Halloween: Oct 31
  if (m === 10 && d === 31) {
    return { holiday: 'halloween', setPrefix: 'halloweenbusters', theme: 'halloween' };
  }

  // Easter: Easter Sunday ±3 days
  const easter = getEasterSunday(y);
  const diffDays = Math.round((date.getTime() - easter.getTime()) / 86400000);
  if (Math.abs(diffDays) <= 3) {
    return { holiday: 'easter', setPrefix: 'easterbusters', theme: 'easter' };
  }

  return null;
}

// ---------------------------------------------------------------------------
// Holiday theming — apply/remove CSS classes and decorations on <body>
// ---------------------------------------------------------------------------
function applyHolidayTheme(holiday) {
  document.body.classList.remove('theme-christmas', 'theme-halloween', 'theme-easter');
  const existing = document.getElementById('holiday-decoration');
  if (existing) existing.remove();

  if (!holiday) return;

  document.body.classList.add('theme-' + holiday);

  const deco = document.createElement('div');
  deco.id = 'holiday-decoration';
  deco.className = 'holiday-decoration holiday-decoration-' + holiday;

  const DECOS = {
    christmas: '&#10052; &#127876; &#10052; &#127876; &#10052; &#127876; &#10052;',
    halloween: '&#127809; &#128122; &#127809; &#128122; &#127809; &#128122; &#127809;',
    easter:    '&#128592; &#127857; &#128592; &#127857; &#128592; &#127857; &#128592;',
  };
  deco.innerHTML = DECOS[holiday] || '';
  document.body.insertBefore(deco, document.body.firstChild);
}

function formatDateBritish(date) {
  return new Intl.DateTimeFormat('en-GB', {
    day: 'numeric',
    month: 'long',
    year: 'numeric',
    timeZone: 'UTC',
  }).format(date);
}

// ---------------------------------------------------------------------------
// localStorage helpers
// ---------------------------------------------------------------------------
function getUserId() {
  const key = 'rockbusters_user_id';
  let id = localStorage.getItem(key);
  if (!id) {
    id = typeof crypto !== 'undefined' && crypto.randomUUID
      ? crypto.randomUUID()
      : Date.now().toString(36) + '-' + Math.random().toString(36).slice(2);
    localStorage.setItem(key, id);
  }
  return id;
}

function getDisplayName() {
  return localStorage.getItem('rockbusters_display_name');
}

function setDisplayName(name) {
  localStorage.setItem('rockbusters_display_name', name);
}

function loadProgress(setId) {
  const key = `rockbusters_progress_${setId}`;
  try {
    const raw = localStorage.getItem(key);
    if (raw) {
      const parsed = JSON.parse(raw);
      return {
        correct: Array.isArray(parsed.correct) ? parsed.correct : [],
        revealed: Boolean(parsed.revealed),
      };
    }
  } catch (_) {}
  return { correct: [], revealed: false };
}

function saveProgress(setId, state) {
  localStorage.setItem(`rockbusters_progress_${setId}`, JSON.stringify(state));
}

// ---------------------------------------------------------------------------
// API
// ---------------------------------------------------------------------------
function getApiUrl() {
  const meta = document.querySelector(`meta[name="${API_URL_ATTR}"]`);
  return meta ? (meta.getAttribute('content') || '') : '';
}

async function postScore(setId, clueNumber) {
  const apiUrl = getApiUrl();
  if (!apiUrl) return;
  try {
    await fetch(`${apiUrl}/api/score`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        user_id: getUserId(),
        display_name: getDisplayName() || 'Anonymous',
        set_id: setId,
        clue_number: clueNumber,
      }),
    });
  } catch (e) {
    console.warn('Score post failed:', e);
  }
}

async function postReveal(setId) {
  const apiUrl = getApiUrl();
  if (!apiUrl) return;
  try {
    await fetch(`${apiUrl}/api/reveal`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        user_id: getUserId(),
        display_name: getDisplayName() || 'Anonymous',
        set_id: setId,
      }),
    });
  } catch (e) {
    console.warn('Reveal post failed:', e);
  }
}

// ---------------------------------------------------------------------------
// Leaderboard
// ---------------------------------------------------------------------------
async function loadLeaderboard() {
  const apiUrl = getApiUrl();
  const list = document.getElementById('leaderboard-list');
  if (!list) return;

  if (!apiUrl) {
    list.innerHTML = '<p style="font-size:0.88rem;color:#888">Leaderboard unavailable.</p>';
    return;
  }

  list.innerHTML = '<p style="font-size:0.88rem;color:#888">Loading...</p>';

  try {
    const res = await fetch(`${apiUrl}/api/leaderboard`);
    if (!res.ok) throw new Error(`HTTP ${res.status}`);
    const data = await res.json();
    const entries = data.leaderboard ?? [];

    if (entries.length === 0) {
      list.innerHTML = '<p style="font-size:0.88rem;color:#888">No scores yet. Be the first.</p>';
      return;
    }

    list.innerHTML = '';
    entries.forEach((entry, idx) => {
      const row = document.createElement('div');
      row.className = 'leaderboard-row';

      const rank = document.createElement('span');
      rank.className = 'lb-rank';
      rank.textContent = idx + 1;

      const name = document.createElement('span');
      name.className = 'lb-name';
      name.textContent = entry.display_name || 'Anonymous';

      const score = document.createElement('span');
      score.className = 'lb-score';
      score.textContent = entry.total_points ?? 0;

      row.appendChild(rank);
      row.appendChild(name);
      row.appendChild(score);

      if (entry.today_points > 0) {
        const today = document.createElement('span');
        today.className = 'lb-today';
        today.textContent = `+${entry.today_points} today`;
        row.appendChild(today);
      }

      list.appendChild(row);
    });
  } catch (e) {
    console.warn('Leaderboard fetch failed:', e);
    list.innerHTML = '<p style="font-size:0.88rem;color:#888">Leaderboard unavailable.</p>';
  }
}

// ---------------------------------------------------------------------------
// Score tracker UI
// ---------------------------------------------------------------------------
function updateScoreTracker(correctCount) {
  for (let i = 1; i <= 3; i++) {
    const dot = document.getElementById(`score-dot-${i}`);
    if (dot) dot.classList.toggle('earned', i <= correctCount);
  }
  const label = document.getElementById('score-label');
  if (label) label.textContent = `${correctCount} / 3`;
}

// ---------------------------------------------------------------------------
// Confetti
// ---------------------------------------------------------------------------
function launchConfetti() {
  const canvas = document.getElementById('confetti-canvas');
  if (!canvas) return;
  const ctx = canvas.getContext('2d');

  canvas.width = window.innerWidth;
  canvas.height = window.innerHeight;

  const COLOURS = ['#b35a00','#d4860a','#f5a623','#2ecc71','#3498db','#e74c3c','#9b59b6','#f39c12'];
  const particles = [];

  for (let i = 0; i < 120; i++) {
    particles.push({
      x: Math.random() * canvas.width,
      y: Math.random() * -canvas.height * 0.4,
      w: 6 + Math.random() * 8,
      h: 3 + Math.random() * 4,
      colour: COLOURS[Math.floor(Math.random() * COLOURS.length)],
      rot: Math.random() * Math.PI * 2,
      rotSpeed: (Math.random() - 0.5) * 0.15,
      vx: (Math.random() - 0.5) * 3,
      vy: 2.5 + Math.random() * 3.5,
      alpha: 1,
    });
  }

  let frame;
  let elapsed = 0;

  function draw() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    elapsed++;
    let any = false;
    particles.forEach(p => {
      p.x += p.vx;
      p.y += p.vy;
      p.rot += p.rotSpeed;
      if (elapsed > 80) p.alpha = Math.max(0, p.alpha - 0.012);
      if (p.y < canvas.height + 20 && p.alpha > 0) {
        any = true;
        ctx.save();
        ctx.globalAlpha = p.alpha;
        ctx.translate(p.x, p.y);
        ctx.rotate(p.rot);
        ctx.fillStyle = p.colour;
        ctx.fillRect(-p.w / 2, -p.h / 2, p.w, p.h);
        ctx.restore();
      }
    });
    if (any) {
      frame = requestAnimationFrame(draw);
    } else {
      ctx.clearRect(0, 0, canvas.width, canvas.height);
    }
  }

  if (frame) cancelAnimationFrame(frame);
  draw();
}

// ---------------------------------------------------------------------------
// Dev mode — offset-based set rotation, passcode-gated
// ---------------------------------------------------------------------------

// SHA-256 of "monkeynews" — plaintext never stored in source
const DEV_PASSCODE_HASH = '7cad4eb0e04bd259d1291faa24c9b04a52cb6697ede50931cde44e046019c20d';
// In-memory only — lost on every navigation or refresh, never persisted
let _devUnlocked = false;
const DEV_OFFSET_KEY = 'rockbusters_dev_offset';

async function sha256hex(str) {
  const buf = await crypto.subtle.digest('SHA-256', new TextEncoder().encode(str));
  return Array.from(new Uint8Array(buf)).map(b => b.toString(16).padStart(2, '0')).join('');
}

function devIsUnlocked() {
  return _devUnlocked;
}

function devGetOffset() {
  return parseInt(localStorage.getItem(DEV_OFFSET_KEY) || '0', 10) || 0;
}

function devSetOffset(n) {
  localStorage.setItem(DEV_OFFSET_KEY, String(n));
}

async function devUnlock() {
  const raw = window.prompt('Dev passcode:');
  if (!raw) return;
  const hash = await sha256hex(raw.trim());
  if (hash === DEV_PASSCODE_HASH) {
    _devUnlocked = true;
    devShowPanel();
    devUpdateInfo();
  } else {
    window.alert('Wrong passcode.');
  }
}

function devLock() {
  _devUnlocked = false;
  const panel = document.getElementById('dev-panel');
  if (panel) panel.style.display = 'none';
  document.body.style.paddingBottom = '';
}

function devShowPanel() {
  const panel = document.getElementById('dev-panel');
  if (panel) {
    panel.style.display = 'flex';
    document.body.style.paddingBottom = '52px';
  }
}

function devUpdateInfo() {
  const info = document.getElementById('dev-set-info');
  if (!info) return;
  const offset = devGetOffset();
  const offsetStr = offset === 0 ? 'offset: 0 (today)' : `offset: ${offset > 0 ? '+' : ''}${offset}`;
  const setStr = _setId ? `  ·  ${_setId}` : '';
  info.textContent = offsetStr + setStr;
}

function devStep(delta) {
  devSetOffset(devGetOffset() + delta);
  loadQuiz();
}

function devResetToToday() {
  devSetOffset(0);
  loadQuiz();
}

async function devResetLeaderboard() {
  const secret = window.prompt('Dev passcode:');
  if (!secret) return;
  const apiUrl = getApiUrl();
  if (!apiUrl) { window.alert('No API URL configured.'); return; }
  if (!window.confirm('Reset the entire leaderboard? This cannot be undone.')) return;
  try {
    const res = await fetch(`${apiUrl}/api/admin/reset-leaderboard?secret=${encodeURIComponent(secret)}`, { method: 'POST' });
    const data = await res.json();
    if (res.ok) {
      window.alert('Leaderboard reset.');
      loadLeaderboard();
    } else {
      window.alert(`Error: ${data.detail || res.status}`);
    }
  } catch (e) {
    window.alert(`Failed: ${e.message}`);
  }
}

// ---------------------------------------------------------------------------
// Quiz state — module-level, read by all handlers
// ---------------------------------------------------------------------------
let _answerClues = [];
let _progress = null;
let _setId = null;
let _totalClues = 3;

// ---------------------------------------------------------------------------
// DOM helpers
// ---------------------------------------------------------------------------
function setText(id, value) {
  const el = document.getElementById(id);
  if (el) el.textContent = value;
}

function setResult(clueNumber, type, message) {
  const el = document.getElementById(`result-${clueNumber}`);
  if (!el) return;
  el.textContent = message;
  el.className = `result ${type}`;
}

function disableClue(clueNumber) {
  const input = document.getElementById(`guess-input-${clueNumber}`);
  const btn = document.getElementById(`guess-btn-${clueNumber}`);
  if (input) input.disabled = true;
  if (btn) btn.disabled = true;
}

function enableClue(clueNumber) {
  const input = document.getElementById(`guess-input-${clueNumber}`);
  const btn = document.getElementById(`guess-btn-${clueNumber}`);
  if (input) { input.disabled = false; input.value = ''; }
  if (btn) btn.disabled = false;
}

function markClueBlockCorrect(clueNumber) {
  const block = document.getElementById(`clue-block-${clueNumber}`);
  if (block) block.classList.add('correct');
}

function showAnswers(answerClues) {
  const section = document.getElementById('answers-section');
  if (section) section.style.display = '';
  answerClues.forEach(ac => {
    const el = document.getElementById(`answer-line-${ac.number}`);
    if (el) el.textContent = `${ac.answer}: ${ac.reasoning}`;
  });
  const warning = document.getElementById('answers-warning');
  if (warning) warning.textContent = "You've seen the answers — no points for today's set.";
}

// Reset all mutable quiz UI back to a clean state before re-rendering
function resetQuizUI() {
  for (let n = 1; n <= 3; n++) {
    enableClue(n);
    setResult(n, '', '');
    const block = document.getElementById(`clue-block-${n}`);
    if (block) block.classList.remove('correct');
    const ansLine = document.getElementById(`answer-line-${n}`);
    if (ansLine) ansLine.textContent = '';
  }

  const answersSection = document.getElementById('answers-section');
  if (answersSection) answersSection.style.display = 'none';

  const warning = document.getElementById('answers-warning');
  if (warning) warning.textContent = '';

  const revealBtn = document.getElementById('reveal-btn');
  if (revealBtn) { revealBtn.style.display = ''; revealBtn.disabled = false; }

  const banner = document.getElementById('all-correct-banner');
  if (banner) banner.style.display = 'none';
}

function checkAllCorrect() {
  if (_progress && _progress.correct.length === _totalClues && !_progress.revealed) {
    const banner = document.getElementById('all-correct-banner');
    if (banner && banner.style.display === 'none') {
      banner.style.display = '';
      launchConfetti();
    }
  }
}

// ---------------------------------------------------------------------------
// handleGuess — reads module-level state; safe to call multiple times
// ---------------------------------------------------------------------------
function handleGuess(clueNumber) {
  if (!_progress || !_answerClues) return;

  if (_progress.revealed) {
    setResult(clueNumber, 'info', "You've seen the answers — no more guesses.");
    return;
  }
  if (_progress.correct.includes(clueNumber)) {
    setResult(clueNumber, 'info', "Already got that one.");
    return;
  }

  const input = document.getElementById(`guess-input-${clueNumber}`);
  const userInput = input ? input.value : '';
  const answerClue = _answerClues.find(ac => ac.number === clueNumber);
  if (!answerClue) return;

  if (checkAnswer(answerClue.aliases, userInput)) {
    _progress.correct.push(clueNumber);
    saveProgress(_setId, _progress);
    setResult(clueNumber, 'correct', 'Correct!');
    disableClue(clueNumber);
    markClueBlockCorrect(clueNumber);
    updateScoreTracker(_progress.correct.length);
    postScore(_setId, clueNumber);
    checkAllCorrect();
  } else {
    setResult(clueNumber, 'incorrect', randomWrongResponse());
  }
}

// ---------------------------------------------------------------------------
// handleReveal — reads module-level state
// ---------------------------------------------------------------------------
function handleReveal() {
  if (!_progress) return;
  if (!_answerClues || _answerClues.length === 0) return;
  if (_progress.revealed) return;

  _progress.revealed = true;
  saveProgress(_setId, _progress);

  for (let n = 1; n <= _totalClues; n++) disableClue(n);
  showAnswers(_answerClues);
  postReveal(_setId);

  const revealBtn = document.getElementById('reveal-btn');
  if (revealBtn) { revealBtn.disabled = true; revealBtn.style.display = 'none'; }
}

// ---------------------------------------------------------------------------
// renderQuiz — pure content update; does NOT wire event listeners
// ---------------------------------------------------------------------------
function renderQuiz(todaySet, answerClues, progress) {
  // Reset UI to clean state first
  resetQuizUI();

  // Update module-level state
  _answerClues = answerClues;
  _progress = progress;
  _setId = todaySet.id;
  _totalClues = todaySet.clues.length;

  // Populate content
  setText('quiz-title', todaySet.title);
  setText('quiz-date', formatDateBritish(getTodayLondon()));
  setText('quiz-intro', todaySet.intro);
  setText('quiz-prize', todaySet.prize);

  todaySet.clues.forEach(clue => {
    const n = clue.number;
    setText(`clue-${n}`, clue.clue);
    setText(`initials-${n}`, clue.initials);
  });

  // Restore progress state
  updateScoreTracker(progress.correct.length);

  progress.correct.forEach(n => {
    setResult(n, 'correct', "Already got that one.");
    disableClue(n);
    markClueBlockCorrect(n);
  });

  if (progress.correct.length === _totalClues && !progress.revealed) {
    const banner = document.getElementById('all-correct-banner');
    if (banner) banner.style.display = '';
  }

  if (progress.revealed) {
    showAnswers(answerClues);
    for (let n = 1; n <= _totalClues; n++) disableClue(n);
    const revealBtn = document.getElementById('reveal-btn');
    if (revealBtn) { revealBtn.disabled = true; revealBtn.style.display = 'none'; }
  }

  if (devIsUnlocked()) devUpdateInfo();
}

// ---------------------------------------------------------------------------
// loadQuiz — fetch + render; safe to call repeatedly
// ---------------------------------------------------------------------------
async function loadQuiz() {
  try {
    const today = getTodayLondon();
    const holiday = getHolidayForDate(today);

    // Apply or remove holiday theming
    applyHolidayTheme(holiday ? holiday.holiday : null);

    // Fetch holiday sets if needed, else regular sets
    const fetchPaths = ['data/rockbusters.json', 'data/rockbusters-answers.json'];
    if (holiday) {
      fetchPaths.push('data/holiday-sets.json', 'data/holiday-answers.json');
    }

    const [qRes, aRes, hqRes, haRes] = await Promise.all(fetchPaths.map(p => fetch(p)));
    if (!qRes.ok) throw new Error(`Quiz data HTTP ${qRes.status}`);
    if (!aRes.ok) throw new Error(`Answer data HTTP ${aRes.status}`);

    const allAnswers = await aRes.json();

    let todaySet, answerClues;

    if (holiday && hqRes && hqRes.ok && haRes && haRes.ok) {
      const holidaySets = await hqRes.json();
      const holidayAnswers = await haRes.json();
      const matchingSets = holidaySets.filter(s => s.id.startsWith(holiday.setPrefix));
      if (matchingSets.length > 0) {
        const idx = getTodaysIndex(matchingSets.length);
        todaySet = matchingSets[idx];
        const answerSet = holidayAnswers.find(a => a.id === todaySet.id);
        answerClues = answerSet ? answerSet.clues : [];
      }
    }

    // Fallback to regular rotation if no holiday set found
    if (!todaySet) {
      const allSets = await qRes.json();
      const enabledSets = allSets.filter(s => s.enabled !== false);
      if (enabledSets.length === 0) throw new Error('No enabled sets found.');
      const todayIndex = getTodaysIndex(enabledSets.length);
      todaySet = enabledSets[todayIndex];
      const answerSet = allAnswers.find(a => a.id === todaySet.id);
      answerClues = answerSet ? answerSet.clues : [];
    }

    const progress = loadProgress(todaySet.id);
    renderQuiz(todaySet, answerClues, progress);
    loadLeaderboard();
  } catch (err) {
    console.error('loadQuiz failed:', err);
    const container = document.getElementById('quiz-container');
    if (container) {
      container.innerHTML = '<p class="error">Failed to load today\'s quiz. Try refreshing.</p>';
    }
  }
}

// ---------------------------------------------------------------------------
// Help modal
// ---------------------------------------------------------------------------
function openHelp() {
  const modal = document.getElementById('help-modal');
  if (modal) modal.style.display = '';
  document.body.style.overflow = 'hidden';
}

function closeHelp() {
  const modal = document.getElementById('help-modal');
  if (modal) modal.style.display = 'none';
  document.body.style.overflow = '';
}

// ---------------------------------------------------------------------------
// About toggle
// ---------------------------------------------------------------------------
function toggleAbout() {
  const content = document.getElementById('about-content');
  const btn = document.getElementById('about-toggle-btn');
  if (!content) return;
  const visible = content.style.display !== 'none';
  content.style.display = visible ? 'none' : '';
  if (btn) btn.textContent = visible ? 'About Rockbusters' : 'Hide';
}

// ---------------------------------------------------------------------------
// Countdown to midnight GMT
// ---------------------------------------------------------------------------
function updateCountdown() {
  const el = document.getElementById('countdown');
  if (!el) return;

  const now = new Date();
  // Midnight tonight in GMT = start of tomorrow UTC
  const nowUtc = now.getTime() + now.getTimezoneOffset() * 60000; // ms since epoch in UTC
  const todayUtcMidnight = Math.floor(nowUtc / 86400000) * 86400000;
  const nextMidnightUtc = todayUtcMidnight + 86400000;
  const msLeft = nextMidnightUtc - nowUtc;

  const h = Math.floor(msLeft / 3600000);
  const m = Math.floor((msLeft % 3600000) / 60000);
  const s = Math.floor((msLeft % 60000) / 1000);

  const pad = n => String(n).padStart(2, '0');
  el.textContent = `Next Rockbusters in ${pad(h)}:${pad(m)}:${pad(s)}`;
  el.classList.toggle('countdown-urgent', h === 0 && m < 10);
}

function startCountdown() {
  updateCountdown();
  setInterval(updateCountdown, 1000);
}

// ---------------------------------------------------------------------------
// Wire all static buttons once — called once from initApp
// ---------------------------------------------------------------------------
function wireQuizButtons() {
  // Clue guess buttons — handlers read module-level state, safe as permanent listeners
  for (let n = 1; n <= 3; n++) {
    const btn = document.getElementById(`guess-btn-${n}`);
    const input = document.getElementById(`guess-input-${n}`);
    if (btn) btn.addEventListener('click', () => handleGuess(n));
    if (input) input.addEventListener('keydown', e => { if (e.key === 'Enter') handleGuess(n); });
  }

  const revealBtn = document.getElementById('reveal-btn');
  if (revealBtn) revealBtn.addEventListener('click', handleReveal);

  const helpOpenBtn = document.getElementById('help-open-btn');
  const helpCloseBtn = document.getElementById('help-close-btn');
  const helpModal = document.getElementById('help-modal');
  if (helpOpenBtn) helpOpenBtn.addEventListener('click', openHelp);
  if (helpCloseBtn) helpCloseBtn.addEventListener('click', closeHelp);
  if (helpModal) helpModal.addEventListener('click', e => { if (e.target === helpModal) closeHelp(); });
  document.addEventListener('keydown', e => { if (e.key === 'Escape') closeHelp(); });

  const aboutBtn = document.getElementById('about-toggle-btn');
  if (aboutBtn) aboutBtn.addEventListener('click', toggleAbout);

  const refreshBtn = document.getElementById('leaderboard-refresh-btn');
  if (refreshBtn) refreshBtn.addEventListener('click', loadLeaderboard);

  // Dev panel buttons
  const devPrev = document.getElementById('dev-prev-btn');
  const devNext = document.getElementById('dev-next-btn');
  const devReset = document.getElementById('dev-reset-btn');
  const devResetLbBtn = document.getElementById('dev-reset-lb-btn');
  const devLockBtn = document.getElementById('dev-lock-btn');
  if (devPrev)       devPrev.addEventListener('click', () => devStep(-1));
  if (devNext)       devNext.addEventListener('click', () => devStep(1));
  if (devReset)      devReset.addEventListener('click', devResetToToday);
  if (devResetLbBtn) devResetLbBtn.addEventListener('click', devResetLeaderboard);
  if (devLockBtn)    devLockBtn.addEventListener('click', devLock);
}

// ---------------------------------------------------------------------------
// initApp
// ---------------------------------------------------------------------------
function initApp() {
  wireQuizButtons();
  startCountdown();

  // Hidden trigger: click site title 3x within 3 seconds
  let _tapCount = 0;
  let _tapTimer = null;
  const siteTitle = document.querySelector('.site-title');
  if (siteTitle) {
    siteTitle.addEventListener('click', () => {
      if (devIsUnlocked()) return;
      _tapCount++;
      clearTimeout(_tapTimer);
      _tapTimer = setTimeout(() => { _tapCount = 0; }, 3000);
      console.log('[dev] tap', _tapCount, '/ 3');
      if (_tapCount >= 3) {
        _tapCount = 0;
        devUnlock();
      }
    });
  }

  const displayName = getDisplayName();

  if (!displayName) {
    const namePrompt = document.getElementById('name-prompt');
    const quizContainer = document.getElementById('quiz-container');
    if (namePrompt) namePrompt.style.display = '';
    if (quizContainer) quizContainer.style.display = 'none';

    const submitBtn = document.getElementById('name-submit-btn');
    const nameInput = document.getElementById('name-input');

    const submitName = () => {
      const name = nameInput ? nameInput.value.trim() : '';
      if (name) {
        setDisplayName(name);
        if (namePrompt) namePrompt.style.display = 'none';
        if (quizContainer) quizContainer.style.display = '';
        loadQuiz();
      }
    };

    if (submitBtn) submitBtn.addEventListener('click', submitName);
    if (nameInput) nameInput.addEventListener('keydown', e => { if (e.key === 'Enter') submitName(); });
  } else {
    const namePrompt = document.getElementById('name-prompt');
    const quizContainer = document.getElementById('quiz-container');
    if (namePrompt) namePrompt.style.display = 'none';
    if (quizContainer) quizContainer.style.display = '';
    loadQuiz();
  }
}

// ---------------------------------------------------------------------------
// Expose to global scope (no bundler)
// ---------------------------------------------------------------------------
window.initApp = initApp;
window.loadQuiz = loadQuiz;
window.loadLeaderboard = loadLeaderboard;
window.normalize = normalize;
window.checkAnswer = checkAnswer;
window.getTodaysIndex = getTodaysIndex;
window.getTodayLondon = getTodayLondon;
window.formatDateBritish = formatDateBritish;
window.getUserId = getUserId;
window.getDisplayName = getDisplayName;
window.setDisplayName = setDisplayName;
window.loadProgress = loadProgress;
window.saveProgress = saveProgress;
window.handleGuess = handleGuess;
window.handleReveal = handleReveal;
window.devUnlock = devUnlock;

// ---------------------------------------------------------------------------
// Boot
// ---------------------------------------------------------------------------
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', initApp);
} else {
  initApp();
}
