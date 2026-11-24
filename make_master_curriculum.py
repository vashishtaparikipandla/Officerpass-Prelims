import json
import datetime
import os

start_date = datetime.date(2026, 11, 24)

# Load microtopics DB
with open('micro-topics/microtopics-db.json', 'r') as f:
    micro_db = json.load(f)

# Load CA DB
with open('data/current-affairs-db.json', 'r') as f:
    ca_db = json.load(f)

# Load sample polity 50q
with open('practice-tests/micro-topics/polity-parliament-50q.json', 'r') as f:
    polity_50q = json.load(f)

print(f"Data sources loaded: {len(micro_db)} subjects, {len(ca_db)} CA articles, {len(polity_50q)} polity MCQs.")
