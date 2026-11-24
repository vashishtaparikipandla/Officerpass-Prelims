import os

output_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'dashboard', 'index.html')
html_content = '''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>OfficerPass — UPSC Prelims Command Engine</title>
<style>
:root {
  --bg: #0b0d11;
  --surface: #12161f;
  --surface-alt: #181f2c;
  --border: #232b3b;
  --border-light: #2e394e;
  --text: #f1f5f9;
  --muted: #94a3b8;
  --dark-muted: #64748b;
  --gold: #d97706;
  --gold-bright: #f59e0b;
  --gold-dim: rgba(245, 158, 11, 0.12);
  --blue: #2563eb;
  --blue-bright: #3b82f6;
  --blue-dim: rgba(59, 130, 246, 0.12);
  --green: #059669;
  --green-bright: #10b981;
  --green-dim: rgba(16, 185, 129, 0.12);
  --red: #dc2626;
  --red-dim: rgba(220, 38, 38, 0.12);
  --purple: #7c3aed;
  --radius: 8px;
  --radius-sm: 4px;
  font-size: 14px;
}
* { box-sizing: border-box; margin: 0; padding: 0; }
body {
  background: var(--bg);
  color: var(--text);
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  line-height: 1.5;
}
svg { vertical-align: middle; }

/* Header & Top Bar */
.top-header {
  background: var(--surface);
  border-bottom: 1px solid var(--border);
  padding: 12px 24px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  position: sticky;
  top: 0;
  z-index: 50;
}
.brand-group {
  display: flex;
  align-items: center;
  gap: 12px;
}
.brand-name {
  font-size: 17px;
  font-weight: 700;
  letter-spacing: -0.02em;
  color: var(--text);
}
.candidate-badge {
  background: var(--gold-dim);
  color: var(--gold-bright);
  border: 1px solid rgba(245, 158, 11, 0.3);
  font-size: 11px;
  font-weight: 600;
  padding: 3px 8px;
  border-radius: 9999px;
  letter-spacing: 0.02em;
}

/* Day Switcher Controls */
.day-controls {
  display: flex;
  align-items: center;
  gap: 8px;
  background: var(--surface-alt);
  padding: 4px 6px;
  border: 1px solid var(--border);
  border-radius: var(--radius);
}
.day-nav-btn {
  background: transparent;
  border: none;
  color: var(--muted);
  cursor: pointer;
  padding: 6px 10px;
  border-radius: var(--radius-sm);
  display: inline-flex;
  align-items: center;
  gap: 4px;
  font-size: 12px;
  font-weight: 600;
  transition: all 0.15s ease;
}
.day-nav-btn:hover {
  background: var(--border);
  color: var(--text);
}
.day-select-input {
  background: var(--bg);
  border: 1px solid var(--border);
  color: var(--gold-bright);
  font-size: 13px;
  font-weight: 700;
  padding: 4px 8px;
  border-radius: var(--radius-sm);
  width: 140px;
  text-align: center;
}
.jump-today-btn {
  background: var(--gold);
  border: none;
  color: #fff;
  font-size: 11px;
  font-weight: 700;
  padding: 6px 12px;
  border-radius: var(--radius-sm);
  cursor: pointer;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  transition: opacity 0.15s;
}
.jump-today-btn:hover { opacity: 0.9; }

/* Main Navigation Tabs */
.nav-bar {
  background: var(--surface);
  border-bottom: 1px solid var(--border);
  padding: 0 24px;
  display: flex;
  gap: 24px;
  overflow-x: auto;
}
.nav-tab {
  padding: 14px 4px;
  font-size: 13px;
  font-weight: 600;
  color: var(--muted);
  cursor: pointer;
  border-bottom: 2px solid transparent;
  display: flex;
  align-items: center;
  gap: 8px;
  transition: all 0.15s;
  white-space: nowrap;
}
.nav-tab:hover { color: var(--text); }
.nav-tab.active {
  color: var(--gold-bright);
  border-bottom-color: var(--gold-bright);
}
.nav-tab svg {
  width: 16px;
  height: 16px;
  stroke: currentColor;
  fill: none;
  stroke-width: 2;
  stroke-linecap: round;
  stroke-linejoin: round;
}

/* App Container */
.app-container {
  max-width: 1240px;
  margin: 0 auto;
  padding: 24px 20px 60px;
  width: 100%;
  flex: 1;
}

/* Tab Panels */
.tab-content { display: none; }
.tab-content.active { display: block; }

/* NEIL SIR PRINCIPLE CARD */
.neil-sir-hero {
  background: linear-gradient(180deg, rgba(245,158,11,0.08) 0%, rgba(18,22,31,0.8) 100%);
  border: 1px solid rgba(245,158,11,0.35);
  border-radius: var(--radius);
  padding: 24px 28px;
  margin-bottom: 24px;
  position: relative;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.25);
}
.neil-sir-label {
  font-size: 11px;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.1em;
  color: var(--gold-bright);
  display: flex;
  align-items: center;
  gap: 6px;
  margin-bottom: 8px;
}
.neil-sir-quote {
  font-size: 19px;
  font-weight: 600;
  color: #fff;
  line-height: 1.45;
  letter-spacing: -0.01em;
}

/* WEEKLY REVISION BANNER */
.mock-day-banner {
  background: rgba(16, 185, 129, 0.1);
  border: 1px solid rgba(16, 185, 129, 0.35);
  border-radius: var(--radius);
  padding: 16px 20px;
  margin-bottom: 24px;
  display: flex;
  align-items: center;
  justify-content: space-between;
}
.mock-day-title {
  font-size: 15px;
  font-weight: 700;
  color: var(--green-bright);
}
.mock-day-sub {
  font-size: 12px;
  color: var(--muted);
  margin-top: 2px;
}

/* DATE & PHASE HEADER */
.day-header-meta {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 20px;
  flex-wrap: wrap;
  gap: 12px;
}
.day-title-wrap h1 {
  font-size: 22px;
  font-weight: 700;
  color: var(--text);
  letter-spacing: -0.02em;
}
.day-sub-info {
  display: flex;
  gap: 12px;
  align-items: center;
  margin-top: 4px;
  font-size: 12px;
  color: var(--muted);
}
.phase-pill {
  background: var(--surface-alt);
  border: 1px solid var(--border);
  padding: 3px 10px;
  border-radius: 9999px;
  font-size: 11px;
  font-weight: 600;
  color: var(--blue-bright);
}
.progress-summary {
  display: flex;
  align-items: center;
  gap: 10px;
  background: var(--surface);
  padding: 8px 14px;
  border-radius: var(--radius);
  border: 1px solid var(--border);
  font-size: 12px;
  font-weight: 600;
}

/* TWO MAIN STUDY BOXES */
.study-blocks-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 20px;
  margin-bottom: 32px;
}
@media (max-width: 860px) {
  .study-blocks-grid { grid-template-columns: 1fr; }
}

.study-card {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: var(--radius);
  overflow: hidden;
  display: flex;
  flex-direction: column;
}
.card-top {
  padding: 16px 20px;
  border-bottom: 1px solid var(--border);
  display: flex;
  align-items: center;
  justify-content: space-between;
}
.card-top.morning {
  background: linear-gradient(90deg, rgba(245, 158, 11, 0.08) 0%, transparent 100%);
  border-top: 3px solid var(--gold-bright);
}
.card-top.evening {
  background: linear-gradient(90deg, rgba(59, 130, 246, 0.08) 0%, transparent 100%);
  border-top: 3px solid var(--blue-bright);
}
.card-title-group {
  display: flex;
  align-items: center;
  gap: 10px;
}
.time-badge {
  font-size: 11px;
  font-weight: 700;
  padding: 3px 8px;
  border-radius: var(--radius-sm);
  letter-spacing: 0.03em;
}
.time-badge.morning {
  background: var(--gold-dim);
  color: var(--gold-bright);
  border: 1px solid rgba(245, 158, 11, 0.3);
}
.time-badge.evening {
  background: var(--blue-dim);
  color: var(--blue-bright);
  border: 1px solid rgba(59, 130, 246, 0.3);
}
.card-heading {
  font-size: 14px;
  font-weight: 700;
  color: var(--text);
}
.card-body {
  padding: 20px;
  flex: 1;
  display: flex;
  flex-direction: column;
  gap: 16px;
}

/* Core Source Pill */
.source-pill-box {
  display: flex;
  align-items: center;
  justify-content: space-between;
  background: var(--surface-alt);
  border: 1px solid var(--border);
  padding: 10px 14px;
  border-radius: var(--radius-sm);
}
.source-text {
  font-size: 13px;
  font-weight: 600;
  color: var(--text);
}
.source-tag {
  font-size: 10px;
  font-weight: 700;
  text-transform: uppercase;
  color: var(--muted);
  letter-spacing: 0.05em;
}

/* Micro-Checkpoints List */
.sub-items-container {
  display: flex;
  flex-direction: column;
  gap: 8px;
}
.sub-item-row {
  display: flex;
  align-items: flex-start;
  gap: 10px;
  padding: 8px 10px;
  border-radius: var(--radius-sm);
  background: var(--bg);
  border: 1px solid var(--border);
  transition: all 0.15s;
}
.sub-item-row:hover {
  border-color: var(--border-light);
}
.custom-checkbox {
  appearance: none;
  width: 17px;
  height: 17px;
  border: 1.5px solid var(--dark-muted);
  border-radius: 4px;
  outline: none;
  cursor: pointer;
  margin-top: 2px;
  display: grid;
  place-content: center;
  transition: all 0.15s;
  background: transparent;
}
.custom-checkbox:checked {
  background: var(--green-bright);
  border-color: var(--green-bright);
}
.custom-checkbox:checked::after {
  content: "";
  width: 5px;
  height: 8px;
  border: solid white;
  border-width: 0 2px 2px 0;
  transform: rotate(45deg);
  margin-bottom: 2px;
}
.sub-item-label {
  font-size: 12.5px;
  color: var(--text);
  line-height: 1.4;
  cursor: pointer;
  flex: 1;
}
.sub-item-row.completed .sub-item-label {
  color: var(--muted);
  text-decoration: line-through;
}

/* Personal Touch Notes Box */
.notes-container {
  margin-top: 8px;
  border-top: 1px solid var(--border);
  padding-top: 14px;
}
.notes-label {
  font-size: 11px;
  font-weight: 700;
  text-transform: uppercase;
  color: var(--muted);
  letter-spacing: 0.05em;
  margin-bottom: 6px;
  display: flex;
  justify-content: space-between;
}
.notes-textarea {
  width: 100%;
  background: var(--bg);
  border: 1px solid var(--border);
  color: var(--text);
  font-family: inherit;
  font-size: 12.5px;
  padding: 10px;
  border-radius: var(--radius-sm);
  resize: vertical;
  min-height: 64px;
}
.notes-textarea:focus {
  outline: none;
  border-color: var(--gold-bright);
}
.save-note-btn {
  background: var(--surface-alt);
  border: 1px solid var(--border);
  color: var(--muted);
  font-size: 11px;
  font-weight: 600;
  padding: 4px 10px;
  border-radius: var(--radius-sm);
  cursor: pointer;
  margin-top: 6px;
  align-self: flex-end;
}
.save-note-btn:hover {
  background: var(--border);
  color: var(--text);
}

/* Evening Target Cards */
.evening-target-box {
  background: var(--bg);
  border: 1px solid var(--border);
  padding: 14px 16px;
  border-radius: var(--radius-sm);
  display: flex;
  flex-direction: column;
  gap: 8px;
}
.target-header {
  font-size: 11px;
  font-weight: 700;
  text-transform: uppercase;
  color: var(--blue-bright);
  letter-spacing: 0.05em;
  display: flex;
  align-items: center;
  justify-content: space-between;
}
.target-title {
  font-size: 13.5px;
  font-weight: 600;
  color: var(--text);
}
.target-subtext {
  font-size: 12px;
  color: var(--muted);
  line-height: 1.4;
}
.target-action-btn {
  background: var(--surface-alt);
  border: 1px solid var(--border);
  color: var(--text);
  font-size: 12px;
  font-weight: 600;
  padding: 8px 12px;
  border-radius: var(--radius-sm);
  cursor: pointer;
  text-align: center;
  transition: all 0.15s;
  text-decoration: none;
  display: inline-block;
  margin-top: 4px;
}
.target-action-btn:hover {
  background: var(--blue-dim);
  border-color: var(--blue-bright);
  color: var(--blue-bright);
}

/* DAY SPECIFIC PRACTICE MCQS SECTION */
.day-mcqs-section {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: var(--radius);
  padding: 24px;
  margin-bottom: 30px;
}
.mcq-sec-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 20px;
  flex-wrap: wrap;
  gap: 12px;
}
.mcq-sec-title {
  font-size: 17px;
  font-weight: 700;
  color: var(--text);
  display: flex;
  align-items: center;
  gap: 8px;
}
.mcq-stats-pill {
  background: var(--surface-alt);
  border: 1px solid var(--border);
  font-size: 12px;
  font-weight: 600;
  padding: 4px 12px;
  border-radius: 9999px;
  color: var(--gold-bright);
}
.mcqs-deck-grid {
  display: flex;
  flex-direction: column;
  gap: 18px;
}
.single-mcq-card {
  background: var(--bg);
  border: 1px solid var(--border);
  border-radius: var(--radius);
  padding: 18px 20px;
  transition: border-color 0.15s;
}
.single-mcq-card:hover {
  border-color: var(--border-light);
}
.mcq-meta-row {
  display: flex;
  align-items: center;
  justify-content: space-between;
  font-size: 11px;
  font-weight: 700;
  text-transform: uppercase;
  color: var(--muted);
  letter-spacing: 0.05em;
  margin-bottom: 10px;
}
.star-btn {
  background: transparent;
  border: none;
  cursor: pointer;
  color: var(--dark-muted);
  display: inline-flex;
  align-items: center;
}
.star-btn.starred { color: var(--gold-bright); }
.star-btn svg { width: 16px; height: 16px; fill: currentColor; }
.mcq-question-text {
  font-size: 13.5px;
  font-weight: 500;
  color: var(--text);
  line-height: 1.5;
  margin-bottom: 14px;
  white-space: pre-line;
}
.mcq-options-list {
  display: flex;
  flex-direction: column;
  gap: 8px;
}
.mcq-option-item {
  background: var(--surface);
  border: 1px solid var(--border);
  padding: 10px 14px;
  border-radius: var(--radius-sm);
  font-size: 13px;
  color: var(--text);
  cursor: pointer;
  transition: all 0.15s;
  display: flex;
  align-items: center;
  gap: 10px;
}
.mcq-option-item:hover:not(.locked) {
  border-color: var(--blue-bright);
  background: var(--surface-alt);
}
.mcq-option-item.correct {
  background: var(--green-dim) !important;
  border-color: var(--green-bright) !important;
  color: var(--green-bright) !important;
  font-weight: 600;
}
.mcq-option-item.wrong {
  background: var(--red-dim) !important;
  border-color: var(--red) !important;
  color: #fca5a5 !important;
}
.mcq-explanation-box {
  display: none;
  margin-top: 12px;
  background: var(--surface-alt);
  border-left: 3px solid var(--gold-bright);
  padding: 12px 16px;
  border-radius: 0 var(--radius-sm) var(--radius-sm) 0;
  font-size: 12.5px;
  color: var(--text);
  line-height: 1.5;
}
.mcq-explanation-box.visible { display: block; }
.exp-title {
  font-size: 11px;
  font-weight: 700;
  text-transform: uppercase;
  color: var(--gold-bright);
  letter-spacing: 0.05em;
  margin-bottom: 4px;
}

/* ROADMAP TAB */
.roadmap-filter-bar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 24px;
  flex-wrap: wrap;
  gap: 12px;
}
.filter-pills-group {
  display: flex;
  gap: 8px;
  flex-wrap: wrap;
}
.filter-pill-btn {
  background: var(--surface);
  border: 1px solid var(--border);
  color: var(--muted);
  font-size: 12px;
  font-weight: 600;
  padding: 6px 14px;
  border-radius: 9999px;
  cursor: pointer;
  transition: all 0.15s;
}
.filter-pill-btn:hover { color: var(--text); }
.filter-pill-btn.active {
  background: var(--gold-bright);
  border-color: var(--gold-bright);
  color: #000;
}
.roadmap-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
  gap: 16px;
}
.roadmap-day-card {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: var(--radius);
  padding: 16px;
  cursor: pointer;
  transition: all 0.15s;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}
.roadmap-day-card:hover {
  border-color: var(--gold-bright);
  transform: translateY(-2px);
}
.roadmap-day-card.current {
  border-color: var(--gold-bright);
  background: var(--gold-dim);
}
.roadmap-day-card.mock {
  border-left: 4px solid var(--green-bright);
}
.rm-day-top {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 8px;
}
.rm-day-num {
  font-size: 12px;
  font-weight: 700;
  color: var(--gold-bright);
}
.rm-day-date {
  font-size: 11px;
  color: var(--muted);
}
.rm-day-title {
  font-size: 13.5px;
  font-weight: 600;
  color: var(--text);
  line-height: 1.4;
  margin-bottom: 12px;
}
.rm-day-footer {
  display: flex;
  align-items: center;
  justify-content: space-between;
  font-size: 11px;
  color: var(--muted);
}

/* CURRENT AFFAIRS TAB */
.ca-controls-bar {
  display: flex;
  flex-direction: column;
  gap: 14px;
  margin-bottom: 24px;
}
.ca-search-row {
  display: flex;
  gap: 12px;
  align-items: center;
}
.ca-search-input {
  flex: 1;
  background: var(--surface);
  border: 1px solid var(--border);
  color: var(--text);
  padding: 10px 14px;
  border-radius: var(--radius);
  font-size: 13px;
}
.ca-search-input:focus {
  outline: none;
  border-color: var(--gold-bright);
}
.ca-refresh-btn {
  background: var(--surface);
  border: 1px solid var(--border);
  color: var(--text);
  font-size: 12px;
  font-weight: 600;
  padding: 10px 16px;
  border-radius: var(--radius);
  cursor: pointer;
  display: inline-flex;
  align-items: center;
  gap: 6px;
}
.ca-refresh-btn:hover { border-color: var(--border-light); }
.ca-filter-row {
  display: flex;
  align-items: center;
  justify-content: space-between;
  flex-wrap: wrap;
  gap: 12px;
}
.unread-toggle-wrap {
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: 12px;
  color: var(--muted);
}
.ca-articles-grid {
  display: flex;
  flex-direction: column;
  gap: 16px;
}
.ca-article-card {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: var(--radius);
  padding: 20px;
  transition: all 0.15s;
}
.ca-article-card:hover { border-color: var(--border-light); }
.ca-card-top-meta {
  display: flex;
  align-items: center;
  justify-content: space-between;
  flex-wrap: wrap;
  gap: 8px;
  margin-bottom: 10px;
}
.ca-badges-group {
  display: flex;
  align-items: center;
  gap: 8px;
}
.pillar-badge {
  font-size: 11px;
  font-weight: 700;
  padding: 2px 8px;
  border-radius: var(--radius-sm);
  text-transform: uppercase;
  letter-spacing: 0.04em;
}
.pillar-badge.Polity { background: rgba(59,130,246,0.12); color: #60a5fa; }
.pillar-badge.Economy { background: rgba(16,185,129,0.12); color: #34d399; }
.pillar-badge.Environment { background: rgba(245,158,11,0.12); color: #fbbf24; }
.pillar-badge.SciTech { background: rgba(139,92,246,0.12); color: #a78bfa; }
.pillar-badge.IR { background: rgba(236,72,153,0.12); color: #f472b6; }
.pillar-badge.Geography { background: rgba(14,165,233,0.12); color: #38bdf8; }
.pillar-badge.History { background: rgba(249,115,22,0.12); color: #fb923c; }

.prob-badge {
  background: var(--gold-dim);
  color: var(--gold-bright);
  font-size: 11px;
  font-weight: 700;
  padding: 2px 8px;
  border-radius: var(--radius-sm);
}
.ca-article-title {
  font-size: 15px;
  font-weight: 700;
  color: var(--text);
  margin-bottom: 10px;
  line-height: 1.4;
}
.ca-article-title a {
  color: inherit;
  text-decoration: none;
}
.ca-article-title a:hover { color: var(--gold-bright); }
.ca-summary-bullets {
  margin-left: 18px;
  font-size: 13px;
  color: #cbd5e1;
  line-height: 1.5;
  margin-bottom: 14px;
}
.ca-summary-bullets li { margin-bottom: 4px; }
.ca-static-anchor-box {
  background: var(--bg);
  border: 1px solid var(--border);
  padding: 8px 12px;
  border-radius: var(--radius-sm);
  font-size: 12px;
  color: var(--muted);
  margin-bottom: 14px;
}
.ca-card-actions {
  display: flex;
  align-items: center;
  justify-content: space-between;
  border-top: 1px solid var(--border);
  padding-top: 12px;
}
.ca-action-btn {
  background: var(--surface-alt);
  border: 1px solid var(--border);
  color: var(--text);
  font-size: 12px;
  font-weight: 600;
  padding: 6px 12px;
  border-radius: var(--radius-sm);
  cursor: pointer;
  transition: all 0.15s;
}
.ca-action-btn:hover {
  background: var(--border);
}
.read-status-btn {
  background: transparent;
  border: 1px solid var(--border);
  color: var(--muted);
  font-size: 11px;
  font-weight: 600;
  padding: 4px 10px;
  border-radius: var(--radius-sm);
  cursor: pointer;
}
.read-status-btn.read {
  border-color: var(--green-bright);
  color: var(--green-bright);
  background: var(--green-dim);
}

/* CSAT LAB TAB */
.csat-modules-grid {
  display: flex;
  flex-direction: column;
  gap: 20px;
}
.csat-module-card {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: var(--radius);
  overflow: hidden;
}
.csat-mod-header {
  padding: 18px 24px;
  background: var(--surface-alt);
  border-bottom: 1px solid var(--border);
  display: flex;
  align-items: center;
  justify-content: space-between;
  flex-wrap: wrap;
  gap: 12px;
}
.csat-mod-title {
  font-size: 16px;
  font-weight: 700;
  color: var(--text);
}
.csat-mod-ref {
  font-size: 12px;
  font-weight: 600;
  color: var(--blue-bright);
}
.csat-mod-body {
  padding: 24px;
  display: flex;
  flex-direction: column;
  gap: 20px;
}
.child-concept-box {
  background: rgba(59, 130, 246, 0.08);
  border-left: 3px solid var(--blue-bright);
  padding: 14px 18px;
  border-radius: 0 var(--radius-sm) var(--radius-sm) 0;
}
.child-concept-title {
  font-size: 11px;
  font-weight: 700;
  text-transform: uppercase;
  color: var(--blue-bright);
  letter-spacing: 0.05em;
  margin-bottom: 6px;
}
.child-concept-text {
  font-size: 13.5px;
  color: var(--text);
  line-height: 1.5;
}
.shortcuts-box {
  background: var(--bg);
  border: 1px solid var(--border);
  padding: 14px 18px;
  border-radius: var(--radius-sm);
}
.shortcuts-title {
  font-size: 11px;
  font-weight: 700;
  text-transform: uppercase;
  color: var(--gold-bright);
  letter-spacing: 0.05em;
  margin-bottom: 8px;
}
.shortcuts-list {
  margin-left: 18px;
  font-size: 13px;
  color: #cbd5e1;
  line-height: 1.5;
}
.shortcuts-list li { margin-bottom: 6px; }

.pyq-walkthrough-box {
  background: var(--surface-alt);
  border: 1px solid var(--border);
  border-radius: var(--radius-sm);
  padding: 16px 20px;
}
.pyq-tag {
  font-size: 11px;
  font-weight: 700;
  text-transform: uppercase;
  color: var(--green-bright);
  letter-spacing: 0.05em;
  margin-bottom: 6px;
}
.pyq-q {
  font-size: 13.5px;
  font-weight: 600;
  color: var(--text);
  margin-bottom: 10px;
}
.pyq-step {
  font-size: 13px;
  color: #cbd5e1;
  line-height: 1.5;
  margin-bottom: 6px;
  white-space: pre-line;
}
.pyq-ans {
  margin-top: 10px;
  font-size: 13px;
  font-weight: 700;
  color: var(--green-bright);
}

/* SLIDE-OVER DRAWER FOR ARTICLE MCQS */
.drawer-overlay {
  display: none;
  position: fixed;
  top: 0; left: 0; right: 0; bottom: 0;
  background: rgba(0, 0, 0, 0.7);
  z-index: 100;
}
.drawer-overlay.active { display: block; }
.drawer-panel {
  position: fixed;
  top: 0; right: 0; bottom: 0;
  width: 90%;
  max-width: 600px;
  background: var(--surface);
  border-left: 1px solid var(--border);
  z-index: 101;
  overflow-y: auto;
  padding: 30px 24px;
  box-shadow: -10px 0 30px rgba(0, 0, 0, 0.5);
  display: none;
}
.drawer-panel.active { display: block; }
.drawer-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 20px;
  border-bottom: 1px solid var(--border);
  padding-bottom: 14px;
}
.drawer-title {
  font-size: 16px;
  font-weight: 700;
  color: var(--text);
}
.drawer-close-btn {
  background: transparent;
  border: none;
  color: var(--muted);
  cursor: pointer;
  font-size: 20px;
  padding: 4px;
}
.drawer-close-btn:hover { color: var(--text); }

/* Utility & Icons */
.icon-svg {
  display: inline-block;
  stroke-width: 2;
  stroke: currentColor;
  fill: none;
  stroke-linecap: round;
  stroke-linejoin: round;
}
</style>
</head>
<body>

<!-- TOP HEADER -->
<header class="top-header">
  <div class="brand-group">
    <svg class="icon-svg" width="22" height="22" viewBox="0 0 24 24" style="stroke:var(--gold-bright);">
      <circle cx="12" cy="12" r="10"></circle>
      <polyline points="12 6 12 12 16 14"></polyline>
    </svg>
    <div class="brand-name">OfficerPass</div>
    <div class="candidate-badge">Vashishta • Prelims 2027 • Attempt 5</div>
  </div>

  <!-- Interactive Day Switcher (Day 1 to 180) -->
  <div class="day-controls">
    <button class="day-nav-btn" onclick="prevDay()" title="Previous Day">
      <svg class="icon-svg" width="14" height="14" viewBox="0 0 24 24"><polyline points="15 18 9 12 15 6"></polyline></svg>
      Prev
    </button>
    <select id="day-selector" class="day-select-input" onchange="onDaySelectChange(this.value)">
      <!-- Populated via JS 1 to 180 -->
    </select>
    <button class="day-nav-btn" onclick="nextDay()" title="Next Day">
      Next
      <svg class="icon-svg" width="14" height="14" viewBox="0 0 24 24"><polyline points="9 18 15 12 9 6"></polyline></svg>
    </button>
    <button class="jump-today-btn" onclick="jumpToToday()">Today</button>
  </div>
</header>

<!-- MAIN NAVIGATION TABS -->
<nav class="nav-bar">
  <div class="nav-tab active" onclick="switchTab('today')" id="tab-today">
    <svg viewBox="0 0 24 24"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"></rect><line x1="16" y1="2" x2="16" y2="6"></line><line x1="8" y1="2" x2="8" y2="6"></line><line x1="3" y1="10" x2="21" y2="10"></line></svg>
    Day Focus
  </div>
  <div class="nav-tab" onclick="switchTab('roadmap')" id="tab-roadmap">
    <svg viewBox="0 0 24 24"><polygon points="1 6 1 22 8 18 16 22 23 18 23 2 16 6 8 2 1 6"></polygon><line x1="8" y1="2" x2="8" y2="18"></line><line x1="16" y1="6" x2="16" y2="22"></line></svg>
    180-Day Master Roadmap
  </div>
  <div class="nav-tab" onclick="switchTab('news')" id="tab-news">
    <svg viewBox="0 0 24 24"><path d="M4 22h16a2 2 0 0 0 2-2V4a2 2 0 0 0-2-2H8a2 2 0 0 0-2 2v16a2 2 0 0 1-2 2Zm0 0a2 2 0 0 1-2-2v-9c0-1.1.9-2 2-2h2"></path><path d="M18 14h-8"></path><path d="M15 18h-5"></path><path d="M10 6h8v4h-8V6Z"></path></svg>
    Current Affairs Feed
  </div>
  <div class="nav-tab" onclick="switchTab('mcqs')" id="tab-mcqs">
    <svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"></circle><path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3"></path><line x1="12" y1="17" x2="12.01" y2="17"></line></svg>
    MCQ Bank & Starred Recall
  </div>
  <div class="nav-tab" onclick="switchTab('csat')" id="tab-csat">
    <svg viewBox="0 0 24 24"><path d="M6 2v14a6 6 0 0 0 12 0V2"></path><line x1="6" y1="6" x2="18" y2="6"></line><line x1="6" y1="10" x2="18" y2="10"></line></svg>
    CSAT Lab (UNGIST Mastery)
  </div>
</nav>

<!-- MAIN APP BODY -->
<main class="app-container">

  <!-- TAB 1: DAY FOCUS (TODAY ENGINE) -->
  <section class="tab-content active" id="content-today">
    
    <!-- Neil Sir Mental Anchor (Prominent) -->
    <div class="neil-sir-hero">
      <div class="neil-sir-label">
        <svg class="icon-svg" width="14" height="14" viewBox="0 0 24 24" style="stroke:var(--gold-bright);"><circle cx="12" cy="12" r="10"></circle><line x1="12" y1="16" x2="12" y2="12"></line><line x1="12" y1="8" x2="12.01" y2="8"></line></svg>
        Neil Sir Principle of the Day
      </div>
      <div class="neil-sir-quote" id="neil-sir-text">
        "UPSC is not testing photographic memory; it tests your clarity under ambiguity. Eliminate the extreme statement first."
      </div>
    </div>

    <!-- Weekly Revision Mode Banner (Shown on Mock Days) -->
    <div class="mock-day-banner" id="mock-banner" style="display:none;">
      <div>
        <div class="mock-day-title">Weekly Consolidation & Sectional Mock Exam Mode</div>
        <div class="mock-day-sub">Today is dedicated to consolidating error notebooks and attempting the timed sectional simulation test.</div>
      </div>
      <span class="candidate-badge" style="background:var(--green-dim); color:var(--green-bright); border-color:rgba(16,185,129,0.3);">Mock Day</span>
    </div>

    <!-- Day Header Metadata -->
    <div class="day-header-meta">
      <div class="day-title-wrap">
        <h1 id="day-heading">Day 1: Parliament: Composition, Sessions & Presiding Officers</h1>
        <div class="day-sub-info">
          <span id="day-date-display">Tuesday, 24 November 2026</span>
          <span>•</span>
          <span class="phase-pill" id="phase-pill">Phase 1: Foundational Concept Building</span>
          <span>•</span>
          <span id="week-display">Week 1 of 26</span>
        </div>
      </div>
      <div class="progress-summary">
        <span style="color:var(--muted);">Checkpoints:</span>
        <span id="day-progress-text" style="color:var(--gold-bright);">0 / 4 Completed</span>
      </div>
    </div>

    <!-- TWO DISTINCT STUDY BOXES (06:00-08:00 & 20:30-22:30) -->
    <div class="study-blocks-grid">
      
      <!-- Morning Box: Static Foundational Concept -->
      <div class="study-card">
        <div class="card-top morning">
          <div class="card-title-group">
            <svg class="icon-svg" width="16" height="16" viewBox="0 0 24 24" style="stroke:var(--gold-bright);">
              <circle cx="12" cy="12" r="5"></circle>
              <line x1="12" y1="1" x2="12" y2="3"></line>
              <line x1="12" y1="21" x2="12" y2="23"></line>
              <line x1="4.22" y1="4.22" x2="5.64" y2="5.64"></line>
              <line x1="18.36" y1="18.36" x2="19.78" y2="19.78"></line>
              <line x1="1" y1="12" x2="3" y2="12"></line>
              <line x1="21" y1="12" x2="23" y2="12"></line>
            </svg>
            <div class="card-heading">Morning Block • Static Foundation</div>
          </div>
          <span class="time-badge morning">06:00 – 08:00 AM (2h)</span>
        </div>
        <div class="card-body">
          <div class="source-pill-box">
            <div>
              <div class="source-tag">Core Source Textbook</div>
              <div class="source-text" id="morning-source-text">Laxmikanth Ch 22: Parliament</div>
            </div>
            <span class="phase-pill" id="morning-subj-badge">Polity</span>
          </div>

          <!-- Micro-Checkpoints List -->
          <div>
            <div style="font-size:11px; font-weight:700; text-transform:uppercase; color:var(--muted); letter-spacing:0.05em; margin-bottom:8px;">
              Granular Sub-Topic Checkpoints
            </div>
            <div class="sub-items-container" id="morning-sub-items">
              <!-- Rendered via JS -->
            </div>
          </div>

          <!-- Personal Recall Notes -->
          <div class="notes-container">
            <div class="notes-label">
              <span>Personal Touch & Mnemonic Notes</span>
              <span id="note-save-indicator" style="color:var(--green-bright); display:none;">Saved</span>
            </div>
            <textarea id="topic-notes-input" class="notes-textarea" placeholder="Add keywords, mnemonics, or tricky exceptions to remember for quick recall..."></textarea>
            <button class="save-note-btn" onclick="saveCurrentTopicNotes()">Save Note</button>
          </div>
        </div>
      </div>

      <!-- Evening Box: Current Affairs & CSAT Practice -->
      <div class="study-card">
        <div class="card-top evening">
          <div class="card-title-group">
            <svg class="icon-svg" width="16" height="16" viewBox="0 0 24 24" style="stroke:var(--blue-bright);">
              <path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"></path>
            </svg>
            <div class="card-heading">Evening Block • Current Affairs & CSAT</div>
          </div>
          <span class="time-badge evening">20:30 – 22:30 PM (2h)</span>
        </div>
        <div class="card-body">
          
          <!-- Current Affairs Target Card -->
          <div class="evening-target-box">
            <div class="target-header">
              <span>Daily Current Affairs Target</span>
              <span id="ca-pillar-badge" class="pillar-badge Polity">Polity</span>
            </div>
            <div class="target-title" id="evening-ca-target">5 Articles + 5-10 Inline MCQs</div>
            <div class="target-subtext">Review the latest editorial and official releases with UPSC relevance scoring.</div>
            <button class="target-action-btn" onclick="switchTab('news')">Open Current Affairs Feed</button>
          </div>

          <!-- CSAT Target Card -->
          <div class="evening-target-box">
            <div class="target-header">
              <span>CSAT Daily Target (UNGIST Material)</span>
              <span style="color:var(--gold-bright); font-size:11px; font-weight:700;">20–30 Mins</span>
            </div>
            <div class="target-title" id="evening-csat-title">UNGIST Ch 1: Unit Digit Cyclicity & Remainder Theorem</div>
            <div class="target-subtext" id="evening-csat-subtext">Master the 4-step Ferris wheel loop and solve 5 daily arithmetic problems with zero algebra.</div>
            <button class="target-action-btn" onclick="switchTab('csat')">Open CSAT Mastery Lab</button>
          </div>

          <!-- Quick Daily Tasks -->
          <div style="font-size:12px; color:var(--muted); line-height:1.4; border-top:1px solid var(--border); padding-top:10px;">
            <div style="font-weight:600; color:var(--text); margin-bottom:4px;">Evening Routine Checklist:</div>
            <div>• 45 Mins: Read 5 CA Articles & mark read</div>
            <div>• 45 Mins: CSAT module concept + 5 practice problems</div>
            <div>• 30 Mins: Solve the 25 Day Practice MCQs below</div>
          </div>

        </div>
      </div>

    </div>

    <!-- DAY SPECIFIC PRACTICE MCQS SECTION (25 Questions) -->
    <div class="day-mcqs-section">
      <div class="mcq-sec-header">
        <div class="mcq-sec-title">
          <svg class="icon-svg" width="18" height="18" viewBox="0 0 24 24" style="stroke:var(--gold-bright);">
            <circle cx="12" cy="12" r="10"></circle>
            <path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3"></path>
            <line x1="12" y1="17" x2="12.01" y2="17"></line>
          </svg>
          Day Practice Questions (25 UPSC Pattern MCQs)
        </div>
        <div class="mcq-stats-pill" id="day-mcq-score-pill">Solved: 0 / 25</div>
      </div>
      <div class="mcqs-deck-grid" id="day-mcqs-list">
        <!-- Rendered via JS -->
      </div>
    </div>

  </section>

  <!-- TAB 2: 180-DAY MASTER ROADMAP -->
  <section class="tab-content" id="content-roadmap">
    <div class="roadmap-filter-bar">
      <div class="filter-pills-group" id="roadmap-phase-filters">
        <button class="filter-pill-btn active" onclick="filterRoadmapPhase('all', this)">All 180 Days</button>
        <button class="filter-pill-btn" onclick="filterRoadmapPhase(1, this)">Phase 1: Foundation (1–105)</button>
        <button class="filter-pill-btn" onclick="filterRoadmapPhase(2, this)">Phase 2: Revision & PT365 (106–140)</button>
        <button class="filter-pill-btn" onclick="filterRoadmapPhase(3, this)">Phase 3: Simulation Mocks (141–180)</button>
        <button class="filter-pill-btn" onclick="filterRoadmapPhase('mock', this)">Mock Days (Every 7th Day)</button>
      </div>
      <div style="font-size:12px; color:var(--muted);">
        Click any day to jump directly to its study agenda
      </div>
    </div>
    <div class="roadmap-grid" id="roadmap-cards-grid">
      <!-- Rendered via JS -->
    </div>
  </section>

  <!-- TAB 3: CURRENT AFFAIRS FEED -->
  <section class="tab-content" id="content-news">
    <div class="ca-controls-bar">
      <div class="ca-search-row">
        <input type="text" id="ca-search-input" class="ca-search-input" placeholder="Search news by topic, ministry, scheme, or keyword..." oninput="onCASearchChange(this.value)">
        <button class="ca-refresh-btn" onclick="refreshLiveNewsFeed()" id="ca-refresh-btn">
          <svg class="icon-svg" width="14" height="14" viewBox="0 0 24 24"><polyline points="23 4 23 10 17 10"></polyline><polyline points="1 20 1 14 7 14"></polyline><path d="M3.51 9a9 9 0 0 1 14.85-3.36L23 10M1 14l4.64 4.36A9 9 0 0 0 20.49 15"></path></svg>
          Refresh Live News
        </button>
      </div>
      <div class="ca-filter-row">
        <div class="filter-pills-group" id="ca-pillar-filters">
          <button class="filter-pill-btn active" onclick="filterCAPillar('all', this)">All Pillars</button>
          <button class="filter-pill-btn" onclick="filterCAPillar('Polity', this)">Polity</button>
          <button class="filter-pill-btn" onclick="filterCAPillar('Economy', this)">Economy</button>
          <button class="filter-pill-btn" onclick="filterCAPillar('Environment', this)">Environment</button>
          <button class="filter-pill-btn" onclick="filterCAPillar('SciTech', this)">SciTech</button>
          <button class="filter-pill-btn" onclick="filterCAPillar('IR', this)">IR & Geopolitics</button>
          <button class="filter-pill-btn" onclick="filterCAPillar('Geography', this)">Geography</button>
          <button class="filter-pill-btn" onclick="filterCAPillar('History', this)">History & Culture</button>
        </div>
        <div class="unread-toggle-wrap">
          <input type="checkbox" id="ca-unread-only" onchange="onUnreadOnlyToggle(this.checked)" class="custom-checkbox">
          <label for="ca-unread-only" style="cursor:pointer; font-weight:600;">Show Unread Only</label>
        </div>
      </div>
    </div>

    <!-- CA Articles Feed Grid -->
    <div class="ca-articles-grid" id="ca-articles-container">
      <!-- Rendered via JS -->
    </div>
  </section>

  <!-- TAB 4: MCQ BANK & STARRED RECALL -->
  <section class="tab-content" id="content-mcqs">
    <div class="roadmap-filter-bar">
      <div class="filter-pills-group" id="mcq-bank-filters">
        <button class="filter-pill-btn active" onclick="filterMCQBank('starred', this)">Starred Recall Deck</button>
        <button class="filter-pill-btn" onclick="filterMCQBank('Polity', this)">Polity</button>
        <button class="filter-pill-btn" onclick="filterMCQBank('Economy', this)">Economy</button>
        <button class="filter-pill-btn" onclick="filterMCQBank('Geography', this)">Geography</button>
        <button class="filter-pill-btn" onclick="filterMCQBank('Environment', this)">Environment</button>
        <button class="filter-pill-btn" onclick="filterMCQBank('History', this)">History & Culture</button>
        <button class="filter-pill-btn" onclick="filterMCQBank('SciTech', this)">SciTech</button>
        <button class="filter-pill-btn" onclick="filterMCQBank('CSAT', this)">CSAT</button>
      </div>
      <div id="mcq-bank-count-pill" class="candidate-badge">0 Questions</div>
    </div>
    <div class="mcqs-deck-grid" id="mcq-bank-container">
      <!-- Rendered via JS -->
    </div>
  </section>

  <!-- TAB 5: CSAT LAB (UNGIST MASTERY) -->
  <section class="tab-content" id="content-csat">
    <div style="margin-bottom:20px;">
      <h2 style="font-size:18px; font-weight:700;">CSAT Mastery Lab (UNGIST Concept Breakdowns)</h2>
      <p style="font-size:12.5px; color:var(--muted); margin-top:4px;">
        Zero formulas. Zero algebraic x and y. Pure 6th-grade visual intuition models from Ram Mohan Pandey's UNGIST curriculum.
      </p>
    </div>
    <div class="csat-modules-grid" id="csat-modules-container">
      <!-- Rendered via JS from /api/csat -->
    </div>
  </section>

</main>

<!-- SLIDE-OVER DRAWER FOR ARTICLE MCQS -->
<div class="drawer-overlay" id="drawer-overlay" onclick="closeDrawer()"></div>
<div class="drawer-panel" id="drawer-panel">
  <div class="drawer-header">
    <div class="drawer-title" id="drawer-article-title">Article Analysis & MCQs</div>
    <button class="drawer-close-btn" onclick="closeDrawer()">&times;</button>
  </div>
  <div id="drawer-body-content">
    <!-- Populated via JS -->
  </div>
</div>

<script>
// Master State & Variables
let allCurriculum = [];
let allCA = [];
let csatModules = [];
let currentDay = 1;
let userState = {
  checks: {},
  sub_checks: {},
  notes: {},
  read_articles: {},
  starred_mcqs: {},
  mcq_answers: {}
};

// Current filters
let activeRoadmapPhase = 'all';
let activeCAPillar = 'all';
let caSearchTerm = '';
let caUnreadOnly = false;
let activeMCQFilter = 'starred';

// INITIALIZATION
window.addEventListener('DOMContentLoaded', async () => {
  await loadState();
  await loadCurriculum();
  await loadCAData();
  await loadCSATData();
  
  initDaySelector();
  renderDayView(currentDay);
  renderRoadmap();
  renderCAList();
  renderMCQBank();
  renderCSATModules();
});

// 1. STATE PERSISTENCE
async function loadState() {
  try {
    const res = await fetch('/api/state');
    if (res.ok) {
      userState = await res.json();
      if (!userState.checks) userState.checks = {};
      if (!userState.sub_checks) userState.sub_checks = {};
      if (!userState.notes) userState.notes = {};
      if (!userState.read_articles) userState.read_articles = {};
      if (!userState.starred_mcqs) userState.starred_mcqs = {};
      if (!userState.mcq_answers) userState.mcq_answers = {};
    }
  } catch (e) {
    console.warn('Using local fallback state:', e);
  }
}

async function saveState() {
  try {
    await fetch('/api/state', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(userState)
    });
  } catch (e) {
    console.error('Save state error:', e);
  }
}

// 2. DATA LOADERS
async function loadCurriculum() {
  try {
    const res = await fetch('/api/curriculum');
    if (res.ok) {
      allCurriculum = await res.json();
    }
  } catch (e) {
    console.error('Curriculum load error:', e);
  }
}

async function loadCAData() {
  try {
    const res = await fetch('/api/ca?include_mcqs=true');
    if (res.ok) {
      allCA = await res.json();
    }
  } catch (e) {
    console.error('CA load error:', e);
  }
}

async function loadCSATData() {
  try {
    const res = await fetch('/api/csat');
    if (res.ok) {
      csatModules = await res.json();
    }
  } catch (e) {
    console.error('CSAT load error:', e);
  }
}

// 3. DAY NAVIGATION & SELECTOR
function initDaySelector() {
  const sel = document.getElementById('day-selector');
  sel.innerHTML = '';
  for (let i = 1; i <= 180; i++) {
    const opt = document.createElement('option');
    opt.value = i;
    opt.textContent = `Day ${i} of 180`;
    sel.appendChild(opt);
  }
}

function onDaySelectChange(val) {
  jumpToDay(parseInt(val, 10));
}

function prevDay() {
  if (currentDay > 1) jumpToDay(currentDay - 1);
}

function nextDay() {
  if (currentDay < 180) jumpToDay(currentDay + 1);
}

function jumpToToday() {
  // Compute day index from start date (2026-11-24)
  const start = new Date(2026, 10, 24); // Month is 0-indexed (10 = Nov)
  const today = new Date();
  const diffTime = today - start;
  const diffDays = Math.floor(diffTime / (1000 * 60 * 60 * 24)) + 1;
  const targetDay = Math.min(Math.max(diffDays, 1), 180);
  jumpToDay(targetDay);
}

function jumpToDay(dayNum) {
  currentDay = dayNum;
  document.getElementById('day-selector').value = dayNum;
  renderDayView(currentDay);
  if (document.getElementById('content-today').classList.contains('active')) {
    window.scrollTo({ top: 0, behavior: 'smooth' });
  }
}

// 4. DAY VIEW RENDERING
function renderDayView(dayNum) {
  const dayData = allCurriculum.find(d => d.day === dayNum) || allCurriculum[0];
  if (!dayData) return;

  // Header info
  document.getElementById('day-heading').textContent = `Day ${dayData.day}: ${dayData.topic_title}`;
  document.getElementById('day-date-display').textContent = dayData.date_display || dayData.date;
  document.getElementById('phase-pill').textContent = dayData.phase_name;
  document.getElementById('week-display').textContent = `Week ${dayData.week} of 26`;

  // Neil Sir Mental Principle
  document.getElementById('neil-sir-text').textContent = dayData.neil_sir_principle || 'Eliminate the extreme option first.';

  // Mock Day Banner
  const mockBanner = document.getElementById('mock-banner');
  mockBanner.style.display = dayData.is_mock_day ? 'flex' : 'none';

  // Morning Block
  document.getElementById('morning-source-text').textContent = dayData.core_sources;
  document.getElementById('morning-subj-badge').textContent = dayData.subjects ? dayData.subjects[0] : 'GS';

  // Sub-items checkpoints
  const subContainer = document.getElementById('morning-sub-items');
  subContainer.innerHTML = '';
  let completedCount = 0;
  const subList = dayData.sub_items || [];

  subList.forEach(sub => {
    const isChecked = !!userState.sub_checks[sub.id];
    if (isChecked) completedCount++;

    const row = document.createElement('div');
    row.className = `sub-item-row ${isChecked ? 'completed' : ''}`;
    row.id = `row-${sub.id}`;

    const cb = document.createElement('input');
    cb.type = 'checkbox';
    cb.className = 'custom-checkbox';
    cb.checked = isChecked;
    cb.onchange = () => toggleSubCheck(sub.id, cb.checked);

    const lbl = document.createElement('label');
    lbl.className = 'sub-item-label';
    lbl.textContent = sub.text;
    lbl.onclick = () => { cb.checked = !cb.checked; toggleSubCheck(sub.id, cb.checked); };

    row.appendChild(cb);
    row.appendChild(lbl);
    subContainer.appendChild(row);
  });

  document.getElementById('day-progress-text').textContent = `${completedCount} / ${subList.length} Completed`;

  // Notes
  const topicId = dayData.topic_id;
  document.getElementById('topic-notes-input').value = userState.notes[topicId] || '';

  // Evening Block
  const eveningData = dayData.session_evening || {};
  document.getElementById('evening-ca-target').textContent = eveningData.ca_target || '5 Current Affairs Articles';
  document.getElementById('evening-csat-title').textContent = eveningData.csat_topic || 'CSAT Daily Target';
  const caBadge = document.getElementById('ca-pillar-badge');
  const mainSubj = dayData.subjects ? dayData.subjects[0] : 'Polity';
  caBadge.textContent = mainSubj;
  caBadge.className = `pillar-badge ${mainSubj}`;

  // Day Specific MCQs
  renderDayMCQs(dayData.day_mcqs || []);
}

function toggleSubCheck(subId, isChecked) {
  userState.sub_checks[subId] = isChecked;
  const row = document.getElementById(`row-${subId}`);
  if (row) {
    if (isChecked) row.classList.add('completed');
    else row.classList.remove('completed');
  }

  // Update progress text
  const dayData = allCurriculum.find(d => d.day === currentDay);
  if (dayData) {
    const total = dayData.sub_items ? dayData.sub_items.length : 0;
    const completed = dayData.sub_items ? dayData.sub_items.filter(s => !!userState.sub_checks[s.id]).length : 0;
    document.getElementById('day-progress-text').textContent = `${completed} / ${total} Completed`;
  }
  saveState();
}

function saveCurrentTopicNotes() {
  const dayData = allCurriculum.find(d => d.day === currentDay);
  if (!dayData) return;
  const val = document.getElementById('topic-notes-input').value;
  userState.notes[dayData.topic_id] = val;
  saveState();
  const ind = document.getElementById('note-save-indicator');
  ind.style.display = 'inline';
  setTimeout(() => { ind.style.display = 'none'; }, 2000);
}

// 5. DAY MCQS RENDERING
function renderDayMCQs(mcqs) {
  const container = document.getElementById('day-mcqs-list');
  container.innerHTML = '';
  let answeredCount = 0;

  mcqs.forEach((mcq, idx) => {
    const card = document.createElement('div');
    card.className = 'single-mcq-card';
    card.id = `mcq-card-${mcq.id}`;

    const isStarred = !!userState.starred_mcqs[mcq.id];
    const savedAns = userState.mcq_answers[mcq.id];
    if (savedAns !== undefined) answeredCount++;

    // Meta row
    const metaRow = document.createElement('div');
    metaRow.className = 'mcq-meta-row';
    metaRow.innerHTML = `
      <span>Question ${idx + 1} of ${mcqs.length} • ${mcq.topic || 'UPSC Pattern'}</span>
      <button class="star-btn ${isStarred ? 'starred' : ''}" onclick="toggleStarMCQ('${mcq.id}', this)" title="Star for Recall">
        <svg viewBox="0 0 24 24"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon></svg>
      </button>
    `;

    // Question
    const qText = document.createElement('div');
    qText.className = 'mcq-question-text';
    qText.textContent = mcq.q;

    // Options
    const optList = document.createElement('div');
    optList.className = 'mcq-options-list';

    const cleanAns = (mcq.answer || '').replace(/[()]/g, '').trim().toLowerCase();

    (mcq.options || []).forEach(opt => {
      const optItem = document.createElement('div');
      optItem.className = 'mcq-option-item';
      optItem.textContent = opt;

      const optPrefix = opt.trim().substring(0, 4).replace(/[()]/g, '').trim().toLowerCase();
      const isThisCorrect = (optPrefix === cleanAns);

      if (savedAns !== undefined) {
        optItem.classList.add('locked');
        if (isThisCorrect) optItem.classList.add('correct');
        else if (optPrefix === savedAns) optItem.classList.add('wrong');
      }

      optItem.onclick = () => {
        if (userState.mcq_answers[mcq.id] !== undefined) return;
        userState.mcq_answers[mcq.id] = optPrefix;
        saveState();

        const allOpts = optList.querySelectorAll('.mcq-option-item');
        allOpts.forEach(o => o.classList.add('locked'));

        if (isThisCorrect) {
          optItem.classList.add('correct');
        } else {
          optItem.classList.add('wrong');
          allOpts.forEach(o => {
            const p = o.textContent.trim().substring(0, 4).replace(/[()]/g, '').trim().toLowerCase();
            if (p === cleanAns) o.classList.add('correct');
          });
        }
        expBox.classList.add('visible');
        updateDayMCQScore();
      };

      optList.appendChild(optItem);
    });

    // Explanation Box
    const expBox = document.createElement('div');
    expBox.className = `mcq-explanation-box ${savedAns !== undefined ? 'visible' : ''}`;
    expBox.innerHTML = `
      <div class="exp-title">Explanation & Static Anchor:</div>
      <div>${mcq.explanation || 'Refer to relevant chapter for concept depth.'}</div>
    `;

    card.appendChild(metaRow);
    card.appendChild(qText);
    card.appendChild(optList);
    card.appendChild(expBox);
    container.appendChild(card);
  });

  document.getElementById('day-mcq-score-pill').textContent = `Solved: ${answeredCount} / ${mcqs.length}`;
}

function updateDayMCQScore() {
  const dayData = allCurriculum.find(d => d.day === currentDay);
  if (!dayData) return;
  const mcqs = dayData.day_mcqs || [];
  const answered = mcqs.filter(m => userState.mcq_answers[m.id] !== undefined).length;
  document.getElementById('day-mcq-score-pill').textContent = `Solved: ${answered} / ${mcqs.length}`;
}

function toggleStarMCQ(mcqId, btn) {
  const isNowStarred = !userState.starred_mcqs[mcqId];
  userState.starred_mcqs[mcqId] = isNowStarred;
  if (btn) {
    if (isNowStarred) btn.classList.add('starred');
    else btn.classList.remove('starred');
  }
  saveState();
  renderMCQBank();
}

// 6. ROADMAP RENDERING
function renderRoadmap() {
  const container = document.getElementById('roadmap-cards-grid');
  container.innerHTML = '';

  let filtered = allCurriculum;
  if (activeRoadmapPhase === 'mock') {
    filtered = allCurriculum.filter(d => d.is_mock_day);
  } else if (activeRoadmapPhase !== 'all') {
    filtered = allCurriculum.filter(d => d.phase === parseInt(activeRoadmapPhase, 10));
  }

  filtered.forEach(day => {
    const card = document.createElement('div');
    card.className = `roadmap-day-card ${day.day === currentDay ? 'current' : ''} ${day.is_mock_day ? 'mock' : ''}`;
    card.onclick = () => {
      jumpToDay(day.day);
      switchTab('today');
    };

    card.innerHTML = `
      <div class="rm-day-top">
        <span class="rm-day-num">Day ${day.day}</span>
        <span class="rm-day-date">${day.date}</span>
      </div>
      <div class="rm-day-title">${day.topic_title}</div>
      <div class="rm-day-footer">
        <span>${day.subjects ? day.subjects[0] : 'GS'}</span>
        <span>${day.is_mock_day ? 'Mock Day' : day.core_sources}</span>
      </div>
    `;
    container.appendChild(card);
  });
}

function filterRoadmapPhase(phase, btn) {
  activeRoadmapPhase = phase;
  const btns = document.querySelectorAll('#roadmap-phase-filters .filter-pill-btn');
  btns.forEach(b => b.classList.remove('active'));
  btn.classList.add('active');
  renderRoadmap();
}

// 7. CURRENT AFFAIRS RENDERING
function renderCAList() {
  const container = document.getElementById('ca-articles-container');
  container.innerHTML = '';

  let filtered = allCA;
  if (activeCAPillar !== 'all') {
    filtered = filtered.filter(a => a.pillar && a.pillar.toLowerCase() === activeCAPillar.toLowerCase());
  }
  if (caSearchTerm.trim()) {
    const q = caSearchTerm.toLowerCase();
    filtered = filtered.filter(a => (a.title && a.title.toLowerCase().includes(q)) || (a.pillar && a.pillar.toLowerCase().includes(q)));
  }
  if (caUnreadOnly) {
    filtered = filtered.filter(a => !userState.read_articles[a.id]);
  }

  filtered.forEach(art => {
    const isRead = !!userState.read_articles[art.id];
    const card = document.createElement('div');
    card.className = 'ca-article-card';
    card.id = `ca-card-${art.id}`;

    const bullets = (art.summary_points || []).map(p => `<li>${p}</li>`).join('');

    card.innerHTML = `
      <div class="ca-card-top-meta">
        <div class="ca-badges-group">
          <span class="pillar-badge ${art.pillar}">${art.pillar}</span>
          <span style="font-size:11px; color:var(--muted);">${art.source || 'The Hindu'} • ${art.date}</span>
        </div>
        <span class="prob-badge">${art.relevance_score || 92}% Prelims Probability</span>
      </div>
      <div class="ca-article-title">
        <a href="javascript:void(0)" onclick="openArticleDrawer('${art.id}')">${art.title}</a>
      </div>
      <ul class="ca-summary-bullets">
        ${bullets || '<li>Key governance reform points relevant for UPSC Prelims.</li>'}
      </ul>
      <div class="ca-static-anchor-box">
        <strong>GS Static Anchor:</strong> ${art.gs_connection || 'Indian Polity & Governance'}
      </div>
      <div class="ca-card-actions">
        <button class="ca-action-btn" onclick="openArticleDrawer('${art.id}')">Practice 5 MCQs</button>
        <button class="read-status-btn ${isRead ? 'read' : ''}" onclick="toggleArticleRead('${art.id}', this)">
          ${isRead ? 'Marked as Read' : 'Mark as Read'}
        </button>
      </div>
    `;
    container.appendChild(card);
  });
}

function onCASearchChange(val) {
  caSearchTerm = val;
  renderCAList();
}

function filterCAPillar(pillar, btn) {
  activeCAPillar = pillar;
  const btns = document.querySelectorAll('#ca-pillar-filters .filter-pill-btn');
  btns.forEach(b => b.classList.remove('active'));
  btn.classList.add('active');
  renderCAList();
}

function onUnreadOnlyToggle(isChecked) {
  caUnreadOnly = isChecked;
  renderCAList();
}

function toggleArticleRead(artId, btn) {
  const isNowRead = !userState.read_articles[artId];
  userState.read_articles[artId] = isNowRead;
  if (btn) {
    if (isNowRead) {
      btn.classList.add('read');
      btn.textContent = 'Marked as Read';
    } else {
      btn.classList.remove('read');
      btn.textContent = 'Mark as Read';
    }
  }
  saveState();
  if (caUnreadOnly) renderCAList();
}

async function refreshLiveNewsFeed() {
  const btn = document.getElementById('ca-refresh-btn');
  btn.textContent = 'Refreshing...';
  try {
    const res = await fetch('/api/news/refresh');
    if (res.ok) {
      const data = await res.json();
      btn.textContent = `Refreshed (${data.count} items)`;
      await loadCAData();
      renderCAList();
    }
  } catch (e) {
    btn.textContent = 'Refresh Failed';
  }
  setTimeout(() => {
    btn.innerHTML = `
      <svg class="icon-svg" width="14" height="14" viewBox="0 0 24 24"><polyline points="23 4 23 10 17 10"></polyline><polyline points="1 20 1 14 7 14"></polyline><path d="M3.51 9a9 9 0 0 1 14.85-3.36L23 10M1 14l4.64 4.36A9 9 0 0 0 20.49 15"></path></svg>
      Refresh Live News
    `;
  }, 2500);
}

// 8. DRAWER FOR ARTICLE MCQS
function openArticleDrawer(artId) {
  const art = allCA.find(a => a.id === artId);
  if (!art) return;

  document.getElementById('drawer-article-title').textContent = art.title;
  const body = document.getElementById('drawer-body-content');
  body.innerHTML = `
    <div style="font-size:12px; color:var(--muted); margin-bottom:14px;">
      <span class="pillar-badge ${art.pillar}">${art.pillar}</span> • ${art.source} • ${art.date}
    </div>
    <div style="font-size:13px; color:var(--text); line-height:1.5; margin-bottom:18px;">
      <strong>Core Summary:</strong>
      <ul style="margin-left:18px; margin-top:6px;">
        ${(art.summary_points || []).map(p => `<li>${p}</li>`).join('')}
      </ul>
    </div>
    <div class="ca-static-anchor-box" style="margin-bottom:20px;">
      <strong>Static Syllabus Link:</strong> ${art.gs_connection}
    </div>
    <div style="font-size:14px; font-weight:700; margin-bottom:12px; color:var(--gold-bright);">
      Practice MCQs for this Article (${(art.mcqs || []).length} Questions)
    </div>
    <div class="mcqs-deck-grid" id="drawer-mcqs-list"></div>
  `;

  // Render article MCQs inside drawer
  const container = document.getElementById('drawer-mcqs-list');
  (art.mcqs || []).forEach((mcq, idx) => {
    const card = document.createElement('div');
    card.className = 'single-mcq-card';
    card.style.background = 'var(--surface-alt)';

    const qText = document.createElement('div');
    qText.className = 'mcq-question-text';
    qText.textContent = `${idx + 1}. ${mcq.q}`;

    const optList = document.createElement('div');
    optList.className = 'mcq-options-list';

    const cleanAns = (mcq.answer || '').replace(/[()]/g, '').trim().toLowerCase();

    (mcq.options || []).forEach(opt => {
      const optItem = document.createElement('div');
      optItem.className = 'mcq-option-item';
      optItem.textContent = opt;

      const optPrefix = opt.trim().substring(0, 4).replace(/[()]/g, '').trim().toLowerCase();
      const isThisCorrect = (optPrefix === cleanAns);

      optItem.onclick = () => {
        const allOpts = optList.querySelectorAll('.mcq-option-item');
        allOpts.forEach(o => o.classList.add('locked'));
        if (isThisCorrect) {
          optItem.classList.add('correct');
        } else {
          optItem.classList.add('wrong');
          allOpts.forEach(o => {
            const p = o.textContent.trim().substring(0, 4).replace(/[()]/g, '').trim().toLowerCase();
            if (p === cleanAns) o.classList.add('correct');
          });
        }
        expBox.classList.add('visible');
      };

      optList.appendChild(optItem);
    });

    const expBox = document.createElement('div');
    expBox.className = 'mcq-explanation-box';
    expBox.innerHTML = `
      <div class="exp-title">Explanation:</div>
      <div>${mcq.explanation || ''}</div>
    `;

    card.appendChild(qText);
    card.appendChild(optList);
    card.appendChild(expBox);
    container.appendChild(card);
  });

  document.getElementById('drawer-overlay').classList.add('active');
  document.getElementById('drawer-panel').classList.add('active');
}

function closeDrawer() {
  document.getElementById('drawer-overlay').classList.remove('active');
  document.getElementById('drawer-panel').classList.remove('active');
}

// 9. MCQ BANK RENDERING
function renderMCQBank() {
  const container = document.getElementById('mcq-bank-container');
  container.innerHTML = '';

  let pool = [];

  if (activeMCQFilter === 'starred') {
    // Gather all starred MCQs across curriculum and CA
    allCurriculum.forEach(d => {
      (d.day_mcqs || []).forEach(m => {
        if (userState.starred_mcqs[m.id]) pool.push(m);
      });
    });
    allCA.forEach(a => {
      (a.mcqs || []).forEach(m => {
        if (userState.starred_mcqs[m.id]) pool.push(m);
      });
    });
  } else {
    // Gather by subject
    allCurriculum.forEach(d => {
      if (d.subjects && d.subjects[0] === activeMCQFilter) {
        (d.day_mcqs || []).forEach(m => pool.push(m));
      }
    });
  }

  document.getElementById('mcq-bank-count-pill').textContent = `${pool.length} Questions Available`;

  if (pool.length === 0) {
    container.innerHTML = `
      <div style="padding:40px 20px; text-align:center; color:var(--muted); background:var(--surface); border-radius:var(--radius); border:1px solid var(--border);">
        <p style="font-size:15px; font-weight:600; color:var(--text);">No questions found in this category.</p>
        <p style="font-size:12px; margin-top:4px;">Star any question while practicing to add it directly into your Starred Recall Deck.</p>
      </div>
    `;
    return;
  }

  // Render pool (show up to 30 at a time)
  pool.slice(0, 30).forEach((mcq, idx) => {
    const card = document.createElement('div');
    card.className = 'single-mcq-card';

    const isStarred = !!userState.starred_mcqs[mcq.id];

    card.innerHTML = `
      <div class="mcq-meta-row">
        <span>Question ${idx + 1} • ${mcq.topic || 'UPSC Prelims Question'}</span>
        <button class="star-btn ${isStarred ? 'starred' : ''}" onclick="toggleStarMCQ('${mcq.id}', this)" title="Star for Recall">
          <svg viewBox="0 0 24 24"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon></svg>
        </button>
      </div>
      <div class="mcq-question-text">${mcq.q}</div>
      <div class="mcq-options-list">
        ${(mcq.options || []).map(opt => `<div class="mcq-option-item">${opt}</div>`).join('')}
      </div>
      <div class="mcq-explanation-box visible" style="margin-top:10px;">
        <div class="exp-title">Answer: ${mcq.answer}</div>
        <div>${mcq.explanation || ''}</div>
      </div>
    `;
    container.appendChild(card);
  });
}

function filterMCQBank(filterKey, btn) {
  activeMCQFilter = filterKey;
  const btns = document.querySelectorAll('#mcq-bank-filters .filter-pill-btn');
  btns.forEach(b => b.classList.remove('active'));
  btn.classList.add('active');
  renderMCQBank();
}

// 10. CSAT LAB RENDERING
function renderCSATModules() {
  const container = document.getElementById('csat-modules-container');
  container.innerHTML = '';

  csatModules.forEach(mod => {
    const card = document.createElement('div');
    card.className = 'csat-module-card';

    const shortcuts = (mod.mental_shortcuts || []).map(s => `<li>${s}</li>`).join('');
    const pyq = mod.pyq_walkthrough || {};

    card.innerHTML = `
      <div class="csat-mod-header">
        <div class="csat-mod-title">${mod.title}</div>
        <div class="csat-mod-ref">${mod.ungist_ref}</div>
      </div>
      <div class="csat-mod-body">
        
        <!-- Child Logic Breakdown -->
        <div class="child-concept-box">
          <div class="child-concept-title">Explain Like I'm 10 • Intuitive Mental Model</div>
          <div class="child-concept-text">${mod.child_concept}</div>
        </div>

        <!-- Shortcuts / Rules -->
        <div class="shortcuts-box">
          <div class="shortcuts-title">Mental Shortcuts & Speed Formulas</div>
          <ul class="shortcuts-list">${shortcuts}</ul>
        </div>

        <!-- Solved UPSC PYQ Walkthrough -->
        <div class="pyq-walkthrough-box">
          <div class="pyq-tag">Official UPSC PYQ Step-by-Step Walkthrough</div>
          <div class="pyq-q">${pyq.question || ''}</div>
          <div class="pyq-step"><strong>Child Logic:</strong> ${pyq.step1_child_logic || ''}</div>
          <div class="pyq-step"><strong>Working:</strong> ${pyq.step2_working || ''}</div>
          <div class="pyq-ans">Answer: ${pyq.step3_answer || ''}</div>
        </div>

      </div>
    `;
    container.appendChild(card);
  });
}

// 11. TAB SWITCHER
function switchTab(tabId) {
  const tabs = document.querySelectorAll('.nav-tab');
  tabs.forEach(t => t.classList.remove('active'));
  const activeTab = document.getElementById(`tab-${tabId}`);
  if (activeTab) activeTab.classList.add('active');

  const contents = document.querySelectorAll('.tab-content');
  contents.forEach(c => c.classList.remove('active'));
  const targetContent = document.getElementById(`content-${tabId}`);
  if (targetContent) targetContent.classList.add('active');

  window.scrollTo({ top: 0, behavior: 'smooth' });
}
</script>
</body>
</html>
'''

with open(output_path, 'w') as f:
    f.write(html_content)

print(f"Successfully generated clean dashboard HTML at {output_path} (length: {len(html_content)} bytes).")
