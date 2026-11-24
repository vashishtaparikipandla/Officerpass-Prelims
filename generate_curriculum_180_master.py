import json
import datetime
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, 'data')
start_date = datetime.date(2026, 11, 24)

# Load existing microtopics for sub-items and sources
with open(os.path.join(BASE_DIR, 'micro-topics', 'microtopics-db.json'), 'r') as f:
    micro_db = json.load(f)

# Load CA DB
with open(os.path.join(BASE_DIR, 'data', 'current-affairs-db.json'), 'r') as f:
    ca_db = json.load(f)

# Load sample polity 50q
with open(os.path.join(BASE_DIR, 'practice-tests', 'micro-topics', 'polity-parliament-50q.json'), 'r') as f:
    polity_50q = json.load(f)

# Pool CA MCQs by pillar
ca_mcqs_by_pillar = {
    'Polity': [], 'Economy': [], 'Environment': [], 'SciTech': [], 'Geography': [], 'History': [], 'IR': []
}
for art in ca_db:
    pil = art.get('pillar', 'Polity')
    if pil in ca_mcqs_by_pillar:
        for m in art.get('mcqs', []):
            ca_mcqs_by_pillar[pil].append({
                'topic': f"{pil} Current Affairs",
                'type': 'statement',
                'q': m.get('q', ''),
                'options': m.get('options', []),
                'answer': m.get('answer', '(a)'),
                'explanation': m.get('explanation', '')
            })

# Comprehensive Static Question Bank Generator
static_questions_by_subject = {
    "Polity": list(polity_50q),
    "Economy": [],
    "Geography": [],
    "Environment": [],
    "History": [],
    "SciTech": [],
    "CSAT": []
}

# Add substantial static questions for Economy
economy_static_raw = [
    {
        "topic": "National Income Accounting",
        "type": "statement",
        "q": "With reference to Gross Value Added (GVA) and Gross Domestic Product (GDP) in India, consider the following statements:\n1. GVA at basic prices includes production taxes and excludes production subsidies.\n2. GDP at market prices is derived by adding product taxes and subtracting product subsidies from GVA at basic prices.\n3. The headline GDP growth reported in India is based on Real GDP at factor cost.",
        "options": ["(a) 1 and 2 only", "(b) 2 and 3 only", "(c) 1 and 3 only", "(d) 1, 2 and 3"],
        "answer": "(a)",
        "explanation": "Statement 3 is incorrect: Since the 2015 revision (base year 2011-12), headline GDP in India is measured at Constant Market Prices (Real GDP at market prices), not factor cost. Statements 1 and 2 correctly state the CSO/NSO national accounting formulas."
    },
    {
        "topic": "Monetary Policy & Inflation",
        "type": "statement",
        "q": "Consider the following statements regarding the Monetary Policy Committee (MPC) of India:\n1. The MPC consists of six members, with three nominated by the Central Government and three from the Reserve Bank of India.\n2. The Governor of the RBI acts as the ex-officio Chairperson of the MPC and has a casting vote in the event of a tie.\n3. The inflation target mandated under the RBI Act 1934 is determined by the RBI Governor alone every five years.",
        "options": ["(a) 1 and 2 only", "(b) 2 and 3 only", "(c) 1 and 3 only", "(d) 1, 2 and 3"],
        "answer": "(a)",
        "explanation": "Statement 3 is incorrect: Under Section 45ZA of the RBI Act 1934, the inflation target (4% +/- 2%) is determined by the Central Government in consultation with the RBI, once every five years, not by the Governor alone. Statements 1 and 2 are direct provisions of Section 45ZB."
    },
    {
        "topic": "Standing Deposit Facility (SDF)",
        "type": "statement",
        "q": "With reference to the Standing Deposit Facility (SDF) introduced by the Reserve Bank of India, consider the following statements:\n1. It allows the RBI to absorb liquidity from commercial banks without providing government securities as collateral.\n2. It replaced the fixed rate reverse repo as the floor of the Liquidity Adjustment Facility (LAF) corridor.\n3. It is accessible only to Scheduled Commercial Banks and excludes Regional Rural Banks.",
        "options": ["(a) 1 and 2 only", "(b) 2 and 3 only", "(c) 1 only", "(d) 1, 2 and 3"],
        "answer": "(a)",
        "explanation": "Statement 3 is incorrect: Eligible participants include all LAF participants including Regional Rural Banks, Small Finance Banks, and Primary Dealers. Statements 1 and 2 are correct: SDF was empowered by amendment to Section 17 of RBI Act to absorb collateral-free liquidity at 25 bps below the policy repo rate."
    },
    {
        "topic": "Insolvency and Bankruptcy Code (IBC)",
        "type": "statement",
        "q": "Consider the following statements regarding the Corporate Insolvency Resolution Process (CIRP) under the IBC 2016:\n1. The resolution process can be triggered by financial creditors, operational creditors, or the corporate debtor itself.\n2. The Committee of Creditors (CoC) consists only of operational creditors.\n3. The approval of a resolution plan requires a minimum voting share of 66% of financial creditors.",
        "options": ["(a) 1 and 3 only", "(b) 1 and 2 only", "(c) 3 only", "(d) 1, 2 and 3"],
        "answer": "(a)",
        "explanation": "Statement 2 is incorrect: The Committee of Creditors (CoC) consists solely of Financial Creditors (unless there are no financial creditors, in which case operational creditors form the committee). Operational creditors attend without voting rights. Statement 3 was amended from 75% to 66% to facilitate faster resolution."
    },
    {
        "topic": "Balance of Payments & Forex",
        "type": "statement",
        "q": "Which of the following items are included under the Capital Account of India's Balance of Payments?\n1. Foreign Direct Investment (FDI)\n2. External Commercial Borrowings (ECBs)\n3. Remittances by overseas Indians\n4. Special Drawing Rights (SDR) allocations by the IMF",
        "options": ["(a) 1, 2 and 4 only", "(b) 1 and 2 only", "(c) 2 and 3 only", "(d) 1, 2, 3 and 4"],
        "answer": "(a)",
        "explanation": "Item 3 (Remittances) is an unrequited transfer included under the Current Account (Invisibles), not the Capital Account. FDI, ECBs, FPI, and SDR allocations create external assets or liabilities and belong strictly to the Capital Account."
    },
    {
        "topic": "Agricultural MSP & WTO Boxes",
        "type": "statement",
        "q": "With reference to the World Trade Organization (WTO) Agreement on Agriculture (AoA), consider the following statements:\n1. Green Box subsidies are considered non-trade distorting and can be provided without any financial limits.\n2. Blue Box subsidies refer to direct payments under production-limiting programs and are exempt from reduction commitments.\n3. India's Minimum Support Price (MSP) public stockholding for food security falls under the Green Box.",
        "options": ["(a) 1 and 2 only", "(b) 2 and 3 only", "(c) 1 only", "(d) 1, 2 and 3"],
        "answer": "(a)",
        "explanation": "Statement 3 is incorrect: Under WTO AoA, government price support/MSP procurement is classified as trade-distorting Amber Box domestic support (measured as Aggregate Measurement of Support - AMS). India protects its MSP buffer procurement using the Bali Peace Clause, because it is an Amber Box measure exceeding the 10% de minimis limit based on 1986-88 external reference prices."
    },
    {
        "topic": "Central Bank Digital Currency (CBDC)",
        "type": "statement",
        "q": "Consider the following statements regarding the Central Bank Digital Currency (e-Rupee) in India:\n1. It is a sovereign digital currency appearing as a liability on the RBI's balance sheet.\n2. Unlike banknotes, e-Rupee cannot be held anonymously in offline digital wallets.\n3. It is interest-bearing to encourage retail adoption over commercial bank deposits.",
        "options": ["(a) 1 only", "(b) 1 and 2 only", "(c) 2 and 3 only", "(d) 1, 2 and 3"],
        "answer": "(a)",
        "explanation": "Statements 2 and 3 are incorrect: e-Rupee does NOT earn any interest, specifically to prevent disintermediation of commercial banks (people moving money from bank deposits into risk-free CBDC). It is designed to offer features similar to physical cash, including anonymous small-value transactions."
    },
    {
        "topic": "Fiscal Deficit & FRBM",
        "type": "statement",
        "q": "If the Primary Deficit of the Union Government in a fiscal year is zero, which of the following is definitely true?\n1. Revenue deficit must also be zero.\n2. Fiscal deficit is exactly equal to the government's net interest payment obligations on past debt.\n3. The government has no need to borrow from the market in that year.",
        "options": ["(a) 2 only", "(b) 1 and 2 only", "(c) 2 and 3 only", "(d) 1, 2 and 3"],
        "answer": "(a)",
        "explanation": "Primary Deficit = Fiscal Deficit - Interest Payments. If Primary Deficit = 0, then Fiscal Deficit = Interest Payments. This means the entire fresh borrowing of the government during that year is consumed purely in paying interest on accumulated past debt. Statement 3 is false because the government still borrows to pay that interest."
    }
]
static_questions_by_subject["Economy"].extend(economy_static_raw)

# Add substantial static questions for Geography
geography_static_raw = [
    {
        "topic": "Geomorphology & Earth's Interior",
        "type": "statement",
        "q": "Consider the following statements regarding earthquake waves:\n1. P-waves are compressional waves and can travel through solids, liquids, and gases.\n2. S-waves are transverse shear waves and cannot pass through the liquid outer core of the Earth.\n3. The shadow zone of S-waves is smaller than the shadow zone of P-waves.",
        "options": ["(a) 1 and 2 only", "(b) 2 and 3 only", "(c) 1 only", "(d) 1, 2 and 3"],
        "answer": "(a)",
        "explanation": "Statement 3 is incorrect: The shadow zone of S-waves is significantly LARGER than that of P-waves. S-waves are completely blocked beyond 105 degrees from the epicenter (spanning over 40% of the Earth's surface), whereas P-waves have a ring-shaped shadow zone between 105 and 145 degrees."
    },
    {
        "topic": "Indian Monsoon & Jet Streams",
        "type": "statement",
        "q": "Which of the following factors contribute to the onset and intensity of the Southwest Monsoon in India?\n1. Intense heating of the Tibetan Plateau during summer\n2. Shift of the Inter-Tropical Convergence Zone (ITCZ) northward over the Ganga plain\n3. Presence of the Tropical Easterly Jet (TEJ) over the Indian Peninsula\n4. Development of a strong high-pressure cell over Madagascar (Mascarene High)",
        "options": ["(a) 1, 2, 3 and 4", "(b) 1 and 2 only", "(c) 2, 3 and 4 only", "(d) 1, 3 and 4 only"],
        "answer": "(a)",
        "explanation": "All four are key meteorological drivers: Tibetan heating creates vertical convection and the TEJ; ITCZ northward migration draws maritime equatorial air; Mascarene High acts as the Southern Hemisphere pressure engine pumping moisture-laden winds across the equator into the Arabian Sea branch."
    },
    {
        "topic": "Indian Drainage Systems",
        "type": "statement",
        "q": "Consider the following Himalayan and Peninsular rivers:\n1. Narmada\n2. Tapti\n3. Mahanadi\n4. Damodar\nWhich of the above flow through rift valleys created by tectonic faulting?",
        "options": ["(a) 1, 2 and 4 only", "(b) 1 and 2 only", "(c) 3 and 4 only", "(d) 1, 2, 3 and 4"],
        "answer": "(a)",
        "explanation": "Narmada, Tapti, and Damodar all flow through fault-trough rift valleys. Damodar flows through a rift valley on the Chotanagpur Plateau. Mahanadi flows through an ordinary broad valley and forms a prominent delta on the Odisha coast."
    },
    {
        "topic": "Oceanography: Currents & Deserts",
        "type": "statement",
        "q": "Why are the major hot deserts of the world (like Atacama, Namib, and Sahara) located on the western margins of continents in the subtropics?\n1. Presence of offshore Trade Winds that blow moisture away from the western coast.\n2. Influence of cold ocean currents along the western coasts, which create atmospheric stability and inhibit precipitation.\n3. Location in the subtropical high-pressure belts where air descends and warms adiabatically.",
        "options": ["(a) 1, 2 and 3", "(b) 1 and 2 only", "(c) 2 and 3 only", "(d) 1 and 3 only"],
        "answer": "(a)",
        "explanation": "All three factors combine: Trade winds blow from East to West (offshore on western coasts); Subtropical highs cause descending, desiccating air; Cold currents (Peru, Benguela, Canaries) prevent convective cloud formation by chilling the lower air layer."
    },
    {
        "topic": "Indian Soils: Black Soil",
        "type": "statement",
        "q": "With reference to Black Cotton Soil (Regur) in India, consider the following statements:\n1. It is derived from the weathering of basaltic lava of the Deccan Traps.\n2. It has high moisture-retentive capacity and develops deep wide cracks during dry periods.\n3. It is rich in nitrogen, phosphorus, and organic matter.",
        "options": ["(a) 1 and 2 only", "(b) 2 and 3 only", "(c) 1 and 3 only", "(d) 1, 2 and 3"],
        "answer": "(a)",
        "explanation": "Statement 3 is incorrect: Like most Indian soils, Black soil is severely DEFICIENT in nitrogen, phosphorus, and organic matter (humus). However, it is rich in lime, iron, magnesia, and alumina, and retains moisture exceptionally well due to montmorillonite clay content."
    }
]
static_questions_by_subject["Geography"].extend(geography_static_raw)

# Add substantial static questions for Environment
environment_static_raw = [
    {
        "topic": "Ecosystem Energy & Biomass",
        "type": "statement",
        "q": "Consider the following statements regarding ecological pyramids in an ecosystem:\n1. The pyramid of energy is always upright and can never be inverted in any natural ecosystem.\n2. The pyramid of biomass in an aquatic ecosystem (like a deep lake or sea) is often inverted.\n3. The pyramid of numbers in a parasitic food chain can be inverted.",
        "options": ["(a) 1, 2 and 3", "(b) 1 and 2 only", "(c) 2 and 3 only", "(d) 1 and 3 only"],
        "answer": "(a)",
        "explanation": "All three are correct ecological principles. Energy is lost at each trophic step (10% law), so energy pyramid is strictly upright. In marine ecosystems, phytoplankton have very small biomass at any single moment but high turnover, supporting a larger biomass of zooplankton and fish (inverted biomass pyramid). A single tree supporting thousands of parasites creates an inverted numbers pyramid."
    },
    {
        "topic": "Wildlife Protection Act 1972",
        "type": "statement",
        "q": "With reference to the Wildlife (Protection) Amendment Act 2022, consider the following statements:\n1. The number of schedules was reduced from six to four.\n2. Schedule I provides the highest level of protection for animal species.\n3. Schedule IV is dedicated to specimens of flora and fauna listed under CITES Appendices.\n4. Vermin species are now permanently listed under a separate dedicated Schedule V.",
        "options": ["(a) 1, 2 and 3 only", "(b) 1 and 2 only", "(c) 2, 3 and 4 only", "(d) 1, 2, 3 and 4"],
        "answer": "(a)",
        "explanation": "Statement 4 is incorrect: The 2022 Amendment completely ABOLISHED Schedule V (Vermin). The Central Government can now declare any animal as vermin for a specified period and area by official notification, rather than maintaining a permanent statutory vermin schedule."
    },
    {
        "topic": "National Parks vs Wildlife Sanctuaries",
        "type": "statement",
        "q": "Consider the following statements regarding protected areas in India:\n1. Boundaries of a National Park can only be altered by a resolution passed by the State Legislature on the recommendation of the National Board for Wildlife (NBWL).\n2. Grazing of livestock is strictly prohibited inside a National Park, but may be permitted under regulated conditions in a Wildlife Sanctuary.\n3. A Wildlife Sanctuary can be created for the protection of a particular single species, whereas a National Park has no such single-species focus.",
        "options": ["(a) 1, 2 and 3", "(b) 1 and 2 only", "(c) 2 and 3 only", "(d) 1 and 3 only"],
        "answer": "(a)",
        "explanation": "All three statements are correct under the Wildlife Protection Act 1972. Section 35 governs National Parks (no livestock grazing, boundary change requires NBWL approval), while Section 18-26 governs Sanctuaries (Chief Wildlife Warden may permit regulated grazing and activities)."
    },
    {
        "topic": "International Climate Conventions",
        "type": "statement",
        "q": "Consider the following international environmental agreements:\n1. Cartagena Protocol — Biosafety and Living Modified Organisms\n2. Nagoya Protocol — Access and Benefit Sharing of Genetic Resources\n3. Basel Convention — Transboundary Movement of Hazardous Wastes\n4. Rotterdam Convention — Prior Informed Consent Procedure for Certain Hazardous Chemicals\nWhich of the above pairs are correctly matched?",
        "options": ["(a) 1, 2, 3 and 4", "(b) 1 and 2 only", "(c) 2, 3 and 4 only", "(d) 1, 3 and 4 only"],
        "answer": "(a)",
        "explanation": "All four pairings are correctly matched. Cartagena and Nagoya are protocols under the Convention on Biological Diversity (CBD). Basel controls hazardous waste disposal. Rotterdam ensures prior informed consent for banned/restricted toxic chemicals."
    },
    {
        "topic": "Air Quality Index & NAAQS",
        "type": "statement",
        "q": "Which of the following atmospheric pollutants are monitored under the National Air Quality Index (AQI) in India?\n1. PM2.5 and PM10\n2. Carbon Monoxide (CO)\n3. Carbon Dioxide (CO2)\n4. Ammonia (NH3)\n5. Lead (Pb)",
        "options": ["(a) 1, 2, 4 and 5 only", "(b) 1, 2 and 3 only", "(c) 1, 2, 3, 4 and 5", "(d) 2, 4 and 5 only"],
        "answer": "(a)",
        "explanation": "Carbon Dioxide (CO2) is NOT one of the 8 pollutants under the National Air Quality Index. The 8 AQI pollutants are: PM10, PM2.5, NO2, SO2, CO, O3 (Ozone), NH3 (Ammonia), and Pb (Lead)."
    }
]
static_questions_by_subject["Environment"].extend(environment_static_raw)

# Add substantial static questions for History
history_static_raw = [
    {
        "topic": "Indus Valley Civilization",
        "type": "statement",
        "q": "Which of the following Harappan sites is uniquely divided into three distinct parts (Citadel, Middle Town, and Lower Town) and possesses a massive stone-cut water reservoir system?",
        "options": ["(a) Dholavira", "(b) Lothal", "(c) Rakhigarhi", "(d) Kalibangan"],
        "answer": "(a)",
        "explanation": "Dholavira in the Rann of Kutch (Gujarat) is the only Harappan city divided into three parts fortified by stone walls. It is celebrated for its sophisticated water harvesting and interconnected rock-cut reservoirs, earning UNESCO World Heritage status in 2021."
    },
    {
        "topic": "Buddhism & Jainism",
        "type": "statement",
        "q": "With reference to the religious history of ancient India, consider the following statements:\n1. Anekantavada and Syadvada are core philosophical doctrines of Jainism.\n2. The concept of Pratityasamutpada (Dependent Origination) forms the foundational teaching of Buddhism.\n3. Hinayana Buddhism worships the images of Bodhisattvas, whereas Mahayana Buddhism completely prohibits image worship.",
        "options": ["(a) 1 and 2 only", "(b) 2 and 3 only", "(c) 1 only", "(d) 1, 2 and 3"],
        "answer": "(a)",
        "explanation": "Statement 3 is reversed: It was MAHAYANA Buddhism that introduced image worship of Buddha and Bodhisattvas (like Avalokiteshvara). Hinayana (Theravada) originally represented Buddha only through symbols (Footprints, Stupa, Wheel, Tree) and focused on individual monastic salvation."
    },
    {
        "topic": "Temple Architecture",
        "type": "statement",
        "q": "Consider the following features of Indian temple architecture:\n1. Presence of a towering entrance gateway called Gopuram\n2. Enclosed boundary walls around the temple complex\n3. Presence of a large temple water reservoir (Kalyani / Tank) within the complex\nWhich of the above features are characteristic of the Dravida style of temple architecture?",
        "options": ["(a) 1, 2 and 3", "(b) 1 and 2 only", "(c) 2 and 3 only", "(d) 1 and 3 only"],
        "answer": "(a)",
        "explanation": "All three features are hallmarks of Dravidian temple architecture (South India) as exemplified by the Brihadisvara Temple at Thanjavur. Nagara style temples (North India) typically lack boundary walls, gopurams, and internal temple water tanks."
    },
    {
        "topic": "British Land Revenue Settlements",
        "type": "statement",
        "q": "With reference to the British land revenue systems in India, consider the following statements:\n1. Under the Permanent Settlement introduced by Cornwallis in Bengal, the Zamindars were recognized as owners of the land subject to the Sunset Law.\n2. The Ryotwari system was introduced primarily in Madras and Bombay Presidencies by Thomas Munro and Alexander Read.\n3. In the Mahalwari system, the settlement was made directly with individual cultivators without involving the village community.",
        "options": ["(a) 1 and 2 only", "(b) 2 and 3 only", "(c) 1 and 3 only", "(d) 1, 2 and 3"],
        "answer": "(a)",
        "explanation": "Statement 3 is incorrect: Under the Mahalwari system (introduced by Holt Mackenzie in NW Provinces/Punjab), the settlement was made with the entire village community (Mahal) or its headman (Lambardar) who was collectively responsible for collecting revenue, not with individual peasants directly."
    },
    {
        "topic": "Freedom Struggle: Gandhian Sessions",
        "type": "statement",
        "q": "The historic Karachi Session of the Indian National Congress (1931), presided over by Sardar Vallabhbhai Patel, is memorable for which of the following reasons?\n1. Adoption of the Resolution on Fundamental Rights\n2. Adoption of the National Economic Programme\n3. Endorsement of the Gandhi-Irwin Pact",
        "options": ["(a) 1, 2 and 3", "(b) 1 and 2 only", "(c) 2 and 3 only", "(d) 1 and 3 only"],
        "answer": "(a)",
        "explanation": "All three are historic achievements of the Karachi Session (March 1931). Drafted by Jawaharlal Nehru, the resolutions on Fundamental Rights and the National Economic Programme committed the national movement to agrarian reform, labour rights, and state control of key industries."
    }
]
static_questions_by_subject["History"].extend(history_static_raw)

# Add substantial static questions for ScienceTech
scitech_static_raw = [
    {
        "topic": "Space Tech: Orbits & Launchers",
        "type": "statement",
        "q": "Consider the following statements regarding satellite orbits:\n1. A Geostationary orbit lies in the equatorial plane at an altitude of approximately 35,786 km.\n2. A satellite in Sun-Synchronous Orbit (SSO) passes over any given point of the Earth's surface at the same local mean solar time.\n3. Polar satellites are primarily used for continuous telecommunications, while Geostationary satellites are used for earth observation and cartography.",
        "options": ["(a) 1 and 2 only", "(b) 2 and 3 only", "(c) 1 only", "(d) 1, 2 and 3"],
        "answer": "(a)",
        "explanation": "Statement 3 is reversed: Polar Sun-Synchronous satellites are used for Earth observation, remote sensing, agriculture, and cartography (because they fly low and scan the globe under uniform sunlight). Geostationary satellites are stationary over one spot and are used for 24/7 telecommunications, DTH television, and meteorological observation."
    },
    {
        "topic": "Biotechnology: CRISPR-Cas9",
        "type": "statement",
        "q": "With reference to CRISPR-Cas9 gene editing technology, consider the following statements:\n1. Cas9 is a bacterial endonuclease enzyme that functions as molecular scissors to cut double-stranded DNA.\n2. A synthetic guide RNA (gRNA) directs the Cas9 enzyme to the precise location in the genome to be edited.\n3. The CRISPR mechanism was originally discovered as an adaptive immune defense system in bacteria against invading viruses.",
        "options": ["(a) 1, 2 and 3", "(b) 1 and 2 only", "(c) 2 and 3 only", "(d) 1 and 3 only"],
        "answer": "(a)",
        "explanation": "All three statements correctly describe CRISPR-Cas9 technology, which earned Emmanuelle Charpentier and Jennifer Doudna the 2020 Nobel Prize in Chemistry. Bacteria use CRISPR sequences to remember and destroy bacteriophage viruses; scientists engineered the system to edit eukaryotic DNA with surgical precision."
    },
    {
        "topic": "Vaccine Technology Platforms",
        "type": "statement",
        "q": "Which of the following pairs of COVID-19 vaccines and their respective platform technologies are correctly matched?\n1. Covishield — Viral Vector vaccine using chimpanzee adenovirus\n2. Covaxin — Inactivated whole-virion vaccine\n3. ZyCoV-D — Plasmid DNA vaccine\n4. Pfizer-BioNTech — mRNA vaccine encapsulated in lipid nanoparticles",
        "options": ["(a) 1, 2, 3 and 4", "(b) 1 and 2 only", "(c) 2 and 4 only", "(d) 1, 3 and 4 only"],
        "answer": "(a)",
        "explanation": "All four vaccine platforms are correctly matched. Covishield uses Oxford/AstraZeneca's non-replicating chimpanzee adenovirus vector (ChAdOx1); Bharat Biotech's Covaxin uses an inactivated whole virus with Algel-IMDG adjuvant; ZyCoV-D is the world's first needle-free plasmid DNA vaccine; Pfizer and Moderna use nucleoside-modified mRNA."
    }
]
static_questions_by_subject["SciTech"].extend(scitech_static_raw)

# Add substantial static questions for CSAT
csat_static_raw = [
    {
        "topic": "CSAT Number System: Cyclicity",
        "type": "problem",
        "q": "What is the unit digit of the expression (3^65 x 6^59 x 7^71)?",
        "options": ["(a) 4", "(b) 2", "(c) 6", "(d) 8"],
        "answer": "(a)",
        "explanation": "Step 1: Cyclicity of 3 is 4. 65 / 4 gives remainder 1 -> Unit digit = 3^1 = 3.\nStep 2: Any power of 6 always ends in 6 -> Unit digit = 6.\nStep 3: Cyclicity of 7 is 4. 71 / 4 gives remainder 3 -> Unit digit = 7^3 = 343 -> 3.\nMultiply unit digits: 3 x 6 x 3 = 54 -> Unit digit is 4."
    },
    {
        "topic": "CSAT Number System: Remainder",
        "type": "problem",
        "q": "A number when divided successively by 4 and 5 leaves remainders 1 and 4 respectively. When it is successively divided by 5 and 4, the respective remainders will be:",
        "options": ["(a) 4, 1", "(b) 3, 2", "(c) 2, 3", "(d) 1, 2"],
        "answer": "(c)",
        "explanation": "Let the final quotient be 1.\nSecond dividend = (5 x 1) + 4 = 9.\nFirst number = (4 x 9) + 1 = 37.\nNow divide 37 successively by 5 and 4:\n37 / 5 = Quotient 7, Remainder 2.\n7 / 4 = Quotient 1, Remainder 3.\nRespective remainders are 2 and 3."
    },
    {
        "topic": "CSAT Quantitative: Time & Work (LCM Units)",
        "type": "problem",
        "q": "A can complete a piece of work in 12 days and B can complete the same work in 18 days. If they work together on alternate days starting with A, in how many days will the work be completed?",
        "options": ["(a) 14 1/3 days", "(b) 14 1/2 days", "(c) 15 days", "(d) 14 2/3 days"],
        "answer": "(a)",
        "explanation": "Total Work = LCM(12, 18) = 36 units.\nA's 1-day work = 36/12 = 3 units.\nB's 1-day work = 36/18 = 2 units.\nIn a 2-day cycle (A + B), work done = 3 + 2 = 5 units.\n7 such 2-day cycles (14 days) complete: 7 x 5 = 35 units.\nRemaining work = 36 - 35 = 1 unit.\nOn day 15, it is A's turn (efficiency = 3 units/day).\nTime taken by A = 1/3 day.\nTotal days = 14 + 1/3 = 14 1/3 days."
    },
    {
        "topic": "CSAT Quantitative: Speed & Trains",
        "type": "problem",
        "q": "A train running at 54 km/h takes 20 seconds to completely cross a platform 180 metres long. What is the length of the train?",
        "options": ["(a) 120 metres", "(b) 150 metres", "(c) 100 metres", "(d) 140 metres"],
        "answer": "(a)",
        "explanation": "Speed in m/s = 54 x (5/18) = 15 m/s.\nTotal distance crossed = Speed x Time = 15 x 20 = 300 metres.\nDistance = Length of Train + Length of Platform.\n300 = Length of Train + 180\nLength of Train = 300 - 180 = 120 metres."
    },
    {
        "topic": "CSAT Reading Comprehension: Sherlocking",
        "type": "rc",
        "q": "Passage: 'Technological innovations inevitably disrupt existing employment structures. However, viewing artificial intelligence purely as an agent of job destruction misapprehends economic history. Historically, mechanization displaced physical labour while generating unforeseen cognitive and service industries. The challenge today is not technology itself, but the widening latency between job destruction and human skilling.'\nWhich of the following reflects the most logical and critical assumption made by the author?",
        "options": [
            "(a) Proactive and rapid workforce reskilling can effectively mitigate technology-induced employment shocks.",
            "(b) Artificial intelligence will create more jobs than any other previous industrial revolution.",
            "(c) Governments should ban automation in high-employment sectors to preserve traditional jobs.",
            "(d) Human intelligence will permanently remain superior to machine learning in the service sector."
        ],
        "answer": "(a)",
        "explanation": "Option (a) directly captures the author's stated problem: 'the widening latency between job destruction and human skilling.' The author assumes that closing this latency through reskilling resolves the challenge. Options (b), (c), and (d) introduce extreme or unsupported claims ('ban automation', 'permanently superior', 'more jobs than any other revolution')."
    }
]
static_questions_by_subject["CSAT"].extend(csat_static_raw)

print(f"Static questions ready: { {k: len(v) for k, v in static_questions_by_subject.items()} }")

from build_full_curriculum_180 import plan_specs

# Full 180-Day Curriculum Metadata Generator
days_curriculum = []

for day in range(1, 181):
    curr_date = start_date + datetime.timedelta(days=day - 1)
    date_iso = curr_date.strftime("%Y-%m-%d")
    date_display = curr_date.strftime("%A, %d %B %Y")
    
    # Calculate Phase & Week
    week = ((day - 1) // 7) + 1
    is_mock = (day % 7 == 0)
    
    if day <= 105:
        phase = 1
        phase_name = "Phase 1: Foundational Concept Building (Weeks 1–15)"
    elif day <= 140:
        phase = 2
        phase_name = "Phase 2: Consolidated 1st Revision & PT 365 (Weeks 16–20)"
    else:
        phase = 3
        phase_name = "Phase 3: High-Yield Sprint & Full-Length Simulation (Weeks 21–26)"
        
    # Check if we have pre-defined spec in plan_specs
    # If day in plan_specs, use it; else generate systematic progression
    matching_spec = next((s for s in plan_specs if s[0] == day), None)
    
    if matching_spec:
        _, subj, topic_title, source, topic_id, sub_items_raw, csat_topic, quote = matching_spec
        sub_items = [{"id": f"{topic_id}__d{day}_s{idx}", "text": text} for idx, text in enumerate(sub_items_raw)]
    else:
        # Generate systematic progression for Days 106-180
        if 106 <= day <= 112:
            subj = "Polity"
            topic_id = "pol-rev"
            source = "Laxmikanth & PT 365 Polity"
            if day == 112:
                topic_title = "Polity Consolidated Revision & Full Simulation Mock"
                sub_items_raw = [
                    "Full spectrum review of Articles 1 to 395 and Constitutional Amendments (42nd, 44th, 73rd, 91st, 103rd-106th)",
                    "Attempt 100-Question Polity Grand Simulation Test under timed morning conditions (06:00-08:00 AM)",
                    "Error Notebook audit: Resolve recurrent errors in Judicial Review and Emergency Provisions",
                    "PT 365 Polity: Key Supreme Court rulings on Governor, Anti-Defection & Electoral Bonds"
                ]
                csat_topic = "UNGIST Ch 1-5: Number System, Ratio & Averages Consolidated Mock Drill"
                quote = "A revision day is not an afterthought; it is where fragmented facts fuse into permanent executive intuition."
            else:
                day_offset = day - 105
                titles = [
                    "Polity Revision: Articles 1-51A, Fundamental Rights Landmark SC Judgments & Basic Structure",
                    "Polity Revision: Parliament & State Legislatures, Money Bills, Speaker Discretion & Anti-Defection",
                    "Polity Revision: Judiciary, Collegium Evolution, Contempt of Court & Special Leave Petitions",
                    "Polity Revision: Federalism, Inter-State Water Disputes, GST Council & 16th Finance Commission",
                    "Polity Revision: Local Governance (73rd/74th CA), PESA Act 1996 & 5th/6th Schedules Administration",
                    "Polity Revision: Constitutional & Statutory Bodies (ECI, CAG, FC, UPSC, NHRC, Lokpal) & RPA 1951"
                ]
                topic_title = titles[day_offset - 1]
                sub_items_raw = [
                    f"Rapid recall of key constitutional articles and doctrines for {topic_title.split(':')[1].strip()}",
                    "Solve 25 targeted PYQs and advanced MCQs with elimination reasoning",
                    "Map 2 years of current affairs and constitutional bench rulings to static provisions",
                    "Personal notes update: Add high-yield mnemonic triggers"
                ]
                csat_topic = f"UNGIST Chapter {day_offset}: Quant Speed Solving & Formula Refresh"
                quote = "Every Article you revise today strengthens your immunity against examiner traps in May."
        elif 113 <= day <= 119:
            subj = "Economy"
            topic_id = "eco-rev"
            source = "NCERT Macro, Economic Survey & Budget"
            if day == 119:
                topic_title = "Economy Consolidated Revision & Full Simulation Mock"
                sub_items_raw = [
                    "Complete synthesis of Macroeconomics, Monetary Transmission, Banking, Budget & Balance of Payments",
                    "Attempt 100-Question Economy Grand Simulation Test (06:00-08:00 AM)",
                    "Analyze trade-offs: Inflation targeting vs Growth, Fiscal Deficit vs Capex multiplier",
                    "PT 365 Economy: Financial sector regulations, SEBI updates & CBDC rollout"
                ]
                csat_topic = "UNGIST Ch 6-10: Percentages, Profit-Loss & Time-Distance Speed Drill"
                quote = "Economics in UPSC is about transmission mechanisms. Connect policy actions to their real-world echoes."
            else:
                day_offset = day - 112
                titles = [
                    "Economy Revision: National Income Accounting, GVA, Real vs Nominal GDP & Inflation Indices",
                    "Economy Revision: Monetary Policy Tools, Liquidity Management (SDF, MSF), Money Multiplier & RBI Balance Sheet",
                    "Economy Revision: Banking Sector Architecture, NPA Resolution, IBC 2016, Bad Bank & Prompt Corrective Action",
                    "Economy Revision: Fiscal Policy, Union Budget Classifications, FRBM Act Targets & Direct/Indirect Taxes",
                    "Economy Revision: External Sector, Balance of Payments, CAD Financing, Forex Reserves & REER/NEER",
                    "Economy Revision: Agriculture Sector, CACP Cost Concepts (A2+FL vs C2), WTO Boxes & Food Subsidy Bill"
                ]
                topic_title = titles[day_offset - 1]
                sub_items_raw = [
                    f"Consolidate core economic formulas and institutional frameworks for {topic_title.split(':')[1].strip()}",
                    "Solve 25 high-yield conceptual MCQs testing cause-and-effect relationships",
                    "Integrate latest Economic Survey figures and Union Budget allocations",
                    "Note down technical definitions and common distractor words"
                ]
                csat_topic = f"UNGIST Quant Topic {day_offset + 5}: Shortcuts and Unit Digit Checks"
                quote = "When interest rates change, everything moves. Keep your eye on the systemic domino effect."
        elif 120 <= day <= 126:
            subj = "Geography"
            topic_id = "geo-rev"
            source = "NCERT Class 11 & 12, PMFIAS & Atlas"
            if day == 126:
                topic_title = "Geography & Environment Combined Grand Mock Test"
                sub_items_raw = [
                    "Full-scale synthesis of Geomorphology, Climatology, Drainage, Protected Areas & Climate Treaties",
                    "Attempt 100-Question Geography & Environment Grand Simulation Test (06:00-08:00 AM)",
                    "Map-based verification: 20 international straits, conflict borders, and Indian river confluences",
                    "Verify IUCN red-list updates for flagship endangered species"
                ]
                csat_topic = "UNGIST Ch 11-15: Time-Work, P&C, Probability & Data Interpretation Speed Drill"
                quote = "Environment and Geography are spatial sciences. If you can see the map in your mind, the options fall into place."
            else:
                day_offset = day - 119
                titles = [
                    "Geography Revision: Climatology & Oceanography (Monsoon, Jet Streams, ENSO, IOD, Currents, Corals)",
                    "Geography Revision: Indian Drainage Systems (Indus, Ganga, Brahmaputra & Peninsular Rivers)",
                    "Geography Revision: World Mapping, Strategic Chokepoints, Enclosed Seas, Conflict Zones & Mineral Belts",
                    "Environment Revision: Protected Areas (National Parks, Biosphere Reserves, Tiger Reserves, Ramsar Sites)",
                    "Environment Revision: Environmental Laws (WPA 2022 Amendment, EPA 1986, FRA 2006, Biological Diversity Act)",
                    "Environment Revision: Climate Change Treaties (UNFCCC, Paris Agreement NDCs, Article 6, Kigali, CBD)"
                ]
                topic_title = titles[day_offset - 1]
                sub_items_raw = [
                    f"Rapid map and conceptual review for {topic_title.split(':')[1].strip()}",
                    "Practice sketching boundaries, river origins, and treaty chronologies",
                    "Solve 25 targeted Prelims questions emphasizing spatial relationships and exceptions",
                    "Review environmental bodies (NTCA, NBWL, CPCB, CAQM) statutory mandates"
                ]
                csat_topic = f"UNGIST Reasoning Chapter {day_offset}: Clocks, Calendar & Spatial Puzzles"
                quote = "A well-drawn mental map never lies. Trust the physical geography anchors."
        elif 127 <= day <= 133:
            subj = "History"
            topic_id = "his-rev"
            source = "Spectrum, NCERT & Nitin Singhania"
            if day == 133:
                topic_title = "History, Culture & SciTech Combined Grand Mock Test"
                sub_items_raw = [
                    "Chronological synthesis from Harappa through Guptas, Delhi Sultanate, Mughals & Freedom Struggle",
                    "Attempt 100-Question History, Culture & SciTech Grand Simulation Test (06:00-08:00 AM)",
                    "Review administrative terms, temple architectural styles, and ISRO/Biotech missions",
                    "Catalogue trick options in chronological and biographical questions"
                ]
                csat_topic = "UNGIST Logical Reasoning: Syllogisms, Venn Diagrams & Seating Marathon"
                quote = "History in Prelims is chronological logic and administrative vocabulary. Master the terms."
            else:
                day_offset = day - 126
                titles = [
                    "History Revision: Ancient India Chronology (IVC, Vedic, Buddhism, Jainism, Mauryas, Guptas)",
                    "History Revision: Medieval India (Delhi Sultanate, Vijayanagara Empire, Mughals, Bhakti & Sufi)",
                    "Art & Culture Revision: Temple Architecture (Nagara, Dravida, Vesara), Caves, Sculptures & UNESCO Sites",
                    "Modern History Revision: British Land Settlements, Economic Drain, 1857 Revolt & 19th Century Reformers",
                    "Modern History Revision: Freedom Struggle (Swadeshi, Non-Cooperation, Civil Disobedience, Quit India, Acts)",
                    "Science & Tech Revision: Space (ISRO, Orbits, Missions), Biotechnology (CRISPR, Vaccines) & Emerging Defense Tech"
                ]
                topic_title = titles[day_offset - 1]
                sub_items_raw = [
                    f"Rapid timeline review and key terms for {topic_title.split(':')[1].strip()}",
                    "Solve 25 high-yield MCQs testing chronological order and administrative definitions",
                    "Review literature, foreign travellers' accounts, and institutional founders",
                    "Consolidate error notebook entries for historical facts"
                ]
                csat_topic = f"UNGIST CSAT: Reading Comprehension 5-Passage Speed Sherlocking"
                quote = "Buddhism, Jainism, and Gandhi are UPSC's evergreen sanctuaries. You must never lose a mark there."
        elif 134 <= day <= 140:
            subj = "CurrentAffairs"
            topic_id = "ca-rev"
            source = "2-Year PT 365 & Current Affairs Compilations"
            if day == 140:
                topic_title = "Phase 2 Grand Milestone Exam: Full UPSC Prelims Double Paper Simulation"
                sub_items_raw = [
                    "Paper 1 (GS-I 100 Questions, 09:30-11:30 AM): Strict exam-hall simulation with negative marking",
                    "Break & Rest (11:30 AM - 14:30 PM): Rest biological clock and mental reset",
                    "Paper 2 (CSAT 80 Questions, 14:30-16:30 PM): Timed execution of Sherlocking + Quant selection",
                    "Phase 2 Audit: Complete evaluation of 140 days of structured preparation"
                ]
                csat_topic = "Full Official UPSC CSAT 2024 Question Paper Under Timed Exam Conditions"
                quote = "Phase 2 is complete. You have built the foundation and reinforced the structure. Now begins the championship sprint."
            else:
                day_offset = day - 133
                titles = [
                    "PT 365 Consolidation 1: Polity, Governance & Landmark Constitutional Bench Rulings (2025–2027)",
                    "PT 365 Consolidation 2: Indian Economy, Banking Innovations, Flagship Schemes & Trade Agreements",
                    "PT 365 Consolidation 3: Environment, Wildlife Species in News, COP Summits & Ramsar Additions",
                    "PT 365 Consolidation 4: Science & Technology, ISRO Deep Space Missions, AI Treaties & Biotech",
                    "PT 365 Consolidation 5: International Relations, Strategic Chokepoints, West Asia & Multilateral Summits",
                    "PT 365 Consolidation 6: National & Global Indices, Reports, Committee Recommendations & Awards"
                ]
                topic_title = titles[day_offset - 1]
                sub_items_raw = [
                    f"Consolidate 2-year current affairs compilation for {topic_title.split(':')[1].strip()}",
                    "Anchor each news development back to its static syllabus root",
                    "Solve 25 UPSC-level current affairs MCQs with elimination reasoning",
                    "Review one-line factual summaries in personal revision deck"
                ]
                csat_topic = f"UNGIST CSAT Mixed Practice Set {day_offset}: Quant, Reasoning & Comprehension"
                quote = "Current affairs without static grounding is trivia; current affairs anchored to the Constitution is an IAS rank."
        else: # Days 141-180 (Phase 3: High-Yield Sprint & Full-Length Simulation)
            day_offset = day - 140
            subj = "Simulation"
            topic_id = f"sim-{day_offset}"
            source = "All-India Mock Series & 10-Year PYQ Forensic"
            
            if is_mock:
                topic_title = f"Phase 3 Weekly All-India Simulation Exam (GS 1 Full Mock + CSAT Full Mock)"
                sub_items_raw = [
                    f"Simulated Exam Paper 1 (09:30-11:30 AM): Target 85+ attempts with calculated risk management",
                    "Mid-day rest and cognitive recharge (11:30 AM - 14:30 PM)",
                    f"Simulated Exam Paper 2 (14:30-16:30 PM): Target 75+ net score in CSAT with zero anxiety",
                    "Evening forensic audit: Analyze negative marks, question selection errors, and time pressure slips"
                ]
                csat_topic = "Full Official CSAT Simulation Paper under strict 2-hour timer"
                quote = "In the final weeks, stamina is as vital as knowledge. Train your brain to stay razor-sharp for 4 hours."
            elif day >= 176:
                countdown = 180 - day
                titles = [
                    "Final Countdown T-4: Biological Clock Alignment & Zero-Stress Static Refresh",
                    "Final Countdown T-3: One-Page Memory Sheets Review (Articles, Treaties, Maps)",
                    "Final Countdown T-2: Examination Logistics, Hall Ticket, Black Ballpoint Pens & Route Check",
                    "Final Countdown T-1: Complete Cognitive Rest, Evening Walk & Mental Closure ('The Work is Done')",
                    "PRELIMS DAY: Execution Protocol! Methodical, Calm, Ruthless Elimination. You Are an Officer."
                ]
                topic_title = titles[day - 176]
                sub_items_raw = [
                    "Follow exact exam-day wake-up time (05:30 AM) and light hydration routine",
                    "Glance through high-yield memory triggers (Articles 14, 19, 21, 32, 200, 356, WPA schedules)",
                    "Zero anxiety, zero new material, zero doubt",
                    "Anchor into Neil Sir's core mental conviction: 'I am prepared for any surprise.'"
                ]
                csat_topic = "Light CSAT Formula Flashcard Scan (15 minutes only)"
                quote = "The journey from 40, 28, 55, 62 to an IAS officer is not decided by luck. It is decided by today's calm."
            else:
                titles = [
                    "All-India Mock 1 Execution + Forensic Option Post-Mortem",
                    "High-Probability Drill: Fundamental Rights & Constitutional Emergency Nuances",
                    "All-India Mock 2 Execution + Negative Marking Reduction Protocol",
                    "High-Probability Drill: Macroeconomics Inflation, BoP & Monetary Transmission",
                    "All-India Mock 3 Execution + 2-Hour Time Budget Optimization",
                    "High-Probability Drill: Protected Areas, Ramsar Sites & IUCN Red List Species",
                    "10-Year PYQ Forensic 1: UPSC Prelims 2024 & 2023 Option Traps & Patterns",
                    "All-India Mock 5 Execution + Post-Test Weak Area Remediation",
                    "10-Year PYQ Forensic 2: UPSC Prelims 2022 & 2021 'Pair-based' Logic",
                    "All-India Mock 6 Execution + Accuracy Rate Calibration (Target >75%)",
                    "10-Year PYQ Forensic 3: UPSC Prelims 2020 & 2019 Question Framing Analysis",
                    "High-Probability Drill: Indian River Confluences, Passes & World Conflict Straits",
                    "10-Year PYQ Forensic 4: UPSC Prelims 2018 & 2017 Science & Agriculture Patterns",
                    "All-India Mock 8 Execution + 3-Round Attempt Strategy Fine-Tuning",
                    "10-Year PYQ Forensic 5: UPSC Prelims 2016 & 2015 History Elimination Patterns",
                    "All-India Mock 9 Execution + Target Attempt Range Finalization (82-88 questions)",
                    "High-Probability Drill: Buddhism, Jainism, Gandhian Sessions & British Acts",
                    "CSAT High-Speed Intensive: 50 Questions in 75 Minutes (RC + Quant Selection)",
                    "All-India Mock 11 Execution + Pressure Inoculation Protocol",
                    "Rapid One-Page Review: All 12 Schedules & Major Constitutional Amendments",
                    "All-India Mock 12 Execution + Eliminating Unforced Errors",
                    "Rapid One-Page Review: Economic Survey Metrics, Budget Ratios & Deficits",
                    "All-India Mock 13 Execution + Final Speed Calibration",
                    "Rapid One-Page Review: Protected Areas, Biosphere Reserves & Ramsar Map Sheet",
                    "Grand All-India Full-Dress Rehearsal (FLT 15): Exact Exam Hall Timing (09:30-11:30 AM)",
                    "Error Notebook Final Review: Resolve Every Recurring Weak Spot",
                    "Grand All-India CSAT Full-Dress Rehearsal: Exact Exam Hall Timing (14:30-16:30 PM)",
                    "High-Probability 80%+ Topics Master Scan: Fast-forward through Top 20 Themes",
                    "Mindset & Psychological Anchoring: Neil Sir's 10 Commandments of Exam Composure",
                    "Final Atlas Review: 20 Most Critical World Conflict Locations & Straits"
                ]
                idx = (day - 141) % len(titles)
                topic_title = titles[idx]
                sub_items_raw = [
                    f"Focused study and timed drill for {topic_title}",
                    "Execute 3-round attempt strategy: Round 1 (100% sure), Round 2 (50-50 elimination), Round 3 (Educated guess)",
                    "Log mistakes strictly into Error Category: (A) Careless reading, (B) Knowledge gap, (C) Failed guess",
                    "Practice 15 minutes of calm, steady box-breathing to condition heart rate under pressure"
                ]
                csat_topic = f"UNGIST CSAT Speed Solving Drill {day_offset}: 10 Passages + 10 Quant in 35 mins"
                quote = "In the final sprint, you do not rise to the level of your hopes; you fall to the level of your training."
        
        sub_items = [{"id": f"{topic_id}__d{day}_s{idx}", "text": text} for idx, text in enumerate(sub_items_raw)]

    # Assemble Day MCQs (25 questions per day)
    day_mcqs = []
    
    # 1. Add static questions from subject
    subj_pool = static_questions_by_subject.get(subj, static_questions_by_subject["Polity"])
    if not subj_pool:
        subj_pool = static_questions_by_subject["Polity"]
    
    # Pick 10-15 static questions (rotating)
    num_static = 12
    for i in range(num_static):
        base_q = subj_pool[(day * 3 + i) % len(subj_pool)]
        q_copy = dict(base_q)
        q_copy['id'] = f"d{day}_q{i+1}"
        day_mcqs.append(q_copy)
        
    # 2. Add CA questions (8-10 questions rotating)
    ca_pool = ca_mcqs_by_pillar.get(subj, ca_mcqs_by_pillar.get('Polity', []))
    if not ca_pool:
        ca_pool = ca_mcqs_by_pillar['Polity']
        
    num_ca = 8
    for i in range(num_ca):
        base_ca = ca_pool[(day * 2 + i) % len(ca_pool)]
        ca_copy = dict(base_ca)
        ca_copy['id'] = f"d{day}_ca{i+1}"
        day_mcqs.append(ca_copy)
        
    # 3. Add CSAT questions (5 questions)
    csat_pool = static_questions_by_subject["CSAT"]
    for i in range(5):
        base_csat = csat_pool[(day + i) % len(csat_pool)]
        csat_copy = dict(base_csat)
        csat_copy['id'] = f"d{day}_csat{i+1}"
        day_mcqs.append(csat_copy)
        
    day_obj = {
        "day": day,
        "date": date_iso,
        "date_display": date_display,
        "phase": phase,
        "phase_name": phase_name,
        "week": week,
        "is_mock_day": is_mock,
        "subjects": [subj],
        "topic_id": topic_id,
        "topic_title": topic_title,
        "core_sources": source,
        "syllabus_anchor": f"GS Foundation › {subj} Core Syllabus",
        "sub_items": sub_items,
        "session_morning": {
            "time": "06:00 – 08:00 AM",
            "focus": f"Core Static: {topic_title}",
            "source": source,
            "tasks": [
                f"Read {source} deeply, focusing on constitutional articles, mechanisms, and exceptions",
                "Complete the granular sub-item checkpoints in the morning box",
                "Solve the 12 morning static MCQs and review any missed explanations",
                "Add your personal memory anchors into the topic notes"
            ]
        },
        "session_evening": {
            "time": "20:30 – 22:30 PM",
            "focus": f"Current Affairs ({subj}) & {csat_topic}",
            "ca_target": f"Read and analyze 5 Current Affairs articles ({subj} pillar) with inline MCQs",
            "csat_topic": csat_topic,
            "tasks": [
                f"Read 5 latest {subj} articles in the Current Affairs feed and test the 5-10 inline MCQs",
                f"Practice {csat_topic} using UNGIST mental models and zero-formula shortcuts",
                "Solve the 5 daily CSAT questions in the Day MCQ bank",
                "Final 10-minute daily review: Internalize the Neil Sir Principle of the Day"
            ]
        },
        "neil_sir_principle": quote,
        "day_mcqs": day_mcqs
    }
    
    days_curriculum.append(day_obj)

print(f"Generated {len(days_curriculum)} days of complete curriculum.")

# Save to data/curriculum-180.json
output_file = os.path.join(DATA_DIR, 'curriculum-180.json')
with open(output_file, 'w') as f:
    json.dump(days_curriculum, f, indent=2)

print(f"Successfully saved full 180-day master curriculum to {output_file}.")
