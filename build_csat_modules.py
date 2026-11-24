import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CSAT_DIR = os.path.join(BASE_DIR, 'csat')
os.makedirs(CSAT_DIR, exist_ok=True)

modules = [
    {
        "id": "csat-mod-01",
        "title": "Number System: Unit Digit Cyclicity & Trailing Zeroes",
        "ungist_ref": "UNGIST Chapter 1 (Pages 8-24)",
        "difficulty": "Easy to Moderate (Guaranteed 5-8 Marks in CSAT)",
        "child_concept": "Imagine a clock with only 4 numbers (1, 2, 3, 4). When you multiply a number by itself repeatedly, the last digit gets stuck in a repeating Ferris wheel loop that resets every 4 spins!",
        "cyclicity_table": [
            {"base": "2", "cycle": "2 -> 4 -> 8 -> 6", "length": 4, "rule": "Divide power by 4: rem 1=2, rem 2=4, rem 3=8, rem 0=6"},
            {"base": "3", "cycle": "3 -> 9 -> 7 -> 1", "length": 4, "rule": "Divide power by 4: rem 1=3, rem 2=9, rem 3=7, rem 0=1"},
            {"base": "4", "cycle": "4 -> 6", "length": 2, "rule": "Odd power = 4, Even power = 6"},
            {"base": "7", "cycle": "7 -> 9 -> 3 -> 1", "length": 4, "rule": "Divide power by 4: rem 1=7, rem 2=9, rem 3=3, rem 0=1"},
            {"base": "8", "cycle": "8 -> 4 -> 2 -> 6", "length": 4, "rule": "Divide power by 4: rem 1=8, rem 2=4, rem 3=2, rem 0=6"},
            {"base": "9", "cycle": "9 -> 1", "length": 2, "rule": "Odd power = 9, Even power = 1"},
            {"base": "0, 1, 5, 6", "cycle": "Never changes", "length": 1, "rule": "Always ends in the exact same digit!"}
        ],
        "trailing_zeroes_rule": "Trailing zeroes are born when a 2 marries a 5 (2 x 5 = 10). In factorials (like 100!), there are always way more 2s than 5s. So simply count the 5s using Legendre's Formula: [n/5] + [n/25] + [n/125]...",
        "mental_shortcuts": [
            "To find the unit digit of 7^95: Divide 95 by 4. 95 = 23 x 4 + 3. Remainder is 3. The 3rd step in 7's wheel is 7^3 = 343 -> Unit digit is 3!",
            "How many zeroes in 100! ? 100/5 = 20; 100/25 = 4; Total = 20 + 4 = 24 trailing zeroes!"
        ],
        "pyq_walkthrough": {
            "question": "UPSC CSAT 2023: What is the remainder when (85 x 87 x 89 x 91 x 95 x 96) is divided by 100?",
            "step1_child_logic": "100 = 4 x 25. Let's look for factors of 4 and 25 inside the numbers.",
            "step2_working": "85 = 5 x 17; 95 = 5 x 19. Notice 5 x 5 = 25! So 25 is present.\nNow 96 = 4 x 24. So 4 is present!\nSince the product contains both 25 and 4, it contains 25 x 4 = 100 as a factor.",
            "step3_answer": "Since 100 divides the number completely, the remainder is ZERO! Solved in 10 seconds without multiplying a single large number."
        }
    },
    {
        "id": "csat-mod-02",
        "title": "Percentages & Profit-Loss: The ₹100 Bill Method",
        "ungist_ref": "UNGIST Chapter 6 & 7 (Pages 119-172)",
        "difficulty": "Easy (Guaranteed 6-10 Marks)",
        "child_concept": "Forget algebraic x and y! Whenever a problem talks in percentages, pretend you have a ₹100 note in your pocket. ₹100 makes every percentage calculation as simple as counting single rupee coins.",
        "fraction_ladder": [
            {"fraction": "1/2", "percent": "50%"},
            {"fraction": "1/3", "percent": "33.33%"},
            {"fraction": "1/4", "percent": "25%"},
            {"fraction": "1/5", "percent": "20%"},
            {"fraction": "1/6", "percent": "16.66%"},
            {"fraction": "1/7", "percent": "14.28%"},
            {"fraction": "1/8", "percent": "12.5%"}
        ],
        "mental_shortcuts": [
            "The Up-Down Ladder Rule: If price goes UP by 1/n, consumption must go DOWN by 1/(n+1) to keep spending unchanged! Example: Price up by 25% (1/4) -> Consumption down by 1/5 (20%)!",
            "Successive Percentage: Net Change = a + b + (ab/100). If price increases by 20% then discounts by 10%: +20 - 10 + (20 x -10)/100 = 10 - 2 = +8% net profit."
        ],
        "pyq_walkthrough": {
            "question": "UPSC CSAT 2021: The price of an article was increased by 20% and then the two-successive discounts of 10% and 10% were given. What is the net profit or loss percentage?",
            "step1_child_logic": "Start with original price = ₹100.",
            "step2_working": "1. Increase by 20% -> New price = ₹120.\n2. First 10% discount on ₹120: 10% of 120 is ₹12. Price becomes 120 - 12 = ₹108.\n3. Second 10% discount on ₹108: 10% of 108 is ₹10.80. Price becomes 108 - 10.80 = ₹97.20.\n4. Original price was ₹100, final price is ₹97.20.",
            "step3_answer": "Net Loss = 100 - 97.20 = 2.8% loss!"
        }
    },
    {
        "id": "csat-mod-03",
        "title": "Averages: The Playground Seesaw Balancing Model",
        "ungist_ref": "UNGIST Chapter 5 (Pages 107-118)",
        "difficulty": "Easy (Guaranteed 4-6 Marks)",
        "child_concept": "Average is just the center balance point of a playground seesaw. Everyone sitting on the seesaw wants the exact same number of chocolates. If someone joins with extra chocolates, they must share the extra equally with everyone in the room!",
        "mental_shortcuts": [
            "Deviation Formula: Extra brought by newcomer = (Old Count + 1) x (Increase in Average).",
            "Replacement Formula: New person weight = Replaced person weight + (Total Persons x Change in Average)."
        ],
        "pyq_walkthrough": {
            "question": "UPSC CSAT 2020: The average weight of 12 students in a class is 40 kg. When the teacher's weight is included, the average weight increases by 2 kg. What is the weight of the teacher?",
            "step1_child_logic": "Imagine 12 students are sitting on a seesaw, each weighing 40 kg. The teacher enters the room.",
            "step2_working": "Total people in room now = 12 + 1 = 13 people.\nTo lift everyone's average by +2 kg, the teacher must provide: 13 x 2 kg = 26 kg of extra weight!\nPlus the teacher must keep 40 kg for herself to match the baseline.\nTeacher's weight = 40 kg (baseline) + 26 kg (lift for 13 people) = 66 kg!",
            "step3_answer": "Teacher's weight is 66 kg. Done in 5 seconds without multiplying 13 x 42."
        }
    },
    {
        "id": "csat-mod-04",
        "title": "Time and Work: The LCM Total-Units Method",
        "ungist_ref": "UNGIST Chapter 11 & 12 (Pages 199-229)",
        "difficulty": "Easy (Never use fractions like 1/12 + 1/18!)",
        "child_concept": "Never add fractions like 1/12 + 1/18 under exam pressure! Instead, imagine the total work is baking a fixed number of cookies. The total cookies to bake is simply the LCM of the days!",
        "mental_shortcuts": [
            "Step 1: Total Cookies = LCM of days given.",
            "Step 2: Find how many cookies each person bakes per day (Efficiency = Total Cookies / Days).",
            "Step 3: Combine their daily cookies and divide. Time = Total Cookies / Daily Cookies."
        ],
        "pyq_walkthrough": {
            "question": "UPSC CSAT 2022: Person A can complete a work in 10 days, Person B in 15 days, and Person C in 30 days. If all three work together, in how many days will the work be completed?",
            "step1_child_logic": "Let Total Work = LCM(10, 15, 30) = 30 cookies.",
            "step2_working": "A bakes: 30 / 10 = 3 cookies per day.\nB bakes: 30 / 15 = 2 cookies per day.\nC bakes: 30 / 30 = 1 cookie per day.\nTogether in 1 day they bake: 3 + 2 + 1 = 6 cookies per day.",
            "step3_answer": "Time taken = 30 cookies / 6 cookies per day = 5 DAYS! Zero fractions, zero panic."
        }
    },
    {
        "id": "csat-mod-05",
        "title": "Time, Speed & Distance: The 5/18 Converter & Relative Speed",
        "ungist_ref": "UNGIST Chapter 8, 9 & 10 (Pages 173-198)",
        "difficulty": "Moderate",
        "child_concept": "Trains are measured in metres, but highway speeds are in km/hr. To turn km/hr into metres-per-second, multiply by 5/18 (because 18 km/hr = 5 m/s). When two trains run toward each other, their speeds add up; when chasing in the same direction, their speeds subtract!",
        "mental_shortcuts": [
            "Speed Multiples: 18 km/h = 5 m/s | 36 km/h = 10 m/s | 54 km/h = 15 m/s | 72 km/h = 20 m/s | 90 km/h = 25 m/s.",
            "Crossing Pole: Distance = Train length only (pole has zero width).",
            "Crossing Platform: Distance = Train length + Platform length.",
            "Average Speed for equal distances: 2xy / (x + y)."
        ],
        "pyq_walkthrough": {
            "question": "UPSC CSAT 2023: Two trains of equal length 150m each are running on parallel tracks in opposite directions at 54 km/hr and 90 km/hr. How many seconds will they take to completely cross each other?",
            "step1_child_logic": "Opposite directions -> Speeds ADD UP! Total distance to clear = Train 1 + Train 2 = 150m + 150m = 300m.",
            "step2_working": "Relative Speed = 54 + 90 = 144 km/hr.\nConvert 144 km/hr to m/s: 144 x (5/18) = 8 x 5 = 40 m/s.\nDistance = 300 metres.",
            "step3_answer": "Time = Distance / Speed = 300 / 40 = 7.5 SECONDS!"
        }
    },
    {
        "id": "csat-mod-06",
        "title": "Permutations & Combinations: Handshakes & Tie/Gap Tricks",
        "ungist_ref": "UNGIST Chapter 13 (Pages 230-254)",
        "difficulty": "Moderate (UPSC tests 4-6 questions every year)",
        "child_concept": "Permutation is about ARRANGING in a line (order matters: Gold, Silver, Bronze). Combination is about SELECTING a committee or team (order doesn't matter: Rahul and Priya are the same team as Priya and Rahul).",
        "mental_shortcuts": [
            "Handshake Theorem: If n people shake hands with each other once, total handshakes = n(n - 1) / 2.",
            "Tie Method (Keep Together): Tie the items together in a bag, treat the bag as 1 single item, arrange everything, then multiply by internal arrangements.",
            "Gap Method (Never Together): Arrange other items first, then place the restricted items in the gaps between them."
        ],
        "pyq_walkthrough": {
            "question": "UPSC CSAT 2023: In how many ways can 5 boys and 4 girls sit in a row such that no two girls sit together?",
            "step1_child_logic": "No two girls together -> Use the GAP method! Place the 5 boys first, which creates safe isolated chairs (gaps) between them.",
            "step2_working": "1. Arrange 5 boys: _ B1 _ B2 _ B3 _ B4 _ B5 _\nNumber of ways to arrange 5 boys = 5! = 120 ways.\n2. Count available gaps: There are 6 gaps (1 before B1, 4 between boys, 1 after B5).\n3. Pick 4 gaps for the 4 girls: 6C4 = 6C2 = (6 x 5) / 2 = 15 choices.\n4. Arrange the 4 girls in chosen gaps = 4! = 24 ways.",
            "step3_answer": "Total ways = 120 x 15 x 24 = 43,200 ways!"
        }
    },
    {
        "id": "csat-mod-07",
        "title": "Clocks & Calendar: The 7-Day Cycle & Angle Formula",
        "ungist_ref": "UNGIST Chapter 18 & 19 (Pages 297-309)",
        "difficulty": "Easy (Guaranteed 2-4 Marks)",
        "child_concept": "There are only 7 days in a week. Days repeat in an endless loop of 7. An ordinary year (365 days = 52 weeks + 1 day) shifts the calendar forward by exactly 1 odd day. A leap year (366 days) shifts it forward by 2 odd days!",
        "mental_shortcuts": [
            "Clock Angle Formula: Angle = |30H - (11/2)M| degrees.",
            "Speed of Hands: Minute hand travels at 6 degrees/minute; Hour hand travels at 0.5 degrees/minute; Relative speed = 5.5 degrees/min.",
            "Century Odd Days: 100 years = 5 odd days; 200 years = 3; 300 years = 1; 400 years = 0 odd days!"
        ],
        "pyq_walkthrough": {
            "question": "UPSC CSAT 2021: What is the angle between the hour hand and the minute hand of a clock at 3:40?",
            "step1_child_logic": "H = 3, M = 40. Apply the universal formula: |30H - 5.5M|.",
            "step2_working": "30 x 3 = 90.\n5.5 x 40 = 220.\nDifference = |90 - 220| = |-130| = 130 degrees.",
            "step3_answer": "Angle between hands is 130 degrees!"
        }
    },
    {
        "id": "csat-mod-08",
        "title": "Syllogisms: The Mom & Baby Venn Circle Rules",
        "ungist_ref": "UNGIST Chapter 32 (Pages 366-371)",
        "difficulty": "Easy to Moderate (3-5 Questions)",
        "child_concept": "Do not read syllogisms as English grammar! Treat them as physical circles on a table:\n- 'All A are B': Circle A lives completely INSIDE Circle B.\n- 'Some A are B': Circles A and B overlap in a shared slice.\n- 'No A is B': Circles A and B are locked in separate rooms with a wall between them.",
        "mental_shortcuts": [
            "Golden Rule 1: Two positive statements ('All', 'Some') can NEVER lead to a negative conclusion ('No', 'Some not').",
            "Golden Rule 2: If Circle A is inside Circle B, and Circle B does not touch Circle C, then Circle A can NEVER touch Circle C."
        ],
        "pyq_walkthrough": {
            "question": "UPSC CSAT 2022: Statements: 1. All cats are dogs. 2. Some dogs are tigers. Conclusions: I. Some cats are tigers. II. No cat is a tiger.",
            "step1_child_logic": "Check relationship between cats and tigers: Circle Cat is inside Dog. Tiger overlaps Dog. But Tiger circle might or might not touch the inner Cat circle!",
            "step2_working": "Conclusion I ('Some cats are tigers') is possible, but not definitely certain.\nConclusion II ('No cat is a tiger') is also possible, but not definitely certain.\nNotice: They form a complementary pair (Some + No) sharing the exact same subjects (cats, tigers)!",
            "step3_answer": "EITHER Conclusion I OR Conclusion II follows! The classic UPSC complementary pair."
        }
    },
    {
        "id": "csat-mod-09",
        "title": "Reading Comprehension: The 4-Step 'Sherlocking' Method",
        "ungist_ref": "Official UPSC CSAT 2018–2024 Analysis",
        "difficulty": "High Weightage (~27 Questions, ~67.5 Marks)",
        "child_concept": "Reading Comprehension is not an English exam! You do not need rich vocabulary. It is an exercise in detective evidence. Treat the passage as a crime scene: the author is the witness, and the correct option is the ONLY claim the author explicitly makes.",
        "sherlocking_steps": [
            {"step": "Step 1: Read the Question Stem FIRST", "rule": "Never read the passage first! Read the question to know your mission: Is it asking for 'Critical Assumption', 'Most Logical Corollary', or 'Central Crux'?"},
            {"step": "Step 2: Locate the Exact Sentence Anchor", "rule": "Scan the passage like an eagle for the keyword in the question. The answer lives in that exact sentence or the sentence right after it."},
            {"step": "Step 3: Murder the Extreme Words", "rule": "UPSC questions are written by balanced civil servants. Eliminate any option with extreme words: 'always', 'never', 'solely', 'entirely', 'banned', 'drastically', 'only'."},
            {"step": "Step 4: Pick the Modest, Defensible Claim", "rule": "The correct answer almost always uses cautious, nuanced language: 'can', 'may', 'partially', 'contributes to', 'requires multi-stakeholder effort'."}
        ],
        "pyq_walkthrough": {
            "question": "UPSC CSAT 2023: Passage on Climate Change and Agriculture ending with: 'Food security in developing nations is imperiled by irregular monsoons, necessitating resilient seed varieties and micro-irrigation systems.' Which is the most logical corollary?",
            "step1_child_logic": "Scan for extreme options:\n- Option A: 'Developing nations must ban rice cultivation.' -> EXTREME ('ban'). KILL IT.\n- Option B: 'Climate change will lead to permanent global famine by 2030.' -> EXTREME ('permanent global famine'). KILL IT.\n- Option C: 'Adapting farming practices and water-use efficiency is essential for agricultural resilience.' -> BALANCED, matches passage perfectly!\n- Option D: 'Traditional farmers are solely responsible for water depletion.' -> EXTREME ('solely'). KILL IT.",
            "step2_working": "Options A, B, and D murdered in 15 seconds using extreme-word filters.",
            "step3_answer": "Option C is correct. Zero ambiguity."
        }
    }
]

output_file = os.path.join(CSAT_DIR, 'csat-modules.json')
with open(output_file, 'w') as f:
    json.dump(modules, f, indent=2)

print(f"Successfully generated CSAT mastery modules at {output_file} ({len(modules)} chapters).")
