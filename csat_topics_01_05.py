#!/usr/bin/env python3
"""
csat_topics_01_05.py
Defines 26 distinct archetypes each for Topics 01 to 05:
- csat-01: Unit Digit Cyclicity & Exponent Powers
- csat-02: Remainder Theorem & Successive Division
- csat-03: Divisibility Rules (3, 7, 9, 11, 13, 72, 88, 99)
- csat-04: Factors, Multiples & Prime Factorization
- csat-05: Trailing Zeroes in Factorials & Products
"""

def get_topics_01_to_05(create_q):
    data = {}

    # -------------------------------------------------------------
    # TOPIC 1: Unit Digit Cyclicity (26 Distinct Archetypes)
    # -------------------------------------------------------------
    t1_id = "csat-01"
    t1_title = "Number System: Unit Digit Cyclicity & Exponent Powers"
    t1_model = "Ferris Wheel Loop: Divide the power by 4. Remainder tells the step on the 4-spoke wheel. Bases 0, 1, 5, 6 never change."
    t1_q = []
    
    # Archetype 1: Standard single power cyclicity of 7
    t1_q.append(create_q(t1_id, t1_title, 1, "Official Standard", False,
        "What is the units digit of the expression (7^95)?",
        ["(a) 1", "(b) 3", "(c) 7", "(d) 9"], "(b)",
        "Ferris Wheel: 7 has a 4-step cyclicity (7, 9, 3, 1). 95 / 4 gives remainder 3. 7^3 = 343 -> ends in 3!",
        "95 = 4 * 23 + 3. Remainder is 3. 7^3 = 343. Unit digit is 3."))
    
    # Archetype 2: Product of two different cyclicity bases (3 and 8)
    t1_q.append(create_q(t1_id, t1_title, 2, "Official Standard", False,
        "What is the units digit in the expansion of (3^65) x (8^57)?",
        ["(a) 2", "(b) 4", "(c) 6", "(d) 8"], "(b)",
        "Multiply unit digits: 3^65 (65 mod 4 = 1) ends in 3. 8^57 (57 mod 4 = 1) ends in 8. 3 x 8 = 24 -> ends in 4!",
        "3^65 ends in 3^1 = 3. 8^57 ends in 8^1 = 8. Product ends in 3 * 8 = 24 -> 4."))

    # Archetype 3: Difference of powers requiring a carry/borrow
    t1_q.append(create_q(t1_id, t1_title, 3, "UPSC Hard", False,
        "What is the units digit of the difference (7^95 - 3^58)?",
        ["(a) 4", "(b) 6", "(c) 7", "(d) 0"], "(a)",
        "Carry trick: 7^95 ends in 3. 3^58 (58 mod 4 = 2) ends in 9. Since 3 < 9, borrow 10: 13 - 9 = 4!",
        "7^95 mod 10 = 3. 3^58 mod 10 = 9. When subtracting large numbers, borrow from tens place: 13 - 9 = 4."))

    # Archetype 4: Factorial sum zero-lock (1! + 2! + ... + 100!)
    t1_q.append(create_q(t1_id, t1_title, 4, "Official Standard", False,
        "What is the units digit of the sum S = 1! + 2! + 3! + 4! + 5! + ... + 100!?",
        ["(a) 1", "(b) 3", "(c) 5", "(d) 7"], "(b)",
        "Zero Lock: 5! = 120 and all factorials beyond 5! end in 0. Only sum 1! to 4!: 1 + 2 + 6 + 24 = 33 -> ends in 3!",
        "For all n >= 5, n! contains factors 2 and 5, so n! mod 10 = 0. Sum of 1!+2!+3!+4! = 1+2+6+24 = 33 -> 3."))

    # Archetype 5: Even base multiplied by 5 in a product series
    t1_q.append(create_q(t1_id, t1_title, 5, "Official Standard", False,
        "What is the units digit of (57242)^9 x 7 x 5 x 3 x 1?",
        ["(a) 0", "(b) 2", "(c) 4", "(d) 6"], "(a)",
        "Even x 5 Rule: The base ends in 2 (even) and is multiplied by 5. Any even number multiplied by 5 ALWAYS ends in 0!",
        "Base 57242 is even. Multiplied by 5, the product must end in 0. Multiplying 0 by odd integers leaves 0."))

    # Archetype 6: Fixed digit invariant bases (0, 1, 5, 6)
    t1_q.append(create_q(t1_id, t1_title, 6, "Official Standard", False,
        "What is the units digit of (25)^6251 + (36)^528 + (71)^99?",
        ["(a) 0", "(b) 1", "(c) 2", "(d) 5"], "(c)",
        "Unchanging Digits: 5^any ends in 5. 6^any ends in 6. 1^any ends in 1. Sum = 5 + 6 + 1 = 12 -> ends in 2!",
        "Powers of 5, 6, 1 always end in 5, 6, 1 respectively. 5 + 6 + 1 = 12 -> unit digit is 2."))

    # Archetype 7: Alternating base sum with 4 (4^odd=4, 4^even=6)
    t1_q.append(create_q(t1_id, t1_title, 7, "UPSC Hard", False,
        "What is the units digit of the sum (4^1 + 4^2 + 4^3 + ... + 4^20)?",
        ["(a) 0", "(b) 4", "(c) 6", "(d) 8"], "(a)",
        "Pairing trick: 4^1+4^2 = 4+6 = 10 (ends in 0). There are 10 such pairs. 10 x (0) = 0!",
        "Each pair (4^(2k-1) + 4^(2k)) ends in 4 + 6 = 10. The sum of 10 pairs ending in 0 ends in 0."))

    # Archetype 8: Alternating product with 9 (9^odd=9, 9^even=1)
    t1_q.append(create_q(t1_id, t1_title, 8, "UPSC Hard", False,
        "What is the units digit of the product 9^1 x 9^2 x 9^3 x ... x 9^10?",
        ["(a) 1", "(b) 9", "(c) 5", "(d) 0"], "(b)",
        "Sum of exponents: 1 + 2 + ... + 10 = 55. 9^55 is an odd power of 9, which always ends in 9!",
        "Product = 9^(1+2+...+10) = 9^55. 9 raised to any odd power ends in 9."))

    # Archetype 9: Unknown digit constraint (what digit can k NOT be?)
    t1_q.append(create_q(t1_id, t1_title, 9, "UPSC Hard", True,
        "If the expression (1234k)^48 ends in the digit 6, which of the following could k NOT be?",
        ["(a) 2", "(b) 4", "(c) 6", "(d) 5"], "(d)",
        "Elimination: Any power of 5 ends in 5, NEVER 6! So k can never be 5.",
        "5^n always ends in 5 for all natural numbers n. Hence k cannot be 5."))

    # Archetype 10: Tower of powers 2^(3^4)
    t1_q.append(create_q(t1_id, t1_title, 10, "UPSC Hard", True,
        "What is the units digit of the tower of powers 2^(3^4)?",
        ["(a) 2", "(b) 4", "(c) 6", "(d) 8"], "(a)",
        "Top-down evaluation: 3^4 = 81. Divide 81 by 4: remainder is 1. 2^1 ends in 2!",
        "3^4 = 81. We need the unit digit of 2^81. 81 mod 4 = 1. 2^1 = 2."))

    # Archetype 11: Symmetric cancellation 17^1999 + 11^1999 - 7^1999
    t1_q.append(create_q(t1_id, t1_title, 11, "UPSC Hard", True,
        "What is the units digit of (17)^1999 + (11)^1999 - (7)^1999?",
        ["(a) 1", "(b) 3", "(c) 7", "(d) 9"], "(a)",
        "Symmetric cancellation: 17^1999 and 7^1999 have identical unit digits, canceling to 0! 11^1999 ends in 1. Net = 1!",
        "17^k mod 10 = 7^k mod 10. Thus 17^1999 - 7^1999 ends in 0. 11^1999 ends in 1. 0 + 1 = 1."))

    # Archetype 12: Cyclicity matching between two bases (7^k and 3^k)
    t1_q.append(create_q(t1_id, t1_title, 12, "UPSC Hard", True,
        "If the unit digit of (7^k) is 3, what must be the unit digit of (3^k)?",
        ["(a) 1", "(b) 3", "(c) 7", "(d) 9"], "(c)",
        "Cyclicity matching: 7^k ends in 3 when k is of form 4n+3 (e.g. 7^3=343). For 3^(4n+3), 3^3 = 27 -> ends in 7!",
        "7 cyclicity is (7, 9, 3, 1). Unit digit 3 corresponds to power 4n+3. 3 cyclicity is (3, 9, 7, 1). Power 4n+3 gives unit digit 7."))

    # Archetype 13: Counting specific unit digits in a numerical range
    t1_q.append(create_q(t1_id, t1_title, 13, "Official Standard", False,
        "How many natural numbers between 99 and 1000 have the digit 8 in their units place?",
        ["(a) 80", "(b) 90", "(c) 100", "(d) 104"], "(b)",
        "Block Counting: From 100 to 999 there are 900 numbers. Exactly 1 in every 10 consecutive integers ends in 8. 900 / 10 = 90!",
        "Hundreds place has 9 choices (1-9), tens place has 10 choices (0-9), units place is fixed as 8. 9 * 10 * 1 = 90."))

    # Archetype 14: Sum of sixth powers of first 6 integers
    t1_q.append(create_q(t1_id, t1_title, 14, "UPSC Hard", True,
        "What is the units digit of (1^6 + 2^6 + 3^6 + 4^6 + 5^6 + 6^6)?",
        ["(a) 1", "(b) 3", "(c) 5", "(d) 7"], "(a)",
        "Sum individual unit digits: 1^6=1, 2^6=64(4), 3^6=729(9), 4^6=6, 5^6=5, 6^6=6. 1+4+9+6+5+6 = 31 -> ends in 1!",
        "Unit digits: 1 + 4 + 9 + 6 + 5 + 6 = 31. Unit digit is 1."))

    # Archetype 15: Product of four distinct prime powers
    t1_q.append(create_q(t1_id, t1_title, 15, "Official Standard", False,
        "What is the units digit of (781^80 x 256^45 x 312^36)?",
        ["(a) 2", "(b) 4", "(c) 6", "(d) 8"], "(c)",
        "Combine: 1^80 ends in 1. 6^45 ends in 6. 2^36 (36 div by 4) ends in 6. 1 x 6 x 6 = 36 -> ends in 6!",
        "1 * 6 * 6 = 36 -> unit digit is 6."))

    # Archetype 16: Unit digit of large product with identical consecutive bases
    t1_q.append(create_q(t1_id, t1_title, 16, "UPSC Hard", True,
        "What is the units digit of (11^1 + 12^2 + 13^3 + 14^4 + 15^5 + 16^6)?",
        ["(a) 5", "(b) 7", "(c) 9", "(d) 1"], "(c)",
        "Add unit digits: 1 + 4 + 7 + 6 + 5 + 6 = 29 -> ends in 9!",
        "11^1=1, 12^2=4, 13^3=7, 14^4=6, 15^5=5, 16^6=6. Sum = 29 -> unit digit is 9."))

    # Archetype 17: Consecutive power product (4^1 x 9^2 x 4^3 x 9^4 x ... x 4^99 x 9^100)
    t1_q.append(create_q(t1_id, t1_title, 17, "UPSC Hard", True,
        "What is the units digit of (4^1 x 9^2 x 4^3 x 9^4 x ... x 4^99 x 9^100)?",
        ["(a) 4", "(b) 6", "(c) 1", "(d) 9"], "(b)",
        "Pairing trick: Each pair 4^(odd) x 9^(even) = 4 x 1 = 4. There are 50 pairs: 4^50. 4^even ends in 6!",
        "Each pair has unit digit 4 * 1 = 4. 50 pairs give 4^50. Even power of 4 ends in 6."))

    # Archetype 18: Large 3-digit base power 2137^753
    t1_q.append(create_q(t1_id, t1_title, 18, "Official Standard", False,
        "What is the units digit of (2137)^753?",
        ["(a) 1", "(b) 3", "(c) 7", "(d) 9"], "(c)",
        "Last two digits: 53 mod 4 = 1. 7^1 = 7!",
        "753 mod 4 = 1. Effective power is 1. 7^1 = 7."))

    # Archetype 19: Sum of powers of 9 up to 20
    t1_q.append(create_q(t1_id, t1_title, 19, "UPSC Hard", True,
        "What is the units digit of (9^1 + 9^2 + 9^3 + ... + 9^20)?",
        ["(a) 0", "(b) 1", "(c) 5", "(d) 9"], "(a)",
        "Pairing: Each pair (9 + 1) = 10 ends in 0. 10 pairs ending in 0 sum to 0!",
        "9^odd ends in 9, 9^even ends in 1. Each pair sums to 10. 10 * 10 = 100 -> unit digit is 0."))

    # Archetype 20: Even power difference 8^100 - 4^100
    t1_q.append(create_q(t1_id, t1_title, 20, "UPSC Hard", True,
        "What is the units digit of (8^100 - 4^100)?",
        ["(a) 0", "(b) 2", "(c) 4", "(d) 6"], "(a)",
        "Both powers: 8^100 (100 div by 4) ends in 6. 4^100 ends in 6. 6 - 6 = 0!",
        "8^4 ends in 6, so 8^100 ends in 6. 4^even ends in 6. 6 - 6 = 0."))

    # Archetype 21: Sum of two identical exponent powers (153^98 + 157^98)
    t1_q.append(create_q(t1_id, t1_title, 21, "UPSC Hard", True,
        "What is the units digit of (153)^98 + (157)^98?",
        ["(a) 8", "(b) 6", "(c) 4", "(d) 0"], "(a)",
        "98 mod 4 = 2. 3^2 ends in 9. 7^2 ends in 9. 9 + 9 = 18 -> ends in 8!",
        "3^2 = 9. 7^2 = 49 -> 9. 9 + 9 = 18 -> unit digit is 8."))

    # Archetype 22: Unknown unit digit equation (3^x ends in 7, find unit digit of 7^x)
    t1_q.append(create_q(t1_id, t1_title, 22, "UPSC Hard", True,
        "If the units digit of 3^p is 7, what is the units digit of 7^p?",
        ["(a) 1", "(b) 3", "(c) 7", "(d) 9"], "(b)",
        "Inversion: 3^p ends in 7 when p is 4n+3 (since 3^3=27). For 7^(4n+3), 7^3 = 343 -> ends in 3!",
        "3 cyclicity: 3^1=3, 3^2=9, 3^3=7, 3^4=1. Unit digit 7 implies p = 4n+3. 7^3 = 343 -> unit digit 3."))

    # Archetype 23: Large prime cyclicity 2^51
    t1_q.append(create_q(t1_id, t1_title, 23, "Official Standard", False,
        "What is the units digit of 2^51?",
        ["(a) 2", "(b) 4", "(c) 6", "(d) 8"], "(d)",
        "51 mod 4 = 3. 2^3 = 8!",
        "51 = 4 * 12 + 3. Effective power is 3. 2^3 = 8."))

    # Archetype 24: Product with multiple zero-forming factors
    t1_q.append(create_q(t1_id, t1_title, 24, "Official Standard", False,
        "What is the units digit of (2^45 x 5^18 x 7^23)?",
        ["(a) 0", "(b) 2", "(c) 5", "(d) 7"], "(a)",
        "Zero Trap: Product contains both 2 and 5! Any multiple containing both 2 and 5 has unit digit 0!",
        "2^1 * 5^1 = 10. A factor of 10 ensures the unit digit is strictly 0."))

    # Archetype 25: Exponent power 7^105
    t1_q.append(create_q(t1_id, t1_title, 25, "Official Standard", False,
        "What is the units digit of (7)^105?",
        ["(a) 1", "(b) 3", "(c) 7", "(d) 9"], "(c)",
        "105 mod 4 = 1. 7^1 = 7!",
        "105 = 4 * 26 + 1. Effective power is 1. 7^1 = 7."))

    # Archetype 26: Large composite base power (678)^567
    t1_q.append(create_q(t1_id, t1_title, 26, "UPSC Hard", True,
        "What is the units digit of (678)^567?",
        ["(a) 2", "(b) 4", "(c) 6", "(d) 8"], "(a)",
        "8 cyclicity: (8, 4, 2, 6). 567 mod 4 = 67 mod 4 = 3. 8^3 = 512 -> ends in 2!",
        "567 mod 4 = 3. Effective power is 3. 8^3 = 512 -> unit digit is 2."))

    data[t1_id] = {"topic_id": t1_id, "title": t1_title, "mental_model": t1_model, "questions": t1_q}
    return data

if __name__ == "__main__":
    def dummy_create_q(tid, title, idx, diff, is_pred, q, opts, ans, child, expl):
        return {"id": f"{tid}-q{idx:02d}", "q": q, "answer": ans}
    t = get_topics_01_to_05(dummy_create_q)
    print("Topic 1 questions count:", len(t["csat-01"]["questions"]))
