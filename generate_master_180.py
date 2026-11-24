import json
import datetime
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, 'data')

# 1. Load microtopics and CA database to draw from
with open(os.path.join(BASE_DIR, 'micro-topics', 'microtopics-db.json'), 'r') as f:
    micro_db = json.load(f)

with open(os.path.join(DATA_DIR, 'current-affairs-db.json'), 'r') as f:
    ca_db = json.load(f)

# Load existing 50Q polity practice questions
polity_50q_file = os.path.join(BASE_DIR, 'practice-tests', 'micro-topics', 'polity-parliament-50q.json')
polity_50q = []
if os.path.exists(polity_50q_file):
    with open(polity_50q_file, 'r') as f:
        polity_50q = json.load(f)

print(f"Loaded microtopics, {len(ca_db)} CA articles, and {len(polity_50q)} sample practice questions.")
