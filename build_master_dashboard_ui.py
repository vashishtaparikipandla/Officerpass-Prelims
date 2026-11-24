"""
build_master_dashboard_ui.py
Generates the complete OfficerPass Uiverse Light UI with:
1. Day Focus: Morning Box + Evening Box (CSAT Checkpoints) + Day GS MCQs + Day CSAT Topic PYQs (interactive, hidden answers)
2. 180-Day Roadmap with jump actions
3. Current Affairs Feed with Date Selector, Local Persistence, 2-3 line summaries & Drawer MCQs
4. MCQ Bank & Starred Recall: Interactive options, answers hidden until clicked, instant green/red, Starred deck
5. Official UPSC PYQ Bank (1995-2026): 4,140 questions, official year tags, subject & era filters, interactive practice
6. CSAT Lab: Day-by-Day Navigator (1-180) + UNGIST Concept Compendium
"""

import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_PATH = os.path.join(BASE_DIR, 'dashboard', 'index.html')

HTML_CONTENT = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>OfficerPass — UPSC Prelims Command Engine</title>
<style>
/* UIVERSE GALAXY LIGHT THEME SYSTEM */
:root {
  --bg: #f8fafc;
  --surface: #ffffff;
  --surface-alt: #f1f5f9;
  --surface-hover: #f8fafc;
  --border: #e2e8f0;
  --border-light: #cbd5e1;
  --border-focus: #3b82f6;
  
  --text-main: #0f172a;
  --text-body: #1e293b;
  --text-muted: #64748b;
  --text-subtle: #94a3b8;
  
  --primary: #2563eb;
  --primary-hover: #1d4ed8;
  --primary-light: #eff6ff;
  --primary-border: #bfdbfe;
  
  --amber: #d97706;
  --amber-light: #fffbeb;
  --amber-border: #fde68a;
  --amber-text: #92400e;
  
  --emerald: #059669;
  --emerald-light: #ecfdf5;
  --emerald-border: #a7f3d0;
  --emerald-text: #065f46;
  
  --rose: #e11d48;
  --rose-light: #fff1f2;
  --rose-border: #fecdd3;
  --rose-text: #9f1239;
  
  --indigo: #4f46e5;
  --indigo-light: #eef2ff;
  --indigo-border: #c7d2fe;
  --indigo-text: #3730a3;
  
  --radius-sm: 6px;
  --radius: 10px;
  --radius-lg: 16px;
  --radius-full: 9999px;
  
  --shadow-sm: 0 1px 2px 0 rgba(0, 0, 0, 0.05);
  --shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.07), 0 2px 4px -2px rgba(0, 0, 0, 0.05);
  --shadow-md: 0 10px 15px -3px rgba(0, 0, 0, 0.08), 0 4px 6px -4px rgba(0, 0, 0, 0.04);
  --shadow-lg: 0 20px 25px -5px rgba(0, 0, 0, 0.08), 0 8px 10px -6px rgba(0, 0, 0, 0.03);
}

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  -webkit-font-smoothing: antialiased;
}

body {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
  background-color: var(--bg);
  color: var(--text-body);
  line-height: 1.5;
  min-height: 100vh;
}

/* HEADER & TOP NAVBAR */
.app-header {
  background: var(--surface);
  border-bottom: 1px solid var(--border);
  position: sticky;
  top: 0;
  z-index: 50;
  box-shadow: var(--shadow-sm);
}

.header-inner {
  max-width: 1400px;
  margin: 0 auto;
  padding: 12px 24px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 16px;
}

.brand-wrap {
  display: flex;
  align-items: center;
  gap: 12px;
}

.brand-badge {
  background: var(--text-main);
  color: #ffffff;
  padding: 4px 8px;
  border-radius: var(--radius-sm);
  font-size: 11px;
  font-weight: 800;
  letter-spacing: 0.08em;
  text-transform: uppercase;
}

.brand-title {
  font-size: 17px;
  font-weight: 800;
  color: var(--text-main);
  letter-spacing: -0.02em;
}

.brand-sub {
  font-size: 11px;
  color: var(--text-muted);
  font-weight: 500;
}

.candidate-badge {
  display: flex;
  align-items: center;
  gap: 8px;
  background: var(--surface-alt);
  border: 1px solid var(--border);
  padding: 6px 12px;
  border-radius: var(--radius-full);
  font-size: 12px;
  color: var(--text-body);
}

.candidate-dot {
  width: 7px;
  height: 7px;
  background: var(--emerald);
  border-radius: 50%;
}

/* NAVIGATION BAR */
.nav-tabs-bar {
  background: var(--surface);
  border-bottom: 1px solid var(--border);
  overflow-x: auto;
  white-space: nowrap;
  scrollbar-width: none;
  -webkit-overflow-scrolling: touch;
}
.nav-tabs-bar::-webkit-scrollbar { display: none; }

.nav-tabs-inner {
  max-width: 1400px;
  margin: 0 auto;
  padding: 0 24px;
  display: flex;
  gap: 4px;
}

.nav-tab {
  padding: 14px 18px;
  font-size: 13.5px;
  font-weight: 600;
  color: var(--text-muted);
  cursor: pointer;
  border-bottom: 2px solid transparent;
  transition: all 0.15s ease;
  display: inline-flex;
  align-items: center;
  gap: 8px;
}

.nav-tab:hover {
  color: var(--text-main);
  background: var(--surface-hover);
}

.nav-tab.active {
  color: var(--primary);
  border-bottom-color: var(--primary);
  background: #ffffff;
}

.nav-tab svg {
  width: 16px;
  height: 16px;
  stroke: currentColor;
  stroke-width: 2;
  fill: none;
}

/* MAIN CONTENT CONTAINER */
.app-container {
  max-width: 1400px;
  margin: 0 auto;
  padding: 24px;
}

.tab-content {
  display: none;
}
.tab-content.active {
  display: block;
  animation: fadeIn 0.2s ease-in-out;
}

@keyframes fadeIn {
  from { opacity: 0; transform: translateY(4px); }
  to { opacity: 1; transform: translateY(0); }
}

/* NEIL SIR MENTAL ANCHOR HERO */
.neil-sir-hero {
  background: var(--surface);
  border: 1px solid var(--border);
  border-left: 4px solid var(--amber);
  border-radius: var(--radius);
  padding: 18px 24px;
  margin-bottom: 24px;
  box-shadow: var(--shadow-sm);
}

.neil-sir-label {
  font-size: 11px;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.06em;
  color: var(--amber-text);
  margin-bottom: 6px;
  display: flex;
  align-items: center;
  gap: 6px;
}

.neil-sir-quote {
  font-size: 15.5px;
  font-weight: 700;
  color: var(--text-main);
  line-height: 1.45;
}

/* DAY SELECTOR & META BAR */
.day-control-card {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: var(--radius-lg);
  padding: 20px 24px;
  margin-bottom: 24px;
  box-shadow: var(--shadow-sm);
}

.day-control-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  flex-wrap: wrap;
  gap: 16px;
  margin-bottom: 16px;
}

.day-heading-wrap h1 {
  font-size: 20px;
  font-weight: 800;
  color: var(--text-main);
  letter-spacing: -0.02em;
}

.day-sub-meta {
  font-size: 12.5px;
  color: var(--text-muted);
  margin-top: 4px;
}

.day-nav-actions {
  display: flex;
  align-items: center;
  gap: 8px;
}

.day-select-input {
  background: var(--surface-alt);
  border: 1px solid var(--border);
  color: var(--text-main);
  padding: 8px 14px;
  border-radius: var(--radius);
  font-size: 13.5px;
  font-weight: 600;
  cursor: pointer;
  outline: none;
}

.btn-icon {
  background: var(--surface);
  border: 1px solid var(--border);
  color: var(--text-body);
  padding: 8px 14px;
  border-radius: var(--radius);
  font-size: 12px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.15s;
  display: inline-flex;
  align-items: center;
  gap: 6px;
}

.btn-icon:hover {
  background: var(--surface-alt);
  border-color: var(--border-light);
}

/* STUDY BOXES: 2-COLUMN TIMETABLE */
.study-boxes-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 20px;
  margin-bottom: 28px;
}

@media (max-width: 900px) {
  .study-boxes-grid { grid-template-columns: 1fr; }
}

.study-box {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: var(--radius-lg);
  padding: 24px;
  box-shadow: var(--shadow-sm);
  display: flex;
  flex-direction: column;
}

.study-box-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 16px;
  padding-bottom: 14px;
  border-bottom: 1px solid var(--border);
}

.study-time-pill {
  background: var(--primary-light);
  color: var(--primary);
  border: 1px solid var(--primary-border);
  font-size: 11.5px;
  font-weight: 700;
  padding: 4px 10px;
  border-radius: var(--radius-full);
  display: inline-flex;
  align-items: center;
  gap: 6px;
}

.study-box-title {
  font-size: 15px;
  font-weight: 700;
  color: var(--text-main);
}

.target-card {
  background: var(--surface-alt);
  border: 1px solid var(--border);
  border-radius: var(--radius);
  padding: 18px;
  margin-bottom: 16px;
}

.target-meta-row {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 8px;
}

.prob-badge {
  background: var(--amber-light);
  color: var(--amber-text);
  border: 1px solid var(--amber-border);
  font-size: 11px;
  font-weight: 700;
  padding: 2px 8px;
  border-radius: var(--radius-full);
}

.sub-items-container {
  display: flex;
  flex-direction: column;
  gap: 10px;
  margin-top: 14px;
}

.sub-item-row {
  background: #ffffff;
  border: 1px solid var(--border);
  padding: 10px 14px;
  border-radius: var(--radius-sm);
  display: flex;
  align-items: flex-start;
  gap: 10px;
  transition: all 0.15s;
}

.sub-item-row:hover {
  border-color: var(--border-light);
  box-shadow: var(--shadow-sm);
}

.sub-item-row.completed {
  background: #f8fafc;
  border-color: #cbd5e1;
}

.sub-item-row.completed .sub-item-label {
  text-decoration: line-through;
  color: var(--text-muted);
}

.custom-checkbox {
  appearance: none;
  width: 17px;
  height: 17px;
  border: 1.5px solid #94a3b8;
  border-radius: 4px;
  margin-top: 2px;
  cursor: pointer;
  position: relative;
  transition: all 0.15s;
  flex-shrink: 0;
  background: #ffffff;
}

.custom-checkbox:checked {
  background: var(--emerald);
  border-color: var(--emerald);
}

.custom-checkbox:checked::after {
  content: "";
  position: absolute;
  top: 2px;
  left: 5px;
  width: 4px;
  height: 8px;
  border: solid #ffffff;
  border-width: 0 2px 2px 0;
  transform: rotate(45deg);
}

.sub-item-label {
  font-size: 13px;
  color: var(--text-body);
  line-height: 1.45;
  cursor: pointer;
  flex: 1;
}

.target-action-btn {
  background: #ffffff;
  border: 1px solid var(--border);
  color: var(--text-main);
  padding: 8px 14px;
  border-radius: var(--radius-sm);
  font-size: 12px;
  font-weight: 600;
  cursor: pointer;
  display: inline-flex;
  align-items: center;
  gap: 6px;
  margin-top: 12px;
  transition: all 0.15s;
}

.target-action-btn:hover {
  border-color: var(--primary);
  color: var(--primary);
}

/* PRACTICE MCQS SECTIONS */
.day-mcqs-section {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: var(--radius-lg);
  padding: 24px;
  box-shadow: var(--shadow-sm);
}

.mcq-sec-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 20px;
  padding-bottom: 14px;
  border-bottom: 1px solid var(--border);
}

.mcq-sec-title {
  font-size: 16px;
  font-weight: 800;
  color: var(--text-main);
  display: flex;
  align-items: center;
  gap: 8px;
}

.mcq-stats-pill {
  background: var(--surface-alt);
  border: 1px solid var(--border);
  font-size: 12px;
  font-weight: 700;
  padding: 4px 12px;
  border-radius: var(--radius-full);
  color: var(--text-body);
}

.mcqs-deck-grid {
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.single-mcq-card {
  background: var(--surface-alt);
  border: 1px solid var(--border);
  border-radius: var(--radius);
  padding: 20px;
}

.mcq-meta-row {
  display: flex;
  align-items: center;
  justify-content: space-between;
  font-size: 12px;
  font-weight: 600;
  color: var(--text-muted);
  margin-bottom: 12px;
}

.star-btn {
  background: none;
  border: none;
  cursor: pointer;
  color: #94a3b8;
  padding: 4px;
  display: inline-flex;
  align-items: center;
  transition: transform 0.15s, color 0.15s;
}

.star-btn svg {
  width: 17px;
  height: 17px;
  fill: transparent;
  stroke: currentColor;
  stroke-width: 2;
}

.star-btn:hover {
  transform: scale(1.15);
  color: var(--amber);
}

.star-btn.starred {
  color: var(--amber);
}
.star-btn.starred svg {
  fill: var(--amber);
}

.mcq-question-text {
  font-size: 14.5px;
  font-weight: 600;
  color: var(--text-main);
  line-height: 1.55;
  margin-bottom: 16px;
  white-space: pre-line;
}

.mcq-options-list {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.mcq-option-item {
  background: #ffffff;
  border: 1px solid var(--border);
  padding: 12px 16px;
  border-radius: var(--radius);
  font-size: 13.5px;
  color: var(--text-body);
  cursor: pointer;
  transition: all 0.15s;
  display: flex;
  align-items: flex-start;
  gap: 12px;
  word-break: break-word;
}

.mcq-option-item:hover:not(.locked) {
  border-color: var(--primary);
  background: var(--primary-light);
  transform: translateX(2px);
}

.mcq-option-item.correct {
  background: var(--emerald-light) !important;
  border-color: var(--emerald) !important;
  color: var(--emerald-text) !important;
  font-weight: 600;
}

.mcq-option-item.wrong {
  background: var(--rose-light) !important;
  border-color: var(--rose) !important;
  color: var(--rose-text) !important;
}

.mcq-option-item.locked {
  cursor: default;
}

.mcq-explanation-box {
  display: none;
  background: #ffffff;
  border: 1px solid var(--border);
  border-left: 3px solid var(--primary);
  padding: 14px 18px;
  border-radius: var(--radius);
  font-size: 13px;
  line-height: 1.55;
  color: var(--text-body);
  margin-top: 14px;
}

.mcq-explanation-box.visible {
  display: block;
  animation: fadeIn 0.2s ease-in-out;
}

.exp-title {
  font-weight: 700;
  color: var(--text-main);
  margin-bottom: 4px;
}

/* ROADMAP GRID */
.roadmap-filter-bar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  flex-wrap: wrap;
  gap: 12px;
  margin-bottom: 24px;
}

.filter-pills-group {
  display: flex;
  align-items: center;
  flex-wrap: wrap;
  gap: 6px;
}

.filter-pill-btn {
  background: var(--surface);
  border: 1px solid var(--border);
  color: var(--text-body);
  font-size: 12px;
  font-weight: 600;
  padding: 6px 14px;
  border-radius: var(--radius-full);
  cursor: pointer;
  transition: all 0.15s;
}

.filter-pill-btn:hover {
  border-color: var(--border-light);
}

.filter-pill-btn.active {
  background: var(--primary);
  border-color: var(--primary);
  color: #ffffff;
}

.roadmap-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(260px, 1fr));
  gap: 14px;
}

.roadmap-day-card {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: var(--radius);
  padding: 16px;
  cursor: pointer;
  transition: all 0.15s;
  box-shadow: var(--shadow-sm);
  display: flex;
  flex-direction: column;
}

.roadmap-day-card:hover {
  transform: translateY(-2px);
  border-color: var(--primary);
  box-shadow: var(--shadow);
}

.roadmap-day-card.current {
  border-color: var(--primary);
  background: var(--primary-light);
}

.roadmap-day-card.mock {
  border-color: var(--amber-border);
  background: var(--amber-light);
}

/* CURRENT AFFAIRS CONTROLS & CARDS */
.ca-controls-bar {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: var(--radius-lg);
  padding: 18px 24px;
  margin-bottom: 24px;
  box-shadow: var(--shadow-sm);
  display: flex;
  flex-direction: column;
  gap: 14px;
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
  color: var(--text-main);
  padding: 11px 16px;
  border-radius: var(--radius);
  font-size: 13.5px;
  box-shadow: var(--shadow-sm);
  outline: none;
}

.ca-search-input:focus {
  border-color: var(--primary);
  box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.12);
}

.ca-filter-select {
  background: var(--surface);
  border: 1px solid var(--border);
  color: var(--text-main);
  padding: 11px 16px;
  border-radius: var(--radius);
  font-size: 13px;
  font-weight: 600;
  outline: none;
  cursor: pointer;
}

.ca-refresh-btn {
  background: var(--surface);
  border: 1px solid var(--border);
  color: var(--text-main);
  font-size: 12px;
  font-weight: 600;
  padding: 11px 18px;
  border-radius: var(--radius);
  cursor: pointer;
  display: inline-flex;
  align-items: center;
  gap: 6px;
  box-shadow: var(--shadow-sm);
  transition: all 0.15s;
}

.ca-refresh-btn:hover {
  background: var(--surface-alt);
  border-color: var(--border-light);
}

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
  font-size: 12.5px;
  color: var(--text-muted);
}

.ca-articles-grid {
  display: flex;
  flex-direction: column;
  gap: 18px;
}

.ca-article-card {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: var(--radius-lg);
  padding: 22px;
  box-shadow: var(--shadow-sm);
  transition: all 0.15s;
}

.ca-article-card:hover {
  box-shadow: var(--shadow);
  border-color: var(--border-light);
}

.pillar-badge {
  font-size: 11px;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  padding: 3px 9px;
  border-radius: var(--radius-full);
}

.pillar-badge.Polity { background: #eff6ff; color: #1d4ed8; border: 1px solid #bfdbfe; }
.pillar-badge.Economy { background: #ecfdf5; color: #047857; border: 1px solid #a7f3d0; }
.pillar-badge.Environment { background: #f0fdf4; color: #15803d; border: 1px solid #bbf7d0; }
.pillar-badge.SciTech { background: #faf5ff; color: #7e22ce; border: 1px solid #e9d5ff; }
.pillar-badge.IR { background: #fff1f2; color: #be123c; border: 1px solid #fecdd3; }
.pillar-badge.Geography { background: #fefce8; color: #a16207; border: 1px solid #fef08a; }
.pillar-badge.History { background: #fdf4ff; color: #a21caf; border: 1px solid #f5d0fe; }

.year-badge-pill {
  background: var(--primary-light);
  color: var(--primary);
  border: 1px solid var(--primary-border);
  font-size: 11.5px;
  font-weight: 800;
  padding: 3px 10px;
  border-radius: var(--radius-full);
  display: inline-flex;
  align-items: center;
  gap: 4px;
}

.ca-article-title {
  font-size: 16px;
  font-weight: 700;
  color: var(--text-main);
  margin-bottom: 12px;
  line-height: 1.4;
}

.ca-summary-bullets {
  margin-left: 20px;
  font-size: 13.5px;
  color: var(--text-body);
  line-height: 1.5;
  margin-bottom: 14px;
}

.ca-static-anchor-box {
  background: var(--surface-alt);
  border: 1px solid var(--border);
  padding: 10px 14px;
  border-radius: var(--radius);
  font-size: 12.5px;
  color: var(--text-muted);
  margin-bottom: 16px;
}

.ca-card-actions {
  display: flex;
  align-items: center;
  justify-content: space-between;
  border-top: 1px solid var(--border);
  padding-top: 14px;
}

.ca-action-btn {
  background: var(--surface-alt);
  border: 1px solid var(--border);
  color: var(--text-main);
  font-size: 12px;
  font-weight: 600;
  padding: 7px 14px;
  border-radius: var(--radius-sm);
  cursor: pointer;
  transition: all 0.15s;
}

.ca-action-btn:hover {
  background: var(--primary);
  border-color: var(--primary);
  color: #fff;
}

/* CSAT MODULES & DAY CARDS */
.csat-modules-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
  gap: 18px;
}

.csat-day-card {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: var(--radius-lg);
  padding: 20px;
  box-shadow: var(--shadow-sm);
  display: flex;
  flex-direction: column;
  transition: all 0.15s;
}

.csat-day-card:hover {
  border-color: var(--primary);
  box-shadow: var(--shadow);
}

.csat-day-top-meta {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 12px;
}

.csat-day-pill {
  background: var(--primary-light);
  color: var(--primary);
  font-size: 11px;
  font-weight: 700;
  padding: 3px 9px;
  border-radius: var(--radius-full);
}

.csat-day-title {
  font-size: 15px;
  font-weight: 700;
  color: var(--text-main);
  margin-bottom: 6px;
}

.csat-day-source {
  font-size: 12px;
  color: var(--text-muted);
  margin-bottom: 12px;
}

/* DRAWER PANEL */
.drawer-overlay {
  position: fixed;
  inset: 0;
  background: rgba(15, 23, 42, 0.4);
  backdrop-filter: blur(2px);
  z-index: 100;
  display: none;
}
.drawer-overlay.active { display: block; }

.drawer-panel {
  position: fixed;
  top: 0;
  right: 0;
  bottom: 0;
  width: 100%;
  max-width: 680px;
  background: var(--surface);
  z-index: 101;
  box-shadow: var(--shadow-lg);
  transform: translateX(100%);
  transition: transform 0.25s cubic-bezier(0.16, 1, 0.3, 1);
  overflow-y: auto;
  padding: 28px;
}
.drawer-panel.active { transform: translateX(0); }

.drawer-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  border-bottom: 1px solid var(--border);
  padding-bottom: 18px;
  margin-bottom: 20px;
}

.drawer-title {
  font-size: 17px;
  font-weight: 800;
  color: var(--text-main);
}

.drawer-close-btn {
  background: var(--surface-alt);
  border: 1px solid var(--border);
  width: 32px;
  height: 32px;
  border-radius: 50%;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 18px;
}

.icon-svg {
  stroke-width: 2;
  fill: none;
}

/* =========================================================
   UI/UX PRO MAX RESPONSIVE SYSTEM FOR MOBILE & TABLET
   Preserves all colors & typography; eliminates overflow & breaks
   ========================================================= */

html, body {
  overflow-x: hidden;
  width: 100%;
  position: relative;
  -webkit-text-size-adjust: 100%;
}

button, input, select, textarea, .nav-tab, .filter-pill-btn, .mcq-option-item, .sub-item-row {
  -webkit-tap-highlight-color: transparent;
}

/* TABLET BREAKPOINT (<= 1024px) */
@media (max-width: 1024px) {
  .header-inner {
    padding: 12px 18px;
  }
  .app-container {
    padding: 20px 18px;
  }
  .study-boxes-grid {
    grid-template-columns: 1fr;
    gap: 18px;
  }
  .roadmap-grid {
    grid-template-columns: repeat(auto-fill, minmax(min(100%, 240px), 1fr));
  }
  .csat-modules-grid {
    grid-template-columns: repeat(auto-fill, minmax(min(100%, 280px), 1fr));
  }
}

/* MOBILE LANDSCAPE & PHONES (<= 768px) */
@media (max-width: 768px) {
  /* Prevent iOS input auto-zooming */
  input[type="text"], input[type="search"], select, textarea {
    font-size: 16px !important;
  }

  .header-inner {
    padding: 10px 14px;
    flex-direction: column;
    align-items: stretch;
    gap: 8px;
  }
  .brand-wrap {
    display: flex;
    align-items: center;
    justify-content: space-between;
  }
  .brand-title {
    font-size: 15.5px;
  }
  .candidate-badge {
    align-self: flex-start;
    font-size: 11px;
    padding: 4px 10px;
  }

  /* Nav tabs momentum scroll */
  .nav-tabs-inner {
    padding: 0 12px;
    gap: 2px;
  }
  .nav-tab {
    padding: 11px 12px;
    font-size: 12.5px;
    gap: 6px;
    flex-shrink: 0;
  }
  .nav-tab svg {
    width: 14px;
    height: 14px;
  }

  .app-container {
    padding: 14px 10px;
  }

  /* Hero */
  .neil-sir-hero {
    padding: 14px 14px;
    margin-bottom: 16px;
  }
  .neil-sir-quote {
    font-size: 14px;
    line-height: 1.45;
  }

  /* Day control header */
  .day-control-card {
    padding: 16px 14px;
    margin-bottom: 16px;
  }
  .day-control-header {
    flex-direction: column;
    align-items: stretch;
    gap: 12px;
  }
  .day-heading-wrap h1 {
    font-size: 17px;
    line-height: 1.35;
  }
  .day-nav-actions {
    width: 100%;
    display: grid;
    grid-template-columns: auto 1fr auto;
    gap: 6px;
  }
  .day-select-input {
    width: 100%;
    text-align: center;
    padding: 8px 6px;
  }
  .btn-icon {
    padding: 8px 10px;
    font-size: 12px;
    white-space: nowrap;
    justify-content: center;
  }

  /* Study boxes */
  .study-boxes-grid {
    grid-template-columns: 1fr;
    gap: 16px;
    margin-bottom: 20px;
  }
  .study-box {
    padding: 16px 14px;
  }
  .study-box-header {
    flex-direction: column;
    align-items: flex-start;
    gap: 8px;
    padding-bottom: 10px;
    margin-bottom: 12px;
  }
  .study-box-title {
    font-size: 14px;
  }
  .target-card {
    padding: 14px 12px;
  }
  .target-meta-row {
    flex-wrap: wrap;
    gap: 6px;
  }
  .sub-item-row {
    padding: 10px 10px;
    gap: 8px;
    min-height: 44px;
  }
  .sub-item-label {
    font-size: 12.5px;
    line-height: 1.4;
  }

  /* MCQ Sections */
  .day-mcqs-section {
    padding: 16px 12px;
  }
  .mcq-sec-header {
    flex-direction: column;
    align-items: flex-start;
    gap: 8px;
    margin-bottom: 14px;
    padding-bottom: 10px;
  }
  .single-mcq-card {
    padding: 14px 12px;
  }
  .mcq-meta-row {
    flex-wrap: wrap;
    gap: 6px;
    font-size: 11.5px;
  }
  .mcq-question-text {
    font-size: 13.5px;
    line-height: 1.5;
    margin-bottom: 12px;
  }
  .mcq-option-item {
    padding: 10px 12px;
    font-size: 13px;
    gap: 10px;
    min-height: 44px;
  }
  .mcq-explanation-box {
    padding: 12px 14px;
    font-size: 12.5px;
  }

  /* Current Affairs Controls */
  .ca-controls-bar {
    padding: 14px 12px;
    gap: 12px;
    margin-bottom: 16px;
  }
  .ca-search-row {
    flex-direction: column;
    align-items: stretch;
    gap: 10px;
  }
  .ca-search-input, .ca-filter-select, .ca-refresh-btn {
    width: 100%;
  }
  .ca-refresh-btn {
    justify-content: center;
  }
  .ca-filter-row {
    flex-direction: column;
    align-items: stretch;
    gap: 10px;
  }
  .filter-pills-group {
    display: flex;
    flex-wrap: wrap;
    gap: 6px;
    width: 100%;
  }
  .filter-pill-btn {
    padding: 5px 10px;
    font-size: 11.5px;
  }
  .ca-article-card {
    padding: 16px 12px;
  }
  .ca-article-title {
    font-size: 15px;
    line-height: 1.4;
  }
  .ca-summary-bullets {
    margin-left: 16px;
    font-size: 12.5px;
    margin-bottom: 12px;
  }
  .ca-card-actions {
    flex-direction: column;
    align-items: stretch;
    gap: 10px;
  }
  .ca-action-btn {
    width: 100%;
    text-align: center;
    padding: 10px 14px;
  }

  /* Roadmap & CSAT Grids */
  .roadmap-grid {
    grid-template-columns: 1fr;
    gap: 10px;
  }
  .csat-modules-grid {
    grid-template-columns: 1fr;
    gap: 12px;
  }
  .csat-day-card {
    padding: 16px 12px;
  }

  /* Slide-over Drawer */
  .drawer-panel {
    max-width: 100vw;
    width: 100vw;
    padding: 18px 12px;
  }
}

/* ULTRA COMPACT PHONES (<= 380px) */
@media (max-width: 380px) {
  .brand-title {
    font-size: 14.5px;
  }
  .day-heading-wrap h1 {
    font-size: 15.5px;
  }
  .btn-icon {
    padding: 7px 8px;
    font-size: 11px;
  }
  .day-nav-actions {
    gap: 4px;
  }
  .nav-tab {
    padding: 10px 10px;
    font-size: 11.5px;
  }
  .filter-pill-btn {
    padding: 4px 8px;
    font-size: 10.5px;
  }
}
</style>
</head>
<body>

<!-- TOP APPLICATION HEADER -->
<header class="app-header">
  <div class="header-inner">
    <div class="brand-wrap">
      <span class="brand-badge">UPSC 2027</span>
      <div>
        <div class="brand-title">OfficerPass Command Engine</div>
        <div class="brand-sub">Curated for Vashishta Parikipandla • OBC-NCL Final Stand</div>
      </div>
    </div>
    <div class="candidate-badge">
      <span class="candidate-dot"></span>
      <span id="header-today-date">24 Nov 2026 • 180-Day Blueprint</span>
    </div>
  </div>
</header>

<!-- NAVIGATION TABS -->
<nav class="nav-tabs-bar">
  <div class="nav-tabs-inner">
    <div class="nav-tab active" onclick="switchTab('today')" id="tab-today">
      <svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline></svg>
      Today's Focus
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
    <div class="nav-tab" onclick="switchTab('pyq')" id="tab-pyq">
      <svg viewBox="0 0 24 24"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line><polyline points="10 9 9 9 8 9"></polyline></svg>
      Official PYQ Bank (1995–2026)
    </div>
    <div class="nav-tab" onclick="switchTab('csat')" id="tab-csat">
      <svg viewBox="0 0 24 24"><path d="M6 2v14a6 6 0 0 0 12 0V2"></path><line x1="6" y1="6" x2="18" y2="6"></line><line x1="6" y1="10" x2="18" y2="10"></line></svg>
      CSAT Lab (UNGIST Mastery)
    </div>
  </div>
</nav>

<!-- MAIN APP BODY -->
<main class="app-container">

  <!-- TAB 1: DAY FOCUS -->
  <section class="tab-content active" id="content-today">
    
    <!-- Neil Sir Mental Anchor Hero -->
    <div class="neil-sir-hero">
      <div class="neil-sir-label">
        <svg class="icon-svg" width="14" height="14" viewBox="0 0 24 24" style="stroke:var(--amber);"><circle cx="12" cy="12" r="10"></circle><line x1="12" y1="16" x2="12" y2="12"></line><line x1="12" y1="8" x2="12.01" y2="8"></line></svg>
        Neil Sir Principle of the Day
      </div>
      <div class="neil-sir-quote" id="neil-sir-text">
        Mark then and there in the OMR. Second-guessing your first instinct costs 2.66 marks every single time.
      </div>
    </div>

    <!-- Day Control Header -->
    <div class="day-control-card">
      <div class="day-control-header">
        <div class="day-heading-wrap">
          <div style="display:flex; align-items:center; gap:8px; margin-bottom:4px;">
            <span class="prob-badge" id="phase-pill" style="background:var(--primary-light); color:var(--primary); border-color:var(--primary-border);">Phase 1: Foundation</span>
            <span style="font-size:12px; color:var(--text-muted);" id="week-display">Week 1 of 26</span>
          </div>
          <h1 id="day-heading">Day 1: Parliament — Composition & Anti-Defection</h1>
          <div class="day-sub-meta" id="day-date-display">Tuesday, 24 November 2026</div>
        </div>

        <div class="day-nav-actions">
          <button class="btn-icon" onclick="changeDay(-1)">
            <svg class="icon-svg" width="14" height="14" viewBox="0 0 24 24"><polyline points="15 18 9 12 15 6"></polyline></svg>
            Prev Day
          </button>
          
          <select id="day-selector" class="day-select-input" onchange="jumpToDay(parseInt(this.value, 10))">
            <!-- Populated via JS 1 to 180 -->
          </select>

          <button class="btn-icon" onclick="changeDay(1)">
            Next Day
            <svg class="icon-svg" width="14" height="14" viewBox="0 0 24 24"><polyline points="9 18 15 12 9 6"></polyline></svg>
          </button>
        </div>
      </div>

      <!-- Quick Metrics -->
      <div style="display:flex; align-items:center; justify-content:space-between; border-top:1px solid var(--border); padding-top:12px; font-size:12.5px;">
        <span style="color:var(--text-muted);">Daily Completion Progress:</span>
        <span id="day-progress-text" style="font-weight:700; color:var(--primary);">0 / 8 Checkpoints Done</span>
      </div>
    </div>

    <!-- 2-COLUMN STUDY BOXES -->
    <div class="study-boxes-grid">
      
      <!-- BOX 1: MORNING DEEP FOCUS (06:00 - 08:00 AM) -->
      <div class="study-box">
        <div class="study-box-header">
          <div>
            <span class="study-time-pill">
              <svg class="icon-svg" width="12" height="12" viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline></svg>
              06:00 – 08:00 AM (2 Hours)
            </span>
          </div>
          <div class="study-box-title">Morning Core Static Focus</div>
        </div>

        <div class="target-card">
          <div class="target-meta-row">
            <span class="pillar-badge Polity" id="morning-pillar-badge">Indian Polity</span>
            <span class="prob-badge" id="morning-prob-badge">99% Probability</span>
          </div>
          <div class="target-title" id="morning-topic-title" style="font-size:15px; font-weight:700; color:var(--text-main); margin-bottom:6px;">
            Parliament: Composition, Sessions & Presiding Officers
          </div>
          <div style="font-size:12px; color:var(--text-muted); font-weight:600;" id="morning-source-ref">
            Source: M. Laxmikanth Chapter 22
          </div>

          <div style="margin-top:12px;">
            <div style="font-size:11px; font-weight:700; text-transform:uppercase; color:var(--text-muted); letter-spacing:0.05em; margin-bottom:8px;">
              Granular Topic Checkpoints
            </div>
            <div class="sub-items-container" id="morning-sub-items">
              <!-- Rendered via JS -->
            </div>
          </div>
        </div>

        <!-- Notes -->
        <div style="margin-top:auto;">
          <label style="font-size:12px; font-weight:700; color:var(--text-muted); text-transform:uppercase; letter-spacing:0.05em; display:flex; justify-content:space-between; margin-bottom:6px;">
            <span>Personal Topic Notes & Traps</span>
            <span id="note-save-indicator" style="color:var(--emerald); display:none;">Saved to disk</span>
          </label>
          <textarea id="topic-notes-input" placeholder="Type key articles, personal mnemonics, or tricky traps here..." style="width:100%; height:75px; background:var(--surface-alt); border:1px solid var(--border); border-radius:var(--radius); padding:10px; font-size:12.5px; color:var(--text-main); resize:none; outline:none;" onblur="saveCurrentTopicNotes()"></textarea>
        </div>
      </div>

      <!-- BOX 2: EVENING CONSOLIDATION (20:30 - 22:30 PM) -->
      <div class="study-box">
        <div class="study-box-header">
          <div>
            <span class="study-time-pill" style="background:var(--amber-light); color:var(--amber-text); border-color:var(--amber-border);">
              <svg class="icon-svg" width="12" height="12" viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline></svg>
              20:30 – 22:30 PM (2 Hours)
            </span>
          </div>
          <div class="study-box-title">Evening CA & CSAT Target</div>
        </div>

        <div style="display:flex; flex-direction:column; gap:14px;">
          
          <!-- Current Affairs Anchor -->
          <div class="target-card" style="margin-bottom:0;">
            <div class="target-meta-row">
              <span class="pillar-badge Polity" id="evening-ca-badge">Polity Focus</span>
              <span class="prob-badge" style="background:#eff6ff; color:#1e40af; border-color:#bfdbfe;">45 Mins CA Revision</span>
            </div>
            <div class="target-title" style="font-size:14px; font-weight:700; color:var(--text-main);">
              Current Affairs Digest & Static Linkage
            </div>
            <div style="font-size:12px; color:var(--text-muted); margin-top:4px;" id="evening-ca-desc">
              Review curated articles and test yourself on linked prelims MCQs.
            </div>
            <button class="target-action-btn" onclick="switchTab('news')">
              Open Daily Current Affairs Feed
            </button>
          </div>

          <!-- CSAT Day-Specific Micro-Topic & Checkpoints -->
          <div class="target-card" style="margin-bottom:0; background:#ffffff; border:1px solid var(--border);">
            <div class="target-meta-row">
              <span class="pillar-badge CSAT" style="background:var(--indigo-light); color:var(--indigo-text); border-color:var(--indigo-border);">CSAT Daily Topic</span>
              <span id="evening-csat-prob" class="prob-badge" style="background:var(--primary-light); color:var(--primary); border-color:var(--primary-border);">98% Probability</span>
            </div>
            <div class="target-title" id="evening-csat-title" style="font-size:14.5px; font-weight:700; color:var(--text-main);">
              Number System: Unit Digit Cyclicity & Exponent Powers
            </div>
            <div style="font-size:11.5px; font-weight:600; color:var(--text-muted);" id="evening-csat-source">
              Source: UNGIST Chapter 1 (Pages 8–16)
            </div>

            <!-- Granular CSAT Micro-Checkpoints -->
            <div style="margin-top:10px;">
              <div style="font-size:11px; font-weight:700; text-transform:uppercase; color:var(--text-muted); letter-spacing:0.05em; margin-bottom:8px;">
                CSAT Topic Checkpoints
              </div>
              <div class="sub-items-container" id="evening-csat-sub-items">
                <!-- Rendered via JS -->
              </div>
            </div>

            <button class="target-action-btn" onclick="switchTab('csat')" style="margin-top:8px;">
              Open CSAT Daily Navigator & UNGIST Lab
            </button>
          </div>

        </div>
      </div>

    </div>

    <!-- SECTION A: DAY SPECIFIC GS PRACTICE MCQS (25 Questions) -->
    <div class="day-mcqs-section">
      <div class="mcq-sec-header">
        <div class="mcq-sec-title">
          <svg class="icon-svg" width="20" height="20" viewBox="0 0 24 24" style="stroke:var(--primary);">
            <circle cx="12" cy="12" r="10"></circle>
            <path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3"></path>
            <line x1="12" y1="17" x2="12.01" y2="17"></line>
          </svg>
          Day GS Practice Questions (UPSC Pattern MCQs)
        </div>
        <div class="mcq-stats-pill" id="day-mcq-score-pill">Solved: 0 / 25</div>
      </div>
      <div class="mcqs-deck-grid" id="day-mcqs-list">
        <!-- Rendered via JS -->
      </div>
    </div>

    <!-- SECTION B: DAY SPECIFIC CSAT PRACTICE & OFFICIAL TOPIC PYQS -->
    <div class="day-mcqs-section" style="margin-top:28px;">
      <div class="mcq-sec-header">
        <div class="mcq-sec-title">
          <svg class="icon-svg" width="20" height="20" viewBox="0 0 24 24" style="stroke:var(--indigo);">
            <path d="M6 2v14a6 6 0 0 0 12 0V2"></path>
            <line x1="6" y1="6" x2="18" y2="6"></line>
            <line x1="6" y1="10" x2="18" y2="10"></line>
          </svg>
          Evening CSAT Practice & Official Topic PYQs
        </div>
        <div class="mcq-stats-pill" id="day-csat-mcq-score-pill">CSAT Solved: 0 / 4</div>
      </div>
      <div class="mcqs-deck-grid" id="day-csat-mcqs-list">
        <!-- Rendered via JS from dayData.csat_topic_pyqs -->
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
      <div style="font-size:12px; color:var(--text-muted);">
        Click any day card to jump directly to its study agenda
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
        
        <select id="ca-date-filter" class="ca-filter-select" onchange="onCADateChange(this.value)">
          <option value="all">All Dates Accumulated</option>
          <!-- Populated via JS -->
        </select>

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
          <label for="ca-unread-only" style="cursor:pointer; font-weight:600; color:var(--text-body);">Show Unread Only</label>
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
        <button class="filter-pill-btn active" onclick="filterMCQBank('starred', this)">
          Starred Recall Deck
        </button>
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

    <!-- Information banner on hidden answers -->
    <div style="background:var(--surface); border:1px solid var(--border); border-radius:var(--radius); padding:12px 18px; margin-bottom:18px; font-size:12.5px; color:var(--text-muted); display:flex; align-items:center; gap:8px;">
      <svg class="icon-svg" width="16" height="16" viewBox="0 0 24 24" style="stroke:var(--primary);"><circle cx="12" cy="12" r="10"></circle><line x1="12" y1="16" x2="12" y2="12"></line><line x1="12" y1="8" x2="12.01" y2="8"></line></svg>
      <span>Answers and explanations are hidden by default to test your recall. Click any option to verify whether you are right or wrong and unlock the full rationale.</span>
    </div>

    <div class="mcqs-deck-grid" id="mcq-bank-container">
      <!-- Rendered via JS -->
    </div>
  </section>

  <!-- TAB 5: OFFICIAL PYQ BANK (1995–2026) -->
  <section class="tab-content" id="content-pyq">
    <div class="ca-controls-bar" style="margin-bottom:20px;">
      <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:12px; margin-bottom:10px;">
        <div>
          <h2 style="font-size:19px; font-weight:800; color:var(--text-main);">Official UPSC Previous Year Questions (1995–2026)</h2>
          <p style="font-size:12.5px; color:var(--text-muted); margin-top:2px;">
            Authentic questions purely built by UPSC with official keys & year tags. Answers are hidden until clicked.
          </p>
        </div>
        <div id="pyq-total-count-badge" class="year-badge-pill">
          4,140 Official PYQs Available
        </div>
      </div>

      <div class="ca-search-row">
        <input type="text" id="pyq-search-input" class="ca-search-input" placeholder="Search official PYQs by keyword, concept, or year (e.g. Repo, Preamble, Wildlife, 2024)..." oninput="onPYQSearchChange(this.value)">
      </div>

      <!-- Subject Filters -->
      <div class="ca-filter-row">
        <div class="filter-pills-group" id="pyq-subject-filters">
          <button class="filter-pill-btn active" onclick="filterPYQSubject('all', this)">All Subjects</button>
          <button class="filter-pill-btn" onclick="filterPYQSubject('Polity', this)">Polity (422)</button>
          <button class="filter-pill-btn" onclick="filterPYQSubject('Economy', this)">Economy (618)</button>
          <button class="filter-pill-btn" onclick="filterPYQSubject('Environment', this)">Environment (385)</button>
          <button class="filter-pill-btn" onclick="filterPYQSubject('Geography', this)">Geography (545)</button>
          <button class="filter-pill-btn" onclick="filterPYQSubject('SciTech', this)">SciTech (917)</button>
          <button class="filter-pill-btn" onclick="filterPYQSubject('Modern History', this)">Modern History (319)</button>
          <button class="filter-pill-btn" onclick="filterPYQSubject('Ancient & Medieval', this)">Ancient & Med (193)</button>
          <button class="filter-pill-btn" onclick="filterPYQSubject('Art & Culture', this)">Art & Culture (219)</button>
          <button class="filter-pill-btn" onclick="filterPYQSubject('CSAT', this)">CSAT Aptitude (177)</button>
        </div>
      </div>

      <!-- Era Filters -->
      <div style="display:flex; align-items:center; gap:8px; flex-wrap:wrap; margin-top:4px;">
        <span style="font-size:11.5px; font-weight:700; text-transform:uppercase; color:var(--text-muted); letter-spacing:0.05em;">Era:</span>
        <div class="filter-pills-group" id="pyq-era-filters">
          <button class="filter-pill-btn active" onclick="filterPYQEra('all', this)">All Years</button>
          <button class="filter-pill-btn" onclick="filterPYQEra('recent', this)">2024–2026 Recent</button>
          <button class="filter-pill-btn" onclick="filterPYQEra('contemporary', this)">2020–2023 Contemporary</button>
          <button class="filter-pill-btn" onclick="filterPYQEra('classic', this)">2015–2019 Classic</button>
          <button class="filter-pill-btn" onclick="filterPYQEra('2010_2014', this)">2010–2014</button>
          <button class="filter-pill-btn" onclick="filterPYQEra('archive', this)">1995–2009 Archive</button>
        </div>
      </div>
    </div>

    <!-- PYQ Questions Grid -->
    <div class="mcqs-deck-grid" id="pyq-deck-container">
      <!-- Rendered via JS -->
    </div>

    <!-- Load More Pagination Button -->
    <div style="text-align:center; margin-top:24px;" id="pyq-load-more-wrap">
      <button class="btn-icon" style="padding:10px 24px; font-size:13.5px;" onclick="loadMorePYQs()">
        Load More Official PYQs
      </button>
    </div>
  </section>

  <!-- TAB 6: CSAT LAB (DAY-SPECIFIC NAVIGATOR & UNGIST MASTERY) -->
  <section class="tab-content" id="content-csat">
    <div style="margin-bottom:24px; display:flex; justify-content:space-between; align-items:flex-start; flex-wrap:wrap; gap:16px;">
      <div>
        <h2 style="font-size:20px; font-weight:800; color:var(--text-main);">CSAT Daily Engine & UNGIST Mastery</h2>
        <p style="font-size:13px; color:var(--text-muted); margin-top:4px;">
          Day-specific CSAT micro-topics, checklists, and 6th-grade visual intuition models from Ram Mohan Pandey's UNGIST curriculum.
        </p>
      </div>

      <!-- Mode Toggle -->
      <div class="filter-pills-group" id="csat-view-mode-toggle">
        <button class="filter-pill-btn active" onclick="switchCSATViewMode('daily', this)">Day-by-Day CSAT (1–180)</button>
        <button class="filter-pill-btn" onclick="switchCSATViewMode('concepts', this)">UNGIST Concept Compendium</button>
      </div>
    </div>

    <!-- VIEW 1: DAY-BY-DAY CSAT SCHEDULE -->
    <div id="csat-daily-view">
      <div class="ca-controls-bar" style="margin-bottom:20px;">
        <div class="ca-search-row">
          <input type="text" id="csat-search-input" class="ca-search-input" placeholder="Search CSAT topics (e.g. Unit Digit, Averages, Trains, Sherlocking, Permutations...)" oninput="onCSATSearchChange(this.value)">
        </div>
        <div class="ca-filter-row">
          <div class="filter-pills-group" id="csat-phase-filters">
            <button class="filter-pill-btn active" onclick="filterCSATPhase('all', this)">All 180 Days</button>
            <button class="filter-pill-btn" onclick="filterCSATPhase(1, this)">Phase 1: Foundation (1–105)</button>
            <button class="filter-pill-btn" onclick="filterCSATPhase(2, this)">Phase 2: RC Intensive (106–140)</button>
            <button class="filter-pill-btn" onclick="filterCSATPhase(3, this)">Phase 3: Simulation Mocks (141–180)</button>
          </div>
          <div id="csat-schedule-count" class="candidate-badge" style="background:#eff6ff; color:#1e40af; border-color:#bfdbfe;">
            180 Daily Micro-Topics
          </div>
        </div>
      </div>

      <!-- Grid of Day-Specific CSAT Cards -->
      <div class="csat-modules-grid" id="csat-daily-grid">
        <!-- Rendered dynamically via JS -->
      </div>
    </div>

    <!-- VIEW 2: UNGIST CONCEPT COMPENDIUM (9 CORE CHAPTERS) -->
    <div id="csat-concepts-view" style="display:none;">
      <div class="csat-modules-grid" id="csat-modules-container">
        <!-- Rendered via JS from /api/csat -->
      </div>
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

// Filters State
let activeRoadmapPhase = 'all';
let activeCAPillar = 'all';
let activeCADate = 'all';
let caSearchTerm = '';
let caUnreadOnly = false;

let activeMCQFilter = 'starred';

// PYQ Bank State
let activePYQSubject = 'all';
let activePYQEra = 'all';
let pyqSearchTerm = '';
let pyqLimit = 50;
let pyqOffset = 0;
let pyqTotalAvailable = 0;
let pyqLoadedList = [];

let csatViewMode = 'daily';
let activeCSATPhase = 'all';
let csatSearchTerm = '';

// INITIALIZATION
window.addEventListener('DOMContentLoaded', async () => {
  await loadState();
  await loadCurriculum();
  await loadCAData();
  await loadCSATData();
  
  initDaySelector();
  populateCADateFilter();
  renderDayView(currentDay);
  renderRoadmap();
  renderCAList();
  renderMCQBank();
  renderCSATModules();
  renderCSATDaily();
  loadAndRenderPYQs();
});

// 1. STATE PERSISTENCE (GET / POST /api/state)
async function loadState() {
  try {
    const res = await fetch('/api/state');
    if (res.ok) {
      const data = await res.json();
      userState = {
        checks: data.checks || {},
        sub_checks: data.sub_checks || {},
        notes: data.notes || {},
        read_articles: data.read_articles || {},
        starred_mcqs: data.starred_mcqs || {},
        mcq_answers: data.mcq_answers || {}
      };
    }
  } catch (e) {
    console.error('Load state error:', e);
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
      populateCADateFilter();
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

// 3. DAY SELECTOR & NAVIGATION
function initDaySelector() {
  const sel = document.getElementById('day-selector');
  sel.innerHTML = '';
  for (let i = 1; i <= 180; i++) {
    const opt = document.createElement('option');
    opt.value = i;
    opt.textContent = `Day ${i}`;
    sel.appendChild(opt);
  }
  sel.value = currentDay;
}

function changeDay(delta) {
  const next = currentDay + delta;
  if (next >= 1 && next <= 180) {
    jumpToDay(next);
  }
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
  document.getElementById('neil-sir-text').textContent = dayData.neil_sir_principle || 'Mark then and there in the OMR. Second-guessing your first instinct costs 2.66 marks every single time.';

  // Morning Block
  const morningData = dayData.session_morning || {};
  const mainSubj = (dayData.subjects && dayData.subjects[0]) || 'Polity';
  
  const mBadge = document.getElementById('morning-pillar-badge');
  mBadge.textContent = mainSubj;
  mBadge.className = `pillar-badge ${mainSubj}`;

  document.getElementById('morning-topic-title').textContent = dayData.topic_title;
  document.getElementById('morning-source-ref').textContent = `Core Source: ${dayData.core_sources || morningData.source || 'Standard Reference'}`;

  // Morning Sub-checkpoints
  const subContainer = document.getElementById('morning-sub-items');
  subContainer.innerHTML = '';
  const gsSubList = dayData.sub_items || [];
  let completedCount = 0;

  gsSubList.forEach(sub => {
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

  // Evening Block - Current Affairs linkage
  const caBadge = document.getElementById('evening-ca-badge');
  caBadge.textContent = `${mainSubj} Current Affairs`;
  caBadge.className = `pillar-badge ${mainSubj}`;

  // Evening Block - Day-Specific CSAT Micro-Topic & Checkpoints
  const csatData = dayData.csat_micro_topic || {};
  document.getElementById('evening-csat-title').textContent = csatData.title || 'CSAT Daily Target';
  document.getElementById('evening-csat-source').textContent = csatData.ungist_ref || 'UNGIST Quantitative Aptitude & Reasoning';
  document.getElementById('evening-csat-prob').textContent = `${csatData.prob || 95}% Probability`;

  const csatSubContainer = document.getElementById('evening-csat-sub-items');
  csatSubContainer.innerHTML = '';
  const csatSubList = csatData.sub_items || [];

  csatSubList.forEach(sub => {
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
    csatSubContainer.appendChild(row);
  });

  // Total daily checkpoints (GS + CSAT)
  const totalCheckpoints = gsSubList.length + csatSubList.length;
  document.getElementById('day-progress-text').textContent = `${completedCount} / ${totalCheckpoints} Completed (${gsSubList.length} GS + ${csatSubList.length} CSAT)`;

  // Notes
  const topicId = dayData.topic_id;
  document.getElementById('topic-notes-input').value = userState.notes[topicId] || '';

  // Day Specific GS MCQs
  renderDayMCQs(dayData.day_mcqs || []);

  // Day Specific CSAT Topic PYQs
  renderDayCSATMCQs(dayData.csat_topic_pyqs || []);
}

function toggleSubCheck(subId, isChecked) {
  userState.sub_checks[subId] = isChecked;

  // Update Today tab row if present
  const row = document.getElementById(`row-${subId}`);
  if (row) {
    if (isChecked) row.classList.add('completed');
    else row.classList.remove('completed');
    const cb = row.querySelector('input[type="checkbox"]');
    if (cb) cb.checked = isChecked;
  }

  // Update CSAT Lab row if present
  const labRow = document.getElementById(`csat-lab-row-${subId}`);
  if (labRow) {
    if (isChecked) labRow.classList.add('completed');
    else labRow.classList.remove('completed');
    const labCb = labRow.querySelector('input[type="checkbox"]');
    if (labCb) labCb.checked = isChecked;
  }

  // Update progress text in Today tab
  const dayData = allCurriculum.find(d => d.day === currentDay);
  if (dayData) {
    const gsList = dayData.sub_items || [];
    const csatList = (dayData.csat_micro_topic && dayData.csat_micro_topic.sub_items) ? dayData.csat_micro_topic.sub_items : [];
    const total = gsList.length + csatList.length;
    const completed = [...gsList, ...csatList].filter(s => !!userState.sub_checks[s.id]).length;
    const progEl = document.getElementById('day-progress-text');
    if (progEl) progEl.textContent = `${completed} / ${total} Completed (${gsList.length} GS + ${csatList.length} CSAT)`;
  }

  // Update CSAT Lab card count without disrupting scroll
  if (csatViewMode === 'daily') {
    allCurriculum.forEach(d => {
      const csat = d.csat_micro_topic || {};
      const subList = csat.sub_items || [];
      if (subList.some(s => s.id === subId)) {
        const doneCount = subList.filter(s => !!userState.sub_checks[s.id]).length;
        const countEl = document.getElementById(`csat-lab-done-${d.day}`);
        if (countEl) countEl.textContent = `${doneCount} / ${subList.length} Done`;
      }
    });
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

// 5. DAY GS MCQS RENDERING
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

    // Explanation Box (Hidden until clicked)
    const expBox = document.createElement('div');
    expBox.className = `mcq-explanation-box ${savedAns !== undefined ? 'visible' : ''}`;
    expBox.innerHTML = `
      <div class="exp-title">Official Answer: ${mcq.answer}</div>
      <div>${mcq.explanation || ''}</div>
    `;

    card.appendChild(metaRow);
    card.appendChild(qText);
    card.appendChild(optList);
    card.appendChild(expBox);
    container.appendChild(card);
  });

  document.getElementById('day-mcq-score-pill').textContent = `Solved: ${answeredCount} / ${mcqs.length}`;
}

// 5b. DAY CSAT TOPIC PYQS RENDERING
function renderDayCSATMCQs(csatPyqs) {
  const container = document.getElementById('day-csat-mcqs-list');
  container.innerHTML = '';
  let answeredCount = 0;

  csatPyqs.forEach((mcq, idx) => {
    const card = document.createElement('div');
    card.className = 'single-mcq-card';
    card.id = `csat-mcq-card-${mcq.id}`;

    const isStarred = !!userState.starred_mcqs[mcq.id];
    const savedAns = userState.mcq_answers[mcq.id];
    if (savedAns !== undefined) answeredCount++;

    // Meta row with official year tag
    const metaRow = document.createElement('div');
    metaRow.className = 'mcq-meta-row';
    metaRow.innerHTML = `
      <div style="display:flex; align-items:center; gap:8px;">
        <span class="year-badge-pill" style="font-size:11px;">${mcq.year_tag || '[UPSC CSAT]'}</span>
        <span>Question ${idx + 1} of ${csatPyqs.length} • ${mcq.topic}</span>
      </div>
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
        updateDayCSATScore();
      };

      optList.appendChild(optItem);
    });

    // Explanation Box with Child Logic
    const expBox = document.createElement('div');
    expBox.className = `mcq-explanation-box ${savedAns !== undefined ? 'visible' : ''}`;
    expBox.innerHTML = `
      <div style="background:var(--primary-light); border:1px solid var(--primary-border); padding:8px 12px; border-radius:var(--radius-sm); margin-bottom:8px; font-size:12.5px; color:var(--primary); font-weight:700;">
        ${mcq.child_logic || 'Child Logic: Eliminate extreme values first.'}
      </div>
      <div class="exp-title">Official Answer: ${mcq.answer}</div>
      <div style="white-space:pre-line;">${mcq.explanation || ''}</div>
    `;

    card.appendChild(metaRow);
    card.appendChild(qText);
    card.appendChild(optList);
    card.appendChild(expBox);
    container.appendChild(card);
  });

  document.getElementById('day-csat-mcq-score-pill').textContent = `CSAT Solved: ${answeredCount} / ${csatPyqs.length}`;
}

function updateDayMCQScore() {
  const dayData = allCurriculum.find(d => d.day === currentDay);
  if (!dayData) return;
  const mcqs = dayData.day_mcqs || [];
  const answered = mcqs.filter(m => userState.mcq_answers[m.id] !== undefined).length;
  document.getElementById('day-mcq-score-pill').textContent = `Solved: ${answered} / ${mcqs.length}`;
}

function updateDayCSATScore() {
  const dayData = allCurriculum.find(d => d.day === currentDay);
  if (!dayData) return;
  const mcqs = dayData.csat_topic_pyqs || [];
  const answered = mcqs.filter(m => userState.mcq_answers[m.id] !== undefined).length;
  document.getElementById('day-csat-mcq-score-pill').textContent = `CSAT Solved: ${answered} / ${mcqs.length}`;
}

function toggleStarMCQ(mcqId, btn) {
  const isNowStarred = !userState.starred_mcqs[mcqId];
  userState.starred_mcqs[mcqId] = isNowStarred;
  if (btn) {
    if (isNowStarred) btn.classList.add('starred');
    else btn.classList.remove('starred');
  }
  saveState();
  if (activeMCQFilter === 'starred') {
    renderMCQBank();
  }
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

    const mainSubj = (day.subjects && day.subjects[0]) || 'General';
    const subList = day.sub_items || [];
    const csatSubList = (day.csat_micro_topic && day.csat_micro_topic.sub_items) ? day.csat_micro_topic.sub_items : [];
    const allSubs = [...subList, ...csatSubList];
    const doneCount = allSubs.filter(s => !!userState.sub_checks[s.id]).length;

    card.innerHTML = `
      <div style="display:flex; align-items:center; justify-content:space-between; margin-bottom:8px;">
        <span style="font-size:12px; font-weight:800; color:var(--primary);">Day ${day.day}</span>
        <span class="pillar-badge ${mainSubj}" style="font-size:10px;">${mainSubj}</span>
      </div>
      <div style="font-size:13.5px; font-weight:700; color:var(--text-main); margin-bottom:4px; line-height:1.4;">
        ${day.topic_title}
      </div>
      <div style="font-size:11.5px; color:var(--text-muted); margin-bottom:8px;">
        CSAT: ${(day.csat_micro_topic && day.csat_micro_topic.title) ? day.csat_micro_topic.title.substring(0, 32) : 'Aptitude'}...
      </div>
      <div style="margin-top:auto; padding-top:8px; border-top:1px solid var(--border); display:flex; justify-content:space-between; font-size:11.5px;">
        <span style="color:var(--text-muted);">${day.date}</span>
        <span style="font-weight:700; color:${doneCount === allSubs.length && allSubs.length > 0 ? 'var(--emerald)' : 'var(--text-muted)'};">
          ${doneCount} / ${allSubs.length} Done
        </span>
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

// 7. CURRENT AFFAIRS FEED RENDERING & LOCAL ACCUMULATION
function populateCADateFilter() {
  const sel = document.getElementById('ca-date-filter');
  if (!sel) return;
  const currentVal = sel.value;
  
  // Extract distinct dates
  const dates = [...new Set(allCA.map(a => a.date).filter(Boolean))].sort().reverse();
  
  sel.innerHTML = `<option value="all">All Dates (${allCA.length} Articles Accumulated)</option>`;
  dates.forEach(d => {
    const count = allCA.filter(a => a.date === d).length;
    const opt = document.createElement('option');
    opt.value = d;
    opt.textContent = `${d} (${count} Articles)`;
    sel.appendChild(opt);
  });
  if (dates.includes(currentVal)) {
    sel.value = currentVal;
  }
}

function onCADateChange(val) {
  activeCADate = val;
  renderCAList();
}

function renderCAList() {
  const container = document.getElementById('ca-articles-container');
  container.innerHTML = '';

  let filtered = allCA;

  // Pillar Filter
  if (activeCAPillar !== 'all') {
    filtered = filtered.filter(a => (a.pillar || '').toLowerCase() === activeCAPillar.toLowerCase());
  }

  // Date Filter
  if (activeCADate !== 'all') {
    filtered = filtered.filter(a => a.date === activeCADate);
  }

  // Search Filter
  if (caSearchTerm.trim()) {
    const q = caSearchTerm.toLowerCase();
    filtered = filtered.filter(a => {
      const t = (a.title || '').toLowerCase();
      const s = (a.summary_points || []).join(' ').toLowerCase();
      const g = (a.gs_connection || '').toLowerCase();
      return t.includes(q) || s.includes(q) || g.includes(q);
    });
  }

  // Unread filter
  if (caUnreadOnly) {
    filtered = filtered.filter(a => !userState.read_articles[a.id]);
  }

  if (filtered.length === 0) {
    container.innerHTML = `
      <div style="padding:48px; text-align:center; color:var(--text-muted); background:var(--surface); border-radius:var(--radius); border:1px solid var(--border);">
        <p style="font-size:16px; font-weight:700; color:var(--text-main);">No articles found matching criteria.</p>
        <p style="font-size:13px; margin-top:4px;">Try clearing search filters or refreshing live news feed.</p>
      </div>
    `;
    return;
  }

  filtered.forEach(art => {
    const card = document.createElement('div');
    card.className = 'ca-article-card';

    const isRead = !!userState.read_articles[art.id];
    const bulletsHtml = (art.summary_points || []).map(p => `<li>${p}</li>`).join('');

    card.innerHTML = `
      <div style="display:flex; align-items:center; justify-content:space-between; margin-bottom:12px;">
        <div style="display:flex; align-items:center; gap:8px;">
          <span class="pillar-badge ${art.pillar}">${art.pillar}</span>
          <span class="year-badge-pill" style="font-size:11px; font-weight:600; background:var(--surface-alt); color:var(--text-muted); border-color:var(--border);">
            ${art.date || 'Today'}
          </span>
          <span style="font-size:12px; color:var(--text-muted);">${art.source || 'Curated Feed'}</span>
        </div>
        <button class="read-status-btn ${isRead ? 'read' : ''}" onclick="toggleArticleRead('${art.id}', this)">
          ${isRead ? 'Read' : 'Mark as Read'}
        </button>
      </div>

      <div class="ca-article-title">${art.title}</div>
      <ul class="ca-summary-bullets">${bulletsHtml}</ul>

      <div class="ca-static-anchor-box">
        <strong>Syllabus Linkage:</strong> ${art.gs_connection || 'GS Static Integration'}
      </div>

      <div class="ca-card-actions">
        <span style="font-size:12px; color:var(--text-muted);">
          ${(art.mcqs || []).length} UPSC Practice MCQs Available
        </span>
        <button class="ca-action-btn" onclick="openArticleDrawer('${art.id}')">
          Practice MCQs for this Article
        </button>
      </div>
    `;
    container.appendChild(card);
  });
}

function filterCAPillar(pillar, btn) {
  activeCAPillar = pillar;
  const btns = document.querySelectorAll('#ca-pillar-filters .filter-pill-btn');
  btns.forEach(b => b.classList.remove('active'));
  btn.classList.add('active');
  renderCAList();
}

function onCASearchChange(val) {
  caSearchTerm = val;
  renderCAList();
}

function onUnreadOnlyToggle(checked) {
  caUnreadOnly = checked;
  renderCAList();
}

function toggleArticleRead(artId, btn) {
  const isNowRead = !userState.read_articles[artId];
  userState.read_articles[artId] = isNowRead;
  if (btn) {
    if (isNowRead) {
      btn.classList.add('read');
      btn.textContent = 'Read';
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
  btn.textContent = 'Fetching Live News...';
  try {
    const res = await fetch('/api/news/refresh');
    if (res.ok) {
      const data = await res.json();
      btn.textContent = `Accumulated (${data.count || 0} new)`;
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

// 8. DRAWER FOR ARTICLE MCQS (ANSWERS HIDDEN UNTIL CLICKED)
function openArticleDrawer(artId) {
  const art = allCA.find(a => a.id === artId);
  if (!art) return;

  document.getElementById('drawer-article-title').textContent = art.title;
  const body = document.getElementById('drawer-body-content');
  body.innerHTML = `
    <div style="font-size:12.5px; color:var(--text-muted); margin-bottom:14px;">
      <span class="pillar-badge ${art.pillar}">${art.pillar}</span> • ${art.source} • ${art.date}
    </div>
    <div style="font-size:13.5px; color:var(--text-body); line-height:1.55; margin-bottom:18px;">
      <strong style="color:var(--text-main);">Core Summary:</strong>
      <ul style="margin-left:20px; margin-top:6px;">
        ${(art.summary_points || []).map(p => `<li>${p}</li>`).join('')}
      </ul>
    </div>
    <div class="ca-static-anchor-box" style="margin-bottom:20px;">
      <strong style="color:var(--text-main);">Static Syllabus Link:</strong> ${art.gs_connection}
    </div>
    <div style="font-size:15px; font-weight:800; margin-bottom:14px; color:var(--text-main);">
      Practice MCQs for this Article (${(art.mcqs || []).length} Questions)
    </div>
    <div class="mcqs-deck-grid" id="drawer-mcqs-list"></div>
  `;

  const container = document.getElementById('drawer-mcqs-list');
  (art.mcqs || []).forEach((mcq, idx) => {
    const card = document.createElement('div');
    card.className = 'single-mcq-card';
    card.style.background = '#ffffff';

    const isStarred = !!userState.starred_mcqs[mcq.id];
    const savedAns = userState.mcq_answers[mcq.id];

    // Meta
    const metaRow = document.createElement('div');
    metaRow.className = 'mcq-meta-row';
    metaRow.innerHTML = `
      <span>Question ${idx + 1} of ${(art.mcqs || []).length}</span>
      <button class="star-btn ${isStarred ? 'starred' : ''}" onclick="toggleStarMCQ('${mcq.id}', this)" title="Star for Recall">
        <svg viewBox="0 0 24 24"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon></svg>
      </button>
    `;

    const qText = document.createElement('div');
    qText.className = 'mcq-question-text';
    qText.textContent = mcq.q;

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
      };

      optList.appendChild(optItem);
    });

    const expBox = document.createElement('div');
    expBox.className = `mcq-explanation-box ${savedAns !== undefined ? 'visible' : ''}`;
    expBox.innerHTML = `
      <div class="exp-title">Explanation:</div>
      <div>${mcq.explanation || ''}</div>
    `;

    card.appendChild(metaRow);
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

// 9. MCQ BANK RENDERING (INTERACTIVE OPTIONS, ANSWERS HIDDEN UNTIL CLICKED)
function renderMCQBank() {
  const container = document.getElementById('mcq-bank-container');
  container.innerHTML = '';

  let pool = [];

  if (activeMCQFilter === 'starred') {
    // Collect all starred questions across curriculum, CA, and CSAT
    allCurriculum.forEach(d => {
      (d.day_mcqs || []).forEach(m => {
        if (userState.starred_mcqs[m.id]) pool.push(m);
      });
      (d.csat_topic_pyqs || []).forEach(m => {
        if (userState.starred_mcqs[m.id]) pool.push(m);
      });
    });
    allCA.forEach(a => {
      (a.mcqs || []).forEach(m => {
        if (userState.starred_mcqs[m.id]) pool.push(m);
      });
    });
  } else if (activeMCQFilter === 'CSAT') {
    allCurriculum.forEach(d => {
      (d.csat_topic_pyqs || []).forEach(m => pool.push(m));
    });
  } else {
    allCurriculum.forEach(d => {
      if (d.subjects && d.subjects[0] === activeMCQFilter) {
        (d.day_mcqs || []).forEach(m => pool.push(m));
      }
    });
  }

  document.getElementById('mcq-bank-count-pill').textContent = `${pool.length} Questions Available`;

  if (pool.length === 0) {
    container.innerHTML = `
      <div style="padding:48px 24px; text-align:center; color:var(--text-muted); background:var(--surface); border-radius:var(--radius); border:1px solid var(--border); box-shadow:var(--shadow-sm);">
        <p style="font-size:16px; font-weight:700; color:var(--text-main);">No questions found in this category.</p>
        <p style="font-size:13px; margin-top:4px;">Star any question while practicing to add it directly into your Starred Recall Deck.</p>
      </div>
    `;
    return;
  }

  pool.forEach((mcq, idx) => {
    const card = document.createElement('div');
    card.className = 'single-mcq-card';

    const isStarred = !!userState.starred_mcqs[mcq.id];
    const savedAns = userState.mcq_answers[mcq.id];

    // Meta row
    const metaRow = document.createElement('div');
    metaRow.className = 'mcq-meta-row';
    metaRow.innerHTML = `
      <span>Question ${idx + 1} of ${pool.length} • ${mcq.topic || 'UPSC Pattern'}</span>
      <button class="star-btn ${isStarred ? 'starred' : ''}" onclick="toggleStarMCQ('${mcq.id}', this)" title="Star for Recall">
        <svg viewBox="0 0 24 24"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon></svg>
      </button>
    `;

    // Question
    const qText = document.createElement('div');
    qText.className = 'mcq-question-text';
    qText.textContent = mcq.q;

    // Options list (Interactive buttons!)
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
      };

      optList.appendChild(optItem);
    });

    // Explanation Box (HIDDEN until clicked!)
    const expBox = document.createElement('div');
    expBox.className = `mcq-explanation-box ${savedAns !== undefined ? 'visible' : ''}`;
    expBox.innerHTML = `
      <div class="exp-title">Official Answer: ${mcq.answer}</div>
      <div style="white-space:pre-line;">${mcq.explanation || ''}</div>
    `;

    card.appendChild(metaRow);
    card.appendChild(qText);
    card.appendChild(optList);
    card.appendChild(expBox);
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

// 10. OFFICIAL PYQ BANK (1995-2026 GS & CSAT)
async function loadAndRenderPYQs(append = false) {
  const container = document.getElementById('pyq-deck-container');
  if (!append) {
    container.innerHTML = '<div style="padding:32px; text-align:center; color:var(--text-muted);">Loading official UPSC questions...</div>';
    pyqOffset = 0;
    pyqLoadedList = [];
  }

  let url = `/api/pyqs?limit=${pyqLimit}&offset=${pyqOffset}`;
  if (activePYQSubject !== 'all') url += `&subject=${encodeURIComponent(activePYQSubject)}`;
  if (activePYQEra !== 'all') url += `&era=${encodeURIComponent(activePYQEra)}`;
  if (pyqSearchTerm.trim()) url += `&q=${encodeURIComponent(pyqSearchTerm.trim())}`;

  try {
    const res = await fetch(url);
    if (res.ok) {
      const data = await res.json();
      pyqTotalAvailable = data.total;
      document.getElementById('pyq-total-count-badge').textContent = `${data.total} Questions Found`;

      if (!append) container.innerHTML = '';
      if (data.pyqs.length === 0 && !append) {
        container.innerHTML = `
          <div style="padding:48px 24px; text-align:center; color:var(--text-muted); background:var(--surface); border-radius:var(--radius); border:1px solid var(--border);">
            <p style="font-size:16px; font-weight:700; color:var(--text-main);">No official PYQs found matching search criteria.</p>
          </div>
        `;
        document.getElementById('pyq-load-more-wrap').style.display = 'none';
        return;
      }

      pyqLoadedList.push(...data.pyqs);

      data.pyqs.forEach((mcq, idx) => {
        const globalIdx = pyqOffset + idx + 1;
        const card = document.createElement('div');
        card.className = 'single-mcq-card';
        card.id = `pyq-card-${mcq.id}`;

        const isStarred = !!userState.starred_mcqs[mcq.id];
        const savedAns = userState.mcq_answers[mcq.id];

        // Meta row with official year tag
        const metaRow = document.createElement('div');
        metaRow.className = 'mcq-meta-row';
        metaRow.innerHTML = `
          <div style="display:flex; align-items:center; gap:8px;">
            <span class="year-badge-pill">${mcq.year_tag || `[UPSC CSE ${mcq.year}]`}</span>
            <span class="pillar-badge ${mcq.subject_group || 'Polity'}" style="font-size:10px;">${mcq.subject}</span>
            <span style="font-size:12px; color:var(--text-muted);">${mcq.topic}</span>
          </div>
          <button class="star-btn ${isStarred ? 'starred' : ''}" onclick="toggleStarMCQ('${mcq.id}', this)" title="Star for Recall">
            <svg viewBox="0 0 24 24"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon></svg>
          </button>
        `;

        // Question
        const qText = document.createElement('div');
        qText.className = 'mcq-question-text';
        qText.textContent = `${globalIdx}. ${mcq.q}`;

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
          };

          optList.appendChild(optItem);
        });

        // Explanation Box (HIDDEN until clicked)
        const expBox = document.createElement('div');
        expBox.className = `mcq-explanation-box ${savedAns !== undefined ? 'visible' : ''}`;
        expBox.innerHTML = `
          ${mcq.child_logic ? `<div style="background:var(--primary-light); border:1px solid var(--primary-border); padding:8px 12px; border-radius:var(--radius-sm); margin-bottom:8px; font-size:12.5px; color:var(--primary); font-weight:700;">${mcq.child_logic}</div>` : ''}
          <div class="exp-title">Official Answer: ${mcq.answer}</div>
          <div style="white-space:pre-line;">${mcq.explanation || ''}</div>
        `;

        card.appendChild(metaRow);
        card.appendChild(qText);
        card.appendChild(optList);
        card.appendChild(expBox);
        container.appendChild(card);
      });

      // Show/hide load more
      const loadMoreWrap = document.getElementById('pyq-load-more-wrap');
      if (pyqLoadedList.length < pyqTotalAvailable) {
        loadMoreWrap.style.display = 'block';
      } else {
        loadMoreWrap.style.display = 'none';
      }
    }
  } catch (e) {
    console.error('Error loading PYQs:', e);
  }
}

function loadMorePYQs() {
  pyqOffset += pyqLimit;
  loadAndRenderPYQs(true);
}

function filterPYQSubject(subj, btn) {
  activePYQSubject = subj;
  const btns = document.querySelectorAll('#pyq-subject-filters .filter-pill-btn');
  btns.forEach(b => b.classList.remove('active'));
  btn.classList.add('active');
  loadAndRenderPYQs(false);
}

function filterPYQEra(era, btn) {
  activePYQEra = era;
  const btns = document.querySelectorAll('#pyq-era-filters .filter-pill-btn');
  btns.forEach(b => b.classList.remove('active'));
  btn.classList.add('active');
  loadAndRenderPYQs(false);
}

function onPYQSearchChange(val) {
  pyqSearchTerm = val;
  loadAndRenderPYQs(false);
}

// 11. CSAT LAB RENDERING (DAY-SPECIFIC + CONCEPT COMPENDIUM)
function switchCSATViewMode(mode, btn) {
  csatViewMode = mode;
  const btns = document.querySelectorAll('#csat-view-mode-toggle .filter-pill-btn');
  btns.forEach(b => b.classList.remove('active'));
  btn.classList.add('active');

  const dailyView = document.getElementById('csat-daily-view');
  const conceptsView = document.getElementById('csat-concepts-view');

  if (mode === 'daily') {
    dailyView.style.display = 'block';
    conceptsView.style.display = 'none';
    renderCSATDaily();
  } else {
    dailyView.style.display = 'none';
    conceptsView.style.display = 'block';
    renderCSATModules();
  }
}

function filterCSATPhase(phase, btn) {
  activeCSATPhase = phase;
  const btns = document.querySelectorAll('#csat-phase-filters .filter-pill-btn');
  btns.forEach(b => b.classList.remove('active'));
  btn.classList.add('active');
  renderCSATDaily();
}

function onCSATSearchChange(val) {
  csatSearchTerm = val;
  renderCSATDaily();
}

function renderCSATDaily() {
  const container = document.getElementById('csat-daily-grid');
  if (!container) return;
  container.innerHTML = '';

  let filtered = allCurriculum;
  if (activeCSATPhase !== 'all') {
    filtered = filtered.filter(d => d.phase === parseInt(activeCSATPhase, 10));
  }
  if (csatSearchTerm.trim()) {
    const q = csatSearchTerm.toLowerCase();
    filtered = filtered.filter(d => {
      const csat = d.csat_micro_topic || {};
      const title = (csat.title || '').toLowerCase();
      const source = (csat.ungist_ref || '').toLowerCase();
      const keys = (csat.keywords || '').toLowerCase();
      return title.includes(q) || source.includes(q) || keys.includes(q);
    });
  }

  document.getElementById('csat-schedule-count').textContent = `${filtered.length} Daily Micro-Topics`;

  if (filtered.length === 0) {
    container.innerHTML = `
      <div style="padding:40px; text-align:center; color:var(--text-muted); background:var(--surface); border-radius:var(--radius); border:1px solid var(--border);">
        <p style="font-size:15px; font-weight:700; color:var(--text-main);">No CSAT micro-topics found matching "${csatSearchTerm}".</p>
      </div>
    `;
    return;
  }

  filtered.forEach(day => {
    const csat = day.csat_micro_topic || {};
    const card = document.createElement('div');
    card.className = 'csat-day-card';

    const subList = csat.sub_items || [];
    const completedInDay = subList.filter(s => !!userState.sub_checks[s.id]).length;

    const subChecklistHtml = subList.map(s => {
      const isChecked = !!userState.sub_checks[s.id];
      return `
        <div class="sub-item-row ${isChecked ? 'completed' : ''}" id="csat-lab-row-${s.id}">
          <input type="checkbox" class="custom-checkbox" ${isChecked ? 'checked' : ''} onchange="toggleSubCheck('${s.id}', this.checked)">
          <label class="sub-item-label" onclick="this.previousElementSibling.click()">${s.text}</label>
        </div>
      `;
    }).join('');

    card.innerHTML = `
      <div class="csat-day-top-meta">
        <div style="display:flex; align-items:center; gap:8px;">
          <span class="csat-day-pill">Day ${day.day} • Week ${day.week}</span>
          <span style="font-size:12px; color:var(--text-muted);">${day.date}</span>
        </div>
        <span class="prob-badge" style="background:var(--primary-light); color:var(--primary); border-color:var(--primary-border);">
          ${csat.prob || 95}% CSAT Weightage
        </span>
      </div>

      <div class="csat-day-title">${csat.title || 'CSAT Daily Study'}</div>
      <div class="csat-day-source">Source Reference: ${csat.ungist_ref || 'UNGIST CSAT Book'}</div>

      <div style="font-size:11px; font-weight:700; text-transform:uppercase; color:var(--text-muted); letter-spacing:0.05em; margin-bottom:8px; display:flex; justify-content:space-between;">
        <span>Micro-Checkpoints</span>
        <span id="csat-lab-done-${day.day}" style="color:var(--primary);">${completedInDay} / ${subList.length} Done</span>
      </div>

      <div class="sub-items-container" style="margin-bottom:14px;">
        ${subChecklistHtml}
      </div>

      <div style="display:flex; align-items:center; justify-content:space-between; border-top:1px solid var(--border); padding-top:12px;">
        <span style="font-size:12px; color:var(--text-muted);">Concurrent GS: ${day.topic_title.substring(0, 38)}...</span>
        <button class="target-action-btn" onclick="jumpToDay(${day.day}); switchTab('today');" style="margin-top:0;">
          Jump to Day ${day.day} Focus
        </button>
      </div>
    `;
    container.appendChild(card);
  });
}

function renderCSATModules() {
  const container = document.getElementById('csat-modules-container');
  if (!container) return;
  container.innerHTML = '';

  csatModules.forEach(mod => {
    const card = document.createElement('div');
    card.className = 'csat-day-card';

    const shortcuts = (mod.mental_shortcuts || []).map(s => `<li>${s}</li>`).join('');
    const pyq = mod.pyq_walkthrough || {};

    card.innerHTML = `
      <div class="csat-day-top-meta">
        <span class="csat-day-pill">${mod.difficulty || 'Core CSAT Topic'}</span>
        <span style="font-size:12px; color:var(--text-muted);">${mod.ungist_ref}</span>
      </div>
      <div class="csat-day-title" style="font-size:17px; margin-bottom:12px;">${mod.title}</div>
      
      <!-- Child Logic Breakdown -->
      <div style="background:var(--surface-alt); border:1px solid var(--border); padding:14px; border-radius:var(--radius); margin-bottom:14px;">
        <div style="font-size:11px; font-weight:700; text-transform:uppercase; color:var(--primary); letter-spacing:0.05em; margin-bottom:4px;">
          Explain Like I'm 10 • Intuitive Mental Model
        </div>
        <div style="font-size:13.5px; color:var(--text-body); line-height:1.5;">${mod.child_concept}</div>
      </div>

      <!-- Shortcuts / Rules -->
      <div style="background:#ffffff; border:1px solid var(--border); padding:14px; border-radius:var(--radius); margin-bottom:14px;">
        <div style="font-size:11px; font-weight:700; text-transform:uppercase; color:var(--amber-text); letter-spacing:0.05em; margin-bottom:6px;">
          Mental Shortcuts & Speed Formulas
        </div>
        <ul style="margin-left:18px; font-size:12.5px; color:var(--text-body); line-height:1.5;">${shortcuts}</ul>
      </div>

      <!-- Solved UPSC PYQ Walkthrough -->
      <div style="background:var(--primary-light); border:1px solid var(--primary-border); padding:14px; border-radius:var(--radius);">
        <div style="font-size:11px; font-weight:800; color:var(--primary); text-transform:uppercase; letter-spacing:0.05em; margin-bottom:6px;">
          Official UPSC PYQ Step-by-Step Walkthrough
        </div>
        <div style="font-size:13px; font-weight:600; color:var(--text-main); margin-bottom:8px;">${pyq.question || ''}</div>
        <div style="font-size:12px; margin-bottom:4px;"><strong>Child Logic:</strong> ${pyq.step1_child_logic || ''}</div>
        <div style="font-size:12px; margin-bottom:4px;"><strong>Working:</strong> ${pyq.step2_working || ''}</div>
        <div style="font-size:12.5px; font-weight:700; color:var(--primary); margin-top:6px;">Answer: ${pyq.step3_answer || ''}</div>
      </div>
    `;
    container.appendChild(card);
  });
}

// 12. TAB SWITCHER
function switchTab(tabId) {
  const tabs = document.querySelectorAll('.nav-tab');
  tabs.forEach(t => t.classList.remove('active'));
  const activeTab = document.getElementById(`tab-${tabId}`);
  if (activeTab) activeTab.classList.add('active');

  const contents = document.querySelectorAll('.tab-content');
  contents.forEach(c => c.classList.remove('active'));
  const targetContent = document.getElementById(`content-${tabId}`);
  if (targetContent) targetContent.classList.add('active');

  if (tabId === 'csat' && csatViewMode === 'daily') {
    renderCSATDaily();
  } else if (tabId === 'pyq') {
    if (pyqLoadedList.length === 0) loadAndRenderPYQs(false);
  } else if (tabId === 'mcqs') {
    renderMCQBank();
  }

  window.scrollTo({ top: 0, behavior: 'smooth' });
}
</script>
</body>
</html>
"""

def main():
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, 'w', encoding='utf-8') as f:
        f.write(HTML_CONTENT)
    print(f"Successfully generated Master UI to {OUTPUT_PATH}! Length: {len(HTML_CONTENT)} characters.")

if __name__ == '__main__':
    main()
