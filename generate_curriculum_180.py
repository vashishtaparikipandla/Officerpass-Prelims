import json
import datetime

start_date = datetime.date(2026, 11, 24)

# 1. Microtopics mapping from microtopics-db.json
with open('micro-topics/microtopics-db.json', 'r') as f:
    micro_db = json.load(f)

# Flatten microtopics
all_microtopics = {}
for subj, topic_list in micro_db.items():
    for t in topic_list:
        all_microtopics[t['id']] = t

print(f"Loaded {len(all_microtopics)} microtopics from DB.")
