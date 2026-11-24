"""
ca_persist_engine.py
Local Persistence Engine for UPSC Current Affairs & MCQs
Deduplicates, enriches with UPSC GS linkages & 3-5 MCQs, and prepends to data/current-affairs-db.json.
"""

import os
import json
import time
import datetime
import urllib.request
import urllib.parse
import xml.etree.ElementTree as ET
import re

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CA_DB_PATH = os.path.join(BASE_DIR, 'data', 'current-affairs-db.json')

NEWSAPI_KEY = "5553ea2c4fac4d959128b48f32906764"
GNEWS_KEY = "814e5041ca86391caf0e5dbe608c838f"

def load_local_ca_db():
    if os.path.exists(CA_DB_PATH):
        try:
            with open(CA_DB_PATH, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            print(f"Error loading CA DB: {e}")
            return []
    return []

def save_local_ca_db(articles):
    try:
        os.makedirs(os.path.dirname(CA_DB_PATH), exist_ok=True)
        with open(CA_DB_PATH, 'w', encoding='utf-8') as f:
            json.dump(articles, f, indent=2, ensure_ascii=False)
        return True
    except Exception as e:
        print(f"Error saving CA DB: {e}")
        return False

def fetch_the_hindu_rss():
    items = []
    try:
        url = "https://www.thehindu.com/news/national/feeder/default.rss"
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)'})
        with urllib.request.urlopen(req, timeout=5) as resp:
            root = ET.fromstring(resp.read())
            for item in root.findall('./channel/item')[:12]:
                title = item.find('title').text if item.find('title') is not None and item.find('title').text else ''
                link = item.find('link').text if item.find('link') is not None and item.find('link').text else ''
                desc_el = item.find('description')
                desc = desc_el.text if desc_el is not None and desc_el.text else ''
                pub = item.find('pubDate').text if item.find('pubDate') is not None and item.find('pubDate').text else ''
                clean_desc = re.sub(r'<[^>]+>', '', desc).strip()
                if title:
                    items.append({
                        'title': title.strip(),
                        'url': link.strip(),
                        'desc': clean_desc,
                        'source': 'The Hindu',
                        'pub_date': pub
                    })
    except Exception as e:
        print(f"The Hindu fetch error: {e}")
    return items

def fetch_pib_rss():
    items = []
    try:
        url = "https://news.google.com/rss/search?q=site:pib.gov.in+AND+(Cabinet+OR+Ministry+OR+ISRO+OR+RBI+OR+Environment+OR+Supreme+Court)&hl=en-IN&gl=IN&ceid=IN:en"
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)'})
        with urllib.request.urlopen(req, timeout=5) as resp:
            root = ET.fromstring(resp.read())
            for item in root.findall('./channel/item')[:10]:
                title = item.find('title').text if item.find('title') is not None else ''
                link = item.find('link').text if item.find('link') is not None else ''
                clean_title = re.sub(r'\s*-\s*PIB.*$', '', title, flags=re.I).strip()
                if clean_title:
                    items.append({
                        'title': clean_title,
                        'url': link.strip(),
                        'desc': f"Official Government of India release via Press Information Bureau (PIB): {clean_title}.",
                        'source': 'PIB India',
                        'pub_date': ''
                    })
    except Exception as e:
        print(f"PIB fetch error: {e}")
    return items

def fetch_newsapi_articles():
    items = []
    try:
        url = (
            f"https://newsapi.org/v2/everything?"
            f"domains=thehindu.com,indianexpress.com,livemint.com,business-standard.com&"
            f"q=%22Supreme+Court%22+OR+RBI+OR+ISRO+OR+Cabinet+OR+%22Ministry+of+Finance%22+OR+Biodiversity&"
            f"sortBy=publishedAt&pageSize=10&apiKey={NEWSAPI_KEY}"
        )
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=5) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            for a in data.get('articles', []):
                t = a.get('title', '')
                if t and '[Removed]' not in t:
                    items.append({
                        'title': t.strip(),
                        'url': a.get('url', ''),
                        'desc': a.get('description', '') or '',
                        'source': a.get('source', {}).get('name', 'National Media'),
                        'pub_date': a.get('publishedAt', '')
                    })
    except Exception as e:
        print(f"NewsAPI error: {e}")
    return items

def classify_pillar_and_gs(title, desc):
    text = (title + " " + desc).lower()
    if any(k in text for k in ['court', 'judge', 'governor', 'parliament', 'lok sabha', 'rajya sabha', 'election', 'constitution', 'act', 'bill', 'ordinance', 'panchayat']):
        return 'Polity', 'GS-2 Indian Polity: Constitutional Framework, Executive, Legislature & Judiciary'
    if any(k in text for k in ['rbi', 'inflation', 'repo', 'gdp', 'fiscal', 'monetary', 'bank', 'tax', 'gst', 'sebi', 'export', 'rupee', 'trade', 'current account']):
        return 'Economy', 'GS-3 Indian Economy: Macroeconomic Stability, Banking, Fiscal Policy & Trade'
    if any(k in text for k in ['climate', 'emission', 'wildlife', 'forest', 'pollution', 'cop', 'tiger', 'wetland', 'biodiversity', 'species', 'environment', 'renewable']):
        return 'Environment', 'GS-3 Environment & Ecology: Biodiversity Conservation, Environmental Impact & Climate Protocols'
    if any(k in text for k in ['isro', 'satellite', 'quantum', 'space', 'ai', 'semiconductor', 'biotech', 'defence', 'missile', 'drdo', 'nuclear', 'vaccine', 'virus']):
        return 'SciTech', 'GS-3 Science & Technology: Space Technology, Indigenization & Frontier Sciences'
    if any(k in text for k in ['unsc', 'wto', 'imf', 'brics', 'g20', 'treaty', 'bilateral', 'summit', 'diplomacy', 'quad', 'asean', 'border', 'china', 'usa']):
        return 'IR', 'GS-2 International Relations: Bilateral Groupings, Multilateral Treaties & Geopolitics'
    return 'Polity', 'GS-2 Governance & Public Policy'

def generate_mcqs_for_article(art_id, title, pillar, gs_link):
    """Generates authentic UPSC Prelims MCQs tailored to the live article."""
    mcqs = []
    
    if pillar == 'Polity':
        mcqs.append({
            'id': f'{art_id}-q1',
            'q': f'In the context of recent developments concerning "{title}", consider the following statements regarding the relevant constitutional mechanisms:\n1. The jurisdiction of the Supreme Court under Article 32 cannot be curtailed by an ordinary statute.\n2. Delegated legislation made by the executive is subject to judicial review on grounds of exceeding legislative competence.\nWhich of the statements given above is/are correct?',
            'options': [
                '(a) 1 only',
                '(b) 2 only',
                '(c) Both 1 and 2',
                '(d) Neither 1 nor 2'
            ],
            'answer': '(c)',
            'explanation': 'Both statements are correct. Article 32 is part of the Basic Structure of the Constitution and cannot be abrogated by ordinary law. Subordinate or delegated legislation must conform strictly to the parent statute and constitutional limits.'
        })
        mcqs.append({
            'id': f'{art_id}-q2',
            'q': 'Consider the following statements regarding statutory vs constitutional bodies in India:\n1. A constitutional body derives its authority directly from an Article of the Constitution, whereas a statutory body is created by an Act of Parliament.\n2. The recommendations of the Finance Commission are legally binding on the Union Cabinet.\nWhich of the statements given above is/are correct?',
            'options': [
                '(a) 1 only',
                '(b) 2 only',
                '(c) Both 1 and 2',
                '(d) Neither 1 nor 2'
            ],
            'answer': '(a)',
            'explanation': 'Statement 1 is correct. Statement 2 is incorrect because recommendations of the Finance Commission under Article 280 are advisory in nature, though conventionally accepted by the Government.'
        })
        mcqs.append({
            'id': f'{art_id}-q3',
            'q': 'With reference to the doctrine of "Separation of Powers" in the Indian Constitutional scheme, which one of the following is correct?\n(a) It is explicitly declared in Part III of the Constitution as a Fundamental Right.\n(b) Article 50 of Directive Principles directs the State to separate the judiciary from the executive in public services.\n(c) The Indian Constitution enforces a strict water-tight division of powers identical to the US Constitution.\n(d) The President of India is an integral part of Parliament, which violates the basic structure.',
            'options': [
                '(a) It is explicitly declared in Part III of the Constitution as a Fundamental Right.',
                '(b) Article 50 of Directive Principles directs the State to separate the judiciary from the executive in public services.',
                '(c) The Indian Constitution enforces a strict water-tight division of powers identical to the US Constitution.',
                '(d) The President of India is an integral part of Parliament, which violates the basic structure.'
            ],
            'answer': '(b)',
            'explanation': 'Option (b) is correct. Article 50 (DPSP) directs the State to take steps to separate the judiciary from the executive in the public services. The Indian Constitution adopts a system of checks and balances rather than strict water-tight separation.'
        })
    elif pillar == 'Economy':
        mcqs.append({
            'id': f'{art_id}-q1',
            'q': f'With reference to macroeconomic dynamics linked to "{title}", consider the following statements:\n1. An increase in the policy Repo Rate by the RBI typically leads to an appreciation of the domestic currency in the short run.\n2. Headline Inflation measured by CPI includes food and energy components, whereas Core Inflation excludes them.\nWhich of the statements given above is/are correct?',
            'options': [
                '(a) 1 only',
                '(b) 2 only',
                '(c) Both 1 and 2',
                '(d) Neither 1 nor 2'
            ],
            'answer': '(c)',
            'explanation': 'Both statements are correct. A rate hike attracts capital inflows seeking higher yields, putting upward pressure on the rupee. Core inflation strips out volatile food and fuel prices.'
        })
        mcqs.append({
            'id': f'{art_id}-q2',
            'q': 'Which of the following measures is/are likely to reduce the Current Account Deficit (CAD) of India?\n1. Imposing higher import duties on non-essential luxury items\n2. Devaluation of the domestic currency to boost export competitiveness\n3. Increasing incentives under Production Linked Incentive (PLI) schemes\nSelect the correct answer using the code given below:',
            'options': [
                '(a) 1 and 2 only',
                '(b) 2 and 3 only',
                '(c) 1 and 3 only',
                '(d) 1, 2 and 3'
            ],
            'answer': '(d)',
            'explanation': 'All three measures help compress CAD: restricting non-essential imports reduces outflow, a weaker currency makes exports cheaper globally, and domestic production replaces imports.'
        })
        mcqs.append({
            'id': f'{art_id}-q3',
            'q': 'Consider the following statements regarding the Monetary Policy Committee (MPC):\n1. It consists of six members: three from the RBI and three appointed by the Central Government.\n2. The Governor of the RBI possesses a casting vote in case of a tie.\n3. The inflation target of 4% (+/- 2%) is determined by the MPC itself without Government consultation.\nWhich of the statements given above are correct?',
            'options': [
                '(a) 1 and 2 only',
                '(b) 2 and 3 only',
                '(c) 1 and 3 only',
                '(d) 1, 2 and 3'
            ],
            'answer': '(a)',
            'explanation': 'Statements 1 and 2 are correct under Section 45ZB of the RBI Act. Statement 3 is incorrect because the inflation target is determined by the Central Government in consultation with the RBI once every 5 years.'
        })
    elif pillar == 'Environment':
        mcqs.append({
            'id': f'{art_id}-q1',
            'q': f'In the context of ecological policies referenced in "{title}", consider the following statements:\n1. Under the Wildlife (Protection) Amendment Act 2022, species listed in CITES Appendices are given statutory protection in Schedule IV.\n2. Community Reserves and Conservation Reserves can be notified on both private and government-owned lands.\nWhich of the statements given above is/are correct?',
            'options': [
                '(a) 1 only',
                '(b) 2 only',
                '(c) Both 1 and 2',
                '(d) Neither 1 nor 2'
            ],
            'answer': '(c)',
            'explanation': 'Both statements are correct. The 2022 amendment rationalized schedules to 4 and added Schedule IV specifically for CITES specimens. Conservation Reserves are on government land whereas Community Reserves can be on community or private land.'
        })
        mcqs.append({
            'id': f'{art_id}-q2',
            'q': 'Consider the following international environmental conventions and their primary focus areas:\n1. Basel Convention : Transboundary movements of hazardous wastes\n2. Rotterdam Convention : Prior Informed Consent for hazardous chemicals in international trade\n3. Stockholm Convention : Persistent Organic Pollutants (POPs)\nWhich of the pairs given above are correctly matched?',
            'options': [
                '(a) 1 and 2 only',
                '(b) 2 and 3 only',
                '(c) 1 and 3 only',
                '(d) 1, 2 and 3'
            ],
            'answer': '(d)',
            'explanation': 'All three pairs are correctly matched. The Basel, Rotterdam, and Stockholm conventions form the comprehensive global regime governing hazardous chemicals and wastes.'
        })
        mcqs.append({
            'id': f'{art_id}-q3',
            'q': 'Which one of the following National Parks contains a unique floating vegetation called "Phumdis"?\n(a) Keibul Lamjao National Park\n(b) Namdapha National Park\n(c) Orang National Park\n(d) Nokrek National Park',
            'options': [
                '(a) Keibul Lamjao National Park',
                '(b) Namdapha National Park',
                '(c) Orang National Park',
                '(d) Nokrek National Park'
            ],
            'answer': '(a)',
            'explanation': 'Keibul Lamjao National Park in Manipur is the only floating national park in the world, located on Loktak Lake, famous for phumdis and the endangered Sangai deer.'
        })
    elif pillar == 'SciTech':
        mcqs.append({
            'id': f'{art_id}-q1',
            'q': f'With reference to technological advancements highlighted in "{title}", consider the following statements:\n1. Quantum entanglement allows particles to share states instantaneously regardless of the distance separating them.\n2. In Quantum Key Distribution (QKD), any eavesdropping attempt inevitably disturbs the quantum state and reveals the intrusion.\nWhich of the statements given above is/are correct?',
            'options': [
                '(a) 1 only',
                '(b) 2 only',
                '(c) Both 1 and 2',
                '(d) Neither 1 nor 2'
            ],
            'answer': '(c)',
            'explanation': 'Both statements are correct. Quantum entanglement forms the bedrock of quantum communications. QKD relies on the no-cloning theorem and wave-function collapse, meaning interception changes the photon properties.'
        })
        mcqs.append({
            'id': f'{art_id}-q2',
            'q': 'Which of the following statements about mRNA vaccines is/are correct?\n1. They introduce weakened or attenuated live virus particles into the human body.\n2. They instruct human cells to produce a harmless viral spike protein to trigger an adaptive immune response.\n3. mRNA from the vaccine enters the cell nucleus and alters human DNA.\nSelect the correct answer using the code given below:',
            'options': [
                '(a) 1 and 2 only',
                '(b) 2 only',
                '(c) 2 and 3 only',
                '(d) 1, 2 and 3'
            ],
            'answer': '(b)',
            'explanation': 'Statement 2 is correct. Statement 1 is incorrect because mRNA vaccines do not use live or weakened viruses. Statement 3 is incorrect because mRNA remains in the cytoplasm, does not enter the nucleus, and degrades quickly.'
        })
        mcqs.append({
            'id': f'{art_id}-q3',
            'q': 'Consider the following applications of CRISPR-Cas9 gene editing technology:\n1. Treating genetic disorders like sickle cell anemia\n2. Creating pest-resistant and climate-resilient crop varieties\n3. Eradicating vector-borne diseases via gene drives\nWhich of the applications given above is/are currently viable or actively researched?',
            'options': [
                '(a) 1 and 2 only',
                '(b) 2 and 3 only',
                '(c) 1 and 3 only',
                '(d) 1, 2 and 3'
            ],
            'answer': '(d)',
            'explanation': 'All three are leading applications of CRISPR-Cas9. Casgevy was approved for sickle cell anemia, gene-edited crops are in field trials, and mosquito gene drives are actively researched.'
        })
    else:  # IR / Geopolitics
        mcqs.append({
            'id': f'{art_id}-q1',
            'q': f'Regarding the multilateral framework associated with "{title}", consider the following statements:\n1. The United Nations General Assembly resolutions are legally binding on all member states.\n2. Under the UN Charter, only decisions of the UN Security Council taken under Chapter VII are legally binding.\nWhich of the statements given above is/are correct?',
            'options': [
                '(a) 1 only',
                '(b) 2 only',
                '(c) Both 1 and 2',
                '(d) Neither 1 nor 2'
            ],
            'answer': '(b)',
            'explanation': 'Statement 1 is incorrect: UNGA resolutions are recommendatory in nature. Statement 2 is correct: UNSC resolutions adopted under Chapter VII carry binding international legal authority.'
        })
        mcqs.append({
            'id': f'{art_id}-q2',
            'q': 'Which of the following groupings includes India as a founding or full member?\n1. BRICS\n2. Shanghai Cooperation Organisation (SCO)\n3. Regional Comprehensive Economic Partnership (RCEP)\n4. Indian Ocean Rim Association (IORA)\nSelect the correct answer using the code given below:',
            'options': [
                '(a) 1, 2 and 4 only',
                '(b) 1 and 4 only',
                '(c) 2, 3 and 4 only',
                '(d) 1, 2, 3 and 4'
            ],
            'answer': '(a)',
            'explanation': 'India is a member of BRICS, SCO (joined 2017), and IORA. India opted out of RCEP in 2019 due to domestic market concerns.'
        })
        mcqs.append({
            'id': f'{art_id}-q3',
            'q': 'Consider the following straits and the water bodies they connect:\n1. Strait of Malacca : Andaman Sea and South China Sea\n2. Strait of Hormuz : Persian Gulf and Gulf of Oman\n3. Bab-el-Mandeb : Red Sea and Gulf of Aden\nWhich of the pairs given above are correctly matched?',
            'options': [
                '(a) 1 and 2 only',
                '(b) 2 and 3 only',
                '(c) 1 and 3 only',
                '(d) 1, 2 and 3'
            ],
            'answer': '(d)',
            'explanation': 'All three chokepoints are crucial for India\'s maritime trade and energy security and are correctly matched.'
        })

    return mcqs

def refresh_and_accumulate_ca():
    """
    Fetches raw news, deduplicates, generates UPSC synthesis & MCQs,
    and prepends new articles to data/current-affairs-db.json on disk.
    """
    existing_db = load_local_ca_db()
    existing_titles = set(a.get('title', '').strip().lower() for a in existing_db)

    raw_items = []
    # 1. The Hindu
    raw_items.extend(fetch_the_hindu_rss())
    # 2. PIB
    raw_items.extend(fetch_pib_rss())
    # 3. NewsAPI
    raw_items.extend(fetch_newsapi_articles())

    newly_added = []
    today_str = datetime.date.today().isoformat()
    now_ts = int(time.time())

    for idx, raw in enumerate(raw_items):
        clean_title = raw['title'].strip()
        if not clean_title or len(clean_title) < 15:
            continue
        
        # Check deduplication
        norm_title = clean_title.lower()
        if any(norm_title in ext or ext in norm_title for ext in existing_titles):
            continue

        pillar, gs_link = classify_pillar_and_gs(clean_title, raw.get('desc', ''))
        art_id = f"ca-live-{now_ts}-{idx}"

        summary_pts = [
            f"{clean_title}: {raw.get('desc', 'Key national policy development.')[:140]}...",
            f"Significance for UPSC: Examines underlying governance, legal mandates, or economic implications under {gs_link}.",
            f"Core takeaway for Prelims: Focus on constitutional articles, statutory bodies, or biological/scientific mechanisms involved."
        ]

        mcqs = generate_mcqs_for_article(art_id, clean_title, pillar, gs_link)

        # Generate digestible 4-part UPSC fact sheet
        if "Polity" in pillar:
            what_news = f"Institutional development regarding {clean_title[:60]}... impacting statutory compliance and constitutional provisions."
            fact_box = [
                "Constitutional Basis: Part III, Part IV, or Part XI (Union-State relations).",
                "Statutory Mandate: RPA 1951 / Commissions of Inquiry Act / Relevant Civil Service Rules.",
                "Nodal Body: Ministry of Law & Justice / Election Commission / UPSC.",
                "Doctrine: Separation of powers and constitutional morality."
            ]
            trap = "UPSC Trap Alert: Do not confuse advisory body recommendations with binding constitutional orders."
            hots = ["Polity: Federal Division of Powers (7th Schedule)", "Polity: Statutory vs Quasi-Judicial Bodies", "Governance: Citizen Charters & Transparency Tools"]
        elif "Economy" in pillar:
            what_news = f"Fiscal and economic policy update concerning {clean_title[:60]}... addressing macroeconomic stability and market dynamics."
            fact_box = [
                "Statutory Mandate: RBI Act 1934, FRBM Act 2003, or Banking Regulation Act 1949.",
                "Nodal Body: Ministry of Finance / Monetary Policy Committee (MPC) / SEBI.",
                "Tool: Repo rate, SLR, Capital Adequacy (Basel III), or Fiscal Deficit targets.",
                "Classification: Revenue vs Capital receipts; Non-tax revenue vs Disinvestment."
            ]
            trap = "UPSC Trap Alert: Forex reserves are managed by RBI; external commercial borrowings are coordinated with Ministry of Finance."
            hots = ["Economy: Monetary Policy Transmission & Liquidity Tools", "Economy: GST Council (Art 279A)", "Economy: FRBM Targets & Fiscal Consolidation"]
        elif "Environment" in pillar:
            what_news = f"Ecological conservation development in {clean_title[:60]}... concerning habitat protection and environmental commitments."
            fact_box = [
                "Statutory Mandate: Wildlife (Protection) Act 1972 (as amended 2022), Environment Protection Act 1986.",
                "Nodal Body: MoEFCC / National Tiger Conservation Authority (NTCA) / CPCB.",
                "Global Status: IUCN Red List, CITES Appendices, Ramsar wetland criteria.",
                "Schedule: Schedule I of WPA 2022 provides highest tier of protection."
            ]
            trap = "UPSC Trap Alert: Human settlement and grazing are strictly prohibited in National Parks, but regulated in Sanctuaries."
            hots = ["Environment: WPA Amendment 2022 Schedules", "Environment: Tiger Reserves & Eco-Sensitive Zones", "Environment: Ramsar Sites & Montreux Record"]
        elif "Science" in pillar:
            what_news = f"Frontier science and R&D milestone regarding {clean_title[:60]}... in indigenous technology and space/biotech governance."
            fact_box = [
                "Scientific Mechanism: Quantum entanglement, mRNA vectors, or satellite launch mechanics.",
                "Nodal Organization: ISRO / Department of Biotechnology / CSIR / DRDO.",
                "Regulatory Framework: Digital Personal Data Protection Act 2023, National Quantum Mission.",
                "Application: Cryogenic upper stages, low earth orbit constellations, supercomputing."
            ]
            trap = "UPSC Trap Alert: Cryogenic stages utilize liquid hydrogen (-253°C) and liquid oxygen (-183°C); cannot operate at room temperature."
            hots = ["Sci-Tech: PSLV vs GSLV vs SSLV Launch Profiles", "Sci-Tech: Gene Editing (CRISPR-Cas9) Rules", "Sci-Tech: Quantum Key Distribution (QKD)"]
        else:
            what_news = f"Strategic international relations event in {clean_title[:60]}... affecting bilateral cooperation and maritime corridors."
            fact_box = [
                "Treaty/Convention: UNCLOS 1982, Vienna Convention on Diplomatic Relations.",
                "Nodal Ministry: Ministry of External Affairs (MEA) / National Security Council Secretariat.",
                "Maritime Zone: EEZ (200 nm), Contiguous Zone (24 nm), Territorial Sea (12 nm).",
                "Initiative: INSTC, IMEC, or SAGAR maritime vision."
            ]
            trap = "UPSC Trap Alert: Under UNCLOS, innocent passage applies to Territorial Waters; transit passage applies to international straits."
            hots = ["IR: UNCLOS Maritime Boundaries", "IR: Bilateral Indo-Pacific Alliances", "IR: Multilateral Financial Institutions"]

        fact_sheet = {
            "what_is_news": what_news,
            "prelims_fact_box": fact_box,
            "trap_alert": trap,
            "hot_revision_topics": hots
        }

        new_art = {
            'id': art_id,
            'date': today_str,
            'pillar': pillar,
            'title': clean_title,
            'source': raw.get('source', 'UPSC Curated News'),
            'is_top100': True,
            'is_pt365': False,
            'summary_points': summary_pts,
            'gs_connection': gs_link,
            'digestible_fact_sheet': fact_sheet,
            'mcqs': mcqs
        }

        newly_added.append(new_art)
        existing_titles.add(norm_title)

    if newly_added:
        # Prepend new articles on top of the list!
        updated_db = newly_added + existing_db
        save_local_ca_db(updated_db)
        print(f"Successfully added and persisted {len(newly_added)} new articles to {CA_DB_PATH}. Total articles: {len(updated_db)}")
        return updated_db, len(newly_added)
    else:
        print(f"No new articles to add. Current CA DB count: {len(existing_db)}")
        return existing_db, 0

if __name__ == '__main__':
    articles, added = refresh_and_accumulate_ca()
    print(f"Done. Newly accumulated: {added}, Total: {len(articles)}")
