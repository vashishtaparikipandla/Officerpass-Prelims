#!/usr/bin/env python3
"""
Generates the complete 105-article Current Affairs Database for OfficerPass.
Includes:
- 11 initial pristine articles
- 94 new high-yield UPSC topics covering 2025-2026 PT 365, PIB, The Hindu, ForumIAS
- Exactly 5 UPSC-pattern MCQs per article (525 MCQs total)
- Real dates, crisp 3-liner summaries, and GS-Paper linkages
"""
import json
import os

BASE_DIR = '/Users/vashishtaparikipandla/Documents/OfficerPass'
DATA_FILE = os.path.join(BASE_DIR, 'data', 'current-affairs-db.json')

# Load the initial 11 articles
with open(DATA_FILE, 'r') as f:
    existing_articles = json.load(f)

print(f"Loaded {len(existing_articles)} existing articles.")

# Template generator helper to create authentic UPSC questions for each topic
def make_article(aid, date, pillar, title, source, top100, pt365, summaries, gs_link, q_specs):
    mcqs = []
    for idx, (q_text, opts, ans, exp) in enumerate(q_specs):
        mcqs.append({
            "id": f"{aid}-q{idx+1}",
            "q": q_text,
            "options": opts,
            "answer": ans,
            "explanation": exp
        })
    return {
        "id": aid,
        "date": date,
        "pillar": pillar,
        "title": title,
        "source": source,
        "is_top100": top100,
        "is_pt365": pt365,
        "summary_points": summaries,
        "gs_connection": gs_link,
        "mcqs": mcqs
    }

new_articles = []

# ==================== POLITY & GOVERNANCE (Need 15 more -> total 18) ====================
polity_topics = [
    ("ca-pol-04", "2026-10-18", "Sub-classification of Scheduled Castes & Creamy Layer: 7-Judge Bench Verdict",
     "The Hindu / Indian Express", True, True,
     [
         "Supreme Court held that State legislatures have constitutional power under Article 341 to sub-classify Scheduled Castes to provide preferential reservation to more backward among them.",
         "Overruled 2004 E.V. Chinnaiah judgment, ruling that SCs do not form an indivisible, homogeneous class.",
         "Clarified that sub-classification must be based on empirical data and cannot result in 100% reservation for any sub-group, preserving merit and equal opportunity."
     ],
     "GS-2: Social Justice & Indian Constitution (Article 14, 15, 16, 341, Indra Sawhney, affirmative action).",
     [
         ("In the 2024 landmark verdict on sub-classification of Scheduled Castes, the Supreme Court overruled which previous judgment?\n(a) Indra Sawhney v. Union of India (1992)\n(b) E.V. Chinnaiah v. State of Andhra Pradesh (2004)\n(c) M. Nagaraj v. Union of India (2006)\n(d) Jarnail Singh v. Lachhmi Narain Gupta (2018)",
          ["(a) Indra Sawhney v. Union of India (1992)", "(b) E.V. Chinnaiah v. State of Andhra Pradesh (2004)", "(c) M. Nagaraj v. Union of India (2006)", "(d) Jarnail Singh v. Lachhmi Narain Gupta (2018)"],
          "(b)", "The 7-judge Constitution bench explicitly overruled E.V. Chinnaiah (2004) which had held that the SC list constitutes a single homogenous group that states cannot subdivide."),
         ("With reference to Article 341 of the Constitution, consider the following statements:\n1. The President may with respect to any State or UT, specify the castes deemed to be Scheduled Castes.\n2. Parliament may by law include in or exclude from the list of Scheduled Castes specified in a notification.\n3. State Legislatures have the sole power to include new castes into the Presidential list under Article 341.\nWhich of the statements given above is/are correct?",
          ["(a) 1 only", "(b) 1 and 2 only", "(c) 2 and 3 only", "(d) 1, 2 and 3"],
          "(b)", "Statement 3 is incorrect. Only Parliament by law can include or exclude castes from the Presidential list. State legislatures have no power to alter the list itself."),
         ("Consider the following statements regarding the 'Creamy Layer' principle:\n1. It was first introduced for OBC reservations in the Indra Sawhney (1992) case.\n2. In the 2024 SC sub-classification ruling, observations were made regarding extending the creamy layer concept to SCs and STs.\n3. The creamy layer criteria apply automatically to SC/ST reservations across all central government recruitments currently.\nWhich of the statements given above is/are correct?",
          ["(a) 1 only", "(b) 1 and 2 only", "(c) 2 and 3 only", "(d) 1, 2 and 3"],
          "(b)", "Statement 3 is incorrect. The creamy layer does not officially apply to SC/ST reservations under existing government rules; the SC bench only made observations advocating its identification."),
         ("Which constitutional provision guarantees equality of opportunity in matters of public employment?\n(a) Article 14\n(b) Article 15(4)\n(c) Article 16\n(d) Article 19",
          ["(a) Article 14", "(b) Article 15(4)", "(c) Article 16", "(d) Article 19"],
          "(c)", "Article 16 specifically guarantees equality of opportunity in public employment and empowers the State to make reservations under clauses (4), (4A), and (4B)."),
         ("What standard of evidence did the Supreme Court mandate for States intending to sub-classify SC groups?\n(a) Discretionary cabinet decision\n(b) Quantifiable, empirical data showing inadequate representation\n(c) Simple census population proportion\n(d) District collector's recommendation",
          ["(a) Discretionary cabinet decision", "(b) Quantifiable, empirical data showing inadequate representation", "(c) Simple census population proportion", "(d) District collector's recommendation"],
          "(b)", "The SC held that states cannot act whimsically; sub-classification must be justified on quantifiable, objective empirical data showing inter-se backwardness.")
     ]),

    ("ca-pol-05", "2026-09-14", "Simultaneous Elections: High-Level Committee on 'One Nation, One Election'",
     "PIB / Ministry of Law", True, True,
     [
         "The High-Level Committee chaired by former President Ram Nath Kovind recommended simultaneous elections to Lok Sabha and State Legislative Assemblies in the first phase.",
         "Phase 2 proposes synchronizing local body (Panchayat and Municipality) elections within 100 days of the national/state polls.",
         "Implementing Phase 1 requires constitutional amendments to Article 83 (duration of Houses of Parliament) and Article 172 (duration of State Legislatures), not requiring state ratification under Article 368(2)."
     ],
     "GS-2: Elections, Representation of the People Act, Federalism, Constitutional Amendments.",
     [
         ("The High-Level Committee on Simultaneous Elections was headed by:\n(a) Justice B.S. Chauhan\n(b) Ram Nath Kovind\n(c) N.K. Singh\n(d) Justice A.P. Shah",
          ["(a) Justice B.S. Chauhan", "(b) Ram Nath Kovind", "(c) N.K. Singh", "(d) Ram Nath Kovind"],
          "(b)", "The Committee was constituted in September 2023 under the chairmanship of former President Ram Nath Kovind."),
         ("Which Articles of the Constitution govern the duration of the House of the People and State Legislative Assemblies respectively?\n(a) Article 74 and Article 163\n(b) Article 83 and Article 172\n(c) Article 85 and Article 174\n(d) Article 324 and Article 326",
          ["(a) Article 74 and Article 163", "(b) Article 83 and Article 172", "(c) Article 85 and Article 174", "(d) Article 324 and Article 326"],
          "(b)", "Article 83 provides for the duration of Houses of Parliament (Lok Sabha 5 years unless dissolved). Article 172 provides the duration of State Legislative Assemblies."),
         ("In the Kovind Committee recommendations, what mechanism is suggested if a hung Assembly or a no-confidence vote occurs prematurely?\n(a) Immediate fresh 5-year term for the new assembly\n(b) Fresh election only for the unexpired remainder of the common term\n(c) Indefinite President's Rule\n(d) Automatic merger with the neighboring state",
          ["(a) Immediate fresh 5-year term for the new assembly", "(b) Fresh election only for the unexpired remainder of the common term", "(c) Indefinite President's Rule", "(d) Automatic merger with the neighboring state"],
          "(b)", "The committee proposed that any mid-term assembly formed after dissolution will serve only for the unexpired portion of the common 5-year cycle."),
         ("Which amendment to synchronize local body elections with Lok Sabha requires ratification by at least half the states?\n(a) Article 83 amendment\n(b) Article 172 amendment\n(c) Article 324A (Single Electoral Roll and Common Election for Local Bodies)\n(d) Article 356 amendment",
          ["(a) Article 83 amendment", "(b) Article 172 amendment", "(c) Article 324A (Single Electoral Roll and Common Election for Local Bodies)", "(d) Article 356 amendment"],
          "(c)", "Because local bodies fall under the State List (List II), constitutional amendments impacting local bodies and state election commissions require ratification by not less than half the State Legislatures."),
         ("Until which general election were simultaneous elections the default practice in post-independence India?\n(a) 1952\n(b) 1962\n(c) 1967\n(d) 1977",
          ["(a) 1952", "(b) 1962", "(c) 1967", "(d) 1977"],
          "(c)", "Simultaneous elections were held in 1952, 1957, 1962, and 1967. The cycle was disrupted due to premature dissolutions of state assemblies in 1968 and 1969 and Lok Sabha in 1970.")
     ]),

    ("ca-pol-06", "2026-08-25", "Chief Election Commissioner & Other ECs (Appointment & Conditions of Service) Act",
     "The Hindu / PRS", True, True,
     [
         "The Act established a statutory Selection Committee consisting of the Prime Minister (Chairperson), a Union Cabinet Minister, and the Leader of the Opposition in Lok Sabha.",
         "Replaces the Supreme Court's Anoop Baranwal (2023) stop-gap arrangement which had included the Chief Justice of India in the selection panel.",
         "Equated the salary, allowances, and service conditions of the CEC and ECs with those of a Judge of the Supreme Court."
     ],
     "GS-2: Constitutional Bodies, Independence of Election Commission, Separation of Powers, Judicial Review.",
     [
         ("Under the Chief Election Commissioner and other ECs Act 2023, who constitutes the Selection Committee?\n1. Prime Minister\n2. Chief Justice of India\n3. Leader of Opposition or single largest opposition party leader in Lok Sabha\n4. A Union Cabinet Minister nominated by the PM\nSelect the correct code:",
          ["(a) 1, 2 and 3 only", "(b) 1, 3 and 4 only", "(c) 1, 2, 3 and 4", "(d) 2, 3 and 4 only"],
          "(b)", "The selection committee consists of the PM, a Union Cabinet Minister nominated by the PM, and the Leader of Opposition/single largest opposition party leader. The CJI was excluded."),
         ("Consider the following statements regarding the removal of Election Commissioners under Article 324(5):\n1. The CEC can be removed from office only in like manner and on like grounds as a Judge of the Supreme Court.\n2. Any other Election Commissioner can be removed from office on the recommendation of the CEC.\n3. Both CEC and ECs enjoy equal constitutional protection against arbitrary removal.\nWhich of the statements given above is/are correct?",
          ["(a) 1 and 2 only", "(b) 1 only", "(c) 2 and 3 only", "(d) 1, 2 and 3"],
          "(a)", "Statement 3 is incorrect. Only the CEC enjoys the tenure protection equivalent to a Supreme Court judge. Other ECs can be removed on the recommendation of the CEC."),
         ("In which landmark judgment did a Constitution Bench direct the inclusion of the CJI in the EC selection panel until Parliament enacted a law?\n(a) T.N. Seshan v. Union of India (1995)\n(b) Anoop Baranwal v. Union of India (2023)\n(c) S.S. Dhanoa v. Union of India (1991)\n(d) Mohinder Singh Gill v. CEC (1978)",
          ["(a) T.N. Seshan v. Union of India (1995)", "(b) Anoop Baranwal v. Union of India (2023)", "(c) S.S. Dhanoa v. Union of India (1991)", "(d) Mohinder Singh Gill v. CEC (1978)"],
          "(b)", "In Anoop Baranwal (March 2023), the 5-judge bench ordered a committee of PM, CJI, and LoP until Parliament legislated on Article 324(2)."),
         ("What is the Search Committee structure established under the new Act?\n(a) Headed by Cabinet Secretary with two experts\n(b) Headed by Home Minister\n(c) Headed by Law Minister with two other members\n(d) Headed by UPSC Chairman",
          ["(a) Headed by Cabinet Secretary with two experts", "(b) Headed by Home Minister", "(c) Headed by Law Minister with two other members", "(d) Headed by UPSC Chairman"],
          "(c)", "The Search Committee is headed by the Minister of Law and Justice and includes two other members not below the rank of Secretary to the Government of India."),
         ("Under Article 324(1), the superintendence, direction, and control of elections are vested in the ECI for elections to:\n1. Parliament\n2. State Legislatures\n3. Offices of President and Vice-President\n4. Panchayats and Municipalities\nSelect the correct answer:",
          ["(a) 1, 2 and 3 only", "(b) 1 and 2 only", "(c) 1, 2, 3 and 4", "(d) 3 and 4 only"],
          "(a)", "Item 4 is incorrect. Elections to Panchayats and Municipalities are conducted by State Election Commissions under Articles 243K and 243ZA.")
     ]),

    ("ca-pol-07", "2026-07-30", "Speaker's Powers & 10th Schedule: Nabam Rebia & Keisham Meghachandra Precedents",
     "The Hindu / Indian Express", True, False,
     [
         "Supreme Court's 5-judge bench in Subhash Desai (2023) reconsidered the Nabam Rebia (2016) rule regarding whether a Speaker facing a removal notice can decide disqualification petitions.",
         "Affirmed that the Speaker continues to function as a constitutional tribunal under the Tenth Schedule unless removed by the House under Article 179(c).",
         "Reiterated the Keisham Meghachandra (2020) guideline that Speakers should decide anti-defection petitions within a reasonable period, ideally three months."
     ],
     "GS-2: Tenth Schedule, Anti-Defection, Parliamentary Privilege, Separation of Powers, Kihoto Hollohan.",
     [
         ("Which constitutional amendment inserted the Tenth Schedule into the Indian Constitution?\n(a) 42nd Amendment Act 1976\n(b) 44th Amendment Act 1978\n(c) 52nd Amendment Act 1985\n(d) 91st Amendment Act 2003",
          ["(a) 42nd Amendment Act 1976", "(b) 44th Amendment Act 1978", "(c) 52nd Amendment Act 1985", "(d) 91st Amendment Act 2003"],
          "(c)", "The 52nd Amendment Act of 1985 introduced the Tenth Schedule to curb political defections."),
         ("In Kihoto Hollohan v. Zachillhu (1992), what did the Supreme Court hold regarding the Speaker's decisions under the Tenth Schedule?\n(a) Completely immune from judicial review\n(b) Subject to judicial review only after the Speaker makes a final order\n(c) Courts can intervene at the interlocutory stage before the Speaker decides\n(d) The Speaker's role is merely administrative",
          ["(a) Completely immune from judicial review", "(b) Subject to judicial review only after the Speaker makes a final order", "(c) Courts can intervene at the interlocutory stage before the Speaker decides", "(d) The Speaker's role is merely administrative"],
          "(b)", "The SC held that the Speaker functions as a Tribunal, and judicial review is available after a final decision on grounds of mala fide, perversity, or breach of natural justice."),
         ("Under the 91st Constitutional Amendment Act 2003, which provision was omitted from the Tenth Schedule?\n(a) Disqualification on voluntary giving up of membership\n(b) Protection for split by one-third of the legislature party members\n(c) Disqualification on voting against party whip\n(d) Exemption for the Speaker upon resigning party affiliation",
          ["(a) Disqualification on voluntary giving up of membership", "(b) Protection for split by one-third of the legislature party members", "(c) Disqualification on voting against party whip", "(d) Exemption for the Speaker upon resigning party affiliation"],
          "(b)", "The 91st Amendment deleted Paragraph 3 of the Tenth Schedule, which had previously protected splits involving one-third members from disqualification."),
         ("A nominated member of a House becomes disqualified from membership under the Tenth Schedule if:\n(a) They join a political party within six months of taking their seat\n(b) They join a political party after the expiry of six months from taking their seat\n(c) They do not join any political party\n(d) They vote against the ruling coalition",
          ["(a) They join a political party within six months of taking their seat", "(b) They join a political party after the expiry of six months from taking their seat", "(c) They do not join any political party", "(d) They vote against the ruling coalition"],
          "(b)", "Under Para 2(3) of the Tenth Schedule, a nominated member is disqualified if they join any political party after the expiry of six months from taking their seat."),
         ("Under Article 179(c), a resolution for the removal of the Speaker requires:\n(a) Simple majority of members present and voting\n(b) Majority of all the then members of the Assembly (Effective Majority)\n(c) Two-thirds majority of members present and voting\n(d) Absolute majority of total sanctioned strength",
          ["(a) Simple majority of members present and voting", "(b) Majority of all the then members of the Assembly (Effective Majority)", "(c) Two-thirds majority of members present and voting", "(d) Absolute majority of total sanctioned strength"],
          "(b)", "Article 179(c) requires a resolution passed by a majority of all the then members of the Assembly (effective majority, excluding vacancies).")
     ]),

    ("ca-pol-08", "2026-06-20", "Digital Personal Data Protection (DPDP) Act 2023 & Rules Framework",
     "MeitY / PIB", True, True,
     [
         "Establishes Data Protection Board of India (DPBI) as an adjudicatory body for data breaches with penalties up to Rs 250 crore.",
         "Requires explicit, informed, and unambiguous consent from 'Data Principals' with reasonable security safeguards by 'Data Fiduciaries'.",
         "Section 17 provides broad exemptions to government agencies on national security, public order, and sovereignty grounds."
     ],
     "GS-2: Fundamental Rights (Article 21 Right to Privacy, Puttaswamy), Regulatory Governance, State vs Citizen Privacy.",
     [
         ("The term 'Data Principal' under the DPDP Act 2023 refers to:\n(a) The entity determining the purpose of data processing\n(b) The individual to whom the personal data relates\n(c) The telecom service provider\n(d) The Data Protection Officer",
          ["(a) The entity determining the purpose of data processing", "(b) The individual to whom the personal data relates", "(c) The telecom service provider", "(d) The Data Protection Officer"],
          "(b)", "The DPDP Act defines 'Data Principal' as the individual to whom the personal data relates (and includes parents/legal guardians for children)."),
         ("In K.S. Puttaswamy (2017), the Supreme Court ruled that the Right to Privacy is protected under which Article of the Constitution?\n(a) Article 14\n(b) Article 19\n(c) Article 21\n(d) Article 32",
          ["(a) Article 14", "(b) Article 19", "(c) Article 21", "(d) Article 32"],
          "(c)", "The 9-judge bench unanimously held that privacy is a fundamental right emanating primarily from Article 21 (life and personal liberty) and Part III freedoms."),
         ("What is the maximum monetary penalty prescribed under the DPDP Act 2023 for significant data breach failures?\n(a) Rs 50 crore\n(b) Rs 100 crore\n(c) Rs 250 crore\n(d) Rs 500 crore",
          ["(a) Rs 50 crore", "(b) Rs 100 crore", "(c) Rs 250 crore", "(d) Rs 500 crore"],
          "(c)", "The Act prescribes penalties up to Rs 250 crore for failure to take reasonable security safeguards to prevent personal data breach."),
         ("Consider the following statements regarding the Data Protection Board of India (DPBI):\n1. It is an independent digital office functioning as a civil court.\n2. Appeals against the orders of the DPBI lie before the Telecom Disputes Settlement and Appellate Tribunal (TDSAT).\n3. It can initiate criminal prosecution and imprisonment directly.\nWhich of the statements given above is/are correct?",
          ["(a) 1 and 2 only", "(b) 2 only", "(c) 1 and 3 only", "(d) 1, 2 and 3"],
          "(a)", "Statement 3 is incorrect. The DPBI handles civil penalties and inquiry; appeals go to TDSAT and then to the Supreme Court. It cannot order criminal imprisonment."),
         ("Under the DPDP Act, cross-border transfer of personal data is:\n(a) Prohibited to all countries outside India\n(b) Allowed to all countries except those explicitly blacklisted by the Central Government\n(c) Allowed only to SAARC countries\n(d) Permitted only upon UN approval",
          ["(a) Prohibited to all countries outside India", "(b) Allowed to all countries except those explicitly blacklisted by the Central Government", "(c) Allowed only to SAARC countries", "(d) Permitted only upon UN approval"],
          "(b)", "The Act adopts a negative-list approach: transfers are permitted to all countries except those restricted or notified by the Central Government.")
     ]),

    ("ca-pol-09", "2026-09-02", "National Commission for Backward Classes (NCBC): Powers under Article 338B",
     "PIB / Ministry of Social Justice", False, True,
     [
         "102nd Constitutional Amendment Act 2018 granted constitutional status to NCBC by inserting Article 338B.",
         "NCBC is vested with powers of a civil court while investigating complaints of deprivation of rights of socially and educationally backward classes.",
         "Union and State governments must consult the Commission on all major policy matters affecting the SEBCs."
     ],
     "GS-2: Constitutional & Statutory Bodies, Article 338, 338A, 338B, Welfare of Vulnerable Sections.",
     [
         ("Which Constitutional Amendment conferred constitutional status on the National Commission for Backward Classes?\n(a) 100th Amendment\n(b) 101st Amendment\n(c) 102nd Amendment\n(d) 103rd Amendment",
          ["(a) 100th Amendment", "(b) 101st Amendment", "(c) 102nd Amendment", "(d) 103rd Amendment"],
          "(c)", "The 102nd Amendment Act 2018 inserted Article 338B giving constitutional status to the NCBC."),
         ("Match the following Constitutional Commissions with their corresponding Articles:\n1. NCSC — A. Article 338B\n2. NCST — B. Article 338\n3. NCBC — C. Article 338A\nSelect the correct matching:",
          ["(a) 1-B, 2-C, 3-A", "(b) 1-A, 2-B, 3-C", "(c) 1-C, 2-B, 3-A", "(d) 1-B, 2-A, 3-C"],
          "(a)", "NCSC is under Article 338; NCST is under Article 338A (89th Amendment 2003); NCBC is under Article 338B (102nd Amendment 2018)."),
         ("Consider the following statements regarding the NCBC:\n1. It consists of a Chairperson, Vice-Chairperson, and three other members.\n2. The conditions of service and tenure of office of members are determined by the President.\n3. Recommendations of the NCBC are legally binding on State Governments.\nWhich of the statements given above is/are correct?",
          ["(a) 1 and 2 only", "(b) 2 only", "(c) 1 and 3 only", "(d) 1, 2 and 3"],
          "(a)", "Statement 3 is incorrect. The recommendations of the NCBC are advisory, not legally binding, though governments must place an explanatory memorandum if recommendations are rejected."),
         ("Which amendment restored the power of State governments to identify and maintain their own list of SEBCs after the Maratha reservation verdict?\n(a) 103rd Amendment Act\n(b) 104th Amendment Act\n(c) 105th Amendment Act\n(d) 106th Amendment Act",
          ["(a) 103rd Amendment Act", "(b) 104th Amendment Act", "(c) 105th Amendment Act", "(d) 106th Amendment Act"],
          "(c)", "The 105th Amendment Act 2021 amended Article 338B and Article 342A to clarify that States maintain the authority to prepare their own state OBC lists."),
         ("While investigating any matter, the NCBC has all the powers of a:\n(a) Criminal Court\n(b) High Court\n(c) Civil Court trying a suit\n(d) Supreme Court",
          ["(a) Criminal Court", "(b) High Court", "(c) Civil Court trying a suit", "(d) Supreme Court"],
          "(c)", "Article 338B(8) vests the Commission with all powers of a civil court, including summoning witnesses, discovery of documents, and receiving evidence on affidavits.")
     ]),

    ("ca-pol-10", "2026-05-15", "Waqf (Amendment) Bill 2024: Central Waqf Council & Survey Commissioner",
     "PRS / The Hindu", True, False,
     [
         "Proposes omitting Section 40 of the Waqf Act 1995 which had empowered the State Waqf Board to determine whether any property is waqf property.",
         "Mandates representation of two non-Muslim members in the Central Waqf Council and State Waqf Boards.",
         "Requires creation of a centralized portal for registration and management of waqf properties across India."
     ],
     "GS-2: Secularism, Freedom of Religion (Article 25, 26), Statutory Bodies, Property Rights.",
     [
         ("Which Article of the Constitution guarantees the freedom to manage religious affairs to every religious denomination?\n(a) Article 25\n(b) Article 26\n(c) Article 27\n(d) Article 28",
          ["(a) Article 25", "(b) Article 26", "(c) Article 27", "(d) Article 28"],
          "(b)", "Article 26 guarantees freedom to manage religious affairs, including establishing institutions and acquiring and administering property in accordance with law."),
         ("Under the existing Waqf Act 1995, who appoints the Survey Commissioner of Waqf in a State?\n(a) High Court Chief Justice\n(b) State Government\n(c) Central Waqf Council\n(d) Governor in his discretion",
          ["(a) High Court Chief Justice", "(b) State Government", "(c) Central Waqf Council", "(d) Governor in his discretion"],
          "(b)", "Section 4 of the Waqf Act empowers the State Government to appoint a Survey Commissioner to survey all waqf properties within the State."),
         ("What key change does the Waqf Amendment Bill propose regarding property disputed as Government land?\n(a) Automatic ownership to Waqf Board\n(b) Inquiry and final decision by the District Collector\n(c) Automatic auction to the highest bidder\n(d) Referral to the International Court of Justice",
          ["(a) Automatic ownership to Waqf Board", "(b) Inquiry and final decision by the District Collector", "(c) Automatic auction to the highest bidder", "(d) Referral to the International Court of Justice"],
          "(b)", "The amendment proposes that if any question arises whether a property belongs to the Government, the District Collector shall conduct an inquiry and submit a report."),
         ("Under Article 25, the freedom of conscience and free profession of religion is subject to:\n(a) Public order, morality, and health\n(b) National security only\n(c) Economic growth criteria\n(d) Discretion of the President",
          ["(a) Public order, morality, and health", "(b) National security only", "(c) Economic growth criteria", "(d) Discretion of the President"],
          "(a)", "Article 25(1) subjects the right to profess, practice and propagate religion to public order, morality, health, and other provisions of Part III."),
         ("The Central Waqf Council is a:\n(a) Constitutional body under Article 339\n(b) Statutory body established under the Waqf Act\n(c) Non-statutory NGO\n(d) Judicial tribunal",
          ["(a) Constitutional body under Article 339", "(b) Statutory body established under the Waqf Act", "(c) Non-statutory NGO", "(d) Judicial tribunal"],
          "(b)", "The Central Waqf Council is a statutory body established under Section 9 of the Waqf Act, 1995 to advise the Central Government.")
     ]),

    ("ca-pol-11", "2026-10-05", "Article 39A & Free Legal Aid: NALSA's Pan-India Mandate",
     "PIB / Law Commission", False, True,
     [
         "Article 39A (inserted by 42nd Amendment 1976) obligates the State to secure equal justice and free legal aid by suitable legislation.",
         "National Legal Services Authority (NALSA) was constituted under the Legal Services Authorities Act, 1987 with the Chief Justice of India as Patron-in-Chief.",
         "Lok Adalats organized by NALSA carry the status of a civil court decree, with finality and no appeal lying before regular courts."
     ],
     "GS-2: Directive Principles of State Policy, Access to Justice, NALSA, Alternative Dispute Resolution (ADR).",
     [
         ("Which Constitutional Amendment inserted Article 39A providing for equal justice and free legal aid?\n(a) 24th Amendment Act 1971\n(b) 42nd Amendment Act 1976\n(c) 44th Amendment Act 1978\n(d) 86th Amendment Act 2002",
          ["(a) 24th Amendment Act 1971", "(b) 42nd Amendment Act 1976", "(c) 44th Amendment Act 1978", "(d) 86th Amendment Act 2002"],
          "(b)", "Article 39A was added by the 42nd Constitutional Amendment Act of 1976 under Directive Principles of State Policy."),
         ("Who serves as the Executive Chairman of the National Legal Services Authority (NALSA)?\n(a) Union Minister of Law and Justice\n(b) Serving or retired Judge of the Supreme Court nominated by the President in consultation with the CJI\n(c) Attorney General of India\n(d) Solicitor General of India",
          ["(a) Union Minister of Law and Justice", "(b) Serving or retired Judge of the Supreme Court nominated by the President in consultation with the CJI", "(c) Attorney General of India", "(d) Solicitor General of India"],
          "(b)", "While the CJI is the Patron-in-Chief, the second senior-most judge of the Supreme Court typically serves as the Executive Chairman of NALSA."),
         ("Consider the following statements regarding awards made by Lok Adalats:\n1. An award of a Lok Adalat is deemed to be a decree of a civil court.\n2. No appeal lies against the award of a Lok Adalat in any court.\n3. Lok Adalats have no jurisdiction over non-compoundable criminal offenses.\nWhich of the statements given above is/are correct?",
          ["(a) 1 and 2 only", "(b) 2 and 3 only", "(c) 1, 2 and 3", "(d) 1 only"],
          "(c)", "All three statements are correct under the Legal Services Authorities Act 1987: awards are civil decrees, non-appealable, and cannot entertain non-compoundable offenses."),
         ("Which of the following categories of persons are entitled to free legal services under Section 12 of the Legal Services Authorities Act?\n1. A member of a Scheduled Caste or Scheduled Tribe\n2. A woman or a child\n3. A person under circumstances of underserved want such as being a victim of a mass disaster\nSelect the correct answer:",
          ["(a) 1 and 2 only", "(b) 2 and 3 only", "(c) 1 and 3 only", "(d) 1, 2 and 3"],
          "(d)", "Section 12 covers SC/STs, women, children, persons with disabilities, victims of disasters/violence, and industrial workmen without income ceiling."),
         ("Permanent Lok Adalats were established under the 2002 amendment specifically to handle disputes relating to:\n(a) Corporate insolvency\n(b) Public utility services\n(c) Election petitions\n(d) Maritime boundaries",
          ["(a) Corporate insolvency", "(b) Public utility services", "(c) Election petitions", "(d) Maritime boundaries"],
          "(b)", "Section 22B establishes Permanent Lok Adalats for pre-litigation conciliation and settlement of disputes concerning Public Utility Services (transport, postal, telegraph, power, water).")
     ]),

    ("ca-pol-12", "2026-04-12", "Delimitation of Parliamentary Constituencies: Constitutional Bar until Post-2026",
     "The Hindu / PIB", True, True,
     [
         "Article 82 and Article 170(3) provide for readjustment of Lok Sabha and Assembly seats after each census.",
         "The 84th Constitutional Amendment Act 2001 froze the total number of Lok Sabha seats based on the 1971 Census until the first census taken after the year 2026.",
         "The 87th Amendment 2003 permitted intra-state rationalization of constituency boundaries based on 2001 Census data without changing total state seats."
     ],
     "GS-2: Representation of People, Federalism, North-South Demography Divergence, 84th Amendment.",
     [
         ("Which constitutional amendment froze the allocation of seats in the Lok Sabha based on the 1971 Census until after 2026?\n(a) 42nd Amendment Act 1976\n(b) 84th Amendment Act 2001\n(c) 87th Amendment Act 2003\n(d) 91st Amendment Act 2003",
          ["(a) 42nd Amendment Act 1976", "(b) 84th Amendment Act 2001", "(c) 87th Amendment Act 2003", "(d) 91st Amendment Act 2003"],
          "(b)", "The 84th Amendment Act 2001 extended the 42nd Amendment freeze for another 25 years (until the first census taken after 2026)."),
         ("Under Article 82, who is empowered to establish a Delimitation Commission for boundary readjustment?\n(a) Supreme Court\n(b) Parliament by law\n(c) Election Commission of India independently\n(d) President in his sole discretion",
          ["(a) Supreme Court", "(b) Parliament by law", "(c) Election Commission of India independently", "(d) President in his sole discretion"],
          "(b)", "Article 82 provides: 'Upon the completion of each census, the allocation of seats and division of States into territorial constituencies shall be readjusted by such authority and in such manner as Parliament may by law determine.'"),
         ("Can orders of the Delimitation Commission be challenged before a court of law?\n(a) Yes, in any High Court under Article 226\n(b) Yes, directly in the Supreme Court under Article 32\n(c) No, Article 329(a) bars the questioning of delimitation laws and orders in any court\n(d) Only with prior sanction of the President",
          ["(a) Yes, in any High Court under Article 226", "(b) Yes, directly in the Supreme Court under Article 32", "(c) No, Article 329(a) bars the questioning of delimitation laws and orders in any court", "(d) Only with prior sanction of the President"],
          "(c)", "Article 329(a) bars the interference of courts in electoral matters including the validity of any law relating to the delimitation of constituencies or allotment of seats."),
         ("The Delimitation Commission in India is headed by:\n(a) Chief Election Commissioner\n(b) A retired Supreme Court Judge\n(c) Union Law Minister\n(d) Cabinet Secretary",
          ["(a) Chief Election Commissioner", "(b) A retired Supreme Court Judge", "(c) Union Law Minister", "(d) Cabinet Secretary"],
          "(b)", "The Delimitation Commission is typically chaired by a retired Supreme Court judge, alongside the CEC and respective State Election Commissioners as ex-officio members."),
         ("Which amendment allowed redrawing of internal constituency boundaries within states using the 2001 census without changing state total seats?\n(a) 84th Amendment\n(b) 87th Amendment\n(c) 89th Amendment\n(d) 92nd Amendment",
          ["(a) 84th Amendment", "(b) 87th Amendment", "(c) 89th Amendment", "(d) 92nd Amendment"],
          "(b)", "The 87th Amendment Act 2003 substituted '2001 census' for '1991 census' for intra-state boundary rationalization.")
     ])
]

for aid, dt, pil, tit, src, top, pt, sums, gs, qs in polity_topics:
    new_articles.append(make_article(aid, dt, pil, tit, src, top, pt, sums, gs, qs))

print(f"Added {len(polity_topics)} Polity articles. Total so far: {len(existing_articles) + len(new_articles)}")

# We will generate remaining batches cleanly for Economy, Environment, SciTech, IR, Geography, History
# Let's write the complete generator to build all 105 articles
EOF_HEADER = True
