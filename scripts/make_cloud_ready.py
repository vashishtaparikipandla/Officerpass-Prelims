#!/usr/bin/env python3
import os
import re

DASHBOARD_FILE = "/Users/vashishtaparikipandla/Documents/OfficerPass/dashboard/index.html"
ROOT_INDEX = "/Users/vashishtaparikipandla/Documents/OfficerPass/index.html"

with open(DASHBOARD_FILE, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Update Header to add the Cloud Sync Badge
old_header_date = '''    <div class="candidate-badge">
      <span class="candidate-dot"></span>
      <span id="header-today-date">24 Nov 2026 • 180-Day Blueprint</span>
    </div>'''

new_header_date = '''    <div style="display:flex; align-items:center; gap:8px; flex-wrap:wrap;">
      <div class="candidate-badge" id="git-sync-status-badge" onclick="syncStateToGitHub(true)" title="Click to manually sync progress & notes to GitHub repository" style="cursor:pointer; display:flex; align-items:center; gap:6px;">
        <span class="candidate-dot" id="git-sync-dot" style="background:#10b981;"></span>
        <span id="git-sync-status-text">Cloud Sync: Active</span>
        <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M21.5 2v6h-6M2.5 22v-6h6M2 11.5a10 10 0 0 1 18.8-4.3M22 12.5a10 10 0 0 1-18.8 4.2"/></svg>
      </div>
      <div class="candidate-badge">
        <span class="candidate-dot"></span>
        <span id="header-today-date">24 Nov 2026 • 180-Day Blueprint</span>
      </div>
    </div>'''

if old_header_date in content:
    content = content.replace(old_header_date, new_header_date)
    print("Added Cloud Sync badge in header.")
else:
    print("Notice: Header badge already modified or not found as exact string.")

# 2. Add Universal Cloud Adapters
adapters_code = '''
// ============================================================================
// UNIVERSAL CLOUD & GITHUB ADAPTER SYSTEM (24/7 Zero-Server Resilience)
// ============================================================================
const DATA_PREFIX = (function() {
  const p = window.location.pathname;
  if (p.includes('/dashboard/')) return '../data/';
  return 'data/';
})();

const GITHUB_REPO_OWNER = 'vashishtaparikipandla';
const GITHUB_REPO_NAME = 'Officerpass-Prelims';
let GITHUB_PAT = localStorage.getItem('officerpass_gh_pat') || '';
let stateFileSha = null;
let isSyncingToGit = false;

function updateSyncStatusUI(text, isError = false) {
  const badgeText = document.getElementById('git-sync-status-text');
  const badgeDot = document.getElementById('git-sync-dot');
  if (badgeText) badgeText.textContent = text;
  if (badgeDot) badgeDot.style.background = isError ? '#ef4444' : '#10b981';
}

let staticPYQMasterCache = null;
async function fetchPYQsAdapter(subject, era, q, limit, offset) {
  if (!staticPYQMasterCache) {
    const res = await fetch(DATA_PREFIX + 'pyq-master-db.json');
    if (!res.ok) throw new Error('Failed to load pyq-master-db.json');
    staticPYQMasterCache = await res.json();
  }
  let list = staticPYQMasterCache;
  if (subject && subject !== 'all') {
    list = list.filter(item => (item.subject || '').toLowerCase() === subject.toLowerCase());
  }
  if (era && era !== 'all') {
    if (era.includes('-')) {
      const parts = era.split('-').map(Number);
      list = list.filter(item => {
        const y = Number(item.year);
        return y >= parts[0] && y <= parts[1];
      });
    } else {
      const yNum = Number(era);
      list = list.filter(item => Number(item.year) === yNum);
    }
  }
  if (q && q.trim()) {
    const term = q.trim().toLowerCase();
    list = list.filter(item => {
      const qText = (item.question || item.prompt || '').toLowerCase();
      const exp = (item.explanation || '').toLowerCase();
      return qText.includes(term) || exp.includes(term);
    });
  }
  const total = list.length;
  const page = list.slice(offset, offset + limit);
  return { total, pyqs: page };
}

let staticCSATQuestionsCache = null;
async function fetchCSATQuestionsAdapter(dayNum) {
  if (!staticCSATQuestionsCache) {
    const res = await fetch(DATA_PREFIX + 'csat-topic-questions-db.json');
    if (!res.ok) throw new Error('Failed to load csat-topic-questions-db.json');
    staticCSATQuestionsCache = await res.json();
  }
  let topicId = null;
  if (allCurriculum && allCurriculum.length > 0) {
    const d = allCurriculum.find(item => String(item.day) === String(dayNum));
    if (d && d.csat_topic_bank_id) {
      topicId = d.csat_topic_bank_id;
    }
  }
  if (!topicId || !staticCSATQuestionsCache[topicId]) {
    const num = ((parseInt(dayNum, 10) - 1) % 25) + 1;
    topicId = `csat-${num < 10 ? '0' + num : num}`;
  }
  return staticCSATQuestionsCache[topicId] || null;
}

let staticTrapsVaultCache = null;
async function fetchTrapsAdapter(subject) {
  if (!staticTrapsVaultCache) {
    const res = await fetch(DATA_PREFIX + 'upsc-traps-vault.json');
    if (!res.ok) throw new Error('Failed to load upsc-traps-vault.json');
    staticTrapsVaultCache = await res.json();
  }
  const subjData = (staticTrapsVaultCache.subjects && staticTrapsVaultCache.subjects[subject]) || {
    subject: subject,
    title: subject,
    subtitle: '',
    total_items: 0,
    sections: [],
    items: []
  };
  return {
    subject: subject,
    title: subjData.title,
    subtitle: subjData.subtitle,
    total_items: subjData.total_items || (subjData.items || []).length,
    sections: subjData.sections || [],
    items: subjData.items || []
  };
}

async function syncStateToGitHub(manual = false) {
  if (isSyncingToGit || !GITHUB_PAT) return;
  isSyncingToGit = true;
  updateSyncStatusUI(manual ? 'Syncing...' : 'Cloud Saving...');

  try {
    if (!stateFileSha) {
      const getRes = await fetch(`https://api.github.com/repos/${GITHUB_REPO_OWNER}/${GITHUB_REPO_NAME}/contents/data/state.json`, {
        headers: { 'Authorization': `token ${GITHUB_PAT}` }
      });
      if (getRes.ok) {
        const fileInfo = await getRes.json();
        stateFileSha = fileInfo.sha;
      }
    }

    const statePayload = {
      ...userState,
      updatedAt: new Date().toISOString()
    };
    const contentEncoded = btoa(unescape(encodeURIComponent(JSON.stringify(statePayload, null, 2))));

    const putRes = await fetch(`https://api.github.com/repos/${GITHUB_REPO_OWNER}/${GITHUB_REPO_NAME}/contents/data/state.json`, {
      method: 'PUT',
      headers: {
        'Authorization': `token ${GITHUB_PAT}`,
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        message: 'Auto-sync user study progress & notes [OfficerPass Cloud]',
        content: contentEncoded,
        sha: stateFileSha || undefined
      })
    });

    if (putRes.ok) {
      const resJson = await putRes.json();
      stateFileSha = resJson.content?.sha || null;
      updateSyncStatusUI(`Cloud Synced (${new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })})`);
      if (manual) alert('All notes, task progress, and calendar memory entries successfully committed to GitHub!');
    } else {
      stateFileSha = null;
      updateSyncStatusUI('Saved Locally');
    }
  } catch (err) {
    console.warn('GitHub cloud sync note:', err.message);
    updateSyncStatusUI('Saved Locally');
  } finally {
    isSyncingToGit = false;
  }
}
'''

# 3. Replace state loaders and savers
old_state_fns = '''async function loadState() {
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
        mcq_answers: data.mcq_answers || {},
        ca_memory_calendar: data.ca_memory_calendar || {}
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
}'''

new_state_fns = '''function applyStateData(data) {
  if (!data) return;
  userState = {
    checks: data.checks || {},
    sub_checks: data.sub_checks || {},
    notes: data.notes || {},
    read_articles: data.read_articles || {},
    starred_mcqs: data.starred_mcqs || {},
    mcq_answers: data.mcq_answers || {},
    ca_memory_calendar: data.ca_memory_calendar || {}
  };
}

async function loadState() {
  // 1. Immediately load local device storage
  try {
    const local = localStorage.getItem('officerpass_state');
    if (local) {
      applyStateData(JSON.parse(local));
      updateSyncStatusUI('Loaded (Local)');
    }
  } catch (e) {}

  // 2. Resiliently fetch remote state
  try {
    let remoteData = null;
    try {
      const res = await fetch('/api/state');
      if (res.ok) remoteData = await res.json();
    } catch (_) {}

    if (!remoteData) {
      const staticRes = await fetch(DATA_PREFIX + 'state.json');
      if (staticRes.ok) remoteData = await staticRes.json();
    }

    if (remoteData) {
      if (!localStorage.getItem('officerpass_state')) {
        applyStateData(remoteData);
        try { localStorage.setItem('officerpass_state', JSON.stringify(userState)); } catch (_) {}
      }
    }
  } catch (e) {
    console.warn('State load error:', e);
  }
}

let saveStateDebounceTimer = null;
async function saveState() {
  // 1. Instant local persistence
  try {
    localStorage.setItem('officerpass_state', JSON.stringify(userState));
  } catch (e) {}

  // 2. Save to local server if alive
  try {
    fetch('/api/state', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(userState)
    }).catch(() => {});
  } catch (_) {}

  // 3. Debounced GitHub Cloud Commit
  clearTimeout(saveStateDebounceTimer);
  saveStateDebounceTimer = setTimeout(() => {
    syncStateToGitHub(false);
  }, 2500);
}

// 2. DATA LOADERS
async function loadCurriculum() {
  try {
    let data = null;
    try {
      const res = await fetch('/api/curriculum');
      if (res.ok) data = await res.json();
    } catch (_) {}
    if (!data) {
      const staticRes = await fetch(DATA_PREFIX + 'curriculum-180.json');
      if (staticRes.ok) data = await staticRes.json();
    }
    if (data) allCurriculum = data;
  } catch (e) {
    console.error('Curriculum load error:', e);
  }
}

async function loadCAData() {
  try {
    let data = null;
    try {
      const res = await fetch('/api/ca?include_mcqs=true');
      if (res.ok) data = await res.json();
    } catch (_) {}
    if (!data) {
      const staticRes = await fetch(DATA_PREFIX + 'current-affairs-db.json');
      if (staticRes.ok) data = await staticRes.json();
    }
    if (data) {
      allCA = data;
      populateCADateFilter();
    }
  } catch (e) {
    console.error('CA load error:', e);
  }
}

async function loadCSATData() {
  try {
    let data = null;
    try {
      const res = await fetch('/api/csat');
      if (res.ok) data = await res.json();
    } catch (_) {}
    if (!data) {
      if (allCurriculum && allCurriculum.length > 0) {
        data = allCurriculum;
      } else {
        const staticRes = await fetch(DATA_PREFIX + 'curriculum-180.json');
        if (staticRes.ok) data = await staticRes.json();
      }
    }
    if (data) csatModules = data;
  } catch (e) {
    console.error('CSAT load error:', e);
  }
}'''

if old_state_fns in content:
    content = content.replace(old_state_fns, adapters_code + "\n" + new_state_fns)
    print("Replaced state & curriculum loaders with universal resilient adapters.")
else:
    print("Error: Could not locate old_state_fns in content.")

# 4. Replace CSAT drawer fetch
old_csat_drawer_fetch = '''  if (!csatArenaCache[dayNum]) {
    try {
      const res = await fetch(`/api/csat/questions?day=${dayNum}`);
      if (res.ok) {
        csatArenaCache[dayNum] = await res.json();
      }
    } catch (e) {
      console.error('Failed to load CSAT questions:', e);
    }
  }'''

new_csat_drawer_fetch = '''  if (!csatArenaCache[dayNum]) {
    try {
      let loaded = null;
      try {
        const res = await fetch(`/api/csat/questions?day=${dayNum}`);
        if (res.ok) loaded = await res.json();
      } catch (_) {}
      if (!loaded) {
        loaded = await fetchCSATQuestionsAdapter(dayNum);
      }
      if (loaded) {
        csatArenaCache[dayNum] = loaded;
      }
    } catch (e) {
      console.error('Failed to load CSAT questions:', e);
    }
  }'''

if old_csat_drawer_fetch in content:
    content = content.replace(old_csat_drawer_fetch, new_csat_drawer_fetch)
    print("Replaced CSAT drawer fetch with adapter.")
else:
    print("Notice: old_csat_drawer_fetch not found.")

# 5. Replace loadAndRenderPYQs
old_pyq_fetch = '''  try {
    const res = await fetch(url);
    if (res.ok) {
      const data = await res.json();'''

new_pyq_fetch = '''  try {
    let data = null;
    try {
      const res = await fetch(url);
      if (res.ok) data = await res.json();
    } catch (_) {}
    if (!data) {
      data = await fetchPYQsAdapter(activePYQSubject, activePYQEra, pyqSearchTerm, pyqLimit, pyqOffset);
    }
    if (data) {'''

if old_pyq_fetch in content:
    content = content.replace(old_pyq_fetch, new_pyq_fetch, 1)
    print("Replaced PYQ fetch with adapter.")
else:
    print("Notice: old_pyq_fetch not found.")

# 6. Replace loadTrapsData
old_traps_fetch = '''async function loadTrapsData() {
  try {
    const res = await fetch(`/api/traps?subject=${encodeURIComponent(activeTrapsSubject)}`);
    if (res.ok) {
      trapsVaultData = await res.json();
      updateTrapsUIStats();
      populateTrapsSectionFilter();
      renderTrapsVault();
    }
  } catch (err) {
    console.error('Error loading traps vault:', err);
  }
}'''

new_traps_fetch = '''async function loadTrapsData() {
  try {
    let data = null;
    try {
      const res = await fetch(`/api/traps?subject=${encodeURIComponent(activeTrapsSubject)}`);
      if (res.ok) data = await res.json();
    } catch (_) {}
    if (!data) {
      data = await fetchTrapsAdapter(activeTrapsSubject);
    }
    if (data) {
      trapsVaultData = data;
      updateTrapsUIStats();
      populateTrapsSectionFilter();
      renderTrapsVault();
    }
  } catch (err) {
    console.error('Error loading traps vault:', err);
  }
}'''

if old_traps_fetch in content:
    content = content.replace(old_traps_fetch, new_traps_fetch)
    print("Replaced Traps Vault fetch with adapter.")
else:
    print("Notice: old_traps_fetch not found.")

# Write updated content to dashboard/index.html and root index.html
with open(DASHBOARD_FILE, "w", encoding="utf-8") as f:
    f.write(content)

with open(ROOT_INDEX, "w", encoding="utf-8") as f:
    f.write(content)

print("Successfully written updated universal code to dashboard/index.html and root index.html!")
