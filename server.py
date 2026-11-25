#!/usr/bin/env python3
import http.server
import socketserver
import json
import os
import urllib.request
import xml.etree.ElementTree as ET
import time
from urllib.parse import urlparse
import urllib.parse
import concurrent.futures
import threading
import subprocess

PORT = 8080
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE_DIR, 'data', 'state.json')

# API Keys
GNEWS_API_KEY = '814e5041ca86391caf0e5dbe608c838f'
NEWSAPI_KEY = '5553ea2c4fac4d959128b48f32906764'

news_cache = {
    'timestamp': 0,
    'articles': []
}

import re

def classify_and_anchor(title, desc):
    """
    Filters for UPSC relevance using word boundaries and attaches syllabus static anchor & relevance score.
    """
    text = f"{title} {desc}".lower()
    
    # 1. Economy
    if re.search(r'\b(rbi|repo rate|monetary policy|inflation|bond|yield|gdp|fiscal|npa|banking|forex|imf|wto|cad|msp|rupee|t-bills|deficit|securities|disinvestment|fdi|fpi|sebi|liquidity|cess|surcharge|gst council|economic survey|budget|psb|priority sector|bad bank|narcl)\b', text):
        score = 85
        if re.search(r'\b(rbi|repo rate|monetary policy|fiscal deficit|gdp|wto|msp|gst council)\b', text):
            score = 94
        return 'Economy', 'Macroeconomics › Banking, Monetary Policy & Fiscal Framework', score
    
    # 2. Polity & Governance
    if re.search(r'\b(supreme court|high court|governor|parliament|lok sabha|rajya sabha|constitution|bill|ordinance|election commission|cji|bench|fundamental right|writs|10th schedule|defection|anti-defection|article \d+|collegium|tribunal|cag|finance commission|delimit|panchayat|pesa)\b', text):
        score = 88
        if re.search(r'\b(supreme court|constitution|article \d+|collegium|writs|fundamental right|governor)\b', text):
            score = 96
        return 'Polity', 'Indian Polity › Constitution, Parliament & Judicial Review', score
    
    # 3. Environment & Ecology
    if re.search(r'\b(wildlife|biodiversity|pollution|cop\d+|climate change|forest|wetland|ramsar|tiger reserve|national park|cheetah|air quality|endangered species|ecosystem|unfccc|green hydrogen|carbon credit|ocean acidification|aqi|naaqs|cpcb|cites|cms|kigali|montreal|iucn)\b', text):
        score = 86
        if re.search(r'\b(ramsar|tiger reserve|national park|unfccc|biodiversity|endangered|iucn)\b', text):
            score = 95
        return 'Environment', 'Environment › WPA 1972, Ramsar Sites, Treaties & Climate Mechanisms', score
    
    # 4. Science & Technology
    if re.search(r'\b(isro|satellite|gaganyaan|chandrayaan|aditya-l1|space station|drdo|missile|artificial intelligence|\bai\b|quantum computing|crispr|gene editing|biotechnology|mrna vaccine|antimicrobial resistance|\bamr\b|telescope|semiconductor|supercomputer|nuclear)\b', text):
        score = 84
        if re.search(r'\b(isro|crispr|aditya-l1|gaganyaan|quantum|drdo)\b', text):
            score = 92
        return 'SciTech', 'Science & Tech › Space Tech, Biotechnology & Public Health', score
    
    # 5. International Relations & Geopolitics
    if re.search(r'\b(brics|g20|sco|asean|quad|i2u2|summit|unclos|red sea|sahel|west asia|strait of hormuz|bab-el-mandeb|unsc|bilateral treaty|extradition|imec|chokepoint|gaza|taiwan)\b', text):
        score = 82
        if re.search(r'\b(brics|g20|quad|unclos|red sea|bab-el-mandeb|strait of hormuz)\b', text):
            score = 91
        return 'IR', 'International Relations › Multilateral Groupings & Strategic Geopolitics', score

    # 6. Reports, Indices & Governance
    if re.search(r'\b(report|index|ranking|niti aayog|undp|world bank|wef|hunger index|multidimensional poverty|hdi|mpi)\b', text):
        return 'Economy', 'Governance & Social Development › National & Global Indices', 88
    
    return None, None, 0

def fetch_gnews():
    items = []
    try:
        gnews_url = (
            f"https://gnews.io/api/v4/search?"
            f"q=India+AND+(RBI+OR+%22Supreme+Court%22+OR+ISRO+OR+Environment+OR+Economy+OR+Parliament)&"
            f"lang=en&country=in&max=10&apikey={GNEWS_API_KEY}"
        )
        req = urllib.request.Request(gnews_url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=3) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            for a in data.get('articles', []):
                items.append({
                    'source': a.get('source', {}).get('name', 'GNews'),
                    'title': a.get('title', ''),
                    'url': a.get('url', ''),
                    'desc': a.get('description', '') or '',
                    'time': a.get('publishedAt', '')
                })
    except Exception as e:
        print(f"GNews API error: {e}")
    return items

def fetch_google_rss():
    items = []
    try:
        gnews_rss = "https://news.google.com/rss/search?q=RBI+OR+ISRO+OR+%22Supreme+Court%22+OR+Biodiversity+OR+%22Cabinet+approves%22+OR+%22Monetary+Policy%22&hl=en-IN&gl=IN&ceid=IN:en"
        req = urllib.request.Request(gnews_rss, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=3) as resp:
            root = ET.fromstring(resp.read())
            for item in root.findall('./channel/item')[:12]:
                title = item.find('title').text if item.find('title') is not None else ''
                link = item.find('link').text if item.find('link') is not None else ''
                pub = item.find('pubDate').text if item.find('pubDate') is not None else ''
                src = item.find('source').text if item.find('source') is not None else 'Google News'
                items.append({
                    'source': src,
                    'title': title,
                    'url': link,
                    'desc': '',
                    'time': pub
                })
    except Exception as e:
        print(f"Google News RSS error: {e}")
    return items

def fetch_the_hindu():
    items = []
    try:
        hindu_rss = "https://www.thehindu.com/news/national/feeder/default.rss"
        req = urllib.request.Request(hindu_rss, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=3) as resp:
            root = ET.fromstring(resp.read())
            for item in root.findall('./channel/item')[:10]:
                title = item.find('title').text if item.find('title') is not None else ''
                link = item.find('link').text if item.find('link') is not None else ''
                desc = item.find('description').text if item.find('description') is not None else ''
                pub = item.find('pubDate').text if item.find('pubDate') is not None else ''
                items.append({
                    'source': 'The Hindu',
                    'title': title,
                    'url': link,
                    'desc': desc,
                    'time': pub
                })
    except Exception as e:
        print(f"The Hindu RSS error: {e}")
    return items

def fetch_newsapi():
    items = []
    try:
        napi_url = (
            f"https://newsapi.org/v2/everything?"
            f"domains=thehindu.com,indianexpress.com,livemint.com,business-standard.com&"
            f"q=%22Supreme+Court%22+OR+RBI+OR+ISRO+OR+Cabinet+OR+Economy&"
            f"sortBy=publishedAt&pageSize=8&apiKey={NEWSAPI_KEY}"
        )
        req = urllib.request.Request(napi_url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=3) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            for a in data.get('articles', []):
                items.append({
                    'source': a.get('source', {}).get('name', 'NewsAPI'),
                    'title': a.get('title', ''),
                    'url': a.get('url', ''),
                    'desc': a.get('description', '') or '',
                    'time': a.get('publishedAt', '')
                })
    except Exception as e:
        print(f"NewsAPI error: {e}")
    return items

def fetch_pib():
    items = []
    try:
        pib_url = "https://news.google.com/rss/search?q=site:pib.gov.in+AND+(Cabinet+OR+Ministry+OR+ISRO+OR+RBI+OR+Environment+OR+Supreme+Court)&hl=en-IN&gl=IN&ceid=IN:en"
        req = urllib.request.Request(pib_url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=3) as resp:
            root = ET.fromstring(resp.read())
            for item in root.findall('./channel/item')[:10]:
                title = item.find('title').text if item.find('title') is not None else ''
                link = item.find('link').text if item.find('link') is not None else ''
                pub = item.find('pubDate').text if item.find('pubDate') is not None else ''
                items.append({
                    'source': 'PIB',
                    'title': title,
                    'url': link,
                    'desc': '',
                    'time': pub
                })
    except Exception as e:
        print(f"PIB RSS error: {e}")
    return items

def fetch_upsc_curated_news():
    raw_articles = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        futures = [
            executor.submit(fetch_gnews),
            executor.submit(fetch_google_rss),
            executor.submit(fetch_the_hindu),
            executor.submit(fetch_newsapi),
            executor.submit(fetch_pib)
        ]
        for f in concurrent.futures.as_completed(futures):
            try:
                res = f.result()
                raw_articles.extend(res)
            except Exception as e:
                pass

    seen_titles = set()
    curated = []

    for idx, art in enumerate(raw_articles):
        title = art['title'].strip()
        norm_title = title.lower()[:45]
        if not title or norm_title in seen_titles:
            continue

        pillar, static_anchor, score = classify_and_anchor(title, art['desc'])
        if pillar is not None:
            seen_titles.add(norm_title)
            curated.append({
                'id': f"live-news-{len(curated)+1}",
                'title': title,
                'source': art['source'],
                'url': art['url'],
                'desc': art['desc'],
                'time': art['time'],
                'pillar': pillar,
                'static_anchor': static_anchor,
                'relevance_score': score
            })

    return curated[:30]

def commit_state_to_git():
    """Auto-commits data/ state changes to git and pushes if remote origin is configured."""
    try:
        subprocess.run(['git', 'add', 'data/state.json', 'data/current-affairs-db.json', 'data/csat-topic-questions-db.json', 'data/upsc-traps-vault.json'], cwd=BASE_DIR, capture_output=True)
        t_str = time.strftime('%Y-%m-%d %H:%M:%S')
        subprocess.run(['git', 'commit', '-m', f"Auto-save state and notes: {t_str}"], cwd=BASE_DIR, capture_output=True)
        chk = subprocess.run(['git', 'remote', 'get-url', 'origin'], cwd=BASE_DIR, capture_output=True, text=True)
        if chk.returncode == 0 and chk.stdout.strip():
            subprocess.run(['git', 'push', 'origin', 'main'], cwd=BASE_DIR, capture_output=True)
    except Exception as ge:
        pass

class OfficerPassHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        super().end_headers()

    def do_OPTIONS(self):
        self.send_response(200)
        self.end_headers()

    def do_GET(self):
        parsed = urlparse(self.path)
        
        # 1. API State
        if parsed.path == '/api/state':
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            if os.path.exists(DATA_FILE):
                with open(DATA_FILE, 'r') as f:
                    self.wfile.write(f.read().encode('utf-8'))
            else:
                self.wfile.write(b'{"checks": {}, "notes": {}}')
            return

        # 2. API News (UPSC Curated)
        if parsed.path == '/api/news':
            global news_cache
            now = time.time()
            if now - news_cache['timestamp'] > 600 or not news_cache['articles']:
                news_cache['articles'] = fetch_upsc_curated_news()
                news_cache['timestamp'] = now
            
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(news_cache['articles']).encode('utf-8'))
            return

# 2b. Force News Refresh with Persistent Storage
        if parsed.path == '/api/news/refresh':
            try:
                from ca_persist_engine import refresh_and_accumulate_ca
                updated_db, new_count = refresh_and_accumulate_ca()
                self.send_response(200)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({
                    'status': 'refreshed',
                    'count': new_count,
                    'total': len(updated_db)
                }).encode('utf-8'))
            except Exception as e:
                self.send_response(500)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({'error': str(e)}).encode('utf-8'))
            return

        # 2bb. Official UPSC Master PYQs API (1995-2026 GS & CSAT)
        if parsed.path == '/api/pyqs':
            pyq_file = os.path.join(BASE_DIR, 'data', 'pyq-master-db.json')
            if not os.path.exists(pyq_file):
                self.send_response(404)
                self.end_headers()
                self.wfile.write(b'{"error": "PYQ database not found"}')
                return

            with open(pyq_file, 'r', encoding='utf-8') as pf:
                pyqs = json.load(pf)

            params = dict(urllib.parse.parse_qsl(parsed.query))
            filtered = pyqs

            if params.get('subject') and params['subject'] != 'all':
                subj_filter = params['subject'].lower()
                filtered = [
                    q for q in filtered 
                    if q.get('subject_group', '').lower() == subj_filter 
                    or subj_filter in q.get('subject', '').lower()
                ]

            if params.get('year'):
                try:
                    y = int(params['year'])
                    filtered = [q for q in filtered if q.get('year') == y]
                except ValueError:
                    pass

            if params.get('era') and params['era'] != 'all':
                era = params['era']
                if era == 'recent': # 2024-2026
                    filtered = [q for q in filtered if q.get('year', 0) >= 2024]
                elif era == 'contemporary': # 2020-2023
                    filtered = [q for q in filtered if 2020 <= q.get('year', 0) <= 2023]
                elif era == 'classic': # 2015-2019
                    filtered = [q for q in filtered if 2015 <= q.get('year', 0) <= 2019]
                elif era == '2010_2014':
                    filtered = [q for q in filtered if 2010 <= q.get('year', 0) <= 2014]
                elif era == 'archive': # 1995-2009
                    filtered = [q for q in filtered if q.get('year', 0) < 2010]

            if params.get('q'):
                search_q = params['q'].lower().strip()
                filtered = [
                    q for q in filtered
                    if search_q in q.get('q', '').lower()
                    or search_q in q.get('topic', '').lower()
                    or search_q in str(q.get('year', ''))
                    or search_q in q.get('subject', '').lower()
                ]

            limit = int(params.get('limit', 100))
            offset = int(params.get('offset', 0))
            total_count = len(filtered)
            sliced = filtered[offset:offset+limit]

            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({
                'total': total_count,
                'count': len(sliced),
                'offset': offset,
                'limit': limit,
                'pyqs': sliced
            }).encode('utf-8'))
            return

        # 2c. CSAT Modules API
        if parsed.path == '/api/csat':
            csat_file = os.path.join(BASE_DIR, 'csat', 'csat-modules.json')
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            if os.path.exists(csat_file):
                with open(csat_file, 'r') as cf:
                    self.wfile.write(cf.read().encode('utf-8'))
            else:
                self.wfile.write(b'[]')
            return

        # 2d. CSAT Topic Practice Questions Bank (25+ questions per topic)
        if parsed.path == '/api/csat/questions':
            q_file = os.path.join(BASE_DIR, 'data', 'csat-topic-questions-db.json')
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            if os.path.exists(q_file):
                params = dict(urllib.parse.parse_qsl(parsed.query))
                topic_id = params.get('topic_id')
                day = params.get('day')
                with open(q_file, 'r') as qf:
                    data = json.load(qf)
                
                if topic_id and topic_id in data:
                    self.wfile.write(json.dumps(data[topic_id]).encode('utf-8'))
                elif day:
                    curr_file = os.path.join(BASE_DIR, 'data', 'curriculum-180.json')
                    matched_tid = None
                    if os.path.exists(curr_file):
                        with open(curr_file, 'r') as cf:
                            cdata = json.load(cf)
                            for d in cdata:
                                if str(d.get('day')) == str(day):
                                    matched_tid = d.get('csat_topic_bank_id')
                                    break
                    if matched_tid and matched_tid in data:
                        self.wfile.write(json.dumps(data[matched_tid]).encode('utf-8'))
                    else:
                        tid = f"csat-{((int(day)-1)%25)+1:02d}"
                        self.wfile.write(json.dumps(data.get(tid, {})).encode('utf-8'))
                else:
                    self.wfile.write(json.dumps(data).encode('utf-8'))
            else:
                self.wfile.write(b'{}')
            return

        # 3. Calendar direct feed
        if parsed.path in ['/calendar', '/officerpass.ics']:
            cal_file = os.path.join(BASE_DIR, 'calendar', 'officerpass-schedule.ics')
            if os.path.exists(cal_file):
                self.send_response(200)
                self.send_header('Content-Type', 'text/calendar; charset=utf-8')
                self.send_header('Content-Disposition', 'attachment; filename="officerpass-schedule.ics"')
                self.end_headers()
                with open(cal_file, 'rb') as f:
                    self.wfile.write(f.read())
                return

        # 4. CA endpoint (must check before root fallback)
        if parsed.path == '/api/ca':
            try:
                with open(os.path.join(BASE_DIR, 'data', 'current-affairs-db.json'), 'r') as f:
                    ca_data = json.load(f)
                params = dict(urllib.parse.parse_qsl(parsed.query))
                filtered = ca_data
                if params.get('pillar'):
                    filtered = [a for a in filtered if a.get('pillar','').lower() == params['pillar'].lower()]
                if params.get('date'):
                    filtered = [a for a in filtered if a.get('date','').startswith(params['date'])]
                if params.get('top100') == 'true':
                    filtered = [a for a in filtered if a.get('is_top100', False)]
                if params.get('pt365') == 'true':
                    filtered = [a for a in filtered if a.get('is_pt365', False)]
                if params.get('unread') == 'true':
                    state = {}
                    if os.path.exists(DATA_FILE):
                        with open(DATA_FILE, 'r') as sf:
                            state = json.load(sf)
                    read_dict = state.get('read_articles', {})
                    filtered = [a for a in filtered if not read_dict.get(a.get('id'), False)]
                include_mcqs = params.get('include_mcqs') == 'true'
                if not include_mcqs:
                    filtered = [{k: v for k, v in a.items() if k != 'mcqs'} for a in filtered]
                self.send_response(200)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps(filtered).encode('utf-8'))
            except Exception as e:
                self.send_response(500)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({'error': str(e)}).encode('utf-8'))
            return

        if parsed.path.startswith('/api/ca/'):
            article_id = parsed.path.replace('/api/ca/', '').strip('/')
            try:
                with open(os.path.join(BASE_DIR, 'data', 'current-affairs-db.json'), 'r') as f:
                    ca_data = json.load(f)
                article = next((a for a in ca_data if a['id'] == article_id), None)
                if article:
                    self.send_response(200)
                    self.send_header('Content-Type', 'application/json')
                    self.end_headers()
                    self.wfile.write(json.dumps(article).encode('utf-8'))
                else:
                    self.send_response(404)
                    self.send_header('Content-Type', 'application/json')
                    self.end_headers()
                    self.wfile.write(json.dumps({'error': 'Not found'}).encode('utf-8'))
            except Exception as e:
                self.send_response(500)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({'error': str(e)}).encode('utf-8'))
            return

        if parsed.path == '/api/curriculum':
            try:
                curriculum_file = os.path.join(BASE_DIR, 'data', 'curriculum-180.json')
                with open(curriculum_file, 'r') as f:
                    curriculum = json.load(f)
                params = dict(urllib.parse.parse_qsl(parsed.query))
                if params.get('day'):
                    day_num = int(params['day'])
                    day_data = next((d for d in curriculum if d['day'] == day_num), None)
                    result = day_data if day_data else {'error': 'Day not found'}
                else:
                    result = curriculum
                self.send_response(200)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps(result).encode('utf-8'))
            except Exception as e:
                self.send_response(500)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({'error': str(e)}).encode('utf-8'))
            return

        # 5. UPSC Traps Vault endpoint
        if parsed.path == '/api/traps':
            try:
                traps_file = os.path.join(BASE_DIR, 'data', 'upsc-traps-vault.json')
                with open(traps_file, 'r', encoding='utf-8') as f:
                    vault = json.load(f)
                params = dict(urllib.parse.parse_qsl(parsed.query))
                
                subject = params.get('subject')
                if subject and subject in vault.get('subjects', {}):
                    subj_data = vault['subjects'][subject]
                    items = subj_data.get('items', [])
                    if params.get('pyq') == 'true':
                        items = [it for it in items if it.get('is_pyq')]
                    if params.get('section'):
                        sec_num = int(params['section'])
                        items = [it for it in items if it.get('section_num') == sec_num]
                    if params.get('q'):
                        q_term = params['q'].lower()
                        items = [it for it in items if q_term in it.get('prompt','').lower() or q_term in it.get('distinction','').lower() or q_term in it.get('authority','').lower()]
                    result = {
                        'subject': subject,
                        'title': subj_data.get('title'),
                        'subtitle': subj_data.get('subtitle'),
                        'total_items': len(items),
                        'sections': subj_data.get('sections', []),
                        'items': items
                    }
                else:
                    result = vault

                self.send_response(200)
                self.send_header('Content-Type', 'application/json; charset=utf-8')
                self.end_headers()
                self.wfile.write(json.dumps(result, ensure_ascii=False).encode('utf-8'))
            except Exception as e:
                self.send_response(500)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({'error': str(e)}).encode('utf-8'))
            return

        # 6. Root
        if parsed.path in ['/', '/index.html']:
            self.path = '/dashboard/index.html'

        return super().do_GET()

    def do_POST(self):
        parsed = urlparse(self.path)
        if parsed.path == '/api/state':
            content_length = int(self.headers.get('Content-Length', 0))
            post_data = self.rfile.read(content_length)
            try:
                state_data = json.loads(post_data.decode('utf-8'))
                state_data['updatedAt'] = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())
                os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
                with open(DATA_FILE, 'w') as f:
                    json.dump(state_data, f, indent=2)
                
                # Auto-commit to Git in background thread
                threading.Thread(target=commit_state_to_git, daemon=True).start()

                self.send_response(200)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(b'{"status": "saved"}')
            except Exception as e:
                self.send_response(400)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({'error': str(e)}).encode('utf-8'))
            return

        self.send_response(404)
        self.end_headers()

def run_server():
    os.chdir(BASE_DIR)
    
    # Warm the news cache on startup in background
    def warm_cache():
        global news_cache
        try:
            news_cache['articles'] = fetch_upsc_curated_news()
            news_cache['timestamp'] = time.time()
            print(f"Pre-cached {len(news_cache['articles'])} UPSC curated news articles.")
        except Exception as e:
            print(f"Warm cache error: {e}")

    threading.Thread(target=warm_cache, daemon=True).start()

    http.server.ThreadingHTTPServer.allow_reuse_address = True
    with http.server.ThreadingHTTPServer(('0.0.0.0', PORT), OfficerPassHandler) as httpd:
        print(f"OfficerPass server running on port {PORT}")
        httpd.serve_forever()

if __name__ == '__main__':
    run_server()
