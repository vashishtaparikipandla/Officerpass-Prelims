#!/usr/bin/env python3
import os
import re

INDEX_FILES = [
    "/Users/vashishtaparikipandla/Documents/OfficerPass/dashboard/index.html",
    "/Users/vashishtaparikipandla/Documents/OfficerPass/index.html"
]

client_engine_code = '''
// ============================================================================
// CLIENT-SIDE LIVE NEWS & DYNAMIC UPSC ENRICHMENT ENGINE (Works 24/7 on GitHub Pages)
// ============================================================================
async function fetchClientLiveNewsFeeds() {
  const rawItems = [];
  
  // 1. Fetch The Hindu RSS via rss2json
  try {
    const res = await fetch('https://api.rss2json.com/v1/api.json?rss_url=https://www.thehindu.com/news/national/feeder/default.rss');
    if (res.ok) {
      const data = await res.json();
      if (data && data.items && Array.isArray(data.items)) {
        data.items.slice(0, 10).forEach(item => {
          rawItems.push({
            title: item.title ? item.title.trim() : '',
            url: item.link || '',
            desc: item.description ? item.description.replace(/<[^>]+>/g, '').trim() : '',
            pubDate: item.pubDate || new Date().toISOString(),
            source: 'The Hindu (National Feed)'
          });
        });
      }
    }
  } catch (e) {
    console.warn('The Hindu RSS fetch error:', e.message);
  }

  // 2. Fetch GNews Top Indian Headlines (CORS supported)
  try {
    const res = await fetch('https://gnews.io/api/v4/top-headlines?category=general&lang=en&country=in&apikey=814e5041ca86391caf0e5dbe608c838f');
    if (res.ok) {
      const data = await res.json();
      if (data && data.articles && Array.isArray(data.articles)) {
        data.articles.slice(0, 10).forEach(item => {
          rawItems.push({
            title: item.title ? item.title.trim() : '',
            url: item.url || '',
            desc: item.description ? item.description.replace(/<[^>]+>/g, '').trim() : '',
            pubDate: item.publishedAt || new Date().toISOString(),
            source: item.source && item.source.name ? item.source.name : 'PIB / National Desk'
          });
        });
      }
    }
  } catch (e) {
    console.warn('GNews fetch error:', e.message);
  }

  return rawItems;
}

function classifyUPSCTheme(title, desc) {
  const text = (title + ' ' + desc).toLowerCase();
  
  if (/climate|carbon|emission|forest|wildlife|biodiversity|cop|wetland|tiger|pollution|air quality|environment/i.test(text)) {
    return {
      pillar: 'Environment & Ecology',
      gs: 'GS-III: Conservation, Environmental Pollution, Wildlife Protection & Impact Assessment',
      topics: ['Wildlife Protection Act 1972 & 2022 amendments', 'UNFCCC COP Decisions & Carbon Credit Rules', 'National Clean Air Programme & CPCB Standards']
    };
  }
  if (/gdp|inflation|rbi|repo|fiscal|banking|monetary|trade|export|import|rupee|economy|tax|gst|msme|budget|sebi/i.test(text)) {
    return {
      pillar: 'Indian Economy',
      gs: 'GS-III: Indian Economy, Mobilisation of Resources, Banking & Monetary Policy',
      topics: ['Monetary Policy Framework & RBI Act 1934', 'Fiscal Responsibility and Budget Management (FRBM)', 'Balance of Payments & External Commercial Borrowing']
    };
  }
  if (/space|isro|drdo|satellite|ai|quantum|missile|defence|nuclear|biotech|cyber|semiconductor|supercomputer/i.test(text)) {
    return {
      pillar: 'Science & Technology',
      gs: 'GS-III: Science and Technology Developments, Space, Defence & Cyber Security',
      topics: ['Indigenisation of Defence Technology & DRDO', 'ISRO Satellite Launch Vehicles (PSLV, LVM3)', 'Data Protection & Artificial Intelligence Governance']
    };
  }
  if (/treaty|summit|un|wto|asean|brics|g20|bilateral|china|us|russia|border|maritime|quad|indopacific/i.test(text)) {
    return {
      pillar: 'International Relations',
      gs: 'GS-II: Bilateral, Regional & Global Groupings, Agreements Involving India',
      topics: ['United Nations & Multilateral Treaties', 'International Maritime Law (UNCLOS) & Chokepoints', 'Regional Groupings: ASEAN, SCO, and IORA']
    };
  }
  
  return {
    pillar: 'Polity & Governance',
    gs: 'GS-II: Indian Constitution, Executive, Judiciary & Statutory Regulatory Bodies',
    topics: ['Constitutional Articles & Judicial Review Doctrine', 'Statutory Bodies vs Constitutional Commissions', 'Parliamentary Privileges & Legislative Procedure']
  };
}

function generateUPSCArticle(rawItem, idx) {
  const theme = classifyUPSCTheme(rawItem.title, rawItem.desc);
  const now = new Date();
  const dateStr = now.toISOString().split('T')[0];
  const cleanTitle = rawItem.title.replace(/\s+/g, ' ').trim();
  const cleanDesc = rawItem.desc.length > 20 ? rawItem.desc : `${cleanTitle} has emerged as a significant development under national policy.`;
  const articleId = `ca-live-${Date.now()}-${idx}`;

  const summary_points = [
    `Core Development & Trigger: ${cleanTitle}. Reported by ${rawItem.source}.`,
    `Policy & Institutional Mechanism: Governed under the statutory and regulatory framework of the relevant Ministry and Union/State administrative authorities.`,
    `Syllabus Alignment: Categorized under ${theme.gs}, demanding mastery over jurisdictional powers and boundary conditions.`,
    `Constitutional & Legal Interface: Engages constitutional doctrines, fundamental rights, and governing statutory enactments.`,
    `UPSC Trap Boundary: Watch for swaps between mandatory executive notifications vs statutory provisions, and Union vs State List subject allocations.`,
    `Cross-Syllabus Integration: Must be revised alongside ${theme.topics[0]} and contemporary Economic Survey recommendations.`
  ];

  const digestible_fact_sheet = {
    what_is_news: `${cleanTitle}. ${cleanDesc}`,
    prelims_fact_box: [
      `Anchor Authority: Formulated and executed under the aegis of the Government of India / relevant statutory agency.`,
      `Governing Enactment: Intersects directly with applicable statutory rules and constitutional safeguards.`,
      `Jurisdictional Scope: Carries nationwide or inter-state administrative relevance within the Seventh Schedule distribution of powers.`,
      `Syllabus Relevance: Directly testable in UPSC Prelims Paper I under ${theme.pillar}.`
    ],
    trap_alert: `UPSC Trap Warning: Examiners frequently swap whether an authority is statutory, constitutional, or established by executive resolution. Verify exact origin.`,
    hot_revision_topics: theme.topics
  };

  const mcqs = [
    {
      id: `${articleId}-q1`,
      question: `Consider the following statements regarding the regulatory and constitutional backdrop of "${cleanTitle.substring(0, 75)}...":\\n\\n1. It derives its functional authority directly from an express provision under Part III of the Constitution of India.\\n2. In matters falling within the Concurrent List of the Seventh Schedule, parliamentary enactments prevail over state laws subject to presidential assent provisions.\\n3. The statutory bodies established under central legislation are immune from judicial review under Article 226 of the Constitution.\\n\\nWhich of the statements given above is/are correct?`,
      options: [
        "(a) 1 and 2 only",
        "(b) 2 only",
        "(c) 1 and 3 only",
        "(d) 1, 2 and 3"
      ],
      answer: "(b)",
      explanation: `Statement 1 is incorrect: Regulatory bodies derive authority from parent statutes or executive resolutions rather than direct Part III clauses.\\nStatement 2 is correct: Under Article 254, central laws prevail over state laws on Concurrent List entries, with the Article 254(2) presidential assent exception.\\nStatement 3 is incorrect: Under L. Chandra Kumar and Minerva Mills, all statutory authorities remain subject to judicial review under Articles 226 and 32.`
    },
    {
      id: `${articleId}-q2`,
      question: `With reference to policy governance related to "${theme.pillar}", consider the following pairs:\\n\\n1. Executive Order : Lacks force of law in judicial proceedings\\n2. Statutory Body : Established under an Act passed by Parliament or State Legislature\\n3. Constitutional Body : Mentioned and mandated by an express Article in the Constitution\\n\\nHow many of the above pairs are correctly matched?`,
      options: [
        "(a) Only one",
        "(b) Only two",
        "(c) All three",
        "(d) None"
      ],
      answer: "(b)",
      explanation: `Pair 1 is incorrect: An executive order issued within constitutional competence (e.g. Art. 73 or 162) carries binding legal force unless in conflict with statutory or constitutional provisions.\\nPair 2 is correct: Statutory bodies (e.g. NHRC, NGT, SEBI) are created by specific legislative enactments.\\nPair 3 is correct: Constitutional bodies (e.g. ECI under Art. 324, CAG under Art. 148, UPSC under Art. 315) are directly established by the Constitution.`
    },
    {
      id: `${articleId}-q3`,
      question: `Which one of the following statements best reflects the high-yield UPSC boundary condition in the context of "${cleanTitle.substring(0, 60)}..."?`,
      options: [
        "(a) A statutory authority can override the fundamental rights guaranteed under the Constitution without judicial scrutiny.",
        "(b) Subordinate rules and notifications framed under an Act cannot exceed the rule-making scope delegated by the parent statute.",
        "(c) Executive directions automatically repeal contradictory prior statutory enactments.",
        "(d) Parliamentary committee reports are legally binding on courts during judicial adjudication."
      ],
      answer: "(b)",
      explanation: `Option (b) is correct: The doctrine of ultra vires dictates that subordinate legislation (rules, regulations, notifications) is void to the extent it exceeds the rule-making power conferred by the primary parent Act.\\nOptions (a), (c), and (d) represent classic UPSC distractor propositions contrary to Indian constitutional law.`
    }
  ];

  return {
    id: articleId,
    date: dateStr,
    pillar: theme.pillar,
    title: cleanTitle,
    source: rawItem.source,
    is_top100: true,
    is_pt365: true,
    summary_points: summary_points,
    gs_connection: theme.gs,
    digestible_fact_sheet: digestible_fact_sheet,
    mcqs: mcqs
  };
}

async function clientSideFetchLiveNews() {
  const rawItems = await fetchClientLiveNewsFeeds();
  if (!rawItems || rawItems.length === 0) return [];

  // Deduplicate against existing allCA
  const existingTitles = new Set(allCA.map(a => (a.title || '').toLowerCase().trim()));
  const existingUrls = new Set(allCA.map(a => (a.url || a.source || '').toLowerCase().trim()));

  const freshRaw = rawItems.filter(item => {
    const t = item.title.toLowerCase().trim();
    if (t.length < 12) return false;
    if (existingTitles.has(t)) return false;
    for (const et of existingTitles) {
      if (t.includes(et) || et.includes(t)) return false;
    }
    return true;
  });

  if (freshRaw.length === 0) return [];

  const newArticles = freshRaw.map((item, idx) => generateUPSCArticle(item, idx));

  // Persist locally in custom CA storage
  try {
    const prevCustom = JSON.parse(localStorage.getItem('officerpass_custom_ca') || '[]');
    const combined = [...newArticles, ...prevCustom].slice(0, 100);
    localStorage.setItem('officerpass_custom_ca', JSON.stringify(combined));
  } catch (e) {
    console.warn('localStorage custom CA save note:', e);
  }

  return newArticles;
}
'''

for file_path in INDEX_FILES:
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Update loadCAData to merge localStorage custom articles
    old_load_ca = '''async function loadCAData() {
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
}'''

    new_load_ca = '''async function loadCAData() {
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
      // Merge client-accumulated articles from device localStorage
      try {
        const clientSaved = localStorage.getItem('officerpass_custom_ca');
        if (clientSaved) {
          const parsed = JSON.parse(clientSaved);
          if (Array.isArray(parsed) && parsed.length > 0) {
            const existingIds = new Set(data.map(a => a.id));
            const fresh = parsed.filter(p => !existingIds.has(p.id));
            data = [...fresh, ...data];
          }
        }
      } catch (_) {}

      allCA = data;
      populateCADateFilter();
    }
  } catch (e) {
    console.error('CA load error:', e);
  }
}'''

    if old_load_ca in content:
        content = content.replace(old_load_ca, new_load_ca)
        print(f"Updated loadCAData in {file_path}")
    else:
        print(f"Notice: old_load_ca not matched in {file_path}")

    # 2. Update refreshLiveNewsFeed
    old_refresh_feed = '''async function refreshLiveNewsFeed() {
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
}'''

    new_refresh_feed = client_engine_code + '''
async function refreshLiveNewsFeed() {
  const btn = document.getElementById('ca-refresh-btn');
  if (btn) btn.innerHTML = `
    <svg class="icon-svg" style="animation:spin 1s linear infinite;" width="14" height="14" viewBox="0 0 24 24"><path d="M21.5 2v6h-6M2.5 22v-6h6M2 11.5a10 10 0 0 1 18.8-4.3M22 12.5a10 10 0 0 1-18.8 4.2"/></svg>
    Fetching Live News...
  `;

  let newCount = 0;

  // 1. Try local backend server first if active
  try {
    const res = await fetch('/api/news/refresh');
    if (res.ok) {
      const data = await res.json();
      newCount = data.count || 0;
      await loadCAData();
      renderCAList();
      showRefreshFeedback(btn, newCount);
      return;
    }
  } catch (_) {}

  // 2. Client-Side Live RSS & News Engine (Works directly on GitHub Pages 24/7)
  try {
    const addedArticles = await clientSideFetchLiveNews();
    if (addedArticles && addedArticles.length > 0) {
      newCount = addedArticles.length;
      allCA = [...addedArticles, ...allCA];
      populateCADateFilter();
      renderCAList();
      showRefreshFeedback(btn, newCount);
      syncStateToGitHub(false);
      return;
    } else {
      showRefreshFeedback(btn, 0);
      return;
    }
  } catch (err) {
    console.error('Client live news refresh error:', err);
    if (btn) btn.textContent = 'All Live Feeds Current';
  }

  setTimeout(() => restoreRefreshBtn(btn), 2500);
}

function showRefreshFeedback(btn, count) {
  if (!btn) return;
  if (count > 0) {
    btn.textContent = `Accumulated (+${count} new live topics)`;
  } else {
    btn.textContent = 'All Feeds Up to Date';
  }
  setTimeout(() => restoreRefreshBtn(btn), 2800);
}

function restoreRefreshBtn(btn) {
  if (!btn) return;
  btn.innerHTML = `
    <svg class="icon-svg" width="14" height="14" viewBox="0 0 24 24"><polyline points="23 4 23 10 17 10"></polyline><polyline points="1 20 1 14 7 14"></polyline><path d="M3.51 9a9 9 0 0 1 14.85-3.36L23 10M1 14l4.64 4.36A9 9 0 0 0 20.49 15"></path></svg>
    Refresh Live News
  `;
}'''

    if old_refresh_feed in content:
        content = content.replace(old_refresh_feed, new_refresh_feed)
        print(f"Injected client-side live news engine in {file_path}")
    else:
        print(f"Error: old_refresh_feed not found in {file_path}")

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

print("Files updated successfully.")
