#!/usr/bin/env python3
"""
generate_full_csat_database.py
Generates the authoritative, 650-question CSAT Topic Questions Database for OfficerPass.
25 topics x 26 distinct, non-repetitive, high-probability UPSC questions = 650 questions.
Each question contains:
- id: e.g. csat-01-q01
- topic_id: csat-01
- topic: title
- index: 1-26
- year_tag: [UPSC CSAT 2023] or [UPSC CSAT Predictor 2027]
- difficulty: Official Standard or UPSC Hard
- is_predictor_2027: bool
- q: Question text
- options: 4 options
- answer: (a), (b), (c), or (d)
- child_logic: 6th-grade visual intuition
- explanation: Step-by-step rigorous solution
"""

import json
import os
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_FILE = os.path.join(BASE_DIR, "data", "csat-topic-questions-db.json")

def make_q(tid, title, idx, ytag, diff, is_pred, q, opts, ans, child, expl):
    assert len(opts) == 4, f"Options must have 4 items: {opts}"
    assert ans in ["(a)", "(b)", "(c)", "(d)"], f"Answer must be in (a)-(d): {ans}"
    return {
        "id": f"{tid}-q{idx:02d}",
        "topic_id": tid,
        "topic": title,
        "index": idx,
        "year_tag": ytag,
        "difficulty": diff,
        "is_predictor_2027": is_pred,
        "q": q,
        "options": opts,
        "answer": ans,
        "child_logic": child,
        "explanation": expl
    }

def build_topic_01():
    tid = "csat-01"
    title = "Number System: Unit Digit Cyclicity & Exponent Powers"
    model = "Ferris Wheel Loop: Divide the power by 4. The remainder tells you which spoke on the 4-step wheel to take (rem 1->power 1, rem 2->power 2, rem 3->power 3, rem 0->power 4). Digits 0, 1, 5, 6 never change."
    specs = [
        ("[UPSC CSAT 2023]", "Official Standard", False,
         "What is the unit digit in the expansion of (57242)^9 x 7 x 5 x 3 x 1 ?",
         ["(a) 0", "(b) 2", "(c) 4", "(d) 6"], "(a)",
         "Ferris Wheel + Zero Lock: The base 57242 ends in 2 (an even number) and is multiplied by 5. Any even number multiplied by 5 ALWAYS ends in 0!",
         "Base ends in 2; multiplying any even number by 5 yields unit digit 0 (e.g. 2 x 5 = 10). Once 0 is formed at unit place, any further multiplication preserves 0."),
        ("[UPSC CSAT 2023]", "Official Standard", False,
         "What is the remainder when 85 x 87 x 89 x 91 x 95 x 96 is divided by 100 ?",
         ["(a) 0", "(b) 1", "(c) 2", "(d) 4"], "(a)",
         "Zero Hunt: 100 = 25 x 4. 85 = 5x17, 95 = 5x19 (gives 5x5=25). 96 = 4x24 (gives 4). 25 x 4 = 100 divides cleanly!",
         "85 = 5*17, 95 = 5*19 -> product contains 25. 96 = 4*24 -> product contains 4. 25*4 = 100 is a factor, so remainder is 0."),
        ("[UPSC CSAT 2021]", "Official Standard", False,
         "What is the unit digit of the expression 3^2019 ?",
         ["(a) 1", "(b) 3", "(c) 7", "(d) 9"], "(c)",
         "Ferris Wheel: 3 cyclicity is 4 (3, 9, 7, 1). 2019 / 4 leaves remainder 3. 3^3 = 27 -> unit digit 7!",
         "2019 = 4 * 504 + 3. Effective power is 3. 3^3 = 27. Unit digit is 7."),
        ("[UPSC CSAT 2017]", "Official Standard", False,
         "How many numbers are there between 99 and 1000 such that the digit 8 occupies the units place ?",
         ["(a) 64", "(b) 80", "(c) 90", "(d) 104"], "(c)",
         "Block Counting: From 100 to 999 there are 900 numbers. Exactly 1 in every 10 ends in 8. 900 / 10 = 90!",
         "Hundreds place has 9 choices (1-9), tens place has 10 choices (0-9), units place is fixed as 8 (1 choice). 9 * 10 * 1 = 90."),
        ("[UPSC CSAT 2016]", "Official Standard", False,
         "What is the unit digit in the product 781^80 x 256^45 x 312^36 ?",
         ["(a) 2", "(b) 4", "(c) 6", "(d) 8"], "(c)",
         "Fixed Anchor: 1^any = 1. 6^any = 6. 2^36 has 36/4=rem 0 -> 2^4 = 16 (ends in 6). 1 x 6 x 6 = 36 -> ends in 6!",
         "781^80 ends in 1; 256^45 ends in 6; 312^36: 36 is divisible by 4, so 2^4 ends in 6. Product = 1 * 6 * 6 = 36 -> unit digit is 6."),
        ("[UPSC CSAT 2014]", "Official Standard", False,
         "What is the unit digit of (432)^412 x (499)^431 ?",
         ["(a) 2", "(b) 4", "(c) 6", "(d) 8"], "(b)",
         "2 and 9 rules: 2^412 (412 div by 4) -> 2^4 ends in 6. 9^odd ends in 9. 6 x 9 = 54 -> ends in 4!",
         "412 mod 4 = 0 -> 2^4 ends in 6. 431 is odd -> 9^odd ends in 9. 6 x 9 = 54. Unit digit is 4."),
        ("[UPSC CSAT Predictor 2027]", "UPSC Hard", True,
         "What is the unit digit of 7^95 - 3^58 ?",
         ["(a) 4", "(b) 6", "(c) 7", "(d) 0"], "(a)",
         "Ferris Wheel: 7^95 -> 95 mod 4 = 3 -> 7^3 ends in 3. 3^58 -> 58 mod 4 = 2 -> 3^2 ends in 9. 13 - 9 = 4 (borrow 1)!",
         "7^95: 95 = 4*23 + 3 -> 7^3 = 343 (ends in 3). 3^58: 58 = 4*14 + 2 -> 3^2 = 9. When subtracting, borrow 10: 13 - 9 = 4."),
        ("[UPSC CSAT Predictor 2027]", "UPSC Hard", True,
         "What is the unit digit of (13^24) x (68^57) x (24^13) ?",
         ["(a) 2", "(b) 4", "(c) 6", "(d) 8"], "(a)",
         "Calculate each: 3^24 ends in 1 (24 div by 4). 8^57 (57 mod 4 = 1) ends in 8. 4^13 (odd power) ends in 4. 1 x 8 x 4 = 32 -> ends in 2!",
         "3^24 ends in 1; 8^57: 57 mod 4 = 1 -> ends in 8; 4^13: 4^odd ends in 4. Product = 1 * 8 * 4 = 32 -> unit digit is 2."),
        ("[UPSC CSAT Predictor 2027]", "UPSC Hard", True,
         "Find the unit digit of the sum S = 1! + 2! + 3! + 4! + 5! + ... + 100!.",
         ["(a) 1", "(b) 3", "(c) 5", "(d) 7"], "(b)",
         "Factorial Zero Lock: 5! = 120 and every factorial beyond 5! ends in 0. So only sum 1! to 4!: 1 + 2 + 6 + 24 = 33 -> ends in 3!",
         "1! = 1, 2! = 2, 3! = 6, 4! = 24. Sum = 33. All n! for n >= 5 contain 2*5 = 10, thus end in 0. Total sum unit digit = 3."),
        ("[UPSC CSAT Predictor 2027]", "UPSC Hard", True,
         "What is the unit digit of (17)^1999 + (11)^1999 - (7)^1999 ?",
         ["(a) 1", "(b) 3", "(c) 7", "(d) 9"], "(a)",
         "Cancellation: 17^1999 and 7^1999 have the exact same unit digit! They cancel out to 0. 11^1999 always ends in 1. Net unit digit = 1!",
         "Unit digit of 17^k equals unit digit of 7^k. Therefore, 17^1999 - 7^1999 ends in 0. 11^1999 ends in 1. 0 + 1 = 1."),
        ("[UPSC CSAT Predictor 2027]", "UPSC Hard", True,
         "What is the unit digit of 2^(3^4) ?",
         ["(a) 2", "(b) 4", "(c) 6", "(d) 8"], "(a)",
         "Tower of Powers: 3^4 = 81. 81 mod 4 = 1. So 2^81 ends in 2^1 = 2!",
         "3^4 = 81. We need unit digit of 2^81. 81 = 4*20 + 1 -> remainder is 1. 2^1 = 2."),
        ("[UPSC CSAT Predictor 2027]", "UPSC Hard", True,
         "What is the unit digit of 8^100 - 4^100 ?",
         ["(a) 0", "(b) 2", "(c) 4", "(d) 6"], "(a)",
         "Powers mod 4: 8^100 (100 div by 4) -> 8^4 ends in 6. 4^100 (even power) ends in 6. 6 - 6 = 0!",
         "8^100: 100 is divisible by 4, so unit digit is 8^4 mod 10 = 6. 4^even ends in 6. 6 - 6 = 0."),
        ("[UPSC CSAT Predictor 2027]", "UPSC Hard", True,
         "What is the unit digit of the expression 1^6 + 2^6 + 3^6 + 4^6 + 5^6 + 6^6 ?",
         ["(a) 1", "(b) 5", "(c) 7", "(d) 9"], "(a)",
         "Add each term mod 10: 1^6=1, 2^6=64(4), 3^6=729(9), 4^6=(6), 5^6=(5), 6^6=(6). Sum = 1+4+9+6+5+6 = 31 -> ends in 1!",
         "1^6 = 1; 2^6 = 64 -> 4; 3^6 = 9^3 -> 9; 4^6 = 6; 5^6 = 5; 6^6 = 6. Sum = 1 + 4 + 9 + 6 + 5 + 6 = 31 -> unit digit is 1."),
        ("[UPSC CSAT Predictor 2027]", "UPSC Hard", True,
         "Find the unit digit of (234)^100 + (234)^101.",
         ["(a) 0", "(b) 4", "(c) 6", "(d) 8"], "(a)",
         "Alternating 4: 4^even ends in 6, 4^odd ends in 4. Sum = 6 + 4 = 10 -> ends in 0!",
         "4^100 ends in 6; 4^101 ends in 4. 6 + 4 = 10. Unit digit is 0."),
        ("[UPSC CSAT Predictor 2027]", "UPSC Hard", True,
         "What is the unit digit of (12345k)^72 if the unit digit is 6? Which digit can k NOT be?",
         ["(a) 2", "(b) 4", "(c) 6", "(d) 5"], "(d)",
         "Zero/Five Rule: Any number ending in 5 raised to any power ends in 5, NEVER 6! So k can never be 5.",
         "Powers of numbers ending in 5 always end in 5. Thus, k cannot be 5."),
        ("[UPSC CSAT Predictor 2027]", "UPSC Hard", True,
         "What is the unit digit of 3^65 x 6^59 x 7^71 ?",
         ["(a) 2", "(b) 4", "(c) 6", "(d) 8"], "(b)",
         "Step-by-step: 3^65 (65 mod 4 = 1) -> 3. 6^59 -> 6. 7^71 (71 mod 4 = 3) -> 7^3 ends in 3. Product = 3 x 6 x 3 = 54 -> ends in 4!",
         "3^65 ends in 3; 6^59 ends in 6; 7^71 ends in 3. 3 * 6 * 3 = 54 -> unit digit is 4."),
        ("[UPSC CSAT Predictor 2027]", "UPSC Hard", True,
         "If the unit digit of (7^k) is 3, what will be the unit digit of (3^k)?",
         ["(a) 1", "(b) 3", "(c) 7", "(d) 9"], "(c)",
         "Cyclicity matching: 7^k ends in 3 when k is of form 4n + 3 (e.g. 7^3 = 343). For 3^(4n+3), 3^3 = 27 -> ends in 7!",
         "7^1=7, 7^2=9, 7^3=3, 7^4=1. Unit digit 3 means k = 4n + 3. For 3^k: 3^(4n+3) has unit digit 3^3 = 27 -> 7."),
        ("[UPSC CSAT Predictor 2027]", "UPSC Hard", True,
         "What is the unit digit of (2137)^753 ?",
         ["(a) 1", "(b) 3", "(c) 7", "(d) 9"], "(c)",
         "Last two digits: 53 mod 4 = 1. So 7^1 = 7!",
         "753 mod 4 = 1. 7^1 = 7. Unit digit is 7."),
        ("[UPSC CSAT Predictor 2027]", "UPSC Hard", True,
         "What is the unit digit of 9^1 + 9^2 + 9^3 + ... + 9^20 ?",
         ["(a) 0", "(b) 1", "(c) 5", "(d) 9"], "(a)",
         "Pairing: 9^odd ends in 9, 9^even ends in 1. Each pair (9^1 + 9^2) ends in 9+1=10 (ends in 0). 10 such pairs -> ends in 0!",
         "There are 10 pairs of (9 + 1) = 10. The sum of 10 terms ending in 0 ends in 0."),
        ("[UPSC CSAT Predictor 2027]", "UPSC Hard", True,
         "What is the unit digit of 7^105 ?",
         ["(a) 1", "(b) 3", "(c) 7", "(d) 9"], "(c)",
         "Ferris Wheel: 105 mod 4 = 1. 7^1 = 7!",
         "105 = 4*26 + 1. Effective power is 1. 7^1 = 7."),
        ("[UPSC CSAT Predictor 2027]", "UPSC Hard", True,
         "What is the unit digit of (153)^98 + (157)^98 ?",
         ["(a) 8", "(b) 6", "(c) 4", "(d) 0"], "(a)",
         "Cyclicity 4: 98 mod 4 = 2. 3^2 ends in 9. 7^2 ends in 9. Sum = 9 + 9 = 18 -> ends in 8!",
         "98 mod 4 = 2. 3^2 = 9. 7^2 = 49 -> 9. 9 + 9 = 18 -> unit digit is 8."),
        ("[UPSC CSAT Predictor 2027]", "UPSC Hard", True,
         "Find the unit digit of (25)^6251 + (36)^528 + (73)^54.",
         ["(a) 0", "(b) 4", "(c) 6", "(d) 8"], "(a)",
         "Term by term: 5^any ends in 5. 6^any ends in 6. 3^54 (54 mod 4 = 2) ends in 3^2 = 9. 5 + 6 + 9 = 20 -> ends in 0!",
         "5 + 6 + 9 = 20. Unit digit is 0."),
        ("[UPSC CSAT Predictor 2027]", "UPSC Hard", True,
         "What is the unit digit of 2^51 ?",
         ["(a) 2", "(b) 4", "(c) 6", "(d) 8"], "(d)",
         "Cyclicity of 2: 51 mod 4 = 3. 2^3 = 8!",
         "51 = 4*12 + 3. 2^3 = 8. Unit digit is 8."),
        ("[UPSC CSAT Predictor 2027]", "UPSC Hard", True,
         "What is the unit digit of 4^1 x 9^2 x 4^3 x 9^4 x ... x 4^99 x 9^100 ?",
         ["(a) 4", "(b) 6", "(c) 1", "(d) 9"], "(b)",
         "Group into pairs: (4^odd x 9^even) = (4 x 1) = 4. There are 50 pairs: 4^50. 4^even ends in 6!",
         "Each pair 4^(2k-1)*9^(2k) ends in 4*1 = 4. There are 50 such pairs. Product = 4^50. 4^even ends in 6."),
        ("[UPSC CSAT Predictor 2027]", "UPSC Hard", True,
         "What is the unit digit of (678)^567 ?",
         ["(a) 2", "(b) 4", "(c) 6", "(d) 8"], "(a)",
         "8 cyclicity: 567 mod 4 = 67 mod 4 = 3. 8^3 = 512 -> ends in 2!",
         "67 = 4*16 + 3. 8^3 = 512 -> unit digit is 2."),
        ("[UPSC CSAT Predictor 2027]", "UPSC Hard", True,
         "What is the unit digit of 11^1 + 12^2 + 13^3 + 14^4 + 15^5 + 16^6 ?",
         ["(a) 5", "(b) 7", "(c) 9", "(d) 1"], "(c)",
         "Sum unit digits: 1 + 4 + 7 + 6 + 5 + 6 = 29 -> ends in 9!",
         "11^1=1, 12^2=4, 13^3=7, 14^4=6, 15^5=5, 16^6=6. 1+4+7+6+5+6 = 29 -> unit digit is 9.")
    ]
    qs = [make_q(tid, title, i, s[0], s[1], s[2], s[3], s[4], s[5], s[6], s[7]) for i, s in enumerate(specs, 1)]
    return {"topic_id": tid, "title": title, "mental_model": model, "questions": qs}

print("Topic 01 definition ready")
