#!/usr/bin/env python3
"""
fix_csat_curriculum_mapping.py
Ensures every day in data/curriculum-180.json is mapped to its exact, distinct CSAT topic.
Synchronizes csat_micro_topic.topic_id with csat_topic_bank_id so each day card
accurately loads its own dedicated question bank.
"""

import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CURR_FILE = os.path.join(BASE_DIR, "data", "curriculum-180.json")

# Authoritative catalog of all 25 CSAT syllabus topics
CSAT_TOPIC_CATALOG = [
    {
        "topic_id": "csat-01",
        "title": "Number System: Unit Digit Cyclicity & Exponent Powers",
        "ungist_ref": "UNGIST Ch 1 (Pages 8-16)",
        "prob": 98,
        "keywords": "Ferris Wheel Loop, Cyclicity of 2, 3, 7, 8 (Cycle 4), 4 & 9 (Cycle 2), Fixed endings 0, 1, 5, 6",
        "sub_items": [
            "Master the 4-step Ferris Wheel rule: divide the power by 4, the remainder is the effective power",
            "Memorize base cyclicity: 2 (2,4,8,6), 3 (3,9,7,1), 7 (7,9,3,1), 8 (8,4,2,6)",
            "Handle fixed digits: Any power of 0, 1, 5, 6 always ends in the exact same digit",
            "Solve distinct cyclicity variants: factorial sums, large power differences, and unknown digit constraints"
        ]
    },
    {
        "topic_id": "csat-02",
        "title": "Number System: Remainder Theorem & Successive Division",
        "ungist_ref": "UNGIST Ch 2 (Pages 17-29)",
        "prob": 95,
        "keywords": "Elevator Floors, Binomial Remainder (-1)^n, Fermat's Little Theorem, Successive Division",
        "sub_items": [
            "Work backwards from quotient to reconstruct N in successive division",
            "Use (-1)^n and (+1)^n binomial expansions for large powers",
            "Apply Fermat's Little Theorem a^(p-1) = 1 mod p for prime divisors",
            "Solve double divisor remainder questions and LCM(a,b,c)k + r remainder formats"
        ]
    },
    {
        "topic_id": "csat-03",
        "title": "Number System: Divisibility Rules (3, 7, 9, 11, 13, 72, 88, 99)",
        "ungist_ref": "UNGIST Ch 3 (Pages 30-44)",
        "prob": 96,
        "keywords": "Digit Hopscotch, Alternating Sum for 11, Factor Split (72=8x9, 88=8x11), Repunit Numbers",
        "sub_items": [
            "Alternating sum test for 11: difference of odd-place and even-place digits",
            "Composite divisibility: factorize into co-prime pairs (72 = 8x9, 88 = 8x11)",
            "Analyze abcabc repeated blocks: always divisible by 1001 = 7 x 11 x 13",
            "Determine unknown digits x and y in 8-digit and 9-digit UPSC divisibility expressions"
        ]
    },
    {
        "topic_id": "csat-04",
        "title": "Number System: Factors, Multiples & Prime Factorization",
        "ungist_ref": "UNGIST Ch 4 (Pages 45-58)",
        "prob": 92,
        "keywords": "Spice Jars, Total Factors (a+1)(b+1), Sum of Factors, Product of Factors, Co-prime Pairs 2^(k-1)",
        "sub_items": [
            "Prime factorize N = p^a * q^b * r^c and compute total, even, and odd divisors",
            "Compute product of factors using N^(Total/2)",
            "Identify perfect square factor counts using even exponents",
            "Solve HCF and LCM word problems: ringing bells, circular tracks, and paving tiles"
        ]
    },
    {
        "topic_id": "csat-05",
        "title": "Number System: Trailing Zeroes in Factorials & Products",
        "ungist_ref": "UNGIST Ch 5 (Pages 59-70)",
        "prob": 94,
        "keywords": "Shoe Pair Factory, Legendre Formula [N/5]+[N/25], Factorial Zero Jumps, Factorial Addition Bottleneck",
        "sub_items": [
            "Count trailing zeroes via Legendre's formula [N/5] + [N/25] + [N/125]",
            "Determine bottleneck in products where powers of 2 are scarce",
            "Solve factorial sum zeroes: minimum factorial dictates the trailing zeroes count",
            "Identify why certain trailing zero counts (e.g. 29, 30) can never exist"
        ]
    },
    {
        "topic_id": "csat-06",
        "title": "Percentages: The ₹100 Bill Method & Fraction-Percentage Ladder",
        "ungist_ref": "UNGIST Ch 6 (Pages 71-84)",
        "prob": 96,
        "keywords": "₹100 Bill Anchor, Fraction Ladder (1/6=16.67%, 1/7=14.28%), Price-Consumption Reduction",
        "sub_items": [
            "Anchor unknown base quantities to ₹100 for instant mental calculation",
            "Apply price-consumption trade-off: r/(100+r) * 100",
            "Solve voting and election margin problems with valid and invalid votes",
            "Calculate passing marks and deficit/surplus percentages in exam cohorts"
        ]
    },
    {
        "topic_id": "csat-07",
        "title": "Percentages: Successive Changes, Population & Compounding",
        "ungist_ref": "UNGIST Ch 7 (Pages 85-98)",
        "prob": 93,
        "keywords": "Net % = a + b + ab/100, Equal Rise and Fall Loss (x^2/100), Population Growth, Area Dimension Changes",
        "sub_items": [
            "Apply net percentage change formula a + b + (ab/100)",
            "Recognize equal % rise and % drop always produces a net loss of x^2/100",
            "Calculate geometric population growth and depreciation over multi-year horizons",
            "Compute 2D and 3D geometric dimension shifts (rectangle area, sphere volume)"
        ]
    },
    {
        "topic_id": "csat-08",
        "title": "Profit and Loss: Markup, Discounts & Faulty Balances",
        "ungist_ref": "UNGIST Ch 8 (Pages 99-114)",
        "prob": 95,
        "keywords": "Vendor Scale Fraud, Error/(True-Error) * 100, Successive Discounts, Selling at Cost Price Trap",
        "sub_items": [
            "Calculate fraudulent weight profit: [Error / (True Weight - Error)] * 100",
            "Compute marked price markup and successive discount equivalents",
            "Solve two-article sale at identical SP with equal gain% and loss% (net loss x^2/100)",
            "Calculate dishonest merchant mixing adulterants with cost price sales"
        ]
    },
    {
        "topic_id": "csat-09",
        "title": "Averages: The Playground Seesaw Balancing Scale & Cricket Innings",
        "ungist_ref": "UNGIST Ch 9 (Pages 115-128)",
        "prob": 94,
        "keywords": "Seesaw Deviation Balancing, Innings Average Jump, Candidate Replacement, Wrong Score Rectification",
        "sub_items": [
            "Balance net positive deviations against net negative deviations",
            "Rectify incorrectly transcribed scores using net change / total count",
            "Calculate batsman average shifts before and after a milestone innings",
            "Determine weight/age of new entrant replacing an existing cohort member"
        ]
    },
    {
        "topic_id": "csat-10",
        "title": "Ratio and Proportion, Mixtures & Alligation Cross",
        "ungist_ref": "UNGIST Ch 10 (Pages 129-144)",
        "prob": 95,
        "keywords": "Alligation Diagonal Cross, Repeated Replacement V(1 - x/V)^n, Alloy Mixing, Milk-Water Dilution",
        "sub_items": [
            "Solve diagonal alligation: (Dearer - Mean) / (Mean - Cheaper)",
            "Apply repeated removal and replacement formula: Final = Initial * (1 - x/V)^n",
            "Combine two alloys with different constituent ratios into a unified mixture",
            "Determine volume of water added to alter concentration from A:B to C:D"
        ]
    },
    {
        "topic_id": "csat-11",
        "title": "Time and Work: The LCM Brick Wall & Alternate Days",
        "ungist_ref": "UNGIST Ch 11 (Pages 145-160)",
        "prob": 97,
        "keywords": "Brick Wall LCM, Daily Unit Efficiencies, Alternate Days 2-Day Cycle, Men-Women Equivalence",
        "sub_items": [
            "Set total work equal to LCM of days and calculate individual daily brick outputs",
            "Solve alternate-day work cycles: determine full 2-day cycles and remaining fractions",
            "Handle workers leaving or joining midway through project execution",
            "Equate multi-category labor forces: m Men = w Women = c Children"
        ]
    },
    {
        "topic_id": "csat-12",
        "title": "Pipes and Cisterns: Inlets vs Outlets & Leaks",
        "ungist_ref": "UNGIST Ch 12 (Pages 161-174)",
        "prob": 93,
        "keywords": "Bathtub Inflow-Outflow, Net Rate = Inlets - Leaks, Alternating Taps, Emptying Rate",
        "sub_items": [
            "Assign positive units to filling inlets and negative units to draining outlets",
            "Calculate leak emptying rate when combined with an active inflow tap",
            "Determine time taken when pipes operate on alternating 1-hour shifts",
            "Compute tank capacity given inflow rate in liters per minute"
        ]
    },
    {
        "topic_id": "csat-13",
        "title": "Time, Speed & Distance: 5/18 Converter & Harmonic Average Speed",
        "ungist_ref": "UNGIST Ch 13 (Pages 175-192)",
        "prob": 97,
        "keywords": "Harmonic Mean 2xy/(x+y), 5/18 m/s Converter, Late-Early Arrival Equations, Relative Chase Speed",
        "sub_items": [
            "Apply harmonic mean 2xy/(x+y) for round trips over identical distances",
            "Solve late-early arrival problems: s1(t + t1) = s2(t - t2)",
            "Calculate linear pursuit: relative speed = s1 - s2 for same direction chase",
            "Compute post-meeting travel times using speed ratio s1/s2 = sqrt(t2/t1)"
        ]
    },
    {
        "topic_id": "csat-14",
        "title": "Trains: Crossing Poles vs Platforms & Relative Speeds",
        "ungist_ref": "UNGIST Ch 14 (Pages 193-208)",
        "prob": 96,
        "keywords": "Moving Bridge, Distance = L (Pole) vs L + P (Platform), Opposite Directions Add Speeds, Passenger Crossing",
        "sub_items": [
            "Crossing stationary point object (pole, person): distance = train length L",
            "Crossing extended object (platform, bridge): distance = train length L + platform length P",
            "Two trains crossing in opposite directions: distance = L1 + L2, relative speed = s1 + s2",
            "Faster train crossing a passenger seated in slower train: distance = length of faster train"
        ]
    },
    {
        "topic_id": "csat-15",
        "title": "Boats and Streams: Upstream vs Downstream",
        "ungist_ref": "UNGIST Ch 15 (Pages 209-222)",
        "prob": 94,
        "keywords": "Airport Travelator, Downstream D = B + S, Upstream U = B - S, Boat Speed B = (D+U)/2, Stream S = (D-U)/2",
        "sub_items": [
            "Downstream speed D = Boat speed B + Stream speed S",
            "Upstream speed U = Boat speed B - Stream speed S",
            "Solve for boat in still water B = (D + U)/2 and current speed S = (D - U)/2",
            "Calculate round-trip journey time over distance d: t = d/(B+S) + d/(B-S)"
        ]
    },
    {
        "topic_id": "csat-16",
        "title": "Permutations & Combinations: Handshake Theorem, Tie Method & Gap Method",
        "ungist_ref": "UNGIST Ch 16 (Pages 223-242)",
        "prob": 98,
        "keywords": "Handshake n(n-1)/2, Tie Method for Together Items, Gap Method for Never Together, Committee Constraints",
        "sub_items": [
            "Apply handshake theorem: n people shaking hands = n(n-1)/2",
            "Tie method: bind items that must remain contiguous into one super-item",
            "Gap method: arrange unconstrained items first, then seat restricted items in gaps",
            "Select committees with 'at least one' constraint using total minus prohibited cases"
        ]
    },
    {
        "topic_id": "csat-17",
        "title": "Probability: Complementary Odds, Dice, Bags & Coins",
        "ungist_ref": "UNGIST Ch 17 (Pages 243-258)",
        "prob": 95,
        "keywords": "Complementary P(at least 1) = 1 - P(none), Independent Events, Marbles Without Replacement, Sum of Dice",
        "sub_items": [
            "Apply complementary probability: P(at least one success) = 1 - P(zero successes)",
            "Calculate outcomes for two dice: sum is prime, sum is at least 9, doubles",
            "Compute drawing marbles/balls from urns without replacement",
            "Calculate leap year having 53 Sundays / 53 Mondays probability"
        ]
    },
    {
        "topic_id": "csat-18",
        "title": "Clocks: Angle Formula |30H - 5.5M|, Overlaps & Gaining/Losing Clocks",
        "ungist_ref": "UNGIST Ch 18 (Pages 259-272)",
        "prob": 93,
        "keywords": "Tortoise & Hare, Angle = |30H - 5.5M|, 22 Overlaps per Day, 44 Right Angles per Day, Faulty Gain/Loss Clock",
        "sub_items": [
            "Apply clock angle formula: Angle = |30H - 5.5M|",
            "Calculate exact minute when hands coincide (0 deg), oppose (180 deg), or right angle (90 deg)",
            "Memorize 24-hour frequencies: 22 overlaps, 22 opposite hands, 44 right angles",
            "Solve faulty clock gaining or losing x seconds per hour"
        ]
    },
    {
        "topic_id": "csat-19",
        "title": "Calendar: The 7-Day Cycle, Odd Days & Century Repeats",
        "ungist_ref": "UNGIST Ch 19 (Pages 273-286)",
        "prob": 94,
        "keywords": "7-Day Wheel, Ordinary Year = 1 Odd Day, Leap Year = 2 Odd Days, 400 Years = 0 Odd Days, Calendar Repeats",
        "sub_items": [
            "Count odd days: ordinary year has 1 odd day; leap year has 2 odd days",
            "Determine century odd days: 100 yrs = 5, 200 yrs = 3, 300 yrs = 1, 400 yrs = 0",
            "Calculate day of the week for historical dates (15 Aug 1947, 26 Jan 1950)",
            "Identify repeating calendar years: leap year repeats in 28 yrs, leap+1 in 6 yrs"
        ]
    },
    {
        "topic_id": "csat-20",
        "title": "Cubes and Dice: Opposite Faces & Cut Painted Cubes",
        "ungist_ref": "UNGIST Ch 20 (Pages 287-300)",
        "prob": 92,
        "keywords": "Rubik's Layers, 3-Face=8, 2-Face=12(n-2), 1-Face=6(n-2)^2, 0-Face=(n-2)^3, Unfolded Dice Opposite Faces",
        "sub_items": [
            "Count painted faces in n x n x n cut cube: 3-face=8, 2-face=12(n-2), 1-face=6(n-2)^2, 0-face=(n-2)^3",
            "Identify opposite faces on unfolded cross-shaped dice nets",
            "Determine minimum plane cuts needed to partition a solid into k pieces",
            "Solve multi-color painted cube faces with adjacent color constraints"
        ]
    },
    {
        "topic_id": "csat-21",
        "title": "Blood Relations: Generation Family Tree Mapping & Coded Relations",
        "ungist_ref": "UNGIST Ch 21 (Pages 301-316)",
        "prob": 96,
        "keywords": "Generation Ladder, Vertical Generation Links, Horizontal Sibling Links, Double Spouse Lines, Coded Relations",
        "sub_items": [
            "Construct multi-generation family tree diagrams with gender markers",
            "Decode pointing problems: 'He is the only son of my father's sister...'",
            "Solve coded symbol equations: P + Q means P is mother of Q, P x Q means P is brother",
            "Establish relationships in complex 6-8 member joint families with dual professions"
        ]
    },
    {
        "topic_id": "csat-22",
        "title": "Direction Sense: 8-Point Compass & Pythagoras Trajectory",
        "ungist_ref": "UNGIST Ch 22 (Pages 317-332)",
        "prob": 95,
        "keywords": "Right Triangle Displacement, Euclidean Distance sqrt(N^2 + E^2), Clockwise Rotation, Sunset Shadow Rule",
        "sub_items": [
            "Track turns on 8-point compass: North, South, East, West, NE, NW, SE, SW",
            "Calculate net Euclidean displacement using Pythagoras theorem: sqrt(Delta X^2 + Delta Y^2)",
            "Solve shadow problems at sunrise (shadow points West) and sunset (shadow points East)",
            "Handle compass rotation transformations (e.g. if North-East becomes South)"
        ]
    },
    {
        "topic_id": "csat-23",
        "title": "Syllogisms: Mom & Baby Venn Circles & Either-Or Rules",
        "ungist_ref": "UNGIST Ch 23 (Pages 333-350)",
        "prob": 97,
        "keywords": "Mom & Baby Kangaroo Venn, All A are B, Some A are B, No A is B, Complementary Either-Or Pair",
        "sub_items": [
            "Draw Euler/Venn circles: All A are B (concentric), Some A are B (overlap), No A is B (disjoint)",
            "Apply negative statement elimination: No A is B precludes any subset of A from touching B",
            "Identify Either-Or complementary pairs: Some P are Q + No P is Q",
            "Evaluate 3-statement and 4-statement complex UPSC syllogism arguments"
        ]
    },
    {
        "topic_id": "csat-24",
        "title": "Seating Arrangements & Complex Puzzles (Linear & Circular)",
        "ungist_ref": "UNGIST Ch 24 (Pages 351-370)",
        "prob": 96,
        "keywords": "Definite Anchor First, Center-Facing vs Outward-Facing, Linear North-South, Ranking & Ordering",
        "sub_items": [
            "Place the person with fixed/unambiguous anchor position first",
            "Distinguish between center-facing (right is counter-clockwise) vs outward-facing (right is clockwise)",
            "Solve linear seating rows facing North or mixed North-South directions",
            "Solve height, weight, and rank ordering puzzles with comparative inequalities"
        ]
    },
    {
        "topic_id": "csat-25",
        "title": "Reading Comprehension: The 4-Step 'Sherlocking' Method (Crux, Corollaries & Assumptions)",
        "ungist_ref": "UNGIST Ch 25 (Pages 371-410)",
        "prob": 99,
        "keywords": "Sherlock Strict Scope, Crux Extraction, Crucial Assumption Implied, Logical Corollary, Trap Elimination",
        "sub_items": [
            "Enforce strict text scope: reject outside general knowledge not grounded in passage",
            "Eliminate extreme distractor words: 'only', 'never', 'all', 'completely', 'prohibit'",
            "Identify unstated logical bridges required for the author's conclusion (Crucial Assumption)",
            "Differentiate between direct factual summary vs author's core philosophical argument (Crux)"
        ]
    }
]

def main():
    if not os.path.exists(CURR_FILE):
        print(f"File {CURR_FILE} not found.")
        return

    with open(CURR_FILE, "r", encoding="utf-8") as f:
        curr = json.load(f)

    print(f"Loaded {len(curr)} days from curriculum.")
    
    # Map each day cleanly across the 25 topics
    for idx, day in enumerate(curr):
        day_num = day.get("day", idx + 1)
        # Cycle through 25 topics cleanly: day 1 -> topic 1, day 25 -> topic 25, day 26 -> topic 1
        topic_idx = (day_num - 1) % len(CSAT_TOPIC_CATALOG)
        topic_meta = CSAT_TOPIC_CATALOG[topic_idx]
        tid = topic_meta["topic_id"]

        # Build sub_items list
        sub_list = [
            {"id": f"csat__d{day_num}_s{s_idx}", "text": text}
            for s_idx, text in enumerate(topic_meta["sub_items"])
        ]

        day["csat_micro_topic"] = {
            "id": f"csat-d{day_num}",
            "topic_id": tid,
            "title": topic_meta["title"],
            "ungist_ref": topic_meta["ungist_ref"],
            "prob": topic_meta["prob"],
            "keywords": topic_meta["keywords"],
            "sub_items": sub_list
        }
        # Synchronize csat_topic_bank_id strictly!
        day["csat_topic_bank_id"] = tid
        day["csat_practice_25_count"] = 26

    with open(CURR_FILE, "w", encoding="utf-8") as f:
        json.dump(curr, f, indent=2, ensure_ascii=False)

    print(f"Successfully updated all 180 days in {CURR_FILE}.")
    
    # Verification
    bank_counts = {}
    for d in curr:
        b = d["csat_topic_bank_id"]
        bank_counts[b] = bank_counts.get(b, 0) + 1
    print("New CSAT Bank ID distribution across 180 days:")
    for tid in sorted(bank_counts.keys()):
        print(f"  {tid}: {bank_counts[tid]} days")

if __name__ == "__main__":
    main()
