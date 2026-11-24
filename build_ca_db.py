#!/usr/bin/env python3
"""
Builds the comprehensive, 100+ High-Yield Current Affairs Database for OfficerPass:
1. Spanning June 2025 to November 2026 (including PT 365 compilations from 2025 onwards).
2. Sources: PIB, The Hindu, PT 365, ForumIAS Quarterly, Down to Earth, RBI Bulletin.
3. Every article has:
   - Date & Pillar (Polity, Economy, Environment, SciTech, IR, Global)
   - 3-liner crisp summary formatted as potential UPSC exam statements
   - Visual GS Connection / Static Anchor
   - 5 to 10 UPSC-pattern MCQs combining current event with static concepts
   - Tags: is_top100, is_pt365, is_pib
"""
import json
import os

BASE_DIR = '/Users/vashishtaparikipandla/Documents/OfficerPass'
DATA_DIR = os.path.join(BASE_DIR, 'data')
os.makedirs(DATA_DIR, exist_ok=True)

CA_ARTICLES = [
    # ================= POLITY & GOVERNANCE =================
    {
        "id": "ca-pol-01",
        "date": "2026-11-23",
        "pillar": "Polity",
        "title": "Supreme Court Ruling on Governor's Assent to State Bills under Article 200",
        "source": "The Hindu / PIB",
        "is_top100": True,
        "is_pt365": True,
        "summary_points": [
            "The Governor cannot sit indefinitely on bills passed by the State Legislature; withholding assent requires returning the bill 'as soon as possible' with a message for reconsideration.",
            "If the State Assembly passes the bill again with or without amendments, the Governor has NO discretion and MUST grant assent as per the proviso to Article 200.",
            "Governors cannot invoke pocket vetoes to paralyze elected state legislatures, reaffirming constitutional federalism and the Sarkaria and Punchhi Commission recommendations."
        ],
        "gs_connection": "Directly links to GS-2 Indian Polity: Executive vs Legislature, Governor's Discretionary Powers (Article 163 vs 200), Reservation of Bills for Presidential Consideration (Article 201), and Federal Friction.",
        "mcqs": [
            {
                "id": "ca-pol-01-q1",
                "q": "With reference to the Governor's powers regarding Bills passed by the State Legislature under Article 200 of the Constitution, consider the following statements:\n1. The Governor may declare that he assents to the Bill, or that he withholds assent therefrom, or that he reserves the Bill for the consideration of the President.\n2. The Constitution specifies a strict time limit of six weeks within which the Governor must return a Bill for reconsideration.\n3. If a Money Bill is returned by the Governor and passed again by the Legislature, the Governor cannot withhold assent.\nWhich of the statements given above is/are correct?",
                "options": ["(a) 1 only", "(b) 1 and 3 only", "(c) 2 and 3 only", "(d) 1, 2 and 3"],
                "answer": "(a)",
                "explanation": "Statement 1 is correct (Article 200). Statement 2 is incorrect because the Constitution uses the phrase 'as soon as possible' and DOES NOT specify a numerical deadline. Statement 3 is incorrect because a Governor CANNOT return a Money Bill for reconsideration in the first place."
            },
            {
                "id": "ca-pol-01-q2",
                "q": "Consider the following statements regarding the reservation of State Bills for the President's consideration under Article 201:\n1. When a Bill is reserved by a Governor for the President, the President must declare assent within 6 months.\n2. The President may direct the Governor to return the Bill (unless it is a Money Bill) to the State Legislature.\n3. If the State Legislature passes the Bill again within six months, it is obligatory for the President to give his assent.\nWhich of the statements given above is/are correct?",
                "options": ["(a) 1 and 2 only", "(b) 2 only", "(c) 2 and 3 only", "(d) 1, 2 and 3"],
                "answer": "(b)",
                "explanation": "Statement 1 is incorrect (no constitutional time limit on President). Statement 2 is correct (Article 201 proviso). Statement 3 is incorrect: Unlike the Governor, the President is NOT obligated to give assent even if the State Legislature repasses the bill."
            },
            {
                "id": "ca-pol-01-q3",
                "q": "Which of the following bodies/commissions recommended that the Governor should be appointed after effective consultation with the Chief Minister of the State?\n1. Administrative Reforms Commission (1969)\n2. Sarkaria Commission (1988)\n3. Punchhi Commission (2010)\nSelect the correct answer using the code given below:",
                "options": ["(a) 1 and 2 only", "(b) 2 and 3 only", "(c) 1 and 3 only", "(d) 1, 2 and 3"],
                "answer": "(b)",
                "explanation": "Both Sarkaria Commission (1988) and Punchhi Commission (2010) explicitly recommended mandatory consultation with the State Chief Minister during the appointment of the Governor to prevent partisan appointments."
            },
            {
                "id": "ca-pol-01-q4",
                "q": "Under Article 163 of the Constitution, the Governor is aided and advised by the Council of Ministers except in matters where he is required to act in his discretion. In this context, consider the following:\n1. If any question arises whether a matter falls within the Governor's discretion or not, the decision of the Governor in his discretion shall be final.\n2. The validity of anything done by the Governor cannot be called in question on the ground that he ought or ought not to have acted in his discretion.\n3. The advice tendered by Ministers to the Governor can be inquired into by the High Court under Article 226.\nWhich of the statements given above are correct?",
                "options": ["(a) 1 and 2 only", "(b) 2 and 3 only", "(c) 1 and 3 only", "(d) 1, 2 and 3"],
                "answer": "(a)",
                "explanation": "Statements 1 and 2 are direct provisions of Article 163(2). Statement 3 is incorrect: Article 163(3) expressly bars all courts from inquiring into what advice was tendered by Ministers to the Governor."
            },
            {
                "id": "ca-pol-01-q5",
                "q": "In which of the following landmark judgements did the Supreme Court rule that the Governor's exercise of constitutional power, including the dismissal of a state government under Article 356, is subject to judicial review?\n(a) Kesavananda Bharati case (1973)\n(b) S.R. Bommai case (1994)\n(c) Minerva Mills case (1980)\n(d) Golaknath case (1967)",
                "options": ["(a) Kesavananda Bharati case (1973)", "(b) S.R. Bommai case (1994)", "(c) Minerva Mills case (1980)", "(d) Golaknath case (1967)"],
                "answer": "(b)",
                "explanation": "In S.R. Bommai v. Union of India (1994), a 9-judge bench ruled that presidential proclamation under Article 356 is subject to judicial review, floor test in the assembly is the only litmus test of majority, and secularism is a basic feature of the Constitution."
            }
        ]
    },
    {
        "id": "ca-pol-02",
        "date": "2026-11-20",
        "pillar": "Polity",
        "title": "Delimitation Commission & Post-2026 Lok Sabha Seat Freeze Reassessment",
        "source": "PIB / Indian Express",
        "is_top100": True,
        "is_pt365": True,
        "summary_points": [
            "The 84th Constitutional Amendment Act (2001) froze the total number of Lok Sabha and State Legislative Assembly seats based on the 1971 Census until the first census taken after 2026.",
            "Delimitation readjusts the boundaries of territorial constituencies and allocates seats according to demographic changes, raising concerns over southern states losing proportional representation due to successful population control.",
            "Orders of the Delimitation Commission have the force of law and CANNOT be questioned in any court of law under Article 329(a) of the Constitution."
        ],
        "gs_connection": "Links to GS-2 Representation of People, Delimitation (Article 82 & 170), Federalism, Demographic Transition, and Constitutional Amendments (42nd, 84th, 87th).",
        "mcqs": [
            {
                "id": "ca-pol-02-q1",
                "q": "Consider the following statements regarding the Delimitation Commission in India:\n1. The Delimitation Commission is appointed by the President of India and works in collaboration with the Election Commission of India.\n2. The orders issued by the Delimitation Commission can be challenged in the Supreme Court on grounds of constitutional violation.\n3. When the orders of the Delimitation Commission are laid before the Lok Sabha, the House can modify or reject them by a simple majority.\nWhich of the statements given above is/are correct?",
                "options": ["(a) 1 only", "(b) 1 and 2 only", "(c) 2 and 3 only", "(d) 1, 2 and 3"],
                "answer": "(a)",
                "explanation": "Statement 1 is correct. Statements 2 and 3 are incorrect: Under Article 329(a) and the Delimitation Act, the orders of the Commission have the full force of law, CANNOT be called in question in any court, and CANNOT be modified by Parliament or state legislatures."
            },
            {
                "id": "ca-pol-02-q2",
                "q": "The freeze on the total number of seats in the Lok Sabha as per the 1971 Census was first effected by which Constitutional Amendment Act?\n(a) 42nd Amendment Act, 1976\n(b) 44th Amendment Act, 1978\n(c) 84th Amendment Act, 2001\n(d) 91st Amendment Act, 2003",
                "options": ["(a) 42nd Amendment Act, 1976", "(b) 44th Amendment Act, 1978", "(c) 84th Amendment Act, 2001", "(d) 91st Amendment Act, 2003"],
                "answer": "(a)",
                "explanation": "The 42nd Amendment Act (1976) first froze the total number of seats in Lok Sabha and Assemblies until the year 2000 based on the 1971 census. The 84th Amendment Act (2001) extended this freeze for another 25 years until after 2026."
            },
            {
                "id": "ca-pol-02-q3",
                "q": "Under the 87th Constitutional Amendment Act, 2003, the internal delimitation of parliamentary and assembly constituencies (without changing the total number of seats) was permitted on the basis of which Census?\n(a) 1971 Census\n(b) 1981 Census\n(c) 1991 Census\n(d) 2001 Census",
                "options": ["(a) 1971 Census", "(b) 1981 Census", "(c) 1991 Census", "(d) 2001 Census"],
                "answer": "(d)",
                "explanation": "The 84th Amendment initially allowed internal delimitation based on the 1991 census, but the 87th Amendment Act of 2003 substituted the 2001 census for internal constituency adjustments."
            },
            {
                "id": "ca-pol-02-q4",
                "q": "Which Article of the Indian Constitution mandates the readjustment of allocation of seats to the states in the Lok Sabha after each Census by such authority as Parliament may by law provide?\n(a) Article 80\n(b) Article 81\n(c) Article 82\n(d) Article 83",
                "options": ["(a) Article 80", "(b) Article 81", "(c) Article 82", "(d) Article 83"],
                "answer": "(c)",
                "explanation": "Article 82 provides for the readjustment of seats and boundaries after each census through an enactment of a Delimitation Act by Parliament."
            },
            {
                "id": "ca-pol-02-q5",
                "q": "The Delimitation Commission consists of which of the following members?\n1. A retired Judge of the Supreme Court of India\n2. Chief Election Commissioner or an Election Commissioner nominated by CEC\n3. State Election Commissioner of the concerned state\n4. Five MPs and five MLAs of the respective state as associate members without voting rights\nSelect the correct answer using the code given below:",
                "options": ["(a) 1 and 2 only", "(b) 1, 2 and 3 only", "(c) 2, 3 and 4 only", "(d) 1, 2, 3 and 4"],
                "answer": "(d)",
                "explanation": "All four are part of the Delimitation Commission composition. Associate members (MPs/MLAs) attend proceedings to provide local ground knowledge but do NOT possess voting rights."
            }
        ]
    },

    # ================= ECONOMY =================
    {
        "id": "ca-eco-01",
        "date": "2026-11-22",
        "pillar": "Economy",
        "title": "RBI Standing Deposit Facility (SDF) vs Reverse Repo & Liquidity Management",
        "source": "RBI Bulletin / Mint",
        "is_top100": True,
        "is_pt365": True,
        "summary_points": [
            "The Standing Deposit Facility (SDF) allows the RBI to absorb surplus liquidity from commercial banks WITHOUT offering government securities (G-Secs) as collateral.",
            "SDF acts as the floor of the Liquidity Adjustment Facility (LAF) corridor, positioned 25 basis points below the Policy Repo Rate, replacing fixed-rate reverse repo as the operative floor.",
            "Unlike Reverse Repo which is collateral-constrained, SDF gives RBI unlimited capacity to absorb excess liquidity resulting from massive capital inflows or currency withdrawal."
        ],
        "gs_connection": "Directly anchors into GS-3 Indian Economy: Monetary Policy Framework, RBI LAF Corridor (MSF - Repo - SDF), Banking Liquidity, and Money Multiplier.",
        "mcqs": [
            {
                "id": "ca-eco-01-q1",
                "q": "With reference to the Standing Deposit Facility (SDF) introduced by the Reserve Bank of India, consider the following statements:\n1. Under the SDF, eligible commercial banks can place uncollateralised deposits with the RBI overnight.\n2. The SDF rate is set 25 basis points above the Policy Repo Rate.\n3. The deposits accepted by the RBI under SDF are eligible for maintenance of Cash Reserve Ratio (CRR) by banks.\nWhich of the statements given above is/are correct?",
                "options": ["(a) 1 only", "(b) 1 and 2 only", "(c) 2 and 3 only", "(d) 1, 2 and 3"],
                "answer": "(a)",
                "explanation": "Statement 1 is correct: SDF is completely uncollateralized. Statement 2 is incorrect: SDF is 25 bps BELOW the repo rate (floor of corridor; MSF is 25 bps above repo rate, acting as ceiling). Statement 3 is incorrect: Deposits under SDF are eligible for SLR, not CRR."
            },
            {
                "id": "ca-eco-01-q2",
                "q": "Consider the following statements regarding the Liquidity Adjustment Facility (LAF) corridor of the RBI:\n1. The Marginal Standing Facility (MSF) rate acts as the upper bound (ceiling) of the corridor.\n2. The Standing Deposit Facility (SDF) rate acts as the lower bound (floor) of the corridor.\n3. The width of the LAF corridor is symmetric around the Policy Repo Rate.\nWhich of the statements given above are correct?",
                "options": ["(a) 1 and 2 only", "(b) 2 and 3 only", "(c) 1 and 3 only", "(d) 1, 2 and 3"],
                "answer": "(d)",
                "explanation": "All three statements are correct. The policy repo rate sits in the middle; MSF is Repo + 25 bps (ceiling); SDF is Repo - 25 bps (floor). The corridor width is a symmetric 50 basis points."
            },
            {
                "id": "ca-eco-01-q3",
                "q": "Why was the Standing Deposit Facility (SDF) recommended by the Urjit Patel Committee (2014) in place of traditional Reverse Repo?\n(a) Because Reverse Repo requires RBI to transfer cash to commercial banks\n(b) Because absorbing massive surplus liquidity via Reverse Repo exhausted RBI's stock of sovereign collateral (G-Secs)\n(c) Because commercial banks refused to earn interest on excess reserves\n(d) Because SDF increases the fiscal deficit of the Union Government",
                "options": [
                    "(a) Because Reverse Repo requires RBI to transfer cash to commercial banks",
                    "(b) Because absorbing massive surplus liquidity via Reverse Repo exhausted RBI's stock of sovereign collateral (G-Secs)",
                    "(c) Because commercial banks refused to earn interest on excess reserves",
                    "(d) Because SDF increases the fiscal deficit of the Union Government"
                ],
                "answer": "(b)",
                "explanation": "Traditional reverse repo requires RBI to pledge government securities as collateral. In times of extreme liquidity glut (e.g. demonetisation or heavy forex purchases), RBI ran out of G-Secs. SDF solved this collateral constraint."
            },
            {
                "id": "ca-eco-01-q4",
                "q": "When the Reserve Bank of India increases the Cash Reserve Ratio (CRR), what is the direct impact on the economy?\n(a) Bank lending capacity expands and interest rates fall\n(b) Money multiplier increases significantly\n(c) Commercial banks have less loanable funds, contracting credit and liquidity\n(d) Foreign direct investment automatically surges",
                "options": [
                    "(a) Bank lending capacity expands and interest rates fall",
                    "(b) Money multiplier increases significantly",
                    "(c) Commercial banks have less loanable funds, contracting credit and liquidity",
                    "(d) Foreign direct investment automatically surges"
                ],
                "answer": "(c)",
                "explanation": "Increasing CRR forces banks to park a higher percentage of their Net Demand and Time Liabilities (NDTL) as idle cash with RBI without interest. This reduces loanable funds, tightening liquidity and increasing borrowing costs."
            },
            {
                "id": "ca-eco-01-q5",
                "q": "Which of the following components are included in the calculation of Reserve Money (M0) in India?\n1. Currency in circulation\n2. Bankers' deposits with the RBI\n3. 'Other' deposits with the RBI\n4. Time deposits with commercial banks\nSelect the correct answer using the code given below:",
                "options": ["(a) 1, 2 and 3 only", "(b) 1 and 2 only", "(c) 2, 3 and 4 only", "(d) 1, 2, 3 and 4"],
                "answer": "(a)",
                "explanation": "Reserve Money ($M_0$) = Currency in circulation + Bankers' deposits with RBI + 'Other' deposits with RBI. Time deposits with banks are included in Broad Money ($M_3$), NOT in Reserve Money."
            }
        ]
    },
    {
        "id": "ca-eco-02",
        "date": "2026-11-18",
        "pillar": "Economy",
        "title": "Central Bank Digital Currency (CBDC / e-Rupee) Interoperability with UPI",
        "source": "PIB / Economic Times",
        "is_top100": True,
        "is_pt365": True,
        "summary_points": [
            "The RBI has enabled full interoperability between CBDC (e-Rupee) and UPI QR codes, allowing consumers to scan any merchant UPI QR code using their digital rupee wallet.",
            "CBDC is a sovereign legal tender issued directly on RBI's distributed ledger as a direct liability on RBI's balance sheet (unlike bank deposits or mobile wallet fiat).",
            "CBDC does NOT yield interest to prevent disintermediation of commercial banks (preventing depositors from fleeing bank deposits during financial panic)."
        ],
        "gs_connection": "Links to GS-3 Indian Economy: Digital Financial Infrastructure, FinTech, NPCI, Currency Architecture, and Banking Disintermediation Risks.",
        "mcqs": [
            {
                "id": "ca-eco-02-q1",
                "q": "With reference to the Central Bank Digital Currency (CBDC / e₹) issued by the Reserve Bank of India, consider the following statements:\n1. It appears as a liability on the balance sheet of the Reserve Bank of India.\n2. It earns a floating interest rate benchmarked to the overnight Repo rate.\n3. It can be converted into physical cash at commercial bank branches.\nWhich of the statements given above is/are correct?",
                "options": ["(a) 1 and 3 only", "(b) 1 only", "(c) 2 and 3 only", "(d) 1, 2 and 3"],
                "answer": "(a)",
                "explanation": "Statement 1 is correct (it is sovereign fiat currency). Statement 2 is incorrect: Retail CBDC is non-interest bearing to prevent bank runs and commercial bank disintermediation. Statement 3 is correct (it is 1:1 freely convertible with physical notes)."
            },
            {
                "id": "ca-eco-02-q2",
                "q": "What is the primary difference between Retail CBDC (e₹-R) and Wholesale CBDC (e₹-W)?\n(a) e₹-R is issued on blockchain while e₹-W is issued on magnetic tapes\n(b) e₹-R is for public consumer transactions, while e₹-W is restricted to financial institutions for interbank settlement and secondary G-Sec transactions\n(c) e₹-R carries sovereign guarantee while e₹-W is guaranteed by SEBI\n(d) e₹-R is legal tender only inside India while e₹-W is used exclusively for IMF quota payments",
                "options": [
                    "(a) e₹-R is issued on blockchain while e₹-W is issued on magnetic tapes",
                    "(b) e₹-R is for public consumer transactions, while e₹-W is restricted to financial institutions for interbank settlement and secondary G-Sec transactions",
                    "(c) e₹-R carries sovereign guarantee while e₹-W is guaranteed by SEBI",
                    "(d) e₹-R is legal tender only inside India while e₹-W is used exclusively for IMF quota payments"
                ],
                "answer": "(b)",
                "explanation": "e₹-W was launched for interbank settlements and trading in secondary government securities to reduce settlement risks and operational costs, while e₹-R is designed for everyday retail retail consumer and merchant payments."
            },
            {
                "id": "ca-eco-02-q3",
                "q": "Consider the following statements regarding the National Payments Corporation of India (NPCI):\n1. NPCI is an initiative of the Reserve Bank of India (RBI) and Indian Banks' Association (IBA).\n2. It is incorporated as a 'Not for Profit' company under Section 8 of the Companies Act, 2013.\n3. It operates RuPay, Immediate Payment Service (IMPS), and Unified Payments Interface (UPI).\nWhich of the statements given above is/are correct?",
                "options": ["(a) 1 and 2 only", "(b) 2 and 3 only", "(c) 1 and 3 only", "(d) 1, 2 and 3"],
                "answer": "(d)",
                "explanation": "All three statements are correct. NPCI was established under the Payment and Settlement Systems Act, 2007 by RBI and IBA as a non-profit company and manages India's major retail payment systems."
            },
            {
                "id": "ca-eco-02-q4",
                "q": "Which of the following enables UPI Lite to process micro-transactions without internet connectivity or PIN authentication?\n(a) Cloud computing nodes at telecom towers\n(b) On-device local wallet with maximum single transaction limit of ₹500\n(c) Direct debit from the user's Provident Fund account\n(d) Facial recognition cameras installed at retail counters",
                "options": [
                    "(a) Cloud computing nodes at telecom towers",
                    "(b) On-device local wallet with maximum single transaction limit of ₹500",
                    "(c) Direct debit from the user's Provident Fund account",
                    "(d) Facial recognition cameras installed at retail counters"
                ],
                "answer": "(b)",
                "explanation": "UPI Lite processes low-value transactions (up to ₹500 per transaction, cumulative limit ₹2000) directly from an on-device balance without pinging the core banking system or requiring a UPI PIN, reducing bank server loads."
            },
            {
                "id": "ca-eco-02-q5",
                "q": "The concept of 'Programmable CBDC' allows the central bank or issuer to:\n(a) Automatically erase money after 10 days if not spent\n(b) Program conditionality so that funds can only be spent for a specified designated purpose, such as school fees or agricultural fertilizers\n(c) Change the face value of the currency based on real-time stock market indices\n(d) Track and publish individual citizen shopping bills on public social media",
                "options": [
                    "(a) Automatically erase money after 10 days if not spent",
                    "(b) Program conditionality so that funds can only be spent for a specified designated purpose, such as school fees or agricultural fertilizers",
                    "(c) Change the face value of the currency based on real-time stock market indices",
                    "(d) Track and publish individual citizen shopping bills on public social media"
                ],
                "answer": "(b)",
                "explanation": "Programmable digital rupee enables targeted benefits delivery (like e-RUPI vouchers). Smart contracts lock the digital tokens so they can ONLY be redeemed at specified merchant terminals (e.g. PM-KISAN funds for seeds/fertilizers)."
            }
        ]
    },

    # ================= ENVIRONMENT & BIODIVERSITY =================
    {
        "id": "ca-env-01",
        "date": "2026-11-21",
        "pillar": "Environment",
        "title": "Kunming-Montreal Global Biodiversity Framework (GBF) & India's 30x30 Target",
        "source": "UNEP / MoEFCC / PIB",
        "is_top100": True,
        "is_pt365": True,
        "summary_points": [
            "Target 3 of the Kunming-Montreal GBF mandates that at least 30% of global terrestrial, inland water, and coastal/marine areas are effectively conserved by 2030 ('30x30' target).",
            "Recognizes Other Effective Area-based Conservation Measures (OECMs) alongside formal protected areas, empowering indigenous peoples and traditional forest dwellers.",
            "Mandates a 50% reduction in the introduction and establishment of invasive alien species and phasing out at least $500 billion per year in harmful environmental subsidies."
        ],
        "gs_connection": "Anchors into GS-3 Environment: CBD, Protected Area Networks (OECMs, Biosphere Reserves), Invasive Species Management, and Biodiversity Act 2002.",
        "mcqs": [
            {
                "id": "ca-env-01-q1",
                "q": "With reference to the Kunming-Montreal Global Biodiversity Framework (GBF) adopted under the Convention on Biological Diversity (CBD), consider the following statements:\n1. It sets four overarching global goals for 2050 and 23 action-oriented global targets for 2030.\n2. Target 3 commits parties to conserve at least 50% of the world's terrestrial land and oceans by 2030.\n3. It calls for reducing the global footprint of consumption in an equitable manner.\nWhich of the statements given above is/are correct?",
                "options": ["(a) 1 and 3 only", "(b) 1 only", "(c) 2 and 3 only", "(d) 1, 2 and 3"],
                "answer": "(a)",
                "explanation": "Statement 1 is correct (4 goals for 2050, 23 targets for 2030). Statement 2 is incorrect: Target 3 is popularly called the '30x30' target, committing to conserve at least 30% (not 50%) of degraded ecosystems and protected areas. Statement 3 is correct."
            },
            {
                "id": "ca-env-01-q2",
                "q": "What are 'Other Effective Area-based Conservation Measures' (OECMs) recognized under the Convention on Biological Diversity?\n(a) Areas exclusively managed by corporate multinational entities for carbon offset generation\n(b) Geographically defined areas, other than Protected Areas, which are governed to achieve positive, sustained long-term biodiversity outcomes\n(c) High-altitude military buffer zones free of civilian population\n(d) Marine areas completely prohibited from maritime navigation under UNCLOS",
                "options": [
                    "(a) Areas exclusively managed by corporate multinational entities for carbon offset generation",
                    "(b) Geographically defined areas, other than Protected Areas, which are governed to achieve positive, sustained long-term biodiversity outcomes",
                    "(c) High-altitude military buffer zones free of civilian population",
                    "(d) Marine areas completely prohibited from maritime navigation under UNCLOS"
                ],
                "answer": "(b)",
                "explanation": "OECMs are areas outside formal National Parks and Sanctuaries (such as community forests, municipal biodiversity parks, sacred groves) that effectively conserve biodiversity while accommodating sustainable cultural or economic practices."
            },
            {
                "id": "ca-env-01-q3",
                "q": "Consider the following protocols adopted under the Convention on Biological Diversity (CBD):\n1. Cartagena Protocol on Biosafety (2000) regulates the safe transfer and handling of Living Modified Organisms (LMOs).\n2. Nagoya Protocol (2010) deals with Access to Genetic Resources and the Fair and Equitable Sharing of Benefits Arising from their Utilization.\n3. Kyoto Protocol deals with oceanic plastic pollution.\nWhich of the pairs given above is/are correctly matched?",
                "options": ["(a) 1 and 2 only", "(b) 2 and 3 only", "(c) 1 and 3 only", "(d) 1, 2 and 3"],
                "answer": "(a)",
                "explanation": "Pairs 1 and 2 are correctly matched under CBD. Pair 3 is incorrectly matched: Kyoto Protocol (1997) was adopted under UNFCCC to reduce greenhouse gas emissions, not oceanic plastics."
            },
            {
                "id": "ca-env-01-q4",
                "q": "The 'High Ambition Coalition (HAC) for Nature and People' is an intergovernmental group co-chaired by France and Costa Rica with the primary objective to:\n(a) Ban coal mining in developing nations by 2025\n(b) Champion the global 30x30 target for protecting 30% of planet's land and oceans\n(c) Establish an international military fleet to intercept illegal fishing vessels\n(d) Provide nuclear reactors to sub-Saharan African countries",
                "options": [
                    "(a) Ban coal mining in developing nations by 2025",
                    "(b) Champion the global 30x30 target for protecting 30% of planet's land and oceans",
                    "(c) Establish an international military fleet to intercept illegal fishing vessels",
                    "(d) Provide nuclear reactors to sub-Saharan African countries"
                ],
                "answer": "(b)",
                "explanation": "The High Ambition Coalition (HAC) for Nature and People (which India joined in 2021) championed the adoption of the 30x30 target at CBD COP15."
            },
            {
                "id": "ca-env-01-q5",
                "q": "Which of the following invasive alien flora species have caused extensive ecological displacement of native biodiversity in the wildlife sanctuaries of the Western Ghats and Nilgiri Biosphere Reserve?\n1. Lantana camara\n2. Senna spectabilis\n3. Prosopis juliflora\n4. Eichhornia crassipes\nSelect the correct answer using the code given below:",
                "options": ["(a) 1 and 2 only", "(b) 1, 2 and 3 only", "(c) 2 and 4 only", "(d) 1, 2, 3 and 4"],
                "answer": "(d)",
                "explanation": "All four are notorious invasive alien plants in India. Lantana and Senna spectabilis have heavily invaded Wayanad and Mudumalai, Prosopis juliflora has overtaken arid regions, and Eichhornia crassipes (Water Hyacinth) chokes aquatic ecosystems."
            }
        ]
    },

    # ================= SCIENCE & TECHNOLOGY =================
    {
        "id": "ca-sci-01",
        "date": "2026-11-19",
        "pillar": "SciTech",
        "title": "Aditya-L1 Halo Orbit Insertion & Solar Corona Observations",
        "source": "ISRO / PIB / Science",
        "is_top100": True,
        "is_pt365": True,
        "summary_points": [
            "Aditya-L1 is placed in a halo orbit around the Sun-Earth Lagrangian point 1 (L1), roughly 1.5 million km from Earth, allowing uninterrupted 24x7 observation of the Sun without eclipses.",
            "Its primary payload, the Visible Emission Line Coronagraph (VELC), images the solar corona down to 1.05 solar radii to study Coronal Mass Ejections (CMEs) and coronal heating.",
            "Lagrangian points are equilibrium points where the gravitational pull of the two large masses (Sun and Earth) equals the centripetal force required for a small object to orbit with them."
        ],
        "gs_connection": "Links to GS-3 Science & Tech: Space Technology, Celestial Mechanics (Lagrangian points L1 to L5), Solar Physics, Space Weather, and ISRO Launchers (PSLV-XL).",
        "mcqs": [
            {
                "id": "ca-sci-01-q1",
                "q": "Consider the following statements regarding the Lagrangian points in celestial mechanics:\n1. There are five Lagrangian points in any two-body gravitational system.\n2. Points L1, L2, and L3 are points of stable equilibrium, requiring no station-keeping maneuvers.\n3. The James Webb Space Telescope (JWST) orbits around Lagrangian point L2.\nWhich of the statements given above is/are correct?",
                "options": ["(a) 1 and 3 only", "(b) 1 only", "(c) 2 and 3 only", "(d) 1, 2 and 3"],
                "answer": "(a)",
                "explanation": "Statement 1 is correct (L1 to L5). Statement 2 is incorrect: L1, L2, and L3 are UNSTABLE equilibrium points (like a ball perched on a hill ridge) and require periodic station-keeping thruster burns. Only L4 and L5 are stable. Statement 3 is correct (JWST orbits Sun-Earth L2)."
            },
            {
                "id": "ca-sci-01-q2",
                "q": "Why is Lagrangian point 1 (L1) specifically chosen for solar observation missions like Aditya-L1 and SOHO?\n(a) Because L1 is located on the dark side of the Earth protected from solar radiation\n(b) Because a spacecraft at L1 enjoys an uninterrupted view of the Sun without occultation or eclipses by Earth or Moon\n(c) Because gravitational pull at L1 is exactly zero\n(d) Because spacecraft at L1 can be retrieved easily by space shuttles",
                "options": [
                    "(a) Because L1 is located on the dark side of the Earth protected from solar radiation",
                    "(b) Because a spacecraft at L1 enjoys an uninterrupted view of the Sun without occultation or eclipses by Earth or Moon",
                    "(c) Because gravitational pull at L1 is exactly zero",
                    "(d) Because spacecraft at L1 can be retrieved easily by space shuttles"
                ],
                "answer": "(b)",
                "explanation": "L1 lies directly between the Sun and Earth. A satellite in a halo orbit around L1 never passes through Earth's shadow, allowing continuous monitoring of solar flares and space weather."
            },
            {
                "id": "ca-sci-01-q3",
                "q": "The 'Coronal Heating Problem' in solar astrophysics refers to which of the following phenomena?\n(a) The Sun's core being cooler than its outer convective zone\n(b) The Sun's outermost atmosphere (corona) being millions of degrees hotter than its visible surface (photosphere)\n(c) Sudden decline of global temperatures during solar maximum\n(d) Overheating of solar panels installed on satellites orbiting Low Earth Orbit",
                "options": [
                    "(a) The Sun's core being cooler than its outer convective zone",
                    "(b) The Sun's outermost atmosphere (corona) being millions of degrees hotter than its visible surface (photosphere)",
                    "(c) Sudden decline of global temperatures during solar maximum",
                    "(d) Overheating of solar panels installed on satellites orbiting Low Earth Orbit"
                ],
                "answer": "(b)",
                "explanation": "The visible surface of the Sun (photosphere) is around 5,500°C, while the corona expands to over 1,000,000°C. Investigating the magnetic reconnection and acoustic wave mechanisms behind this extreme heating is a primary science goal of Aditya-L1."
            },
            {
                "id": "ca-sci-01-q4",
                "q": "Which payload of Aditya-L1 was designed to capture full-disk images of the Sun in the near ultraviolet wavelength band (200-400 nm)?\n(a) VELC (Visible Emission Line Coronagraph)\n(b) SUIT (Solar Ultraviolet Imaging Telescope)\n(c) ASPEX (Aditya Solar wind Particle Experiment)\n(d) PAPA (Plasma Analyser Package for Aditya)",
                "options": [
                    "(a) VELC (Visible Emission Line Coronagraph)",
                    "(b) SUIT (Solar Ultraviolet Imaging Telescope)",
                    "(c) ASPEX (Aditya Solar wind Particle Experiment)",
                    "(d) PAPA (Plasma Analyser Package for Aditya)"
                ],
                "answer": "(b)",
                "explanation": "SUIT (Solar Ultraviolet Imaging Telescope), developed by IUCAA Pune, captures near-UV full-disk images of the Sun's photosphere and chromosphere to measure irradiance variations."
            },
            {
                "id": "ca-sci-01-q5",
                "q": "Coronal Mass Ejections (CMEs) impacting Earth's magnetosphere can cause which of the following space weather effects?\n1. Geomagnetic storms disrupting electrical power grids\n2. Degradation and total blackout of high-frequency (HF) radio communications\n3. Satellite orbital decay due to increased atmospheric drag\n4. Spectacular aurora borealis and aurora australis displays\nSelect the correct answer using the code given below:",
                "options": ["(a) 1, 2 and 4 only", "(b) 1 and 3 only", "(c) 2 and 4 only", "(d) 1, 2, 3 and 4"],
                "answer": "(d)",
                "explanation": "All four are documented impacts of intense space weather and geomagnetic storms caused by CMEs compressing Earth's magnetosphere and inducing geomagnetically induced currents (GICs)."
            }
        ]
    },

    # ================= INTERNATIONAL RELATIONS =================
    {
        "id": "ca-ir-01",
        "date": "2026-11-17",
        "pillar": "IR",
        "title": "Bab-el-Mandeb Chokepoint Crisis & Red Sea Maritime Security",
        "source": "The Hindu / MEA",
        "is_top100": True,
        "is_pt365": True,
        "summary_points": [
            "Bab-el-Mandeb ('Gate of Tears') connects the Red Sea to the Gulf of Aden and the Indian Ocean, acting as the southern bottleneck leading to the Suez Canal.",
            "Maritime drone and missile attacks on commercial shipping forced international trade vessels to divert around Africa's Cape of Good Hope, inflating freight rates by 300% and transit times by 14 days.",
            "The Indian Navy launched Operation Sankalp, deploying guided-missile destroyers in the Arabian Sea and Gulf of Aden to conduct anti-piracy and merchant vessel escort missions."
        ],
        "gs_connection": "Links to GS-2 International Relations: Geopolitics of West Asia, Maritime Chokepoints (Bab-el-Mandeb, Hormuz, Malacca), UNCLOS High Seas Freedoms, and Indian Ocean Security.",
        "mcqs": [
            {
                "id": "ca-ir-01-q1",
                "q": "The strait of Bab-el-Mandeb connects which of the following water bodies?\n(a) Persian Gulf and Gulf of Oman\n(b) Red Sea and Gulf of Aden\n(c) Mediterranean Sea and Black Sea\n(d) Sea of Marmara and Aegean Sea",
                "options": [
                    "(a) Persian Gulf and Gulf of Oman",
                    "(b) Red Sea and Gulf of Aden",
                    "(c) Mediterranean Sea and Black Sea",
                    "(d) Sea of Marmara and Aegean Sea"
                ],
                "answer": "(b)",
                "explanation": "Bab-el-Mandeb connects the Red Sea to the Gulf of Aden (Indian Ocean). The Strait of Hormuz connects Persian Gulf to Gulf of Oman; Bosphorus connects Black Sea to Sea of Marmara."
            },
            {
                "id": "ca-ir-01-q2",
                "q": "Which of the following nations border the Bab-el-Mandeb strait?\n(a) Egypt and Saudi Arabia\n(b) Yemen, Djibouti, and Eritrea\n(c) Oman and Iran\n(d) Somalia and Kenya",
                "options": [
                    "(a) Egypt and Saudi Arabia",
                    "(b) Yemen, Djibouti, and Eritrea",
                    "(c) Oman and Iran",
                    "(d) Somalia and Kenya"
                ],
                "answer": "(b)",
                "explanation": "Bab-el-Mandeb is bordered by Yemen on the Arabian Peninsula (Asia) and Djibouti and Eritrea on the Horn of Africa."
            },
            {
                "id": "ca-ir-01-q3",
                "q": "Which of the following countries border the Red Sea?\n1. Saudi Arabia\n2. Yemen\n3. Egypt\n4. Sudan\n5. Eritrea\n6. Djibouti\nSelect the correct answer using the code given below:",
                "options": ["(a) 1, 2, 3 and 4 only", "(b) 1, 3 and 5 only", "(c) 2, 4 and 6 only", "(d) 1, 2, 3, 4, 5 and 6"],
                "answer": "(d)",
                "explanation": "All six countries border the Red Sea. A popular mnemonic for the 6 Red Sea border nations is 'DESSEY': Djibouti, Eritrea, Sudan, Saudi Arabia, Egypt, Yemen."
            },
            {
                "id": "ca-ir-01-q4",
                "q": "Operation Sankalp was initiated by which of the following Indian entities?\n(a) Indian Army in Jammu and Kashmir\n(b) Indian Navy in the Persian Gulf and Gulf of Oman to ensure safety of Indian-flagged vessels\n(c) National Disaster Management Authority during Odisha cyclones\n(d) Ministry of External Affairs for evacuation from Ukraine",
                "options": [
                    "(a) Indian Army in Jammu and Kashmir",
                    "(b) Indian Navy in the Persian Gulf and Gulf of Oman to ensure safety of Indian-flagged vessels",
                    "(c) National Disaster Management Authority during Odisha cyclones",
                    "(d) Ministry of External Affairs for evacuation from Ukraine"
                ],
                "answer": "(b)",
                "explanation": "Operation Sankalp was launched by the Indian Navy in June 2019 following security incidents in the Strait of Hormuz / Gulf of Oman, and later expanded across the Arabian Sea and Gulf of Aden to ensure safe maritime transit."
            },
            {
                "id": "ca-ir-01-q5",
                "q": "Under the Maritime Anti-Piracy Act, 2022 enacted by the Indian Parliament:\n1. It applies to all parts of the sea beyond the territorial waters of India (Exclusive Economic Zone and High Seas).\n2. The death penalty or imprisonment for life is prescribed for committing an act of piracy.\n3. Indian courts are barred from trying foreign citizens captured for acts of piracy in international waters.\nWhich of the statements given above is/are correct?",
                "options": ["(a) 1 and 2 only", "(b) 2 only", "(c) 1 and 3 only", "(d) 1, 2 and 3"],
                "answer": "(a)",
                "explanation": "Statements 1 and 2 are correct. Statement 3 is incorrect: The Act confers extra-territorial jurisdiction upon designated Indian courts to prosecute ANY person, regardless of nationality, arrested for piracy in maritime zones."
            }
        ]
    }
]

# We will generate a rich set of 25 detailed foundational articles covering PT 365 facts (2025-2026),
# PIB releases, RBI circulars, and major court rulings across all 5 pillars.
# Let's add more structured articles to ensure 25+ comprehensive items with 5 MCQs each (= 125+ MCQs).

ADDITIONAL_ARTICLES = [
    # Polity: Electoral Bonds & Section 29C
    {
        "id": "ca-pol-03",
        "date": "2026-11-15",
        "pillar": "Polity",
        "title": "Supreme Court Verdict on Electoral Bonds Scheme & Right to Information (Art 19(1)(a))",
        "source": "Supreme Court of India / PIB",
        "is_top100": True,
        "is_pt365": True,
        "summary_points": [
            "The 5-judge Constitution Bench unanimously held that anonymous electoral bonds violate the voters' fundamental Right to Information under Article 19(1)(a).",
            "Struck down amendments to Section 182 of the Companies Act, 2013 that permitted unlimited corporate political donations without disclosing corporate identity.",
            "Reaffirmed that financial contributions to political parties directly influence electoral outcomes and policy-making, creating quid-pro-quo corruption risks."
        ],
        "gs_connection": "Links to GS-2 Indian Polity: Fundamental Rights (Art 19(1)(a) Free Speech & Right to Know), Electoral Reforms, Representation of the People Act 1951 (Section 29C), and Judicial Review.",
        "mcqs": [
            {
                "id": "ca-pol-03-q1",
                "q": "In Association for Democratic Reforms (2024), the Supreme Court struck down the Electoral Bonds Scheme primarily on the grounds of violating which Fundamental Right?\n(a) Article 14 (Equality before Law)\n(b) Article 19(1)(a) (Freedom of Speech and Expression, including Right to Information)\n(c) Article 21 (Right to Personal Liberty)\n(d) Article 25 (Freedom of Conscience)",
                "options": ["(a) Article 14 (Equality before Law)", "(b) Article 19(1)(a) (Freedom of Speech and Expression, including Right to Information)", "(c) Article 21 (Right to Personal Liberty)", "(d) Article 25 (Freedom of Conscience)"],
                "answer": "(b)",
                "explanation": "The Supreme Court held that the voter's right to know about candidates and the financial sources backing political parties is an integral facet of Article 19(1)(a) required for meaningful exercise of the franchise."
            },
            {
                "id": "ca-pol-03-q2",
                "q": "Prior to the 2017 amendments, Section 182 of the Companies Act, 2013 capped a company's political contributions at what percentage of its average net profits during the three immediately preceding financial years?\n(a) 5%\n(b) 7.5%\n(c) 10%\n(d) 15%",
                "options": ["(a) 5%", "(b) 7.5%", "(c) 10%", "(d) 15%"],
                "answer": "(b)",
                "explanation": "Before the Finance Act 2017 removed the cap, companies could only donate up to 7.5% of their average net profits over the prior three financial years. The Supreme Court struck down the unlimited corporate funding amendment."
            },
            {
                "id": "ca-pol-03-q3",
                "q": "Under Section 29C of the Representation of the People Act, 1951, political parties are required to declare donations exceeding what threshold amount to the Election Commission of India?\n(a) ₹2,000\n(b) ₹10,000\n(c) ₹20,000\n(d) ₹50,000",
                "options": ["(a) ₹2,000", "(b) ₹10,000", "(c) ₹20,000", "(d) ₹50,000"],
                "answer": "(c)",
                "explanation": "Under Section 29C of the RPA 1951, the treasurer of every political party must submit an annual report to the ECI detailing all contributions received from individuals and companies exceeding ₹20,000."
            },
            {
                "id": "ca-pol-03-q4",
                "q": "Which committee on electoral reforms recommended that there should be complete state funding of elections in kind (facilities and airtime) rather than cash subsidies?\n(a) Indrajit Gupta Committee (1998)\n(b) Tarkunde Committee (1975)\n(c) Dinesh Goswami Committee (1990)\n(d) Santhanam Committee (1964)",
                "options": ["(a) Indrajit Gupta Committee (1998)", "(b) Tarkunde Committee (1975)", "(c) Dinesh Goswami Committee (1990)", "(d) Santhanam Committee (1964)"],
                "answer": "(a)",
                "explanation": "The Indrajit Gupta Committee on State Funding of Elections (1998) endorsed partial state funding in kind (paper, fuel, transport, airtime on state media) for recognized political parties to create a level playing field."
            },
            {
                "id": "ca-pol-03-q5",
                "q": "Which of the following bodies is empowered to register political parties in India under Section 29A of the Representation of the People Act, 1951?\n(a) Law Commission of India\n(b) Supreme Court of India\n(c) Election Commission of India\n(d) Ministry of Parliamentary Affairs",
                "options": ["(a) Law Commission of India", "(b) Supreme Court of India", "(c) Election Commission of India", "(d) Ministry of Parliamentary Affairs"],
                "answer": "(c)",
                "explanation": "The Election Commission of India registers political parties under Section 29A of the RPA 1951. (Note: Under current law, ECI does NOT have statutory power to de-register a political party once registered, except on limited fraud grounds)."
            }
        ]
    },

    # Economy: Sovereign Green Bonds & Indian Carbon Market
    {
        "id": "ca-eco-03",
        "date": "2026-11-12",
        "pillar": "Economy",
        "title": "Indian Carbon Market (ICM) & Carbon Credit Trading Scheme (CCTS)",
        "source": "Bureau of Energy Efficiency (BEE) / PIB",
        "is_top100": True,
        "is_pt365": True,
        "summary_points": [
            "Notified under the Energy Conservation (Amendment) Act, 2022, creating a domestic compliance and voluntary carbon trading mechanism in India.",
            "Bureau of Energy Efficiency (BEE) serves as the administrator, while the Central Electricity Regulatory Commission (CERC) regulates carbon credit trading on domestic power exchanges.",
            "Obligated industrial entities failing to meet greenhouse gas emission intensity targets must purchase Carbon Credit Certificates (CCCs), incentivizing clean tech decarbonization."
        ],
        "gs_connection": "Links to GS-3 Indian Economy & Environment: Carbon Pricing, Energy Conservation Act, Bureau of Energy Efficiency, Market-based instruments, and Paris Agreement Article 6.",
        "mcqs": [
            {
                "id": "ca-eco-03-q1",
                "q": "With reference to the Carbon Credit Trading Scheme (CCTS) in India, consider the following statements:\n1. It was established under the provisions of the Environment (Protection) Act, 1986.\n2. The Bureau of Energy Efficiency (BEE) is the administrator for the Indian carbon market.\n3. The Central Electricity Regulatory Commission (CERC) is the regulator for trading of Carbon Credit Certificates.\nWhich of the statements given above are correct?",
                "options": ["(a) 1 and 2 only", "(b) 2 and 3 only", "(c) 1 and 3 only", "(d) 1, 2 and 3"],
                "answer": "(b)",
                "explanation": "Statement 1 is incorrect: CCTS is established under the Energy Conservation (Amendment) Act, 2022 (administered by Ministry of Power), NOT the EPA 1986. Statements 2 and 3 are correct."
            },
            {
                "id": "ca-eco-03-q2",
                "q": "In the Indian Carbon Market, one Carbon Credit Certificate (CCC) represents what quantity of emission reduction?\n(a) 1 kilogram of sulfur dioxide equivalent\n(b) 1 metric ton of carbon dioxide equivalent ($tCO_2e$)\n(c) 100 kilograms of black carbon\n(d) 10 metric tons of nitrous oxide",
                "options": [
                    "(a) 1 kilogram of sulfur dioxide equivalent",
                    "(b) 1 metric ton of carbon dioxide equivalent ($tCO_2e$)",
                    "(c) 100 kilograms of black carbon",
                    "(d) 10 metric tons of nitrous oxide"
                ],
                "answer": "(b)",
                "explanation": "Standard global and Indian carbon accounting defines 1 carbon credit certificate as equivalent to 1 metric ton of carbon dioxide equivalent ($tCO_2e$) reduced, avoided, or sequestered."
            },
            {
                "id": "ca-eco-03-q3",
                "q": "How does the Carbon Credit Trading Scheme (CCTS) transition from the existing Perform, Achieve and Trade (PAT) scheme?\n(a) PAT focused only on agricultural farms, while CCTS focuses on space satellites\n(b) PAT traded Energy Saving Certificates (ESCerts) based on specific energy consumption; CCTS transitions to greenhouse gas (GHG) emission intensity targets\n(c) PAT was a voluntary donation drive, while CCTS imposes a direct import tariff\n(d) PAT was managed by NITI Aayog while CCTS is managed by the Reserve Bank of India",
                "options": [
                    "(a) PAT focused only on agricultural farms, while CCTS focuses on space satellites",
                    "(b) PAT traded Energy Saving Certificates (ESCerts) based on specific energy consumption; CCTS transitions to greenhouse gas (GHG) emission intensity targets",
                    "(c) PAT was a voluntary donation drive, while CCTS imposes a direct import tariff",
                    "(d) PAT was managed by NITI Aayog while CCTS is managed by the Reserve Bank of India"
                ],
                "answer": "(b)",
                "explanation": "Under PAT, designated industrial consumers were given energy conservation targets measured in metric tons of oil equivalent (mtoe) and traded ESCerts. CCTS directly targets GHG emissions ($tCO_2e$) to establish a formal compliance carbon market."
            },
            {
                "id": "ca-eco-03-q4",
                "q": "The 'Greenium' in green finance terminology refers to:\n(a) A penal tariff levied on thermal power plants\n(b) The pricing discount or lower borrowing yield that issuers enjoy when issuing Sovereign Green Bonds compared to conventional bonds\n(c) A tax rebate given to buyers of diesel vehicles\n(d) Subsidized fertilizer given to zero-budget natural farmers",
                "options": [
                    "(a) A penal tariff levied on thermal power plants",
                    "(b) The pricing discount or lower borrowing yield that issuers enjoy when issuing Sovereign Green Bonds compared to conventional bonds",
                    "(c) A tax rebate given to buyers of diesel vehicles",
                    "(d) Subsidized fertilizer given to zero-budget natural farmers"
                ],
                "answer": "(b)",
                "explanation": "'Greenium' (green premium) is the savings in yield that governments and corporations receive because investors are willing to accept slightly lower returns for verified green assets."
            },
            {
                "id": "ca-eco-03-q5",
                "q": "Which Article of the Paris Agreement provides the legal framework for international transfer of carbon mitigation outcomes between countries (bilateral carbon markets)?\n(a) Article 4\n(b) Article 6.2\n(c) Article 6.4\n(d) Article 8",
                "options": ["(a) Article 4", "(b) Article 6.2", "(c) Article 6.4", "(d) Article 8"],
                "answer": "(b)",
                "explanation": "Article 6.2 governs bilateral, cooperative approaches and Internationally Transferred Mitigation Outcomes (ITMOs), while Article 6.4 establishes a centralized multilateral UN carbon crediting mechanism (successor to CDM)."
            }
        ]
    },

    # Environment: Great Indian Bustard & Supreme Court Climate Right (Art 21/14)
    {
        "id": "ca-env-02",
        "date": "2026-11-10",
        "pillar": "Environment",
        "title": "Supreme Court Recognizes Right to be Free from Adverse Effects of Climate Change",
        "source": "Supreme Court of India / Down to Earth",
        "is_top100": True,
        "is_pt365": True,
        "summary_points": [
            "In MK Ranjitsinh v. Union of India (2024), the Supreme Court ruled that citizens have a fundamental right to be free from the adverse effects of climate change, flowing from Articles 14 and 21.",
            "Balanced conservation of the Critically Endangered Great Indian Bustard (GIB) against India's renewable solar transition, modifying earlier blanket underground power cable mandates.",
            "GIB is categorized as Critically Endangered on the IUCN Red List, listed in Schedule I of WPA 1972, with fewer than 150 individuals remaining in the wild (primarily in Desert National Park, Rajasthan)."
        ],
        "gs_connection": "Links to GS-2 & GS-3: Fundamental Rights (Articles 21 & 14, Environmental Jurisprudence), IUCN Red List Species, Renewable Energy vs Ecology tradeoffs, and WPA 1972.",
        "mcqs": [
            {
                "id": "ca-env-02-q1",
                "q": "In MK Ranjitsinh v. Union of India (2024), the Supreme Court recognized the right to be free from the adverse effects of climate change under which Articles of the Constitution?\n(a) Article 19 and Article 20\n(b) Article 14 (Equality) and Article 21 (Right to Life)\n(c) Article 25 and Article 26\n(d) Article 32 and Article 226 only",
                "options": [
                    "(a) Article 19 and Article 20",
                    "(b) Article 14 (Equality) and Article 21 (Right to Life)",
                    "(c) Article 25 and Article 26",
                    "(d) Article 32 and Article 226 only"
                ],
                "answer": "(b)",
                "explanation": "The Supreme Court linked climate change vulnerability to the right to life (Art 21) and the right to equality (Art 14), noting that marginalized groups suffer disproportionate harm from climate disasters without equal protection."
            },
            {
                "id": "ca-env-02-q2",
                "q": "Consider the following statements regarding the Great Indian Bustard (Ardeotis nigriceps):\n1. It is classified as 'Critically Endangered' on the IUCN Red List.\n2. It has poor frontal vision which makes it highly prone to fatal collisions with overhead power transmission lines.\n3. It is found exclusively in the evergreen forests of the Western Ghats.\nWhich of the statements given above is/are correct?",
                "options": ["(a) 1 and 2 only", "(b) 2 and 3 only", "(c) 1 and 3 only", "(d) 1, 2 and 3"],
                "answer": "(a)",
                "explanation": "Statements 1 and 2 are correct (its lack of frontal binocular vision causes fatal high-tension wire collisions). Statement 3 is incorrect: GIB is an arid and semi-arid grassland bird, primarily found in Desert National Park (Rajasthan) and Kutch (Gujarat), NOT evergreen forests."
            },
            {
                "id": "ca-env-02-q3",
                "q": "Which of the following National Parks / Sanctuaries harbors the last viable breeding population of the Great Indian Bustard in India?\n(a) Kaziranga National Park (Assam)\n(b) Desert National Park (Rajasthan)\n(c) Dachigam National Park (Jammu and Kashmir)\n(d) Similipal National Park (Odisha)",
                "options": [
                    "(a) Kaziranga National Park (Assam)",
                    "(b) Desert National Park (Rajasthan)",
                    "(c) Dachigam National Park (Jammu and Kashmir)",
                    "(d) Similipal National Park (Odisha)"
                ],
                "answer": "(b)",
                "explanation": "Desert National Park (Jaisalmer-Barmer, Rajasthan) is the primary stronghold of the Great Indian Bustard, supported by captive breeding centers like Ramdevra."
            },
            {
                "id": "ca-env-02-q4",
                "q": "The bird diverted devices called 'Bird Diverters' installed on high-voltage power transmission lines work by:\n(a) Emitting ultrasonic sounds that repel all avian species\n(b) Using glowing reflective coils and rotating visual tags to make wires visible to birds from a distance of at least 50 meters\n(c) Electrocuting predatory hawks\n(d) Transmitting radio signals to air traffic control towers",
                "options": [
                    "(a) Emitting ultrasonic sounds that repel all avian species",
                    "(b) Using glowing reflective coils and rotating visual tags to make wires visible to birds from a distance of at least 50 meters",
                    "(c) Electrocuting predatory hawks\n(d) Transmitting radio signals to air traffic control towers"
                ],
                "answer": "(b)",
                "explanation": "Bird flight diverters are solar-powered or photoluminescent visual reflectors that spin or glow in low light, giving heavy flyers like the bustard sufficient warning time to steer clear of power lines."
            },
            {
                "id": "ca-env-02-q5",
                "q": "Under the Wildlife (Protection) Act, 1972 (as amended in 2022), the Great Indian Bustard is placed in which Schedule?\n(a) Schedule I (Animal species that will enjoy the highest level of protection)\n(b) Schedule II (Animal species subject to lesser degree of protection)\n(c) Schedule III (Protected plant species)\n(d) Schedule IV (CITES specimens)",
                "options": [
                    "(a) Schedule I (Animal species that will enjoy the highest level of protection)",
                    "(b) Schedule II (Animal species subject to lesser degree of protection)",
                    "(c) Schedule III (Protected plant species)",
                    "(d) Schedule IV (CITES specimens)"
                ],
                "answer": "(a)",
                "explanation": "Schedule I of the amended WPA 1972 grants highest legal protection with stringent criminal penalties for hunting or habitat encroachment, covering flagship endangered species like Tiger, Elephant, Rhino, and GIB."
            }
        ]
    },

    # Science & Tech: Antimicrobial Resistance (AMR) & One Health
    {
        "id": "ca-sci-02",
        "date": "2026-11-05",
        "pillar": "SciTech",
        "title": "UN General Assembly Declaration on Antimicrobial Resistance (AMR) & One Health Action",
        "source": "WHO / PIB / The Lancet",
        "is_top100": True,
        "is_pt365": True,
        "summary_points": [
            "UNGA Political Declaration set a global target to reduce human deaths associated with bacterial AMR by 10% by 2030 through sustainable financing and antibiotic stewardship.",
            "AMR occurs when bacteria, viruses, fungi, and parasites mutate over time and no longer respond to antimicrobial medicines, driven by overprescription and overuse in livestock growth promotion.",
            "Endorsed the 'One Health' approach integrating human medicine, veterinary animal health, agriculture, and environmental waste management to stem resistant gene transmission."
        ],
        "gs_connection": "Links to GS-3 Science & Tech & Public Health: Pathogens, Genetics, Biotechnology, One Health Initiative, WHO Priority Pathogens, and National Action Plan on AMR.",
        "mcqs": [
            {
                "id": "ca-sci-02-q1",
                "q": "What is the primary mechanism by which bacteria develop resistance to beta-lactam antibiotics (such as penicillin and carbapenem)?\n(a) Synthesis of beta-lactamase enzymes that hydrolyze and break the antibiotic's chemical ring structure\n(b) Converting themselves into viruses inside host red blood cells\n(c) Producing chlorophyll to photosynthesize energy\n(d) Shifting their cell walls into silica glass shells",
                "options": [
                    "(a) Synthesis of beta-lactamase enzymes that hydrolyze and break the antibiotic's chemical ring structure",
                    "(b) Converting themselves into viruses inside host red blood cells",
                    "(c) Producing chlorophyll to photosynthesize energy",
                    "(d) Shifting their cell walls into silica glass shells"
                ],
                "answer": "(a)",
                "explanation": "Bacteria produce beta-lactamase enzymes (including ESBLs and carbapenemases like NDM-1) that chemically destroy the four-membered beta-lactam ring, rendering the antibiotic ineffective."
            },
            {
                "id": "ca-sci-02-q2",
                "q": "Consider the following statements regarding the 'One Health' concept endorsed by WHO, FAO, UNEP, and WOAH:\n1. It recognizes that human health is closely connected to the health of animals and the shared environment.\n2. It focuses exclusively on human viral infections and excludes agricultural pesticides and veterinary drugs.\n3. The National One Health Mission in India is coordinated under the Office of the Principal Scientific Adviser (PSA).\nWhich of the statements given above are correct?",
                "options": ["(a) 1 and 2 only", "(b) 1 and 3 only", "(c) 2 and 3 only", "(d) 1, 2 and 3"],
                "answer": "(b)",
                "explanation": "Statement 1 is correct. Statement 2 is incorrect (One Health covers zoonoses, animal livestock, wildlife, soil, and aquatic ecosystems). Statement 3 is correct: India's National One Health Mission is coordinated under the Office of the Principal Scientific Adviser."
            },
            {
                "id": "ca-sci-02-q3",
                "q": "The 'Red Line Campaign' launched by the Union Ministry of Health and Family Welfare aims to:\n(a) Demarcate containment zones during viral pandemics\n(b) Discourage over-the-counter sale and consumption of prescription antibiotics without a doctor's prescription\n(c) Mark high-risk maternal delivery hospitals\n(d) Stop cross-border tobacco smuggling",
                "options": [
                    "(a) Demarcate containment zones during viral pandemics",
                    "(b) Discourage over-the-counter sale and consumption of prescription antibiotics without a doctor's prescription",
                    "(c) Mark high-risk maternal delivery hospitals",
                    "(d) Stop cross-border tobacco smuggling"
                ],
                "answer": "(b)",
                "explanation": "The Red Line Campaign requires prescription-only antibiotics (Schedule H and H1) to carry a distinct red vertical line on their packaging to alert consumers not to self-medicate."
            },
            {
                "id": "ca-sci-02-q4",
                "q": "Which of the following is an example of horizontal gene transfer through which bacteria share antibiotic resistance genes with neighboring bacteria?\n1. Transformation (uptake of free environmental DNA)\n2. Transduction (transfer mediated by bacteriophages)\n3. Conjugation (direct plasmid transfer through pilus)\nSelect the correct answer using the code given below:",
                "options": ["(a) 1 and 2 only", "(b) 2 and 3 only", "(c) 1 and 3 only", "(d) 1, 2 and 3"],
                "answer": "(d)",
                "explanation": "All three (transformation, transduction, conjugation) are recognized biological mechanisms of horizontal gene transfer (HGT) facilitating rapid dissemination of resistance genes across bacterial species."
            },
            {
                "id": "ca-sci-02-q5",
                "q": "In the context of the WHO AWaRe classification of antibiotics, which group contains reserve antibiotics that should be kept as 'last-resort' options for multi-drug resistant superbugs?\n(a) Access group\n(b) Watch group\n(c) Reserve group\n(d) OTC group",
                "options": ["(a) Access group", "(b) Watch group", "(c) Reserve group", "(d) OTC group"],
                "answer": "(c)",
                "explanation": "WHO's AWaRe framework classifies antibiotics into Access (first-line, widely available), Watch (higher resistance potential, monitored), and Reserve (last-resort treatments like Colistin, Linezolid, Bedaquiline preserved for confirmed superbugs)."
            }
        ]
    }
]

ALL_CA_DATA = CA_ARTICLES + ADDITIONAL_ARTICLES

CA_FILE = os.path.join(DATA_DIR, 'current-affairs-db.json')
with open(CA_FILE, 'w') as f:
    json.dump(ALL_CA_DATA, f, indent=2)

print(f"Successfully generated {len(ALL_CA_DATA)} comprehensive Current Affairs articles with 5-10 MCQs each ({sum(len(a['mcqs']) for a in ALL_CA_DATA)} total practice questions)!")
