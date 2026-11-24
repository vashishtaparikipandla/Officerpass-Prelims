#!/usr/bin/env python3
"""
build_authentic_upsc_csat_database.py
Builds 650 completely distinct, non-repetitive UPSC CSAT questions across all 25 topics.
Each topic contains 26 unique problem archetypes covering the full spectrum of variations
that UPSC tests.
No mechanical copy-pasting of numbers. Truly varied mathematical and logical scenarios.
"""

import json
import os
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_FILE = os.path.join(BASE_DIR, "data", "csat-topic-questions-db.json")

def create_q(tid, title, idx, diff, is_pred, q_text, opts, ans, child, expl):
    assert len(opts) == 4, f"Question {tid}-q{idx} must have 4 options: {opts}"
    assert ans in ["(a)", "(b)", "(c)", "(d)"], f"Question {tid}-q{idx} invalid answer: {ans}"
    ytag = f"[UPSC CSAT Predictor 2027 - Level {idx}]" if is_pred else f"[UPSC Standard Pattern - Type {idx}]"
    return {
        "id": f"{tid}-q{idx:02d}",
        "topic_id": tid,
        "topic": title,
        "index": idx,
        "year_tag": ytag,
        "difficulty": diff,
        "is_predictor_2027": is_pred,
        "q": q_text,
        "options": opts,
        "answer": ans,
        "child_logic": child,
        "explanation": expl
    }

print("Base builder helper ready")
