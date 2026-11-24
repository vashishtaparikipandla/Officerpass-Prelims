import json
import datetime
import os

start_date = datetime.date(2026, 11, 24)

# Microtopics DB
with open('micro-topics/microtopics-db.json', 'r') as f:
    micro_db = json.load(f)

# CA DB
with open('data/current-affairs-db.json', 'r') as f:
    ca_db = json.load(f)

# CA MCQs pool
ca_mcqs_by_pillar = {
    'Polity': [],
    'Economy': [],
    'Environment': [],
    'SciTech': [],
    'Geography': [],
    'History': [],
    'IR': []
}
for art in ca_db:
    pil = art.get('pillar', 'Polity')
    if pil in ca_mcqs_by_pillar:
        for m in art.get('mcqs', []):
            ca_mcqs_by_pillar[pil].append({
                'topic': f"{pil} Current Affairs",
                'type': 'statement',
                'q': m.get('q', ''),
                'options': m.get('options', []),
                'answer': m.get('answer', '(a)'),
                'explanation': m.get('explanation', '')
            })

# Load Polity 50Q
with open('practice-tests/micro-topics/polity-parliament-50q.json', 'r') as f:
    polity_50q = json.load(f)

print(f"Loaded CA MCQs: { {k: len(v) for k, v in ca_mcqs_by_pillar.items()} }")
