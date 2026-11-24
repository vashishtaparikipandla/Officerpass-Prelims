import json
import os

db_path = 'micro-topics/microtopics-db.json'
with open(db_path, 'r') as f:
    db = json.load(f)

csat_micro_catalog = [
    {
        "id": "csat-01",
        "topic": "Number System: Unit Digit Cyclicity & Exponent Powers",
        "prob": 98,
        "tier": 1,
        "pyqs": 28,
        "core_sources": "UNGIST Ch 1 (Pages 8-16)",
        "keywords": "Ferris Wheel Loop, Cyclicity of 2, 3, 7, 8 (Cycle 4), 4 & 9 (Cycle 2), Fixed endings 0, 1, 5, 6",
        "sub_items": [
            {"id": "csat-01__sub-0", "text": "Master the 4-step Ferris Wheel rule: divide the power by 4, the remainder is the effective power"},
            {"id": "csat-01__sub-1", "text": "Memorize base cyclicity: 2 (2,4,8,6), 3 (3,9,7,1), 7 (7,9,3,1), 8 (8,4,2,6)"},
            {"id": "csat-01__sub-2", "text": "Handle fixed digits: Any power of 0, 1, 5, 6 always ends in the exact same digit"},
            {"id": "csat-01__sub-3", "text": "Solve 5 unit digit questions: Find unit digit of 7^95, 3^65, (3^65 x 6^59 x 7^71)"}
        ]
    },
    {
        "id": "csat-02",
        "topic": "Number System: Remainder Theorem & Successive Division",
        "prob": 96,
        "tier": 1,
        "pyqs": 26,
        "core_sources": "UNGIST Ch 1 (Pages 17-28)",
        "keywords": "Successive division remainder reconstruction, Polynomial remainder theorem, Factor cancelation trick",
        "sub_items": [
            {"id": "csat-02__sub-0", "text": "Successive Division Ladder: Work backwards from quotient 1 to reconstruct the original dividend"},
            {"id": "csat-02__sub-1", "text": "Factor cancelation remainder rule: If dividing product (e.g. 85 x 87... by 100), factor out 25 and 4"},
            {"id": "csat-02__sub-2", "text": "Negative Remainders: Use (divisor - remainder) to simplify powers near multiples (e.g. 2^31 / 9)"},
            {"id": "csat-02__sub-3", "text": "Solve 5 UPSC PYQs on remainder of consecutive product and successive division"}
        ]
    },
    {
        "id": "csat-03",
        "topic": "Number System: Divisibility Rules (3, 7, 9, 11, 13)",
        "prob": 95,
        "tier": 1,
        "pyqs": 32,
        "core_sources": "UNGIST Ch 1 (Pages 29-42)",
        "keywords": "Sum of digits (3 & 9), Alternating sum of digits (11), Triple subtraction method (7, 11, 13)",
        "sub_items": [
            {"id": "csat-03__sub-0", "text": "Rule for 3 & 9: Sum of digits must be divisible by 3 or 9"},
            {"id": "csat-03__sub-1", "text": "Rule for 11: Difference between sum of odd-place digits and even-place digits must be 0 or multiple of 11"},
            {"id": "csat-03__sub-2", "text": "Combined Rule for 7, 11, 13: Split number into 3-digit groups from right, alternate signs; difference must divide by 7, 11, or 13"},
            {"id": "csat-03__sub-3", "text": "Solve 5 missing-digit problems: If 481_673 is divisible by 9, find the missing digit"}
        ]
    },
    {
        "id": "csat-04",
        "topic": "Number System: Factors, Multiples & Prime Factorization",
        "prob": 90,
        "tier": 1,
        "pyqs": 22,
        "core_sources": "UNGIST Ch 1 (Pages 43-58)",
        "keywords": "Total factors formula (p+1)(q+1)(r+1), Prime factorization tree, Odd vs Even factors",
        "sub_items": [
            {"id": "csat-04__sub-0", "text": "Break any composite number into prime bases: N = 2^a x 3^b x 5^c"},
            {"id": "csat-04__sub-1", "text": "Total number of factors = (a + 1)(b + 1)(c + 1)"},
            {"id": "csat-04__sub-2", "text": "Number of even factors: a x (b + 1)(c + 1); Number of odd factors: (b + 1)(c + 1)"},
            {"id": "csat-04__sub-3", "text": "Practice finding total and prime factors for 720, 1080, and 1200"}
        ]
    },
    {
        "id": "csat-05",
        "topic": "Number System: Trailing Zeroes in Factorials",
        "prob": 92,
        "tier": 1,
        "pyqs": 18,
        "core_sources": "UNGIST Ch 1 (Pages 59-74)",
        "keywords": "Legendre's formula, 2x5 pair rule, Powers of 5 counting in n!",
        "sub_items": [
            {"id": "csat-05__sub-0", "text": "Understand zero creation: A trailing zero is created ONLY by 2 x 5 = 10"},
            {"id": "csat-05__sub-1", "text": "In any factorial (n!), 2s are plentiful, so number of zeroes is governed entirely by count of 5s"},
            {"id": "csat-05__sub-2", "text": "Legendre's Formula: [n/5] + [n/25] + [n/125] + [n/625]... (integer quotients only)"},
            {"id": "csat-05__sub-3", "text": "Calculate trailing zeroes for 100! (24 zeroes), 200! (49 zeroes), and 500! (124 zeroes)"}
        ]
    },
    {
        "id": "csat-06",
        "topic": "Percentages: The ₹100 Bill Method & Fraction Ladder",
        "prob": 95,
        "tier": 1,
        "pyqs": 45,
        "core_sources": "UNGIST Ch 6 (Pages 119-140)",
        "keywords": "Base 100 substitution, Fraction ladder (1/6 = 16.66%, 1/8 = 12.5%), Price vs Consumption inverse balance",
        "sub_items": [
            {"id": "csat-06__sub-0", "text": "Never assume 'x': Always set the original unknown quantity to ₹100"},
            {"id": "csat-06__sub-1", "text": "Master the Fraction Ladder: 1/2=50%, 1/3=33.3%, 1/4=25%, 1/5=20%, 1/6=16.67%, 1/7=14.28%, 1/8=12.5%"},
            {"id": "csat-06__sub-2", "text": "Price-Consumption Inverse Rule: If price goes UP by 1/n, consumption must drop by 1/(n+1) to keep budget constant"},
            {"id": "csat-06__sub-3", "text": "Solve 5 problems: Petrol price rises by 25%, sugar price drops by 20%"}
        ]
    },
    {
        "id": "csat-07",
        "topic": "Percentages: Successive Changes & Population Growth",
        "prob": 90,
        "tier": 1,
        "pyqs": 28,
        "core_sources": "UNGIST Ch 6 (Pages 141-158)",
        "keywords": "Formula a + b + ab/100, Compounding vs simple percentage change, Area expansion problems",
        "sub_items": [
            {"id": "csat-07__sub-0", "text": "Net Change Formula: Net % = a + b + (ab/100) (use negative sign for discounts/reductions)"},
            {"id": "csat-07__sub-1", "text": "Rectangle Area Effect: Length +20%, Breadth -10% -> Net area change = +20 - 10 + (-200/100) = +8%"},
            {"id": "csat-07__sub-2", "text": "Two successive discounts of 10% and 20%: -10 - 20 + 200/100 = -28% (Single equivalent discount 28%)"},
            {"id": "csat-07__sub-3", "text": "Solve 5 UPSC successive percentage problems"}
        ]
    },
    {
        "id": "csat-08",
        "topic": "Profit and Loss: Markup, Discounts & Faulty Balances",
        "prob": 92,
        "tier": 1,
        "pyqs": 35,
        "core_sources": "UNGIST Ch 7 (Pages 159-172)",
        "keywords": "Cost Price (CP) vs Selling Price (SP) vs Marked Price (MP), Dishonest shopkeeper formula",
        "sub_items": [
            {"id": "csat-08__sub-0", "text": "Distinguish bases: Profit/Loss is ALWAYS on CP; Discount is ALWAYS on Marked Price (MP)"},
            {"id": "csat-08__sub-1", "text": "Equal Selling Price Trap: Two items sold at same SP, one at x% profit and other at x% loss -> Always a net loss of (x/10)^2 %"},
            {"id": "csat-08__sub-2", "text": "Dishonest Dealer Weight Fraud: Profit % = [Error / (True Value - Error)] x 100"},
            {"id": "csat-08__sub-3", "text": "Solve 5 profit & loss problems with ₹100 base substitution"}
        ]
    },
    {
        "id": "csat-09",
        "topic": "Averages: The Playground Seesaw Balancing Scale",
        "prob": 94,
        "tier": 1,
        "pyqs": 40,
        "core_sources": "UNGIST Ch 5 (Pages 107-118)",
        "keywords": "Deviation from assumed mean, Inclusion/Exclusion of teacher, Replacement shortcut",
        "sub_items": [
            {"id": "csat-09__sub-0", "text": "Average as Seesaw Fulcrum: Total surplus above mean must exactly balance total deficit below mean"},
            {"id": "csat-09__sub-1", "text": "Newcomer Joins Shortcut: Extra brought = (New Total Count) x (Increase in Average)"},
            {"id": "csat-09__sub-2", "text": "Replacement Formula: New person weight = Old person weight + (Count x Change in Average)"},
            {"id": "csat-09__sub-3", "text": "Solve 5 average age and cricket score problems mentally without multiplying large numbers"}
        ]
    },
    {
        "id": "csat-10",
        "topic": "Ratio and Proportion, Mixtures & Alligation",
        "prob": 90,
        "tier": 1,
        "pyqs": 36,
        "core_sources": "UNGIST Ch 2 & 3 (Pages 75-98)",
        "keywords": "The Cross Alligation Diagram, Repeated replacement formula, Mean proportional",
        "sub_items": [
            {"id": "csat-10__sub-0", "text": "The Alligation Cross: (Cheaper Price) (Dearer Price) -> Mean Price in center -> Cross-subtract to get quantity ratio"},
            {"id": "csat-10__sub-1", "text": "Repeated Replacement Formula: Final Pure Liquid = Initial Liquid x (1 - x / V)^n"},
            {"id": "csat-10__sub-2", "text": "Ratio scaling trick: To combine A:B = 2:3 and B:C = 4:5, multiply to make B equal (8:12:15)"},
            {"id": "csat-10__sub-3", "text": "Solve 5 mixture and milk-water replacement problems"}
        ]
    },
    {
        "id": "csat-11",
        "topic": "Time and Work: The LCM Total-Units Method",
        "prob": 96,
        "tier": 1,
        "pyqs": 42,
        "core_sources": "UNGIST Ch 11 (Pages 199-219)",
        "keywords": "Total cookies LCM method, Efficiency rates, Alternate day work cycles",
        "sub_items": [
            {"id": "csat-11__sub-0", "text": "Step 1: Set Total Work = LCM of given days (Never use 1/12 + 1/18 fractions!)"},
            {"id": "csat-11__sub-1", "text": "Step 2: Find daily cookie baking rate (Efficiency = Total Work / Days)"},
            {"id": "csat-11__sub-2", "text": "Alternate Day Cycle: Sum work done in a 2-day cycle, find completed cycles, divide remaining cookies"},
            {"id": "csat-11__sub-3", "text": "Solve 5 work problems: A in 10 days, B in 15 days, working together vs alternate days"}
        ]
    },
    {
        "id": "csat-12",
        "topic": "Pipes and Cisterns: Inlets vs Outlets",
        "prob": 88,
        "tier": 1,
        "pyqs": 24,
        "core_sources": "UNGIST Ch 12 (Pages 220-229)",
        "keywords": "Inlet positive work (+), Leak/Outlet negative work (-), Capacity LCM method",
        "sub_items": [
            {"id": "csat-12__sub-0", "text": "Total Tank Capacity = LCM of filling and emptying times"},
            {"id": "csat-12__sub-1", "text": "Inlet pipe is (+) rate units/hour; Leak / waste pipe is (-) rate units/hour"},
            {"id": "csat-12__sub-2", "text": "Net rate = (Inlet rate) - (Leak rate); Time to fill = Total Capacity / Net rate"},
            {"id": "csat-12__sub-3", "text": "Solve 5 tank filling problems with simultaneous leaks"}
        ]
    },
    {
        "id": "csat-13",
        "topic": "Time, Speed & Distance: 5/18 Converter & Harmonic Average Speed",
        "prob": 94,
        "tier": 1,
        "pyqs": 38,
        "core_sources": "UNGIST Ch 8 (Pages 173-185)",
        "keywords": "km/h to m/s conversion x 5/18, Average speed 2xy/(x+y), Relative speed same vs opposite",
        "sub_items": [
            {"id": "csat-13__sub-0", "text": "The Unit Converter: km/h -> m/s multiply by 5/18. Multiples: 18km/h=5m/s, 36=10, 54=15, 72=20, 90=25"},
            {"id": "csat-13__sub-1", "text": "Average Speed for equal distance trips = 2xy / (x + y) (Harmonic mean, never arithmetic mean!)"},
            {"id": "csat-13__sub-2", "text": "Relative Speed: Moving towards each other = S1 + S2; Moving in same direction = S1 - S2"},
            {"id": "csat-13__sub-3", "text": "Solve 5 speed-time-distance problems with unit conversions"}
        ]
    },
    {
        "id": "csat-14",
        "topic": "Trains: Crossing Poles vs Platforms & Relative Speed",
        "prob": 92,
        "tier": 1,
        "pyqs": 30,
        "core_sources": "UNGIST Ch 9 (Pages 186-192)",
        "keywords": "Crossing pole (Distance = Train length), Crossing platform (Distance = Train + Platform), Parallel tracks",
        "sub_items": [
            {"id": "csat-14__sub-0", "text": "Crossing Pole / Man / Tree: Distance covered = Length of Train only (pole width is zero)"},
            {"id": "csat-14__sub-1", "text": "Crossing Platform / Bridge / Tunnel: Distance covered = Train Length + Platform Length"},
            {"id": "csat-14__sub-2", "text": "Two Trains Crossing Each Other: Distance = Train1 + Train2; Speed = S1 + S2 (Opposite) or S1 - S2 (Same)"},
            {"id": "csat-14__sub-3", "text": "Solve 5 train crossing problems under 60 seconds each"}
        ]
    },
    {
        "id": "csat-15",
        "topic": "Boats and Streams: Upstream vs Downstream",
        "prob": 85,
        "tier": 1,
        "pyqs": 18,
        "core_sources": "UNGIST Ch 10 (Pages 193-198)",
        "keywords": "Downstream speed (u + v), Upstream speed (u - v), Still water speed (D + U)/2",
        "sub_items": [
            {"id": "csat-15__sub-0", "text": "Downstream Speed D = u + v (Stream aids the boat)"},
            {"id": "csat-15__sub-1", "text": "Upstream Speed U = u - v (Stream opposes the boat)"},
            {"id": "csat-15__sub-2", "text": "Speed of Boat in still water u = (D + U) / 2; Speed of Stream v = (D - U) / 2"},
            {"id": "csat-15__sub-3", "text": "Solve 5 boat round-trip and stream rate problems"}
        ]
    },
    {
        "id": "csat-16",
        "topic": "Permutations & Combinations: Handshake Theorem & Tie/Gap Tricks",
        "prob": 95,
        "tier": 1,
        "pyqs": 44,
        "core_sources": "UNGIST Ch 13 (Pages 230-254)",
        "keywords": "Fundamental counting principle, Handshakes n(n-1)/2, Tie method (keep together), Gap method (never together)",
        "sub_items": [
            {"id": "csat-16__sub-0", "text": "Permutation = Arranging in line (order matters); Combination = Selecting team (order irrelevant)"},
            {"id": "csat-16__sub-1", "text": "Handshake Theorem: n people shaking hands once = n(n - 1) / 2"},
            {"id": "csat-16__sub-2", "text": "Tie Method (Must be together): Pack items in 1 bag, arrange external items, multiply by internal permutations"},
            {"id": "csat-16__sub-3", "text": "Gap Method (Never together): Place unrestricted items first, place restricted items in the gaps"},
            {"id": "csat-16__sub-4", "text": "Solve 5 arrangements of boys & girls and committee selections"}
        ]
    },
    {
        "id": "csat-17",
        "topic": "Probability: Basic Events, Dice, Coins & Independent Odds",
        "prob": 90,
        "tier": 1,
        "pyqs": 26,
        "core_sources": "UNGIST Ch 14 (Pages 255-270)",
        "keywords": "P(E) = Favorable / Total, Independent events P(A and B) = P(A) x P(B), Complementary P(not E) = 1 - P(E)",
        "sub_items": [
            {"id": "csat-17__sub-0", "text": "Basic Probability = Number of Favorable Outcomes / Total Sample Space"},
            {"id": "csat-17__sub-1", "text": "At Least One Event: P(At least one) = 1 - P(None happen)"},
            {"id": "csat-17__sub-2", "text": "Independent Events: P(A and B) = P(A) x P(B)"},
            {"id": "csat-17__sub-3", "text": "Solve 5 probability problems: 2 dice sum of 7, coin toss sequences, card draws"}
        ]
    },
    {
        "id": "csat-18",
        "topic": "Clocks: Angle Formula & Overlap Points",
        "prob": 88,
        "tier": 1,
        "pyqs": 22,
        "core_sources": "UNGIST Ch 18 (Pages 297-304)",
        "keywords": "Angle formula |30H - 5.5M|, 11 overlaps in 12 hours, 22 right angles in 12 hours",
        "sub_items": [
            {"id": "csat-18__sub-0", "text": "Universal Angle Formula: Angle = |30H - (11/2)M| degrees"},
            {"id": "csat-18__sub-1", "text": "Relative Speed of Hands: Minute hand 6 deg/min, Hour hand 0.5 deg/min -> Relative speed 5.5 deg/min"},
            {"id": "csat-18__sub-2", "text": "Coinciding Hands: Overlap happens every 65 5/11 minutes (11 times in 12 hours, 22 times in 24 hours)"},
            {"id": "csat-18__sub-3", "text": "Calculate angle at 3:40, 7:20, 8:30, and find when hands overlap between 4 and 5"}
        ]
    },
    {
        "id": "csat-19",
        "topic": "Calendar: The 7-Day Cycle & Odd Days Calculation",
        "prob": 90,
        "tier": 1,
        "pyqs": 25,
        "core_sources": "UNGIST Ch 19 (Pages 305-309)",
        "keywords": "7-day loop remainder, Ordinary year = 1 odd day, Leap year = 2 odd days, Century odd days",
        "sub_items": [
            {"id": "csat-19__sub-0", "text": "Odd Days = Remainder after dividing total days by 7"},
            {"id": "csat-19__sub-1", "text": "Year shift: Ordinary year shifts day by +1; Leap year (has Feb 29) shifts day by +2"},
            {"id": "csat-19__sub-2", "text": "Century Odd Days: 100 years = 5 odd days; 200 years = 3; 300 years = 1; 400 years = 0"},
            {"id": "csat-19__sub-3", "text": "Calculate day of the week for any historical or future date"}
        ]
    },
    {
        "id": "csat-20",
        "topic": "Cubes and Dice: Opposite Faces & Cut Painted Cubes",
        "prob": 82,
        "tier": 1,
        "pyqs": 16,
        "core_sources": "UNGIST Ch 20 (Pages 310-317)",
        "keywords": "Standard vs General dice, Unfolded cross dice opposite faces, Painted cube cutting formulas",
        "sub_items": [
            {"id": "csat-20__sub-0", "text": "Unfolded Dice Rule: Alternate faces in the same row/column are opposite to each other (skip 1 square)"},
            {"id": "csat-20__sub-1", "text": "Painted Cube Cut into n x n x n small cubes: Corner cubes (3 painted) = 8 always"},
            {"id": "csat-20__sub-2", "text": "Middle edge cubes (2 painted) = 12(n - 2); Face center cubes (1 painted) = 6(n - 2)^2; Inner core (0 painted) = (n - 2)^3"},
            {"id": "csat-20__sub-3", "text": "Solve 5 unfolded dice and painted cube problems"}
        ]
    },
    {
        "id": "csat-21",
        "topic": "Blood Relations: Generation Family Tree Mapping",
        "prob": 88,
        "tier": 1,
        "pyqs": 28,
        "core_sources": "UNGIST Ch 21 (Pages 318-322)",
        "keywords": "Generation level vertical mapping, Gender symbols (+ for male, - for female), Marriage '=' sign",
        "sub_items": [
            {"id": "csat-21__sub-0", "text": "Draw generations vertically: Grandparents on top, Parents middle, Children below"},
            {"id": "csat-21__sub-1", "text": "Use crisp symbols: (+) for Male, (-) for Female, (=) for Husband-Wife, (---) for Siblings"},
            {"id": "csat-21__sub-2", "text": "Break down long statements backwards: 'He is the son of the only daughter of my mother'"},
            {"id": "csat-21__sub-3", "text": "Solve 5 complex family relation deduction puzzles"}
        ]
    },
    {
        "id": "csat-22",
        "topic": "Direction Sense: 8-Point Compass & Pythagoras Trajectory",
        "prob": 86,
        "tier": 1,
        "pyqs": 24,
        "core_sources": "UNGIST Ch 22 (Pages 323-327)",
        "keywords": "8-point compass, Pythagoras distance sqrt(a^2 + b^2), Left/Right turns facing South",
        "sub_items": [
            {"id": "csat-22__sub-0", "text": "The 8-point compass: North, South, East, West, NE, NW, SE, SW"},
            {"id": "csat-22__sub-1", "text": "Inverted turns: When walking South, turning RIGHT moves towards West; turning LEFT moves towards East"},
            {"id": "csat-22__sub-2", "text": "Shortest Distance = Pythagoras formula sqrt(x^2 + y^2) (Look for 3-4-5 and 5-12-13 triangles)"},
            {"id": "csat-22__sub-3", "text": "Solve 5 multi-turn walking trajectory problems"}
        ]
    },
    {
        "id": "csat-23",
        "topic": "Syllogisms: Mom & Baby Venn Circles & Either-Or Rules",
        "prob": 92,
        "tier": 1,
        "pyqs": 38,
        "core_sources": "UNGIST Ch 32 (Pages 366-371)",
        "keywords": "All A are B (inner circle), Some A are B (overlap), No A is B (disjoint), Complementary pairs",
        "sub_items": [
            {"id": "csat-23__sub-0", "text": "'All A are B': Draw Circle A completely inside Circle B. Anything in A is in B"},
            {"id": "csat-23__sub-1", "text": "'Some A are B': Draw overlapping circles with shared slice"},
            {"id": "csat-23__sub-2", "text": "The Golden Test: A conclusion follows ONLY if it holds in EVERY single valid diagram you can draw"},
            {"id": "csat-23__sub-3", "text": "Complementary Pair (Either-Or): When conclusions are 'Some A are B' and 'No A is B', neither certain alone"},
            {"id": "csat-23__sub-4", "text": "Solve 5 syllogism questions with 3 statements and 3 conclusions"}
        ]
    },
    {
        "id": "csat-24",
        "topic": "Seating Arrangements & Complex Puzzles",
        "prob": 88,
        "tier": 1,
        "pyqs": 32,
        "core_sources": "UNGIST Ch 30 & 33 (Pages 357-361, 372-384)",
        "keywords": "Linear row facing North/South, Circular table facing center vs facing out, Cross-grid matrix",
        "sub_items": [
            {"id": "csat-24__sub-0", "text": "Linear Row: Facing North -> your right is their right; Facing South -> directions reversed"},
            {"id": "csat-24__sub-1", "text": "Circular Table facing center: Clockwise is Left, Anti-clockwise is Right"},
            {"id": "csat-24__sub-2", "text": "Grid Matrix: Plot definite clues first (X is lawyer living on floor 3), never assume possibilities early"},
            {"id": "csat-24__sub-3", "text": "Solve 5 linear and circular seating arrangement puzzles"}
        ]
    },
    {
        "id": "csat-25",
        "topic": "Reading Comprehension: The 4-Step 'Sherlocking' Method",
        "prob": 100,
        "tier": 1,
        "pyqs": 180,
        "core_sources": "Official UPSC CSAT PYQs (2018-2024)",
        "keywords": "50+ Marks RC, Question First, Sentence Anchor, Murder Extreme Words, Modest Claim Selection",
        "sub_items": [
            {"id": "csat-25__sub-0", "text": "Step 1: Read Question Stem FIRST — Identify if hunting for 'Critical Assumption', 'Corollary', or 'Crux'"},
            {"id": "csat-25__sub-1", "text": "Step 2: Scan passage for the exact sentence anchor containing question keywords"},
            {"id": "csat-25__sub-2", "text": "Step 3: Murder Extreme Words — Eliminate options containing 'always', 'never', 'solely', 'only', 'banned', 'entirely'"},
            {"id": "csat-25__sub-3", "text": "Step 4: Pick Modest Claim — Correct answers use cautious phrasing ('may', 'can', 'contributes to')"},
            {"id": "csat-25__sub-4", "text": "Practice 5 UPSC official passages using the 4-step Sherlocking method"}
        ]
    }
]

db['CSAT_MicroTopics'] = csat_micro_catalog
with open(db_path, 'w') as f:
    json.dump(db, f, indent=2)

print(f"Successfully enriched {db_path} with {len(csat_micro_catalog)} granular CSAT microtopics.")
