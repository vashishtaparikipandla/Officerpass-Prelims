#!/usr/bin/env python3
"""
Builds International Relations articles (ca-ir-01 to ca-ir-15: total 15 articles)
"""
import json
import os

BASE_DIR = '/Users/vashishtaparikipandla/Documents/OfficerPass'
with open(os.path.join(BASE_DIR, 'data', 'current-affairs-db.json')) as f:
    existing = json.load(f)

ir1 = [a for a in existing if a['pillar'] == 'IR']

def make_art(aid, dt, pillar, title, src, top100, pt365, sums, gs, qs):
    mcqs = []
    for i, (q, opts, ans, exp) in enumerate(qs):
        mcqs.append({
            "id": f"{aid}-q{i+1}",
            "q": q,
            "options": opts,
            "answer": ans,
            "explanation": exp
        })
    return {
        "id": aid, "date": dt, "pillar": pillar, "title": title, "source": src,
        "is_top100": top100, "is_pt365": pt365, "summary_points": sums, "gs_connection": gs, "mcqs": mcqs
    }

ir_new = [
    ("ca-ir-02", "2026-10-15", "IR", "BRICS Expansion: Inclusion of 5 New Member States & Global South Geopolitics", "MEA / The Hindu", True, True,
     ["BRICS officially expanded its membership beyond Brazil, Russia, India, China, and South Africa by admitting Iran, Egypt, Ethiopia, and the UAE.",
      "The expanded bloc represents ~45% of global population, ~36% of global GDP in PPP terms, and over 40% of global crude oil production.",
      "New Development Bank (NDB) based in Shanghai continues to mobilize resources in local currencies without IMF-style structural conditionalities."],
     "GS-2: Multilateral Groupings, BRICS Expansion, Global South, De-dollarization, New Development Bank.",
     [
         ("Which of the following countries officially joined BRICS as full members in the recent expansion wave?\n1. Iran\n2. Egypt\n3. Ethiopia\n4. United Arab Emirates\nSelect the correct answer:",
          ["(a) 1 and 2 only", "(b) 1, 2, 3 and 4", "(c) 3 and 4 only", "(d) 1 and 4 only"],
          "(b)", "Iran, Egypt, Ethiopia, and the UAE joined as full members starting 2024. Saudi Arabia was invited and participates in ministerial engagements; Argentina declined under President Milei."),
         ("At which BRICS Summit was the formal decision taken to invite new member states to expand the bloc?\n(a) 2021 New Delhi Summit\n(b) 2022 Beijing Summit\n(c) 2023 Johannesburg Summit (South Africa)\n(d) 2024 Kazan Summit (Russia)",
          ["(a) 2021 New Delhi Summit", "(b) 2022 Beijing Summit", "(c) 2023 Johannesburg Summit (South Africa)", "(d) 2024 Kazan Summit (Russia)"],
          "(c)", "The 15th BRICS Summit held in Johannesburg, South Africa in August 2023 adopted the historic declaration inviting six new countries."),
         ("Where is the permanent headquarters of the New Development Bank (NDB) established by BRICS nations?\n(a) New Delhi, India\n(b) Shanghai, China\n(c) Moscow, Russia\n(d) Brasilia, Brazil",
          ["(a) New Delhi, India", "(b) Shanghai, China", "(c) Moscow, Russia", "(d) Brasilia, Brazil"],
          "(b)", "The New Development Bank (NDB) is headquartered in Shanghai, China. Its first President was K.V. Kamath of India."),
         ("How is voting power distributed among the original founding member countries (BRICS) in the New Development Bank?\n(a) Weighted according to GDP contribution\n(b) Equal voting shares of 20% for each of the five founding members\n(c) China holds permanent veto power\n(d) Based on UN quota contributions",
          ["(a) Weighted according to GDP contribution", "(b) Equal voting shares of 20% for each of the five founding members\n", "(c) China holds permanent veto power", "(d) Based on UN quota contributions"],
          "(b)", "Unlike the World Bank where the US holds effective veto, NDB was founded on equal voting power: each founding member held an initial 20% share with no country having a veto."),
         ("What is the primary objective of the BRICS Contingent Reserve Arrangement (CRA)?\n(a) Financing joint military peacekeeping operations\n(b) Providing short-term balance-of-payments liquidity support during currency crises\n(c) Setting global oil benchmark prices\n(d) Issuing single common fiat currency",
          ["(a) Financing joint military peacekeeping operations", "(b) Providing short-term balance-of-payments liquidity support during currency crises", "(c) Setting global oil benchmark prices", "(d) Issuing single common fiat currency"],
          "(b)", "The $100 billion Contingent Reserve Arrangement (CRA) is a financial safety net providing liquidity and precautionary instruments to members facing BoP pressures.")
     ]),

    ("ca-ir-03", "2026-09-12", "IR", "India-Middle East-Europe Economic Corridor (IMEC) Strategic Architecture", "MEA / Livemint", True, True,
     ["IMEC was announced on the sidelines of the G20 New Delhi Summit by India, USA, UAE, Saudi Arabia, France, Germany, Italy, and EU.",
      "Consists of two corridors: Eastern Corridor connecting India to the Arabian Gulf, and Northern Corridor connecting Arabian Gulf to Europe.",
      "Integrates commercial shipping routes with a trans-continental rail network, hydrogen pipelines, and high-speed digital connectivity cables."],
     "GS-2: Connectivity Initiatives, West Asia Geopolitics, IMEC vs BRI, Indo-Pacific Connectivity.",
     [
         ("The India-Middle East-Europe Economic Corridor (IMEC) was officially launched at which international forum?\n(a) COP28 Summit in Dubai\n(b) G20 New Delhi Leaders' Summit (2023)\n(c) WEF Annual Meeting in Davos\n(d) Quad Summit in Hiroshima",
          ["(a) COP28 Summit in Dubai", "(b) G20 New Delhi Leaders' Summit (2023)", "(c) WEF Annual Meeting in Davos", "(d) Quad Summit in Hiroshima"],
          "(b)", "The IMEC MOU was signed on September 9, 2023 on the sidelines of the G20 Summit in New Delhi under the Partnership for Global Infrastructure and Investment (PGII)."),
         ("Which two strategic maritime/rail segments constitute the India-Middle East-Europe Economic Corridor?\n(a) Eastern Corridor (India to Arabian Gulf) and Northern Corridor (Arabian Gulf to Europe)\n(b) Western Corridor (India to Africa) and Arctic Corridor (India to Russia)\n(c) Trans-Himalayan Corridor and Indian Ocean Rim Corridor\n(d) Red Sea Canal and Mediterranean Railway",
          ["(a) Eastern Corridor (India to Arabian Gulf) and Northern Corridor (Arabian Gulf to Europe)", "(b) Western Corridor (India to Africa) and Arctic Corridor (India to Russia)", "(c) Trans-Himalayan Corridor and Indian Ocean Rim Corridor", "(d) Red Sea Canal and Mediterranean Railway"],
          "(a)", "IMEC links ports in western India (JNPT, Mundra) by sea to UAE ports (Jebel Ali, Fujairah), then across rail through Saudi Arabia and Jordan to Israel's Haifa port, connecting by sea to Greece/Europe (Piraeus)."),
         ("Which Israeli Mediterranean port is envisioned as the maritime gateway connecting the overland rail link to Europe under IMEC?\n(a) Ashdod Port\n(b) Haifa Port\n(c) Eilat Port\n(d) Tel Aviv Port",
          ["(a) Ashdod Port\n", "(b) Haifa Port", "(c) Eilat Port", "(d) Tel Aviv Port"],
          "(b)", "Haifa Port (operated by India's Adani Group in consortium) serves as the Mediterranean terminus where freight transitions from rail back onto container vessels bound for Europe."),
         ("In geopolitical strategy, IMEC is widely viewed as a democratic, transparent alternative to which Chinese global initiative?\n(a) Global Development Initiative (GDI)\n(b) Belt and Road Initiative (BRI)\n(c) Regional Comprehensive Economic Partnership (RCEP)\n(d) Shanghai Cooperation Organisation",
          ["(a) Global Development Initiative (GDI)", "(b) Belt and Road Initiative (BRI)", "(c) Regional Comprehensive Economic Partnership (RCEP)", "(d) Shanghai Cooperation Organisation"],
          "(b)", "IMEC offers an open, commercially viable connectivity alternative to China's BRI, which has faced international criticism over debt-trap diplomacy and lack of environmental sustainability."),
         ("Under which US-led multilateral initiative is IMEC financially backed and anchored?\n(a) Marshall Plan 2.0\n(b) Partnership for Global Infrastructure and Investment (PGII)\n(c) Blue Dot Network only\n(d) Build Back Better Act",
          ["(a) Marshall Plan 2.0", "(b) Partnership for Global Infrastructure and Investment (PGII)", "(c) Blue Dot Network only", "(d) Build Back Better Act"],
          "(b)", "IMEC is an flagship infrastructure undertaking under the G7 Partnership for Global Infrastructure and Investment (PGII) aiming to mobilize $600 billion in public-private capital.")
     ]),

    ("ca-ir-04", "2026-08-08", "IR", "Shanghai Cooperation Organisation (SCO): Belarus Admission & Regional Security", "MEA / The Hindu", False, True,
     ["The Shanghai Cooperation Organisation (SCO) admitted the Republic of Belarus as its 10th full member state at the Astana Summit in Kazakhstan.",
      "The Eurasian political, economic, and defense grouping now includes: China, Russia, Kazakhstan, Kyrgyzstan, Tajikistan, Uzbekistan, India, Pakistan, Iran, and Belarus.",
      "Regional Anti-Terrorist Structure (RATS) based in Tashkent serves as the permanent organ combating the 'three evils': terrorism, separatism, and extremism."],
     "GS-2: Regional Groupings, SCO Expansion, Central Asia, Eurasian Geopolitics, RATS Mechanism.",
     [
         ("Which country became the 10th full member state of the Shanghai Cooperation Organisation (SCO) at the 2024 Astana Summit?\n(a) Mongolia\n(b) Belarus\n(c) Armenia\n(d) Turkey",
          ["(a) Mongolia", "(b) Belarus", "(c) Armenia", "(d) Turkey"],
          "(b)", "Belarus officially completed accession procedures to become the 10th member of the SCO at the Astana Summit, following Iran's entry in 2023."),
         ("In which year did India and Pakistan officially become full members of the Shanghai Cooperation Organisation?\n(a) 2014\n(b) 2017\n(c) 2020\n(d) 2022",
          ["(a) 2014", "(b) 2017", "(c) 2020", "(d) 2022"],
          "(b)", "India and Pakistan were simultaneously admitted as full members at the historic Astana Summit in June 2017."),
         ("Where is the permanent headquarters of the Regional Anti-Terrorist Structure (RATS) of the SCO located?\n(a) Beijing, China\n(b) Tashkent, Uzbekistan\n(c) Almaty, Kazakhstan\n(d) Dushanbe, Tajikistan",
          ["(a) Beijing, China", "(b) Tashkent, Uzbekistan", "(c) Almaty, Kazakhstan", "(d) Dushanbe, Tajikistan"],
          "(b)", "While the SCO Secretariat is in Beijing, China, the Regional Anti-Terrorist Structure (RATS) is permanently based in Tashkent, Uzbekistan."),
         ("What are the 'Three Evils' that the SCO Charter specifically commits member states to combat?\n(a) Poverty, illiteracy, and disease\n(b) Terrorism, separatism, and extremism\n(c) Inflation, unemployment, and trade deficits\n(d) Smuggling, counterfeiting, and cyber hacking",
          ["(a) Poverty, illiteracy, and disease", "(b) Terrorism, separatism, and extremism", "(c) Inflation, unemployment, and trade deficits", "(d) Smuggling, counterfeiting, and cyber hacking"],
          "(b)", "The SCO Shanghai Convention of 2001 defines the collective fight against the 'three evils' of terrorism, separatism, and religious/political extremism."),
         ("Which founding member country of the 'Shanghai Five' was absent when the group transitioned into the full SCO in 2001, but is now an SCO member?\n(a) Uzbekistan (joined at 2001 creation)\n(b) Turkmenistan\n(c) Afghanistan\n(d) Mongolia",
          ["(a) Uzbekistan (joined at 2001 creation)", "(b) Turkmenistan\n", "(c) Afghanistan", "(d) Mongolia"],
          "(a)", "The Shanghai Five comprised China, Russia, Kazakhstan, Kyrgyzstan, and Tajikistan. Uzbekistan was invited in 2001, transforming the forum into the SCO.")
     ]),

    ("ca-ir-05", "2026-07-14", "IR", "Quad Leaders' Summit: Indo-Pacific Maritime Domain Awareness (IPMDA)", "MEA / PIB", True, True,
     ["The Quad (Quadrilateral Security Dialogue) comprising India, USA, Japan, and Australia reiterated commitment to a free, open, and inclusive Indo-Pacific.",
      "Indo-Pacific Partnership for Maritime Domain Awareness (IPMDA) provides real-time commercial satellite radio-frequency tracking of 'dark vessels' to regional littoral navies.",
      "Quad Climate Change Adaptation and Mitigation Package (Q-CHAMP) and Quad Semiconductor Supply Chain Initiative advance regional resilience."],
     "GS-2: Indo-Pacific, Maritime Security, Quad, Dark Shipping Detection, International Rules-Based Order.",
     [
         ("What is the primary operational mission of the Quad's Indo-Pacific Partnership for Maritime Domain Awareness (IPMDA)?\n(a) Building joint nuclear aircraft carriers\n(b) Tracking dark shipping, illicit maritime activities, and illegal, unreported and unregulated (IUU) fishing across the Indian Ocean and South China Sea\n(c) Subsidizing cruise ship tourism\n(d) Laying commercial trans-oceanic oil pipelines",
          ["(a) Building joint nuclear aircraft carriers", "(b) Tracking dark shipping, illicit maritime activities, and illegal, unreported and unregulated (IUU) fishing across the Indian Ocean and South China Sea", "(c) Subsidizing cruise ship tourism\n", "(d) Laying commercial trans-oceanic oil pipelines"],
          "(b)", "IPMDA integrates commercial synthetic aperture radar (SAR) and radio-frequency data to track vessels that deliberately switch off their Automatic Identification System (AIS) transponders."),
         ("Where is the Indian Navy's Information Fusion Centre for Indian Ocean Region (IFC-IOR) located?\n(a) Visakhapatnam\n(b) Gurugram, Haryana\n(c) Kochi\n(d) Port Blair",
          ["(a) Visakhapatnam", "(b) Gurugram, Haryana", "(c) Kochi", "(d) Port Blair"],
          "(b)", "IFC-IOR is based at Gurugram, Haryana, hosting international liaison naval officers from partner countries to coordinate white shipping data across the Indian Ocean."),
         ("Which annual multi-lateral naval exercise conducted by India originally began bilaterally with the US Navy in 1992 and now includes all four Quad nations?\n(a) Exercise Malabar\n(b) Exercise Varuna\n(c) Exercise Milan\n(d) Exercise RIMPAC",
          ["(a) Exercise Malabar", "(b) Exercise Varuna", "(c) Exercise Milan", "(d) Exercise RIMPAC"],
          "(a)", "Exercise Malabar began as an Indo-US bilateral naval drill in 1992, expanded to include Japan in 2015, and saw Australia rejoin permanently in 2020, making it a Quad drill."),
         ("The concept of 'Free and Open Indo-Pacific' (FOIP) was first prominently articulated in a diplomatic speech by which global statesman?\n(a) Manmohan Singh\n(b) Shinzo Abe (Address 'Confluence of the Two Seas' in Indian Parliament 2007)\n(c) Barack Obama\n(d) Kevin Rudd",
          ["(a) Manmohan Singh", "(b) Shinzo Abe (Address 'Confluence of the Two Seas' in Indian Parliament 2007)", "(c) Barack Obama", "(d) Kevin Rudd"],
          "(b)", "Japanese Prime Minister Shinzo Abe's 2007 speech to the Indian Parliament conceptualized the Indo-Pacific dynamic linking the Pacific and Indian oceans."),
         ("What is the legal status of the Quad alliance in international diplomacy?\n(a) A formal mutual defense treaty organization like NATO under Article 5\n(b) An informal strategic diplomatic partnership with no mutual military obligation\n(c) A specialized agency of the United Nations\n(d) A preferential trade customs union",
          ["(a) A formal mutual defense treaty organization like NATO under Article 5", "(b) An informal strategic diplomatic partnership with no mutual military obligation", "(c) A specialized agency of the United Nations", "(d) A preferential trade customs union"],
          "(b)", "The Quad is not a military pact or treaty alliance; it is an informal plurilateral forum focusing on regional public goods (vaccines, infrastructure, maritime domain awareness, climate).")
     ]),

    ("ca-ir-06", "2026-06-11", "IR", "India-US Initiative on Critical and Emerging Technologies (iCET)", "MEA / White House", True, True,
     ["iCET led by the National Security Advisors (NSAs) of India and the US deepens strategic technology collaboration across AI, semiconductors, quantum, and defense.",
      "Facilitated landmark co-production agreements including GE Aerospace F414 turbofan engines in India with 80% technology transfer to HAL for Tejas Mk2.",
      "Launched INDUS-X (India-US Defence Acceleration Ecosystem) connecting defense innovation startups, incubators, and university researchers."],
     "GS-2: Bilateral Relations, Defense Technology Transfer, iCET, Jet Engine Co-production, Critical Minerals.",
     [
         ("The Initiative on Critical and Emerging Technologies (iCET) between India and the United States is led and coordinated by:\n(a) Foreign Ministers\n(b) National Security Advisors (NSAs) of both nations\n(c) Commerce Secretaries\n(d) Defense Chiefs of Staff",
          ["(a) Foreign Ministers", "(b) National Security Advisors (NSAs) of both nations", "(c) Commerce Secretaries\n", "(d) Defense Chiefs of Staff"],
          "(b)", "iCET is spearheaded by India's National Security Advisor and the US National Security Advisor to elevate and expand strategic technology partnerships and defense industrial cooperation."),
         ("Under iCET, General Electric signed an MOU with Hindustan Aeronautics Limited (HAL) for licensed co-production of which fighter jet engine in India?\n(a) Pratt & Whitney F135\n(b) GE F414 turbofan engine\n(c) Eurojet EJ200\n(d) Klimov RD-33",
          ["(a) Pratt & Whitney F135", "(b) GE F414 turbofan engine", "(c) Eurojet EJ200", "(d) Klimov RD-33"],
          "(b)", "The GE F414-INS6 engine will be co-produced in India with unprecedented 80% transfer of technology (ToT) to power the indigenous Light Combat Aircraft (LCA) Tejas Mk2."),
         ("What does the 'INDUS-X' initiative launched under the iCET framework focus on?\n(a) Space mining on Mars\n(b) Defense innovation bridge connecting startups, investors, and defense research labs in India and the US\n(c) High-speed passenger bullet trains\n(d) Agricultural fertilizer manufacturing",
          ["(a) Space mining on Mars", "(b) Defense innovation bridge connecting startups, investors, and defense research labs in India and the US", "(c) High-speed passenger bullet trains", "(d) Agricultural fertilizer manufacturing"],
          "(b)", "INDUS-X (India-U.S. Defense Acceleration Ecosystem) bridges defense startups, investors, and military users to co-develop undersea warfare, drones, and AI technologies."),
         ("Which foundational defense agreement signed between India and the US in 2020 enables geospatial intelligence sharing between their armed forces?\n(a) GSOMIA (2002)\n(b) LEMOA (2016)\n(c) COMCASA (2018)\n(d) BECA (Basic Exchange and Cooperation Agreement, 2020)",
          ["(a) GSOMIA (2002)", "(b) LEMOA (2016)", "(c) COMCASA (2018)", "(d) BECA (Basic Exchange and Cooperation Agreement, 2020)"],
          "(d)", "BECA enables sharing of high-end satellite military topographical, nautical, and aeronautical data, enhancing missile targeting precision."),
         ("The 'Minerals Security Partnership' (MSP), which India joined under the iCET ambit, is a US-led multilateral coalition to:\n(a) Fix global market prices of gold bullion\n(b) Secure resilient, diverse global supply chains for critical energy minerals like lithium, cobalt, and rare earths\n(c) Regulate offshore coal mining\n(d) Ban mineral exports from developing countries",
          ["(a) Fix global market prices of gold bullion", "(b) Secure resilient, diverse global supply chains for critical energy minerals like lithium, cobalt, and rare earths", "(c) Regulate offshore coal mining", "(d) Ban mineral exports from developing countries"],
          "(b)", "MSP is a 14-nation partnership to catalyze public and private investment in global critical mineral supply chains, breaking Chinese processing monopolies.")
     ]),

    ("ca-ir-07", "2026-05-08", "IR", "Colombo Security Conclave (CSC): Charter Inscription & Maritime Security Pillar", "MEA / PIB", False, True,
     ["The Colombo Security Conclave (CSC) formalized its foundational Charter and Secretariat in Colombo, Sri Lanka.",
      "Founding member states include India, Sri Lanka, Maldives, Mauritius, and Bangladesh (as new member), with Seychelles participating as an observer.",
      "Operates around five core pillars: Maritime Safety, Countering Terrorism, Combating Transnational Organized Crime, Cyber Security, and Humanitarian Assistance (HADR)."],
     "GS-2: Neighborhood First Policy, SAGAR Doctrine, Indian Ocean Security, Colombo Security Conclave.",
     [
         ("Where is the permanent Secretariat of the Colombo Security Conclave (CSC) located?\n(a) Male, Maldives\n(b) Colombo, Sri Lanka\n(c) Port Louis, Mauritius\n(d) New Delhi, India",
          ["(a) Male, Maldives", "(b) Colombo, Sri Lanka", "(c) Port Louis, Mauritius", "(d) New Delhi, India"],
          "(b)", "The permanent Secretariat of the Colombo Security Conclave was formally institutionalized and established in Colombo, Sri Lanka."),
         ("Which country officially joined the Colombo Security Conclave as its fifth full member state?\n(a) Bangladesh\n(b) Myanmar\n(c) Nepal\n(d) Oman",
          ["(a) Bangladesh", "(b) Myanmar", "(c) Nepal", "(d) Oman"],
          "(a)", "Bangladesh was formally admitted as the fifth full member of the CSC, joining founding nations India, Sri Lanka, Maldives, and Mauritius."),
         ("What is the primary maritime security vision guiding India's engagements in the Indian Ocean Region under the CSC framework?\n(a) Project Mausam\n(b) SAGAR (Security and Growth for All in the Region)\n(c) Act East Policy\n(d) Look West Policy",
          ["(a) Project Mausam", "(b) SAGAR (Security and Growth for All in the Region)", "(c) Act East Policy", "(d) Look West Policy"],
          "(b)", "Prime Minister Narendra Modi's SAGAR doctrine (Security and Growth for All in the Region) frames India's role as a Preferred Security Partner and First Responder in the IOR."),
         ("Which of the following is NOT one of the five identified cooperation pillars of the Colombo Security Conclave?\n(a) Maritime Safety and Security\n(b) Countering Terrorism and Radicalization\n(c) Cyber Security and Protection of Critical Infrastructure\n(d) Mutual Extradition of Political Dissidents",
          ["(a) Maritime Safety and Security", "(b) Countering Terrorism and Radicalization", "(c) Cyber Security and Protection of Critical Infrastructure", "(d) Mutual Extradition of Political Dissidents"],
          "(d)", "The five pillars are: 1. Maritime Safety, 2. Counter-Terrorism, 3. Combating Trafficking & Crime, 4. Cyber Security, and 5. Humanitarian Assistance and Disaster Relief (HADR)."),
         ("Which island nation in the Western Indian Ocean currently participates in the Colombo Security Conclave as an official Observer?\n(a) Madagascar\n(b) Seychelles\n(c) Comoros\n(d) Reunion",
          ["(a) Madagascar\n", "(b) Seychelles", "(c) Comoros", "(d) Reunion"],
          "(b)", "Seychelles has actively engaged in meetings of the Colombo Security Conclave in an observer capacity.")
     ]),

    ("ca-ir-08", "2026-04-05", "IR", "International Criminal Court (ICC): Rome Statute Jurisdiction & Arrest Warrants", "UN / The Hindu", True, False,
     ["ICC Pre-Trial Chambers issued high-profile arrest warrants for war crimes and crimes against humanity arising from the Russia-Ukraine and Israel-Gaza conflicts.",
      "The ICC is governed by the Rome Statute 1998, exercising jurisdiction over genocide, crimes against humanity, war crimes, and the crime of aggression.",
      "India, the United States, China, Russia, and Israel are NOT state parties to the Rome Statute, maintaining reservations over sovereignty and UN Security Council referral powers."],
     "GS-2: International Judicial Bodies, Rome Statute, ICC vs ICJ, Universal Jurisdiction, State Sovereignty.",
     [
         ("What is the primary jurisdictional difference between the International Court of Justice (ICJ) and the International Criminal Court (ICC)?\n(a) ICJ settles legal disputes between sovereign States; ICC prosecutes individual persons for international crimes\n(b) ICJ handles maritime disputes; ICC handles environmental pollution\n(c) ICJ is an NGO; ICC is a UN organ\n(d) There is no jurisdictional difference",
          ["(a) ICJ settles legal disputes between sovereign States; ICC prosecutes individual persons for international crimes", "(b) ICJ handles maritime disputes; ICC handles environmental pollution", "(c) ICJ is an NGO; ICC is a UN organ", "(d) There is no jurisdictional difference"],
          "(a)", "The ICJ (a principal organ of the UN) adjudicates disputes between sovereign states. The ICC (an independent treaty-based body) prosecutes individuals for heinous international crimes."),
         ("Under the Rome Statute, what is meant by the principle of 'Complementarity' governing the ICC?\n(a) The ICC can automatically overrule national supreme courts at will\n(b) The ICC functions only as a court of last resort when a national judicial system is genuinely unwilling or unable to investigate or prosecute\n(c) The ICC must consult the UN General Assembly before every trial\n(d) The court operates only in alternating calendar years",
          ["(a) The ICC can automatically overrule national supreme courts at will", "(b) The ICC functions only as a court of last resort when a national judicial system is genuinely unwilling or unable to investigate or prosecute", "(c) The ICC must consult the UN General Assembly before every trial", "(d) The court operates only in alternating calendar years"],
          "(b)", "Complementarity (Article 17 of Rome Statute) means the ICC does not replace national courts; it intervenes only when national courts fail to act or conduct sham proceedings."),
         ("Is India a State Party to the Rome Statute of the International Criminal Court?\n(a) Yes, India ratified it in 2002\n(b) No, India has neither signed nor ratified the Rome Statute\n(c) India is a signatory but has not ratified it\n(d) India was expelled from the ICC",
          ["(a) Yes, India ratified it in 2002", "(b) No, India has neither signed nor ratified the Rome Statute", "(c) India is a signatory but has not ratified it", "(d) India was expelled from the ICC"],
          "(b)", "India chose not to sign or ratify the Rome Statute due to principled concerns regarding the subordination of the Court to the UN Security Council and definitions of terrorism and nuclear weapons."),
         ("Which body of the United Nations has the authority under Chapter VII of the UN Charter to refer situations to the ICC prosecutor regardless of state ratification?\n(a) UN General Assembly\n(b) UN Security Council\n(c) Economic and Social Council (ECOSOC)\n(d) International Law Commission",
          ["(a) UN General Assembly", "(b) UN Security Council", "(c) Economic and Social Council (ECOSOC)", "(d) International Law Commission"],
          "(b)", "Under Article 13(b) of the Rome Statute, the UN Security Council acting under Chapter VII can refer a situation in any country (even non-member states) to the ICC Prosecutor."),
         ("Where is the permanent seat and headquarters of the International Criminal Court located?\n(a) Geneva, Switzerland\n(b) The Hague, Netherlands\n(c) Strasbourg, France\n(d) Vienna, Austria",
          ["(a) Geneva, Switzerland", "(b) The Hague, Netherlands", "(c) Strasbourg, France", "(d) Vienna, Austria"],
          "(b)", "The permanent seat of the ICC is located in The Hague, Netherlands (the international capital of international law, which also hosts the ICJ and PCA).")
     ]),

    ("ca-ir-09", "2026-03-10", "IR", "India-EFTA Trade and Economic Partnership Agreement (TEPA): $100 Billion Investment Pact", "Ministry of Commerce / PIB", True, True,
     ["India signed a landmark Free Trade Agreement with the European Free Trade Association (EFTA) comprising Switzerland, Norway, Iceland, and Liechtenstein.",
      "Contains a legally binding investment commitment: EFTA nations will invest $100 billion in India over 15 years, creating one million direct jobs.",
      "India agreed to phase out customs duties on 95% of industrial exports from EFTA, while excluding sensitive agricultural products like dairy, soy, and gold."],
     "GS-2: Free Trade Agreements, Foreign Direct Investment, EFTA Nations, European Commercial Relations.",
     [
         ("Which four European countries constitute the European Free Trade Association (EFTA)?\n(a) Switzerland, Norway, Iceland, and Liechtenstein\n(b) United Kingdom, France, Germany, and Italy\n(c) Sweden, Denmark, Finland, and Norway\n(d) Austria, Belgium, Netherlands, and Luxembourg",
          ["(a) Switzerland, Norway, Iceland, and Liechtenstein", "(b) United Kingdom, France, Germany, and Italy", "(c) Sweden, Denmark, Finland, and Norway", "(d) Austria, Belgium, Netherlands, and Luxembourg"],
          "(a)", "EFTA was established in 1960 and consists of four non-EU European nations: Iceland, Liechtenstein, Norway, and Switzerland."),
         ("What unique, first-of-its-kind feature distinguishes the India-EFTA TEPA from India's previous Free Trade Agreements?\n(a) Elimination of all visa requirements for tourists\n(b) A legally binding commitment by EFTA to invest $100 billion in India over 15 years\n(c) Complete adoption of the Swiss Franc as a reserve currency\n(d) Direct free movement of military personnel",
          ["(a) Elimination of all visa requirements for tourists", "(b) A legally binding commitment by EFTA to invest $100 billion in India over 15 years", "(c) Complete adoption of the Swiss Franc as a reserve currency\n", "(d) Direct free movement of military personnel"],
          "(b)", "TEPA is historic because for the first time in global trade history, an FTA ties tariff concessions directly to a legally binding FDI investment commitment ($100B over 15 years)."),
         ("Which sensitive domestic Indian sector was completely excluded from tariff concessions under the EFTA TEPA to protect rural livelihoods?\n(a) IT and software services\n(b) Dairy, meat, soy, and agricultural staples\n(c) Diamond polishing\n(d) Pharmaceutical manufacturing",
          ["(a) IT and software services\n", "(b) Dairy, meat, soy, and agricultural staples", "(c) Diamond polishing", "(d) Pharmaceutical manufacturing"],
          "(b)", "India maintained a negative list strictly safeguarding domestic dairy (protecting dairy farmers against subsidized Swiss dairy), wheat, and soy."),
         ("What is the institutional relationship between EFTA member countries and the European Union (EU)?\n(a) EFTA countries are all full voting members of the EU\n(b) EFTA countries are not members of the EU, but three (Norway, Iceland, Liechtenstein) participate in the EU Single Market via the European Economic Area (EEA)\n(c) EFTA was expelled from Europe\n(d) EFTA has zero trade with the EU",
          ["(a) EFTA countries are all full voting members of the EU", "(b) EFTA countries are not members of the EU, but three (Norway, Iceland, Liechtenstein) participate in the EU Single Market via the European Economic Area (EEA)", "(c) EFTA was expelled from Europe", "(d) EFTA has zero trade with the EU"],
          "(b)", "EFTA operates parallel to the EU. Iceland, Liechtenstein, and Norway belong to the EEA; Switzerland accesses the EU single market via bilateral sectoral agreements."),
         ("In Free Trade Agreement terminology, 'Rules of Origin' (ROO) are designed to:\n(a) Ensure that imported products are produced in the FTA partner country rather than third-party goods merely transshipped to avoid tariffs\n(b) Track the flight route of cargo planes\n(c) Impose language requirements on product labeling\n(d) Ban all manufacturing across borders",
          ["(a) Ensure that imported products are produced in the FTA partner country rather than third-party goods merely transshipped to avoid tariffs", "(b) Track the flight route of cargo planes", "(c) Impose language requirements on product labeling", "(d) Ban all manufacturing across borders"],
          "(a)", "Rules of Origin mandate minimum domestic value addition in the partner nation to prevent trade deflection (e.g. third countries routing cheap goods through Switzerland into India).")
     ]),

    ("ca-ir-10", "2026-10-03", "IR", "Chagos Archipelago Agreement (UK-Mauritius Sovereignty Transfer) & Diego Garcia Base", "MEA / BBC", True, True,
     ["United Kingdom agreed to transfer sovereignty over the Chagos Archipelago in the central Indian Ocean to Mauritius, settling a decades-long decolonization dispute.",
      "The agreement secures the continued operation of the strategic US-UK joint military base on the island of Diego Garcia under a 99-year lease agreement.",
      "India played a quiet, consistent diplomatic role backing Mauritius' decolonization claim based on the 2019 ICJ Advisory Opinion and UNGA Resolution 73/295."],
     "GS-2: Decolonization, Indian Ocean Geopolitics, Diego Garcia, India-Mauritius Relations, ICJ Advisory Opinions.",
     [
         ("The Chagos Archipelago dispute involved sovereignty claims between which two nations?\n(a) France and Madagascar\n(b) United Kingdom and Mauritius\n(c) United States and Seychelles\n(d) India and Maldives",
          ["(a) France and Madagascar", "(b) United Kingdom and Mauritius", "(c) United States and Seychelles", "(d) India and Maldives"],
          "(b)", "The UK detached the Chagos Islands from Mauritius in 1965 prior to Mauritian independence, forming the British Indian Ocean Territory (BIOT), contested by Mauritius."),
         ("Which strategic joint US-UK naval and military base is located on the largest atoll of the Chagos Archipelago?\n(a) Agalega Base\n(b) Diego Garcia\n(c) Assumption Island\n(d) Socotra",
          ["(a) Agalega Base", "(b) Diego Garcia", "(c) Assumption Island", "(d) Socotra"],
          "(b)", "Diego Garcia is a crucial joint military installation hosting US long-range bombers and naval resupply ships overseeing the Middle East and Indo-Pacific."),
         ("In its 2019 landmark Advisory Opinion on the Chagos Archipelago, what did the International Court of Justice (ICJ) conclude?\n(a) The UK's administration of Chagos constitutes an unlawful, continuing wrongful act, and the UK is under an obligation to bring an end to its administration as rapidly as possible\n(b) Mauritius has no legal standing\n(c) The territory belongs permanently to the US\n(d) The islands must be submerged under climate treaties",
          ["(a) The UK's administration of Chagos constitutes an unlawful, continuing wrongful act, and the UK is under an obligation to bring an end to its administration as rapidly as possible", "(b) Mauritius has no legal standing", "(c) The territory belongs permanently to the US", "(d) The islands must be submerged under climate treaties"],
          "(a)", "The ICJ held that the decolonization of Mauritius was not lawfully completed in 1968 because the detachment of Chagos violated the right to self-determination and territorial integrity."),
         ("Which airstrip and maritime jetty facility was jointly inaugurated by India and Mauritius on Mauritius' outer islands in 2024?\n(a) Assumption Island\n(b) Agalega Island\n(c) Rodrigues Island\n(d) Tromelin Island",
          ["(a) Assumption Island\n", "(b) Agalega Island", "(c) Rodrigues Island", "(d) Tromelin Island"],
          "(b)", "India developed an upgraded 3,000-meter airstrip and deep-water jetty at Agalega Island, significantly enhancing Mauritian maritime surveillance and Indian Ocean domain awareness."),
         ("Are Advisory Opinions delivered by the International Court of Justice (ICJ) legally binding on sovereign states?\n(a) Yes, enforceable directly by UN peacekeepers\n(b) No, they are non-binding in strict legal terms but carry significant legal weight and moral authority in international customary law\n(c) They expire after 30 days\n(d) They apply only to EU nations",
          ["(a) Yes, enforceable directly by UN peacekeepers", "(b) No, they are non-binding in strict legal terms but carry significant legal weight and moral authority in international customary law", "(c) They expire after 30 days", "(d) They apply only to EU nations"],
          "(b)", "Unlike contentious judgments between states, ICJ advisory opinions requested by the UNGA or UNSC are non-binding but clarify fundamental principles of international law.")
     ]),

    ("ca-ir-11", "2026-08-22", "IR", "Comprehensive Nuclear-Test-Ban Treaty (CTBT) & Nuclear Arms Architecture", "UN / The Hindu", False, True,
     ["Russia formally withdrew its ratification of the Comprehensive Nuclear-Test-Ban Treaty (CTBT) to achieve strategic symmetry with the United States.",
      "CTBT bans all nuclear explosions, for both military and civilian purposes, in all environments (atmospheric, underwater, and underground).",
      "The treaty has not entered into force because it requires ratification by all 44 specific nuclear-capable states listed in Annex 2 (including India, Pakistan, and North Korea, which have not signed)."],
     "GS-2: Nuclear Non-Proliferation, Disarmament, CTBT Annex 2 States, Global Arms Control.",
     [
         ("The Comprehensive Nuclear-Test-Ban Treaty (CTBT) bans nuclear explosions in which of the following environments?\n(a) Only in the atmosphere and space\n(b) In all environments: underground, underwater, and in the atmosphere\n(c) Only for military weapons tests, permitting peaceful nuclear explosions\n(d) Only in the Arctic and Antarctic",
          ["(a) Only in the atmosphere and space", "(b) In all environments: underground, underwater, and in the atmosphere", "(c) Only for military weapons tests, permitting peaceful nuclear explosions", "(d) Only in the Arctic and Antarctic"],
          "(b)", "Article I of the CTBT establishes a zero-yield ban, prohibiting any nuclear weapon test explosion or any other nuclear explosion in any environment whatsoever."),
         ("Why has the Comprehensive Nuclear-Test-Ban Treaty (CTBT) NOT entered into force despite being adopted by the UN in 1996?\n(a) The UN budget ran out\n(b) Under Article XIV, it requires ratification by all 44 specific nuclear-technology-holding states listed in Annex 2\n(c) The ICJ declared it invalid\n(d) It was vetoed by Switzerland",
          ["(a) The UN budget ran out", "(b) Under Article XIV, it requires ratification by all 44 specific nuclear-technology-holding states listed in Annex 2", "(c) Under Article XIV, it requires ratification by all 44 specific nuclear-technology-holding states listed in Annex 2\n", "(d) It was vetoed by Switzerland"],
          "(b)", "Annex 2 lists 44 states possessors of nuclear reactors. Of these, India, Pakistan, and North Korea have not signed; while the US, China, Iran, Israel, and Egypt have signed but not ratified."),
         ("What is India's official diplomatic position regarding signing the CTBT?\n(a) India opposes the treaty on the grounds that it is non-universal, discriminatory, and fails to offer a time-bound roadmap for complete global nuclear disarmament\n(b) India is waiting for Pakistan to sign first\n(c) India has already ratified the treaty\n(d) India will sign only if admitted to NATO",
          ["(a) India opposes the treaty on the grounds that it is non-universal, discriminatory, and fails to offer a time-bound roadmap for complete global nuclear disarmament", "(b) India is waiting for Pakistan to sign first", "(c) India has already ratified the treaty", "(d) India will sign only if admitted to NATO"],
          "(a)", "India has maintained a voluntary unilateral moratorium on nuclear testing since 1998 but refuses to sign CTBT until nuclear weapon states commit to total, verifiable, non-discriminatory disarmament."),
         ("What global monitoring system verifies compliance with the CTBT using seismic, hydroacoustic, infrasound, and radionuclide stations?\n(a) International Monitoring System (IMS) operated by the CTBTO\n(b) Global Positioning System (GPS)\n(c) World Meteorological Organization radar network\n(d) INTERPOL Red Notices",
          ["(a) International Monitoring System (IMS) operated by the CTBTO", "(b) Global Positioning System (GPS)", "(c) World Meteorological Organization radar network", "(d) INTERPOL Red Notices"],
          "(a)", "The CTBTO PrepCom in Vienna operates the International Monitoring System (IMS) comprising 337 monitoring facilities globally that detect underground shockwaves and radioactive isotopes."),
         ("Which treaty signed in 1963 prohibited nuclear weapon tests in the atmosphere, in outer space, and under water, but permitted underground tests?\n(a) Non-Proliferation Treaty (NPT)\n(b) Partial Test Ban Treaty (PTBT)\n(c) Strategic Arms Reduction Treaty (START)\n(d) Treaty of Tlatelolco",
          ["(a) Non-Proliferation Treaty (NPT)", "(b) Partial Test Ban Treaty (PTBT)", "(c) Strategic Arms Reduction Treaty (START)", "(d) Treaty of Tlatelolco"],
          "(b)", "The Partial Nuclear Test Ban Treaty (PTBT) of 1963 banned tests everywhere except underground, allowing superpowers to continue underground test programs until the CTBT was drafted.")
     ]),

    ("ca-ir-12", "2026-07-20", "IR", "South China Sea Tensions: UNCLOS, Second Thomas Shoal & India's Maritime Stand", "MEA / Reuters", True, True,
     ["Confrontations between Chinese Coast Guard and Philippine resupply vessels intensified around the Second Thomas Shoal (Ayungin Shoal) in the Spratly Islands.",
      "The Permanent Court of Arbitration (PCA) 2016 South China Sea Arbitral Award ruled that China's 'Nine-Dash Line' historic claims have no legal basis under UNCLOS.",
      "India explicitly reaffirmed support for the 2016 Arbitral Award, advocating freedom of navigation, overflight, and unimpeded commerce in accordance with international law."],
     "GS-2: South China Sea, UNCLOS, Arbitral Award 2016, Act East Policy, Freedom of Navigation.",
     [
         ("In the 2016 South China Sea Arbitration ruling (Philippines v. China), what did the Permanent Court of Arbitration (PCA) decide regarding China's 'Nine-Dash Line'?\n(a) Upheld China's sovereignty completely\n(b) Ruled that China's claim to historic rights within the Nine-Dash Line was extinguished by UNCLOS\n(c) Transferred all islands to Vietnam\n(d) Refused to entertain the case due to lack of jurisdiction",
          ["(a) Upheld China's sovereignty completely", "(b) Ruled that China's claim to historic rights within the Nine-Dash Line was extinguished by UNCLOS", "(c) Transferred all islands to Vietnam", "(d) Refused to entertain the case due to lack of jurisdiction"],
          "(b)", "The Tribunal unanimously concluded that there was no legal basis for China to claim historic rights to resources within the sea areas falling within the 'Nine-Dash Line'."),
         ("The BRP Sierra Madre, a grounded World War II warship serving as a military outpost for the Philippines, is situated on which contested geographic feature?\n(a) Scarborough Shoal\n(b) Second Thomas Shoal (Ayungin Shoal)\n(c) Mischief Reef\n(d) Woody Island",
          ["(a) Scarborough Shoal", "(b) Second Thomas Shoal (Ayungin Shoal)", "(c) Mischief Reef", "(d) Woody Island"],
          "(b)", "The Philippines deliberately grounded the BRP Sierra Madre on Second Thomas Shoal in 1999 to assert its sovereign rights in its 200-nautical-mile Exclusive Economic Zone."),
         ("Under Article 121 of the UN Convention on the Law of the Sea (UNCLOS), can an artificial island or low-tide elevation generate a 200-nautical-mile Exclusive Economic Zone (EEZ)?\n(a) Yes, all reclaimed land generates an EEZ\n(b) No, rocks which cannot sustain human habitation or economic life of their own shall have no EEZ or continental shelf\n(c) Only if approved by the International Maritime Organization\n(d) Only if inhabited by military personnel",
          ["(a) Yes, all reclaimed land generates an EEZ", "(b) No, rocks which cannot sustain human habitation or economic life of their own shall have no EEZ or continental shelf", "(c) Only if approved by the International Maritime Organization", "(d) Only if inhabited by military personnel"],
          "(b)", "Article 121(3) specifies that rocks and low-tide elevations cannot generate an EEZ or continental shelf, precluding artificial sand-dredged bases from claiming broad sea rights."),
         ("Which key maritime strait connecting the Indian Ocean to the South China Sea is the most critical energy transit artery for East Asian economies?\n(a) Strait of Hormuz\n(b) Strait of Malacca\n(c) Bab-el-Mandeb\n(d) Bering Strait",
          ["(a) Strait of Hormuz", "(b) Strait of Malacca", "(c) Bab-el-Mandeb", "(d) Bering Strait"],
          "(b)", "The 800-km Strait of Malacca between the Malay Peninsula and Sumatra handles over 80% of China's crude oil imports, creating the strategic 'Malacca Dilemma'."),
         ("Which supersonic anti-ship cruise missile system did India deliver to the Armed Forces of the Philippines under a $375 million defense export agreement?\n(a) Akash Surface-to-Air Missile\n(b) BrahMos supersonic cruise missile\n(c) Pinaka Multi-Barrel Rocket System\n(d) Astra Beyond Visual Range Missile",
          ["(a) Akash Surface-to-Air Missile", "(b) BrahMos supersonic cruise missile", "(c) Pinaka Multi-Barrel Rocket System", "(d) Astra Beyond Visual Range Missile"],
          "(b)", "India delivered shore-based anti-ship variants of the BrahMos supersonic cruise missile (jointly developed with Russia) to the Philippine Marine Corps for coastal defense.")
     ]),

    ("ca-ir-13", "2026-06-28", "IR", "India-ASEAN Comprehensive Strategic Partnership & Review of AITIGA", "MEA / PIB", False, True,
     ["India and ASEAN are expediting the comprehensive review of the ASEAN-India Trade in Goods Agreement (AITIGA) to address persistent trade deficit concerns.",
      "India's trade deficit with ASEAN widened from $7.5 billion at AITIGA's inception in 2010 to over $43 billion, driven by imports of electronics, palm oil, and coal.",
      "Review aims to modernize Rules of Origin, eliminate non-tariff barriers, prevent trade re-routing from China, and improve mutual market access."],
     "GS-2: Act East Policy, ASEAN, Free Trade Agreements, AITIGA Review, Trade Deficit.",
     [
         ("The ASEAN-India Trade in Goods Agreement (AITIGA) entered into force in which year?\n(a) 2005\n(b) 2010\n(c) 2015\n(d) 2020",
          ["(a) 2005", "(b) 2010", "(c) 2015", "(d) 2020"],
          "(b)", "The AITIGA was signed in 2009 and came into effect on January 1, 2010, initiating tariff reduction schedules between India and the 10 ASEAN economies."),
         ("How many member countries currently constitute the Association of Southeast Asian Nations (ASEAN)?\n(a) 8\n(b) 10 (with Timor-Leste admitted in-principle as the 11th member)\n(c) 15\n(d) 20",
          ["(a) 8", "(b) 10 (with Timor-Leste admitted in-principle as the 11th member)", "(c) 15", "(d) 20"],
          "(b)", "The 10 member states are Brunei, Cambodia, Indonesia, Laos, Malaysia, Myanmar, Philippines, Singapore, Thailand, and Vietnam; Timor-Leste was granted observer/in-principle membership status."),
         ("Why did India opt out of joining the Regional Comprehensive Economic Partnership (RCEP) in 2019?\n(a) ASEAN requested India to withdraw\n(b) Unaddressed concerns over surging imports from China, lack of auto-trigger trade defense mechanisms, and strict rules of origin to prevent circumvention\n(c) Mandatory adoption of a common Asian currency\n(d) Opposition from the World Bank",
          ["(a) ASEAN requested India to withdraw", "(b) Unaddressed concerns over surging imports from China, lack of auto-trigger trade defense mechanisms, and strict rules of origin to prevent circumvention", "(c) Mandatory adoption of a common Asian currency", "(d) Opposition from the World Bank"],
          "(b)", "India withdrew from RCEP negotiations in Bangkok (2019) to protect domestic agriculture, MSMEs, and dairy from Chinese market flooding and inadequate safeguard mechanisms."),
         ("Which trilateral highway project connects Moreh in Manipur (India) with Mae Sot in Thailand via Myanmar?\n(a) India-Myanmar-Thailand (IMT) Trilateral Highway\n(b) Kaladan Multi-Modal Transit Transport Project\n(c) Asian Highway 1\n(d) BCIM Economic Corridor",
          ["(a) India-Myanmar-Thailand (IMT) Trilateral Highway", "(b) Kaladan Multi-Modal Transit Transport Project\n", "(c) Asian Highway 1", "(d) BCIM Economic Corridor"],
          "(a)", "The 1,360 km IMT Trilateral Highway connects Moreh in India to Mae Sot in Thailand via Myanmar, anchoring physical connectivity under the Act East Policy."),
         ("Where is the permanent diplomatic headquarters and Secretariat of ASEAN located?\n(a) Singapore\n(b) Jakarta, Indonesia\n(c) Bangkok, Thailand\n(d) Kuala Lumpur, Malaysia",
          ["(a) Singapore", "(b) Jakarta, Indonesia", "(c) Bangkok, Thailand", "(d) Kuala Lumpur, Malaysia"],
          "(b)", "The ASEAN Secretariat is permanently located in Jakarta, Indonesia.")
     ]),

    ("ca-ir-14", "2026-05-19", "IR", "BIMSTEC Charter Entry into Force & Bangkok Vision 2030", "MEA / PIB", True, True,
     ["The BIMSTEC Charter entered into formal legal force in May 2024, transforming BIMSTEC into an intergovernmental treaty-based international organization.",
      "Bay of Bengal Initiative for Multi-Sectoral Technical and Economic Cooperation connects 7 countries: Bangladesh, Bhutan, India, Myanmar, Nepal, Sri Lanka, and Thailand.",
      "India leads the Security Pillar (sub-sectors: Counter-Terrorism, Maritime Security, Cyber Security) under the reorganized 7-sector cooperation framework."],
     "GS-2: Regional Groupings, BIMSTEC Charter, Bay of Bengal, Neighborhood First, Security Pillar.",
     [
         ("The BIMSTEC grouping was originally established through which diplomatic declaration in 1997?\n(a) Dhaka Declaration\n(b) Bangkok Declaration\n(c) Colombo Declaration\n(d) Kathmandu Declaration",
          ["(a) Dhaka Declaration", "(b) Bangkok Declaration", "(c) Colombo Declaration", "(d) Kathmandu Declaration"],
          "(b)", "BIMSTEC was formed on June 6, 1997 through the Bangkok Declaration, originally as BIST-EC (Bangladesh, India, Sri Lanka, Thailand Economic Cooperation)."),
         ("Which two landlocked Himalayan nations joined BIMSTEC in 2004?\n(a) Nepal and Bhutan\n(b) Afghanistan and Nepal\n(c) Tibet and Bhutan\n(d) Sikkim and Ladakh",
          ["(a) Nepal and Bhutan", "(b) Afghanistan and Nepal", "(c) Tibet and Bhutan", "(d) Sikkim and Ladakh"],
          "(a)", "Nepal and Bhutan formally joined BIMSTEC in February 2004, broadening its geographic reach to the upper Himalayan river basins."),
         ("In the rationalized seven-pillar cooperation architecture of BIMSTEC, which pillar is officially led by India?\n(a) Trade, Investment and Development\n(b) Security (Counter-Terrorism, Transnational Crime, Cyber Security, Maritime Security)\n(c) Agriculture and Food Security\n(d) Science, Technology and Innovation",
          ["(a) Trade, Investment and Development", "(b) Security (Counter-Terrorism, Transnational Crime, Cyber Security, Maritime Security)", "(c) Agriculture and Food Security", "(d) Science, Technology and Innovation"],
          "(b)", "India leads the Security pillar. Bangladesh leads Trade/Investment; Bhutan leads Environment/Climate; Myanmar leads Agriculture; Sri Lanka leads Science/Tech; Thailand leads Connectivity; Nepal leads People-to-People Contact."),
         ("Where is the permanent Secretariat of BIMSTEC situated?\n(a) New Delhi, India\n(b) Dhaka, Bangladesh\n(c) Bangkok, Thailand\n(d) Colombo, Sri Lanka",
          ["(a) New Delhi, India", "(b) Dhaka, Bangladesh", "(c) Bangkok, Thailand", "(d) Colombo, Sri Lanka"],
          "(b)", "The BIMSTEC Permanent Secretariat is based in Dhaka, Bangladesh, inaugurated in 2014."),
         ("Why has BIMSTEC gained strategic ascendancy over SAARC in Indian foreign policy over the past decade?\n(a) SAARC was dissolved by the United Nations\n(b) Persistent paralysis in SAARC due to Pakistani obstruction and cross-border terrorism, making BIMSTEC a natural bridge linking South Asia with Southeast Asia\n(c) BIMSTEC possesses nuclear weapons\n(d) SAARC member states ran out of funding",
          ["(a) SAARC was dissolved by the United Nations", "(b) Persistent paralysis in SAARC due to Pakistani obstruction and cross-border terrorism, making BIMSTEC a natural bridge linking South Asia with Southeast Asia", "(c) BIMSTEC possesses nuclear weapons", "(d) SAARC member states ran out of funding"],
          "(b)", "Following repeated terrorist attacks from Pakistan (Uri, Pulwama), India shifted diplomatic capital to BIMSTEC, which excludes Pakistan and aligns with Act East and SAGAR objectives.")
     ]),

    ("ca-ir-15", "2026-04-02", "IR", "African Union Permanent Membership in G20: Global South Leadership", "G20 Secretariat / MEA", True, True,
     ["The 55-member African Union (AU) was formally inducted as a permanent member of the Group of Twenty (G20) during India's New Delhi Summit in 2023.",
      "The AU is only the second regional organization to become a full member of the G20, after the European Union (EU).",
      "Expands the representational legitimacy of the G20, bringing in 1.4 billion people and a continent with a collective GDP of over $3 trillion."],
     "GS-2: Global Governance, G20 Expansion, African Union, India-Africa Partnership, Global South Voice.",
     [
         ("The induction of the African Union as a permanent member of the G20 occurred under the presidency of which country?\n(a) Indonesia (2022)\n(b) India (2023)\n(c) Brazil (2024)\n(d) South Africa (2025)",
          ["(a) Indonesia (2022)", "(b) India (2023)", "(c) Brazil (2024)", "(d) South Africa (2025)"],
          "(b)", "Prime Minister Narendra Modi invited the African Union to take its seat as a permanent member on the opening morning of the G20 New Delhi Summit in September 2023."),
         ("How many sovereign member states are represented by the African Union (AU)?\n(a) 25\n(b) 40\n(c) 55\n(d) 65",
          ["(a) 25", "(b) 40", "(c) 55", "(d) 65"],
          "(c)", "The African Union represents all 55 sovereign nations on the African continent, succeeding the Organization of African Unity (OAU) in 2002."),
         ("Where is the permanent headquarters of the African Union situated?\n(a) Nairobi, Kenya\n(b) Addis Ababa, Ethiopia\n(c) Johannesburg, South Africa\n(d) Cairo, Egypt",
          ["(a) Nairobi, Kenya", "(b) Addis Ababa, Ethiopia", "(c) Johannesburg, South Africa", "(d) Cairo, Egypt"],
          "(b)", "The African Union headquarters is located in Addis Ababa, Ethiopia."),
         ("Which flagship trade agreement operationalized by the African Union creates the world's largest free trade area by number of participating countries?\n(a) African Continental Free Trade Area (AfCFTA)\n(b) COMESA Customs Union\n(c) ECOWAS Trade Treaty\n(d) SADC Monetary Pact",
          ["(a) African Continental Free Trade Area (AfCFTA)", "(b) COMESA Customs Union", "(c) ECOWAS Trade Treaty\n", "(d) SADC Monetary Pact"],
          "(a)", "AfCFTA creates a single continent-wide market of 1.4 billion people with tariff-free trade on 90% of goods, deepening intra-African value chains."),
         ("Prior to the African Union's inclusion, which single African country was the sole member of the G20?\n(a) Nigeria\n(b) South Africa\n(c) Egypt\n(d) Kenya",
          ["(a) Nigeria", "(b) South Africa", "(c) Egypt\n", "(d) Kenya"],
          "(b)", "South Africa was the only African nation in the original G20; the inclusion of the AU ensures equitable continental representation.")
     ])
]

all_ir = ir1 + [make_art(aid, dt, pil, tit, src, top, pt, sums, gs, qs) for aid, dt, pil, tit, src, top, pt, sums, gs, qs in ir_new]
print(f"Total IR articles: {len(all_ir)}")
assert len(all_ir) == 15, f"Expected 15, got {len(all_ir)}"

with open(os.path.join(BASE_DIR, 'data', 'ca_builders', 'ir.json'), 'w') as f:
    json.dump(all_ir, f, indent=2)

print("Saved ir.json successfully!")
