import json
import datetime

start_date = datetime.date(2026, 11, 24)

# Load existing microtopics for sub-items and sources
with open('micro-topics/microtopics-db.json', 'r') as f:
    micro_db = json.load(f)

# Master plan topics for all 180 days
# Structure: (DayNum, Subject, TopicTitle, CoreSource, MicroTopicID, SubItemsList, CSATTopic, NeilSirQuote)

plan_specs = [
    # WEEK 1 (Days 1-7): Polity - Parliament & Executive
    (1, "Polity", "Parliament: Composition, Sessions & Presiding Officers", "Laxmikanth Ch 22", "pol-01", 
     [
         "Composition of Rajya Sabha (Max 250, Art 80) & Lok Sabha (Max 550, Art 81)",
         "Presiding Officers: Speaker election, powers, casting vote (Art 100) and Deputy Speaker constitutional role",
         "Sessions of Parliament: Prorogation vs Adjournment vs Dissolution (Art 85)",
         "Anti-Defection Law (10th Schedule) & Speaker's disqualification powers under Kihoto Hollohan precedent"
     ],
     "UNGIST Ch 1: Number System — Unit Digit Cyclicity (Powers of 2, 3, 7, 8)",
     "UPSC is not testing photographic memory; it tests your clarity under ambiguity. Eliminate the extreme statement first."
    ),
    (2, "Polity", "Parliament: Legislative & Financial Procedures (Money Bills, Budget)", "Laxmikanth Ch 22", "pol-02",
     [
         "Money Bill (Art 110): Speaker's final certificate, RS 14-day limit, No joint sitting",
         "Financial Bills (Category I Art 117(1) vs Category II Art 117(3)) distinctions",
         "Annual Financial Statement (Art 112), Guillotine, Cut Motions (Policy, Economy, Token)",
         "Consolidated Fund of India (Art 266) vs Contingency Fund (Art 267) withdrawal mandates"
     ],
     "UNGIST Ch 1: Number System — Remainder Theorem & Successive Division",
     "A Money Bill cannot be referred to a Joint Sitting. When UPSC presents an absolute assertion, check the constitutional exceptions."
    ),
    (3, "Polity", "Parliamentary Committees, Privileges & Motions", "Laxmikanth Ch 22 & 23", "pol-01",
     [
         "Financial Committees: Public Accounts Committee (22 members, opposition chair convention), Estimates Committee (30 LS only)",
         "Committee on Public Undertakings (22 members) & Departmentally Related Standing Committees (31 members)",
         "Parliamentary Privileges (Art 105): Collective vs Individual privileges (Freedom of speech, 40-day arrest immunity)",
         "Parliamentary Motions: No-Confidence vs Censure Motion, Calling Attention, Adjournment Motion"
     ],
     "UNGIST Ch 1: Number System — Divisibility Rules (3, 7, 9, 11, 13)",
     "The Estimates Committee has NO members from Rajya Sabha. UPSC loves testing asymmetric parliamentary compositions."
    ),
    (4, "Polity", "Union Executive: President & Vice-President Elections and Powers", "Laxmikanth Ch 17 & 18", "pol-03",
     [
         "Presidential Electoral College (Art 54): Elected MLAs + MPs (No nominated members, No MLCs)",
         "Value of MLA vote based on 1971 census formula & Single Transferable Vote system",
         "Pardoning Power of President (Art 72) vs Governor (Art 161) — Death sentence & Court Martial nuances",
         "Vice-President: Ex-officio Chairman of Rajya Sabha (Art 64) and removal resolution in RS with LS agreement"
     ],
     "UNGIST Ch 1: Number System — Factors, Multiples & Prime Factorization",
     "Pardoning power under Art 72 is subject to limited judicial review (Epuru Sudhakar case). No constitutional authority holds arbitrary discretion."
    ),
    (5, "Polity", "State Executive: Governor Discretionary Powers & Ordinances", "Laxmikanth Ch 30", "pol-03",
     [
         "Constitutional Discretion (Art 163): Situational vs explicit constitutional discretion",
         "Assent to Bills (Art 200): Withhold assent, Return for reconsideration, Reserve for President (Art 201)",
         "Ordinance-Making Power: President (Art 123) vs Governor (Art 213) — DC Wadhwa & Krishna Kumar rulings",
         "Immunity of Governor (Art 361) during office term from civil and criminal proceedings"
     ],
     "UNGIST Ch 1: Number System — Number of Trailing Zeroes in Factorials (n/5 + n/25...)",
     "Article 200 does not permit pocket veto indefinitely. Constitutional morality requires timely action on legislative will."
    ),
    (6, "Polity", "Council of Ministers, Cabinet Committees & PMO", "Laxmikanth Ch 19 & 20", "pol-03",
     [
         "Collective Responsibility to Lok Sabha (Art 75(3)) vs Individual Responsibility to President (Art 75(2))",
         "91st Constitutional Amendment 2003: 15% limit on Council of Ministers strength",
         "Cabinet Committees: Appointments Committee, Cabinet Committee on Security (CCS), Economic Affairs (CCEA)",
         "PMO vs Cabinet Secretariat: Role of Cabinet Secretary as head of Civil Services"
     ],
     "UNGIST Ch 1: Number System — LCM and HCF Mental Shortcuts",
     "Ministers hold office during the pleasure of the President, but dismissal requires Prime Minister's advice. Collective responsibility is supreme."
    ),
    (7, "Polity", "Weekly Consolidation 1: Polity Executive & Legislature Sectional Mock Test", "Weekly Revision Mode", "pol-01",
     [
         "Consolidate error notebook on Parliament, President, Governor, and Money Bills",
         "Attempt 100-Question Polity Sectional Mock Test under timed conditions (06:00-08:00 AM)",
         "Forensic analysis of incorrect and guessed options",
         "Map negative-mark questions against careless reading vs factual blind spots"
     ],
     "UNGIST Ch 1: Number System — 2019-2023 UPSC PYQ Marathon Drill",
     "Sunday Mock is not an evaluation of your worth; it is an x-ray of your blind spots. Fix the error, never fear the score."
    ),

    # WEEK 2 (Days 8-14): Fundamental Rights, DPSP & Basic Structure
    (8, "Polity", "Fundamental Rights: Concept of State (Art 12), Judicial Review (Art 13) & Equality (Art 14-16)", "Laxmikanth Ch 7", "pol-04",
     [
         "Definition of 'State' under Art 12: Includes statutory & non-statutory bodies acting as state instrumentality (Ajay Hasia)",
         "Article 13: Laws inconsistent with FRs are void; Doctrine of Severability & Eclipse",
         "Article 14: Equality before Law (British) vs Equal Protection of Laws (American) & Intelligible Differentia",
         "Articles 15 & 16: Non-discrimination grounds, creamy layer concept (Indra Sawhney), EWS quota (103rd CA)"
     ],
     "UNGIST Ch 6: Percentages — Fraction to Percentage Conversion Table (1/6 = 16.66%, 1/7 = 14.28%)",
     "Article 14 permits reasonable classification, not class legislation. Understand the rationale before memorizing case laws."
    ),
    (9, "Polity", "Fundamental Rights: Six Freedoms (Art 19) & Reasonable Restrictions", "Laxmikanth Ch 7", "pol-04",
     [
         "Article 19(1)(a) to (g): Speech, Assembly, Association, Movement, Residence, Profession",
         "Reasonable Restrictions: Exhaustive grounds under Art 19(2) (Public order, decency, sovereignty, friendly relations)",
         "Right to Strike vs Right to Form Associations (TK Rangarajan case)",
         "Sedition (Sec 124A IPC / BNS) vs Freedom of Speech in light of Kedar Nath Singh precedent"
     ],
     "UNGIST Ch 6: Percentages — Successive Percentage Change Formula (a + b + ab/100)",
     "Freedom of speech does not include freedom to create public disorder. Every right in Part III is balanced against state security."
    ),
    (10, "Polity", "Fundamental Rights: Life & Personal Liberty (Art 21, 21A, 22) & Privacy", "Laxmikanth Ch 7", "pol-04",
     [
         "Procedure Established by Law vs Due Process of Law (AK Gopalan to Maneka Gandhi transition)",
         "Right to Privacy: KS Puttaswamy ruling (Three-fold test: Legality, Need, Proportionality)",
         "Article 21A: Right to Education (86th CA) & RTE Act provisions",
         "Article 22: Preventive Detention safeguards (3-month Advisory Board limit, grounds of detention)"
     ],
     "UNGIST Ch 7: Profit and Loss — Cost Price vs Selling Price, Markup and Discount",
     "Due Process of law requires not just a enacted law, but a law that is just, fair, and reasonable."
    ),
    (11, "Polity", "Fundamental Rights: Freedom of Religion (Art 25-28) & Constitutional Remedies (Art 32)", "Laxmikanth Ch 7", "pol-04",
     [
         "Article 25 (Individual) vs Article 26 (Denomination): Essential Religious Practices doctrine",
         "Articles 27 & 28: No tax for religious promotion; Religious instruction in state-aided institutions",
         "Article 32: Heart and Soul of Constitution; Direct access to SC for FR violation",
         "The Five Writs: Habeas Corpus (against private too), Mandamus, Prohibition, Certiorari, Quo-Warranto"
     ],
     "UNGIST Ch 7: Profit and Loss — Dishonest Dealer & Faulty Balance Problems",
     "Mandamus cannot be issued against a private individual or discretionary duty. Learn writ boundaries cold."
    ),
    (12, "Polity", "Directive Principles of State Policy (DPSP) & Fundamental Duties", "Laxmikanth Ch 8 & 9", "pol-08",
     [
         "Classification of DPSP: Socialistic (Art 38, 39, 41), Gandhian (Art 40, 43, 47), Liberal-Intellectual (Art 44, 48, 50, 51)",
         "Minerva Mills case: Harmony between Part III and Part IV forms basic structure",
         "Uniform Civil Code (Art 44) & Separation of Judiciary from Executive (Art 50)",
         "Fundamental Duties (Part IV-A, Art 51A): Swaran Singh Committee, 42nd CA, 86th CA (11th duty)"
     ],
     "UNGIST Ch 2: Ratio and Proportion — Direct & Inverse Variation, Compounded Ratio",
     "Fundamental Duties are non-enforceable directly, but courts use them to interpret constitutional statutes and reasonable restrictions."
    ),
    (13, "Polity", "Basic Structure Doctrine, Preamble & Constitutional Amendments (Art 368)", "Laxmikanth Ch 10 & 11", "pol-11",
     [
         "Preamble: Sovereign, Socialist, Secular, Democratic, Republic; Integral part of Constitution (Kesavananda)",
         "42nd Amendment changes: Added Socialist, Secular, Integrity to Preamble",
         "Evolution of Basic Structure: Shankari Prasad -> Golaknath -> Kesavananda Bharati -> Minerva Mills",
         "Amendment Procedure (Art 368): Special majority vs Special majority with 50% State ratification"
     ],
     "UNGIST Ch 3: Mixture and Alligation — The Cross-Method for Rapid Ratio Solutions",
     "The Preamble is non-justiciable on its own, but serves as the beacon light for interpreting constitutional ambiguity."
    ),
    (14, "Polity", "Weekly Consolidation 2: Rights, Duties & Amendment Sectional Mock Test", "Weekly Revision Mode", "pol-04",
     [
         "Revise Articles 12 through 51A comparative tabular summary",
         "Attempt 100-Question Rights & Basic Structure Sectional Mock Test (06:00-08:00 AM)",
         "Detailed review of writ petitions, reasonable restrictions, and DPSP articles",
         "Catalogue high-yield exceptions into Personal Revision Flashcards"
     ],
     "UNGIST Ch 2 & 3: Ratio, Mixture & Alligation — UPSC CSAT PYQ Marathon",
     "Confidence is not the absence of doubt; it is the presence of disciplined method when doubt arises."
    ),

    # WEEK 3 (Days 15-21): Judiciary, Federalism & Constitutional Bodies
    (15, "Polity", "Supreme Court: Jurisdiction, Independence & Collegium System", "Laxmikanth Ch 26", "pol-05",
     [
         "Appointment of Judges: NJAC 99th CA struck down in Fourth Judges case (2015); Collegium structure (CJI + 4 senior-most)",
         "Original Jurisdiction (Art 131) — Disputes between Centre and States (Excludes treaty disputes & commercial claims)",
         "Appellate Jurisdiction (Art 132-134), Special Leave Petition (Art 136), Advisory Jurisdiction (Art 143)",
         "Court of Record (Art 129), Power to punish for Contempt, Curative Petition (Rupa Ashok Hurra)"
     ],
     "UNGIST Ch 5: Averages — The Physical Balance Scale Mental Model (Deviations from Mean)",
     "Article 131 original jurisdiction does not extend to private individuals suing the Union. Precision of jurisdictional scope is mandatory."
    ),
    (16, "Polity", "High Courts, Subordinate Judiciary & Dedicated Tribunals", "Laxmikanth Ch 34 & 35", "pol-05",
     [
         "High Court Jurisdiction: Writ jurisdiction under Art 226 is wider than SC Art 32 (includes legal rights)",
         "Appointment of HC Judges (Art 217) & Transfer procedure under CJI + 4 senior-most recommendation",
         "Subordinate Courts: District Judge appointment (Art 233) by Governor in consultation with High Court",
         "Tribunals (Part XIV-A): Administrative Tribunals (Art 323A) vs Other Tribunals (Art 323B) — L. Chandra Kumar ruling"
     ],
     "UNGIST Ch 5: Averages — Weighted Average and Replacement Problems",
     "Judicial review under Articles 32 and 226 cannot be ousted by legislative tribunals (L. Chandra Kumar). Basic structure stands unyielding."
    ),
    (17, "Polity", "Federalism & Centre-State Relations (Legislative, Admin & Financial)", "Laxmikanth Ch 14 & 15", "pol-09",
     [
         "7th Schedule Lists: Union (100), State (61), Concurrent (52); Residuary powers with Parliament (Art 248)",
         "Parliamentary legislation on State List: Art 249 (National interest/RS 2/3), Art 250 (Emergency), Art 252 (State request)",
         "Administrative Relations: Centre directions to States (Art 256, 257) & Consequences of non-compliance (Art 365)",
         "Financial Relations: GST Council (Art 279A), Finance Commission recommendations (Art 280), Grants-in-aid (Art 275 vs 282)"
     ],
     "UNGIST Ch 4: Problems Based on Ages — Linear Equation Elimination Shortcuts",
     "Residuary power of legislation rests with the Centre in India, unlike the US or Australia. Remember the Canadian federal tilt."
    ),
    (18, "Polity", "Emergency Provisions: Art 352, 356, 360 & Fundamental Rights Impact", "Laxmikanth Ch 16", "pol-09",
     [
         "National Emergency (Art 352): Grounds (War, External Aggression, Armed Rebellion — 44th CA removed 'internal disturbance')",
         "Approval by both Houses within 1 month by special majority; Periodic approval every 6 months",
         "Impact on Fundamental Rights: Art 358 (Suspends Art 19 automatically on external war) vs Art 359 (Presidential order suspends enforcement; Art 20 & 21 never suspended)",
         "President's Rule (Art 356) safeguards: SR Bommai judgment guidelines (Judicial review, assembly dissolution only after parliamentary approval)"
     ],
     "UNGIST Ch 11: Time and Work — The LCM Total-Units Method (Zero Fraction Math)",
     "Articles 20 and 21 can never be suspended during any Emergency. The 44th Amendment erected an impenetrable shield around liberty."
    ),
    (19, "Polity", "Local Governance: Panchayati Raj (73rd CA) & Municipalities (74th CA)", "Laxmikanth Ch 38 & 39", "pol-07",
     [
         "Compulsory vs Voluntary provisions of 73rd Amendment (11th Schedule, 29 functional items)",
         "Three-tier system (Gram, Intermediate, District); Gram Sabha as foundation (Art 243A)",
         "State Election Commission (Art 243K) & State Finance Commission (Art 243I) every 5 years",
         "PESA Act 1996: Extension to 5th Schedule areas, Gram Sabha mandatory powers on minor forest produce & land acquisition"
     ],
     "UNGIST Ch 11: Time and Work — Efficiency Ratios & Alternate Day Work Puzzles",
     "State Election Commissioners are removed in the same manner as a High Court Judge. Constitutional autonomy protects local grassroots democracy."
    ),
    (20, "Polity", "Constitutional & Non-Constitutional Bodies (ECI, CAG, FC, UPSC, NITI Aayog)", "Laxmikanth Part VII", "pol-06",
     [
         "Election Commission of India (Art 324): CEC vs Election Commissioners status and removal process",
         "Comptroller and Auditor General (Art 148): Guardian of Public Purse, audits Appropriation & Finance Accounts",
         "Finance Commission (Art 280): 16th FC Terms of Reference, devolution formula (horizontal vs vertical)",
         "Non-Constitutional Bodies: NITI Aayog (Executive resolution), NHRC (Statutory, PHR Act 1993), Lokpal"
     ],
     "UNGIST Ch 12: Pipes and Cisterns — Negative Work Units (Inlet vs Outlet Rates)",
     "The CAG audits the accounts of Union and States, but does not control the issue of money from the Consolidated Fund like the British CAG."
    ),
    (21, "Polity", "Weekly Consolidation 3: Complete Polity & Constitution Full Sectional Test", "Weekly Revision Mode", "pol-01",
     [
         "Comprehensive review of Constitutional Articles 1 to 395 and all 12 Schedules",
         "Attempt 100-Question Polity Grand Sectional Mock Test (06:00-08:00 AM)",
         "Calculate Net Marks: Total Correct x 2 - Total Incorrect x 0.66",
         "Identify top 3 recurring Polity error patterns (e.g. Constitutional vs Statutory confusion)"
     ],
     "UNGIST Ch 11 & 12: Time, Work & Cisterns — UPSC CSAT PYQ Marathon",
     "Every question you miss in a practice mock is a question you will never miss in the examination hall. Cherish the mistake."
    ),

    # WEEK 4 (Days 22-28): Economy - Macro Concepts & Monetary Policy
    (22, "Economy", "National Income Accounting: GDP, GVA, Factor Cost vs Market Price", "NCERT Class 12 Macro", "eco-09",
     [
         "GDP calculation approaches: Production (GVA), Expenditure (C + I + G + NX), Income",
         "GVA at Basic Prices = GVA at Factor Cost + Production Taxes - Production Subsidies",
         "GDP at Market Prices = GVA at Basic Prices + Product Taxes - Product Subsidies",
         "Real GDP vs Nominal GDP, GDP Deflator calculation & base year revisions (2011-12)"
     ],
     "UNGIST Ch 8: Time, Speed and Distance — Unit Conversion & Basic Speed-Time Inverses",
     "GVA captures supply-side sector contributions; GDP captures demand-side expenditures. Keep the accounting boundaries sharp."
    ),
    (23, "Economy", "Inflation Dynamics: CPI vs WPI, GDP Deflator & Core Inflation", "Economic Survey / MOSPI", "eco-07",
     [
         "CPI (Combined): Base 2012, Released by NSO/MoSPI, Food weightage ~45.86%, includes services",
         "WPI: Base 2011-12, Released by Office of Economic Adviser (DPIIT), Manufacturing weight ~64.23%, NO services",
         "Headline Inflation (All items) vs Core Inflation (Excludes volatile Food and Fuel)",
         "Producer Price Index (PPI) vs WPI differences & Inflation targeting mandate under Urjit Patel Committee"
     ],
     "UNGIST Ch 8: Time, Speed and Distance — Average Speed Harmonic Formula (2xy/(x+y))",
     "WPI does not include services; CPI gives nearly half its weight to food and beverages. Never confuse the two indices."
    ),
    (24, "Economy", "Monetary Policy Framework: MPC, Policy Rates & Liquidity Management", "Vivek Singh / Ramesh Singh", "eco-01",
     [
         "Flexible Inflation Targeting: CPI 4% +/- 2% band under RBI Act 1934 Section 45ZB",
         "Monetary Policy Committee (MPC): 6 members (3 RBI + 3 Govt nominated), Governor casting vote",
         "Policy Rates: Repo Rate, Reverse Repo, Standing Deposit Facility (SDF, non-collateralized floor)",
         "Marginal Standing Facility (MSF) & Bank Rate as penal rates against SLR securities"
     ],
     "UNGIST Ch 9: Trains — Crossing a Pole vs Crossing a Platform (Distance = Train + Platform)",
     "SDF allows RBI to absorb excess liquidity without offering government securities as collateral. A modern tool born out of demonetization lessons."
    ),
    (25, "Economy", "Money Supply Aggregates, Money Multiplier & Open Market Operations", "NCERT Class 12 / Mrunal", "eco-01",
     [
         "Reserve Money (M0) / High Powered Money: Currency in circulation + Bankers' deposits with RBI + Other deposits",
         "Money Aggregates: M1 (Narrow money: Currency + Demand Deposits), M2, M3 (Broad money: M1 + Time Deposits), M4",
         "Money Multiplier = M3 / M0; Impact of Cash Reserve Ratio (CRR) and currency-deposit ratio",
         "Open Market Operations (OMO): Outright purchase/sale of G-Secs vs Operation Twist (Yield curve flattening)"
     ],
     "UNGIST Ch 9: Trains — Relative Speed (Same Direction: S1 - S2, Opposite: S1 + S2)",
     "When RBI increases CRR, the money multiplier decreases, draining liquidity from the banking system. Track the transmission mechanism."
    ),
    (26, "Economy", "Banking Sector Architecture: Commercial Banks, NPA Resolution & IBC", "Ramesh Singh / Budget", "eco-02",
     [
         "Scheduled Commercial Banks (PSBs, Private, Foreign) & Basel III capital adequacy (CAR/CRAR, Tier 1/2 capital)",
         "Asset Classification: Standard, Sub-standard (NPA <= 12m), Doubtful (>12m), Loss assets",
         "Insolvency and Bankruptcy Code (IBC 2016): Corporate Insolvency Resolution Process (CIRP), 330-day timeline, NCLT role",
         "Prompt Corrective Action (PCA) framework triggers: Capital, Asset quality, Leverage"
     ],
     "UNGIST Ch 10: Boats and Streams — Upstream (u - v) vs Downstream (u + v) Dynamics",
     "IBC shifted power from borrower to creditor. Resolution is overseen by the Committee of Creditors with a 66% voting threshold."
    ),
    (27, "Economy", "Financial Inclusion, Priority Sector Lending & Differentiated Banks", "RBI FAQs / Mrunal", "eco-02",
     [
         "Priority Sector Lending (PSL): 40% target for domestic commercial banks (Agriculture 18%, Micro 7.5%, Weaker sections 12%)",
         "Priority Sector Lending Certificates (PSLC): Trading compliance without transferring loans",
         "Small Finance Banks (SFBs) vs Payments Banks: SFBs can lend; Payments banks can ONLY accept demand deposits up to Rs 2 lakh (No lending)",
         "PM Jan Dhan Yojana, Lead Bank Scheme & National Strategy for Financial Inclusion"
     ],
     "UNGIST Ch 10: Boats and Streams — Solving Distance and Round-Trip Problems",
     "Payments Banks cannot issue credit cards or grant loans. They can only issue debit cards and accept demand deposits."
    ),
    (28, "Economy", "Weekly Consolidation 4: Macroeconomics & Banking Sectional Mock Test", "Weekly Revision Mode", "eco-01",
     [
         "Review formula flashcards: Money Multiplier, GVA vs GDP, CPI weights, Basel III ratios",
         "Attempt 100-Question Macro & Banking Sectional Mock Test (06:00-08:00 AM)",
         "Analyze every question where you were torn between 2 options",
         "Log economy terminology traps into your Notes tab"
     ],
     "UNGIST Ch 8-10: Speed, Distance, Trains & Boats — UPSC CSAT PYQ Marathon",
     "Speed without calibration produces negative marks. In economy questions, read the word 'NOT' three times before marking."
    ),

    # WEEK 5 (Days 29-35): Economy - Fiscal Policy, Financial Markets & External Sector
    (29, "Economy", "Fiscal Policy: Union Budget Components, Revenue vs Capital Account", "Budget Document / Laxmikanth", "eco-05",
     [
         "Revenue Account: Revenue Receipts (Tax & Non-tax: dividends, interest, fees) vs Revenue Expenditure (Subsidies, interest payments, salaries)",
         "Capital Account: Capital Receipts (Borrowings, Disinvestment, Loan recovery) vs Capital Expenditure (Asset creation, infrastructure, loan dispersal)",
         "Effective Revenue Deficit = Revenue Deficit - Grants for Creation of Capital Assets",
         "Quality of Expenditure: Capex vs Opex multiplier effect on GDP growth"
     ],
     "UNGIST Ch 13: Permutations and Combinations — Fundamental Counting Principle & Factorials",
     "Interest payment on past debt is Revenue Expenditure because it creates no new productive physical asset. Classify transactions by asset impact."
    ),
    (30, "Economy", "Deficits & Fiscal Responsibility: Fiscal Deficit, FRBM Act & Debt Dynamics", "Economic Survey", "eco-05",
     [
         "Fiscal Deficit = Total Expenditure - (Revenue Receipts + Non-debt Capital Receipts); It equals net annual borrowing",
         "Primary Deficit = Fiscal Deficit - Interest Payments (Shows current year fiscal profligacy)",
         "FRBM Act 2003: NK Singh Committee recommendations (Debt-to-GDP target: 60% combined, 40% Centre, 20% States)",
         "Escape Clause under FRBM: National security, war, calamity, structural reforms (Allows 0.5% GDP deviation)"
     ],
     "UNGIST Ch 13: Permutations and Combinations — Arrangement with Restrictions (Tie & Gap Methods)",
     "Primary Deficit zero means the government is borrowing purely to finance interest on past debt. Understand the diagnostic meaning of each deficit."
    ),
    (31, "Economy", "Taxation Architecture: Direct vs Indirect Taxes, GST Council & Cess/Surcharge", "Economic Survey", "eco-05",
     [
         "Direct Tax: Progressive, Income tax, Corporate tax (Equalization levy, Minimum Alternate Tax - MAT)",
         "Indirect Tax: Regressive, Goods and Services Tax (Dual GST: CGST, SGST, IGST on inter-state)",
         "GST Council (Art 279A): Centre has 1/3 weight, States have 2/3 weight; 3/4 majority required for decision",
         "Cess (Earmarked for specific purpose) vs Surcharge (General revenue): Not shared with States in Finance Commission divisible pool"
     ],
     "UNGIST Ch 13: Permutations and Combinations — Combination Selection & The Handshake Theorem",
     "Cess and surcharges do not go into the divisible pool shared with States under Article 280. A major friction point in fiscal federalism."
    ),
    (32, "Economy", "Financial Markets: Money Market vs Capital Market, Bonds & Yield Curve", "Mrunal / SEBI", "eco-06",
     [
         "Money Market: Short term (< 1 year); Treasury Bills (91, 182, 364 days, issued at discount), Commercial Paper, Certificate of Deposit",
         "Capital Market: Long term; Shares, Bonds, Debentures; Primary vs Secondary market (SEBI regulation)",
         "Bond Yield Dynamics: Bond Price is inversely proportional to Bond Yield; Inverted Yield Curve as recession indicator",
         "Sovereign Green Bonds, Masala Bonds (Rupee-denominated overseas bonds), Sureties"
     ],
     "UNGIST Ch 14: Probability — Basic Event Probability (Favorable Outcomes / Total Outcomes)",
     "When interest rates rise in an economy, existing bond prices fall, pushing bond yields higher. Bond mathematics is simple inverse physics."
    ),
    (33, "Economy", "External Sector: Balance of Payments (BoP), Current Account Deficit & Forex", "NCERT Class 12 Macro", "eco-04",
     [
         "Balance of Payments: Current Account (Trade in goods + Invisibles: services, transfers, income) vs Capital Account (FDI, FPI, ECBs, NRI deposits)",
         "Current Account Deficit (CAD): Sustainable limits & Financing CAD through non-debt creating capital flows (FDI)",
         "Foreign Exchange Reserves: Foreign Currency Assets (FCA), Gold, SDRs (Special Drawing Rights at IMF), Reserve Tranche Position (RTP)",
         "FDI (Active management, long term, non-debt) vs FPI (Passive investment, hot money, flighty)"
     ],
     "UNGIST Ch 14: Probability — Independent Events & Conditional Probability Intuition",
     "Remittances sent by Indian diaspora abroad are categorized as Unilateral Transfers under the Current Account Invisibles."
    ),
    (34, "Economy", "Exchange Rate Regimes: NEER, REER, Currency Depreciation & Convertibility", "Ramesh Singh", "eco-04",
     [
         "Nominal Effective Exchange Rate (NEER) vs Real Effective Exchange Rate (REER = NEER adjusted for inflation differentials)",
         "Overvalued REER (> 100) implies loss of export competitiveness; Undervalued REER boosts exports",
         "Current Account Convertibility (Full in India since 1994, Art VIII of IMF) vs Capital Account Convertibility (Partial, Tarapore Committee)",
         "Currency Depreciation vs Devaluation (Market-driven vs Govt-decreed)"
     ],
     "UNGIST Ch 14: Probability — Dice & Coin Tossing Problems (UPSC Standard Patterns)",
     "If India's inflation is higher than trading partners and NEER remains constant, REER increases, signaling that Indian goods are becoming less competitive."
    ),
    (35, "Economy", "Weekly Consolidation 5: Fiscal, External & Financial Markets Sectional Mock", "Weekly Revision Mode", "eco-04",
     [
         "Synthesize BoP, Fiscal Deficit, Bond Yields, and Exchange Rate linkages",
         "Attempt 100-Question Fiscal & External Sector Mock Test (06:00-08:00 AM)",
         "Review every macroeconomic cause-and-effect relationship tested",
         "Refine elimination strategies for economic statement-based questions"
     ],
     "UNGIST Ch 13 & 14: Permutation, Combination & Probability — UPSC CSAT PYQ Marathon",
     "In UPSC economy, every action causes a ripple. Always ask: 'If RBI does this, what happens to the rupee, inflation, and bond yields?'"
    ),

    # WEEK 6 (Days 36-42): Agriculture, Food Security & Digital Economy
    (36, "Economy", "Agriculture: Cropping Patterns, MSP Determination & CACP Formulations", "Mrunal / Agricoop", "eco-03",
     [
         "Major Crops: Kharif (Rice, Cotton, Soyabean), Rabi (Wheat, Mustard, Gram), Zaid (Watermelon, Fodder)",
         "Minimum Support Price (MSP): 22 mandated crops + Fair & Remunerative Price (FRP) for Sugarcane",
         "CACP Cost Concepts: A2 (Paid-out costs), A2 + FL (Family labour), C2 (Comprehensive cost including land rent)",
         "Government formula: MSP set at minimum 1.5 times of A2 + FL cost of production"
     ],
     "UNGIST Ch 18: Clocks — Angle between Hands Formula (|30H - (11/2)M|) & Overlap Points",
     "CACP recommends MSP, but the final decision is taken by the Cabinet Committee on Economic Affairs (CCEA) chaired by the PM."
    ),
    (37, "Economy", "Agricultural Subsidies & WTO Agreements: Amber, Blue & Green Boxes", "Economic Survey", "eco-03",
     [
         "Input Subsidies: Fertilizer subsidy (Nutrient Based Subsidy - NBS scheme, Urea neem-coating), Power subsidy, Canal irrigation",
         "WTO Agreement on Agriculture (AoA): Green Box (Non-trade distorting: R&D, decoupled support, no limit)",
         "Blue Box (Direct payments linked to production limiting programs, no limit)",
         "Amber Box: Trade-distorting support subject to De Minimis limits (10% for developing, 5% for developed countries); Peace Clause"
     ],
     "UNGIST Ch 18: Clocks — Faulty Clocks (Gaining or Losing Time) Mental Calculations",
     "Urea is covered under statutory price control, while P&K fertilizers are covered under the Nutrient Based Subsidy (NBS) regime."
    ),
    (38, "Economy", "Food Security: Public Distribution System, Buffer Norms & FCI Restructuring", "Economic Survey", "eco-03",
     [
         "National Food Security Act (NFSA 2013): Covers up to 75% rural and 50% urban population; 5 kg/person/month",
         "Antyodaya Anna Yojana (AAY): 35 kg per family per month for the poorest of poor",
         "Food Subsidy Components = Consumer Subsidy (Economic cost of grain - Central Issue Price) + Carrying cost of buffer stock",
         "Shanta Kumar Committee Recommendations: Reduce NFSA coverage to 40%, direct cash transfer, outsource procurement"
     ],
     "UNGIST Ch 19: Calendar — The 7-Day Cycle & Odd Days Calculation (Ordinary Year = 1, Leap = 2)",
     "Economic cost of foodgrains incurred by FCI comprises: MSP + Procurement incidentals + Distribution costs."
    ),
    (39, "Economy", "Industry, Infrastructure & Manufacturing Policies: PLI, PM GatiShakti & Logistics", "DPIIT", "eco-02",
     [
         "Production Linked Incentive (PLI) Schemes: Objective to create global champions across 14 key sectors",
         "PM GatiShakti National Master Plan: Integrated multi-modal logistics platform for 16 ministries",
         "National Logistics Policy (NLP): Target to reduce logistics cost from 13-14% of GDP to global benchmark (8%)",
         "Special Economic Zones (SEZs) & DESH Bill (Development of Enterprise and Service Hubs)"
     ],
     "UNGIST Ch 19: Calendar — Day of the Week for Any Century Date (Century Odd Days: 100=5, 200=3, 300=1, 400=0)",
     "High logistics cost has historically acted as an invisible tariff on Indian exports. PM GatiShakti tackles departmental silos."
    ),
    (40, "Economy", "Digital Economy: FinTech, UPI, Central Bank Digital Currency (CBDC) & Account Aggregators", "RBI / MeitY", "eco-10",
     [
         "Unified Payments Interface (UPI): NPCI architecture, Immediate Payment Service (IMPS) backend, 2FA protocols",
         "Central Bank Digital Currency (CBDC / e-Rupee): Retail (e-Rupee-R) vs Wholesale (e-Rupee-W); Legal tender on blockchain/DLT",
         "Account Aggregator Framework: Consent-based financial data sharing under RBI NBFC-AA regulation",
         "Open Network for Digital Commerce (ONDC): Democratizing e-commerce away from platform-centric monopolies"
     ],
     "UNGIST Ch 21: Blood Relations — Family Tree Mapping with Gender and Generation Symbols",
     "e-Rupee is a direct sovereign liability of the RBI appearing on its balance sheet, unlike commercial bank money which is bank liability."
    ),
    (41, "Economy", "Poverty Estimation, Inequality & Human Development: Committees & MPI", "NITI Aayog / UNDP", "eco-11",
     [
         "Poverty Lines in India: Lakdawala (1993) -> Tendulkar (2009, based on MRP consumption basket) -> Rangarajan (2014, MMRP basket)",
         "Multidimensional Poverty Index (MPI): NITI Aayog national report; 3 dimensions (Health, Education, Standard of Living) & 12 indicators",
         "Gini Coefficient & Lorenz Curve: Measuring income and wealth inequality (0 = perfect equality, 1 = absolute inequality)",
         "Human Development Index (HDI) components: Life expectancy, Mean & Expected years of schooling, GNI per capita (PPP)"
     ],
     "UNGIST Ch 22: Direction Sense — The 8-Point Compass & Pythagoras Theorem Trajectory",
     "The National MPI uses the Alkire-Foster methodology, weighting Health, Education, and Living Standards equally (1/3 each)."
    ),
    (42, "Economy", "Weekly Consolidation 6: Complete Indian Economy Grand Sectional Mock Test", "Weekly Revision Mode", "eco-01",
     [
         "Synthesize full Indian Economy: Macro, Banking, Fiscal, External, Agriculture & Schemes",
         "Attempt 100-Question Complete Economy Grand Mock Test (06:00-08:00 AM)",
         "Analyze score trends across Weeks 4, 5, and 6",
         "Update personal one-page summary sheets for high-probability economic equations"
     ],
     "UNGIST Ch 18, 19, 21, 22: Clocks, Calendar, Blood & Direction — CSAT PYQ Marathon",
     "You are now conceptually grounded in Polity and Economy — the twin engines of GS Paper I. Trust the foundation."
    ),

    # WEEK 7 (Days 43-49): Geography - Physical Geomorphology & Climatology
    (43, "Geography", "Geomorphology: Earth's Interior, Continental Drift & Plate Tectonics", "NCERT Class 11 Physical", "geo-08",
     [
         "Earth's Layers: Crust, Mantle (Asthenosphere), Core (Outer liquid, Inner solid) & Discontinuities (Mohorovicic, Gutenberg)",
         "Seismic Waves: P-waves (Longitudinal, pass all mediums) vs S-waves (Transverse, cannot pass liquids); Shadow zones",
         "Continental Drift Theory (Alfred Wegener) & Sea Floor Spreading (Harry Hess, paleomagnetism)",
         "Plate Boundaries: Convergent (Subduction, trenches, volcanic arcs), Divergent (Mid-ocean ridges), Transform (San Andreas)"
     ],
     "UNGIST Ch 32: Syllogism — The Circle Venn Diagram Story Method (All, Some, No Rules)",
     "S-waves cannot travel through the outer core, proving it is molten. Earthquake waves act as nature's ultrasound of Earth."
    ),
    (44, "Geography", "Geomorphology: Earthquakes, Volcanoes & Fluvial/Karst Landforms", "NCERT Class 11 Physical", "geo-08",
     [
         "Earthquake Terminology: Focus/Hypocentre vs Epicentre; Mercalli (Intensity/damage) vs Richter (Magnitude/energy)",
         "Volcanic Landforms: Intrusive (Batholith, Laccolith, Sill, Dyke) vs Extrusive (Shield, Composite/Stratovolcano, Caldera)",
         "Fluvial Landforms: Erosional (Gorges, V-shaped valleys, Potholes) vs Depositional (Meanders, Oxbow lakes, Alluvial fans, Deltas)",
         "Karst Topography: Limestone solution features (Sinkholes, Stalactites, Stalagmites, Uvalas)"
     ],
     "UNGIST Ch 32: Syllogism — Either-Or Cases & Possibility Conclusions",
     "Stalactites grow down from the cave ceiling; stalagmites rise up from the cave floor. Never confuse the depositional pair."
    ),
    (45, "Geography", "Climatology: Atmosphere Structure, Insolation & Heat Budget", "NCERT Class 11 Physical", "geo-02",
     [
         "Atmosphere Layers: Troposphere (All weather, normal lapse rate 6.5C/km), Stratosphere (Ozone layer), Mesosphere, Thermosphere",
         "Insolation Factors: Angle of inclination of sun's rays, duration of daylight, atmospheric transparency",
         "Heat Budget of the Earth: Terrestrial radiation (Longwave) vs Solar insolation (Shortwave); Albedo effect",
         "Temperature Inversion: Ground inversion in winter valleys, conditions (Clear skies, calm air, long nights)"
     ],
     "UNGIST Ch 26: Venn Diagrams — Two & Three Set Intersections (Formula: |A U B U C|)",
     "The atmosphere is heated mainly from below by longwave terrestrial radiation, not directly by incoming shortwave solar rays."
    ),
    (46, "Geography", "Climatology: Planetary Winds, Pressure Belts & Tri-Cellular Circulation", "NCERT Class 11 Physical", "geo-02",
     [
         "Atmospheric Pressure Belts: Equatorial Low (Doldrums), Subtropical High (Horse Latitudes), Subpolar Low, Polar High",
         "Coriolis Force: Deflection to right in Northern Hemisphere, left in Southern Hemisphere; Proportional to latitude (Zero at equator)",
         "Tri-cellular Circulation: Hadley Cell (Tropical), Ferrel Cell (Mid-latitude), Polar Cell",
         "Planetary Winds: Trade Winds (Easterlies), Westerlies (Roaring Forties), Polar Easterlies"
     ],
     "UNGIST Ch 26: Venn Diagrams — Syllogistic Deduction without Drawing Complex Overlaps",
     "Coriolis force is zero at the equator, which is why tropical cyclones never form within 5 degrees north or south of the equator."
    ),
    (47, "Geography", "Climatology: Air Masses, Fronts, Cyclones (Tropical vs Extra-Tropical)", "NCERT Class 11 Physical", "geo-02",
     [
         "Air Masses: Maritime Tropical (mT), Continental Polar (cP); Frontogenesis (Warm front vs Cold front vs Occluded front)",
         "Tropical Cyclones: Sea surface temp > 27C, Coriolis force, low vertical wind shear, Eye of cyclone (calm, subsiding air)",
         "Extra-Tropical (Temperate) Cyclones: Frontal origin, travel West to East, affect North-West India as Western Disturbances",
         "Naming of Cyclones in North Indian Ocean: WMO / ESCAP panel guidelines"
     ],
     "UNGIST Ch 30: Seating Arrangements — Linear Row Arrangement (Facing North vs South)",
     "The eye of a tropical cyclone is characterized by calm winds, clear skies, and subsiding warm air — not violent thunderstorms."
    ),
    (48, "Geography", "Climatology: Indian Monsoon Mechanism, Jet Streams & ENSO (El Nino / IOD)", "NCERT Class 11 India Physical", "geo-02",
     [
         "Classical Thermal Theory (Halley) vs Modern Dynamic Theory (ITCZ shift over Tibetan Plateau)",
         "Role of Somali Jet & Tropical Easterly Jet (TEJ) in steering monsoon depressions",
         "ENSO Cycle: Normal Walker Circulation vs El Nino (Warm Pacific, weak monsoon) vs La Nina (Cold Pacific, strong monsoon)",
         "Indian Ocean Dipole (IOD): Positive IOD (Warm western IO, cool eastern IO -> boosts Indian monsoon) vs Negative IOD"
     ],
     "UNGIST Ch 30: Seating Arrangements — Circular Seating Facing Centre vs Facing Outside",
     "A positive Indian Ocean Dipole can offset the drying effect of an El Nino event on the Indian summer monsoon."
    ),
    (49, "Geography", "Weekly Consolidation 7: Geomorphology & Climatology Sectional Mock Test", "Weekly Revision Mode", "geo-02",
     [
         "Map landforms, pressure belts, and global ocean currents on blank world maps",
         "Attempt 100-Question Geomorphology & Climatology Mock Test (06:00-08:00 AM)",
         "Review map-based questions and cyclone dynamics",
         "Catalogue physical geography exceptions into revision notes"
     ],
     "UNGIST Ch 26, 30, 32: Venn, Seating & Syllogism — CSAT PYQ Marathon",
     "Geography questions are 70% spatial visualization. If you can sketch the physical model in 10 seconds, the answer is obvious."
    ),

    # WEEK 8 (Days 50-56): Geography - Oceanography & Indian Physiography/Drainage
    (50, "Geography", "Oceanography: Ocean Floor Relief, Temperature, Salinity & Coral Reefs", "NCERT Class 11 Physical", "geo-07",
     [
         "Ocean Floor Configuration: Continental Shelf (Fishing, petroleum), Continental Slope, Abyssal Plain, Oceanic Trenches",
         "Ocean Salinity Factors: Evaporation, precipitation, fresh water inflow; Halocline & Thermocline layers",
         "Coral Reefs: Symbiotic relationship between Coral polyps and Zooxanthellae; Fringing, Barrier, Atoll formation",
         "Coral Bleaching causes: Marine heatwaves, ocean acidification, sedimentation; Great Barrier Reef & Lakshadweep bleaching"
     ],
     "UNGIST Ch 20: Cubes and Dice — Opposite Face Determination on Unfolded Cubes",
     "Continental shelves hold the richest fisheries and oil reserves because shallow waters allow sunlight penetration and nutrient upwelling."
    ),
    (51, "Geography", "Oceanography: Ocean Currents, Tides & Upwelling Dynamics", "NCERT Class 11 Physical", "geo-07",
     [
         "Ocean Current Drivers: Planetary winds, Coriolis force, salinity/temperature differences (Thermohaline circulation)",
         "Atlantic Currents: Gulf Stream, North Atlantic Drift, Canaries, Benguela; Sargasso Sea formation",
         "Pacific & Indian Ocean Currents: Kuroshio, Oyashio, Peru/Humboldt (Anchovy fisheries), Agulhas, West Australian",
         "Tides: Spring Tides (Sun, Moon, Earth aligned - Syzygy) vs Neap Tides (Right angles - Quadrature)"
     ],
     "UNGIST Ch 20: Cubes and Dice — Painted Faces on 3x3x3 and 4x4x4 Cut Cubes",
     "Cold currents on western margins of continents coincide with the world's great hot deserts (Atacama, Namib, Sahara) due to desiccation."
    ),
    (52, "Geography", "Indian Physiography: The Northern Mountains (Himalayas) & Northern Plains", "NCERT Class 11 India Physical", "geo-04",
     [
         "Himalayan Ranges: Trans-Himalayas (Karakoram, Ladakh, Zaskar), Greater Himalayas (Himadri), Lesser Himalayas (Himachal), Shiwaliks",
         "Major Himalayan Passes: Zoji La, Banihal, Rohtang, Shipki La, Nathu La, Jelep La, Bomdi La",
         "Northern Plains Division: Bhabar (Porous, disappearing streams), Terai (Marshy, malaria belt), Bhangar (Old alluvium, kankar), Khadar (New fertile alluvium)",
         "Duns and Duars: Longitudinal valleys between Lesser Himalayas and Shiwaliks (e.g. Dehradun)"
     ],
     "UNGIST Ch 24: Number Ranking — Finding Total Persons Given Position from Left & Right",
     "Streams disappear in the porous pebble-strewn Bhabar tract and re-emerge in the swampy, waterlogged Terai zone."
    ),
    (53, "Geography", "Indian Physiography: Peninsular Plateau, Western vs Eastern Ghats & Islands", "NCERT Class 11 India Physical", "geo-04",
     [
         "Peninsular Plateau: Central Highlands (Malwa, Bundelkhand, Chotanagpur) vs Deccan Plateau (Deccan Traps, basaltic lava flows)",
         "Western Ghats (Sahyadris): Continuous, higher elevation, orographic rainfall; Passes (Thalghat, Bhorghat, Palghat gap)",
         "Eastern Ghats: Discontinuous, heavily eroded by east-flowing rivers (Mahanadi, Godavari, Krishna, Cauvery); Jindhagada peak",
         "Islands: Andaman & Nicobar (Volcanic origin, 10 Degree Channel separates Andaman and Nicobar) vs Lakshadweep (Coral atolls, 9 Degree Channel separates Minicoy)"
     ],
     "UNGIST Ch 24: Number Ranking — Overlapping Ranks & Person Interchange Problems",
     "The 10 Degree Channel separates Andaman from Nicobar; the 9 Degree Channel separates Minicoy from Lakshadweep main group."
    ),
    (54, "Geography", "Indian Drainage System: Himalayan Rivers (Indus, Ganga, Brahmaputra)", "NCERT Class 11 India Physical", "geo-01",
     [
         "Indus River System: Origin (Bokhar Chu), Right bank tributaries (Shyok, Gilgit), Left bank (Jhelum, Chenab, Ravi, Beas, Sutlej); Indus Water Treaty 1960",
         "Ganga River System: Panch Prayags (Vishnuprayag, Nandprayag, Karnaprayag, Rudraprayag, Devprayag); Major tributaries (Yamuna, Son, Gandak, Kosi, Ghaghara)",
         "Brahmaputra System: Origin (Chemayungdung glacier as Tsangpo), Dihang gorge entry, Majuli river island; Tributaries (Subansiri, Kameng, Manas, Teesta, Lohit, Dibang)",
         "Antecedent Drainage: Rivers older than the Himalayas cutting deep transverse gorges"
     ],
     "UNGIST Ch 16: Number Series — Arithmetic, Geometric & Prime Pattern Recognition",
     "Devprayag is where Alaknanda meets Bhagirathi to form the Ganga. Master the five sacred confluences in exact geographical sequence."
    ),
    (55, "Geography", "Indian Drainage System: Peninsular Rivers (East vs West Flowing)", "NCERT Class 11 India Physical", "geo-01",
     [
         "East-Flowing Rivers (Form Deltas): Godavari (Trimbakeshwar, Dakshin Ganga), Krishna (Mahabaleshwar), Cauvery (Talakaveri), Mahanadi",
         "West-Flowing Rivers (Form Estuaries in Rift Valleys): Narmada (Amarkantak, marble rocks), Tapti (Betul), Sabarmati, Mahi",
         "Water Disputes: Cauvery Water Management Authority, Krishna Water Disputes Tribunal, Godavari Water Disputes",
         "Interlinking of Rivers: Ken-Betwa river linking project details & Panna Tiger Reserve submergence issues"
     ],
     "UNGIST Ch 17: Missing Terms — Matrix & Geometric Figure Missing Number Deduction",
     "Narmada and Tapti flow westward through fault-trough rift valleys, not through broad erosional valleys, hence they form estuaries not deltas."
    ),
    (56, "Geography", "Weekly Consolidation 8: Indian Drainage, Relief & Oceanography Mock Test", "Weekly Revision Mode", "geo-01",
     [
         "Practice plotting all river tributaries, passes, and ocean currents on outline maps",
         "Attempt 100-Question Drainage & Relief Sectional Mock Test (06:00-08:00 AM)",
         "Review North-to-South and West-to-East chronological alignment questions",
         "Catalogue state-wise river basin allocations"
     ],
     "UNGIST Ch 16, 17, 20, 24: Reasoning Mixed Series & Puzzles — CSAT PYQ Marathon",
     "When UPSC asks you to arrange 4 rivers from North to South, sketch their origins first. Spatial anchors eliminate guesswork."
    ),

    # WEEK 9 (Days 57-63): Geography - Indian Soils, Resources & World Mapping
    (57, "Geography", "Indian Soils: Types, Characteristics, Distribution & Soil Degradation", "NCERT Class 11 & 12 India", "geo-05",
     [
         "Alluvial Soils (Largest area ~40%): Rich in potash, poor in phosphorus; Khadar vs Bhangar",
         "Black Soils (Regur / Cotton): Self-ploughing, high clay content, basaltic lava origin, rich in iron/lime, deficient in nitrogen",
         "Red & Yellow Soils: Acidic, iron oxide coloration, developed on crystalline igneous rocks",
         "Laterite Soils: Formed under high temp and intense leaching; rich in bauxite/iron, poor in humus; Cashew & tea plantation"
     ],
     "UNGIST Ch 31: Data Sufficiency — Deciding Sufficiency without Calculating Final Values",
     "Black cotton soil develops deep cracks when dry, causing self-ploughing and high moisture retention capacity."
    ),
    (58, "Geography", "Economic Geography: Mineral Distribution, Coal & Iron Ore Belts of India", "NCERT Class 12 Mineral", "geo-06",
     [
         "Metallic Minerals: Iron ore (Haematite in Odisha-Jharkhand belt; Magnetite in Kudremukh, Karnataka), Manganese (Balaghat), Bauxite (Odisha)",
         "Non-Metallic: Limestone, Mica (Koderma in Jharkhand as mica capital)",
         "Energy Resources: Coal (Gondwana coal ~98% of reserves, non-coking; Tertiary coal in Assam/Meghalaya, high sulphur)",
         "Petroleum & Natural Gas: Mumbai High, Krishna-Godavari Basin (KG-D6), Digboi (Oldest oil field), Coal Bed Methane (CBM)"
     ],
     "UNGIST Ch 31: Data Sufficiency — Two-Statement vs Three-Statement Elimination Rules",
     "Gondwana coal is bituminous and non-coking, requiring India to import metallurgical coking coal for blast furnace steel manufacturing."
    ),
    (59, "Geography", "Indian Agriculture: Cropping Zones, Cash Crops, Irrigation & Green Revolution", "NCERT Class 12 Agriculture", "geo-05",
     [
         "Foodgrains: Rice (Warm, humid > 100cm rain), Wheat (Cool climate, 50-75cm rain, winter showers from Western Disturbances)",
         "Millets (Nutri-cereals): Jowar, Bajra, Ragi (Drought-resistant, coarse grains in dryland farming)",
         "Cash Crops: Cotton (Black soil, 210 frost-free days), Sugarcane (Tropical crop, water-guzzling), Tea (Assam hill slopes), Coffee (Arabica & Robusta in Karnataka)",
         "Irrigation Patterns: Wells and Tube-wells (>60%), Canals (~25%), Tanks (South India peninsula due to hard rock terrain)"
     ],
     "UNGIST Ch 15: Data Interpretation — Reading Complex Bar Graphs & Percentage Shifts",
     "Tank irrigation is predominant in Peninsular India because the hard crystalline non-porous rock terrain prevents tube-well excavation."
    ),
    (60, "Geography", "World Geography: Strategic Chokepoints, Major Straits & Enclosed Seas", "Orient BlackSwan Atlas", "geo-03",
     [
         "Strategic Straits: Strait of Malacca, Strait of Hormuz (Persian Gulf to Gulf of Oman), Bab-el-Mandeb (Red Sea to Gulf of Aden), Bosphorus & Dardanelles",
         "Canals: Suez Canal (Mediterranean to Red Sea), Panama Canal (Atlantic to Pacific)",
         "Enclosed Seas & Riparian Nations: Caspian Sea (TARIK: Turkmenistan, Azerbaijan, Russia, Iran, Kazakhstan)",
         "Black Sea (BURGeR T: Bulgaria, Ukraine, Russia, Georgia, Romania, Turkey) & Mediterranean Sea border states"
     ],
     "UNGIST Ch 15: Data Interpretation — Pie Charts, Degree to Percentage Conversion (360 deg = 100%)",
     "Bab-el-Mandeb connects the Red Sea to the Gulf of Aden; the Strait of Hormuz connects the Persian Gulf to the Gulf of Oman. Learn chokepoints cold."
    ),
    (61, "Geography", "World Geography: Conflict Regions, Disputed Borders & Critical Mountains/Rivers", "Orient BlackSwan Atlas", "geo-03",
     [
         "West Asia Geopolitics: Golan Heights (Israel-Syria), West Bank & Gaza, Sinai Peninsula",
         "African Conflict Zones: Sahel region (Mali, Burkina Faso, Niger), Tigray (Ethiopia), Darfur (Sudan), Lake Chad basin",
         "Major World Rivers: Nile (Victoria to Mediterranean), Amazon (Andes to Atlantic), Danube (Passes 10 European capitals into Black Sea), Mekong",
         "Global Mountain Systems: Andes (Longest continental range), Rockies, Alps, Urals (Divides Europe and Asia), Great Dividing Range"
     ],
     "UNGIST Ch 33: Puzzles — Distribution and Cross-Tabulation Grid Puzzles",
     "The Danube river flows through 10 European nations and empties into the Black Sea, making it Europe's vital commercial waterway."
    ),
    (62, "Geography", "Major Ports, National Waterways & Dedicated Freight Corridors", "Ministry of Ports / NCERT", "geo-09",
     [
         "Major Ports of India: 12 major ports; Deendayal (Kandla - tidal port), JNPT (Largest container), Mumbai, Mormugao, Paradip, Visakhapatnam (Deepest natural port)",
         "Major Port Authorities Act 2021: Corporatization and autonomy for major ports",
         "National Waterways: NW-1 (Ganga: Prayagraj to Haldia, 1620 km), NW-2 (Brahmaputra: Sadiya to Dhubri), NW-3 (Kottapuram to Kollam)",
         "Dedicated Freight Corridors: Western DFC (Dadri to JNPT) vs Eastern DFC (Ludhiana to Dankuni)"
     ],
     "UNGIST Ch 33: Puzzles — Floor-Based & Box-Stacking Reasoning Problems",
     "National Waterway 1 on the Ganga is India's longest inland waterway stretching 1620 km from Prayagraj to Haldia."
    ),
    (63, "Geography", "Weekly Consolidation 9: Complete Physical & Indian Geography Grand Mock Test", "Weekly Revision Mode", "geo-01",
     [
         "Complete synthesis of Geomorphology, Climatology, Oceanography, Indian Drainage & World Maps",
         "Attempt 100-Question Grand Geography Sectional Mock Test (06:00-08:00 AM)",
         "Identify map-based weaknesses (West Asia, African lakes, Indian river tributaries)",
         "Review atlas pins for all international conflict zones"
     ],
     "UNGIST Ch 15 & 33: DI & Complex Puzzles — CSAT PYQ Marathon",
     "Geography maps reward visual curiosity. Three subjects down: Polity, Economy, Geography. The foundation is solidifying."
    ),

    # WEEK 10 (Days 64-70): Environment - Ecology & Protected Areas
    (64, "Environment", "Ecosystem Concepts: Levels of Organization, Food Chains & Energy Flow", "NCERT Class 12 Biology", "env-06",
     [
         "Levels: Individual -> Population -> Community -> Ecosystem -> Biome -> Biosphere",
         "Trophic Levels: Grazing food chain (Living plants base) vs Detritus food chain (Dead organic matter base)",
         "Ecological Pyramids: Pyramid of Energy is ALWAYS upright (Lindeman's 10% law); Pyramid of Biomass in sea is INVERTED",
         "Biomagnification vs Bioaccumulation: Accumulation in single organism vs concentration amplification across food chain"
     ],
     "UNGIST CSAT: Reading Comprehension — The 'Sherlocking' Method (Step 1: Read Question First)",
     "The pyramid of energy is always upright because energy is lost as heat at each trophic level. The second law of thermodynamics governs ecology."
    ),
    (65, "Environment", "Ecosystem Dynamics: Ecological Succession, Ecotone & Keystone Species", "NCERT Class 12 Biology", "env-06",
     [
         "Ecological Succession: Primary succession (Pioneer species on bare rock, lichens) vs Secondary succession (Faster, soil already present)",
         "Climax Community: Stable, self-perpetuating equilibrium state",
         "Ecotone: Transition zone between two distinct biomes (e.g. Mangrove, Estuary); Edge Effect & Edge Species density",
         "Ecological Roles: Keystone Species (Disproportionate impact on ecosystem structure), Indicator species, Flagship, Umbrella species"
     ],
     "UNGIST CSAT: Reading Comprehension — The 'Sherlocking' Method (Step 2: Locate Exact Sentence Anchor)",
     "Mangroves and estuaries are classic ecotones showing the Edge Effect, where species diversity is often higher than in either adjacent community."
    ),
    (66, "Environment", "Biogeochemical Cycles: Carbon, Nitrogen, Phosphorus & Sulphur Cycles", "NCERT Class 12 Biology", "env-10",
     [
         "Gaseous Cycles: Carbon cycle (Ocean as largest carbon sink), Nitrogen cycle (Nitrogen fixation by Rhizobium, Azotobacter; Nitrification by Nitrosomonas/Nitrobacter; Denitrification by Pseudomonas)",
         "Sedimentary Cycles: Phosphorus cycle (Main reservoir is rock phosphate, NO atmospheric component)",
         "Sulphur cycle: Sedimentary with minor atmospheric reservoir (Volcanic H2S, SO2)",
         "Impact of human fertilizer use on Nitrogen cycle: Eutrophication and oceanic dead zones"
     ],
     "UNGIST CSAT: Reading Comprehension — The 'Sherlocking' Method (Step 3: Eliminate Extreme Words)",
     "Phosphorus cycle has no significant atmospheric gas phase; weathering of rock is the sole primary release mechanism."
    ),
    (67, "Environment", "Protected Areas: National Parks, Wildlife Sanctuaries & Biosphere Reserves", "Shankar IAS / PMFIAS", "env-01",
     [
         "National Park (WPA 1972): Highest protection, no human exploitation or grazing permitted; Created by State govt notification",
         "Wildlife Sanctuary: Regulated human activities and traditional grazing permitted",
         "Biosphere Reserve (UNESCO MAB): Core area (Strict nature reserve), Buffer zone (Research, education), Transition zone (Sustainable human settlements)",
         "18 Biosphere Reserves in India; 12 in UNESCO World Network of Biosphere Reserves (Nilgiri was first in 1986)"
     ],
     "UNGIST CSAT: Reading Comprehension — The 'Sherlocking' Method (Step 4: Match Core Claim)",
     "No human habitation or cattle grazing is permitted inside a National Park. Strict preservation differentiates it from a Wildlife Sanctuary."
    ),
    (68, "Environment", "Project Tiger, Tiger Reserves, NTCA & M-STrIPES Protocol", "Shankar IAS / WII", "env-01",
     [
         "Project Tiger (1973): Centrally Sponsored Scheme; National Tiger Conservation Authority (NTCA, statutory under WPA 2006 amendment)",
         "Tiger Reserve Structure: Core/Critical Tiger Habitat (Notified under WPA 1972) + Buffer/Peripheral area",
         "All-India Tiger Estimation (Every 4 years): Camera trapping, double sampling, M-STrIPES digital monitoring app",
         "Latest Tiger Reserves: Ranipur (UP), Ramgarh Vishdhari (Rajasthan), Dholpur-Karauli, Veerangana Durgavati (MP)"
     ],
     "UNGIST CSAT: Reading Comprehension — Critical Assumptions vs Logical Inferences",
     "Critical Tiger Habitats are notified under the Wildlife Protection Act 1972, whereas Critical Wildlife Habitats are recognized under the Forest Rights Act 2006."
    ),
    (69, "Environment", "Wetlands Conservation, Ramsar Convention & Montreux Record", "MoEFCC / Ramsar", "env-07",
     [
         "Ramsar Convention 1971: Intergovernmental treaty on conservation and wise use of wetlands; Ramsar Sites in India (>80 sites)",
         "Montreux Record: Register of wetland sites on List of Ramsar wetlands where ecological character changes have occurred, are occurring, or likely to occur",
         "Indian sites in Montreux Record: Keoladeo National Park (Rajasthan) and Loktak Lake (Manipur); Chilika was removed",
         "Wetlands (Conservation and Management) Rules 2017: Decentralization to State Wetland Authorities; Prohibits untreated waste discharge"
     ],
     "UNGIST CSAT: Reading Comprehension — Best Crux / Core Message Extraction Techniques",
     "Chilika Lake was successfully removed from the Montreux Record due to ecological restoration; Loktak and Keoladeo remain listed."
    ),
    (70, "Environment", "Weekly Consolidation 10: Ecology, Wetlands & Protected Areas Mock Test", "Weekly Revision Mode", "env-01",
     [
         "Map all 18 Biosphere Reserves and recent Ramsar Sites on India physical map",
         "Attempt 100-Question Ecology & Protected Areas Sectional Mock Test (06:00-08:00 AM)",
         "Review questions on ecological succession and inverted biomass pyramids",
         "Compile species-to-park association flashcards"
     ],
     "UNGIST CSAT: Reading Comprehension — 2019-2023 UPSC Official Passages Marathon Drill",
     "Reading Comprehension carries ~50 marks in CSAT. Master the Sherlocking method: find the anchor, kill the extremes, claim the marks."
    ),

    # WEEK 11 (Days 71-77): Environment - Biodiversity, Treaties & Governance
    (71, "Environment", "Biodiversity: Hotspots, IUCN Red List Criteria & Endemic Species", "Shankar IAS / WII", "env-02",
     [
         "Biodiversity Hotspots (Norman Myers criteria): Must contain at least 1,500 species of vascular plants (>0.5% of world total) as endemics AND lost >= 70% of primary vegetation",
         "4 Biodiversity Hotspots in India: Himalayas, Indo-Burma, Western Ghats & Sri Lanka, Sundaland (Nicobar)",
         "IUCN Red List Categories: Extinct, Extinct in Wild, Critically Endangered (CR), Endangered (EN), Vulnerable (VU)",
         "Flagship Indian Species Status: Great Indian Bustard (CR), Lion-tailed Macaque (EN), One-horned Rhino (VU), Snow Leopard (VU)"
     ],
     "UNGIST CSAT: Number System & CSAT Speed Math — Mixed Revision Set 1",
     "To qualify as a Biodiversity Hotspot, an area must have lost at least 70% of its original primary habitat while holding high endemism."
    ),
    (72, "Environment", "Wildlife Protection Act 1972 (2022 Amendment) & Environmental Legislation", "PMFIAS / Shankar IAS", "env-04",
     [
         "Wildlife (Protection) Amendment Act 2022: Rationalized schedules from 6 to 4 (Schedule I: Highest protection, Schedule II: Lesser, Schedule III: Plants, Schedule IV: CITES specimens)",
         "Removed vermin schedule (Central govt can notify by declaration)",
         "Environment (Protection) Act 1986: Umbrella legislation enacted after Bhopal Gas Tragedy (Art 48A & 51A(g))",
         "Forest (Conservation) Act 1980 & 2023 Amendment: Scope of forest definition (Godavarman case) & exemptions along international borders"
     ],
     "UNGIST CSAT: Percentages & Profit-Loss — Speed Mental Drills Set 2",
     "The 2022 WPA amendment reduced schedules from 6 to 4 and explicitly incorporated CITES compliance into domestic Indian law."
    ),
    (73, "Environment", "Forest Rights Act 2006, CAMPA Act & Biological Diversity Act 2002", "PMFIAS / MoEFCC", "env-04",
     [
         "Scheduled Tribes and Other Traditional Forest Dwellers (FRA 2006): Individual Forest Rights (IFR up to 4 hectares) & Community Forest Rights (CFR)",
         "Gram Sabha is the statutory authority to initiate the process for determining forest rights",
         "Compensatory Afforestation Fund Act (CAMPA 2016): National (10%) and State (90%) funds for compensatory afforestation",
         "Biological Diversity Act 2002 (2023 Amendment): Three-tier mechanism (National Biodiversity Authority - NBA, SBB, Biodiversity Management Committees - BMC); Access and Benefit Sharing (ABS)"
     ],
     "UNGIST CSAT: Ratio, Mixture & Alligation — Speed Mental Drills Set 3",
     "Under FRA 2006, the Gram Sabha has the final decisive authority to recognize forest rights and minor forest produce collection."
    ),
    (74, "Environment", "International Environmental Treaties: UNFCCC, Kyoto Protocol & Paris Agreement", "Shankar IAS / MoEFCC", "env-03",
     [
         "UNFCCC (Rio 1992): Common But Differentiated Responsibilities and Respective Capabilities (CBDR-RC)",
         "Kyoto Protocol (1997): Legally binding emission reduction targets for Annex I countries; Clean Development Mechanism (CDM)",
         "Paris Agreement (2015, COP21): Limit global warming well below 2C, pursue 1.5C; Nationally Determined Contributions (NDCs)",
         "India's Updated NDCs: 45% emissions intensity reduction by 2030, 50% non-fossil electric power capacity, 2.5-3 billion tonnes carbon sink; Net Zero by 2070"
     ],
     "UNGIST CSAT: Time, Work & Cisterns — Speed Mental Drills Set 4",
     "The Paris Agreement replaced Kyoto's top-down legally binding targets with bottom-up voluntary Nationally Determined Contributions (NDCs)."
    ),
    (75, "Environment", "International Conventions: CBD, CITES, CMS, Basel, Rotterdam & Stockholm", "Shankar IAS / MoEFCC", "env-03",
     [
         "Convention on Biological Diversity (CBD): Cartagena Protocol (Biosafety & Living Modified Organisms), Nagoya Protocol (Access & Benefit Sharing), Kunming-Montreal Global Biodiversity Framework (30x30 target)",
         "CITES (Washington Convention 1973): Regulates international trade in endangered wild animals and plants; Appendices I, II, III",
         "CMS (Bonn Convention): Conservation of migratory species of wild animals (Central Asian Flyway)",
         "Chemical Conventions: Basel (Hazardous wastes), Rotterdam (Prior informed consent for dangerous chemicals), Stockholm (Persistent Organic Pollutants - POPs)"
     ],
     "UNGIST CSAT: Time, Speed, Distance & Trains — Speed Mental Drills Set 5",
     "Cartagena covers living modified organisms; Nagoya covers access and benefit sharing of genetic resources. Both branch from the CBD tree."
    ),
    (76, "Environment", "Pollution Control, Air Quality Monitoring (AQI/NAAQS) & Waste Rules", "CPCB / MoEFCC", "env-05",
     [
         "National Air Quality Index (AQI): 8 pollutants (PM10, PM2.5, NO2, SO2, CO, O3, NH3, Pb); 6 categories (Good to Severe)",
         "National Ambient Air Quality Standards (NAAQS): 12 pollutants (includes Benzene, Benzo(a)pyrene, Arsenic, Nickel)",
         "Commission for Air Quality Management (CAQM) in NCR & Adjoining Areas Act 2021; Graded Response Action Plan (GRAP)",
         "Waste Management Rules: Solid Waste, Plastic Waste (Extended Producer Responsibility - EPR, ban on single-use plastic), E-Waste, Bio-medical Waste"
     ],
     "UNGIST CSAT: Permutations, Combinations & Probability — Speed Drills Set 6",
     "AQI monitors 8 pollutants; NAAQS covers 12. Carbon dioxide (CO2) is monitored under NEITHER index. UPSC loves this trap."
    ),
    (77, "Environment", "Weekly Consolidation 11: Biodiversity, Treaties & Pollution Mock Test", "Weekly Revision Mode", "env-03",
     [
         "Consolidate international conventions matrix (Treaty, Year, Objective, Legally binding status)",
         "Attempt 100-Question Biodiversity & Conventions Sectional Mock Test (06:00-08:00 AM)",
         "Review environmental legislation provisions and penalties",
         "Verify India's Panchamrit climate goals and NDC commitments"
     ],
     "UNGIST CSAT: Clocks, Calendar & Syllogism — Speed Mental Drills Set 7",
     "Environmental conventions questions are high-yield certainty in UPSC prelims. A sharp comparative table guarantees 10-15 marks."
    ),

    # WEEK 12 (Days 78-84): Environment - Climate Change, Sustainable Agri & Cycles
    (78, "Environment", "Climate Change Science: Radiative Forcing, Carbon Budget & IPCC Reports", "PMFIAS / IPCC", "env-08",
     [
         "Greenhouse Gases & Global Warming Potential (GWP): CO2 (1), Methane (CH4 ~28x over 100y), Nitrous Oxide (N2O ~265x), Fluorinated gases (HFCs, PFCs, SF6)",
         "Kigali Amendment to Montreal Protocol (2016): Phasing down Hydrofluorocarbons (HFCs)",
         "IPCC Assessment Reports (AR6): Working Group findings on 1.5C carbon budget depletion and tipping points",
         "Ocean Acidification (Carbonic acid formation, impact on calcifying organisms) & Blue Carbon ecosystems"
     ],
     "UNGIST CSAT: Reading Comprehension — Tough Technical Passages Deconstruction",
     "The Montreal Protocol addresses ozone depletion; the Kigali Amendment brought HFCs (potent greenhouse gases) under its phase-down mandate."
    ),
    (79, "Environment", "Carbon Markets, Article 6 Mechanisms & Geo-Engineering", "PMFIAS / Down to Earth", "env-08",
     [
         "Article 6 of Paris Agreement: 6.2 (Bilateral ITMOs - Internationally Transferred Mitigation Outcomes) vs 6.4 (Centralized carbon crediting mechanism)",
         "Carbon Border Adjustment Mechanism (CBAM) of European Union: Tariffs on carbon-intensive imports (Steel, aluminium, cement, fertilizer)",
         "Domestic Carbon Credit Trading Scheme (CCTS) under Energy Conservation (Amendment) Act 2022; Bureau of Energy Efficiency (BEE)",
         "Geo-engineering concepts: Solar Radiation Management (Stratospheric aerosol injection) vs Carbon Dioxide Removal (Direct air capture, ocean fertilization)"
     ],
     "UNGIST CSAT: Reading Comprehension — Philosophical & Ethical Passages Deconstruction",
     "CBAM aims to prevent carbon leakage by taxing embedded carbon emissions in imported goods. A major WTO trade friction point for India."
    ),
    (80, "Environment", "Sustainable Agriculture: System of Rice Intensification (SRI), Natural Farming & Biochar", "Down to Earth / PIB", "env-09",
     [
         "System of Rice Intensification (SRI): Alternate wetting and drying, reduced seed rate, less water consumption, lower methane emissions",
         "Zero Budget Natural Farming (ZBNF) / Bhartiya Prakritik Krishi Paddhati: Bijamrit, Jivamrit, Mulching, Waaphasa",
         "Conservation Agriculture: Minimum soil disturbance (Zero tillage), permanent organic soil cover, crop diversification",
         "Biochar: Pyrolysis of biomass; Highly porous, carbon sequestration in soil, improves cation exchange capacity and water retention"
     ],
     "UNGIST CSAT: Reading Comprehension — Economic & Governance Passages Deconstruction",
     "Zero Tillage allows sowing wheat directly into paddy stubble without prior ploughing, conserving soil moisture and reducing fuel costs."
    ),
    (81, "Environment", "Renewable Energy Initiatives: ISA, CDRI, Green Hydrogen & Storage", "MNRE / PIB", "env-08",
     [
         "International Solar Alliance (ISA): Headquarters in Gurugram, India; One Sun One World One Grid (OSOWOG) vision",
         "Coalition for Disaster Resilient Infrastructure (CDRI): India-led global initiative launched at UN Climate Action Summit 2019",
         "National Green Hydrogen Mission: Target 5 MMT annual production by 2030; SIGHT programme (Electrolyser manufacturing incentives)",
         "Energy Storage: Battery Energy Storage Systems (BESS) vs Pumped Storage Hydropower (PSH) for grid balancing"
     ],
     "UNGIST CSAT: CSAT Full Mock Simulation 1 — Section A: Quantitative Reasoning",
     "National Green Hydrogen Mission defines green hydrogen as produced through water electrolysis powered by renewable electricity."
    ),
    (82, "Environment", "Invasive Alien Species, Forest Fire Management & Wildlife Corridors", "WII / MoEFCC", "env-02",
     [
         "Invasive Alien Species in India: Prosopis juliflora (Vilayati kikar), Lantana camara, Water Hyacinth (Eichhornia), Parthenium hysterophorus",
         "Impact: Outcompetes native vegetation, alters hydrology, reduces herbivore forage",
         "Forest Fires in India: Chir Pine forests in Himalayas (Resin-rich dry needles), dry deciduous forests; FSI Forest Fire Alert System (SNPP-VIIRS)",
         "Wildlife Corridors: Elephant Corridors (Right of Passage report), Project Elephant (1992), MIKE programme (Monitoring Illegal Killing of Elephants)"
     ],
     "UNGIST CSAT: CSAT Full Mock Simulation 1 — Section B: Logical Reasoning",
     "Prosopis juliflora depletes groundwater and aggressively displaces native flora in dry regions. UPSC repeatedly tests invasive plant species."
    ),
    (83, "Environment", "Coastal Regulation Zone (CRZ) Norms, Blue Flag Certification & Mangroves", "MoEFCC", "env-04",
     [
         "CRZ Notification 2019: CRZ-I (Ecologically sensitive), CRZ-II (Urban developed), CRZ-III (Rural areas: III-A dense vs III-B less dense), CRZ-IV (Water area up to 12 nautical miles)",
         "Blue Flag Certification: Eco-label by Foundation for Environmental Education (FEE, Denmark); 33 criteria; Indian certified beaches",
         "Mangrove Initiative for Shoreline Habitats & Tangible Incomes (MISHTI scheme): Promoting mangrove afforestation along coastline",
         "State of World's Mangroves: Sundarbans (Largest mangrove forest, Bengal Tiger habitat) & Bhitarkanika (Saltwater crocodile haven)"
     ],
     "UNGIST CSAT: CSAT Full Mock Simulation 1 — Section C: Reading Comprehension",
     "Blue Flag is awarded by Denmark-based NGO Foundation for Environmental Education (FEE) based on 33 stringent environmental and safety criteria."
    ),
    (84, "Environment", "Weekly Consolidation 12: Complete Environment & Ecology Grand Mock Test", "Weekly Revision Mode", "env-01",
     [
         "Complete synthesis of Ecology, Protected Areas, Biodiversity, Conventions & Climate Change",
         "Attempt 100-Question Environment Grand Sectional Mock Test (06:00-08:00 AM)",
         "Benchmark: Target 75+ net score in Environment (the highest weightage subject in Prelims)",
         "Consolidate error notebook with latest species IUCN classifications"
     ],
     "UNGIST CSAT: CSAT Full Mock Simulation 1 — Complete Paper Evaluation & Analysis",
     "Environment and Ecology accounts for 18-22 questions every year due to the combined IFS exam. Mastering this guarantees clearing the cut-off."
    ),

    # WEEK 13 (Days 85-91): Ancient & Medieval History + Art & Culture
    (85, "History", "Indus Valley Civilization: Major Sites, Urban Planning & Material Culture", "NCERT Class 12 Theme 1", "his-08",
     [
         "Town Planning: Citadel vs Lower Town, Grid layout, Burnt brick architecture, Advanced drainage system, Great Bath at Mohenjo-daro",
         "Major Sites & Findings: Harappa (Granaries), Mohenjo-daro (Dancing Girl bronze, Priest King), Dholavira (Water reservoir, 3-part town, sign board), Lothal (Tidal dockyard)",
         "Rakhigarhi (Largest IVC site, DNA studies), Kalibangan (Ploughed field, fire altars), Chanhudaro (Bead making factory, no citadel)",
         "Trade & Economy: Meluhha trade with Mesopotamia, Steatite seals, Pashupati seal, absence of iron and horse evidence"
     ],
     "UNGIST CSAT: Number System & Divisibility Advanced Problems",
     "Dholavira is uniquely divided into three parts (Citadel, Middle Town, Lower Town) and features a world-renowned stone-cut water reservoir system."
    ),
    (86, "History", "Vedic Period, Mahajanapadas & Mauryan Empire (Ashokan Inscriptions)", "RS Sharma / Tamil Nadu", "his-06",
     [
         "Early Vedic (Rigvedic): Pastoral, Sabha & Samiti, egalitarian, pastoral economy (Gavishti), no caste rigidity",
         "Later Vedic: Painted Grey Ware (PGW), iron usage (Krishna Ayas), Janapadas to Mahajanapadas, sacrificial rituals, Varna hierarchy",
         "16 Mahajanapadas: Magadha rise (Bimbisara, Ajatashatru), natural resources, iron mines of Rajgir, elephant army",
         "Mauryan Empire & Ashoka: Kautilya's Arthashastra, Megasthenes' Indica; Ashokan Edicts (Major Rock Edicts, Pillar Edicts, Dhamma, Brahmi/Kharosthi scripts)"
     ],
     "UNGIST CSAT: Advanced Averages & Weighted Deviation Puzzles",
     "Sabha was an assembly of elders; Samiti was the general national assembly of the people in the Early Vedic polity."
    ),
    (87, "History", "Buddhism & Jainism: Philosophy, Literature, Councils & Sects", "RS Sharma / NCERT", "his-01",
     [
         "Buddhism: Four Noble Truths, Eightfold Path, Pratityasamutpada (Dependent Origination), Anatta (No-self), Anicca (Impermanence)",
         "Buddhist Councils: 1st (Rajgriha - Sutta & Vinaya Pitaka), 2nd (Vaishali), 3rd (Pataliputra - Abhidhamma Pitaka), 4th (Kashmir - Hinayana vs Mahayana split)",
         "Jainism: Vardhamana Mahavira, Triratna, Anekantavada (Many-sidedness) & Syadvada, Ahimsa, Digambara vs Svetambara split",
         "Sects & Concepts: Bodhisattvas (Avalokiteshvara, Maitreya - future Buddha), Chaityas (Prayer halls) vs Viharas (Monasteries)"
     ],
     "UNGIST CSAT: Advanced Ratio, Alligation & Replacement Models",
     "Chaitya is a place of worship with a stupa; Vihara is the residential dwelling monastery for Buddhist and Jain monks."
    ),
    (88, "History", "Gupta Empire, Post-Gupta Era & Harshavardhana", "RS Sharma / Satish Chandra", "his-06",
     [
         "Gupta Age: Golden age of classical Sanskrit literature; Kalidasa, Aryabhata (Surya Siddhanta), Varahamihira (Pancha Siddhantika)",
         "Administration & Land Grants: Feudalization of economy (Agrahara grants to Brahmins), decline of urban trade, Fa-Hien's account",
         "Harshavardhana: Kannauj capital, Harsha Charita by Banabhatta, Priyadarshika, Ratnavali; Defeat by Pulakeshin II on Narmada",
         "Hiuen Tsang's travelogue (Si-Yu-Ki): Nalanda University under Acharya Shilabhadra"
     ],
     "UNGIST CSAT: Time and Work Alternate Days & Variable Efficiency Problems",
     "Pulakeshin II of the Western Chalukyas defeated Emperor Harshavardhana on the banks of the Narmada, recorded in the Aihole inscription."
    ),
    (89, "History", "Temple Architecture: Nagara, Dravida & Vesara Styles, Rock-Cut Architecture", "Nitin Singhania / NCERT", "his-04",
     [
         "Nagara Style (North India): Shikhara (Curvilinear), Garbhagriha, Mandapa, Amalaka & Kalasha; No boundary walls or gopurams (Khajuraho, Konark Sun Temple)",
         "Dravida Style (South India): Vimana (Pyramidal stepped tower), imposing Gopurams, enclosed boundary wall, temple water tank (Brihadisvara at Thanjavur)",
         "Vesara Style (Hybrid): Chalukyan temples at Badami, Aihole, Pattadakal; Hoysala temples (Stellate ground plan, chloritic schist, Belur & Halebidu)",
         "Rock-Cut Caves: Ajanta (Buddhist, fresco paintings), Ellora (Buddhist, Hindu, Jain - Kailashnath Monolithic temple Cave 16), Elephanta"
     ],
     "UNGIST CSAT: Speed, Time and Distance Relative Motion & Head-start Problems",
     "Dravida style temples feature stepped pyramidal Vimanas and towering Gopuram entrance gateways; Nagara temples lack gopurams and water tanks."
    ),
    (90, "History", "Bhakti & Sufi Movements: Saints, Philosophies, Literature & Impact", "Satish Chandra / Nitin Singhania", "his-07",
     [
         "South Indian Roots: Alvars (Vaishnavite, 12 saints, Nalayira Divya Prabandham) & Nayanars (Shaivite, 63 saints, Tevaram)",
         "Philosophies: Shankaracharya (Advaita - Non-dualism), Ramanuja (Vishishtadvaita - Qualified non-dualism), Madhvacharya (Dvaita)",
         "North Indian Bhakti: Nirguna (Kabir, Guru Nanak) vs Saguna (Surdas, Tulsidas, Mirabai, Chaitanya Mahaprabhu)",
         "Sufi Silsilas: Chishti (Khwaja Moinuddin Chishti, Nizamuddin Auliya, Qawwali, Sama) vs Suhrawardi (Wealth acceptable) vs Naqshbandi (Orthodox)"
     ],
     "UNGIST CSAT: Permutations and Combinations Complex Constrained Selections",
     "Advaita asserts the ultimate non-difference between Atman and Brahman; Vishishtadvaita asserts qualified non-dualism with devotion (Bhakti) as path to salvation."
    ),
    (91, "History", "Weekly Consolidation 13: Ancient History & Art and Culture Sectional Mock", "Weekly Revision Mode", "his-01",
     [
         "Consolidate chronological timelines from Harappa through Guptas and Temple styles",
         "Attempt 100-Question Ancient & Art-Culture Sectional Mock Test (06:00-08:00 AM)",
         "Review terms tested in UPSC (e.g. Eripatti, Taniyurs, Vishti, Mahattara)",
         "Map rock-cut caves, UNESCO heritage temple sites, and Ashokan edicts"
     ],
     "UNGIST CSAT: Probability Complex Independent and Mutually Exclusive Events",
     "Ancient and Medieval questions in UPSC hinge on administrative terms and religious philosophy. Master the terminology glossary."
    ),

    # WEEK 14 (Days 92-98): Medieval History & Modern British Expansion
    (92, "History", "Delhi Sultanate: Slave, Khalji, Tughlaq Administrations & Market Reforms", "Satish Chandra", "his-10",
     [
         "Dynasties: Mamluk/Slave (Iltutmish - Chahalgani, Iqta system), Khalji (Alauddin - Market reforms, Dagh & Chehra, revenue in cash)",
         "Tughlaqs: Muhammad bin Tughlaq (Token currency, capital shift to Daulatabad), Firoz Shah Tughlaq (Canals, Diwan-i-Khairat)",
         "Administration: Diwan-i-Wizarat (Finance), Diwan-i-Arz (Military), Diwan-i-Insha (Correspondence), Diwan-i-Rasalat (Foreign/Religious)",
         "Architecture: Qutub Minar, Alai Darwaza (True arch and dome, red sandstone), Tughlaqabad fort"
     ],
     "UNGIST CSAT: Clocks & Calendar Tough Multi-Step Calculations",
     "Alauddin Khalji fixed grain prices and mandated land revenue measurement (Masahat), paying soldiers in cash for the first time."
    ),
    (93, "History", "Vijayanagara Empire: Administration, Nayankara System, Foreign Travellers", "NCERT Class 12 Theme 2", "his-05",
     [
         "Establishment (1336): Harihara and Bukka (Sangama dynasty), Saluva, Tuluva (Krishnadevaraya), Aravidu dynasties",
         "Krishnadevaraya: Amuktamalyada (Telugu political treatise), Jambavati Kalyanam (Sanskrit), battle of Raichur",
         "Nayankara System: Military chiefs (Nayakas) given Amaram lands in return for maintaining troops; Mahanavami Dibba celebrations",
         "Foreign Visitors: Nicolo de Conti (Italian), Abdur Razzaq (Persian), Domingo Paes & Fernao Nuniz (Portuguese), Duarte Barbosa"
     ],
     "UNGIST CSAT: Syllogism Advanced Possibility and Negation Deduction",
     "Foreign travellers' accounts of Vijayanagara are a perennial UPSC favorite: Domingo Paes and Fernao Nuniz visited during Krishnadevaraya's reign."
    ),
    (94, "History", "Mughal Empire: Mansabdari System, Land Revenue & Religious Policy", "Satish Chandra", "his-10",
     [
         "Akbar's Consolidation: Mansabdari System (Zat = personal rank/salary, Sawar = cavalry contingent required)",
         "Land Revenue: Todar Mal's Dahsala system (10-year average yield & prices), Zabti system; Polaj (Annually cultivated), Parauti, Chachar, Banjar",
         "Religious Policy: Ibadat Khana (1575), Sulh-i-Kul (Universal peace), Din-i-Ilahi (1582), abolition of Jizya",
         "Decline & Crisis: Jagirdari crisis under Aurangzeb, Deccan campaigns draining treasury, agrarian rebellions"
     ],
     "UNGIST CSAT: Direction Sense & Complex Family Tree Combined Puzzles",
     "Zat indicated the personal status and salary of the Mansabdar; Sawar indicated the exact number of cavalrymen he had to maintain."
    ),
    (95, "History", "Modern India: British Expansion, Carnatic Wars, Plassey, Buxar & Subsidiary Alliance", "Spectrum Modern History", "his-03",
     [
         "Anglo-French Rivalry (Carnatic Wars): Dupleix's subsidiary troops concept; Treaty of Paris 1763",
         "Battle of Plassey (1757) & Battle of Buxar (1764): Treaty of Allahabad (1765) granting Diwani rights of Bengal, Bihar, Orissa to EIC",
         "Lord Wellesley's Subsidiary Alliance (1798): Hyderabad was first to sign, followed by Mysore, Tanjore, Awadh, Peshwa",
         "Lord Dalhousie's Doctrine of Lapse: Satara (first 1848), Sambalpur, Jhansi, Nagpur; Annexation of Awadh on grounds of misgovernance"
     ],
     "UNGIST CSAT: Advanced Venn Diagrams (Three-way intersections and constraints)",
     "The Battle of Buxar (1764) was far more militarily decisive than Plassey, leading directly to the Treaty of Allahabad and EIC Diwani rights."
    ),
    (96, "History", "Modern India: Land Revenue Systems (Permanent, Ryotwari, Mahalwari) & Drain of Wealth", "Spectrum Modern History", "his-03",
     [
         "Permanent Settlement (1793): Lord Cornwallis in Bengal, Bihar, Odisha; Zamindars as owners, state demand fixed at 10/11th, Sunset Law",
         "Ryotwari Settlement: Thomas Munro & Alexander Read in Madras, Bombay, Assam; Direct settlement with peasant (Ryot), periodic revision",
         "Mahalwari Settlement: Holt Mackenzie & RM Bird in NW Province, Punjab; Village community (Mahal) collectively responsible",
         "Economic Drain Theory: Dadabhai Naoroji ('Poverty and Un-British Rule in India'), RC Dutt ('Economic History of India'), Subramania Iyer"
     ],
     "UNGIST CSAT: Complex Circular & Linear Seating Arrangement Logic",
     "The Sunset Law under the Permanent Settlement stipulated that if rent was not paid by sunset on the specified date, the zamindari was auctioned."
    ),
    (97, "History", "1857 Revolt & Socio-Religious Reform Movements of the 19th Century", "Spectrum Modern History", "his-09",
     [
         "1857 Revolt: Causes (Political, economic, military, greased cartridges), Leaders (Nana Saheb, Kunwar Singh, Begum Hazrat Mahal, Rani Lakshmibai); Government of India Act 1858 (Crown takeover)",
         "Raja Ram Mohan Roy: Brahmo Samaj (1828), abolition of Sati (1829), Atmiya Sabha, Sambad Kaumudi",
         "Ishwar Chandra Vidyasagar: Hindu Widows' Remarriage Act (1856), women's education",
         "Arya Samaj (Swami Dayananda - 'Go back to Vedas', Shuddhi), Ramakrishna Mission (Vivekananda - Chicago 1893), Satyashodhak Samaj (Jyotirao Phule - Gulamgiri)"
     ],
     "UNGIST CSAT: Critical Assumptions in UPSC Reading Comprehension Passages",
     "Jyotirao Phule established the Satyashodhak Samaj in 1873 to liberate lower castes from brahminical dominance, dedicating 'Gulamgiri' to American abolitionists."
    ),
    (98, "History", "Weekly Consolidation 14: Medieval & Early Modern History Sectional Mock", "Weekly Revision Mode", "his-03",
     [
         "Review comparative table of land revenue settlements and socio-religious reform leaders",
         "Attempt 100-Question Medieval & Early Modern Sectional Mock Test (06:00-08:00 AM)",
         "Identify gaps in foreign traveller chronologies and treaty clauses",
         "Consolidate error notebook on 19th-century publications and journals"
     ],
     "UNGIST CSAT: Logical Corollaries & Author's Implicit Stance in Reading Comprehension",
     "Early Modern History is structured around British policies and Indian responses. Master the cause-and-effect chain."
    ),

    # WEEK 15 (Days 99-105): Modern Freedom Struggle & Science/Tech Foundation
    (99, "History", "Indian National Movement: Early Phase, Moderates, Extremists & Surat Split (1885-1907)", "Spectrum Modern History", "his-02",
     [
         "Foundation of INC (1885): AO Hume, WC Bonnerjee first president, Safety Valve theory",
         "Moderate Phase: Dadabhai Naoroji, Gopal Krishna Gokhale, Pherozeshah Mehta; Constitutional agitation (Prayer, Petition, Protest)",
         "Extremist Phase: Lal-Bal-Pal, Aurobindo Ghosh; Swadeshi & Boycott Movement (1905) against Partition of Bengal by Curzon",
         "Surat Split (1907): Ideological rift over extending Boycott outside Bengal; Rash Behari Ghosh president"
     ],
     "UNGIST CSAT: Full CSAT Mock Drill 2 — Speed Quantitative Aptitude",
     "The Swadeshi Movement witnessed the first mass boycott of foreign goods and the emergence of national education institutions."
    ),
    (100, "History", "Gandhian Era: Early Satyagrahas, Non-Cooperation & Civil Disobedience (1915-1934)", "Spectrum Modern History", "his-02",
     [
         "Early Experiments: Champaran (1917, Tinkathia indigo), Ahmedabad Mill Strike (1918, first hunger strike), Kheda (1918, first non-cooperation)",
         "Rowlatt Act & Jallianwala Bagh Massacre (1919); Khilafat Movement & Non-Cooperation Movement (1920-22); Chauri Chaura incident withdrawal",
         "Swarajists (CR Das, Motilal Nehru) vs No-Changers (Vallabhbhai Patel, Rajendra Prasad)",
         "Civil Disobedience Movement (1930): Dandi March (Salt Satyagraha), Gandhi-Irwin Pact (1931), Karachi Session 1931 (Resolution on FR & National Economic Programme)"
     ],
     "UNGIST CSAT: Full CSAT Mock Drill 2 — Speed Logical Reasoning",
     "The Karachi Session of INC (1931), presided over by Sardar Patel, adopted the historic resolutions on Fundamental Rights and the National Economic Programme."
    ),
    (101, "History", "Quit India Movement, INA, Subhas Chandra Bose & Partition (1939-1947)", "Spectrum Modern History", "his-02",
     [
         "August Offer 1940 & Individual Satyagraha (Vinoba Bhave first, Nehru second)",
         "Cripps Mission 1942 ('Post-dated cheque on a crashing bank') & Quit India Resolution ('Do or Die', Bombay Gowalia Tank)",
         "Indian National Army (INA) & Netaji Subhas Chandra Bose: Provisional Government of Free India in Singapore; INA Trials at Red Fort",
         "Wavell Plan (Shimla Conference 1945), Cabinet Mission Plan 1946 (Rejected Pakistan, grouping scheme), Mountbatten Plan (June 3 Plan, Partition)"
     ],
     "UNGIST CSAT: Full CSAT Mock Drill 2 — Speed Reading Comprehension",
     "The Quit India Movement was largely leaderless after the midnight arrest of top leaders (Operation Zero Hour), unleashing spontaneous mass resistance."
    ),
    (102, "History", "Constitutional Developments under British Rule: Acts of 1909, 1919 & 1935", "Spectrum / Laxmikanth Ch 1", "his-03",
     [
         "Morley-Minto Reforms 1909: Separate electorates for Muslims; Satyendra Prasad Sinha first Indian in Viceroy's Executive Council",
         "Montagu-Chelmsford Reforms (Govt of India Act 1919): Dyarchy in Provinces (Transferred vs Reserved subjects), Bicameralism at Centre",
         "Government of India Act 1935: All-India Federation (never implemented), Provincial Autonomy (Dyarchy abolished in provinces, introduced at Centre)",
         "Federal Court established (1937), Reserve Bank of India establishment mandate"
     ],
     "UNGIST CSAT: Data Sufficiency Master Traps and Pitfalls",
     "Dyarchy was introduced in the provinces by the 1919 Act, but abolished in provinces and introduced at the Centre by the 1935 Act."
    ),
    (103, "ScienceTech", "Space Technology: ISRO Launch Vehicles, Orbits & Flagship Missions", "ISRO / The Hindu", "sci-01",
     [
         "Launch Vehicles: PSLV (Polar Satellite Launch Vehicle, 4 stages: Solid-Liquid-Solid-Liquid), GSLV Mk II (Cryogenic upper stage), LVM3 / GSLV Mk III (Heavy lifter)",
         "Satellite Orbits: Low Earth Orbit (LEO, 160-2000 km), Sun-Synchronous Orbit (SSO), Geostationary (GEO, 35,786 km, circular above equator), Geosynchronous (GSO)",
         "Flagship Missions: Chandrayaan-3 (Shiv Shakti point, Pragyan rover), Aditya-L1 (Lagrange point 1 halo orbit, uninterrupted solar view), Gaganyaan (Human spaceflight)",
         "Private Space Sector: IN-SPACe (Single-window authorization), NewSpace India Limited (NSIL, commercial arm)"
     ],
     "UNGIST CSAT: Missing Numbers & Matrix Multi-Pattern Deductions",
     "PSLV uses alternating solid and liquid fuel stages (Solid-Liquid-Solid-Liquid), making it ISRO's most versatile and dependable workhorse."
    ),
    (104, "ScienceTech", "Biotechnology, Genetic Engineering & Defense/Emerging Tech", "The Hindu SciTech / DRDO", "sci-02",
     [
         "CRISPR-Cas9: Molecular scissors for targeted gene editing; Guide RNA, Cas9 enzyme; Sickle cell therapy (Casgevy)",
         "Vaccine Platforms: mRNA vaccines (Pfizer, Moderna), Viral vector (Covishield/AstraZeneca), Inactivated whole virus (Covaxin), DNA vaccine (ZyCoV-D)",
         "Defense Technology: Integrated Guided Missile Development Programme (IGMDP - PATNA: Prithvi, Agni, Trishul, Nag, Akash)",
         "Emerging Tech: Quantum Key Distribution (QKD), Generative AI & Large Language Models, Semiconductor fabrication (Lithography)"
     ],
     "UNGIST CSAT: Puzzles Multi-Variable Scheduling & Categorization",
     "CRISPR-Cas9 allows precise alteration of DNA sequences in living cells, recognized by the 2020 Nobel Prize in Chemistry."
    ),
    (105, "History", "Weekly Consolidation 15: Phase 1 Grand Milestone Foundational Exam", "Weekly Revision Mode", "his-02",
     [
         "Comprehensive 100-Question All-Syllabus Grand Mock Test (Polity, Economy, Geography, Environment, History, SciTech)",
         "Simulate real UPSC examination hall conditions (09:30-11:30 AM Paper 1, 14:30-16:30 PM CSAT Paper 2)",
         "Complete Phase 1 Audit: 105 days of foundational ground-up conceptual building concluded",
         "Calculate cumulative foundational accuracy and lock in targets for Phase 2 Consolidated Revision"
     ],
     "UNGIST CSAT: Complete Official CSAT 2023 Paper Simulation",
     "Milestone Achieved: 105 days of rigorous foundational learning completed. The 7-8 year gap is officially bridged. You now move from learner to master."
    )
]

print(f"Base plan specs loaded for {len(plan_specs)} foundational days.")
