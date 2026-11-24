#!/usr/bin/env python3
"""
assemble_master_csat_database.py
Merges Groups 1 to 5 into data/csat-topic-questions-db.json and strictly validates
all 650 distinct questions across all 25 topics.
"""

import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
OUTPUT_FILE = os.path.join(DATA_DIR, "csat-topic-questions-db.json")

group_files = [
    os.path.join(DATA_DIR, "csat_topics_01_05.json"),
    os.path.join(DATA_DIR, "csat_topics_06_10.json"),
    os.path.join(DATA_DIR, "csat_topics_11_15.json"),
    os.path.join(DATA_DIR, "csat_topics_16_20.json"),
    os.path.join(DATA_DIR, "csat_topics_21_25.json"),
]

master_db = {}

for gfile in group_files:
    if not os.path.exists(gfile):
        raise FileNotFoundError(f"Missing group file: {gfile}")
    with open(gfile, "r", encoding="utf-8") as f:
        gdata = json.load(f)
        master_db.update(gdata)

print(f"Total topics loaded: {len(master_db)}")
assert len(master_db) == 25, f"Expected 25 topics, got {len(master_db)}"

total_questions = 0
all_q_ids = set()

for tid in sorted(master_db.keys()):
    topic = master_db[tid]
    questions = topic["questions"]
    assert len(questions) == 26, f"Topic {tid} has {len(questions)} questions instead of 26"
    
    q_texts = set()
    for q in questions:
        assert q["id"] not in all_q_ids, f"Duplicate ID: {q['id']}"
        all_q_ids.add(q["id"])
        
        assert len(q["options"]) == 4, f"Options count error in {q['id']}: {q['options']}"
        assert q["answer"] in ["(a)", "(b)", "(c)", "(d)"], f"Invalid answer key in {q['id']}: {q['answer']}"
        assert len(q["q"].strip()) > 10, f"Question text too short in {q['id']}"
        assert len(q["child_logic"].strip()) > 5, f"Child logic missing in {q['id']}"
        assert len(q["explanation"].strip()) > 5, f"Explanation missing in {q['id']}"
        
        # Verify uniqueness within topic
        q_norm = q["q"].strip()
        assert q_norm not in q_texts, f"Duplicate question text within topic {tid}: {q_norm}"
        q_texts.add(q_norm)
        
        total_questions += 1

print(f"Total questions validated: {total_questions} across 25 topics.")

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    json.dump(master_db, f, indent=2, ensure_ascii=False)

print(f"Successfully assembled and saved to {OUTPUT_FILE} ({os.path.getsize(OUTPUT_FILE)} bytes)!")
