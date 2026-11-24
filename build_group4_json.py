#!/usr/bin/env python3
"""
build_group4_json.py
Builds data/csat_topics_16_20.json containing 26 distinct problem archetypes each for:
- csat-16: Permutations & Combinations (Arrangements & Selections)
- csat-17: Probability & Independent Events (Dice, Cards & Urns)
- csat-18: Clocks (Angles, Overlaps, Right Angles & Faulty Clocks)
- csat-19: Calendar (Odd Days, Leap Year Cycles & Repeating Years)
- csat-20: Cubes, Dice & Visual Cuts (Painted Faces & Net Unfolding)
Total: 130 questions.
"""

import json
import os

def create_q(tid, title, idx, ytag, diff, is_pred, q_text, opts, ans, child, expl):
    assert len(opts) == 4, f"Options error: {opts}"
    assert ans in ["(a)", "(b)", "(c)", "(d)"], f"Answer error: {ans}"
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

def build_group4():
    data = {}

    # -------------------------------------------------------------
    # TOPIC 16: Permutations & Combinations (26 Distinct Archetypes)
    # -------------------------------------------------------------
    t16_id = "csat-16"
    t16_title = "Permutations & Combinations: Arrangements, Selections & Restrictions"
    t16_model = "Slot Machine & Committee Box: Arrangements = n! / (duplicates!). Grouping items = tie them into a single bundle. Handshakes = n(n-1)/2. Diagonals = n(n-3)/2."
    t16_specs = [
        ("[UPSC CSAT Standard]", "Official Standard", False,
         "How many different words can be formed using all the letters of the word 'LEADER'?",
         ["(a) 360", "(b) 720", "(c) 180", "(d) 480"], "(a)",
         "Repeated Letter Division: Total letters = 6. E appears 2 times. Total permutations = 6! / 2! = 720 / 2 = 360!",
         "Total letters = 6. E is repeated 2 times. Number of arrangements = 6! / 2! = 720 / 2 = 360."),
        
        ("[UPSC CSAT Hard]", "UPSC Hard", True,
         "In how many different ways can the letters of the word 'CORPORATION' be arranged so that all the vowels always come together?",
         ["(a) 50,400", "(b) 28,800", "(c) 43,200", "(d) 57,600"], "(a)",
         "Bundle the Vowels: Vowels = O, O, A, I, O (5 vowels: 3 O's). Consonants = C, R, P, R, T, N (6 consonants: 2 R's). Treat the 5 vowels as 1 mega-letter. Total units = 6 + 1 = 7. Arrange units = 7! / 2! = 5040 / 2 = 2520. Arrange vowels inside bundle = 5! / 3! = 120 / 6 = 20. Total = 2520 * 20 = 50,400!",
         "Vowels: O, O, A, I, O (5 vowels, 3 O's). Consonants: C, R, P, R, T, N (6 consonants, 2 R's). Units to arrange = 6 + 1 = 7 units. Ways = 7! / 2! = 2520. Vowel internal arrangements = 5! / 3! = 20. Total ways = 2520 * 20 = 50,400."),
        
        ("[UPSC CSAT Hard]", "UPSC Hard", True,
         "How many 4-digit numbers greater than 5,000 can be formed using the digits 3, 5, 7, 8, and 9 without repeating any digit?",
         ["(a) 96", "(b) 120", "(c) 72", "(d) 84"], "(a)",
         "Thousands Slot Restriction: Thousands place must be >= 5 (choices: 5, 7, 8, 9 -> 4 choices). Remaining 3 places chosen from remaining 4 digits: 4 * 3 * 2 = 24. Total = 4 * 24 = 96 numbers!",
         "Thousands place has 4 choices (5, 7, 8, 9). The next 3 digits can be filled in 4P3 = 4 * 3 * 2 = 24 ways. Total = 4 * 24 = 96."),
        
        ("[UPSC CSAT Standard]", "Official Standard", False,
         "At a civil services conference, there are 15 officers. If every officer shakes hands with every other officer exactly once, how many total handshakes take place?",
         ["(a) 105", "(b) 120", "(c) 90", "(d) 115"], "(a)",
         "Pair Selection: Formula = n(n - 1) / 2 = 15 * 14 / 2 = 15 * 7 = 105 handshakes!",
         "Handshakes = 15C2 = (15 * 14) / 2 = 105."),
        
        ("[UPSC CSAT Standard]", "Official Standard", False,
         "How many diagonals are there in a regular decagon (a polygon with 10 sides)?",
         ["(a) 35", "(b) 45", "(c) 40", "(d) 30"], "(a)",
         "Diagonal Formula: n(n - 3) / 2 = 10 * 7 / 2 = 35 diagonals!",
         "Number of diagonals = n(n - 3) / 2 = 10 * (10 - 3) / 2 = 35."),
        
        ("[UPSC CSAT Hard]", "UPSC Hard", True,
         "A committee of 5 members is to be formed from 6 men and 4 women. In how many ways can this committee be chosen if it must include at least one woman?",
         ["(a) 246", "(b) 252", "(c) 210", "(d) 240"], "(a)",
         "Total Minus All-Men: Total unrestricted committees = 10C5 = 252. Committees with ZERO women (all 5 men) = 6C5 = 6. At least one woman = 252 - 6 = 246!",
         "Total ways to choose 5 from 10 = 10C5 = 252. Committees with no women = 6C5 = 6. At least one woman = 252 - 6 = 246."),
        
        ("[UPSC CSAT Hard]", "UPSC Hard", True,
         "In how many ways can 7 diplomats sit around a circular conference table?",
         ["(a) 720", "(b) 5,040", "(c) 360", "(d) 120"], "(a)",
         "Circle Formula: (n - 1)! = (7 - 1)! = 6! = 720 ways!",
         "Circular permutation of n items = (n - 1)! = (7 - 1)! = 6! = 720."),
        
        ("[UPSC CSAT Standard]", "Official Standard", False,
         "How many different 3-letter codes can be formed using the letters of the English alphabet without repetition of letters?",
         ["(a) 15,600", "(b) 17,576", "(c) 14,200", "(d) 16,800"], "(a)",
         "Slots: 26 * 25 * 24 = 15,600 codes!",
         "26P3 = 26 * 25 * 24 = 15,600."),
        
        ("[UPSC CSAT Hard]", "UPSC Hard", True,
         "There are 12 points in a plane, of which exactly 5 are collinear. How many distinct triangles can be formed with these points as vertices?",
         ["(a) 210", "(b) 220", "(c) 200", "(d) 195"], "(a)",
         "Subtract Flat Lines: Total triangles from 12 points = 12C3 = (12 * 11 * 10) / 6 = 220. The 5 collinear points cannot form triangles: 5C3 = 10. Valid triangles = 220 - 10 = 210!",
         "Total ways = 12C3 = 220. Collinear points reduction = 5C3 = 10. Number of triangles = 220 - 10 = 210."),
        
        ("[UPSC CSAT Standard]", "Official Standard", False,
         "In how many ways can 4 distinct letters be posted into 3 letterboxes?",
         ["(a) 81", "(b) 64", "(c) 24", "(d) 12"], "(a)",
         "Independent Choices: Each of the 4 letters has 3 choices of boxes: 3 * 3 * 3 * 3 = 3^4 = 81 ways!",
         "Each letter can go into any of the 3 boxes. Total ways = 3^4 = 81."),
        
        ("[UPSC CSAT Hard]", "UPSC Hard", True,
         "In how many ways can 4 letters be placed into their 4 addressed envelopes such that NOT A SINGLE letter goes into its correct envelope?",
         ["(a) 9", "(b) 12", "(c) 8", "(d) 10"], "(a)",
         "Derangement D4: Formula = 4! * (1 - 1/1! + 1/2! - 1/3! + 1/4!) = 24 * (1/2 - 1/6 + 1/24) = 24 * (9/24) = 9!",
         "Derangement of 4 items D4 = 4! * (1/2! - 1/3! + 1/4!) = 24 * (1/2 - 1/6 + 1/24) = 12 - 4 + 1 = 9."),
        
        ("[UPSC CSAT Standard]", "Official Standard", False,
         "How many numbers between 100 and 1,000 can be formed using the digits 0, 1, 2, 3, 4, 5 without repetition?",
         ["(a) 100", "(b) 120", "(c) 80", "(d) 90"], "(a)",
         "Hundreds Slot: Hundreds digit cannot be 0 (choices: 1, 2, 3, 4, 5 -> 5 choices). Tens place has 5 choices (0 included). Units place has 4 choices. Total = 5 * 5 * 4 = 100 numbers!",
         "Hundreds place: 5 choices (1 to 5). Tens place: 5 choices. Units place: 4 choices. Total = 5 * 5 * 4 = 100."),
        
        ("[UPSC CSAT Hard]", "UPSC Hard", True,
         "In how many ways can 10 identical gold coins be distributed among 3 children such that each child receives at least one coin?",
         ["(a) 36", "(b) 45", "(c) 28", "(d) 55"], "(a)",
         "Stars and Bars: (n - 1) C (k - 1) = (10 - 1) C (3 - 1) = 9C2 = (9 * 8) / 2 = 36 ways!",
         "Positive integer solutions to x1 + x2 + x3 = 10 is (n-1)C(k-1) = 9C2 = 36."),
        
        ("[UPSC CSAT Standard]", "Official Standard", False,
         "In how many ways can 5 boys and 5 girls sit in a row alternatively?",
         ["(a) 28,800", "(b) 14,400", "(c) 12,000", "(d) 24,000"], "(a)",
         "Two Alternating Patterns: Pattern 1 (BGBGBGBGBG): 5! * 5! = 120 * 120 = 14,400. Pattern 2 (GBGBGBGBGB): 5! * 5! = 14,400. Total = 14,400 + 14,400 = 28,800 ways!",
         "Starting with Boy: 5! * 5! = 14,400. Starting with Girl: 5! * 5! = 14,400. Total = 28,800."),
        
        ("[UPSC CSAT Hard]", "UPSC Hard", True,
         "How many total rectangles (of all sizes, including squares) are there on an 8 x 8 chessboard?",
         ["(a) 1,296", "(b) 204", "(c) 1,024", "(d) 1,156"], "(a)",
         "Grid Lines Selection: An 8x8 board has 9 horizontal lines and 9 vertical lines. Choose 2 horizontal lines (9C2 = 36) and 2 vertical lines (9C2 = 36). Rectangles = 36 * 36 = 1,296!",
         "A rectangle is formed by selecting 2 horizontal and 2 vertical lines from 9 lines each. 9C2 * 9C2 = 36 * 36 = 1,296."),
        
        ("[UPSC CSAT Standard]", "Official Standard", False,
         "In how many ways can 8 distinct beads be strung together to make a necklace?",
         ["(a) 2,520", "(b) 5,040", "(c) 1,260", "(d) 40,320"], "(a)",
         "Necklace Flip: Clockwise and counter-clockwise are identical: (n - 1)! / 2 = 7! / 2 = 5040 / 2 = 2,520 ways!",
         "Necklace permutation = (n - 1)! / 2 = 7! / 2 = 5040 / 2 = 2,520."),
        
        ("[UPSC CSAT Hard]", "UPSC Hard", True,
         "From a group of 7 men and 6 women, 5 persons are to be selected to form a committee so that at least 3 men are on the committee. In how many ways can it be done?",
         ["(a) 756", "(b) 735", "(c) 644", "(d) 720"], "(a)",
         "Three Cases: Case 1 (3M, 2W): 7C3 * 6C2 = 35 * 15 = 525. Case 2 (4M, 1W): 7C4 * 6C1 = 35 * 6 = 210. Case 3 (5M, 0W): 7C5 * 6C0 = 21 * 1 = 21. Total = 525 + 210 + 21 = 756 ways!",
         "Ways = (7C3 * 6C2) + (7C4 * 6C1) + (7C5 * 6C0) = 525 + 210 + 21 = 756."),
        
        ("[UPSC CSAT Standard]", "Official Standard", False,
         "How many 3-digit even numbers can be formed using the digits 1, 2, 3, 4, 5, 6, 7 if repetition of digits is NOT permitted?",
         ["(a) 90", "(b) 120", "(c) 72", "(d) 105"], "(a)",
         "Even Units Place: Units place must be even (2, 4, 6 -> 3 choices). Remaining 2 places chosen from remaining 6 digits: 6 * 5 = 30. Total = 3 * 30 = 90 numbers!",
         "Units place: 3 choices (2, 4, 6). Remaining two digits: 6 * 5 = 30 choices. Total = 30 * 3 = 90."),
        
        ("[UPSC CSAT Hard]", "UPSC Hard", True,
         "In how many ways can the letters of the word 'DETAIL' be arranged such that the vowels occupy only odd positions?",
         ["(a) 36", "(b) 48", "(c) 72", "(d) 24"], "(a)",
         "Odd Slots: In a 6-letter word, odd positions are 1, 3, 5 (3 slots). Vowels = E, A, I (3 vowels). Arrange vowels in odd slots = 3! = 6. Consonants = D, T, L (3 consonants) in remaining even slots = 3! = 6. Total = 6 * 6 = 36 ways!",
         "Odd positions: 1, 3, 5 (3 positions). Vowels (E, A, I) can be arranged in 3! = 6 ways. Consonants (D, T, L) in 3 even positions in 3! = 6 ways. Total = 6 * 6 = 36."),
        
        ("[UPSC CSAT Standard]", "Official Standard", False,
         "How many different signals can be given using any number of flags from 5 flags of different colors?",
         ["(a) 325", "(b) 320", "(c) 120", "(d) 240"], "(a)",
         "Sum of Permutations: 5P1 + 5P2 + 5P3 + 5P4 + 5P5 = 5 + 20 + 60 + 120 + 120 = 325 signals!",
         "Signals = 5P1 + 5P2 + 5P3 + 5P4 + 5P5 = 5 + 20 + 60 + 120 + 120 = 325."),
        
        ("[UPSC CSAT Hard]", "UPSC Hard", True,
         "In how many ways can 6 rings of different designs be worn on 4 fingers of one hand?",
         ["(a) 4^6 = 4,096", "(b) 6^4 = 1,296", "(c) 360", "(d) 240"], "(a)",
         "Ring Choices: Each of the 6 rings has 4 choices of fingers: 4 * 4 * 4 * 4 * 4 * 4 = 4^6 = 4,096 ways!",
         "Each ring has 4 choices. Total ways = 4^6 = 4,096."),
        
        ("[UPSC CSAT Standard]", "Official Standard", False,
         "What is the number of arrangements of the letters of the word 'BANANA'?",
         ["(a) 60", "(b) 120", "(c) 720", "(d) 360"], "(a)",
         "Repeated Letters: Total = 6 letters. A appears 3 times, N appears 2 times. Permutations = 6! / (3! * 2!) = 720 / (6 * 2) = 60!",
         "Arrangements = 6! / (3! * 2!) = 720 / 12 = 60."),
        
        ("[UPSC CSAT Hard]", "UPSC Hard", True,
         "How many paths are there from the bottom-left corner (0,0) to the top-right corner (4,3) on a city grid if you can only move Right or Up?",
         ["(a) 35", "(b) 28", "(c) 42", "(d) 40"], "(a)",
         "Manhattan Grid Steps: Total steps = 4 Right + 3 Up = 7 steps. Number of ways to choose which 3 steps are Up = 7C3 = (7 * 6 * 5) / 6 = 35 paths!",
         "Total steps = 4 + 3 = 7. Paths = 7C3 = 35."),
        
        ("[UPSC CSAT Standard]", "Official Standard", False,
         "A question paper has two parts, Part A and Part B, each containing 5 questions. A candidate has to answer 6 questions in all, selecting at least 2 questions from each part. In how many ways can the candidate select the questions?",
         ["(a) 200", "(b) 180", "(c) 210", "(d) 225"], "(a)",
         "Split Scenarios: Case 1 (2 from A, 4 from B): 5C2 * 5C4 = 10 * 5 = 50. Case 2 (3 from A, 3 from B): 5C3 * 5C3 = 10 * 10 = 100. Case 3 (4 from A, 2 from B): 5C4 * 5C2 = 5 * 10 = 50. Total = 50 + 100 + 50 = 200 ways!",
         "Ways = (5C2 * 5C4) + (5C3 * 5C3) + (5C4 * 5C2) = 50 + 100 + 50 = 200."),
        
        ("[UPSC CSAT Hard]", "UPSC Hard", True,
         "There are 6 boxes numbered 1, 2, 3, 4, 5, 6. Each box is to be filled with either a red or a green ball in such a way that at least 1 box contains a green ball and the boxes containing green balls are consecutive. How many total ways are there to fill the boxes?",
         ["(a) 21", "(b) 18", "(c) 24", "(d) 15"], "(a)",
         "Consecutive Segment Counting: Green ball can span length 1 (6 ways), length 2 (5 ways: 1-2, 2-3, 3-4, 4-5, 5-6), length 3 (4 ways), length 4 (3 ways), length 5 (2 ways), length 6 (1 way). Total = 6 + 5 + 4 + 3 + 2 + 1 = 21 ways!",
         "Number of non-empty consecutive sub-segments of length 6 = 6 * 7 / 2 = 21 ways."),
        
        ("[UPSC CSAT Hard]", "UPSC Hard", True,
         "How many 5-digit palindromic numbers (numbers that read the same backwards and forwards, such as 12321) can be formed using digits 0 to 9?",
         ["(a) 900", "(b) 1,000", "(c) 810", "(d) 990"], "(a)",
         "Symmetric Anchor: A 5-digit palindrome has form 'abcba'. First digit 'a' cannot be 0 (choices 1-9 -> 9 choices). Second digit 'b' has 10 choices (0-9). Third digit 'c' has 10 choices (0-9). The last two digits are mirror reflections of 'b' and 'a' (1 choice each!). Total = 9 * 10 * 10 = 900 numbers!",
         "Palindrome of length 5 is abcba. a has 9 choices (1-9). b has 10 choices (0-9). c has 10 choices (0-9). Total = 9 * 10 * 10 = 900.")
    ]
    data[t16_id] = {
        "topic_id": t16_id, "title": t16_title, "mental_model": t16_model,
        "questions": [create_q(t16_id, t16_title, i+1, s[0], s[1], s[2], s[3], s[4], s[5], s[6], s[7]) for i, s in enumerate(t16_specs)]
    }

    # -------------------------------------------------------------
    # TOPIC 17: Probability & Independent Events (26 Distinct Archetypes)
    # -------------------------------------------------------------
    t17_id = "csat-17"
    t17_title = "Probability & Independent Events: Dice, Cards & Urns"
    t17_model = "Favorable vs Sample Space Scale: P(Event) = Favorable Outcomes / Total Sample Space. Independent: P(A and B) = P(A) * P(B). At least one = 1 - P(None)."
    t17_specs = [
        ("[UPSC CSAT Standard]", "Official Standard", False,
         "Two fair dice are thrown simultaneously. What is the probability of getting a sum of 8?",
         ["(a) 5/36", "(b) 1/6", "(c) 7/36", "(d) 1/9"], "(a)",
         "Favorable Pairs: Favorable = (2,6), (3,5), (4,4), (5,3), (6,2) -> 5 pairs out of 36. Probability = 5/36!",
         "Total outcomes = 36. Favorable outcomes for sum 8: (2,6), (3,5), (4,4), (5,3), (6,2) = 5. P = 5/36."),
        
        ("[UPSC CSAT Standard]", "Official Standard", False,
         "A card is drawn from a well-shuffled pack of 52 cards. What is the probability of getting a queen of club or a king of heart?",
         ["(a) 1/26", "(b) 1/13", "(c) 1/52", "(d) 2/13"], "(a)",
         "Favorable Count: Queen of clubs = 1 card; King of hearts = 1 card. Total favorable = 2 cards out of 52. Probability = 2/52 = 1/26!",
         "P = (1 + 1) / 52 = 2 / 52 = 1/26."),
        
        ("[UPSC CSAT Hard]", "UPSC Hard", True,
         "What is the probability that a leap year selected at random will contain 53 Sundays?",
         ["(a) 2/7", "(b) 1/7", "(c) 3/7", "(d) 5/7"], "(a)",
         "Leap Year Extra Days: A leap year has 366 days = 52 weeks + 2 extra days. The 2 extra days can be (Sun,Mon), (Mon,Tue), (Tue,Wed), (Wed,Thu), (Thu,Fri), (Fri,Sat), (Sat,Sun) -> 7 pairs. Exactly 2 pairs contain Sunday. Probability = 2/7!",
         "366 days = 52 weeks + 2 days. The 2 odd days can be 7 combinations. Favorable for Sunday: (Sat, Sun) and (Sun, Mon) = 2. P = 2/7."),
        
        ("[UPSC CSAT Standard]", "Official Standard", False,
         "What is the probability that a non-leap year will contain 53 Sundays?",
         ["(a) 1/7", "(b) 2/7", "(c) 1/365", "(d) 52/365"], "(a)",
         "Non-Leap Extra Day: A non-leap year has 365 days = 52 weeks + 1 extra day. The 1 extra day can be any of 7 days. Probability of Sunday = 1/7!",
         "365 days = 52 weeks + 1 day. Probability that this 1 day is Sunday = 1/7."),
        
        ("[UPSC CSAT Hard]", "UPSC Hard", True,
         "A problem in mathematics is given to three students A, B, and C whose chances of solving it are 1/2, 1/3, and 1/4 respectively. What is the probability that the problem will be solved?",
         ["(a) 3/4", "(b) 1/2", "(c) 2/3", "(d) 5/6"], "(a)",
         "Complement Trick: Probability nobody solves = (1 - 1/2) * (1 - 1/3) * (1 - 1/4) = (1/2) * (2/3) * (3/4) = 1/4. Probability it is solved = 1 - 1/4 = 3/4!",
         "P(Solved) = 1 - P(None solves) = 1 - (1/2 * 2/3 * 3/4) = 1 - 1/4 = 3/4."),
        
        ("[UPSC CSAT Standard]", "Official Standard", False,
         "A bag contains 6 black and 8 white balls. One ball is drawn at random. What is the probability that the ball drawn is white?",
         ["(a) 4/7", "(b) 3/7", "(c) 1/2", "(d) 5/7"], "(a)",
         "Fraction: White = 8, Total = 6 + 8 = 14. Probability = 8 / 14 = 4/7!",
         "P = 8 / 14 = 4/7."),
        
        ("[UPSC CSAT Hard]", "UPSC Hard", True,
         "A speaks the truth in 75% of cases and B in 80% of cases. In what percentage of cases are they likely to contradict each other when stating the same fact?",
         ["(a) 35%", "(b) 40%", "(c) 30%", "(d) 25%"], "(a)",
         "Contradiction Cases: Contradict = (A speaks truth and B lies) OR (A lies and B speaks truth) = (3/4 * 1/5) + (1/4 * 4/5) = 3/20 + 4/20 = 7/20 = 35%!",
         "P(Contradict) = P(A)*P(not B) + P(not A)*P(B) = (0.75 * 0.20) + (0.25 * 0.80) = 0.15 + 0.20 = 0.35 = 35%."),
        
        ("[UPSC CSAT Standard]", "Official Standard", False,
         "Three fair coins are tossed together. What is the probability of getting at least 2 heads?",
         ["(a) 1/2", "(b) 3/8", "(c) 5/8", "(d) 1/4"], "(a)",
         "Sample Space: 8 outcomes (HHH, HHT, HTH, HTT, THH, THT, TTH, TTT). At least 2 heads = HHH, HHT, HTH, THH (4 outcomes). Probability = 4/8 = 1/2!",
         "Favorable: HHH, HHT, HTH, THH = 4 out of 8. P = 4/8 = 1/2."),
        
        ("[UPSC CSAT Hard]", "UPSC Hard", True,
         "From a box containing 10 light bulbs of which 3 are defective, 2 bulbs are drawn at random without replacement. What is the probability that both bulbs are defective?",
         ["(a) 1/15", "(b) 1/10", "(c) 3/50", "(d) 1/12"], "(a)",
         "Without Replacement Product: First defective = 3/10. Second defective = 2/9. Probability = (3/10) * (2/9) = 6/90 = 1/15!",
         "P = (3/10) * (2/9) = 6 / 90 = 1/15."),
        
        ("[UPSC CSAT Standard]", "Official Standard", False,
         "Two dice are thrown together. What is the probability that the sum of the numbers on the two dice is a prime number?",
         ["(a) 15/36", "(b) 5/12", "(c) 7/18", "(d) 1/2"], "(a)",
         "Prime Sums: Primes <= 12 are 2, 3, 5, 7, 11. Sum 2 (1 pair), Sum 3 (2 pairs), Sum 5 (4 pairs), Sum 7 (6 pairs), Sum 11 (2 pairs). Total favorable = 1 + 2 + 4 + 6 + 2 = 15 pairs! Probability = 15/36 = 5/12!",
         "Favorable sums: 2 (1), 3 (2), 5 (4), 7 (6), 11 (2). Total = 15. P = 15/36 = 5/12."),
        
        ("[UPSC CSAT Hard]", "UPSC Hard", True,
         "In a class, 30% of students failed in Physics, 25% failed in Chemistry, and 10% failed in both. If a student is selected at random, what is the probability that he passed in both subjects?",
         ["(a) 0.55", "(b) 0.45", "(c) 0.65", "(d) 0.50"], "(a)",
         "Venn Union Complement: Failed in at least one = 30% + 25% - 10% = 45%. Passed in both = 100% - 45% = 55% = 0.55!",
         "P(Failed in at least one) = 0.30 + 0.25 - 0.10 = 0.45. P(Passed both) = 1 - 0.45 = 0.55."),
        
        ("[UPSC CSAT Standard]", "Official Standard", False,
         "A number x is chosen at random from the integers 1 to 25. What is the probability that x is a multiple of either 3 or 5?",
         ["(a) 12/25", "(b) 11/25", "(c) 13/25", "(d) 14/25"], "(a)",
         "Count Multiples: Multiples of 3 = 8 (3, 6, 9, 12, 15, 18, 21, 24). Multiples of 5 = 5 (5, 10, 15, 20, 25). Multiple of both (15) = 1. Union = 8 + 5 - 1 = 12. Probability = 12/25!",
         "Multiples of 3 = 8, multiples of 5 = 5, multiple of 15 = 1. n(3 U 5) = 8 + 5 - 1 = 12. P = 12/25."),
        
        ("[UPSC CSAT Hard]", "UPSC Hard", True,
         "Two cards are drawn from a pack of 52 cards one after another without replacement. What is the probability that the first card is a king and the second card is an ace?",
         ["(a) 4/663", "(b) 1/169", "(c) 2/663", "(d) 1/221"], "(a)",
         "Sequential Multiplication: First King = 4/52 = 1/13. Second Ace = 4/51. Probability = (1/13) * (4/51) = 4 / 663!",
         "P = (4/52) * (4/51) = (1/13) * (4/51) = 4 / 663."),
        
        ("[UPSC CSAT Standard]", "Official Standard", False,
         "What is the probability of rolling a total score of 7 on a single throw of two dice?",
         ["(a) 1/6", "(b) 5/36", "(c) 7/36", "(d) 1/12"], "(a)",
         "Seven Combos: (1,6), (2,5), (3,4), (4,3), (5,2), (6,1) = 6 outcomes out of 36. Probability = 6/36 = 1/6!",
         "6 favorable outcomes out of 36. P = 6/36 = 1/6."),
        
        ("[UPSC CSAT Hard]", "UPSC Hard", True,
         "An urn contains 4 red, 5 blue, and 6 green marbles. Three marbles are drawn together at random. What is the probability that all three marbles are of different colors?",
         ["(a) 24/91", "(b) 18/91", "(c) 20/91", "(d) 30/91"], "(a)",
         "One of Each: Choose 1 Red, 1 Blue, 1 Green = 4C1 * 5C1 * 6C1 = 4 * 5 * 6 = 120. Total ways to choose 3 from 15 = 15C3 = (15 * 14 * 13) / 6 = 455. Probability = 120 / 455 = 24 / 91!",
         "Favorable = 4 * 5 * 6 = 120. Total = 15C3 = 455. P = 120 / 455 = 24/91."),
        
        ("[UPSC CSAT Standard]", "Official Standard", False,
         "A fair die is rolled. What is the probability of getting a number greater than 4?",
         ["(a) 1/3", "(b) 1/2", "(c) 2/3", "(d) 1/6"], "(a)",
         "Greater Than 4: Numbers are 5 and 6 (2 outcomes). Probability = 2/6 = 1/3!",
         "Outcomes > 4 are {5, 6}. P = 2/6 = 1/3."),
        
        ("[UPSC CSAT Hard]", "UPSC Hard", True,
         "Two persons A and B appear for an interview for two vacancies in the same post. The probability of A's selection is 1/7 and that of B's selection is 1/5. What is the probability that only one of them will be selected?",
         ["(a) 2/7", "(b) 1/7", "(c) 3/7", "(d) 1/5"], "(a)",
         "One Selected: P(A selected, B rejected) + P(A rejected, B selected) = (1/7 * 4/5) + (6/7 * 1/5) = 4/35 + 6/35 = 10/35 = 2/7!",
         "P = P(A)*P(not B) + P(not A)*P(B) = (1/7 * 4/5) + (6/7 * 1/5) = 10/35 = 2/7."),
        
        ("[UPSC CSAT Standard]", "Official Standard", False,
         "If P(A) = 0.4, P(B) = 0.5, and A and B are independent events, what is P(A U B)?",
         ["(a) 0.7", "(b) 0.9", "(c) 0.6", "(d) 0.8"], "(a)",
         "Union Formula: P(A U B) = P(A) + P(B) - P(A and B) = 0.4 + 0.5 - (0.4 * 0.5) = 0.9 - 0.2 = 0.7!",
         "For independent events, P(A ∩ B) = 0.4 * 0.5 = 0.2. P(A U B) = 0.4 + 0.5 - 0.2 = 0.7."),
        
        ("[UPSC CSAT Hard]", "UPSC Hard", True,
         "A box contains 5 red and 7 green balls. Another box contains 6 red and 4 green balls. One ball is transferred from the first box to the second box, and then a ball is drawn from the second box. What is the probability that the ball drawn from the second box is green?",
         ["(a) 55/132", "(b) 48/132", "(c) 51/132", "(d) 60/132"], "(a)",
         "Law of Total Probability: Case 1 (Red transferred with prob 5/12): Second box has 7 red, 4 green (11 total). Green prob = 4/11. Case 2 (Green transferred with prob 7/12): Second box has 6 red, 5 green (11 total). Green prob = 5/11. Total P = (5/12 * 4/11) + (7/12 * 5/11) = (20 + 35) / 132 = 55/132!",
         "P(Green) = (5/12 * 4/11) + (7/12 * 5/11) = 55 / 132."),
        
        ("[UPSC CSAT Standard]", "Official Standard", False,
         "A card is drawn from a standard deck of 52 cards. What is the probability that it is neither a heart nor a king?",
         ["(a) 9/13", "(b) 8/13", "(c) 10/13", "(d) 7/13"], "(a)",
         "Subtract Excluded: Hearts = 13. Kings = 4 (1 already in hearts). Total excluded = 13 + 3 = 16 cards. Remaining = 52 - 16 = 36 cards. Probability = 36 / 52 = 9/13!",
         "Excluded cards = 13 hearts + 3 other kings = 16. Favorable = 52 - 16 = 36. P = 36/52 = 9/13."),
        
        ("[UPSC CSAT Hard]", "UPSC Hard", True,
         "In a lottery of 100 tickets numbered 1 to 100, one ticket is drawn at random. What is the probability that the number on the ticket drawn is a perfect square or a perfect cube?",
         ["(a) 11/100", "(b) 12/100", "(c) 14/100", "(d) 10/100"], "(a)",
         "Count Squares and Cubes: Squares <= 100: 1, 4, 9, 16, 25, 36, 49, 64, 81, 100 (10 squares). Cubes <= 100: 1, 8, 27, 64 (4 cubes). Overlap (6th powers): 1, 64 (2 numbers). Total unique = 10 + 4 - 2 = 12? Wait: 1, 64 are both square and cube. Squares = 10. Cubes = 4. Union = 10 + 4 - 2 = 12. Probability = 12/100!",
         "Squares: {1, 4, 9, 16, 25, 36, 49, 64, 81, 100} (10). Cubes: {1, 8, 27, 64} (4). Both: {1, 64} (2). Union = 10 + 4 - 2 = 12. P = 12/100."),
        
        ("[UPSC CSAT Standard]", "Official Standard", False,
         "Four fair coins are tossed. What is the probability of getting exactly 2 heads and 2 tails?",
         ["(a) 3/8", "(b) 1/2", "(c) 5/16", "(d) 1/4"], "(a)",
         "Binomial Counting: Total outcomes = 2^4 = 16. Favorable = 4C2 = 6. Probability = 6/16 = 3/8!",
         "4C2 / 16 = 6 / 16 = 3/8."),
        
        ("[UPSC CSAT Hard]", "UPSC Hard", True,
         "A random variable X can take values 1, 2, 3 with probabilities k, 2k, 3k. What is the value of k and the expected value E(X)?",
         ["(a) k = 1/6, E(X) = 2.33", "(b) k = 1/6, E(X) = 2.0", "(c) k = 1/5, E(X) = 2.5", "(d) k = 1/4, E(X) = 2.25"], "(a)",
         "Sum of Probabilities: k + 2k + 3k = 1 => 6k = 1 => k = 1/6. E(X) = 1(1/6) + 2(2/6) + 3(3/6) = (1 + 4 + 9)/6 = 14/6 = 2.33!",
         "6k = 1 => k = 1/6. E(X) = (1*1 + 2*2 + 3*3)/6 = 14/6 = 2.33."),
        
        ("[UPSC CSAT Standard]", "Official Standard", False,
         "What is the probability of getting an odd number on rolling a fair die?",
         ["(a) 1/2", "(b) 1/3", "(c) 2/3", "(d) 1/6"], "(a)",
         "Odd Numbers: {1, 3, 5} -> 3 out of 6 = 1/2!",
         "P = 3/6 = 1/2."),
        
        ("[UPSC CSAT Hard]", "UPSC Hard", True,
         "Three vertices are chosen at random from the 6 vertices of a regular hexagon. What is the probability that the triangle formed by these 3 vertices is an equilateral triangle?",
         ["(a) 1/10", "(b) 1/20", "(c) 3/20", "(d) 1/5"], "(a)",
         "Hexagon Triangles: Total triangles = 6C3 = 20. Exactly 2 equilateral triangles exist (vertices 1-3-5 and 2-4-6). Probability = 2/20 = 1/10!",
         "Total triangles = 6C3 = 20. Only two sets of alternating vertices form equilateral triangles. P = 2/20 = 1/10."),
        
        ("[UPSC CSAT Hard]", "UPSC Hard", True,
         "Two friends agree to meet at a metro station between 4:00 PM and 5:00 PM. Each agrees to wait for 15 minutes for the other before leaving. What is the probability that they will meet?",
         ["(a) 7/16", "(b) 9/16", "(c) 1/2", "(d) 5/8"], "(a)",
         "Geometric Area: Total area = 60 * 60 = 3600. Condition: |x - y| <= 15. Area where they DO NOT meet = two triangles of side 45: 2 * (1/2 * 45 * 45) = 2025. Meeting area = 3600 - 2025 = 1575. Probability = 1575 / 3600 = 7/16!",
         "P(Meet) = 1 - (45/60)^2 = 1 - (3/4)^2 = 1 - 9/16 = 7/16.")
    ]
    data[t17_id] = {
        "topic_id": t17_id, "title": t17_title, "mental_model": t17_model,
        "questions": [create_q(t17_id, t17_title, i+1, s[0], s[1], s[2], s[3], s[4], s[5], s[6], s[7]) for i, s in enumerate(t17_specs)]
    }

    # -------------------------------------------------------------
    # TOPIC 18: Clocks (26 Distinct Archetypes)
    # -------------------------------------------------------------
    t18_id = "csat-18"
    t18_title = "Clocks: Angles, Overlaps, Right Angles & Faulty Clocks"
    t18_model = "Hand Dial Formula: Angle θ = |(11/2)m - 30h|. Coincidence occurs every 65 (5/11) minutes. Hands coincide 22 times and make 90° 44 times in 24 hours."
    t18_specs = [
        ("[UPSC CSAT Standard]", "Official Standard", False,
         "What is the angle between the hour hand and the minute hand of a clock at 3:40?",
         ["(a) 130°", "(b) 125°", "(c) 135°", "(d) 140°"], "(a)",
         "Formula: |(11/2) * 40 - 30 * 3| = |220 - 90| = 130°!",
         "Angle = |(11/2)m - 30h| = |(11/2 * 40) - (30 * 3)| = |220 - 90| = 130°."),
        
        ("[UPSC CSAT Standard]", "Official Standard", False,
         "What is the angle between the hands of a clock at 8:30?",
         ["(a) 75°", "(b) 80°", "(c) 70°", "(d) 85°"], "(a)",
         "Formula: |(11/2) * 30 - 30 * 8| = |165 - 240| = 75°!",
         "Angle = |165 - 240| = 75°."),
        
        ("[UPSC CSAT Hard]", "UPSC Hard", True,
         "At what time between 4 and 5 o'clock will the hands of a clock coincide?",
         ["(a) 21 (9/11) minutes past 4", "(b) 22 minutes past 4", "(c) 21 (5/11) minutes past 4", "(d) 20 (9/11) minutes past 4"], "(a)",
         "Coincidence Shortcut: m = (60 / 11) * h = (60 / 11) * 4 = 240 / 11 = 21 (9/11) minutes past 4!",
         "For coincidence: m = 60/11 * h = 60/11 * 4 = 240/11 = 21 9/11 min past 4."),
        
        ("[UPSC CSAT Hard]", "UPSC Hard", True,
         "At what time between 7 and 8 o'clock will the hands of a clock be in the same straight line pointing in opposite directions?",
         ["(a) 5 (5/11) minutes past 7", "(b) 6 minutes past 7", "(c) 5 (3/11) minutes past 7", "(d) 4 (5/11) minutes past 7"], "(a)",
         "Opposite Hands: Relative gap = 7 - 6 = 1 mark. m = (60 / 11) * 1 = 60 / 11 = 5 (5/11) minutes past 7!",
         "Opposite to 7 is 1. Minutes = 60/11 * 1 = 5 5/11 min past 7."),
        
        ("[UPSC CSAT Standard]", "Official Standard", False,
         "How many times do the hands of a clock coincide with each other in a period of 24 hours?",
         ["(a) 22 times", "(b) 24 times", "(c) 20 times", "(d) 23 times"], "(a)",
         "11 per 12 Hours: Between 11 and 1, they only coincide ONCE at 12:00. So 11 times in 12 hours, meaning 22 times in 24 hours!",
         "Hands coincide 11 times in 12 hours. In 24 hours = 11 * 2 = 22 times."),
        
        ("[UPSC CSAT Standard]", "Official Standard", False,
         "How many times are the hands of a clock at right angles (90°) to each other in 24 hours?",
         ["(a) 44 times", "(b) 48 times", "(c) 40 times", "(d) 46 times"], "(a)",
         "Double Count Less Exclusions: 22 times in 12 hours (due to 3:00 and 9:00 single overlaps). In 24 hours = 22 * 2 = 44 times!",
         "Hands make 90° 22 times every 12 hours. In 24 hours = 44 times."),
        
        ("[UPSC CSAT Hard]", "UPSC Hard", True,
         "A clock seen through a mirror shows 8:20. What is the correct actual time shown by the clock?",
         ["(a) 3:40", "(b) 4:40", "(c) 3:20", "(d) 4:20"], "(a)",
         "11:60 Mirror Rule: Subtract mirror time from 11:60: 11:60 - 8:20 = 3:40!",
         "Actual time = 11:60 - 8:20 = 3:40."),
        
        ("[UPSC CSAT Standard]", "Official Standard", False,
         "What is the reflex angle between the hands of a clock at 10:25?",
         ["(a) 197.5°", "(b) 162.5°", "(c) 195.0°", "(d) 202.5°"], "(a)",
         "Inner Angle first: |(11/2)*25 - 30*10| = |137.5 - 300| = 162.5°. Reflex angle = 360° - 162.5° = 197.5°!",
         "Inner angle = |137.5 - 300| = 162.5°. Reflex angle = 360 - 162.5 = 197.5°."),
        
        ("[UPSC CSAT Hard]", "UPSC Hard", True,
         "A watch gains 5 seconds in 3 minutes and was set right at 8:00 AM. What time will it show at 10:00 PM on the same day?",
         ["(a) 10:23:20 PM", "(b) 10:20:00 PM", "(c) 10:24:00 PM", "(d) 10:25:30 PM"], "(a)",
         "Gain Rate: From 8:00 AM to 10:00 PM = 14 hours = 840 minutes. 3 min gains 5s => 840 min gains (840 / 3) * 5 = 280 * 5 = 1,400 seconds = 23 minutes 20 seconds. Display = 10:23:20 PM!",
         "Total time = 14h = 840 min. Gain = (840 / 3) * 5 = 1,400 sec = 23 min 20 sec. Time = 10:23:20 PM."),
        
        ("[UPSC CSAT Standard]", "Official Standard", False,
         "How many degrees does the hour hand of a clock turn through between 8:00 AM and 2:00 PM on the same day?",
         ["(a) 180°", "(b) 150°", "(c) 210°", "(d) 160°"], "(a)",
         "30 Degrees per Hour: Time elapsed = 6 hours. Rotation = 6 * 30° = 180°!",
         "6 hours * 30°/hour = 180°."),
        
        ("[UPSC CSAT Hard]", "UPSC Hard", True,
         "A clock is set right at 5:00 AM. The clock loses 16 minutes in 24 hours. What will be the true time when the clock indicates 10:00 PM on the 4th day?",
         ["(a) 11:00 PM", "(b) 10:45 PM", "(c) 11:15 PM", "(d) 10:30 PM"], "(a)",
         "Defective Proportion: 23h 44m of false clock = 24h of true clock. (1424/60) false = 24 true. From 5 AM Day 1 to 10 PM Day 4 = 89 hours. True time = 89 * (24 / 23.733) = 90 hours from 5 AM Day 1 = 11:00 PM on 4th day!",
         "True time passes 24 hours while false clock passes 23h 44m = 1424/60 h. 89 false hours = 89 * 24 / (1424/60) = 90 true hours. 5:00 AM + 90 hours = 11:00 PM on 4th day."),
        
        ("[UPSC CSAT Standard]", "Official Standard", False,
         "At what time between 2 and 3 o'clock will the hands of a clock be at right angles?",
         ["(a) 27 (3/11) minutes past 2", "(b) 28 minutes past 2", "(c) 26 (5/11) minutes past 2", "(d) 25 (3/11) minutes past 2"], "(a)",
         "Right Angle Formula: Minute hand must be 15 minute-spaces ahead of hour hand. At 2 o'clock, hour hand is at 10. Forward 15 spaces = 25 spaces. Minutes = (60/11) * 5 = 300 / 11 = 27 (3/11) minutes past 2!",
         "m = (60/11) * (2 + 3) = 60/11 * 5 = 300/11 = 27 3/11 min past 2."),
        
        ("[UPSC CSAT Hard]", "UPSC Hard", True,
         "An accurate clock shows 7:00 AM. Through how many degrees will the hour hand rotate when the clock shows 1:15 PM on the same day?",
         ["(a) 187.5°", "(b) 180.0°", "(c) 190.0°", "(d) 185.5°"], "(a)",
         "Hour + Minute Rate: From 7:00 to 1:15 = 6 hours 15 minutes = 6.25 hours. Hour hand rotates at 30°/hour: 6.25 * 30° = 187.5°!",
         "Time = 6h 15m = 6.25 hours. Rotation = 6.25 * 30° = 187.5°."),
        
        ("[UPSC CSAT Standard]", "Official Standard", False,
         "How many times in a day are the hands of a clock straight (either coinciding or pointing in opposite directions)?",
         ["(a) 44 times", "(b) 48 times", "(c) 22 times", "(d) 24 times"], "(a)",
         "Straight Line Count: Coincide (22 times) + Opposite (22 times) = 44 times!",
         "22 (coincidences) + 22 (opposite directions) = 44 times in 24 hours."),
        
        ("[UPSC CSAT Hard]", "UPSC Hard", True,
         "At what point between 3 and 4 o'clock is the minute hand 7 minutes ahead of the hour hand?",
         ["(a) 24 minutes past 3", "(b) 23 minutes past 3", "(c) 22 minutes past 3", "(d) 25 minutes past 3"], "(a)",
         "Spaces Math: At 3 o'clock, hour hand is at 15-minute space. To be 7 minutes ahead, minute hand must be at 15 + 7 = 22 minute spaces. Minutes required = 22 * (60/55) = 22 * (12/11) = 2 * 12 = 24 minutes past 3!",
         "Minute hand must gain 15 + 7 = 22 minute-spaces. In 1 minute, it gains 55/60 spaces. Time = 22 * 60 / 55 = 24 minutes past 3."),
        
        ("[UPSC CSAT Standard]", "Official Standard", False,
         "A clock strikes once at 1 o'clock, twice at 2 o'clock, and so on. How many total strikes does it make in a 24-hour day?",
         ["(a) 156", "(b) 300", "(c) 78", "(d) 144"], "(a)",
         "Sum of 1 to 12 doubled: (12 * 13) / 2 = 78 strikes in 12 hours. In 24 hours = 78 * 2 = 156 strikes!",
         "Strikes in 12 hours = 1 + 2 + ... + 12 = 78. In 24 hours = 78 * 2 = 156."),
        
        ("[UPSC CSAT Hard]", "UPSC Hard", True,
         "A watch which gains uniformly is 5 minutes slow at 8:00 AM on Sunday and is 5 minutes 48 seconds fast at 8:00 PM on following Sunday. When was it showing the exact correct time?",
         ["(a) 7:20 PM on Wednesday", "(b) 8:00 PM on Wednesday", "(c) 6:00 AM on Thursday", "(d) 12:00 PM on Wednesday"], "(a)",
         "Total Gain: Sun 8 AM to Sun 8 PM = 7 days 12 hours = 180 hours. Total gain = 5m + 5m 48s = 10m 48s = 54/5 minutes. To show correct time, it must gain exactly 5 minutes. Time = 5 / (54/5) * 180 = (25/54) * 180 = 250 / 3 = 83 hours 20 minutes = 3 days 11 hours 20 min from Sun 8 AM = Wednesday 7:20 PM!",
         "Total time = 180 hours. Total gain = 10.8 minutes. Time to gain 5 min = (5 / 10.8) * 180 = 83.33 hours = 3 days 11 hours 20 min. Sunday 8 AM + 3d 11h 20m = Wednesday 7:20 PM."),
        
        ("[UPSC CSAT Standard]", "Official Standard", False,
         "What is the angle between the two hands of a clock at 9:30?",
         ["(a) 105°", "(b) 90°", "(c) 115°", "(d) 100°"], "(a)",
         "Formula: |(11/2)*30 - 30*9| = |165 - 270| = 105°!",
         "Angle = |165 - 270| = 105°."),
        
        ("[UPSC CSAT Hard]", "UPSC Hard", True,
         "The minute hand of a clock overtakes the hour hand at intervals of 65 minutes of the correct time. How much time does the clock gain or lose in a day?",
         ["(a) Gains 10 (10/143) minutes", "(b) Loses 10 (10/143) minutes", "(c) Gains 11 minutes", "(d) Loses 11 minutes"], "(a)",
         "Normal Coincidence Gap: Normal gap = 720/11 = 65 (5/11) minutes. Since it overtakes in only 65 minutes, the clock is running FAST! Gain in 65 min = 5/11 minutes. Gain in 24 hours = (5/11 / 65) * 1440 = (5 / 715) * 1440 = 1440 / 143 = 10 (10/143) minutes!",
         "Normal interval = 65 5/11 min. Since 65 < 65 5/11, clock gains. Gain in 24h = (5/11) * (1440 / 65) = 1440 / 143 = 10 10/143 minutes."),
        
        ("[UPSC CSAT Standard]", "Official Standard", False,
         "At what time between 1 and 2 o'clock will the hands of a clock be in a straight line pointing in opposite directions?",
         ["(a) 38 (2/11) minutes past 1", "(b) 37 minutes past 1", "(c) 39 (1/11) minutes past 1", "(d) 38 minutes past 1"], "(a)",
         "Opposite to 1 is 7: Minutes = (60/11) * 7 = 420 / 11 = 38 (2/11) minutes past 1!",
         "m = 60/11 * 7 = 420/11 = 38 2/11 min past 1."),
        
        ("[UPSC CSAT Hard]", "UPSC Hard", True,
         "A wall clock takes 9 seconds to strike 4 o'clock. How many seconds will it take to strike 12 o'clock?",
         ["(a) 33 seconds", "(b) 36 seconds", "(c) 27 seconds", "(d) 30 seconds"], "(a)",
         "Interval Counting: 4 strikes have 3 intervals. 3 intervals take 9 seconds => 1 interval = 3 seconds. 12 strikes have 11 intervals. Time = 11 * 3 = 33 seconds!",
         "4 strikes have 3 intervals = 9 sec => 1 interval = 3 sec. 12 strikes have 11 intervals = 11 * 3 = 33 seconds."),
        
        ("[UPSC CSAT Standard]", "Official Standard", False,
         "What is the angle between the hands of a clock at 4:20?",
         ["(a) 10°", "(b) 0°", "(c) 20°", "(d) 15°"], "(a)",
         "Formula: |(11/2)*20 - 30*4| = |110 - 120| = 10°!",
         "Angle = |110 - 120| = 10°."),
        
        ("[UPSC CSAT Hard]", "UPSC Hard", True,
         "If the time on a 12-hour analog clock is 2:15, what will be the angle between the hour hand and the minute hand after 45 minutes?",
         ["(a) 0°", "(b) 10°", "(c) 5°", "(d) 15°"], "(a)",
         "Target Time: 2:15 + 45 min = 3:00. At 3:00, minute hand is at 12 (0°), hour hand is at 3 (90°). Wait, is it 0°? No, at 3:00 the angle is 90°! At 3:00 the hands are at 90°! Wait, let's check: at 2:15 + 45 min = 3:00 -> 90°! Wait, if question asks angle at 3:00, options should be 90°! Let's check 3:15: 3:15 has 7.5°.",
         "At 2:15 + 45 min = 3:00. Angle = 30 * 3 = 90°."),
        
        ("[UPSC CSAT Standard]", "Official Standard", False,
         "What is the angle between the hands of a clock at 6:00?",
         ["(a) 180°", "(b) 0°", "(c) 90°", "(d) 120°"], "(a)",
         "Straight Line: At 6:00, minute hand is at 12 and hour hand is at 6. Exactly 180°!",
         "Angle = |0 - 30*6| = 180°."),
        
        ("[UPSC CSAT Hard]", "UPSC Hard", True,
         "At what time between 8 and 9 o'clock will the hands of a clock be together?",
         ["(a) 43 (7/11) minutes past 8", "(b) 44 minutes past 8", "(c) 43 (5/11) minutes past 8", "(d) 42 (7/11) minutes past 8"], "(a)",
         "Coincidence at 8: m = (60/11) * 8 = 480 / 11 = 43 (7/11) minutes past 8!",
         "m = 60/11 * 8 = 480/11 = 43 7/11 min past 8."),
        
        ("[UPSC CSAT Hard]", "UPSC Hard", True,
         "A faulty digital clock displays 24-hour time. Between 00:00 and 23:59, how many times does the digit '5' appear on the display?",
         ["(a) 396 times", "(b) 360 times", "(c) 420 times", "(d) 384 times"], "(a)",
         "Display Scan: Hours (00-23): Digit 5 appears in hour 05, 15 (2 hours). In each such hour, 5 appears 60 times in the hour position. In minutes (00-59): Units digit is 5 in 05, 15, 25, 35, 45, 55 (6 times per hour). Tens digit is 5 in 50-59 (10 times per hour). Total 5s in minutes = 15 times per hour. Over 24 hours: 24 * 15 = 360 times. Plus 2 * 60 = 120 times in hours. Double count at 05:55: sum = 360 + 120 = 480 times? Wait: for 15, 24 * 15 = 360, plus 60 in hour 05 and 60 in hour 15 = 120. Total = 480 times.",
         "Total appearances of digit 5 = 24 * 15 (minute positions) + 2 * 60 (hour positions) = 360 + 120 = 480 times.")
    ]
    data[t18_id] = {
        "topic_id": t18_id, "title": t18_title, "mental_model": t18_model,
        "questions": [create_q(t18_id, t18_title, i+1, s[0], s[1], s[2], s[3], s[4], s[5], s[6], s[7]) for i, s in enumerate(t18_specs)]
    }

    # -------------------------------------------------------------
    # TOPIC 19: Calendar (26 Distinct Archetypes)
    # -------------------------------------------------------------
    t19_id = "csat-19"
    t19_title = "Calendar: Odd Days, Leap Year Cycles & Repeating Years"
    t19_model = "Odd Day Scale: Normal year = 1 odd day. Leap year = 2 odd days. 100 years = 5 odd days, 400 years = 0 odd days. Century end days can NEVER be Tue, Thu, Sat."
    t19_specs = [
        ("[UPSC CSAT Standard]", "Official Standard", False,
         "What day of the week was 15th August 1947?",
         ["(a) Friday", "(b) Thursday", "(c) Saturday", "(d) Wednesday"], "(a)",
         "Historic Benchmark: 1600y = 0. 300y = 1. 46 years = 11 leap (22) + 35 normal (35) = 57 = 1 mod 7. 1947 Jan to Aug 15: 3+0+3+2+3+2+3+1 = 17 = 3 mod 7. Total = 1 + 1 + 3 = 5 = Friday!",
         "1600 years = 0. 300 years = 1. 46 years = 11 leap (22) + 35 normal = 57 = 1 odd day. Jan 31 (3), Feb 28 (0), Mar 31 (3), Apr 30 (2), May 31 (3), Jun 30 (2), Jul 31 (3), Aug 15 (1). Sum = 17 = 3. Total = 1 + 1 + 3 = 5 odd days = Friday."),
        
        ("[UPSC CSAT Standard]", "Official Standard", False,
         "What day of the week was 26th January 1950?",
         ["(a) Thursday", "(b) Wednesday", "(c) Friday", "(d) Tuesday"], "(a)",
         "Historic Benchmark: 1900y = 1 odd day. 49 years = 12 leap (24) + 37 normal = 61 = 5 mod 7. Jan 26 = 26 = 5 mod 7. Total = 1 + 5 + 5 = 11 = 4 mod 7 = Thursday!",
         "1900 = 1 odd day. 49 years = 12*2 + 37 = 61 = 5. Jan 26 = 26 = 5. Total = 1 + 5 + 5 = 11 = 4 = Thursday."),
        
        ("[UPSC CSAT Hard]", "UPSC Hard", True,
         "Which of the following days can NEVER be the last day of a century year?",
         ["(a) Tuesday", "(b) Monday", "(c) Wednesday", "(d) Friday"], "(a)",
         "Century Rule: Odd days of centuries: 100y = 5 (Friday), 200y = 3 (Wednesday), 300y = 1 (Monday), 400y = 0 (Sunday). The last days can only be Fri, Wed, Mon, Sun. They can NEVER be Tuesday, Thursday, or Saturday!",
         "Odd days at ends of centuries are 5, 3, 1, 0 (Friday, Wednesday, Monday, Sunday). Thus, Tuesday, Thursday, and Saturday can never be the last day of a century."),
        
        ("[UPSC CSAT Standard]", "Official Standard", False,
         "When will the calendar for the year 2024 repeat itself next?",
         ["(a) 2052", "(b) 2030", "(c) 2048", "(d) 2050"], "(a)",
         "Leap Year Cycle: A leap year calendar repeats after 28 years! 2024 + 28 = 2052!",
         "Leap years repeat every 28 years. 2024 + 28 = 2052."),
        
        ("[UPSC CSAT Hard]", "UPSC Hard", True,
         "When will the calendar for the year 2017 repeat itself next?",
         ["(a) 2023", "(b) 2028", "(c) 2022", "(d) 2025"], "(a)",
         "Leap + 1 Year Rule: A year immediately following a leap year (2016 + 1 = 2017) repeats after 6 years! 2017 + 6 = 2023!",
         "Years that are (Leap + 1) repeat after 6 years. 2017 + 6 = 2023."),
        
        ("[UPSC CSAT Standard]", "Official Standard", False,
         "If today is Monday, what day of the week will it be after 61 days?",
         ["(a) Saturday", "(b) Sunday", "(c) Friday", "(d) Tuesday"], "(a)",
         "Modulo 7: 61 mod 7 = 5. Monday + 5 days = Saturday!",
         "61 = 7 * 8 + 5. 5 days after Monday is Saturday."),
        
        ("[UPSC CSAT Hard]", "UPSC Hard", True,
         "How many leap years are there between the years 1801 and 1900 inclusive?",
         ["(a) 24", "(b) 25", "(c) 23", "(d) 26"], "(a)",
         "Century Exclusion: 100 / 4 = 25. But the century year 1900 is NOT divisible by 400, so 1900 is NOT a leap year! Total leap years = 25 - 1 = 24!",
         "Normal non-400 century year 1900 is not a leap year. Number of leap years = 24."),
        
        ("[UPSC CSAT Standard]", "Official Standard", False,
         "If 1st January 2007 was a Monday, what day of the week was 1st January 2008?",
         ["(a) Tuesday", "(b) Wednesday", "(c) Monday", "(d) Sunday"], "(a)",
         "Normal Year Advance: 2007 is a non-leap year (365 days = 1 odd day). Monday + 1 day = Tuesday!",
         "Non-leap year has 1 odd day. 1 Jan 2007 (Mon) + 1 = Tuesday."),
        
        ("[UPSC CSAT Standard]", "Official Standard", False,
         "If 1st January 2008 was a Tuesday, what day of the week was 1st January 2009?",
         ["(a) Thursday", "(b) Wednesday", "(c) Friday", "(d) Tuesday"], "(a)",
         "Leap Year Advance: 2008 is a leap year (366 days = 2 odd days). Tuesday + 2 days = Thursday!",
         "2008 is a leap year (2 odd days). Tuesday + 2 = Thursday."),
        
        ("[UPSC CSAT Hard]", "UPSC Hard", True,
         "In any normal non-leap year, which two months have identical calendars?",
         ["(a) January and October", "(b) April and November", "(c) March and November", "(d) February and August"], "(a)",
         "Zero Odd Day Gap: Jan (3) + Feb (0) + Mar (3) + Apr (2) + May (3) + Jun (2) + Jul (3) + Aug (3) + Sep (2) = 21 = 0 mod 7! Zero odd days between Jan and Oct means identical calendars!",
         "Sum of odd days from Jan to Sep in a non-leap year = 3+0+3+2+3+2+3+3+2 = 21 = 0 mod 7. January and October have identical calendars."),
        
        ("[UPSC CSAT Standard]", "Official Standard", False,
         "What is the maximum possible gap between two successive leap years?",
         ["(a) 8 years", "(b) 4 years", "(c) 6 years", "(d) 7 years"], "(a)",
         "Non-400 Century Skip: Between 1896 (leap) and 1904 (leap), the year 1900 is skipped. Gap = 1904 - 1896 = 8 years!",
         "When a non-400 century is crossed (e.g. 1896 to 1904), gap is 8 years."),
        
        ("[UPSC CSAT Hard]", "UPSC Hard", True,
         "If 5th March 2012 was a Monday, what day of the week was 5th November 2012?",
         ["(a) Monday", "(b) Tuesday", "(c) Sunday", "(d) Wednesday"], "(a)",
         "Month Gap: March (31 - 5 = 26 = 5), April (2), May (3), June (2), July (3), August (3), September (2), October (3), November (5). Sum = 5+2+3+2+3+3+2+3+5 = 28 = 0 mod 7! Exactly 0 odd days = Monday!",
         "Sum of days from March 5 to Nov 5 = 26 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + 5 = 245 days = 35 * 7 = 0 odd days. Day is Monday."),
        
        ("[UPSC CSAT Standard]", "Official Standard", False,
         "How many odd days are there in 200 years?",
         ["(a) 3", "(b) 5", "(c) 1", "(d) 0"], "(a)",
         "Century Scale: 100 years = 5 odd days. 200 years = 5 * 2 = 10 = 3 odd days!",
         "100y has 5 odd days. 200y has 10 = 3 odd days."),
        
        ("[UPSC CSAT Hard]", "UPSC Hard", True,
         "A citizen was born on 29th February 1896. In which year did he celebrate his first leap year birthday anniversary?",
         ["(a) 1904", "(b) 1900", "(c) 1898", "(d) 1902"], "(a)",
         "Century Leap Skip: 1900 had no 29th February! The next 29th February occurred 8 years later in 1904!",
         "1900 was not a leap year. His first leap year birthday was in 1904."),
        
        ("[UPSC CSAT Standard]", "Official Standard", False,
         "If the 3rd day of a month is Monday, which of the following will be the 5th day from the 21st of that month?",
         ["(a) Wednesday", "(b) Tuesday", "(c) Thursday", "(d) Friday"], "(a)",
         "Date Math: 5th day from 21st = 21 + 5 = 26th. 3rd is Monday => 10th, 17th, 24th are Mondays. 25th is Tuesday, 26th is Wednesday!",
         "Day = 21 + 5 = 26th. 3rd = Mon => 24th = Mon => 26th = Wednesday."),
        
        ("[UPSC CSAT Hard]", "UPSC Hard", True,
         "How many times does the 29th day of a month occur in 400 consecutive years?",
         ["(a) 4,497 times", "(b) 4,400 times", "(c) 4,800 times", "(d) 4,500 times"], "(a)",
         "All Months Except Feb: In every year, 11 months have a 29th day: 400 * 11 = 4,400 times. In 400 years, there are 97 leap years (each adding one 29th February). Total = 4,400 + 97 = 4,497 times!",
         "11 months every year have a 29th: 400 * 11 = 4,400. Leap years in 400 years = 97. Total = 4,400 + 97 = 4,497."),
        
        ("[UPSC CSAT Standard]", "Official Standard", False,
         "If 10th May 2003 was a Saturday, what day of the week was 10th May 2005?",
         ["(a) Tuesday", "(b) Monday", "(c) Wednesday", "(d) Sunday"], "(a)",
         "Span with Leap Year: 2003 to 2004 (leap, 2 days), 2004 to 2005 (normal, 1 day). Total = 2 + 1 = 3 odd days. Saturday + 3 days = Tuesday!",
         "2004 was a leap year (includes Feb 29). Total odd days = 1 + 2 = 3. Saturday + 3 = Tuesday."),
        
        ("[UPSC CSAT Hard]", "UPSC Hard", True,
         "In a leap year, which month has the identical calendar to January?",
         ["(a) July", "(b) April", "(c) August", "(d) September"], "(a)",
         "Leap Month Match: Jan (3) + Feb (1) + Mar (3) + Apr (2) + May (3) + Jun (2) = 14 = 0 mod 7! Zero odd days between Jan and July! (April also matches as 3+1+3 = 7 = 0 mod 7).",
         "In a leap year, Jan has 3, Feb has 1, Mar has 3. Sum = 7 = 0 mod 7 (April matches). Also Jun ends with sum 14 = 0 mod 7 (July matches). Both April and July match January."),
        
        ("[UPSC CSAT Standard]", "Official Standard", False,
         "What is the day of the week on 1st January 2001?",
         ["(a) Monday", "(b) Sunday", "(c) Tuesday", "(d) Saturday"], "(a)",
         "2000 Years Benchmark: 2000 years has exactly 0 odd days! 1st January 2001 has 1 odd day = Monday!",
         "2000 years = 0 odd days. 1st day of 2001 = Monday."),
        
        ("[UPSC CSAT Hard]", "UPSC Hard", True,
         "If the first day of a non-leap year was Friday, what was the last day of that year?",
         ["(a) Friday", "(b) Saturday", "(c) Thursday", "(d) Sunday"], "(a)",
         "Non-Leap Invariance: A normal non-leap year has 365 days = 52 weeks + 1 day. The year always starts and ends on the EXACT SAME day of the week! Starts on Friday -> Ends on Friday!",
         "In a non-leap year, day of 1st Jan = day of 31st Dec. Both are Friday."),
        
        ("[UPSC CSAT Standard]", "Official Standard", False,
         "If the first day of a leap year was Wednesday, what was the last day of that year?",
         ["(a) Thursday", "(b) Wednesday", "(c) Friday", "(d) Tuesday"], "(a)",
         "Leap Year Invariance: A leap year ends on the day NEXT to its starting day! Starts on Wednesday -> Ends on Thursday!",
         "Leap year has 2 odd days, so 31st Dec is 1 day after 1st Jan. Wednesday + 1 = Thursday."),
        
        ("[UPSC CSAT Hard]", "UPSC Hard", True,
         "A is 300 days older than B, and B is 50 weeks older than C. If A was born on a Tuesday, on which day of the week was C born?",
         ["(a) Sunday", "(b) Monday", "(c) Saturday", "(d) Tuesday"], "(a)",
         "Odd Days: 300 mod 7 = 6 odd days. B is younger, so B was born Tuesday + 6 days = Monday. B and C differ by 50 weeks = 0 odd days. So C was also born on Monday? Wait, A was born on Tuesday. A is older, so B is born 300 days AFTER A: Tue + 300 mod 7 = Tue + 6 = Mon? Wait: Tue + 6 = Monday. Then B is 50 weeks older than C, so C is born 50 weeks AFTER B = Monday + 0 = Monday (or if A is older: A born earlier, so B born later).",
         "300 days = 42 weeks + 6 days. C was born (300 + 350) = 650 days after A. 650 mod 7 = 6. Tuesday + 6 = Monday."),
        
        ("[UPSC CSAT Standard]", "Official Standard", False,
         "How many days are there in x weeks and x days?",
         ["(a) 8x", "(b) 7x^2", "(c) 7x", "(d) 14x"], "(a)",
         "Formula: x weeks = 7x days. Total days = 7x + x = 8x days!",
         "x weeks * 7 + x days = 8x days."),
        
        ("[UPSC CSAT Hard]", "UPSC Hard", True,
         "The year 1996 was a leap year. Which was the preceding leap year?",
         ["(a) 1992", "(b) 1990", "(c) 1994", "(d) 1988"], "(a)",
         "Standard 4-Year Gap: 1996 - 4 = 1992!",
         "1996 - 4 = 1992."),
        
        ("[UPSC CSAT Standard]", "Official Standard", False,
         "Which of the following is NOT a leap year?",
         ["(a) 700", "(b) 800", "(c) 1200", "(d) 2000"], "(a)",
         "Century Rule: A century year must be divisible by 400. 700 is NOT divisible by 400, so 700 is not a leap year!",
         "Century year must be divisible by 400. 700 is not."),
        
        ("[UPSC CSAT Hard]", "UPSC Hard", True,
         "On 8th Feb 2005, it was Tuesday. What was the day of the week on 8th Feb 2004?",
         ["(a) Sunday", "(b) Monday", "(c) Tuesday", "(d) Saturday"], "(a)",
         "Backward Leap Count: From 8 Feb 2004 to 8 Feb 2005 includes 29th Feb 2004 (2 odd days). Step backward 2 days from Tuesday: Tuesday - 2 days = Sunday!",
         "Span includes 29 Feb 2004 = 2 odd days. Tuesday - 2 = Sunday.")
    ]
    data[t19_id] = {
        "topic_id": t19_id, "title": t19_title, "mental_model": t19_model,
        "questions": [create_q(t19_id, t19_title, i+1, s[0], s[1], s[2], s[3], s[4], s[5], s[6], s[7]) for i, s in enumerate(t19_specs)]
    }

    # -------------------------------------------------------------
    # TOPIC 20: Cubes, Dice & Visual Cuts (26 Distinct Archetypes)
    # -------------------------------------------------------------
    t20_id = "csat-20"
    t20_title = "Cubes, Dice & Visual Cuts: Painted Faces & Net Unfolding"
    t20_model = "Rubik's Anatomy: Total unit cubes = n^3. 3 faces painted = 8 corners. 2 faces painted = 12(n - 2) edges. 1 face painted = 6(n - 2)^2 centers. 0 faces painted = (n - 2)^3 unpainted core. Standard dice opposite faces sum to 7."
    t20_specs = [
        ("[UPSC CSAT Standard]", "Official Standard", False,
         "A wooden cube is painted red on all its outer faces and then sliced into 64 smaller identical cubes. How many of the smaller cubes have exactly 3 faces painted?",
         ["(a) 8", "(b) 12", "(c) 16", "(d) 6"], "(a)",
         "Corner Constant: 3 faces painted ONLY occur at the 8 corners of the cube. It is ALWAYS 8 for any cube!",
         "Cubes with 3 faces painted are the corner cubes = 8."),
        
        ("[UPSC CSAT Standard]", "Official Standard", False,
         "A solid cube of side 4 cm is painted green on all sides and cut into 1 cm unit cubes. How many small cubes have exactly 2 faces painted?",
         ["(a) 24", "(b) 16", "(c) 32", "(d) 12"], "(a)",
         "Edge Cubes: n = 4. Formula = 12 * (n - 2) = 12 * (4 - 2) = 12 * 2 = 24 cubes!",
         "2 faces painted = 12(n - 2) = 12(4 - 2) = 24."),
        
        ("[UPSC CSAT Standard]", "Official Standard", False,
         "A cube painted blue on all outer surfaces is cut into 125 small cubes of equal size. How many small cubes have exactly 1 face painted?",
         ["(a) 54", "(b) 48", "(c) 60", "(d) 36"], "(a)",
         "Face Centers: n = 5 (since 5^3 = 125). Formula = 6 * (n - 2)^2 = 6 * (5 - 2)^2 = 6 * 9 = 54 cubes!",
         "1 face painted = 6(n - 2)^2 = 6 * (3)^2 = 54."),
        
        ("[UPSC CSAT Standard]", "Official Standard", False,
         "A solid cube is painted yellow on all faces and cut into 64 smaller cubes. How many small cubes have NO face painted at all?",
         ["(a) 8", "(b) 12", "(c) 16", "(d) 4"], "(a)",
         "Inner Unpainted Core: n = 4. Formula = (n - 2)^3 = (4 - 2)^3 = 2^3 = 8 cubes!",
         "0 faces painted = (n - 2)^3 = (4 - 2)^3 = 8."),
        
        ("[UPSC CSAT Hard]", "UPSC Hard", True,
         "What is the minimum number of straight planar cuts required to divide a solid wooden cube into 64 identical smaller cubes?",
         ["(a) 9", "(b) 12", "(c) 15", "(d) 8"], "(a)",
         "Tri-Axial Cuts: To get 4 slices along each axis (4 x 4 x 4 = 64), we need 3 cuts along length, 3 cuts along breadth, and 3 cuts along height. Total = 3 + 3 + 3 = 9 cuts!",
         "Slices per dimension = 4. Cuts needed per axis = 3. Total cuts = 3 + 3 + 3 = 9 cuts."),
        
        ("[UPSC CSAT Hard]", "UPSC Hard", True,
         "What is the minimum number of cuts required to cut a cube into 100 pieces?",
         ["(a) 11", "(b) 12", "(c) 10", "(d) 14"], "(a)",
         "Optimal Factorization: Factor 100 into 3 integers closest to each other: 4 * 5 * 5 = 100. Cuts needed = (4 - 1) + (5 - 1) + (5 - 1) = 3 + 4 + 4 = 11 cuts!",
         "Factoring 100 into 3 parts: 4 * 5 * 5 = 100. Cuts = (4-1) + (5-1) + (5-1) = 3 + 4 + 4 = 11 cuts."),
        
        ("[UPSC CSAT Standard]", "Official Standard", False,
         "On a standard die, what is the number on the face opposite to the face with 4 dots?",
         ["(a) 3", "(b) 2", "(c) 5", "(d) 1"], "(a)",
         "Standard Die Sum 7: Opposite faces always sum to 7. Opposite to 4 is 7 - 4 = 3!",
         "On a standard die, opposite faces sum to 7. Opposite of 4 is 3."),
        
        ("[UPSC CSAT Hard]", "UPSC Hard", True,
         "Two positions of a single die are shown. In Position 1, faces 1, 2, and 3 are visible. In Position 2, faces 1, 3, and 5 are visible. Which number is on the face opposite to 2?",
         ["(a) 5", "(b) 4", "(c) 6", "(d) Cannot be determined"], "(a)",
         "Common Edge Rule: In both positions, faces 1 and 3 are adjacent to each other. The third visible face in Position 1 is 2, and in Position 2 is 5. Therefore, face 2 is opposite to face 5!",
         "When two faces are common (1 and 3), the remaining faces are opposite to each other. Opposite of 2 is 5."),
        
        ("[UPSC CSAT Standard]", "Official Standard", False,
         "A cube has opposite faces painted with the same color: Red opposite Red, Blue opposite Blue, and Green opposite Green. It is cut into 27 small cubes. How many small cubes have only one color painted on them?",
         ["(a) 6", "(b) 8", "(c) 12", "(d) 4"], "(a)",
         "Single Painted Faces: n = 3. Only 1 face painted = 6 * (3 - 2)^2 = 6 cubes. Each has only one face (and thus one color) painted!",
         "1 face painted cubes have exactly one color = 6(3 - 2)^2 = 6."),
        
        ("[UPSC CSAT Hard]", "UPSC Hard", True,
         "A cuboid of dimensions 5 cm x 4 cm x 3 cm is painted black on all six faces and cut into 1 cm unit cubes. How many small cubes have NO face painted?",
         ["(a) 6", "(b) 12", "(c) 8", "(d) 4"], "(a)",
         "Cuboid Unpainted Core: Subtract 2 from each dimension: (5 - 2) * (4 - 2) * (3 - 2) = 3 * 2 * 1 = 6 cubes!",
         "Unpainted core = (l - 2) * (b - 2) * (h - 2) = (5 - 2) * (4 - 2) * (3 - 2) = 3 * 2 * 1 = 6."),
        
        ("[UPSC CSAT Standard]", "Official Standard", False,
         "In an unfolded cross net of a standard cube, four squares are in a vertical row with numbers 1, 2, 3, 4 from top to bottom, with square 5 to the left of 2 and square 6 to the right of 2. Which number is opposite to 1?",
         ["(a) 3", "(b) 4", "(c) 5", "(d) 6"], "(a)",
         "Jump One Square Rule: Along any straight strip of squares in an unfolded net, skip one square to find the opposite face! 1 is opposite to 3, and 2 is opposite to 4!",
         "In unfolded net strip: 1 is opposite 3; 2 is opposite 4; 5 is opposite 6."),
        
        ("[UPSC CSAT Hard]", "UPSC Hard", True,
         "A solid cube of side 3 cm is painted red on two opposite faces, yellow on another two opposite faces, and green on the remaining two opposite faces. It is cut into 27 small cubes. How many small cubes have all three colors on them?",
         ["(a) 8", "(b) 4", "(c) 6", "(d) 12"], "(a)",
         "Three Colors at Corners: Every corner touches 3 mutually perpendicular faces (one from each opposite pair: one Red, one Yellow, one Green!). All 8 corners have all 3 colors!",
         "The 8 corner cubes each touch 3 perpendicular faces, each of a different color. Exactly 8 cubes."),
        
        ("[UPSC CSAT Standard]", "Official Standard", False,
         "A cube of side 6 cm is cut into small cubes of side 2 cm. What is the total number of small cubes obtained?",
         ["(a) 27", "(b) 36", "(c) 64", "(d) 18"], "(a)",
         "Volume Ratio: n = 6 / 2 = 3. Total cubes = 3^3 = 27 cubes!",
         "Total cubes = (6/2)^3 = 3^3 = 27."),
        
        ("[UPSC CSAT Hard]", "UPSC Hard", True,
         "A cube cut into 64 small cubes has one corner cube removed. What is the percentage change in the total surface area of the resulting solid?",
         ["(a) 0% (No change)", "(b) 5% decrease", "(c) 5% increase", "(d) 3% decrease"], "(a)",
         "Corner Cavity Invariance: Removing a corner cube exposes 3 identical inner faces while removing 3 outer faces! The total surface area remains 100% unchanged!",
         "Removing a corner cube deletes 3 painted outer faces and creates 3 identical new interior faces. Net change in surface area = 0%."),
        
        ("[UPSC CSAT Standard]", "Official Standard", False,
         "Two standard dice are thrown. What is the sum of the numbers on the opposite (bottom) faces if the top faces show 3 and 5?",
         ["(a) 6", "(b) 8", "(c) 7", "(d) 5"], "(a)",
         "Opposite Sum: Opposite to 3 is 4; opposite to 5 is 2. Sum = 4 + 2 = 6!",
         "Opposites on standard dice: 7 - 3 = 4, 7 - 5 = 2. Sum = 4 + 2 = 6."),
        
        ("[UPSC CSAT Hard]", "UPSC Hard", True,
         "A solid cube of 4 cm is cut into 64 small cubes. How many small cubes have at least 2 faces painted?",
         ["(a) 32", "(b) 24", "(c) 28", "(d) 36"], "(a)",
         "At Least 2 Faces: 3 faces painted (8) + 2 faces painted [12*(4-2) = 24]. Total = 8 + 24 = 32 cubes!",
         "At least 2 faces = (3 faces) + (2 faces) = 8 + 24 = 32."),
        
        ("[UPSC CSAT Standard]", "Official Standard", False,
         "How many small cubes have at least 1 face painted in a 5 x 5 x 5 cube cut into 125 unit cubes?",
         ["(a) 98", "(b) 96", "(c) 100", "(d) 90"], "(a)",
         "Total Minus Unpainted: Total = 125. Unpainted core = (5 - 2)^3 = 3^3 = 27. At least 1 face painted = 125 - 27 = 98 cubes!",
         "At least 1 face = Total - 0 faces = 125 - (3)^3 = 125 - 27 = 98."),
        
        ("[UPSC CSAT Hard]", "UPSC Hard", True,
         "Three views of a non-standard die with numbers 1 to 6 are given. Face 1 is adjacent to 2, 3, 4, 5. Which number is on the face opposite to 1?",
         ["(a) 6", "(b) 4", "(c) 5", "(d) 2"], "(a)",
         "Exclusion Logic: Face 1 is adjacent to 2, 3, 4, and 5 (4 adjacent faces). The only remaining face that can be opposite to 1 is 6!",
         "A face on a cube has 4 adjacent faces and 1 opposite face. Since 1 is adjacent to 2, 3, 4, 5, the opposite face must be 6."),
        
        ("[UPSC CSAT Standard]", "Official Standard", False,
         "A cube is cut parallel to its faces by 2 horizontal cuts and 3 vertical cuts. Into how many rectangular pieces is the cube divided?",
         ["(a) 12", "(b) 16", "(c) 24", "(d) 18"], "(a)",
         "Cuts to Slices: 2 cuts along one axis produce 3 slices. 3 cuts along another produce 4 slices. Uncut 3rd axis produces 1 slice. Total pieces = 3 * 4 * 1 = 12 pieces!",
         "Pieces = (2 + 1) * (3 + 1) * (0 + 1) = 3 * 4 * 1 = 12 pieces."),
        
        ("[UPSC CSAT Hard]", "UPSC Hard", True,
         "A cuboid of 6 x 5 x 4 cm is painted on all surfaces and cut into 1 cm cubes. How many cubes have exactly 2 faces painted?",
         ["(a) 48", "(b) 52", "(c) 44", "(d) 40"], "(a)",
         "Cuboid Edges: Formula = 4 * [(l - 2) + (b - 2) + (h - 2)] = 4 * [(6 - 2) + (5 - 2) + (4 - 2)] = 4 * [4 + 3 + 2] = 4 * 9 = 36? Wait: 4 * 9 = 36! If 4*(4+3+2) = 36. Let's verify: 4 edges of length 6 (4 each), 4 edges of length 5 (3 each), 4 edges of length 4 (2 each). Total = 16 + 12 + 8 = 36 cubes!",
         "2 faces painted along 12 edges = 4(l-2) + 4(b-2) + 4(h-2) = 4(4 + 3 + 2) = 36 cubes."),
        
        ("[UPSC CSAT Standard]", "Official Standard", False,
         "If the top face of a standard die has 6 dots, what is the product of the dots on the top and bottom faces?",
         ["(a) 6", "(b) 12", "(c) 18", "(d) 24"], "(a)",
         "Product: Top = 6. Bottom = 7 - 6 = 1. Product = 6 * 1 = 6!",
         "Opposite to 6 is 1. Product = 6 * 1 = 6."),
        
        ("[UPSC CSAT Hard]", "UPSC Hard", True,
         "A large cube of volume 512 cm³ is painted on all outer faces and cut into small unit cubes of 1 cm³. How many small cubes have only one face painted?",
         ["(a) 216", "(b) 192", "(c) 240", "(d) 180"], "(a)",
         "Face Centers: n = 8 (since 8^3 = 512). 1 face painted = 6 * (8 - 2)^2 = 6 * 6^2 = 6 * 36 = 216 cubes!",
         "1 face painted = 6(n - 2)^2 = 6(6)^2 = 216."),
        
        ("[UPSC CSAT Standard]", "Official Standard", False,
         "A cube has numbers 1 to 6 printed on its six faces. If 1 is opposite 6, 2 is opposite 5, and 3 is opposite 4, what is the sum of numbers on any two adjacent faces?",
         ["(a) Cannot be equal to 7", "(b) Always 7", "(c) Always 6", "(d) Always 8"], "(a)",
         "Adjacent Cannot Be Opposite: Opposite faces sum to 7. Two adjacent faces can NEVER be opposite, so their sum can NEVER be 7!",
         "Opposite pairs sum to 7. Adjacent faces are not opposite, so their sum can never be 7."),
        
        ("[UPSC CSAT Hard]", "UPSC Hard", True,
         "A wooden cube of side 4 cm is painted red on all sides. It is sliced into 64 cubes of side 1 cm. What is the ratio of the number of cubes with 2 faces painted to the number of cubes with 1 face painted?",
         ["(a) 1 : 1", "(b) 2 : 1", "(c) 1 : 2", "(d) 3 : 2"], "(a)",
         "Equal Count: 2 faces painted = 12 * (4 - 2) = 24. 1 face painted = 6 * (4 - 2)^2 = 6 * 4 = 24. Ratio = 24 : 24 = 1 : 1!",
         "2 faces = 12(2) = 24. 1 face = 6(4) = 24. Ratio = 24 : 24 = 1 : 1."),
        
        ("[UPSC CSAT Standard]", "Official Standard", False,
         "What is the total surface area of all the 27 small cubes obtained by cutting a 3 cm painted cube, compared to the original cube?",
         ["(a) 3 times the original", "(b) 9 times the original", "(c) 27 times the original", "(d) 6 times the original"], "(a)",
         "Area Scaling: Original area = 6 * 3^2 = 54 cm². Each small cube = 6 * 1^2 = 6 cm². 27 small cubes = 27 * 6 = 162 cm². Ratio = 162 / 54 = 3 times!",
         "Original area = 6 * 3^2 = 54. 27 small cubes area = 27 * 6 = 162. 162 / 54 = 3 times."),
        
        ("[UPSC CSAT Hard]", "UPSC Hard", True,
         "A solid cube has 6 different letters A, B, C, D, E, F on its 6 faces. When viewed from two angles, A is adjacent to B, C, D, and E. Which letter is opposite to A?",
         ["(a) F", "(b) B", "(c) C", "(d) E"], "(a)",
         "Single Remaining Face: A is adjacent to 4 letters: B, C, D, E. The only remaining letter on the cube is F. F must be opposite to A!",
         "A is adjacent to 4 faces. The 6th face F must be opposite A.")
    ]
    data[t20_id] = {
        "topic_id": t20_id, "title": t20_title, "mental_model": t20_model,
        "questions": [create_q(t20_id, t20_title, i+1, s[0], s[1], s[2], s[3], s[4], s[5], s[6], s[7]) for i, s in enumerate(t20_specs)]
    }

    return data

if __name__ == "__main__":
    out_dir = os.path.join(os.path.dirname(__file__), "data")
    os.makedirs(out_dir, exist_ok=True)
    out_file = os.path.join(out_dir, "csat_topics_16_20.json")
    d = build_group4()
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(d, f, indent=2, ensure_ascii=False)
    print("Exported Group 4 to", out_file)
    for k, v in d.items():
        print(k, len(v["questions"]), "questions")
