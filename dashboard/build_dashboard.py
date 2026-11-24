import json
import os

with open('/Users/vashishtaparikipandla/Documents/OfficerPass/micro-topics/microtopics-db.json') as f:
    topics_db = json.load(f)

with open('/Users/vashishtaparikipandla/Documents/OfficerPass/practice-tests/micro-topics/polity-parliament-50q.json') as f:
    quiz_db = json.load(f)

topics_json_str = json.dumps(topics_db)
quiz_json_str = json.dumps(quiz_db)

html_template = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no" />
<title>OfficerPass — UPSC Prelims 2027 Mission Control</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@600;700&family=Plus+Jakarta+Sans:wght@400;500;600;700&family=JetBrains+Mono:wght@400;600&display=swap" rel="stylesheet">
<style>
:root {{
  --bg-primary: #0b0f19;
  --bg-secondary: #111827;
  --bg-card: #1a2234;
  --bg-card-hover: #222d42;
  --border: #2a364f;
  --gold: #d4af37;
  --gold-glow: rgba(212, 175, 55, 0.2);
  --gold-light: #f3e5ab;
  --text-main: #f3f4f6;
  --text-muted: #9ca3af;
  --accent-blue: #3b82f6;
  --accent-green: #10b981;
  --accent-red: #ef4444;
  --tier1: #f59e0b;
  --tier2: #3b82f6;
  --tier3: #6b7280;
}}
* {{ box-sizing: border-box; margin: 0; padding: 0; -webkit-tap-highlight-color: transparent; }}
body {{
  font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
  background: var(--bg-primary);
  color: var(--text-main);
  min-height: 100vh;
  line-height: 1.5;
  padding-bottom: 80px;
}}
header {{
  background: rgba(17, 24, 39, 0.85);
  backdrop-filter: blur(12px);
  border-bottom: 1px solid var(--border);
  position: sticky;
  top: 0;
  z-index: 50;
  padding: 12px 16px;
}}
.header-container {{
  max-width: 1200px;
  margin: 0 auto;
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
  gap: 12px;
}}
.logo-box {{
  display: flex;
  align-items: center;
  gap: 10px;
}}
.badge-gold {{
  background: linear-gradient(135deg, #d4af37, #aa820a);
  color: #0b0f19;
  font-weight: 700;
  padding: 4px 8px;
  border-radius: 6px;
  font-size: 11px;
  letter-spacing: 0.5px;
}}
h1 {{
  font-family: 'Cinzel', serif;
  font-size: 18px;
  color: var(--gold-light);
  letter-spacing: 1px;
}}
.timer-pill {{
  background: rgba(59, 130, 246, 0.15);
  border: 1px solid rgba(59, 130, 246, 0.4);
  color: #93c5fd;
  padding: 6px 12px;
  border-radius: 20px;
  font-size: 12px;
  font-family: 'JetBrains Mono', monospace;
  display: flex;
  align-items: center;
  gap: 6px;
}}
.nav-tabs {{
  max-width: 1200px;
  margin: 12px auto 0;
  display: flex;
  gap: 8px;
  overflow-x: auto;
  padding-bottom: 4px;
}}
.tab-btn {{
  background: var(--bg-secondary);
  border: 1px solid var(--border);
  color: var(--text-muted);
  padding: 8px 16px;
  border-radius: 24px;
  font-size: 13px;
  font-weight: 600;
  cursor: pointer;
  white-space: nowrap;
  transition: all 0.2s;
}}
.tab-btn.active {{
  background: var(--gold);
  color: #0b0f19;
  border-color: var(--gold);
}}
.main-container {{
  max-width: 1200px;
  margin: 16px auto;
  padding: 0 16px;
}}
.hero-stats {{
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
  gap: 12px;
  margin-bottom: 20px;
}}
.stat-card {{
  background: var(--bg-card);
  border: 1px solid var(--border);
  border-radius: 12px;
  padding: 16px;
  display: flex;
  flex-direction: column;
  gap: 6px;
}}
.stat-card h3 {{
  font-size: 12px;
  text-transform: uppercase;
  color: var(--text-muted);
  letter-spacing: 0.5px;
}}
.stat-card .val {{
  font-size: 26px;
  font-weight: 700;
  color: var(--gold-light);
  font-family: 'JetBrains Mono', monospace;
}}
.stat-card .sub {{
  font-size: 12px;
  color: var(--accent-green);
}}
.progress-bar-wrap {{
  width: 100%;
  height: 8px;
  background: #252e42;
  border-radius: 4px;
  overflow: hidden;
  margin-top: 4px;
}}
.progress-bar-fill {{
  height: 100%;
  background: linear-gradient(90deg, #d4af37, #10b981);
  width: 0%;
  transition: width 0.4s ease;
}}
.filter-bar {{
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
  gap: 10px;
  margin-bottom: 16px;
  background: var(--bg-secondary);
  padding: 12px 16px;
  border-radius: 10px;
  border: 1px solid var(--border);
}}
.toggle-btn {{
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: 13px;
  font-weight: 600;
  color: var(--gold);
  cursor: pointer;
  user-select: none;
}}
.subj-chips {{
  display: flex;
  gap: 6px;
  overflow-x: auto;
  padding: 2px 0;
}}
.chip {{
  background: var(--bg-card);
  border: 1px solid var(--border);
  color: var(--text-muted);
  padding: 4px 10px;
  border-radius: 14px;
  font-size: 12px;
  cursor: pointer;
}}
.chip.active {{
  background: rgba(212, 175, 55, 0.15);
  border-color: var(--gold);
  color: var(--gold-light);
}}
.topic-card {{
  background: var(--bg-card);
  border: 1px solid var(--border);
  border-radius: 12px;
  padding: 16px;
  margin-bottom: 12px;
  transition: transform 0.15s, border-color 0.15s;
}}
.topic-card:hover {{
  border-color: rgba(212, 175, 55, 0.4);
}}
.topic-header {{
  display: flex;
  align-items: flex-start;
  gap: 12px;
}}
.custom-checkbox {{
  width: 22px;
  height: 22px;
  accent-color: var(--gold);
  cursor: pointer;
  margin-top: 2px;
}}
.topic-body {{
  flex: 1;
}}
.topic-title {{
  font-size: 15px;
  font-weight: 600;
  color: var(--text-main);
  margin-bottom: 6px;
}}
.topic-title.done {{
  text-decoration: line-through;
  color: var(--text-muted);
}}
.prob-badge {{
  display: inline-block;
  font-size: 11px;
  font-weight: 700;
  padding: 2px 8px;
  border-radius: 4px;
  margin-right: 6px;
}}
.prob-tier1 {{ background: rgba(245, 158, 11, 0.2); color: #fbbf24; border: 1px solid #f59e0b; }}
.prob-tier2 {{ background: rgba(59, 130, 246, 0.2); color: #93c5fd; border: 1px solid #3b82f6; }}
.prob-tier3 {{ background: rgba(107, 114, 128, 0.2); color: #d1d5db; border: 1px solid #6b7280; }}
.topic-meta {{
  font-size: 12px;
  color: var(--text-muted);
  margin-top: 4px;
}}
.topic-notes-btn {{
  background: transparent;
  border: 1px dashed var(--border);
  color: var(--gold);
  font-size: 12px;
  padding: 4px 10px;
  border-radius: 6px;
  margin-top: 10px;
  cursor: pointer;
}}
.notes-drawer {{
  display: none;
  margin-top: 10px;
  padding-top: 10px;
  border-top: 1px solid var(--border);
}}
.notes-drawer textarea {{
  width: 100%;
  background: var(--bg-secondary);
  border: 1px solid var(--border);
  border-radius: 8px;
  color: var(--text-main);
  padding: 10px;
  font-size: 13px;
  font-family: inherit;
  resize: vertical;
  min-height: 70px;
}}
.notes-drawer textarea:focus {{
  outline: none;
  border-color: var(--gold);
}}
.mindmap-box {{
  background: var(--bg-card);
  border: 1px solid var(--border);
  border-radius: 12px;
  padding: 20px;
  margin-bottom: 20px;
}}
.flow-diagram {{
  background: var(--bg-secondary);
  border: 1px solid var(--border);
  border-radius: 8px;
  padding: 16px;
  margin: 12px 0;
  font-family: 'JetBrains Mono', monospace;
  font-size: 12px;
  overflow-x: auto;
  color: #a7f3d0;
  white-space: pre;
}}
.quiz-box {{
  background: var(--bg-card);
  border: 1px solid var(--border);
  border-radius: 12px;
  padding: 20px;
  margin-bottom: 20px;
}}
.quiz-q {{
  font-size: 15px;
  font-weight: 600;
  margin-bottom: 14px;
  white-space: pre-line;
}}
.quiz-opt {{
  background: var(--bg-secondary);
  border: 1px solid var(--border);
  border-radius: 8px;
  padding: 10px 14px;
  margin-bottom: 8px;
  cursor: pointer;
  font-size: 14px;
  transition: all 0.15s;
}}
.quiz-opt:hover {{
  border-color: var(--gold);
}}
.quiz-opt.selected {{
  border-color: var(--gold);
  background: rgba(212, 175, 55, 0.15);
}}
.quiz-opt.correct {{
  border-color: var(--accent-green);
  background: rgba(16, 185, 129, 0.2);
  color: #a7f3d0;
}}
.quiz-opt.wrong {{
  border-color: var(--accent-red);
  background: rgba(239, 68, 68, 0.2);
  color: #fca5a5;
}}
.quiz-expl {{
  display: none;
  background: rgba(17, 24, 39, 0.9);
  border-left: 3px solid var(--gold);
  padding: 12px;
  margin-top: 10px;
  border-radius: 4px;
  font-size: 13px;
  color: #e5e7eb;
}}
.action-btn {{
  background: var(--gold);
  color: #0b0f19;
  border: none;
  padding: 10px 18px;
  border-radius: 8px;
  font-weight: 700;
  font-size: 14px;
  cursor: pointer;
}}
.sync-modal {{
  display: none;
  position: fixed;
  top: 0; left: 0; width: 100%; height: 100%;
  background: rgba(0, 0, 0, 0.8);
  z-index: 100;
  justify-content: center;
  align-items: center;
  padding: 16px;
}}
.modal-card {{
  background: var(--bg-card);
  border: 1px solid var(--border);
  border-radius: 12px;
  max-width: 500px;
  width: 100%;
  padding: 20px;
}}
</style>
</head>
<body>

<header>
  <div class="header-container">
    <div class="logo-box">
      <span class="badge-gold">OFFICERPASS</span>
      <h1>UPSC 2027 MISSION</h1>
    </div>
    <div class="timer-pill" id="next-slot-pill">
      ⏳ Next Slot: 06:00 AM (Morning Core)
    </div>
    <div>
      <button class="action-btn" onclick="openSync()" style="padding: 6px 12px; font-size: 12px;">📲 Sync Phone / Backup</button>
      <a href="../calendar/officerpass-schedule.ics" download class="action-btn" style="padding: 6px 12px; font-size: 12px; text-decoration: none; display: inline-block; margin-left: 6px;">📅 Add Calendar</a>
    </div>
  </div>
  <div class="nav-tabs">
    <button class="tab-btn active" onclick="switchTab('checklist')">🎯 Micro-Topics Checklist</button>
    <button class="tab-btn" onclick="switchTab('mindmaps')">🗺️ Visual Mind Maps & Story Flows</button>
    <button class="tab-btn" onclick="switchTab('quiz')">📝 50-Q Practice Drill (Parliament)</button>
    <button class="tab-btn" onclick="switchTab('csat')">🧩 CSAT 6th-Grade Intuition</button>
  </div>
</header>

<div class="main-container">

  <!-- TAB 1: CHECKLIST -->
  <div id="tab-checklist">
    <div class="hero-stats">
      <div class="stat-card">
        <h3>Completed Topics</h3>
        <div class="val"><span id="stat-completed">0</span> / <span id="stat-total">64</span></div>
        <div class="sub"><span id="stat-percent">0</span>% Syllabus Covered</div>
        <div class="progress-bar-wrap"><div class="progress-bar-fill" id="stat-bar"></div></div>
      </div>
      <div class="stat-card">
        <h3>Golden Topics (>80% Prob)</h3>
        <div class="val"><span id="stat-tier1-done">0</span> / <span id="stat-tier1-total">38</span></div>
        <div class="sub">Critical High-Yield Hotspots</div>
      </div>
      <div class="stat-card">
        <h3>Personal Memory Notes</h3>
        <div class="val" id="stat-notes-count">0</div>
        <div class="sub">Topics with custom anchors</div>
      </div>
    </div>

    <div class="filter-bar">
      <label class="toggle-btn">
        <input type="checkbox" id="golden-toggle" onchange="renderTopics()" style="accent-color: var(--gold); transform: scale(1.2);" />
        🔥 Show ONLY Golden Hotspots (>80% Probability)
      </label>
      <div class="subj-chips" id="subj-chips">
        <div class="chip active" onclick="selectSubj('All')">All</div>
        <div class="chip" onclick="selectSubj('Polity')">Polity</div>
        <div class="chip" onclick="selectSubj('Economy')">Economy</div>
        <div class="chip" onclick="selectSubj('Environment')">Environment</div>
        <div class="chip" onclick="selectSubj('Geography')">Geography</div>
        <div class="chip" onclick="selectSubj('ScienceTech')">Sci-Tech</div>
        <div class="chip" onclick="selectSubj('HistoryCulture')">History</div>
        <div class="chip" onclick="selectSubj('CSAT_Grade6')">CSAT</div>
      </div>
    </div>

    <div id="topics-list"></div>
  </div>

  <!-- TAB 2: MIND MAPS -->
  <div id="tab-mindmaps" style="display: none;">
    <div class="mindmap-box">
      <h2 style="color: var(--gold-light); margin-bottom: 8px;">🏛️ Parliament: The Bill Journey & Deadlock Rules</h2>
      <p style="font-size: 13px; color: var(--text-muted);">Visual mental anchor for Money Bill vs Ordinary Bill vs Constitutional Amendment.</p>
      <div class="flow-diagram">
[ORDINARY BILL]
Introduced: Lok Sabha OR Rajya Sabha
    ↓
Can Rajya Sabha delay? YES (Max 6 months)
    ↓
Deadlock? YES → Article 108 [JOINT SITTING Summoned by President, Presided by Speaker]
    ↓ Simple Majority wins (Lok Sabha numerical strength dominates)

[MONEY BILL (Article 110)]
Introduced: Lok Sabha ONLY (Prior Presidential recommendation required)
    ↓
Can Rajya Sabha reject? NO!
Can Rajya Sabha amend? Recommendations only (Lok Sabha may accept or reject)
    ↓
Max Rajya Sabha delay: Exactly 14 DAYS! (If not returned, deemed passed)
    ↓
Deadlock? IMPOSSIBLE. Joint Sitting? NEVER.

[CONSTITUTIONAL AMENDMENT BILL (Article 368)]
Introduced: Lok Sabha OR Rajya Sabha (No prior President recommendation needed)
    ↓
Must be passed by EACH HOUSE SEPARATELY by SPECIAL MAJORITY!
    ↓
Deadlock? Bill DIES. Joint Sitting? FORBIDDEN BY CONSTITUTION.
      </div>
    </div>

    <div class="mindmap-box">
      <h2 style="color: var(--gold-light); margin-bottom: 8px;">⚖️ Anti-Defection Law (Tenth Schedule) Decision Flow</h2>
      <div class="flow-diagram">
Member of Parliament / Assembly:
├── Independent Member?
│     └── Joins ANY political party after election? → DISQUALIFIED!
├── Nominated Member?
│     ├── Joins a party WITHIN 6 months? → ALLOWED (Safe).
│     └── Joins a party AFTER 6 months? → DISQUALIFIED!
└── Party Member?
      ├── Voluntarily gives up membership? → DISQUALIFIED!
      └── Votes against party Whip? → DISQUALIFIED (Unless condoned within 15 days).
      └── EXEMPTION: Merger of 2/3rd members with another party → SAFE!

Decision Maker: Presiding Officer (Speaker/Chairman)
Is Decision Final? NO → Subject to Judicial Review (Kihoto Hollohan case, 1992).
      </div>
    </div>

    <div class="mindmap-box">
      <h2 style="color: var(--gold-light); margin-bottom: 8px;">🏦 RBI Monetary Policy Transmission Seesaw</h2>
      <div class="flow-diagram">
INFLATION HIGH?
    ↓
RBI RAISES REPO RATE (Interest charged to commercial banks)
    ↓
Commercial Banks raise Lending Rates (Loans get expensive)
    ↓
Borrowing by Businesses & Consumers drops → Money Supply tightens
    ↓
Aggregate Demand cools → INFLATION FALLS!
    ↓
Bond Market Effect: When Interest Rates rise → Bond Prices FALL! (Inverse Curve)
      </div>
    </div>
  </div>

  <!-- TAB 3: PRACTICE QUIZ -->
  <div id="tab-quiz" style="display: none;">
    <div class="quiz-box">
      <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 16px;">
        <div>
          <h2 style="color: var(--gold-light);">📝 Polity Parliament Drill: Question <span id="q-num">1</span> of <span id="q-total">50</span></h2>
          <span style="font-size: 12px; color: var(--gold);" id="q-topic"></span>
        </div>
        <div class="timer-pill" id="quiz-timer">⏱️ 15:00</div>
      </div>

      <div class="quiz-q" id="q-text"></div>
      <div id="q-options"></div>

      <div class="quiz-expl" id="q-expl"></div>

      <div style="display: flex; justify-content: space-between; margin-top: 16px;">
        <button class="action-btn" style="background: var(--bg-card); color: var(--text-main); border: 1px solid var(--border);" onclick="prevQ()">⬅️ Previous</button>
        <button class="action-btn" id="btn-check" onclick="checkAnswer()">Check Answer</button>
        <button class="action-btn" onclick="nextQ()">Next ➡️</button>
      </div>
    </div>
  </div>

  <!-- TAB 4: CSAT 6TH GRADE -->
  <div id="tab-csat" style="display: none;">
    <div class="mindmap-box">
      <h2 style="color: var(--gold-light); margin-bottom: 8px;">💡 CSAT Concept 1: The ₹100 Bill Trick (Percentages)</h2>
      <p style="font-size: 13px; color: var(--text-muted); margin-bottom: 12px;">Solve any price-consumption or profit problem without memorizing formulas.</p>
      <div class="flow-diagram">
PROBLEM: "Price of commodity rises by 25%. How much to reduce consumption to keep spend same?"

6TH-GRADE THOUGHT:
Step 1: Original price = ₹100.
Step 2: New price = ₹125.
Step 3: You only have your ₹100 note.
Step 4: You must return ₹25 worth of goods out of ₹125:
        25 / 125 = 1/5 = 20%!

Done in 5 seconds. No algebra.
      </div>
    </div>

    <div class="mindmap-box">
      <h2 style="color: var(--gold-light); margin-bottom: 8px;">💡 CSAT Concept 2: The Playground Seesaw (Averages)</h2>
      <div class="flow-diagram">
PROBLEM: "30 students have avg age 15. Teacher joins, avg becomes 16. Teacher age?"

6TH-GRADE THOUGHT:
The 30 kids sit balanced at 15.
Teacher walks in. Everyone's age lifts by +1!
Teacher must bring:
1) +1 candy for each of the 30 kids = 30 candies.
2) 16 candies for herself to stay at the new average = 16 candies.
Total = 30 + 16 = 46 years old!
      </div>
    </div>
  </div>

</div>

<!-- SYNC MODAL -->
<div class="sync-modal" id="sync-modal">
  <div class="modal-card">
    <h3 style="color: var(--gold-light); margin-bottom: 10px;">📲 Sync Checklist & Notes Across Devices</h3>
    <p style="font-size: 12px; color: var(--text-muted); margin-bottom: 12px;">
      Your checklist ticks and custom notes are stored locally in this browser. To transfer them to your iPhone/iPad or make a backup:
    </p>
    <button class="action-btn" onclick="exportData()" style="width: 100%; margin-bottom: 8px;">📥 Download Backup JSON</button>
    <div style="font-size: 12px; color: var(--text-muted); margin: 8px 0;">Or paste JSON below to import from phone:</div>
    <textarea id="import-area" style="width: 100%; background: var(--bg-secondary); border: 1px solid var(--border); color: #fff; padding: 8px; border-radius: 6px; font-size: 11px; min-height: 80px;"></textarea>
    <div style="display: flex; gap: 8px; margin-top: 10px;">
      <button class="action-btn" onclick="importData()" style="flex: 1; font-size: 12px;">Import</button>
      <button class="action-btn" onclick="closeSync()" style="background: var(--border); color: #fff; font-size: 12px;">Close</button>
    </div>
  </div>
</div>

<script>
const topicsData = {topics_json_str};
const quizData = {quiz_json_str};

let currentSubj = 'All';
let currentQIdx = 0;
let userQuizAnswers = {{}};

function init() {{
  renderTopics();
  updateStats();
  renderQuizQ();
  startNextSlotTimer();
}}

function switchTab(tabId) {{
  ['checklist', 'mindmaps', 'quiz', 'csat'].forEach(t => {{
    document.getElementById('tab-' + t).style.display = (t === tabId) ? 'block' : 'none';
  }});
  document.querySelectorAll('.tab-btn').forEach((btn, idx) => {{
    btn.classList.toggle('active', ['checklist', 'mindmaps', 'quiz', 'csat'][idx] === tabId);
  }});
}}

function selectSubj(subj) {{
  currentSubj = subj;
  document.querySelectorAll('.chip').forEach(c => {{
    c.classList.toggle('active', c.innerText === subj);
  }});
  renderTopics();
}}

function renderTopics() {{
  const container = document.getElementById('topics-list');
  const onlyGolden = document.getElementById('golden-toggle').checked;
  const savedChecks = JSON.parse(localStorage.getItem('op_checks') || '{{}}');
  const savedNotes = JSON.parse(localStorage.getItem('op_notes') || '{{}}');

  let html = '';
  for (const [subj, list] of Object.entries(topicsData)) {{
    if (currentSubj !== 'All' && currentSubj !== subj) continue;

    const filtered = list.filter(t => !onlyGolden || t.prob >= 80);
    if (filtered.length === 0) continue;

    html += `<h3 style="color: var(--gold-light); margin: 18px 0 10px; font-size: 16px;">${{subj}} (${{filtered.length}} Topics)</h3>`;

    filtered.forEach(t => {{
      const isDone = savedChecks[t.id] || false;
      const note = savedNotes[t.id] || '';
      const tierClass = t.tier === 1 ? 'prob-tier1' : (t.tier === 2 ? 'prob-tier2' : 'prob-tier3');

      html += `
        <div class="topic-card">
          <div class="topic-header">
            <input type="checkbox" class="custom-checkbox" ${{isDone ? 'checked' : ''}} onchange="toggleTopic('${{t.id}}')" />
            <div class="topic-body">
              <div class="topic-title ${{isDone ? 'done' : ''}}">
                <span class="prob-badge ${{tierClass}}">${{t.prob}}% PROB | TIER ${{t.tier}}</span>
                ${{t.topic}}
              </div>
              <div class="topic-meta">
                📖 <strong>Source:</strong> ${{t.core_sources}} | 📊 <strong>PYQs:</strong> ${{t.pyqs}} Qs | 🔑 <strong>Keywords:</strong> ${{t.keywords}}
              </div>
              <button class="topic-notes-btn" onclick="toggleNotes('${{t.id}}')">
                ✏️ ${{note ? 'Edit Notes (' + note.length + ' chars)' : '+ Add Personal Notes / Mnemonics'}}
              </button>
              <div class="notes-drawer" id="notes-${{t.id}}">
                <textarea placeholder="Write personal memory anchors, traps to avoid, or key article numbers..." oninput="saveNote('${{t.id}}', this.value)">${{note}}</textarea>
              </div>
            </div>
          </div>
        </div>
      `;
    }});
  }}
  container.innerHTML = html;
}}

function toggleTopic(id) {{
  const savedChecks = JSON.parse(localStorage.getItem('op_checks') || '{{}}');
  savedChecks[id] = !savedChecks[id];
  localStorage.setItem('op_checks', JSON.stringify(savedChecks));
  renderTopics();
  updateStats();
}}

function toggleNotes(id) {{
  const el = document.getElementById('notes-' + id);
  el.style.display = el.style.display === 'block' ? 'none' : 'block';
}}

function saveNote(id, val) {{
  const savedNotes = JSON.parse(localStorage.getItem('op_notes') || '{{}}');
  savedNotes[id] = val;
  localStorage.setItem('op_notes', JSON.stringify(savedNotes));
  updateStats();
}}

function updateStats() {{
  const savedChecks = JSON.parse(localStorage.getItem('op_checks') || '{{}}');
  const savedNotes = JSON.parse(localStorage.getItem('op_notes') || '{{}}');

  let total = 0;
  let done = 0;
  let t1Total = 0;
  let t1Done = 0;

  for (const list of Object.values(topicsData)) {{
    list.forEach(t => {{
      total++;
      if (savedChecks[t.id]) done++;
      if (t.prob >= 80) {{
        t1Total++;
        if (savedChecks[t.id]) t1Done++;
      }}
    }});
  }}

  const pct = total ? Math.round((done / total) * 100) : 0;
  document.getElementById('stat-completed').innerText = done;
  document.getElementById('stat-total').innerText = total;
  document.getElementById('stat-percent').innerText = pct;
  document.getElementById('stat-bar').style.width = pct + '%';
  document.getElementById('stat-tier1-done').innerText = t1Done;
  document.getElementById('stat-tier1-total').innerText = t1Total;

  const notesCount = Object.values(savedNotes).filter(n => n && n.trim().length > 0).length;
  document.getElementById('stat-notes-count').innerText = notesCount;
}}

function startNextSlotTimer() {{
  const pill = document.getElementById('next-slot-pill');
  function update() {{
    const now = new Date();
    const hours = now.getHours();
    const mins = now.getMinutes();
    let nextName = '';

    if (hours < 6) {{
      nextName = '06:00 AM (Morning Core)';
    }} else if (hours < 7 || (hours === 7 && mins < 30)) {{
      nextName = '07:30 AM (CSAT Drill)';
    }} else if (hours < 20 || (hours === 20 && mins < 30)) {{
      nextName = '08:30 PM (Evening PYQ Drill)';
    }} else if (hours < 21 || (hours === 21 && mins < 15)) {{
      nextName = '09:15 PM (Current Affairs)';
    }} else if (hours < 21 || (hours === 21 && mins < 45)) {{
      nextName = '09:45 PM (Daily Log & Wrap)';
    }} else {{
      nextName = '06:00 AM Tomorrow (Morning Core)';
    }}
    pill.innerText = '⏳ Next Session: ' + nextName;
  }}
  update();
  setInterval(update, 60000);
}}

// QUIZ LOGIC
function renderQuizQ() {{
  const q = quizData[currentQIdx];
  document.getElementById('q-num').innerText = currentQIdx + 1;
  document.getElementById('q-total').innerText = quizData.length;
  document.getElementById('q-topic').innerText = q.topic;
  document.getElementById('q-text').innerText = q.q;

  const optContainer = document.getElementById('q-options');
  let html = '';
  q.options.forEach((opt, idx) => {{
    const isSel = userQuizAnswers[q.id] === opt.substring(0, 3);
    html += `<div class="quiz-opt ${{isSel ? 'selected' : ''}}" onclick="selectQuizOpt(${{q.id}}, '${{opt.substring(0, 3)}}')">${{opt}}</div>`;
  }});
  optContainer.innerHTML = html;

  const explEl = document.getElementById('q-expl');
  explEl.style.display = 'none';
  explEl.innerText = '';
}}

function selectQuizOpt(qId, optCode) {{
  userQuizAnswers[qId] = optCode;
  renderQuizQ();
}}

function checkAnswer() {{
  const q = quizData[currentQIdx];
  const userAns = userQuizAnswers[q.id];
  const explEl = document.getElementById('q-expl');
  explEl.style.display = 'block';
  explEl.innerHTML = `<strong>Official Answer: ${{q.answer}}</strong><br><br>${{q.explanation}}`;

  const optEls = document.querySelectorAll('.quiz-opt');
  optEls.forEach(el => {{
    const code = el.innerText.substring(0, 3);
    if (code === q.answer) el.classList.add('correct');
    else if (code === userAns) el.classList.add('wrong');
  }});
}}

function nextQ() {{
  if (currentQIdx < quizData.length - 1) {{
    currentQIdx++;
    renderQuizQ();
  }}
}}

function prevQ() {{
  if (currentQIdx > 0) {{
    currentQIdx--;
    renderQuizQ();
  }}
}}

// SYNC MODAL
function openSync() {{
  document.getElementById('sync-modal').style.display = 'flex';
}}
function closeSync() {{
  document.getElementById('sync-modal').style.display = 'none';
}}
function exportData() {{
  const data = {{
    checks: JSON.parse(localStorage.getItem('op_checks') || '{{}}'),
    notes: JSON.parse(localStorage.getItem('op_notes') || '{{}}'),
    exportDate: new Date().toISOString()
  }};
  const blob = new Blob([JSON.stringify(data, null, 2)], {{ type: 'application/json' }});
  const url = URL.createObjectURL(blob);
  const a = document.createElement('a');
  a.href = url;
  a.download = 'officerpass-backup-' + new Date().toISOString().slice(0, 10) + '.json';
  a.click();
}}
function importData() {{
  try {{
    const raw = document.getElementById('import-area').value;
    const parsed = JSON.parse(raw);
    if (parsed.checks) localStorage.setItem('op_checks', JSON.stringify(parsed.checks));
    if (parsed.notes) localStorage.setItem('op_notes', JSON.stringify(parsed.notes));
    alert('Import successful!');
    closeSync();
    renderTopics();
    updateStats();
  }} catch (e) {{
    alert('Invalid JSON: ' + e.message);
  }}
}}

window.onload = init;
</script>
</body>
</html>'''

with open('/Users/vashishtaparikipandla/Documents/OfficerPass/dashboard/index.html', 'w') as f:
    f.write(html_template)

print('Successfully written /Users/vashishtaparikipandla/Documents/OfficerPass/dashboard/index.html')
