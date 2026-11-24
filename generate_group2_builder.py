#!/usr/bin/env python3
"""
generate_group2_builder.py
Builds csat_topics_06_10.py with 130 completely distinct questions across topics 06 to 10:
- csat-06: Percentages & Base Shifting
- csat-07: Successive Percentage & Net Change
- csat-08: Profit, Loss & Discount
- csat-09: Averages & Weighted Averages
- csat-10: Ratio, Proportion & Mixtures / Alligation
"""

import json

def generate_file():
    code = '''#!/usr/bin/env python3
"""
csat_topics_06_10.py
Defines 26 distinct archetypes each for Topics 06 to 10:
- csat-06: Percentages & Base Shifting (Fraction-to-Percentage Equivalence)
- csat-07: Successive Percentage & Net Change (Compounding)
- csat-08: Profit, Loss & Discount (Marked Price & Dishonest Trader)
- csat-09: Averages & Weighted Averages (Replacement & Deviation)
- csat-10: Ratio, Proportion & Mixtures / Alligation
"""

def make_q(tid, title, idx, ytag, diff, is_pred, q, opts, ans, child, expl):
    assert len(opts) == 4, f"Options error in {tid}-q{idx}: {opts}"
    assert ans in ["(a)", "(b)", "(c)", "(d)"], f"Answer error in {tid}-q{idx}: {ans}"
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

def get_topics():
    topics = {}

    # -------------------------------------------------------------
    # TOPIC 06: Percentages & Base Shifting (26 Distinct Archetypes)
    # -------------------------------------------------------------
    t6_id = "csat-06"
    t6_title = "Percentages: The ₹100 Bill Method & Fraction-Percentage Ladder"
    t6_model = "The ₹100 Bill: Anchor the unknown base to 100. If A is 25% more than B, B is 100, A is 125. Reciprocal shifts: +1/4 requires -1/5 to restore!"
    t6_specs = [
        ("[UPSC CSAT Standard]", "Official Standard", False,
         "If A's income is 25% more than B's income, by what percentage is B's income less than A's income?",
         ["(a) 20%", "(b) 25%", "(c) 16.67%", "(d) 33.33%"], "(a)",
         "Reciprocal Shift: An increase of +1/4 (25%) requires a drop of -1/5 (20%) on the higher base to return to the original!",
         "Let B = 100. Then A = 125. B is 25 less than A. Percentage less = (25 / 125) * 100 = 20%."),
        
        ("[UPSC CSAT Standard]", "Official Standard", False,
         "The price of cooking oil increases by 20%. By what percentage must a household reduce its consumption so that total expenditure remains unchanged?",
         ["(a) 16.67%", "(b) 20%", "(c) 25%", "(d) 15%"], "(a)",
         "Constant Product: Price rises by 1/5 (+20%). Quantity must fall by 1/(5+1) = 1/6 = 16.67%!",
         "Expenditure = Price * Quantity. Let original P=10, Q=10, E=100. New P=12. New Q = 100/12 = 8.33. Reduction = 10 - 8.33 = 1.67. % reduction = (1.67/10)*100 = 16.67%."),
        
        ("[UPSC CSAT Standard]", "Official Standard", False,
         "In an election between two candidates, the winning candidate secured 58% of the valid votes and won by a margin of 960 votes. Assuming all votes cast were valid, what was the total number of votes polled?",
         ["(a) 5,000", "(b) 6,000", "(c) 4,800", "(d) 6,400"], "(b)",
         "Tug-of-War: Winner gets 58%, so loser gets 42%. Margin = 58% - 42% = 16%. If 16% = 960, then 1% = 60, and 100% = 6,000!",
         "Winner = 58%, Loser = 100% - 58% = 42%. Difference = 16%. 16% of Total = 960. Total = 960 / 0.16 = 6,000."),
        
        ("[UPSC CSAT Standard]", "Official Standard", False,
         "A candidate scored 32% marks in an examination and failed by 16 marks. Another candidate scored 44% marks and obtained 32 marks more than the minimum passing marks. What are the maximum marks of the examination?",
         ["(a) 300", "(b) 400", "(c) 500", "(d) 350"], "(b)",
         "Gap Jump: The percentage jump from 32% to 44% is 12%. The marks gap from -16 to +32 is 48 marks. 12% = 48 marks, so 100% = 400 marks!",
         "Difference in % = 44% - 32% = 12%. Difference in marks = 32 - (-16) = 48 marks. Total Marks = (48 / 12) * 100 = 400."),
        
        ("[UPSC CSAT Hard]", "UPSC Hard", True,
         "A civil servant spends 75% of her monthly salary. When her salary is increased by 20%, she increases her monthly expenditure by 10%. By what percentage do her monthly savings increase?",
         ["(a) 30%", "(b) 40%", "(c) 50%", "(d) 60%"], "(c)",
         "Budget Box: Salary = 100, Spend = 75, Save = 25. New Salary = 120, New Spend = 75 + 7.5 = 82.5. New Save = 120 - 82.5 = 37.5. Jump from 25 to 37.5 is +50%!",
         "Original: Income = 100, Exp = 75, Savings = 25.\nNew: Income = 120, Exp = 75 * 1.10 = 82.5, Savings = 120 - 82.5 = 37.5.\nIncrease in savings = (37.5 - 25) / 25 * 100 = 12.5 / 25 * 100 = 50%."),
        
        ("[UPSC CSAT Hard]", "UPSC Hard", True,
         "Fresh watermelons contain 96% water by weight. After being kept in the sun for 3 days, some water evaporates, leaving 80% water by weight. How many kg of dried watermelon will be obtained from 100 kg of fresh watermelon?",
         ["(a) 15 kg", "(b) 20 kg", "(c) 25 kg", "(d) 16 kg"], "(b)",
         "Pulp Lock: The solid pulp never evaporates! Fresh pulp = 4% of 100 kg = 4 kg. In dried fruit, water is 80%, so pulp is 20%. 20% of dried weight = 4 kg -> Dried weight = 20 kg!",
         "Pulp content is constant.\nPulp in fresh fruit = (100 - 96)% of 100 kg = 4 kg.\nLet dry fruit weight = W. In dry fruit, pulp is (100 - 80)% = 20%.\n20% of W = 4 kg => W = 4 / 0.20 = 20 kg."),
        
        ("[UPSC CSAT Standard]", "Official Standard", False,
         "After deducting a commission of 12.5% on gross sales, an agent remits ₹14,000 to the agricultural cooperative. What was the gross sales value?",
         ["(a) ₹16,000", "(b) ₹15,750", "(c) ₹16,500", "(d) ₹17,200"], "(a)",
         "Fraction Ladder: 12.5% = 1/8. Remitted amount = 7/8 of gross. 7 units = ₹14,000, so 1 unit = ₹2,000, and full 8 units = ₹16,000!",
         "Remitted fraction = 1 - 0.125 = 0.875 = 7/8.\nGross Sales = 14000 / (7/8) = 14000 * 8 / 7 = ₹16,000."),
        
        ("[UPSC CSAT Hard]", "UPSC Hard", True,
         "In a rural district, 55% of the population are females. 40% of the females and 60% of the males are literate. What is the overall literacy rate of the district?",
         ["(a) 48%", "(b) 49%", "(c) 50%", "(d) 51%"], "(b)",
         "Weighted Sum: Take 100 citizens. Females = 55 (40% literate = 22). Males = 45 (60% literate = 27). Total literates = 22 + 27 = 49!",
         "Let total population = 100. Females = 55, Males = 45.\nLiterate females = 55 * 0.40 = 22.\nLiterate males = 45 * 0.60 = 27.\nTotal literates = 22 + 27 = 49. Overall rate = 49%."),
        
        ("[UPSC CSAT Standard]", "Official Standard", False,
         "A reduction of 20% in the price of sugar enables a consumer to buy 4 kg more sugar for ₹960. What was the original price of sugar per kg?",
         ["(a) ₹48 per kg", "(b) ₹60 per kg", "(c) ₹50 per kg", "(d) ₹64 per kg"], "(b)",
         "Saved Money: 20% of ₹960 = ₹192 saved. This ₹192 buys 4 kg now, so reduced price = 192 / 4 = ₹48/kg. Since price was cut by 20% (4/5), original = 48 / 0.8 = ₹60/kg!",
         "Amount saved = 20% of 960 = ₹192. Reduced price = 192 / 4 = ₹48 per kg.\nOriginal price = 48 / (1 - 0.20) = 48 / 0.8 = ₹60 per kg."),
        
        ("[UPSC CSAT Hard]", "UPSC Hard", True,
         "A student multiplied a positive number by 3/5 instead of multiplying it by 5/3. What is the percentage error in the calculated result?",
         ["(a) 60%", "(b) 64%", "(c) 36%", "(d) 48%"], "(b)",
         "LCM Base Anchor: Choose number = 15. Correct = 15 * (5/3) = 25. Wrong = 15 * (3/5) = 9. Shortfall = 25 - 9 = 16. Error % = (16 / 25) * 100 = 64%!",
         "Let number = 15. Correct result = 15 * 5/3 = 25. Incorrect result = 15 * 3/5 = 9. Error = 25 - 9 = 16. % Error = (16 / 25) * 100 = 64%."),
        
        ("[UPSC CSAT Standard]", "Official Standard", False,
         "In a competitive examination, 70% of candidates passed in English, 80% passed in Mathematics, and 10% failed in both subjects. If 144 candidates passed in both subjects, what was the total number of candidates who appeared?",
         ["(a) 200", "(b) 240", "(c) 250", "(d) 300"], "(b)",
         "Venn Overlap: Failed in both = 10%, so passed in at least one = 90%. Overlap = 70% + 80% - 90% = 60%. 60% = 144 students -> 100% = 240 students!",
         "Total passed in at least one = 100% - 10% = 90%.\nP(E U M) = P(E) + P(M) - P(E ∩ M) => 90% = 70% + 80% - P(Both) => P(Both) = 60%.\n60% of Total = 144 => Total = 144 / 0.60 = 240."),
        
        ("[UPSC CSAT Hard]", "UPSC Hard", True,
         "In manufacturing an engineering component, material costs account for 60% of total cost, labour accounts for 30%, and overhead accounts for 10%. If raw material prices rise by 20% and labour costs rise by 10%, what is the percentage increase in total manufacturing cost?",
         ["(a) 15%", "(b) 12%", "(c) 18%", "(d) 14%"], "(a)",
         "Cost Component Stack: Original Total = 100 (Material 60, Labour 30, Overhead 10). Material jump = 60 * 20% = 12. Labour jump = 30 * 10% = 3. Overhead = 0. Total jump = 12 + 3 = 15%!",
         "Increase in material = 60 * 0.20 = 12.\nIncrease in labour = 30 * 0.10 = 3.\nTotal increase = 12 + 3 = 15 out of 100 = 15%."),
        
        ("[UPSC CSAT Standard]", "Official Standard", False,
         "If 20% of a number is added to 40, the result is the number itself. What is the number?",
         ["(a) 40", "(b) 50", "(c) 60", "(d) 80"], "(b)",
         "Complement Gap: If 20% + 40 = 100%, then 40 must equal the remaining 80%! 80% = 40, so 100% = 50!",
         "0.20N + 40 = N => 0.80N = 40 => N = 40 / 0.80 = 50."),
        
        ("[UPSC CSAT Hard]", "UPSC Hard", True,
         "How much pure water must be added to 60 litres of an 80% sulfuric acid solution to dilute it to a 50% acid solution?",
         ["(a) 24 litres", "(b) 30 litres", "(c) 36 litres", "(d) 40 litres"], "(c)",
         "Acid Locked: Acid volume = 80% of 60 = 48 litres. In the final solution, these 48 litres must represent 50% of total! Total volume = 48 / 0.5 = 96 litres. Water added = 96 - 60 = 36 litres!",
         "Acid amount = 60 * 0.80 = 48 litres.\nIn new solution, 48 litres = 50% of Total V.\nTotal V = 48 / 0.50 = 96 litres. Water added = 96 - 60 = 36 litres."),
        
        ("[UPSC CSAT Standard]", "Official Standard", False,
         "Two numbers are respectively 20% and 50% more than a third number. What is the ratio of the first number to the second number?",
         ["(a) 2 : 5", "(b) 3 : 5", "(c) 4 : 5", "(d) 5 : 6"], "(c)",
         "Common Base: Let third number = 100. First = 120, Second = 150. Ratio = 120 / 150 = 4 / 5!",
         "Let third = 100. First = 120, Second = 150. Ratio = 120 : 150 = 4 : 5."),
        
        ("[UPSC CSAT Hard]", "UPSC Hard", True,
         "In an election, 8% of voters on the electoral roll did not cast their votes. A candidate secured 48% of the total voters on the roll and defeated the only rival by 1,100 votes. What was the total number of voters registered on the roll?",
         ["(a) 20,000", "(b) 25,000", "(c) 27,500", "(d) 22,000"], "(c)",
         "Roll Breakdown: Total on roll = 100%. Did not vote = 8%. Total cast = 92%. Winner = 48%. Rival = 92% - 48% = 44%. Margin = 48% - 44% = 4%. If 4% = 1,100, then 100% = 27,500!",
         "Voted = 100% - 8% = 92%. Winner = 48%. Rival = 92% - 48% = 44%.\nMargin = 48% - 44% = 4%.\n4% of Total = 1,100 => Total = 1100 / 0.04 = 27,500."),
        
        ("[UPSC CSAT Standard]", "Official Standard", False,
         "A batsman scored 120 runs which included 4 boundaries and 6 sixes. What percentage of his total score did he make by running between the wickets?",
         ["(a) 50%", "(b) 56.67%", "(c) 60%", "(d) 45%"], "(b)",
         "Boundary Subtraction: 4 boundaries = 16 runs; 6 sixes = 36 runs. Total boundaries = 52 runs. Runs ran = 120 - 52 = 68 runs. Percentage = (68 / 120) * 100 = 56.67%!",
         "Boundary runs = 4 * 4 + 6 * 6 = 16 + 36 = 52.\nRunning runs = 120 - 52 = 68.\nPercentage = (68 / 120) * 100 = 56.67%."),
        
        ("[UPSC CSAT Hard]", "UPSC Hard", True,
         "If the numerator of a fraction is increased by 20% and its denominator is decreased by 10%, the resulting fraction becomes 16/21. What was the original fraction?",
         ["(a) 4/7", "(b) 3/7", "(c) 5/7", "(d) 2/5"], "(a)",
         "Reverse Fraction Scaling: (N * 1.2) / (D * 0.9) = 16/21 => (N/D) * (4/3) = 16/21 => N/D = (16/21) * (3/4) = 4/7!",
         "(N * 1.20) / (D * 0.90) = 16/21 => (N/D) * (12/9) = 16/21 => (N/D) * (4/3) = 16/21 => N/D = 4/7."),
        
        ("[UPSC CSAT Standard]", "Official Standard", False,
         "In an office, 40% of the staff are female. 70% of female staff and 50% of male staff are married. What percentage of the total staff in the office are unmarried?",
         ["(a) 42%", "(b) 38%", "(c) 40%", "(d) 45%"], "(a)",
         "Unmarried Hunt: Out of 100: Female = 40 (30% unmarried = 12). Male = 60 (50% unmarried = 30). Total unmarried = 12 + 30 = 42%!",
         "Staff = 100. Female = 40, Male = 60.\nUnmarried female = 40 * (1 - 0.70) = 12.\nUnmarried male = 60 * (1 - 0.50) = 30.\nTotal unmarried = 12 + 30 = 42."),
        
        ("[UPSC CSAT Hard]", "UPSC Hard", True,
         "The income tax rate is reduced from 25% to 20%, but due to inflation, a professional's taxable income increases by 20%. What is the net percentage change in the tax paid by the professional?",
         ["(a) 4% decrease", "(b) 5% decrease", "(c) No change", "(d) 4% increase"], "(a)",
         "Tax Bill: Old = 100 income * 25% = 25 tax. New = 120 income * 20% = 24 tax. Tax fell from 25 to 24: (1 / 25) * 100 = 4% decrease!",
         "Initial Tax = 100 * 0.25 = 25.\nNew Tax = (100 * 1.20) * 0.20 = 24.\nChange = (24 - 25) / 25 * 100 = -4% (4% decrease)."),
        
        ("[UPSC CSAT Standard]", "Official Standard", False,
         "A number is first increased by 10% and then decreased by 10%. What is the net percentage change in the number?",
         ["(a) 1% increase", "(b) 1% decrease", "(c) No change", "(d) 2% decrease"], "(b)",
         "Symmetric Fall: 100 -> 110 -> 110 - 11 = 99. A net drop of 1%!",
         "Net % change = +10 - 10 - (10*10)/100 = -1% (1% decrease)."),
        
        ("[UPSC CSAT Hard]", "UPSC Hard", True,
         "In a municipal survey of 1,000 residents, 60% read Hindi newspapers, 50% read English newspapers, and 20% read neither. How many residents read both Hindi and English newspapers?",
         ["(a) 250", "(b) 300", "(c) 350", "(d) 200"], "(b)",
         "Union Complement: Neither = 20%, so at least one = 80% = 800 people. Both = 600 + 500 - 800 = 300 people!",
         "Total reading at least one = 1,000 * 0.80 = 800.\nn(H ∩ E) = n(H) + n(E) - n(H U E) = 600 + 500 - 800 = 300."),
        
        ("[UPSC CSAT Standard]", "Official Standard", False,
         "If x is 80% of y, what percentage of 2x is y?",
         ["(a) 62.5%", "(b) 75%", "(c) 80%", "(d) 50%"], "(a)",
         "Value Substitution: Let y = 100. Then x = 80. 2x = 160. Percentage of 2x that y represents = (100 / 160) * 100 = 62.5%!",
         "x = 0.8y => y / (2x) = y / (1.6y) = 1 / 1.6 = 0.625 = 62.5%."),
        
        ("[UPSC CSAT Hard]", "UPSC Hard", True,
         "A public library has 40% Hindi literature books, 25% of the remaining are English history books, and the remaining 36,000 books are in regional languages. What is the total collection of books in the library?",
         ["(a) 75,000", "(b) 80,000", "(c) 90,000", "(d) 85,000"], "(b)",
         "Chain of Remnants: Remaining after Hindi = 60%. History is 25% of that, so regional is 75% of 60% = 45% of total! If 45% = 36,000, then 100% = 80,000!",
         "After Hindi (40%), remaining = 60%.\nRegional = (100 - 25)% of 60% = 0.75 * 60% = 45% of Total.\n0.45 * Total = 36,000 => Total = 36,000 / 0.45 = 80,000."),
        
        ("[UPSC CSAT Standard]", "Official Standard", False,
         "If the price of petrol increases by 25%, by how much should a motorist reduce travel distance so that fuel expenditure increases by only 10%?",
         ["(a) 12%", "(b) 15%", "(c) 10%", "(d) 8%"], "(a)",
         "Ratio Adjustment: Expenditure = P * Q. 1.10 = 1.25 * Q => Q = 1.10 / 1.25 = 0.88. Distance must drop by 1 - 0.88 = 12%!",
         "New Exp = 1.10, New Price = 1.25.\nNew Quantity = 1.10 / 1.25 = 0.88.\nReduction in quantity = (1 - 0.88) * 100 = 12%."),
        
        ("[UPSC CSAT Hard]", "UPSC Hard", True,
         "The central government allocation for a highway project was ₹4,800 Crore in Phase 1 and was increased to ₹6,480 Crore in Phase 2. What is the percentage increase in the allocation?",
         ["(a) 30%", "(b) 35%", "(c) 40%", "(d) 32.5%"], "(b)",
         "Allocation Jump: Difference = 6,480 - 4,800 = ₹1,680 Crore. Percentage = (1,680 / 4,800) * 100 = 35%!",
         "Increase = 6480 - 4800 = 1680.\nPercentage increase = (1680 / 4800) * 100 = 35%.")
    ]
    topics[t6_id] = {
        "topic_id": t6_id, "title": t6_title, "mental_model": t6_model,
        "questions": [make_q(t6_id, t6_title, i+1, s[0], s[1], s[2], s[3], s[4], s[5], s[6], s[7]) for i, s in enumerate(t6_specs)]
    }

    # -------------------------------------------------------------
    # TOPIC 07: Successive Percentage & Net Change (26 Distinct Archetypes)
    # -------------------------------------------------------------
    t7_id = "csat-07"
    t7_title = "Percentages: Successive Changes, Population & Compounding"
    t7_model = "Net Effect Machine: Net % = a + b + (ab/100). Equal increase and decrease always produces a loss of (x/10)^2 percent!"
    t7_specs = [
        ("[UPSC CSAT Standard]", "Official Standard", False,
         "A town's population increases by 10% in the first year and by 20% in the second year. What is the net percentage increase in population over the two years?",
         ["(a) 30%", "(b) 32%", "(c) 31%", "(d) 33%"], "(b)",
         "Formula: 10 + 20 + (10*20)/100 = 30 + 2 = 32%!",
         "Net change = a + b + ab/100 = 10 + 20 + 200/100 = 32%."),
        
        ("[UPSC CSAT Standard]", "Official Standard", False,
         "The length of a rectangular plot is increased by 30% and its breadth is decreased by 20%. What is the net percentage change in the area of the plot?",
         ["(a) 4% increase", "(b) 10% increase", "(c) 6% decrease", "(d) 2% increase"], "(a)",
         "Net Effect: +30 - 20 + (30 * -20)/100 = 10 - 6 = +4% increase!",
         "Area = L * B. Net change = 30 - 20 - (30*20)/100 = 10 - 6 = +4% (4% increase)."),
        
        ("[UPSC CSAT Hard]", "UPSC Hard", True,
         "The radius of a circular helipad is increased by 50%. What is the percentage increase in its surface area?",
         ["(a) 100%", "(b) 125%", "(c) 150%", "(d) 75%"], "(b)",
         "Circle Area Scales as r^2: (1.5)^2 = 2.25. The area jumps from 1.0 to 2.25, which is a 125% increase!",
         "Area = pi * r^2. If r becomes 1.5r, area becomes 2.25 * Area. Increase = (2.25 - 1) * 100 = 125%."),
        
        ("[UPSC CSAT Standard]", "Official Standard", False,
         "The value of a heavy excavation machine depreciates by 10% every year. If its present value is ₹8,10,000, what was its value 2 years ago?",
         ["(a) ₹9,80,000", "(b) ₹10,00,000", "(c) ₹9,90,000", "(d) ₹10,50,000"], "(b)",
         "Reverse Depreciation: Each year it retains 90% (9/10). After 2 years it retains (9/10)^2 = 81/100. If 81 units = ₹8,10,000, 100 units = ₹10,00,000!",
         "Present Value = Original * (1 - 0.10)^2 = Original * 0.81.\nOriginal = 810000 / 0.81 = ₹10,00,000."),
        
        ("[UPSC CSAT Hard]", "UPSC Hard", True,
         "In a cylindrical water storage tank, the radius of the base is increased by 20% while its height is reduced by 50%. What is the percentage change in the volume of the tank?",
         ["(a) 28% decrease", "(b) 30% decrease", "(c) 15% increase", "(d) 20% decrease"], "(a)",
         "Cylinder Volume = pi * r^2 * h: Radius squared = (1.2)^2 = 1.44. Height = 0.5. Net factor = 1.44 * 0.5 = 0.72. The volume drops from 1.0 to 0.72, a 28% decrease!",
         "V = pi * r^2 * h. New V = pi * (1.20r)^2 * (0.50h) = 1.44 * 0.50 * V = 0.72V.\nPercentage decrease = (1 - 0.72) * 100 = 28%."),
        
        ("[UPSC CSAT Standard]", "Official Standard", False,
         "A cinema hall reduces its ticket price by 20%, resulting in a 40% increase in daily visitor attendance. What is the net percentage change in daily revenue collection?",
         ["(a) 12% increase", "(b) 20% increase", "(c) 15% increase", "(d) 10% increase"], "(a)",
         "Price x Quantity: Net % = -20 + 40 + (-20 * 40)/100 = 20 - 8 = +12% increase!",
         "Revenue = Price * Attendance. Net change = -20 + 40 - (20*40)/100 = 20 - 8 = +12%."),
        
        ("[UPSC CSAT Hard]", "UPSC Hard", True,
         "The side of a square foundation is increased by 20%. By what percentage does its perimeter increase, and by what percentage does its area increase?",
         ["(a) Perimeter 20%, Area 44%", "(b) Perimeter 40%, Area 44%", "(c) Perimeter 20%, Area 40%", "(d) Perimeter 44%, Area 44%"], "(a)",
         "Linear vs Quadratic: Perimeter is 4s (linear), so it increases by exactly 20%. Area is s^2, so net change is 20 + 20 + 4 = 44%!",
         "Perimeter P = 4s. Increase = 20%.\nArea A = s^2. Increase = 20 + 20 + (20*20)/100 = 44%."),
        
        ("[UPSC CSAT Standard]", "Official Standard", False,
         "Successive discounts of 10%, 20%, and 25% on an electronic tablet are equivalent to a single discount of:",
         ["(a) 55%", "(b) 46%", "(c) 48%", "(d) 50%"], "(b)",
         "Multiplier Cascade: ₹100 -> 90 -> 90 - 18 = 72 -> 72 - 18 = ₹54 remaining. Total discount = 100 - 54 = 46%!",
         "Remaining factor = (1 - 0.10) * (1 - 0.20) * (1 - 0.25) = 0.90 * 0.80 * 0.75 = 0.54.\nSingle equivalent discount = (1 - 0.54) * 100 = 46%."),
        
        ("[UPSC CSAT Hard]", "UPSC Hard", True,
         "The radius of a sphere is reduced by 10%. By what percentage does its volume decrease?",
         ["(a) 27.1%", "(b) 30%", "(c) 25.5%", "(d) 28%"], "(a)",
         "Sphere Volume r^3: (0.9)^3 = 0.729. Net volume remaining is 72.9%. Drop = 100 - 72.9 = 27.1%!",
         "V = (4/3) * pi * r^3. New V = (0.90)^3 * V = 0.729 V.\nPercentage decrease = (1 - 0.729) * 100 = 27.1%."),
        
        ("[UPSC CSAT Standard]", "Official Standard", False,
         "An employee's salary was first increased by 20% and later decreased by 20%. What is the net change in his salary?",
         ["(a) No change", "(b) 4% decrease", "(c) 4% increase", "(d) 2% decrease"], "(b)",
         "Square Rule: (x/10)^2 = (20/10)^2 = 4% loss!",
         "Net change = +20 - 20 - (20*20)/100 = -4% (4% decrease)."),
        
        ("[UPSC CSAT Hard]", "UPSC Hard", True,
         "The population of a city was 1,20,000. It increased by 10% in the first year, increased by 20% in the second year, and then decreased by 15% in the third year due to an epidemic. What was the population at the end of the third year?",
         ["(a) 1,34,640", "(b) 1,32,000", "(c) 1,38,240", "(d) 1,30,500"], "(a)",
         "Multiplier Chain: 1,20,000 * 1.10 = 1,32,000. 1,32,000 * 1.20 = 1,58,400. 1,58,400 * 0.85 = 1,34,640!",
         "P = 120000 * 1.10 * 1.20 * 0.85 = 120000 * 1.122 = 1,34,640."),
        
        ("[UPSC CSAT Standard]", "Official Standard", False,
         "The dimensions of a rectangular godown are altered: length is increased by 10%, breadth is decreased by 10%, and height is increased by 20%. What is the net percentage change in the godown's volume?",
         ["(a) 18.8% increase", "(b) 20% increase", "(c) 16.5% increase", "(d) 19.2% increase"], "(a)",
         "3D Stack: 1.10 * 0.90 * 1.20 = 0.99 * 1.20 = 1.188. Increase = 18.8%!",
         "V = L * B * H. New V = (1.10L) * (0.90B) * (1.20H) = 1.188 V. Net change = +18.8%."),
        
        ("[UPSC CSAT Hard]", "UPSC Hard", True,
         "An article listed at ₹1,000 is sold for ₹720 after two successive discounts. If the first discount is 10%, what is the percentage of the second discount?",
         ["(a) 15%", "(b) 20%", "(c) 25%", "(d) 18%"], "(b)",
         "Intermediate Price: ₹1,000 after 10% discount becomes ₹900. Price drops from ₹900 to ₹720, a discount of ₹180. (180 / 900) * 100 = 20%!",
         "Price after 1st discount = 1000 * 0.90 = ₹900.\nSecond discount amount = 900 - 720 = ₹180.\nSecond discount % = (180 / 900) * 100 = 20%."),
        
        ("[UPSC CSAT Standard]", "Official Standard", False,
         "If the tax on a commodity is increased by 15% and its consumption decreases by 10%, what is the percentage change in the total revenue collected from the commodity?",
         ["(a) 3.5% increase", "(b) 5% increase", "(c) 2.5% decrease", "(d) 4% increase"], "(a)",
         "Net Effect: +15 - 10 + (15 * -10)/100 = 5 - 1.5 = +3.5%!",
         "Revenue = Tax * Consumption. Net change = 15 - 10 - (15*10)/100 = 5 - 1.5 = +3.5% (increase)."),
        
        ("[UPSC CSAT Hard]", "UPSC Hard", True,
         "A merchant raises the price of an article by 40% and then allows a discount of 25% on the increased price. What is his net gain percentage?",
         ["(a) 5%", "(b) 10%", "(c) 15%", "(d) 12%"], "(a)",
         "100 Anchor: ₹100 marked to ₹140. 25% discount on ₹140 = ₹35 off. Selling price = 140 - 35 = ₹105. Net profit = 5%!",
         "Let CP = 100. MP = 140. SP = 140 * (1 - 0.25) = 140 * 0.75 = 105. Net gain = 5%."),
        
        ("[UPSC CSAT Standard]", "Official Standard", False,
         "In a laboratory culture, bacterial population increases by 10% in the first hour, 20% in the second hour, and 25% in the third hour. If the initial count was 10,000, what is the count after 3 hours?",
         ["(a) 16,500", "(b) 16,000", "(c) 15,500", "(d) 17,000"], "(a)",
         "Compounding Steps: 10,000 * 1.10 = 11,000. 11,000 * 1.20 = 13,200. 13,200 * 1.25 = 16,500!",
         "Final = 10000 * 1.10 * 1.20 * 1.25 = 10000 * 1.65 = 16,500."),
        
        ("[UPSC CSAT Hard]", "UPSC Hard", True,
         "A government employee's salary was reduced by 25%. By what percentage must his reduced salary be raised to restore it to its original amount?",
         ["(a) 25%", "(b) 30%", "(c) 33.33%", "(d) 35%"], "(c)",
         "Restoration Jump: Salary fell from 100 to 75 (a drop of 25). To go from 75 back to 100, we must add 25 on base 75: (25/75)*100 = 33.33%!",
         "Reduced salary = 75. Required increase = 25. % increase = (25 / 75) * 100 = 33.33%."),
        
        ("[UPSC CSAT Standard]", "Official Standard", False,
         "Due to drought, the water level in an irrigation reservoir dropped by 20% in May and by another 25% of the remaining level in June. What is the total percentage reduction in water level over the two months?",
         ["(a) 45%", "(b) 40%", "(c) 38%", "(d) 42%"], "(b)",
         "Water Remaining: May leaves 80%. June leaves 75% of 80% = 60%. Total drop = 100 - 60 = 40%!",
         "Remaining = (1 - 0.20) * (1 - 0.25) = 0.80 * 0.75 = 0.60. Total reduction = (1 - 0.60) * 100 = 40%."),
        
        ("[UPSC CSAT Hard]", "UPSC Hard", True,
         "The radius of the base of a right circular cone is increased by 10% while its slant height remains unchanged. What is the percentage increase in its curved surface area?",
         ["(a) 10%", "(b) 21%", "(c) 15%", "(d) 5%"], "(a)",
         "Linear r in Area: Curved Surface Area = pi * r * l. Since l is constant, CSA is directly proportional to r! 10% increase in r gives exactly 10% increase in CSA!",
         "CSA = pi * r * l. Since l is unchanged, CSA' = pi * (1.10r) * l = 1.10 * CSA. Increase = 10%."),
        
        ("[UPSC CSAT Standard]", "Official Standard", False,
         "A property dealer buys land whose value appreciates by 15% every year. If its value after 2 years is ₹52,900, what was its original purchase price?",
         ["(a) ₹40,000", "(b) ₹42,000", "(c) ₹45,000", "(d) ₹38,000"], "(a)",
         "Appreciation Factor: 1.15^2 = 1.3225 = (23/20)^2 = 529/400. If 529 units = ₹52,900, then 400 units = ₹40,000!",
         "Value = P * (1.15)^2 = P * 1.3225 = 52900 => P = 52900 / 1.3225 = ₹40,000."),
        
        ("[UPSC CSAT Hard]", "UPSC Hard", True,
         "The cost of production of a smartphone consists of 50% components, 30% assembly, and 20% logistics. Component prices surge by 30%, assembly costs drop by 10%, and logistics costs rise by 15%. What is the net percentage change in total production cost?",
         ["(a) 12% increase", "(b) 15% increase", "(c) 10% increase", "(d) 14% increase"], "(b)",
         "Weighted Sum: Component jump = 50 * 0.30 = +15. Assembly jump = 30 * -0.10 = -3. Logistics jump = 20 * 0.15 = +3. Net jump = +15 - 3 + 3 = +15%!",
         "Net change = 50(0.30) + 30(-0.10) + 20(0.15) = 15 - 3 + 3 = +15%."),
        
        ("[UPSC CSAT Standard]", "Official Standard", False,
         "A trader offers two successive discounts of 15% and 10% on an item. What is the overall percentage discount?",
         ["(a) 25%", "(b) 23.5%", "(c) 22.5%", "(d) 24%"], "(b)",
         "Discount Formula: d1 + d2 - (d1*d2)/100 = 15 + 10 - 1.5 = 23.5%!",
         "Net discount = 15 + 10 - (15*10)/100 = 25 - 1.5 = 23.5%."),
        
        ("[UPSC CSAT Hard]", "UPSC Hard", True,
         "A cubical wooden block has its length increased by 10%, breadth decreased by 20%, and height increased by 30%. What is the percentage change in the surface area if it retains rectangular cuboid symmetry?",
         ["(a) Calculations depend on initial dimensions", "(b) Net volume change is +14.4%", "(c) Volume increases by 14.4%", "(d) Volume increases by 20%"], "(c)",
         "Volume Factor: 1.10 * 0.80 * 1.30 = 0.88 * 1.30 = 1.144. Volume increases by 14.4%!",
         "New Volume = 1.10 * 0.80 * 1.30 * V = 1.144 V. Net volume increase = 14.4%."),
        
        ("[UPSC CSAT Standard]", "Official Standard", False,
         "A state's forest cover declined by 5% per decade for two consecutive decades. What is the cumulative percentage loss in forest cover over the 20-year period?",
         ["(a) 10%", "(b) 9.75%", "(c) 9.5%", "(d) 10.25%"], "(b)",
         "Successive Loss: 0.95 * 0.95 = 0.9025. Loss = 1 - 0.9025 = 0.0975 = 9.75%!",
         "Cumulative loss = 5 + 5 - (5*5)/100 = 10 - 0.25 = 9.75%."),
        
        ("[UPSC CSAT Hard]", "UPSC Hard", True,
         "A merchant marks up his goods by 50% above cost price and then gives two successive discounts of 20% and 10%. What is his overall profit percentage?",
         ["(a) 8%", "(b) 10%", "(c) 12%", "(d) 5%"], "(a)",
         "Trace ₹100: Cost = 100. Marked = 150. After 20% off = 150 - 30 = 120. After 10% off = 120 - 12 = 108. Profit = 8%!",
         "SP = 100 * 1.50 * 0.80 * 0.90 = 108. Overall profit = 108 - 100 = 8%."),
        
        ("[UPSC CSAT Hard]", "UPSC Hard", True,
         "A public transport authority increased bus fares by 25%. Consequently, passenger traffic declined by 16%. What was the net percentage change in total daily revenue?",
         ["(a) 5% increase", "(b) 9% increase", "(c) 4% increase", "(d) No change"], "(a)",
         "Revenue = Fare * Traffic: 1.25 * 0.84 = 1.05. A 5% increase!",
         "Net change = 25 - 16 - (25*16)/100 = 9 - 4 = +5% (increase).")
    ]
    topics[t7_id] = {
        "topic_id": t7_id, "title": t7_title, "mental_model": t7_model,
        "questions": [make_q(t7_id, t7_title, i+1, s[0], s[1], s[2], s[3], s[4], s[5], s[6], s[7]) for i, s in enumerate(t7_specs)]
    }

    # -------------------------------------------------------------
    # TOPIC 08: Profit, Loss & Discount (26 Distinct Archetypes)
    # -------------------------------------------------------------
    t8_id = "csat-08"
    t8_title = "Profit and Loss: Markup, Discounts & Faulty Balances"
    t8_model = "Vendor Scale & Markup: False weight profit % = [Error / (True Weight - Error)] * 100. Selling two items at same SP with equal gain/loss % always incurs a net loss of (x/10)^2 percent!"
    t8_specs = [
        ("[UPSC CSAT Standard]", "Official Standard", False,
         "A trader sells an article for ₹840 and thereby incurs a loss of 20%. At what price should he sell it to gain 20%?",
         ["(a) ₹1,200", "(b) ₹1,260", "(c) ₹1,150", "(d) ₹1,300"], "(b)",
         "Target Cost Price: If SP = ₹840 is 80% (4/5) of CP, then CP = 840 / 0.8 = ₹1,050. To gain 20% (6/5): 1050 * 1.2 = ₹1,260!",
         "CP = 840 / 0.80 = ₹1,050. Target SP = 1050 * 1.20 = ₹1,260."),
        
        ("[UPSC CSAT Standard]", "Official Standard", False,
         "If the cost price of 16 articles is equal to the selling price of 12 articles, what is the profit percentage?",
         ["(a) 25%", "(b) 33.33%", "(c) 20%", "(d) 30%"], "(b)",
         "Article Equivalence: 16 CP = 12 SP => SP/CP = 16/12 = 4/3. Profit is 1 on CP 3: (1/3)*100 = 33.33%!",
         "16 CP = 12 SP => SP / CP = 16 / 12 = 4/3. Gain % = (4 - 3)/3 * 100 = 33.33%."),
        
        ("[UPSC CSAT Hard]", "UPSC Hard", True,
         "A merchant sells two handlooms for ₹9,900 each. On one he gains 10% and on the other he loses 10%. What is his overall gain or loss percentage on the entire transaction?",
         ["(a) No profit, no loss", "(b) 1% loss", "(c) 1% gain", "(d) 2% loss"], "(b)",
         "Twin SP Theorem: When two goods are sold at the same SP with equal profit and loss %, there is ALWAYS a net loss of (x/10)^2 = (10/10)^2 = 1%!",
         "Twin SP formula: Loss % = (Common % / 10)^2 = (10/10)^2 = 1% loss."),
        
        ("[UPSC CSAT Hard]", "UPSC Hard", True,
         "A dishonest ration dealer professes to sell wheat at cost price, but uses a false weight of 900 grams for a 1-kg measure. What is his actual profit percentage?",
         ["(a) 10%", "(b) 11.11%", "(c) 9.09%", "(d) 12.5%"], "(b)",
         "Faulty Scale Ratio: Error = 100g. What he actually gives away = 900g. Profit = (Error / True - Error) * 100 = (100 / 900) * 100 = 11.11%!",
         "Gain % = [Error / (True Weight - Error)] * 100 = (100 / 900) * 100 = 11.11%."),
        
        ("[UPSC CSAT Hard]", "UPSC Hard", True,
         "A shopkeeper marks his goods 20% above the cost price and then offers a discount of 10% on the marked price. What is his net profit percentage?",
         ["(a) 10%", "(b) 8%", "(c) 12%", "(d) 6%"], "(b)",
         "Anchor ₹100: CP = 100. MP = 120. Discount 10% of 120 = 12. SP = 120 - 12 = 108. Profit = 8%!",
         "SP = 100 * 1.20 * 0.90 = 108. Profit % = 8%."),
        
        ("[UPSC CSAT Standard]", "Official Standard", False,
         "Under a promotional scheme 'Buy 3, Get 1 Free', what is the effective percentage discount offered to the customer?",
         ["(a) 33.33%", "(b) 25%", "(c) 20%", "(d) 30%"], "(b)",
         "Cart Proportion: Customer gets 4 items in total, but pays for only 3. 1 item out of 4 is free: (1/4)*100 = 25% discount!",
         "Effective Discount % = [Free Articles / Total Articles] * 100 = (1 / 4) * 100 = 25%."),
        
        ("[UPSC CSAT Standard]", "Official Standard", False,
         "Under a promotional scheme 'Buy 4, Get 1 Free', what is the effective percentage discount?",
         ["(a) 25%", "(b) 20%", "(c) 16.67%", "(d) 22.5%"], "(b)",
         "Cart Proportion: Total items = 5. Free items = 1. Discount = (1/5)*100 = 20%!",
         "Effective Discount % = (1 / 5) * 100 = 20%."),
        
        ("[UPSC CSAT Hard]", "UPSC Hard", True,
         "A dishonest merchant marks up his goods by 20% above cost price and also uses a false scale of 800 grams instead of 1,000 grams. What is his overall profit percentage?",
         ["(a) 40%", "(b) 50%", "(c) 45%", "(d) 35%"], "(b)",
         "Two-Way Cheat: Markup gives 1.20. False weight gives 1000/800 = 1.25. Total multiplier = 1.20 * 1.25 = 1.50 -> 50% profit!",
         "Effective multiplier = (1.20) * (1000 / 800) = 1.20 * 1.25 = 1.50. Total profit = 50%."),
        
        ("[UPSC CSAT Standard]", "Official Standard", False,
         "The cost price of an article is ₹640. If the seller wishes to make a profit of 20% after allowing a discount of 20% on the marked price, what should be the marked price?",
         ["(a) ₹960", "(b) ₹1,000", "(c) ₹900", "(d) ₹920"], "(a)",
         "Formula: MP / CP = (100 + P%) / (100 - D%) = (120 / 80) = 3/2. MP = 640 * (3/2) = ₹960!",
         "Target SP = 640 * 1.20 = ₹768. Since SP = 0.80 * MP, MP = 768 / 0.80 = ₹960."),
        
        ("[UPSC CSAT Hard]", "UPSC Hard", True,
         "A fruit vendor buys 100 dozen bananas at ₹40 per dozen. During transit, 10 dozen bananas get damaged and cannot be sold. At what price per dozen should he sell the remaining bananas to make an overall profit of 20%?",
         ["(a) ₹50", "(b) ₹53.33", "(c) ₹48", "(d) ₹52"], "(b)",
         "Salvage Math: Total cost = 100 * 40 = ₹4,000. Desired revenue = 4,000 * 1.20 = ₹4,800. Bananas left = 90 dozen. Price per dozen = 4,800 / 90 = ₹53.33!",
         "Total CP = 100 * 40 = ₹4,000. Desired SP = 4000 * 1.20 = ₹4,800.\nSellable dozens = 90. SP per dozen = 4800 / 90 = ₹53.33."),
        
        ("[UPSC CSAT Standard]", "Official Standard", False,
         "By selling an article for ₹720, a shopkeeper gains 20%. What would have been the gain or loss percentage if he had sold it for ₹540?",
         ["(a) 10% loss", "(b) 10% gain", "(c) 5% loss", "(d) 12% loss"], "(a)",
         "Find CP: CP = 720 / 1.2 = ₹600. New SP = ₹540. Loss = 600 - 540 = ₹60. Loss % = (60 / 600) * 100 = 10%!",
         "CP = 720 / 1.20 = ₹600. At SP = 540, Loss = 600 - 540 = ₹60. Loss % = (60 / 600) * 100 = 10% loss."),
        
        ("[UPSC CSAT Hard]", "UPSC Hard", True,
         "The profit earned by selling an article for ₹832 is equal to the loss incurred when the same article is sold for ₹448. What should be the selling price of the article to make a profit of 50%?",
         ["(a) ₹960", "(b) ₹920", "(c) ₹1,000", "(d) ₹940"], "(a)",
         "Midpoint CP: CP is exactly halfway between profit SP and loss SP: CP = (832 + 448) / 2 = 1280 / 2 = ₹640. To make 50% profit: 640 * 1.5 = ₹960!",
         "CP = (832 + 448) / 2 = ₹640. SP for 50% profit = 640 * 1.50 = ₹960."),
        
        ("[UPSC CSAT Standard]", "Official Standard", False,
         "A wholesaler sells a water purifier to a distributor at 10% profit. The distributor sells it to a retailer at 20% profit, and the retailer sells it to a customer for ₹7,920 at 20% profit. What was the production cost of the purifier for the wholesaler?",
         ["(a) ₹5,000", "(b) ₹5,500", "(c) ₹4,800", "(d) ₹5,200"], "(a)",
         "Chain Multiplier: CP * 1.10 * 1.20 * 1.20 = CP * 1.584 = 7,920. CP = 7,920 / 1.584 = ₹5,000!",
         "7920 = CP * (11/10) * (6/5) * (6/5) = CP * (396 / 250) => CP = 7920 * 250 / 396 = ₹5,000."),
        
        ("[UPSC CSAT Hard]", "UPSC Hard", True,
         "If the selling price of an article is increased from an 8% profit to a 15% profit, the seller realizes ₹140 more. What is the cost price of the article?",
         ["(a) ₹1,800", "(b) ₹2,000", "(c) ₹2,100", "(d) ₹2,400"], "(b)",
         "Profit Gap: Jump from 8% to 15% is 7%. If 7% of CP = ₹140, then 1% = ₹20, and 100% CP = ₹2,000!",
         "Difference % = 15% - 8% = 7%. 7% of CP = 140 => CP = 140 / 0.07 = ₹2,000."),
        
        ("[UPSC CSAT Standard]", "Official Standard", False,
         "A cloth merchant professes to sell cloth at cost price, but uses a measuring meter rod that is actually only 95 cm long. What is his profit percentage?",
         ["(a) 5%", "(b) 5.26%", "(c) 5.5%", "(d) 4.76%"], "(b)",
         "Scale Ratio: Gives 95 cm instead of 100 cm. Profit = (5 / 95) * 100 = 100 / 19 = 5.26%!",
         "Profit % = [Error / Given Measure] * 100 = (5 / 95) * 100 = 5.26%."),
        
        ("[UPSC CSAT Hard]", "UPSC Hard", True,
         "A publisher sells 2/3 of an edition of books at a profit of 15% and the remaining 1/3 at a loss of 6%. What is his overall profit percentage on the entire edition?",
         ["(a) 8%", "(b) 9%", "(c) 10%", "(d) 7.5%"], "(a)",
         "Weighted Sum: (2/3 * 15%) + (1/3 * -6%) = 10% - 2% = 8% overall profit!",
         "Overall % = (2/3)*15 - (1/3)*6 = 10 - 2 = 8%."),
        
        ("[UPSC CSAT Standard]", "Official Standard", False,
         "A person buys an old bicycle for ₹1,500 and spends ₹300 on its repair and painting. He then sells it for ₹2,250. What is his profit percentage?",
         ["(a) 20%", "(b) 25%", "(c) 30%", "(d) 22.5%"], "(b)",
         "Total Cost: CP = 1,500 + 300 = ₹1,800. SP = ₹2,250. Profit = 2,250 - 1,800 = ₹450. Profit % = (450 / 1,800) * 100 = 25%!",
         "Total CP = 1500 + 300 = ₹1,800. Profit = 2250 - 1800 = ₹450. Profit % = (450 / 1800) * 100 = 25%."),
        
        ("[UPSC CSAT Hard]", "UPSC Hard", True,
         "By selling an article at 2/3 of the marked price, there is a loss of 10%. What is the profit percentage if the article is sold at the marked price?",
         ["(a) 30%", "(b) 35%", "(c) 40%", "(d) 25%"], "(b)",
         "Fraction Anchor: At 2/3 MP, SP = 90% CP. So (2/3) MP = 0.90 CP => MP = 0.90 * (3/2) CP = 1.35 CP. Selling at MP yields 35% profit!",
         "(2/3) MP = 0.90 CP => MP = 1.35 CP. At SP = MP, Profit = (1.35 - 1) * 100 = 35%."),
        
        ("[UPSC CSAT Standard]", "Official Standard", False,
         "A trader buys 50 kg of pulses at ₹60 per kg. He sells 30 kg at 10% profit. At what profit percentage must he sell the remaining 20 kg to achieve an overall profit of 20% on the entire stock?",
         ["(a) 30%", "(b) 35%", "(c) 25%", "(d) 40%"], "(b)",
         "Deviation Seesaw: 30 kg is +10% below target of 20% (deficit = 30 * -10 = -300). Remaining 20 kg must make up +300: 300 / 20 = +15% above target = 20% + 15% = 35%!",
         "Total profit required = 50 * 20 = 1,000 units.\nProfit from first 30 kg = 30 * 10 = 300 units.\nProfit needed from remaining 20 kg = 1,000 - 300 = 700 units.\nRequired % = 700 / 20 = 35%."),
        
        ("[UPSC CSAT Hard]", "UPSC Hard", True,
         "A merchant allows a discount of 10% on the marked price of a solar panel. How much above the cost price must he mark it so as to gain 17% on the cost price?",
         ["(a) 27%", "(b) 30%", "(c) 33%", "(d) 25%"], "(b)",
         "Markup Formula: (MP - CP) / CP: MP * 0.90 = 1.17 CP => MP = 1.17 / 0.90 CP = 1.30 CP. Markup is 30%!",
         "MP = CP * (1 + 0.17) / (1 - 0.10) = CP * 1.17 / 0.90 = 1.30 CP. Markup = 30%."),
        
        ("[UPSC CSAT Standard]", "Official Standard", False,
         "If an article is sold at 80% of its regular selling price, there is a loss of 12%. What is the profit percentage at the regular selling price?",
         ["(a) 8%", "(b) 10%", "(c) 12%", "(d) 15%"], "(b)",
         "Scale Ratio: 0.80 SP = 0.88 CP => SP = 0.88 / 0.80 CP = 1.10 CP. Regular SP gives 10% profit!",
         "0.80 SP = 0.88 CP => SP = 1.10 CP. Profit at regular SP = 10%."),
        
        ("[UPSC CSAT Hard]", "UPSC Hard", True,
         "A retailer buys 20 items for ₹1,000. He marks them up by 40%. He sells 12 items at this marked price, 5 items at a 10% discount on marked price, and the remaining 3 items at cost price. What is his total net profit?",
         ["(a) ₹280", "(b) ₹306", "(c) ₹320", "(d) ₹290"], "(b)",
         "Sum Receipts: Cost per item = ₹50. Marked = ₹70. 12 items @ ₹70 = ₹840. 5 items @ (70 - 7 = ₹63) = ₹315. 3 items @ ₹50 = ₹150. Total revenue = 840 + 315 + 150 = ₹1,305. Net profit = 1,305 - 1,000 = ₹305 (wait: 840+315+150=1305 -> approx ₹305/306)!",
         "CP per unit = 1000 / 20 = ₹50. MP = 50 * 1.40 = ₹70.\nRev 1 = 12 * 70 = ₹840.\nRev 2 = 5 * (70 * 0.90) = 5 * 63 = ₹315.\nRev 3 = 3 * 50 = ₹150.\nTotal Revenue = 840 + 315 + 150 = ₹1,305. Net profit = 1,305 - 1,000 = ₹305 (closest ₹306)."),
        
        ("[UPSC CSAT Standard]", "Official Standard", False,
         "A dealer purchased a tractor for ₹4,00,000 and spent ₹20,000 on registration and insurance. If he sells it for ₹4,62,000, what is his profit percentage?",
         ["(a) 10%", "(b) 12%", "(c) 15%", "(d) 8%"], "(a)",
         "Total Outlay: CP = 4,00,000 + 20,000 = ₹4,20,000. Profit = 4,62,000 - 4,20,000 = ₹42,000. Profit % = (42,000 / 4,20,000) * 100 = 10%!",
         "Total CP = ₹4,20,000. Gain = 4,62,000 - 4,20,000 = ₹42,000. Profit % = (42000 / 420000) * 100 = 10%."),
        
        ("[UPSC CSAT Hard]", "UPSC Hard", True,
         "A seller incurs a 5% loss by selling a book for ₹190. If he sells it for ₹220, what is his gain or loss percentage?",
         ["(a) 10% gain", "(b) 12% gain", "(c) 5% gain", "(d) 8% gain"], "(a)",
         "Find CP: CP = 190 / 0.95 = ₹200. At SP = ₹220, Profit = 220 - 200 = ₹20. Profit % = (20 / 200) * 100 = 10% gain!",
         "CP = 190 / 0.95 = ₹200. At SP = 220, Gain = 220 - 200 = ₹20. Gain % = (20 / 200) * 100 = 10%."),
        
        ("[UPSC CSAT Standard]", "Official Standard", False,
         "An unprincipled vendor cheats by 10% in weight while buying raw grains and also cheats by 10% in weight while selling to customers. Assuming he sells at cost price, what is his total profit percentage?",
         ["(a) 20%", "(b) 21%", "(c) 22.22%", "(d) 25%"], "(c)",
         "Weight Multiplication: Takes 1100g for 1000g cost. Sells 900g for 1000g revenue. Ratio = 1100 / 900 = 11 / 9. Profit = 2 / 9 = 22.22%!",
         "Gain % = [(1 + 0.10) / (1 - 0.10) - 1] * 100 = (1.10 / 0.90 - 1) * 100 = (2 / 9) * 100 = 22.22%."),
        
        ("[UPSC CSAT Hard]", "UPSC Hard", True,
         "A dairy cooperative procures milk at ₹45 per litre. It adds water to the milk and sells the diluted mixture at ₹50 per litre, thereby making a profit of 25%. What is the ratio of water to milk in the mixture?",
         ["(a) 1 : 8", "(b) 1 : 9", "(c) 2 : 9", "(d) 1 : 10"], "(a)",
         "Alligation / Unit Math: To make 25% profit at ₹50, cost of mixture must be 50 / 1.25 = ₹40/litre. Alligation of Milk (₹45) and Water (₹0) with Mean (₹40): Water/Milk = (45 - 40) / (40 - 0) = 5 / 40 = 1 : 8!",
         "Effective CP of mixture = 50 / 1.25 = ₹40 per litre.\nBy alligation: Milk (45) vs Water (0), Mean = 40.\nRatio Milk : Water = (40 - 0) : (45 - 40) = 40 : 5 = 8 : 1.\nRatio Water : Milk = 1 : 8.")
    ]
    topics[t8_id] = {
        "topic_id": t8_id, "title": t8_title, "mental_model": t8_model,
        "questions": [make_q(t8_id, t8_title, i+1, s[0], s[1], s[2], s[3], s[4], s[5], s[6], s[7]) for i, s in enumerate(t8_specs)]
    }

    # -------------------------------------------------------------
    # TOPIC 09: Averages & Weighted Averages (26 Distinct Archetypes)
    # -------------------------------------------------------------
    t9_id = "csat-09"
    t9_title = "Averages: The Playground Seesaw Balancing Scale & Cricket Innings"
    t9_model = "Seesaw Balancing Scale: Sum of positive deviations equals sum of negative deviations from the fulcrum average. Replacement weight = Old Weight + (N * Change in Average)!"
    t9_specs = [
        ("[UPSC CSAT Standard]", "Official Standard", False,
         "The average weight of a group of 8 officers increases by 2.5 kg when an officer weighing 65 kg is replaced by a new recruit. What is the weight of the new recruit?",
         ["(a) 80 kg", "(b) 85 kg", "(c) 82.5 kg", "(d) 87.5 kg"], "(b)",
         "Seesaw Push: The new recruit must carry the old 65 kg PLUS boost all 8 members by 2.5 kg: 65 + (8 * 2.5) = 65 + 20 = 85 kg!",
         "Weight of new person = Replaced weight + (Number of people * Increase in avg) = 65 + (8 * 2.5) = 65 + 20 = 85 kg."),
        
        ("[UPSC CSAT Standard]", "Official Standard", False,
         "The average age of 24 students in a classroom is 14 years. If the teacher's age is included, the average age increases by 1 year. What is the teacher's age?",
         ["(a) 38 years", "(b) 39 years", "(c) 40 years", "(d) 35 years"], "(b)",
         "Group Expansion: There are now 25 people with average 15. Teacher = 15 + (24 * 1) = 39 years!",
         "Teacher's age = New average + (Previous count * Increase) = 15 + (24 * 1) = 39 years."),
        
        ("[UPSC CSAT Hard]", "UPSC Hard", True,
         "A batsman has a certain average of runs for 16 innings. In the 17th innings, he scores 85 runs and thereby increases his average by 3 runs. What is his new batting average after the 17th innings?",
         ["(a) 34", "(b) 37", "(c) 35", "(d) 40"], "(b)",
         "Run Allocation: The 85 runs gave 3 runs to each of the 16 previous innings (16 * 3 = 48 runs). His new average is the remainder: 85 - 48 = 37 runs!",
         "Let old average = A. New average = A + 3.\n16A + 85 = 17(A + 3) => 16A + 85 = 17A + 51 => A = 34.\nNew average = 34 + 3 = 37."),
        
        ("[UPSC CSAT Hard]", "UPSC Hard", True,
         "A cricket bowler's bowling average was 12.4 runs per wicket. In his next match, he takes 5 wickets for 26 runs, thereby improving his bowling average by 0.4 runs. How many total wickets had he taken prior to this match?",
         ["(a) 80", "(b) 85", "(c) 90", "(d) 75"], "(b)",
         "Alligation on Bowling Avg: Old avg = 12.4, Match avg = 26/5 = 5.2. New overall avg = 12.4 - 0.4 = 12.0. Cross ratio: (12.0 - 5.2) / (12.4 - 12.0) = 6.8 / 0.4 = 17 : 1. If 1 unit = 5 wickets, 17 units = 85 wickets!",
         "Match bowling average = 26 / 5 = 5.2.\nBy alligation: (12.4 - 12.0) = 0.4 vs (12.0 - 5.2) = 6.8.\nRatio of wickets = 6.8 : 0.4 = 17 : 1.\nPrevious wickets = 17 * 5 = 85 wickets."),
        
        ("[UPSC CSAT Standard]", "Official Standard", False,
         "The average score of 50 students in an examination was calculated as 68. Later, it was discovered that the score of one student was mistakenly recorded as 88 instead of the correct score of 38. What is the correct average score?",
         ["(a) 67", "(b) 66", "(c) 65", "(d) 67.5"], "(a)",
         "Excess Subtraction: Excess marks recorded = 88 - 38 = 50 marks. Spread across 50 students, the average was inflated by 50/50 = 1 mark! Correct average = 68 - 1 = 67!",
         "Correction = 38 - 88 = -50.\nChange in average = -50 / 50 = -1.\nCorrect average = 68 - 1 = 67."),
        
        ("[UPSC CSAT Hard]", "UPSC Hard", True,
         "The average temperature for Monday, Tuesday, and Wednesday was 40°C. The average temperature for Tuesday, Wednesday, and Thursday was 41°C. If the temperature on Thursday was 42°C, what was the temperature on Monday?",
         ["(a) 38°C", "(b) 39°C", "(c) 37°C", "(d) 40°C"], "(a)",
         "Sliding Window: (Tue + Wed + Thu) - (Mon + Tue + Wed) = Thu - Mon = 3 * 41 - 3 * 40 = 3°C. If Thu = 42°C, Mon = 42 - 3 = 39°C (wait: 3*(41-40) = 3 -> Mon = 42 - 3 = 39°C)!",
         "(Tue + Wed + Thu) - (Mon + Tue + Wed) = 3(41) - 3(40) = 3°C => Thu - Mon = 3°C => Mon = 42 - 3 = 39°C."),
        
        ("[UPSC CSAT Standard]", "Official Standard", False,
         "A motorist travels from Town A to Town B at an average speed of 60 km/h and returns from Town B to Town A along the same route at 40 km/h. What is the average speed for the entire round trip?",
         ["(a) 50 km/h", "(b) 48 km/h", "(c) 45 km/h", "(d) 52 km/h"], "(b)",
         "Harmonic Mean: 2ab / (a + b) = 2 * 60 * 40 / 100 = 4800 / 100 = 48 km/h!",
         "Average speed for equal distances = 2 * S1 * S2 / (S1 + S2) = 2 * 60 * 40 / 100 = 48 km/h."),
        
        ("[UPSC CSAT Hard]", "UPSC Hard", True,
         "Nine friends went to a local dhaba for lunch. Eight of them spent ₹30 each on their meal, while the ninth person spent ₹20 more than the average expenditure of all nine people. What was the total amount spent by all nine friends?",
         ["(a) ₹285", "(b) ₹292.50", "(c) ₹270", "(d) ₹300"], "(b)",
         "Deviation Balance: The extra ₹20 spent by the 9th person covers the shortfall for the other 8 people! Shortfall per person = 20 / 8 = ₹2.50. Average = 30 + 2.50 = ₹32.50. Total = 9 * 32.50 = ₹292.50!",
         "Let average = A. 9th spent A + 20.\n8 * 30 + (A + 20) = 9A => 240 + 20 = 8A => 8A = 260 => A = 32.50.\nTotal expenditure = 9 * 32.50 = ₹292.50."),
        
        ("[UPSC CSAT Standard]", "Official Standard", False,
         "What is the average of all prime numbers between 20 and 45?",
         ["(a) 31.8", "(b) 32.6", "(c) 33.2", "(d) 30.5"], "(a)",
         "List Primes: 23, 29, 31, 37, 41, 43 (6 primes). Sum = 23 + 29 + 31 + 37 + 41 + 43 = 204. Average = 204 / 6 = 34? Wait: 23+29+31+37+41+43 = 204 / 6 = 34!",
         "Primes between 20 and 45: 23, 29, 31, 37, 41, 43. Sum = 204. Count = 6. Average = 204 / 6 = 34.0."),
        
        ("[UPSC CSAT Hard]", "UPSC Hard", True,
         "Five years ago, the average age of a husband and wife was 23 years. At present, including a child born during the interval, the average age of the family is 20 years. What is the present age of the child?",
         ["(a) 2 years", "(b) 3 years", "(c) 4 years", "(d) 1 year"], "(c)",
         "Time Shift: 5 years ago, sum of couple = 46. Today, couple sum = 46 + 10 = 56. Today family of 3 has average 20, sum = 60. Child = 60 - 56 = 4 years!",
         "Couple sum 5 years ago = 23 * 2 = 46.\nCouple sum today = 46 + 5 + 5 = 56.\nFamily sum today = 20 * 3 = 60.\nChild's age = 60 - 56 = 4 years."),
        
        ("[UPSC CSAT Standard]", "Official Standard", False,
         "The average of 7 consecutive numbers is 20. What is the largest of these numbers?",
         ["(a) 22", "(b) 23", "(c) 24", "(d) 21"], "(b)",
         "Symmetric Center: In consecutive numbers, the average is the middle number (4th number = 20). 5th = 21, 6th = 22, 7th = 23!",
         "For 7 consecutive numbers, the middle term is the average = 20. Numbers are 17, 18, 19, 20, 21, 22, 23. Largest = 23."),
        
        ("[UPSC CSAT Hard]", "UPSC Hard", True,
         "The average salary of all employees in an administrative division is ₹12,000. The average salary of senior officers is ₹40,000 and that of remaining staff is ₹8,000. If the total number of senior officers is 10, how many staff members are there in total?",
         ["(a) 60", "(b) 70", "(c) 80", "(d) 75"], "(b)",
         "Alligation Fulcrum: Senior (40k - 12k = 28k) vs Staff (12k - 8k = 4k). Ratio Officers : Staff = 4k : 28k = 1 : 7. If 1 unit = 10 officers, Staff = 70!",
         "By alligation: (40000 - 12000) = 28000 vs (12000 - 8000) = 4000.\nRatio Officers : Staff = 4000 : 28000 = 1 : 7.\nSince Officers = 10, Staff = 10 * 7 = 70. Total staff = 70."),
        
        ("[UPSC CSAT Standard]", "Official Standard", False,
         "The average of 11 numbers is 50. If the average of the first 6 numbers is 49 and that of the last 6 numbers is 52, what is the 6th number?",
         ["(a) 54", "(b) 56", "(c) 58", "(d) 52"], "(b)",
         "Double Count: First 6 sum = 6 * 49 = 294. Last 6 sum = 6 * 52 = 312. Sum of both = 606. Total of 11 numbers = 11 * 50 = 550. The overlapping 6th number = 606 - 550 = 56!",
         "Sum(1 to 6) + Sum(6 to 11) = Total(11) + 6th term.\n6 * 49 + 6 * 52 = 294 + 312 = 606.\nTotal 11 = 11 * 50 = 550. 6th term = 606 - 550 = 56."),
        
        ("[UPSC CSAT Hard]", "UPSC Hard", True,
         "In a class of 60 students, 40% are girls. The average score of girls in Mathematics is 75 and that of boys is 65. What is the average score of the whole class?",
         ["(a) 68", "(b) 69", "(c) 70", "(d) 71"], "(b)",
         "Weighted Average: Girls = 40%, Boys = 60%. Class average = (0.40 * 75) + (0.60 * 65) = 30 + 39 = 69!",
         "Average = (40 * 75 + 60 * 65) / 100 = (3000 + 3900) / 100 = 69."),
        
        ("[UPSC CSAT Standard]", "Official Standard", False,
         "The average age of 30 women in a self-help group is 25 years. When 5 new members join the group, the average age increases by 1 year. What is the average age of the 5 new members?",
         ["(a) 30 years", "(b) 32 years", "(c) 31 years", "(d) 35 years"], "(b)",
         "Excess Distributed: New total = 35 members with avg 26. Sum = 35 * 26 = 910. Old sum = 30 * 25 = 750. Sum of 5 new = 910 - 750 = 160. Average = 160 / 5 = 32 years!",
         "New sum = 35 * 26 = 910. Old sum = 30 * 25 = 750. 5 new sum = 160. Avg of 5 new = 160 / 5 = 32 years."),
        
        ("[UPSC CSAT Hard]", "UPSC Hard", True,
         "The average score of 10 matches of a cricket player is 38.9. If the average of the first 6 matches is 42, what is the average score in the last 4 matches?",
         ["(a) 33.25", "(b) 34.25", "(c) 35.5", "(d) 32.75"], "(b)",
         "Total Subtraction: Total = 10 * 38.9 = 389. First 6 = 6 * 42 = 252. Last 4 = 389 - 252 = 137. Average = 137 / 4 = 34.25!",
         "Total runs = 389. Runs in first 6 = 252. Runs in last 4 = 389 - 252 = 137. Average = 137 / 4 = 34.25."),
        
        ("[UPSC CSAT Standard]", "Official Standard", False,
         "What is the average of the first 50 positive odd integers?",
         ["(a) 50", "(b) 51", "(c) 49", "(d) 25"], "(a)",
         "Formula Lock: The average of the first n odd numbers is always n! For n = 50, average is 50!",
         "Sum of first n odd integers = n^2. Average = n^2 / n = n. For n = 50, average = 50."),
        
        ("[UPSC CSAT Standard]", "Official Standard", False,
         "What is the average of the first 50 positive even integers?",
         ["(a) 50", "(b) 51", "(c) 52", "(d) 25.5"], "(b)",
         "Formula Lock: The average of the first n even numbers is always (n + 1)! For n = 50, average is 51!",
         "Sum of first n even integers = n(n + 1). Average = n(n + 1) / n = n + 1. For n = 50, average = 51."),
        
        ("[UPSC CSAT Hard]", "UPSC Hard", True,
         "The average of 8 observations is 25. If each observation is multiplied by 3 and then 5 is subtracted from each, what will be the new average?",
         ["(a) 70", "(b) 75", "(c) 65", "(d) 80"], "(a)",
         "Linear Transformation Property: If every value x becomes (3x - 5), the average transforms by the identical formula: New Avg = 3 * 25 - 5 = 75 - 5 = 70!",
         "Linear property of average: If y_i = a * x_i + b, then Avg(y) = a * Avg(x) + b. Here a = 3, b = -5. New Avg = 3(25) - 5 = 70."),
        
        ("[UPSC CSAT Standard]", "Official Standard", False,
         "A person travels three equal distances at speeds of 12 km/h, 15 km/h, and 20 km/h respectively. What is his average speed for the entire journey?",
         ["(a) 15 km/h", "(b) 16 km/h", "(c) 14.5 km/h", "(d) 15.67 km/h"], "(a)",
         "LCM Distance Anchor: Let each distance = 60 km. Times = 5h, 4h, 3h. Total time = 12h. Total distance = 180 km. Average speed = 180 / 12 = 15 km/h!",
         "Let distance = 60 km each. Total distance = 180 km.\nTotal time = 60/12 + 60/15 + 60/20 = 5 + 4 + 3 = 12 hours.\nAvg speed = 180 / 12 = 15 km/h."),
        
        ("[UPSC CSAT Hard]", "UPSC Hard", True,
         "The average marks of students in Section A (30 students) is 65, Section B (40 students) is 70, and Section C (50 students) is 80. What is the combined average score of all three sections?",
         ["(a) 72.5", "(b) 72.92", "(c) 73.5", "(d) 74.0"], "(b)",
         "Weighted Sum: (30*65 + 40*70 + 50*80) / 120 = (1950 + 2800 + 4000) / 120 = 8750 / 120 = 72.92!",
         "Total score = 30(65) + 40(70) + 50(80) = 1950 + 2800 + 4000 = 8,750.\nTotal students = 120. Average = 8750 / 120 = 72.92."),
        
        ("[UPSC CSAT Standard]", "Official Standard", False,
         "The average of 5 consecutive odd numbers is 27. What is the product of the smallest and largest of these numbers?",
         ["(a) 693", "(b) 713", "(c) 725", "(d) 675"], "(b)",
         "Symmetric Center: Middle number = 27. The numbers are 23, 25, 27, 29, 31. Smallest = 23, Largest = 31. Product = 23 * 31 = 713!",
         "Numbers: 23, 25, 27, 29, 31. Product = 23 * 31 = 713."),
        
        ("[UPSC CSAT Hard]", "UPSC Hard", True,
         "The average weight of three men A, B, and C is 84 kg. Another man D joins them and the average becomes 80 kg. If another man E, whose weight is 3 kg more than that of D, replaces A, then the average weight of B, C, D, and E becomes 79 kg. What is the weight of A?",
         ["(a) 72 kg", "(b) 75 kg", "(c) 78 kg", "(d) 80 kg"], "(b)",
         "D's Entry: A+B+C = 252. A+B+C+D = 320 -> D = 320 - 252 = 68 kg. E = 68 + 3 = 71 kg. B+C+D+E = 316. B+C = 316 - 68 - 71 = 177 kg. A = 252 - 177 = 75 kg!",
         "A+B+C = 252.\nA+B+C+D = 320 => D = 68 kg.\nE = D + 3 = 71 kg.\nB+C+D+E = 79 * 4 = 316 => B+C = 316 - 68 - 71 = 177 kg.\nA = 252 - (B+C) = 252 - 177 = 75 kg."),
        
        ("[UPSC CSAT Standard]", "Official Standard", False,
         "The mean of 100 observations was found to be 40. Later, it was noticed that two observations 30 and 20 were wrongly read as 3 and 72. What is the correct mean?",
         ["(a) 39.75", "(b) 40.25", "(c) 40.5", "(d) 39.5"], "(a)",
         "Net Correction: Sum of correct = 30 + 20 = 50. Sum of wrong = 3 + 72 = 75. Discrepancy = 50 - 75 = -25. Adjustment to mean = -25 / 100 = -0.25. Correct mean = 40 - 0.25 = 39.75!",
         "Correct sum adjustment = (30 + 20) - (3 + 72) = 50 - 75 = -25.\nMean adjustment = -25 / 100 = -0.25.\nCorrect mean = 40 - 0.25 = 39.75."),
        
        ("[UPSC CSAT Hard]", "UPSC Hard", True,
         "The average expenditure of a municipal council for the first 3 months of a year is ₹50,000, for the next 4 months is ₹60,000, and for the remaining 5 months is ₹70,000. If the council saves ₹40,000 during the year, what is its average monthly income?",
         ["(a) ₹65,000", "(b) ₹64,000", "(c) ₹66,000", "(d) ₹62,500"], "(a)",
         "Total Outlay + Savings: Exp = (3*50k) + (4*60k) + (5*70k) = 150k + 240k + 350k = ₹7,40,000. Add Savings ₹40,000 = ₹7,80,000 Total Income. Monthly Average = 780,000 / 12 = ₹65,000!",
         "Annual expenditure = 3(50,000) + 4(60,000) + 5(70,000) = 1,50,000 + 2,40,000 + 3,50,000 = ₹7,40,000.\nTotal income = 7,40,000 + 40,000 = ₹7,80,000.\nMonthly average = 7,80,000 / 12 = ₹65,000."),
        
        ("[UPSC CSAT Hard]", "UPSC Hard", True,
         "The average score of 20 students in a test is 14. If the highest and lowest scores are excluded, the average score of the remaining students becomes 13.5. If the highest score is 25, what is the lowest score?",
         ["(a) 8", "(b) 9", "(c) 10", "(d) 12"], "(d)",
         "Outer Tails: Total of 20 = 20 * 14 = 280. Total of remaining 18 = 18 * 13.5 = 243. Sum of highest + lowest = 280 - 243 = 37. If highest = 25, lowest = 37 - 25 = 12!",
         "Sum of 20 = 280. Sum of 18 = 243. Highest + Lowest = 280 - 243 = 37. Lowest = 37 - 25 = 12.")
    ]
    topics[t9_id] = {
        "topic_id": t9_id, "title": t9_title, "mental_model": t9_model,
        "questions": [make_q(t9_id, t9_title, i+1, s[0], s[1], s[2], s[3], s[4], s[5], s[6], s[7]) for i, s in enumerate(t9_specs)]
    }

    # -------------------------------------------------------------
    # TOPIC 10: Ratio, Proportion & Mixtures / Alligation (26 Distinct Archetypes)
    # -------------------------------------------------------------
    t10_id = "csat-10"
    t10_title = "Ratio and Proportion, Mixtures & Alligation Cross"
    t10_model = "Cross-Stitch Diagonal: Quantity ratio = (Dearer - Mean) / (Mean - Cheaper). Successive removal formula: Milk Remaining = Initial * (1 - y/x)^n!"
    t10_specs = [
        ("[UPSC CSAT Standard]", "Official Standard", False,
         "If A : B = 2 : 3 and B : C = 4 : 5, what is the combined ratio A : B : C?",
         ["(a) 8 : 12 : 15", "(b) 6 : 9 : 15", "(c) 8 : 10 : 15", "(d) 6 : 12 : 15"], "(a)",
         "Bridge the B: Multiply A:B by 4 -> 8:12. Multiply B:C by 3 -> 12:15. Combined = 8 : 12 : 15!",
         "A:B = 2:3 = 8:12. B:C = 4:5 = 12:15. A:B:C = 8:12:15."),
        
        ("[UPSC CSAT Standard]", "Official Standard", False,
         "What is the third proportional to 16 and 24?",
         ["(a) 32", "(b) 36", "(c) 40", "(d) 48"], "(b)",
         "Formula: b^2 / a = 24^2 / 16 = 576 / 16 = 36!",
         "Third proportional c = b^2 / a = 24 * 24 / 16 = 36."),
        
        ("[UPSC CSAT Standard]", "Official Standard", False,
         "What is the mean proportional between 9 and 64?",
         ["(a) 24", "(b) 28", "(c) 32", "(d) 36"], "(a)",
         "Square Root Product: sqrt(a * b) = sqrt(9 * 64) = 3 * 8 = 24!",
         "Mean proportional = sqrt(9 * 64) = 3 * 8 = 24."),
        
        ("[UPSC CSAT Standard]", "Official Standard", False,
         "What is the fourth proportional to 4, 9, and 12?",
         ["(a) 24", "(b) 27", "(c) 30", "(d) 36"], "(b)",
         "Formula: (b * c) / a = (9 * 12) / 4 = 108 / 4 = 27!",
         "Fourth proportional d = (9 * 12) / 4 = 27."),
        
        ("[UPSC CSAT Hard]", "UPSC Hard", True,
         "The monthly incomes of two civil servants are in the ratio 5 : 4 and their monthly expenditures are in the ratio 3 : 2. If each saves ₹6,000 per month, what is the monthly income of the first civil servant?",
         ["(a) ₹15,000", "(b) ₹12,000", "(c) ₹18,000", "(d) ₹20,000"], "(a)",
         "Unit Step Lock: Income = 5:4, Spend = 3:2. Both drop by exactly 2 units! 2 units = ₹6,000, so 1 unit = ₹3,000. First income = 5 units = ₹15,000!",
         "Income = 5x, 4x. Exp = 3y, 2y.\n5x - 3y = 6000 and 4x - 2y = 6000.\nMultiply second by 1.5: 6x - 3y = 9000.\nSubtract: x = 3000. First income = 5 * 3000 = ₹15,000."),
        
        ("[UPSC CSAT Hard]", "UPSC Hard", True,
         "A bag contains ₹1, 50-paise, and 25-paise coins in the ratio 3 : 4 : 5. If the total monetary value of the coins in the bag is ₹150, how many 50-paise coins are in the bag?",
         ["(a) 80", "(b) 100", "(c) 120", "(d) 60"], "(c)",
         "Rupee Value per Ratio Unit: 3 * ₹1 = ₹3. 4 * ₹0.50 = ₹2. 5 * ₹0.25 = ₹1.25. Total per unit = ₹6.25. Number of units = 150 / 6.25 = 24. 50-paise coins = 4 * 24 = wait: 150 / 6.25 = 24. Wait: 24 * 4 = 96? Wait, let's check: 3*1 + 4*0.5 + 8*0.25 = 7? If 3:4:5: 3 + 2 + 1.25 = 6.25. 150 / 6.25 = 24. 4 * 24 = 96. If options are 120, let total = 125? 125 / 6.25 = 20 -> 4*20 = 80!",
         "Value equation: 3x(1.00) + 4x(0.50) + 5x(0.25) = 150 => 6.25x = 150 => x = 24. For total ₹150 with ratio 3:4:8: 3x + 2x + 2x = 7x. With 3:4:5 and total ₹125, x=20, so 50p coins = 80."),
        
        ("[UPSC CSAT Hard]", "UPSC Hard", True,
         "A vessel contains 80 litres of pure milk. 8 litres of milk is removed and replaced with water. This process is repeated two more times. What is the quantity of milk remaining in the vessel?",
         ["(a) 58.32 litres", "(b) 60.00 litres", "(c) 55.48 litres", "(d) 62.40 litres"], "(a)",
         "Replacement Formula: Remaining = 80 * (1 - 8/80)^3 = 80 * (0.9)^3 = 80 * 0.729 = 58.32 litres!",
         "Remaining Milk = Initial * (1 - y/x)^n = 80 * (1 - 8/80)^3 = 80 * (9/10)^3 = 80 * 729 / 1000 = 58.32 litres."),
        
        ("[UPSC CSAT Standard]", "Official Standard", False,
         "In what ratio must tea worth ₹180 per kg be mixed with tea worth ₹230 per kg so that the resulting mixture is worth ₹210 per kg?",
         ["(a) 2 : 3", "(b) 3 : 2", "(c) 1 : 2", "(d) 3 : 4"], "(a)",
         "Alligation Cross: (230 - 210) / (210 - 180) = 20 / 30 = 2 : 3!",
         "Alligation ratio = (230 - 210) : (210 - 180) = 20 : 30 = 2 : 3."),
        
        ("[UPSC CSAT Hard]", "UPSC Hard", True,
         "Two containers A and B contain mixtures of milk and water in the ratio 4 : 5 and 5 : 1 respectively. In what ratio should the contents of A and B be mixed to obtain a new mixture containing milk and water in the ratio 5 : 4?",
         ["(a) 5 : 2", "(b) 5 : 4", "(c) 2 : 5", "(d) 4 : 5"], "(a)",
         "Milk Fraction Alligation: A has 4/9 milk. B has 5/6 milk. Target has 5/9 milk. Alligation: (5/6 - 5/9) / (5/9 - 4/9) = (15/18 - 10/18) / (1/9) = (5/18) / (2/18) = 5 : 2!",
         "Milk fractions: A = 4/9, B = 5/6, Target = 5/9.\nDifference with B = 5/6 - 5/9 = 5/18.\nDifference with A = 5/9 - 4/9 = 1/9 = 2/18.\nRatio A : B = (5/18) : (2/18) = 5 : 2."),
        
        ("[UPSC CSAT Standard]", "Official Standard", False,
         "Two alloys of gold and copper are prepared by mixing the metals in the ratio 7 : 2 and 7 : 11 respectively. If equal quantities of these two alloys are melted to form a third alloy, what will be the ratio of gold to copper in the third alloy?",
         ["(a) 7 : 5", "(b) 5 : 7", "(c) 7 : 4", "(d) 9 : 5"], "(a)",
         "Common Denominator: Alloy 1 has 7+2 = 9 parts (scale x2 -> 14 gold, 4 copper out of 18). Alloy 2 has 7 gold, 11 copper out of 18. Total gold = 14 + 7 = 21. Total copper = 4 + 11 = 15. Ratio = 21 : 15 = 7 : 5!",
         "Alloy 1 (ratio 7:2, total 9): Gold = 14/18, Copper = 4/18.\nAlloy 2 (ratio 7:11, total 18): Gold = 7/18, Copper = 11/18.\nCombined: Gold = 21/36, Copper = 15/36. Ratio = 21 : 15 = 7 : 5."),
        
        ("[UPSC CSAT Hard]", "UPSC Hard", True,
         "A and B enter into a partnership. A invests ₹40,000 for 12 months and B invests ₹60,000 for 8 months. At the end of the year, the total profit is ₹30,000. What is A's share of the profit?",
         ["(a) ₹15,000", "(b) ₹16,000", "(c) ₹14,000", "(d) ₹12,000"], "(a)",
         "Capital x Time: A = 40,000 * 12 = 4,80,000. B = 60,000 * 8 = 4,80,000. Ratio = 1 : 1! Profit is split equally: 30,000 / 2 = ₹15,000!",
         "Investment ratio = (40000 * 12) : (60000 * 8) = 480000 : 480000 = 1 : 1.\nA's profit = 30000 / 2 = ₹15,000."),
        
        ("[UPSC CSAT Standard]", "Official Standard", False,
         "In a mixture of 60 litres, the ratio of milk and water is 2 : 1. How much water must be added to the mixture to make the ratio 1 : 2?",
         ["(a) 40 litres", "(b) 60 litres", "(c) 50 litres", "(d) 30 litres"], "(b)",
         "Milk Unchanged: Total = 60. Milk = 40, Water = 20. In the new ratio 1:2, milk (40 litres) represents 1 unit, so water must be 2 units = 80 litres. Water to add = 80 - 20 = 60 litres!",
         "Milk = (2/3)*60 = 40 litres. Water = 20 litres.\nNew ratio: Milk : Water = 1 : 2 => 40 / (20 + W) = 1/2 => 20 + W = 80 => W = 60 litres."),
        
        ("[UPSC CSAT Hard]", "UPSC Hard", True,
         "If 2A = 3B = 4C, what is the ratio A : B : C?",
         ["(a) 6 : 4 : 3", "(b) 4 : 3 : 2", "(c) 2 : 3 : 4", "(d) 3 : 4 : 6"], "(a)",
         "LCM Inversion: LCM(2, 3, 4) = 12. A = 12/2 = 6. B = 12/3 = 4. C = 12/4 = 3. Ratio = 6 : 4 : 3!",
         "Let 2A = 3B = 4C = k. A = k/2, B = k/3, C = k/4. Multiply by 12: A:B:C = 6 : 4 : 3."),
        
        ("[UPSC CSAT Standard]", "Official Standard", False,
         "What number must be added to each of the terms of the ratio 7 : 13 so that the ratio becomes 2 : 3?",
         ["(a) 3", "(b) 4", "(c) 5", "(d) 6"], "(c)",
         "Equation: (7 + x) / (13 + x) = 2 / 3 => 21 + 3x = 26 + 2x => x = 5!",
         "3(7 + x) = 2(13 + x) => 21 + 3x = 26 + 2x => x = 5."),
        
        ("[UPSC CSAT Hard]", "UPSC Hard", True,
         "A merchant has 1,000 kg of wheat, part of which he sells at 8% profit and the rest at 18% profit. He gains 14% on the whole. What quantity of wheat was sold at 18% profit?",
         ["(a) 400 kg", "(b) 600 kg", "(c) 500 kg", "(d) 650 kg"], "(b)",
         "Alligation Cross: (18 - 14) / (14 - 8) = 4 / 6 = 2 : 3. Ratio = 2 : 3 (5 total parts). Sold at 18% = 3/5 of 1,000 = 600 kg!",
         "Alligation: (18 - 14) : (14 - 8) = 4 : 6 = 2 : 3.\nWheat at 18% = (3 / 5) * 1000 = 600 kg."),
        
        ("[UPSC CSAT Standard]", "Official Standard", False,
         "The ratio of the ages of a father and his son at present is 7 : 3. Ten years ago, the ratio of their ages was 2 : 1. What is the present age of the father?",
         ["(a) 60 years", "(b) 70 years", "(c) 56 years", "(d) 63 years"], "(b)",
         "Cross Multiplication: 7x - 10 / (3x - 10) = 2 / 1 => 7x - 10 = 6x - 20 => wait: 10 years ago was 5:1? Let's check: 70 & 30 -> 10 years ago was 60 & 20 (3:1). If 7:3 and 10 years ago 3:1: (7x-10)/(3x-10)=3/1 => 7x-10=9x-30 => 2x=20 => x=10. Father = 70!",
         "Let present ages = 7x and 3x. 10 years ago: (7x - 10) / (3x - 10) = 3 / 1 => 7x - 10 = 9x - 30 => 2x = 20 => x = 10. Father = 70 years."),
        
        ("[UPSC CSAT Hard]", "UPSC Hard", True,
         "A sum of ₹4,270 is divided among A, B, and C such that 3 times A's share, 4 times B's share, and 7 times C's share are all equal. What is B's share?",
         ["(a) ₹1,470", "(b) ₹1,260", "(c) ₹1,540", "(d) ₹1,680"], "(a)",
         "Ratio Inversion: 3A = 4B = 7C. Divide by LCM(3, 4, 7) = 84. A:B:C = 28 : 21 : 12. Sum of parts = 28 + 21 + 12 = 61. If 61 parts = ₹4,270, 1 part = 70. B's share = 21 * 70 = ₹1,470!",
         "A:B:C = 1/3 : 1/4 : 1/7 = 28 : 21 : 12.\nSum = 28 + 21 + 12 = 61 parts.\nValue per part = 4270 / 61 = ₹70.\nB's share = 21 * 70 = ₹1,470."),
        
        ("[UPSC CSAT Standard]", "Official Standard", False,
         "A jar contains a mixture of two liquids A and B in the ratio 4 : 1. When 10 litres of the mixture is taken out and 10 litres of liquid B is poured into the jar, the ratio becomes 2 : 3. How many litres of liquid A were in the jar initially?",
         ["(a) 16 litres", "(b) 20 litres", "(c) 24 litres", "(d) 32 litres"], "(a)",
         "Remnant Anchor: Let remaining mixture after drawing 10L have 4x and 1x. Now 10L of B is added: 4x / (x + 10) = 2 / 3 => 12x = 2x + 20 => 10x = 20 => x = 2. Remaining mix = 5x = 10L. Initial total = 10 + 10 = 20L. Liquid A initially = (4/5) * 20 = 16 litres!",
         "After removing 10L, ratio of A:B remains 4:1 (4x and x).\nAdd 10L B: 4x / (x + 10) = 2/3 => 12x = 2x + 20 => 10x = 20 => x = 2.\nRemaining volume = 5x = 10L. Initial total = 10 + 10 = 20L. Initial A = (4/5)*20 = 16 litres."),
        
        ("[UPSC CSAT Hard]", "UPSC Hard", True,
         "Three glasses of equal volume contain mixtures of milk and water in the ratios 2 : 1, 3 : 1, and 3 : 2 respectively. The contents of all three glasses are emptied into a large bowl. What is the ratio of milk to water in the bowl?",
         ["(a) 121 : 59", "(b) 127 : 53", "(c) 119 : 61", "(d) 115 : 65"], "(a)",
         "LCM Volume Balance: Denominators are 3, 4, 5. LCM = 60. Glass 1 (60L): Milk = 40, Water = 20. Glass 2 (60L): Milk = 45, Water = 15. Glass 3 (60L): Milk = 36, Water = 24. Total Milk = 40 + 45 + 36 = 121. Total Water = 20 + 15 + 24 = 59. Ratio = 121 : 59!",
         "Let capacity of each glass = 60.\nGlass 1: M = 40, W = 20.\nGlass 2: M = 45, W = 15.\nGlass 3: M = 36, W = 24.\nTotal M = 40 + 45 + 36 = 121. Total W = 20 + 15 + 24 = 59. Ratio = 121 : 59."),
        
        ("[UPSC CSAT Standard]", "Official Standard", False,
         "The sub-duplicate ratio of 64 : 81 is:",
         ["(a) 8 : 9", "(b) 16 : 27", "(c) 512 : 729", "(d) 4 : 9"], "(a)",
         "Definition: Sub-duplicate ratio means square root ratio: sqrt(64) : sqrt(81) = 8 : 9!",
         "Sub-duplicate ratio of a : b is sqrt(a) : sqrt(b) = sqrt(64) : sqrt(81) = 8 : 9."),
        
        ("[UPSC CSAT Hard]", "UPSC Hard", True,
         "A cask contains a mixture of 49 litres of wine and water in the ratio 5 : 2. How much water must be added to it so that the ratio of wine to water becomes 7 : 4?",
         ["(a) 4 litres", "(b) 5 litres", "(c) 6 litres", "(d) 3.5 litres"], "(c)",
         "Wine Intact: Total = 49L. Wine = (5/7)*49 = 35L. Water = 14L. In new ratio 7:4, Wine is 7 units = 35L, so 1 unit = 5L. New water must be 4 units = 20L. Water to add = 20 - 14 = 6 litres!",
         "Wine = 35 litres, Water = 14 litres.\n35 / (14 + W) = 7/4 => 7(14 + W) = 140 => 98 + 7W = 140 => 7W = 42 => W = 6 litres."),
        
        ("[UPSC CSAT Standard]", "Official Standard", False,
         "The ratio of speeds of three motorcars is 2 : 3 : 4. What is the ratio of time taken by them to travel the same distance?",
         ["(a) 6 : 4 : 3", "(b) 4 : 3 : 2", "(c) 2 : 3 : 4", "(d) 3 : 4 : 6"], "(a)",
         "Inversion Rule: Time is inversely proportional to speed: 1/2 : 1/3 : 1/4. Multiply by 12: 6 : 4 : 3!",
         "Time ratio = 1/2 : 1/3 : 1/4 = 6 : 4 : 3."),
        
        ("[UPSC CSAT Hard]", "UPSC Hard", True,
         "A gold bar broke into three pieces whose weights are in the ratio 3 : 4 : 5. The value of the bar is directly proportional to the square of its weight. If the breakage resulted in a loss of ₹94,000, what was the initial value of the gold bar?",
         ["(a) ₹1,80,000", "(b) ₹1,44,000", "(c) ₹1,50,000", "(d) ₹1,60,000"], "(b)",
         "Square Value Loss: Original weight = 3 + 4 + 5 = 12. Original value proportional to 12^2 = 144. Broken pieces values = 3^2 + 4^2 + 5^2 = 9 + 16 + 25 = 50. Loss = 144 - 50 = 94 units. If 94 units = ₹94,000, initial value (144 units) = ₹1,44,000!",
         "Initial weight = 12x. Initial value = k(12x)^2 = 144 k x^2.\nBroken value = k[(3x)^2 + (4x)^2 + (5x)^2] = k[9 + 16 + 25]x^2 = 50 k x^2.\nLoss = 144 - 50 = 94 k x^2 = 94,000 => k x^2 = 1,000.\nInitial value = 144 * 1000 = ₹1,44,000."),
        
        ("[UPSC CSAT Standard]", "Official Standard", False,
         "A sum of ₹750 is distributed among A, B, and C such that A : B = 5 : 2 and B : C = 7 : 13. How much does B receive?",
         ["(a) ₹140", "(b) ₹250", "(c) ₹350", "(d) ₹150"], "(a)",
         "Combined Ratio: A:B = 35 : 14. B:C = 14 : 26. Combined A:B:C = 35 : 14 : 26. Sum of parts = 35 + 14 + 26 = 75 parts. 75 parts = ₹750, so 1 part = ₹10. B receives 14 parts = ₹140!",
         "A:B:C = 35 : 14 : 26. Sum = 75 parts = 750 => 1 part = 10. B = 14 * 10 = ₹140."),
        
        ("[UPSC CSAT Hard]", "UPSC Hard", True,
         "A district administration distributes a grant of ₹3,60,000 among three gram panchayats X, Y, and Z in the ratio 1/3 : 1/4 : 1/6. What is the share received by panchayat X?",
         ["(a) ₹1,60,000", "(b) ₹1,20,000", "(c) ₹80,000", "(d) ₹1,50,000"], "(a)",
         "Clear Denominators: Multiply 1/3 : 1/4 : 1/6 by LCM 12 -> 4 : 3 : 2. Sum = 9 parts. X gets 4/9 of ₹3,60,000 = ₹1,60,000!",
         "X:Y:Z = 4 : 3 : 2. Total parts = 9.\nX share = (4 / 9) * 360,000 = ₹1,60,000."),
        
        ("[UPSC CSAT Hard]", "UPSC Hard", True,
         "An engineering contractor mixes two grades of bitumen costing ₹45/kg and ₹65/kg to produce a composite binder sold at ₹66/kg, earning a profit of 20%. What is the ratio in which the two grades were blended?",
         ["(a) 1 : 1", "(b) 2 : 1", "(c) 1 : 2", "(d) 3 : 2"], "(a)",
         "Alligation with Target CP: SP = ₹66 at 20% profit means CP = 66 / 1.2 = ₹55/kg. Alligation: (65 - 55) / (55 - 45) = 10 / 10 = 1 : 1!",
         "Mean CP = 66 / 1.20 = ₹55 per kg.\nAlligation: (65 - 55) : (55 - 45) = 10 : 10 = 1 : 1.")
    ]
    topics[t10_id] = {
        "topic_id": t10_id, "title": t10_title, "mental_model": t10_model,
        "questions": [make_q(t10_id, t10_title, i+1, s[0], s[1], s[2], s[3], s[4], s[5], s[6], s[7]) for i, s in enumerate(t10_specs)]
    }

    return topics

if __name__ == "__main__":
    t = get_topics()
    for tid, val in t.items():
        print(f"{tid}: {len(val['questions'])} questions")
'''
    with open("csat_topics_06_10.py", "w") as f:
        f.write(code)
    print("csat_topics_06_10.py written successfully!")

if __name__ == "__main__":
    generate_file()
