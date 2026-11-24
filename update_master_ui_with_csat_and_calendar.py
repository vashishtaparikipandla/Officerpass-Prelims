#!/usr/bin/env python3
"""
Updates dashboard/index.html with:
1. CSAT Lab Day Card Enhancement:
   - 25+ difficult UPSC-level practice questions for each topic
   - Expandable arena right inside the day card
   - Hidden answers, instant feedback, child-logic models, step-by-step solutions, Starred Recall integration
2. Current Affairs Calendar View:
   - Switcher between 'Articles & MCQs Feed' and 'Daily Memory Revision Calendar'
   - 6 full-width horizontal rows per day for quick recall keywords/notes
   - Debounced auto-save directly to local disk (data/state.json)
   - Month filters, search across memory points, explicit save buttons
"""

import os
import re

INDEX_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'dashboard', 'index.html')

with open(INDEX_PATH, 'r') as f:
    content = f.read()

# -------------------------------------------------------------------
# 1. NEW CSS STYLES (Insert before </style>)
# -------------------------------------------------------------------
NEW_CSS = """
/* CSAT TOPIC PRACTICE ARENA (25+ QUESTIONS PER TOPIC) */
.csat-arena-toggle-wrap {
  border-top: 1px dashed var(--border);
  padding-top: 14px;
  margin-top: 14px;
}
.csat-arena-deck {
  display: flex;
  flex-direction: column;
  gap: 16px;
  margin-top: 14px;
  padding-top: 14px;
  border-top: 1px solid var(--border);
}
.csat-arena-header {
  background: var(--surface-alt);
  border: 1px solid var(--border);
  border-radius: var(--radius);
  padding: 12px 16px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  flex-wrap: wrap;
  gap: 10px;
}
.csat-mental-model-callout {
  background: #f0fdf4;
  border: 1px solid #bbf7d0;
  border-radius: var(--radius);
  padding: 10px 14px;
  font-size: 12.5px;
  color: #166534;
  font-weight: 600;
  margin-top: 10px;
  display: flex;
  align-items: flex-start;
  gap: 8px;
}
.csat-q-card {
  background: var(--surface-alt);
  border: 1px solid var(--border);
  border-radius: var(--radius);
  padding: 18px;
  transition: border-color 0.15s;
}
.csat-q-card:hover {
  border-color: var(--border-focus);
}
.csat-arena-filter-btn {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: var(--radius-full);
  padding: 4px 12px;
  font-size: 11.5px;
  font-weight: 700;
  color: var(--text-muted);
  cursor: pointer;
  transition: all 0.15s;
}
.csat-arena-filter-btn.active {
  background: var(--primary);
  color: #ffffff;
  border-color: var(--primary);
}

/* CURRENT AFFAIRS MEMORY REVISION CALENDAR VIEW */
.ca-view-switcher {
  display: inline-flex;
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: var(--radius-full);
  padding: 4px;
  gap: 4px;
}
.ca-view-btn {
  padding: 8px 18px;
  border-radius: var(--radius-full);
  font-size: 13px;
  font-weight: 700;
  border: none;
  cursor: pointer;
  background: transparent;
  color: var(--text-muted);
  transition: all 0.15s;
  display: inline-flex;
  align-items: center;
  gap: 6px;
}
.ca-view-btn.active {
  background: var(--primary);
  color: #ffffff;
  box-shadow: 0 1px 3px rgba(37,99,235,0.2);
}
.ca-cal-grid {
  display: flex;
  flex-direction: column;
  gap: 20px;
}
.ca-cal-day-card {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: var(--radius);
  padding: 20px;
  box-shadow: 0 1px 3px rgba(0,0,0,0.03);
}
.ca-cal-day-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
  gap: 10px;
  margin-bottom: 14px;
  padding-bottom: 12px;
  border-bottom: 1px solid var(--border);
}
.ca-cal-date-title {
  font-size: 15px;
  font-weight: 800;
  color: var(--text-main);
  display: flex;
  align-items: center;
  gap: 8px;
}
.ca-cal-rows-list {
  display: flex;
  flex-direction: column;
  gap: 9px;
}
.ca-cal-row-item {
  display: flex;
  align-items: center;
  gap: 10px;
  width: 100%;
}
.ca-cal-row-num {
  font-size: 12px;
  font-weight: 800;
  color: var(--text-muted);
  width: 24px;
  text-align: right;
  flex-shrink: 0;
}
.ca-cal-row-input {
  flex: 1;
  width: 100%;
  background: var(--surface-alt);
  border: 1px solid var(--border);
  border-radius: 6px;
  padding: 10px 14px;
  font-size: 13.5px;
  color: var(--text-main);
  font-family: inherit;
  transition: all 0.15s;
}
.ca-cal-row-input:focus {
  outline: none;
  background: #ffffff;
  border-color: var(--border-focus);
  box-shadow: 0 0 0 3px rgba(37,99,235,0.1);
}
@media (max-width: 768px) {
  .ca-cal-row-input {
    font-size: 16px !important;
    padding: 11px 12px;
  }
}
"""

if "/* CSAT TOPIC PRACTICE ARENA" not in content:
    content = content.replace("</style>", f"{NEW_CSS}\n</style>")

# -------------------------------------------------------------------
# 2. CURRENT AFFAIRS VIEW SWITCHER IN #content-news
# -------------------------------------------------------------------
CA_VIEW_HEADER = """  <!-- TAB 3: CURRENT AFFAIRS FEED & MEMORY REVISION CALENDAR -->
  <section class="tab-content" id="content-news">
    <!-- Top View Switcher -->
    <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:12px; margin-bottom:18px;">
      <div class="ca-view-switcher">
        <button class="ca-view-btn active" id="btn-ca-view-feed" onclick="switchCAView('feed')">
          <svg class="icon-svg" width="15" height="15" viewBox="0 0 24 24"><path d="M4 22h16a2 2 0 0 0 2-2V4a2 2 0 0 0-2-2H8a2 2 0 0 0-2 2v16a2 2 0 0 1-2 2Zm0 0a2 2 0 0 1-2-2v-9c0-1.1.9-2 2-2h2"></path><path d="M18 14h-8"></path><path d="M15 18h-5"></path><path d="M10 6h8v4h-8V6Z"></path></svg>
          Articles & MCQs Feed
        </button>
        <button class="ca-view-btn" id="btn-ca-view-calendar" onclick="switchCAView('calendar')">
          <svg class="icon-svg" width="15" height="15" viewBox="0 0 24 24"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"></rect><line x1="16" y1="2" x2="16" y2="6"></line><line x1="8" y1="2" x2="8" y2="6"></line><line x1="3" y1="10" x2="21" y2="10"></line></svg>
          Daily Memory Revision Calendar
        </button>
      </div>

      <div id="ca-cal-save-indicator" style="display:none; font-size:12.5px; font-weight:700; color:#16a34a; align-items:center; gap:6px;">
        <svg class="icon-svg" width="14" height="14" viewBox="0 0 24 24" style="stroke:#16a34a;"><polyline points="20 6 9 17 4 12"></polyline></svg>
        <span id="ca-cal-save-text">Auto-Saved to Local Disk</span>
      </div>
    </div>

    <!-- SUB-VIEW 1: ARTICLES FEED -->
    <div id="ca-feed-subview">"""

OLD_CA_START = """  <!-- TAB 3: CURRENT AFFAIRS FEED -->
  <section class="tab-content" id="content-news">"""

if "btn-ca-view-calendar" not in content and OLD_CA_START in content:
    content = content.replace(OLD_CA_START, CA_VIEW_HEADER)
    # Now close ca-feed-subview and insert ca-calendar-subview before closing section
    CA_CAL_SUBVIEW = """    </div><!-- /#ca-feed-subview -->

    <!-- SUB-VIEW 2: DAILY MEMORY REVISION CALENDAR -->
    <div id="ca-calendar-subview" style="display:none;">
      <div class="ca-controls-bar" style="margin-bottom:20px;">
        <div class="ca-search-row">
          <input type="text" id="ca-cal-search-input" class="ca-search-input" placeholder="Search keywords across your daily memory notes (e.g. CRR, Article 324, Great Indian Bustard...)" oninput="onCAMemorySearch(this.value)">
          <select id="ca-cal-month-filter" class="ca-filter-select" onchange="onCAMemoryMonthChange(this.value)">
            <option value="all">All Months (180 Days)</option>
            <option value="Nov 2026">November 2026</option>
            <option value="Dec 2026">December 2026</option>
            <option value="Jan 2027">January 2027</option>
            <option value="Feb 2027">February 2027</option>
            <option value="Mar 2027">March 2027</option>
            <option value="Apr 2027">April 2027</option>
            <option value="May 2027">May 2027</option>
          </select>
          <button class="ca-refresh-btn" onclick="saveAllCAMemoryNotes()" style="background:var(--primary); color:#ffffff; border:none;">
            <svg class="icon-svg" width="14" height="14" viewBox="0 0 24 24" style="stroke:#ffffff;"><path d="M19 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h11l5 5v11a2 2 0 0 1-2 2z"></path><polyline points="17 21 17 13 7 13 7 21"></polyline><polyline points="7 3 7 8 15 8"></polyline></svg>
            Save All Memory Notes
          </button>
        </div>
      </div>

      <!-- Information Callout -->
      <div style="background:var(--surface); border:1px solid var(--border); border-radius:var(--radius); padding:14px 18px; margin-bottom:18px; font-size:13px; color:var(--text-body); display:flex; align-items:center; justify-content:space-between; flex-wrap:wrap; gap:10px;">
        <div style="display:flex; align-items:center; gap:8px;">
          <svg class="icon-svg" width="18" height="18" viewBox="0 0 24 24" style="stroke:var(--primary);"><circle cx="12" cy="12" r="10"></circle><line x1="12" y1="16" x2="12" y2="12"></line><line x1="12" y1="8" x2="12.01" y2="8"></line></svg>
          <span><strong>Rapid Recall Deck</strong>: Record 5 to 6 horizontal key points per day after reading news. Each row auto-saves to your local disk so you can recall every theme before UPSC Prelims 2027.</span>
        </div>
        <div id="ca-cal-stats-badge" class="candidate-badge">0 Days Documented</div>
      </div>

      <!-- Daily Memory Cards List -->
      <div class="ca-cal-grid" id="ca-calendar-container">
        <!-- Rendered via JS -->
      </div>
    </div><!-- /#ca-calendar-subview -->
  </section>"""
    content = content.replace("    <!-- CA Articles Feed Grid -->\n    <div class=\"ca-articles-grid\" id=\"ca-articles-container\">\n      <!-- Rendered via JS -->\n    </div>\n  </section>", f"    <!-- CA Articles Feed Grid -->\n    <div class=\"ca-articles-grid\" id=\"ca-articles-container\">\n      <!-- Rendered via JS -->\n    </div>\n{CA_CAL_SUBVIEW}")

# -------------------------------------------------------------------
# 3. JAVASCRIPT LOGIC ENHANCEMENT
# -------------------------------------------------------------------

JS_ENHANCEMENT = """
// ===================================================================
// CSAT LAB 25+ QUESTIONS ARENA ENGINE & CA MEMORY CALENDAR LOGIC
// ===================================================================

function escapeHtml(str) {
  if (!str) return '';
  return String(str)
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&#039;');
}

let csatArenaCache = {};
let activeCSATArenaFilters = {};
let caMemoryCalendarSearchTerm = '';
let caMemoryCalendarMonth = 'all';
let caMemoryDebounceTimer = null;
let currentCAViewMode = 'feed'; // 'feed' | 'calendar'

// 1. View Switcher for Current Affairs
function switchCAView(mode) {
  currentCAViewMode = mode;
  const feedBtn = document.getElementById('btn-ca-view-feed');
  const calBtn = document.getElementById('btn-ca-view-calendar');
  const feedView = document.getElementById('ca-feed-subview');
  const calView = document.getElementById('ca-calendar-subview');
  const saveIndicator = document.getElementById('ca-cal-save-indicator');

  if (mode === 'calendar') {
    feedBtn.classList.remove('active');
    calBtn.classList.add('active');
    feedView.style.display = 'none';
    calView.style.display = 'block';
    if (saveIndicator) saveIndicator.style.display = 'inline-flex';
    renderCAMemoryCalendar();
  } else {
    calBtn.classList.remove('active');
    feedBtn.classList.add('active');
    calView.style.display = 'none';
    feedView.style.display = 'block';
    if (saveIndicator) saveIndicator.style.display = 'none';
    renderCAList();
  }
}

// 2. Render Current Affairs Daily Memory Calendar (5-6 Horizontal Rows)
function renderCAMemoryCalendar() {
  const container = document.getElementById('ca-calendar-container');
  if (!container) return;
  container.innerHTML = '';

  if (!userState.ca_memory_calendar) {
    userState.ca_memory_calendar = {};
  }

  // Build list of all 180 curriculum days or distinct dates
  let daysList = allCurriculum || [];

  // Filter by Month
  if (caMemoryCalendarMonth !== 'all') {
    daysList = daysList.filter(d => (d.date || '').includes(caMemoryCalendarMonth) || (d.date_display || '').includes(caMemoryCalendarMonth));
  }

  // Filter by Search Query in saved rows
  if (caMemoryCalendarSearchTerm.trim()) {
    const q = caMemoryCalendarSearchTerm.toLowerCase();
    daysList = daysList.filter(d => {
      const savedRows = userState.ca_memory_calendar[d.date] || [];
      const matchInRows = savedRows.some(r => (r || '').toLowerCase().includes(q));
      const matchInDate = (d.date || '').toLowerCase().includes(q) || (d.date_display || '').toLowerCase().includes(q);
      const matchInTopic = (d.topic_title || '').toLowerCase().includes(q);
      return matchInRows || matchInDate || matchInTopic;
    });
  }

  let totalFilledDays = 0;
  Object.keys(userState.ca_memory_calendar).forEach(k => {
    const rows = userState.ca_memory_calendar[k] || [];
    if (rows.some(r => (r || '').trim().length > 0)) totalFilledDays++;
  });

  const statsBadge = document.getElementById('ca-cal-stats-badge');
  if (statsBadge) statsBadge.textContent = `${totalFilledDays} Days Documented`;

  if (daysList.length === 0) {
    container.innerHTML = `
      <div style="padding:40px; text-align:center; color:var(--text-muted); background:var(--surface); border-radius:var(--radius); border:1px solid var(--border);">
        <p style="font-size:15px; font-weight:700; color:var(--text-main);">No calendar days match criteria "${caMemoryCalendarSearchTerm}".</p>
      </div>
    `;
    return;
  }

  daysList.forEach(day => {
    const card = document.createElement('div');
    card.className = 'ca-cal-day-card';

    const dateKey = day.date;
    const existingRows = userState.ca_memory_calendar[dateKey] || ['', '', '', '', '', ''];
    // Ensure at least 6 rows exist
    while (existingRows.length < 6) existingRows.push('');

    const placeholders = [
      'Key Point 1: Polity / Constitutional rule / Supreme Court doctrine...',
      'Key Point 2: Economy / RBI notification / Macro fiscal indicator...',
      'Key Point 3: Environment / Protected Area / Species IUCN status / Treaty...',
      'Key Point 4: Science & Tech / Space mission / Biotech / Defence tech...',
      'Key Point 5: International Relations / Map location / Geopolitical chokepoint...',
      'Key Point 6: Rapid Recall hook / Static linkage / Confusing trap...'
    ];

    let rowsHtml = '';
    existingRows.forEach((val, idx) => {
      const pl = idx < placeholders.length ? placeholders[idx] : `Additional Key Point ${idx + 1}...`;
      rowsHtml += `
        <div class="ca-cal-row-item" id="ca-cal-row-${dateKey}-${idx}">
          <div class="ca-cal-row-num">${idx + 1}.</div>
          <input type="text" class="ca-cal-row-input" 
            placeholder="${pl}" 
            value="${escapeHtml(val)}" 
            data-date="${dateKey}" 
            data-row="${idx}" 
            oninput="handleCAMemoryInput('${dateKey}', ${idx}, this.value)"
            onchange="saveState()"
          >
        </div>
      `;
    });

    const filledCount = existingRows.filter(r => (r || '').trim().length > 0).length;

    card.innerHTML = `
      <div class="ca-cal-day-header">
        <div class="ca-cal-date-title">
          <svg class="icon-svg" width="16" height="16" viewBox="0 0 24 24" style="stroke:var(--primary);"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"></rect><line x1="16" y1="2" x2="16" y2="6"></line><line x1="8" y1="2" x2="8" y2="6"></line><line x1="3" y1="10" x2="21" y2="10"></line></svg>
          <span>Day ${day.day} • ${day.date_display || day.date}</span>
          <span style="font-size:12px; font-weight:600; color:var(--text-muted); margin-left:6px;">(${day.topic_title.substring(0, 32)}...)</span>
        </div>
        <div style="display:flex; align-items:center; gap:8px;">
          <span class="candidate-badge" id="ca-cal-count-${dateKey}" style="font-size:11px;">
            ${filledCount} / ${existingRows.length} Points
          </span>
          <button class="target-action-btn" onclick="addCAMemoryRow('${dateKey}')" style="margin-top:0; padding:4px 10px; font-size:11.5px;">
            + Add Row
          </button>
          <button class="btn-icon" onclick="saveState(); showSaveToast('Day ${day.day} memory notes saved.');" style="padding:4px 10px; font-size:11.5px; border-radius:var(--radius-full);">
            Save
          </button>
        </div>
      </div>

      <div class="ca-cal-rows-list" id="ca-cal-rows-list-${dateKey}">
        ${rowsHtml}
      </div>
    `;

    container.appendChild(card);
  });
}

function handleCAMemoryInput(dateKey, rowIdx, val) {
  if (!userState.ca_memory_calendar) userState.ca_memory_calendar = {};
  if (!userState.ca_memory_calendar[dateKey]) userState.ca_memory_calendar[dateKey] = ['', '', '', '', '', ''];
  
  userState.ca_memory_calendar[dateKey][rowIdx] = val;

  // Update badge count
  const badge = document.getElementById(`ca-cal-count-${dateKey}`);
  if (badge) {
    const filled = userState.ca_memory_calendar[dateKey].filter(r => (r || '').trim().length > 0).length;
    badge.textContent = `${filled} / ${userState.ca_memory_calendar[dateKey].length} Points`;
  }

  // Debounced auto-save
  const indicator = document.getElementById('ca-cal-save-text');
  if (indicator) indicator.textContent = 'Saving to disk...';
  
  clearTimeout(caMemoryDebounceTimer);
  caMemoryDebounceTimer = setTimeout(() => {
    saveState();
    if (indicator) indicator.textContent = 'Auto-Saved to Local Disk';
  }, 750);
}

function addCAMemoryRow(dateKey) {
  if (!userState.ca_memory_calendar) userState.ca_memory_calendar = {};
  if (!userState.ca_memory_calendar[dateKey]) userState.ca_memory_calendar[dateKey] = ['', '', '', '', '', ''];
  
  const newIdx = userState.ca_memory_calendar[dateKey].length;
  userState.ca_memory_calendar[dateKey].push('');

  const listContainer = document.getElementById(`ca-cal-rows-list-${dateKey}`);
  if (listContainer) {
    const div = document.createElement('div');
    div.className = 'ca-cal-row-item';
    div.id = `ca-cal-row-${dateKey}-${newIdx}`;
    div.innerHTML = `
      <div class="ca-cal-row-num">${newIdx + 1}.</div>
      <input type="text" class="ca-cal-row-input" 
        placeholder="Additional Key Point ${newIdx + 1}..." 
        value="" 
        data-date="${dateKey}" 
        data-row="${newIdx}" 
        oninput="handleCAMemoryInput('${dateKey}', ${newIdx}, this.value)"
        onchange="saveState()"
      >
    `;
    listContainer.appendChild(div);
  }
  saveState();
}

function saveAllCAMemoryNotes() {
  saveState();
  showSaveToast('All daily memory notes successfully saved to local disk.');
}

function onCAMemorySearch(val) {
  caMemoryCalendarSearchTerm = val;
  renderCAMemoryCalendar();
}

function onCAMemoryMonthChange(val) {
  caMemoryCalendarMonth = val;
  renderCAMemoryCalendar();
}

function showSaveToast(msg) {
  const ind = document.getElementById('ca-cal-save-text');
  if (ind) {
    ind.textContent = `✓ ${msg}`;
    setTimeout(() => {
      ind.textContent = 'Auto-Saved to Local Disk';
    }, 2500);
  }
}

// -------------------------------------------------------------------
// 3. CSAT LAB 25+ QUESTIONS ARENA PER DAY CARD
// -------------------------------------------------------------------
async function toggleCSATArena(dayNum) {
  const deck = document.getElementById(`csat-arena-deck-${dayNum}`);
  const btnText = document.getElementById(`csat-arena-btn-text-${dayNum}`);
  if (!deck) return;

  if (deck.style.display === 'none' || deck.style.display === '') {
    deck.style.display = 'block';
    if (btnText) btnText.textContent = 'Close Questions';
    await loadAndRenderCSATArena(dayNum);
  } else {
    deck.style.display = 'none';
    if (btnText) btnText.textContent = 'Open 26 Questions';
  }
}

async function loadAndRenderCSATArena(dayNum) {
  const deck = document.getElementById(`csat-arena-deck-${dayNum}`);
  if (!deck) return;

  if (!csatArenaCache[dayNum]) {
    deck.innerHTML = `
      <div style="padding:20px; text-align:center; color:var(--text-muted); font-size:13px;">
        Loading 26 UPSC-level questions for Day ${dayNum}...
      </div>
    `;
    try {
      const res = await fetch(`/api/csat/questions?day=${dayNum}`);
      if (res.ok) {
        csatArenaCache[dayNum] = await res.json();
      }
    } catch (e) {
      console.error('Failed to load CSAT questions:', e);
    }
  }

  const topicData = csatArenaCache[dayNum];
  if (!topicData || !topicData.questions) {
    deck.innerHTML = `
      <div style="padding:20px; text-align:center; color:var(--text-muted); font-size:13px;">
        Questions for this topic could not be loaded. Please ensure server is running.
      </div>
    `;
    return;
  }

  renderCSATArenaDeck(dayNum, topicData);
}

function renderCSATArenaDeck(dayNum, topicData) {
  const deck = document.getElementById(`csat-arena-deck-${dayNum}`);
  if (!deck) return;

  const currentFilter = activeCSATArenaFilters[dayNum] || 'all';
  let questions = topicData.questions || [];

  if (currentFilter === 'pyq') {
    questions = questions.filter(q => !q.is_predictor_2027);
  } else if (currentFilter === 'predictor') {
    questions = questions.filter(q => !!q.is_predictor_2027);
  } else if (currentFilter === 'unsolved') {
    questions = questions.filter(q => !userState.mcq_answers[q.id]);
  } else if (currentFilter === 'starred') {
    questions = questions.filter(q => !!userState.starred_mcqs[q.id]);
  }

  const totalQs = topicData.questions.length;
  const answeredInTopic = topicData.questions.filter(q => !!userState.mcq_answers[q.id]).length;
  let correctInTopic = 0;
  topicData.questions.forEach(q => {
    if (userState.mcq_answers[q.id]) {
      const chosen = userState.mcq_answers[q.id].toLowerCase();
      const cor = (q.answer || '').replace(/[()]/g, '').toLowerCase();
      if (chosen === cor) correctInTopic++;
    }
  });

  // Update status pill on parent card
  const statusPill = document.getElementById(`csat-arena-pill-${dayNum}`);
  if (statusPill) {
    statusPill.textContent = `${answeredInTopic} / ${totalQs} Solved (${correctInTopic} Correct)`;
    statusPill.style.color = answeredInTopic === totalQs ? '#16a34a' : 'var(--primary)';
  }

  let questionsHtml = '';
  questions.forEach(q => {
    const isStarred = !!userState.starred_mcqs[q.id];
    const userSelected = userState.mcq_answers[q.id] || null;
    const correctLetter = (q.answer || '').replace(/[()]/g, '').trim().toLowerCase();

    const optionsHtml = (q.options || []).map(optStr => {
      const m = optStr.match(/^\(([a-d])\)\s*(.*)/i);
      const letter = m ? m[1].toLowerCase() : '';
      const text = m ? m[2] : optStr;

      let btnClass = 'mcq-opt-btn';
      if (userSelected) {
        if (letter === userSelected) {
          btnClass += letter === correctLetter ? ' correct' : ' wrong';
        } else if (letter === correctLetter) {
          btnClass += ' correct';
        }
      }

      return `
        <button class="${btnClass}" onclick="selectCSATArenaOption('${q.id}', '${letter}', '${correctLetter}', ${dayNum})">
          <span class="mcq-opt-letter">(${letter.toUpperCase()})</span>
          <span class="mcq-opt-text">${escapeHtml(text)}</span>
        </button>
      `;
    }).join('');

    const isAnswered = !!userSelected;

    questionsHtml += `
      <div class="csat-q-card" id="csat-card-${q.id}">
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:10px;">
          <div style="display:flex; align-items:center; gap:8px;">
            <span class="year-badge-pill">${q.year_tag || '[UPSC CSAT]'}</span>
            <span class="prob-badge" style="background:${q.is_predictor_2027 ? '#fef3c7' : 'var(--surface)'}; color:${q.is_predictor_2027 ? '#92400e' : 'var(--text-muted)'}; border-color:${q.is_predictor_2027 ? '#fde68a' : 'var(--border)'};">
              ${q.difficulty || 'UPSC Hard'}
            </span>
            <span style="font-size:12px; font-weight:700; color:var(--text-muted);">Q${q.index} of ${totalQs}</span>
          </div>
          <button class="star-btn ${isStarred ? 'starred' : ''}" onclick="toggleStarMCQ('${q.id}', this)" title="Save to Starred Recall Deck">
            <svg viewBox="0 0 24 24"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon></svg>
          </button>
        </div>

        <div style="font-size:14px; font-weight:600; line-height:1.5; color:var(--text-main); margin-bottom:14px; white-space:pre-line;">${escapeHtml(q.q)}</div>

        <div class="mcq-options-grid">
          ${optionsHtml}
        </div>

        <!-- 6th-Grade Child Logic & Derivation Box -->
        <div class="mcq-explanation-box ${isAnswered ? 'visible' : ''}" id="csat-expl-${q.id}">
          <div class="expl-header">
            <svg class="icon-svg" width="16" height="16" viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"></circle><line x1="12" y1="16" x2="12" y2="12"></line><line x1="12" y1="8" x2="12.01" y2="8"></line></svg>
            <strong>Official Correct Answer: (${correctLetter.toUpperCase()})</strong>
          </div>
          <div class="expl-body">
            <div style="background:#f0fdf4; border:1px solid #bbf7d0; border-radius:6px; padding:10px 12px; margin-bottom:10px; font-size:12.5px; color:#166534;">
              <strong>Intuitive Child-Logic:</strong> ${escapeHtml(q.child_logic || '')}
            </div>
            <div style="font-size:12.5px; line-height:1.6; color:var(--text-body); white-space:pre-line;">
              ${escapeHtml(q.explanation || '')}
            </div>
          </div>
        </div>
      </div>
    `;
  });

  deck.innerHTML = `
    <!-- Mental Model Callout -->
    <div class="csat-mental-model-callout">
      <svg class="icon-svg" width="18" height="18" viewBox="0 0 24 24" style="stroke:#16a34a; flex-shrink:0; margin-top:2px;"><circle cx="12" cy="12" r="10"></circle><line x1="12" y1="16" x2="12" y2="12"></line><line x1="12" y1="8" x2="12.01" y2="8"></line></svg>
      <div>
        <strong>6th-Grade Intuition Model:</strong> ${escapeHtml(topicData.mental_model || '')}
      </div>
    </div>

    <!-- Arena Header Controls -->
    <div class="csat-arena-header">
      <div style="display:flex; align-items:center; gap:6px; flex-wrap:wrap;">
        <button class="csat-arena-filter-btn ${currentFilter === 'all' ? 'active' : ''}" onclick="filterCSATArena(${dayNum}, 'all')">All Questions (${totalQs})</button>
        <button class="csat-arena-filter-btn ${currentFilter === 'pyq' ? 'active' : ''}" onclick="filterCSATArena(${dayNum}, 'pyq')">Official PYQs</button>
        <button class="csat-arena-filter-btn ${currentFilter === 'predictor' ? 'active' : ''}" onclick="filterCSATArena(${dayNum}, 'predictor')">2027 Predictors</button>
        <button class="csat-arena-filter-btn ${currentFilter === 'unsolved' ? 'active' : ''}" onclick="filterCSATArena(${dayNum}, 'unsolved')">Unsolved</button>
        <button class="csat-arena-filter-btn ${currentFilter === 'starred' ? 'active' : ''}" onclick="filterCSATArena(${dayNum}, 'starred')">Starred</button>
      </div>

      <div style="font-size:12px; font-weight:700; color:var(--text-main);">
        Score: <span style="color:var(--primary); font-size:13.5px;">${correctInTopic}</span> / ${answeredInTopic} answered
      </div>
    </div>

    <!-- Questions Deck -->
    <div class="csat-arena-deck">
      ${questionsHtml}
    </div>
  `;
}

function filterCSATArena(dayNum, filterType) {
  activeCSATArenaFilters[dayNum] = filterType;
  if (csatArenaCache[dayNum]) {
    renderCSATArenaDeck(dayNum, csatArenaCache[dayNum]);
  }
}

function selectCSATArenaOption(qId, selectedLetter, correctLetter, dayNum) {
  userState.mcq_answers[qId] = selectedLetter;
  saveState();

  const card = document.getElementById(`csat-card-${qId}`);
  if (!card) return;

  const buttons = card.querySelectorAll('.mcq-opt-btn');
  buttons.forEach(btn => {
    const text = btn.innerText || '';
    const m = text.match(/^\(([a-d])\)/i);
    const l = m ? m[1].toLowerCase() : '';

    btn.classList.remove('correct', 'wrong');
    if (l === selectedLetter) {
      btn.classList.add(selectedLetter === correctLetter ? 'correct' : 'wrong');
    } else if (l === correctLetter) {
      btn.classList.add('correct');
    }
  });

  const expl = document.getElementById(`csat-expl-${qId}`);
  if (expl) expl.classList.add('visible');

  // Re-render header stats
  if (csatArenaCache[dayNum]) {
    const topicData = csatArenaCache[dayNum];
    const totalQs = topicData.questions.length;
    const answered = topicData.questions.filter(q => !!userState.mcq_answers[q.id]).length;
    let correct = 0;
    topicData.questions.forEach(q => {
      if (userState.mcq_answers[q.id] && userState.mcq_answers[q.id].toLowerCase() === (q.answer || '').replace(/[()]/g, '').toLowerCase()) {
        correct++;
      }
    });
    const statusPill = document.getElementById(`csat-arena-pill-${dayNum}`);
    if (statusPill) {
      statusPill.textContent = `${answered} / ${totalQs} Solved (${correct} Correct)`;
    }
  }
}
"""

if "function switchCAView" not in content:
    content = content.replace("async function loadState() {", f"{JS_ENHANCEMENT}\n\nasync function loadState() {{")

# Also ensure loadState handles ca_memory_calendar
OLD_LOAD_STATE = """      userState = {
        checks: data.checks || {},
        sub_checks: data.sub_checks || {},
        notes: data.notes || {},
        read_articles: data.read_articles || {},
        starred_mcqs: data.starred_mcqs || {},
        mcq_answers: data.mcq_answers || {}
      };"""

NEW_LOAD_STATE = """      userState = {
        checks: data.checks || {},
        sub_checks: data.sub_checks || {},
        notes: data.notes || {},
        read_articles: data.read_articles || {},
        starred_mcqs: data.starred_mcqs || {},
        mcq_answers: data.mcq_answers || {},
        ca_memory_calendar: data.ca_memory_calendar || {}
      };"""

if OLD_LOAD_STATE in content:
    content = content.replace(OLD_LOAD_STATE, NEW_LOAD_STATE)

# -------------------------------------------------------------------
# 4. ENHANCE CSAT DAY CARD IN renderCSATDaily()
# -------------------------------------------------------------------
OLD_CSAT_CARD_FOOTER = """      <div style="display:flex; align-items:center; justify-content:space-between; border-top:1px solid var(--border); padding-top:12px;">
        <span style="font-size:12px; color:var(--text-muted);">Concurrent GS: ${day.topic_title.substring(0, 38)}...</span>
        <button class="target-action-btn" onclick="jumpToDay(${day.day}); switchTab('today');" style="margin-top:0;">
          Jump to Day ${day.day} Focus
        </button>
      </div>"""

NEW_CSAT_CARD_FOOTER = """      <div style="display:flex; align-items:center; justify-content:space-between; border-top:1px solid var(--border); padding-top:12px;">
        <span style="font-size:12px; color:var(--text-muted);">Concurrent GS: ${day.topic_title.substring(0, 38)}...</span>
        <button class="target-action-btn" onclick="jumpToDay(${day.day}); switchTab('today');" style="margin-top:0;">
          Jump to Day ${day.day} Focus
        </button>
      </div>

      <!-- 25+ Topic Practice Questions Arena -->
      <div class="csat-arena-toggle-wrap">
        <div style="display:flex; align-items:center; justify-content:space-between; flex-wrap:wrap; gap:8px;">
          <div style="display:flex; align-items:center; gap:8px;">
            <span style="font-size:12px; font-weight:800; color:var(--text-main);">Topic Question Bank:</span>
            <span class="csat-arena-pill" id="csat-arena-pill-${day.day}" style="font-size:11.5px; font-weight:700; background:var(--surface-alt); padding:3px 9px; border-radius:var(--radius-full); border:1px solid var(--border); color:var(--text-muted);">
              26 UPSC-Level Questions
            </span>
          </div>
          <button class="target-action-btn" onclick="toggleCSATArena(${day.day})" id="csat-arena-btn-${day.day}" style="margin-top:0; padding:6px 14px; font-size:12px; display:inline-flex; align-items:center; gap:6px;">
            <svg class="icon-svg" width="13" height="13" viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"></circle><polygon points="10 8 16 12 10 16 10 8"></polygon></svg>
            <span id="csat-arena-btn-text-${day.day}">Open 26 Questions</span>
          </button>
        </div>

        <div id="csat-arena-deck-${day.day}" class="csat-day-arena-deck" style="display:none;">
          <!-- Dynamically populated when opened -->
        </div>
      </div>"""

if OLD_CSAT_CARD_FOOTER in content:
    content = content.replace(OLD_CSAT_CARD_FOOTER, NEW_CSAT_CARD_FOOTER)

with open(INDEX_PATH, 'w') as f:
    f.write(content)

print(f"[UI UPDATER] Successfully updated {INDEX_PATH} with CSAT 25+ Arena and CA Memory Calendar!")
