#!/usr/bin/env python3
"""
format_csat_math_katex.py
Converts mathematical expressions in data/csat-topic-questions-db.json and
data/curriculum-180.json into standard KaTeX/LaTeX format ($ ... $):
1. Square roots: sqrt(X) -> $\\sqrt{X}$
2. Powers / Exponents: X^Y -> $X^{Y}$
3. Products / Multiplications: numbers * numbers or numbers x numbers -> $\\times$
4. Fractions and factorials properly wrapped in math mode.
"""

import json
import os
import re

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CSAT_DB_PATH = os.path.join(BASE_DIR, "data", "csat-topic-questions-db.json")
CURR_PATH = os.path.join(BASE_DIR, "data", "curriculum-180.json")

def format_math_string(text):
    if not text or not isinstance(text, str):
        return text

    # Step 1: Format nested/complex sqrt first: sqrt(...)
    # Handle sqrt with parentheses
    def repl_sqrt(m):
        inner = m.group(1).strip()
        # replace * with \times inside sqrt
        inner = re.sub(r'\s*[\*x]\s*', r' \\times ', inner)
        return f"$\\sqrt{{{inner}}}$"

    # Repeatedly match sqrt(...) in case of expressions
    for _ in range(3):
        text = re.sub(r'\bsqrt\s*\(([^()]+)\)', repl_sqrt, text, flags=re.IGNORECASE)

    # Step 2: Format powers like (7^95), 7^95, 2^(3^4), (57242)^9
    # Tower of powers: 2^(3^4)
    text = re.sub(r'(\d+)\^\((\d+)\^(\d+)\)', r'${\1}^{(\2^{\3})}$', text)
    # Parenthesized base with power: (7)^1999 or (25)^6251 or (a+b)^2
    text = re.sub(r'\(([a-zA-Z0-9\+\-\s]+)\)\^(\d+)', r'$(\1)^{\2}$', text)
    # Simple powers: 7^95, x^2, N^3
    def repl_pow(m):
        base = m.group(1)
        exp = m.group(2)
        return f"${base}^{{{exp}}}$"
    text = re.sub(r'(?<!\$)\b([a-zA-Z0-9]+)\^([a-zA-Z0-9]+)(?!\$)', repl_pow, text)

    # Step 3: Format products with 'x' between powers or numbers
    # e.g. $(3^{65})$ x $(8^{57})$ -> $(3^{65}) \times (8^{57})$
    text = re.sub(r'(\$\([^\$]+\)\$|\$[^\$]+\$)\s*x\s*(\$\([^\$]+\)\$|\$[^\$]+\$)', r'\1 \\times \2', text)
    # e.g. 7^95 x 3^58 when already in math mode
    text = re.sub(r'\$\s*\\times\s*\$', r' \\times ', text)

    # Step 4: Clean up any double dollar signs if created inside single expressions
    text = re.sub(r'\$\s*\$', '', text)

    return text

def process_csat_db():
    if not os.path.exists(CSAT_DB_PATH):
        print(f"File not found: {CSAT_DB_PATH}")
        return

    with open(CSAT_DB_PATH, "r", encoding="utf-8") as f:
        db = json.load(f)

    enhanced_count = 0
    for topic_id, topic in db.items():
        if "mental_model" in topic:
            topic["mental_model"] = format_math_string(topic["mental_model"])

        for q in topic.get("questions", []):
            orig_q = q.get("q", "")
            q["q"] = format_math_string(orig_q)
            if "options" in q:
                q["options"] = [format_math_string(opt) for opt in q["options"]]
            if "explanation" in q:
                q["explanation"] = format_math_string(q["explanation"])
            if "child_logic" in q:
                q["child_logic"] = format_math_string(q["child_logic"])

            if orig_q != q["q"]:
                enhanced_count += 1

    with open(CSAT_DB_PATH, "w", encoding="utf-8") as f:
        json.dump(db, f, indent=2, ensure_ascii=False)

    print(f"CSAT DB processed: {enhanced_count} questions updated with LaTeX KaTeX formatting.")

def process_curriculum():
    if not os.path.exists(CURR_PATH):
        return

    with open(CURR_PATH, "r", encoding="utf-8") as f:
        curr = json.load(f)

    count = 0
    for day in curr:
        for q in day.get("day_mcqs", []):
            q["q"] = format_math_string(q.get("q", ""))
            if "options" in q:
                q["options"] = [format_math_string(opt) for opt in q["options"]]
            if "explanation" in q:
                q["explanation"] = format_math_string(q.get("explanation", ""))
            count += 1

        for q in day.get("day_csat_pyqs", []):
            q["q"] = format_math_string(q.get("q", ""))
            if "options" in q:
                q["options"] = [format_math_string(opt) for opt in q["options"]]
            if "explanation" in q:
                q["explanation"] = format_math_string(q.get("explanation", ""))
            count += 1

    with open(CURR_PATH, "w", encoding="utf-8") as f:
        json.dump(curr, f, indent=2, ensure_ascii=False)

    print(f"Curriculum processed: {count} questions inspected/formatted.")

if __name__ == "__main__":
    process_csat_db()
    process_curriculum()
