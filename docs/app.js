// Rockbusters — main JavaScript entry point for the daily quiz frontend.

// ---------------------------------------------------------------------------
// Constants
// ---------------------------------------------------------------------------
const EPOCH = new Date(Date.UTC(2026, 0, 1)); // 2026-01-01 UTC
const TIMEZONE = 'Europe/London';
const API_URL_ATTR = 'api-url'; // meta tag name

// ---------------------------------------------------------------------------
// Text normalisation — same rules as Python:
// lowercase, trim, collapse spaces, remove non-alphanumeric-space characters
// ---------------------------------------------------------------------------
function normalize(text) {
  return text
    .toLowerCase()
    .trim()
    .replace(/[^a-z0-9 ]/g, '')
    .replace(/ +/g, ' ');
}

// ---------------------------------------------------------------------------
// Answer checking — compare normalised user input against a clue's aliases
// ---------------------------------------------------------------------------
function checkAnswer(aliases, userInput) {
  const normInput = normalize(userInput);
  return aliases.some(alias => normalize(alias) === normInput);
}

// ---------------------------------------------------------------------------
// Date helpers
// ---------------------------------------------------------------------------

// Get today's London date as a plain Date (midnight UTC, but representing the
// London calendar date — what matters is the y/m/d extracted via Intl).
function getTodayLondon() {
  const now = new Date();
  const parts = new Intl.DateTimeFormat('en-GB', {
    timeZone: TIMEZONE,
    year: 'numeric',
    month: '2-digit',
    day: '2-digit',
  }).formatToParts(now);

  const get = type => parseInt(parts.find(p => p.type === type).value, 10);
  // Return a Date whose UTC midnight represents the London calendar date
  return new Date(Date.UTC(get('year'), get('month') - 1, get('day')));
}

// Get today's 0-based set index: days since EPOCH (London date) % totalSets
function getTodaysIndex(totalSets) {
  const today = getTodayLondon();
  const diffMs = today.getTime() - EPOCH.getTime();
  const diffDays = Math.floor(diffMs / (1000 * 60 * 60 * 24));
  // Handle dates before epoch gracefully (treat as 0)
  const positiveDiff = ((diffDays % totalSets) + totalSets) % totalSets;
  return positiveDiff;
}

// British long date format: "1 July 2026"
function formatDateBritish(date) {
  return new Intl.DateTimeFormat('en-GB', {
    day: 'numeric',
    month: 'long',
    year: 'numeric',
    timeZone: 'UTC', // date is already expressed as UTC midnight for the London day
  }).format(date);
}

// ---------------------------------------------------------------------------
// localStorage helpers
// ---------------------------------------------------------------------------

function getUserId() {
  const key = 'rockbusters_user_id';
  let id = localStorage.getItem(key);
  if (!id) {
    if (typeof crypto !== 'undefined' && crypto.randomUUID) {
      id = crypto.randomUUID();
    } else {
      // Fallback: timestamp + random
      id = Date.now().toString(36) + '-' + Math.random().toString(36).slice(2);
    }
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

// Progress state — keyed by set_id
// Shape: { correct: [1, 3], revealed: false }
function loadProgress(setId) {
  const key = `rockbusters_progress_${setId}`;
  try {
    const raw = localStorage.getItem(key);
    if (raw) {
      const parsed = JSON.parse(raw);
      // Ensure shape is valid
      return {
        correct: Array.isArray(parsed.correct) ? parsed.correct : [],
        revealed: Boolean(parsed.revealed),
      };
    }
  } catch (_) {
    // Ignore parse errors
  }
  return { correct: [], revealed: false };
}

function saveProgress(setId, state) {
  const key = `rockbusters_progress_${setId}`;
  localStorage.setItem(key, JSON.stringify(state));
}

// ---------------------------------------------------------------------------
// API URL from meta tag
// ---------------------------------------------------------------------------
function getApiUrl() {
  const meta = document.querySelector(`meta[name="${API_URL_ATTR}"]`);
  return meta ? (meta.getAttribute('content') || '') : '';
}

// ---------------------------------------------------------------------------
// API call functions — fire and forget, errors logged only
// ---------------------------------------------------------------------------
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
    list.textContent = 'Leaderboard unavailable.';
    return;
  }

  try {
    const res = await fetch(`${apiUrl}/api/leaderboard`);
    if (!res.ok) throw new Error(`HTTP ${res.status}`);
    const data = await res.json();

    if (!Array.isArray(data) || data.length === 0) {
      list.textContent = 'No scores yet.';
      return;
    }

    list.innerHTML = '';
    data.forEach((entry, idx) => {
      const row = document.createElement('div');
      row.className = 'leaderboard-row';
      row.textContent = `${idx + 1}. ${entry.display_name || 'Anonymous'} — ${entry.score ?? 0}`;
      list.appendChild(row);
    });
  } catch (e) {
    console.warn('Leaderboard fetch failed:', e);
    list.textContent = 'Leaderboard unavailable.';
  }
}

// ---------------------------------------------------------------------------
// Quiz rendering and interaction
// ---------------------------------------------------------------------------

// Module-level variables set during loadQuiz so handlers can access them
let _answerClues = [];
let _progress = null;
let _setId = null;

function renderQuiz(todaySet, answerClues, progress) {
  // Cache for handler use
  _answerClues = answerClues;
  _progress = progress;
  _setId = todaySet.id;

  // Populate metadata
  setText('quiz-title', todaySet.title);
  setText('quiz-date', formatDateBritish(getTodayLondon()));
  setText('quiz-intro', todaySet.intro);
  setText('quiz-prize', todaySet.prize);

  // Populate each clue
  todaySet.clues.forEach(clue => {
    const n = clue.number;
    setText(`clue-${n}`, clue.clue);
    setText(`initials-${n}`, clue.initials);
    setText(`result-${n}`, '');

    // Wire up guess button and Enter key
    const btn = document.getElementById(`guess-btn-${n}`);
    const input = document.getElementById(`guess-input-${n}`);

    if (btn) {
      btn.addEventListener('click', () => handleGuess(n));
    }
    if (input) {
      input.addEventListener('keydown', (e) => {
        if (e.key === 'Enter') handleGuess(n);
      });
    }

    // Restore state for already-correct clues
    if (progress.correct.includes(n)) {
      setResult(n, 'correct', "You've already got that one.");
      disableClue(n);
    }
  });

  // Wire up reveal button
  const revealBtn = document.getElementById('reveal-btn');
  if (revealBtn) {
    revealBtn.addEventListener('click', () => handleReveal());
  }

  // If already revealed, show answers
  if (progress.revealed) {
    showAnswers(answerClues);
    disableAllClues(todaySet.clues);
  }
}

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

function disableAllClues(clues) {
  clues.forEach(clue => disableClue(clue.number));
}

function showAnswers(answerClues) {
  const section = document.getElementById('answers-section');
  if (section) section.style.display = '';

  answerClues.forEach(ac => {
    const el = document.getElementById(`answer-line-${ac.number}`);
    if (el) el.textContent = `${ac.answer}: ${ac.reasoning}`;
  });

  const warning = document.getElementById('answers-warning');
  if (warning) {
    warning.textContent = "You've seen the answers, so you can't score for today's set.";
  }
}

// ---------------------------------------------------------------------------
// handleGuess — called on button click or Enter
// ---------------------------------------------------------------------------
function handleGuess(clueNumber) {
  const progress = _progress;
  const answerClues = _answerClues;
  const setId = _setId;

  if (!progress || !answerClues) return;

  if (progress.revealed) {
    setResult(clueNumber, 'info', "You've seen the answers, so no more points today.");
    return;
  }

  if (progress.correct.includes(clueNumber)) {
    setResult(clueNumber, 'info', "You've already got that one.");
    return;
  }

  const input = document.getElementById(`guess-input-${clueNumber}`);
  const userInput = input ? input.value : '';

  const answerClue = answerClues.find(ac => ac.number === clueNumber);
  if (!answerClue) return;

  if (checkAnswer(answerClue.aliases, userInput)) {
    progress.correct.push(clueNumber);
    saveProgress(setId, progress);
    setResult(clueNumber, 'correct', 'Correct!');
    disableClue(clueNumber);
    postScore(setId, clueNumber); // fire and forget
  } else {
    setResult(clueNumber, 'incorrect', 'Nope. Not having that.');
  }
}

// ---------------------------------------------------------------------------
// handleReveal — called on reveal button click
// ---------------------------------------------------------------------------
function handleReveal() {
  const progress = _progress;
  const answerClues = _answerClues;
  const setId = _setId;

  if (!progress || !answerClues) return;

  progress.revealed = true;
  saveProgress(setId, progress);

  // Get the full set's clues from the rendered data to disable all
  const allClueNumbers = answerClues.map(ac => ac.number);
  allClueNumbers.forEach(n => disableClue(n));

  showAnswers(answerClues);
  postReveal(setId); // fire and forget
}

// ---------------------------------------------------------------------------
// loadQuiz — fetch data, compute today's set, render
// ---------------------------------------------------------------------------
async function loadQuiz() {
  try {
    // Fetch the question data
    const qRes = await fetch('data/rockbusters.json');
    if (!qRes.ok) throw new Error(`Failed to load quiz data: HTTP ${qRes.status}`);
    const allSets = await qRes.json();

    // Filter to enabled sets only
    const enabledSets = allSets.filter(s => s.enabled !== false);
    if (enabledSets.length === 0) throw new Error('No enabled sets found.');

    const todayIndex = getTodaysIndex(enabledSets.length);
    const todaySet = enabledSets[todayIndex];

    // Fetch answer data
    const aRes = await fetch('data/rockbusters-answers.json');
    if (!aRes.ok) throw new Error(`Failed to load answer data: HTTP ${aRes.status}`);
    const allAnswers = await aRes.json();

    // Find matching answer set by id
    const answerSet = allAnswers.find(a => a.id === todaySet.id);
    const answerClues = answerSet ? answerSet.clues : [];

    // Load progress
    const progress = loadProgress(todaySet.id);

    // Render
    renderQuiz(todaySet, answerClues, progress);

    // Load leaderboard (async, non-blocking)
    loadLeaderboard();
  } catch (err) {
    console.error('loadQuiz failed:', err);
    const container = document.getElementById('quiz-container');
    if (container) {
      container.innerHTML = `<p class="error">Failed to load today's quiz. Please try refreshing the page.</p>`;
    }
  }
}

// ---------------------------------------------------------------------------
// initApp — called on DOMContentLoaded
// ---------------------------------------------------------------------------
function initApp() {
  const displayName = getDisplayName();

  if (!displayName) {
    // Show name prompt, hide quiz
    const namePrompt = document.getElementById('name-prompt');
    const quizContainer = document.getElementById('quiz-container');
    if (namePrompt) namePrompt.style.display = '';
    if (quizContainer) quizContainer.style.display = 'none';

    // Wire up name submit button
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
    if (nameInput) {
      nameInput.addEventListener('keydown', (e) => {
        if (e.key === 'Enter') submitName();
      });
    }
  } else {
    // Name already set — go straight to quiz
    const namePrompt = document.getElementById('name-prompt');
    const quizContainer = document.getElementById('quiz-container');
    if (namePrompt) namePrompt.style.display = 'none';
    if (quizContainer) quizContainer.style.display = '';
    loadQuiz();
  }
}

// ---------------------------------------------------------------------------
// Expose to global scope for use by inline HTML handlers (no bundler)
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

// ---------------------------------------------------------------------------
// Auto-initialise when the DOM is ready
// ---------------------------------------------------------------------------
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', initApp);
} else {
  // Already parsed (e.g. script deferred or at end of body)
  initApp();
}
