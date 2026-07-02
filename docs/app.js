// Rockbusters — daily phonetic quiz frontend

// ---------------------------------------------------------------------------
// Constants
// ---------------------------------------------------------------------------
const EPOCH = new Date(Date.UTC(2026, 0, 1));
const TIMEZONE = 'Europe/London';
const API_URL_ATTR = 'api-url';

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

// SHA-256 of "boiledham" — plaintext never stored in source
const DEV_PASSCODE_HASH = 'b814c48a478fe52433832f44c65538724c1022983c4949ecf8639b7e99ec8fbc';
const DEV_SESSION_KEY   = 'rockbusters_dev_unlocked';
const DEV_OFFSET_KEY    = 'rockbusters_dev_offset';

async function sha256hex(str) {
  const buf = await crypto.subtle.digest('SHA-256', new TextEncoder().encode(str));
  return Array.from(new Uint8Array(buf)).map(b => b.toString(16).padStart(2, '0')).join('');
}

function devIsUnlocked() {
  return sessionStorage.getItem(DEV_SESSION_KEY) === '1';
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
    sessionStorage.setItem(DEV_SESSION_KEY, '1');
    devShowPanel();
    devUpdateInfo();
  } else {
    window.alert('Wrong passcode.');
  }
}

function devLock() {
  sessionStorage.removeItem(DEV_SESSION_KEY);
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
    setResult(clueNumber, 'incorrect', 'Nope. Not having that.');
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
    const [qRes, aRes] = await Promise.all([
      fetch('data/rockbusters.json'),
      fetch('data/rockbusters-answers.json'),
    ]);
    if (!qRes.ok) throw new Error(`Quiz data HTTP ${qRes.status}`);
    if (!aRes.ok) throw new Error(`Answer data HTTP ${aRes.status}`);

    const allSets = await qRes.json();
    const allAnswers = await aRes.json();

    const enabledSets = allSets.filter(s => s.enabled !== false);
    if (enabledSets.length === 0) throw new Error('No enabled sets found.');

    const todayIndex = getTodaysIndex(enabledSets.length);
    const todaySet = enabledSets[todayIndex];
    const progress = loadProgress(todaySet.id);
    const answerSet = allAnswers.find(a => a.id === todaySet.id);
    const answerClues = answerSet ? answerSet.clues : [];

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
  const devLockBtn = document.getElementById('dev-lock-btn');
  if (devPrev)    devPrev.addEventListener('click', () => devStep(-1));
  if (devNext)    devNext.addEventListener('click', () => devStep(1));
  if (devReset)   devReset.addEventListener('click', devResetToToday);
  if (devLockBtn) devLockBtn.addEventListener('click', devLock);
}

// ---------------------------------------------------------------------------
// initApp
// ---------------------------------------------------------------------------
function initApp() {
  wireQuizButtons();

  // Dev session restore
  if (devIsUnlocked()) {
    devShowPanel();
    devUpdateInfo();
  }

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
