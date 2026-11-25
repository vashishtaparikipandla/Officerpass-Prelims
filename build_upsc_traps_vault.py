#!/usr/bin/env python3
"""
build_upsc_traps_vault.py
Parses the user-provided UPSC Prelims Polity — The Confusion List (115 distinctions across 8 modules)
into a structured JSON database: data/upsc-traps-vault.json.
Designed to be extensible across subjects (Polity, Economy, Environment, Sci-Tech, History, Geography, IR).
"""

import json
import os
import re

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_PATH = os.path.join(BASE_DIR, "data", "upsc-traps-vault.json")

RAW_POLITY_MARKDOWN = """
## 1. Constitution, parliamentary rules, law or convention?

| Recall prompt | Exact distinction | Authority |
|---|---|---|
| No-confidence motion | The Constitution provides collective responsibility to Lok Sabha without naming this motion. Lok Sabha Rule 198 expressly provides the motion against the Council of Ministers as a whole. At least 50 members must rise for leave. That is the admission threshold. | Art. 75(3), LS Rule 198 · **PYQ 2014** |
| Censure motion | Can specify the conduct or policy of an individual minister, several ministers or the Council of Ministers. There is no dedicated censure rule. Lok Sabha handles it under the general rules for motions. | LS Rules 184–189, Practice and Procedure of Parliament |
| Adjournment motion | A Lok Sabha device for a definite matter of urgent public importance, with the Speaker's consent. At least 50 members must rise for leave under Rule 60. Adjournment of a sitting is a different act. | LS Rules 56–63 · **PYQ 2017** |
| Calling Attention | A member with the Chair's permission calls a minister's attention to an urgent matter. This is provided in both Houses. | LS Rule 197, RS Rule 180 |
| Short-duration discussion | A formal discussion without a formal motion or vote. | LS Rules 193–196, RS Rules 176–179 |
| Question Hour | Starred means oral answer and possible supplementaries. Unstarred means written answer without supplementaries. Short-notice questions concern urgent public importance. | LS Rules 32–54, RS Rules 38–59 · **PYQ 2017, 2026** |
| Zero Hour | An established parliamentary practice. In Lok Sabha it generally follows Question Hour. The official FAQ describes the term as lacking formal recognition in parliamentary procedure. | Lok Sabha FAQ |
| Rule 377 and Special Mention | Lok Sabha uses Rule 377 for matters that cannot be raised under specified other rules. Rajya Sabha has its own Special Mention procedure under Rules 180A–180E. | LS Rule 377, RS Rules 180A–180E |
| Rajya Sabha Rule 267 | Suspension of a rule in its application to a motion related to listed business, subject to Chairman's consent. The proviso excludes cases with a specific suspension provision. | RS Rule 267 |
| Deputy Speaker | The office and the duty to choose a member as soon as may be are constitutional. The Speaker fixes the Deputy Speaker's election date under Rule 8. Giving the post to the opposition has been a convention. | Art. 93, LS Rules 7–8 · **PYQ 2017, 2022** |
| Leader of Opposition | The 1977 Act refers to the leader of the opposition party with the greatest numerical strength, recognised by the presiding officer. Section 2 prescribes no 10% threshold. | Leaders of Opposition Act, 1977, s. 2 |
| Political party, direction and whip | The Tenth Schedule expressly uses political party and recognises voting directions issued by a party or authorised person or authority. The separate 1998 Facilities Act expressly names chief whips. For voting or abstaining contrary to a direction, prior permission or condonation within 15 days can avoid disqualification. | Tenth Sch., para. 2(1)(b), Leaders and Chief Whips (Facilities) Act 1998 |
| Private member and private member's Bill | A member who is not a minister is a private member. An MP from the ruling party can qualify. | Lok Sabha Rules and FAQ · **PYQ 2017** |
| Parliamentary privileges | Freedom of speech in Parliament and immunity for speech or votes are express constitutional protections subject to the constitutional framework. Art. 105(3) allows other privileges to be defined by law. House rules prescribe privilege procedure. | Arts. 105, 194, LS Rules 222 onward |
| Office of profit | The disqualification is in the Constitution. The expression has no comprehensive constitutional definition. Parliament can exempt offices by law. | Arts. 102(1)(a), 191(1)(a), Parliament (Prevention of Disqualification) Act, 1959 · **PYQ 2019** |
| Attorney-General and Solicitor-General | Attorney-General is a constitutional office and serves during the President's pleasure. Art. 76 does not require resignation when the appointing government resigns. The Solicitor-General is governed by the Law Officers Rules. | Arts. 76, 88, Law Officers (Conditions of Service) Rules, 1987 · **PYQ 2022** |
| Cabinet and Cabinet committees | Art. 352(3) defines the Union Cabinet for written emergency advice. Cabinet committees are provided for in executive business rules under Art. 77(3). | Art. 352(3), Government of India (Transaction of Business) Rules, 1961 |
| Parliamentary financial committees | PAC and Committee on Public Undertakings each have up to 22 MPs, up to 15 from LS and up to 7 from RS. Estimates Committee has up to 30 MPs, all from LS. A minister cannot be a member of any of these three. | LS Rules 308–312B |
| SC/ST Welfare Committee | Up to 30 MPs. The full composition is 20 LS members and 10 RS members. Lok Sabha Speaker appoints its chair. Ministers are ineligible. Term is at most one year. | LS Rules 331A–331B and general committee rules · **PYQ 2026** |
| Practice of naming three sessions | Budget, Monsoon and Winter are usual names. Art. 85 prescribes a maximum six-month gap between the last sitting of one session and first sitting of the next, with no annual minimum sitting days. | Art. 85 · **PYQ 2020** |

## 2. Bodies with similar names and different legal origins

| Group | Exact distinction | Authority |
|---|---|---|
| Election commissions | ECI supervises elections to Parliament, state legislatures and the offices of President and Vice-President. State Election Commissions supervise panchayat and municipal elections. | Arts. 324, 243K, 243ZA |
| Finance commissions | Union Finance Commission is constituted by the President every fifth year or earlier. State Finance Commission is constituted by the Governor every fifth year and also reviews municipal finances. | Arts. 280, 243I, 243Y · **PYQ 2025** for the state appointing authority |
| GST Council | Constitutional body chaired by the Union Finance Minister. If voting, the Union has one-third of vote weight and states together two-thirds. A decision requires at least three-fourths of weighted votes of members present and voting. | Art. 279A |
| SC, ST and backward classes commissions | NCSC, NCST and NCBC are constitutional under Arts. 338, 338A and 338B respectively. NCBC had a statutory predecessor. | Arts. 338–338B · **PYQ 2023** |
| NHRC, Law Commission and NCDRC | NHRC is statutory under the 1993 Act. NCDRC is statutory under the Consumer Protection Act, 2019. Law Commission is constituted by executive notification. | PHRA 1993, s. 3, CPA 2019, s. 53, Law Commission website · **PYQ 2023** |
| NCW, NCM and NCPCR | Statutory bodies under the National Commission for Women Act, 1990, National Commission for Minorities Act, 1992, and Commissions for Protection of Child Rights Act, 2005 respectively. | Named Acts |
| Lokpal, CVC, CIC and NGT | Statutory under the Lokpal and Lokayuktas Act, 2013, CVC Act, 2003, RTI Act, 2005, and NGT Act, 2010 respectively. | Named Acts |
| NITI Aayog | Constituted by Union Cabinet resolution dated 1 January 2015. | Cabinet Secretariat resolution |
| Inter-State Council, Zonal Councils, North Eastern Council | Inter-State Council was established by presidential order under Art. 263 in 1990. Zonal Councils are under the States Reorganisation Act, 1956. NEC has its own 1971 Act. | Art. 263, States Reorganisation Act, s. 15, NEC Act 1971 |
| Delimitation Commission | Arts. 82 and 170 provide the framework for readjustment under a parliamentary law. The Commission for the last completed nationwide exercise was set up under the Delimitation Act, 2002. | Arts. 82, 170, Delimitation Act 2002 |
| CAG and PAC | CAG is a constitutional auditor. Detailed duties are statutory. PAC is a parliamentary committee that examines specified accounts and CAG reports. President or Governor causes relevant CAG reports to be laid before the appropriate legislature. | Arts. 148–151, CAG Act 1971, LS Rules 308–309 |
| UPSC and joint State PSC | A joint PSC can be created by parliamentary law after resolutions of the legislatures of the participating states. President appoints members of UPSC and joint PSC. Governor appoints State PSC members. President removes PSC members under Art. 317. | Arts. 315–317 |
| Linguistic minorities and SC/ST lists | Special Officer for Linguistic Minorities is appointed by President under Art. 350B. President initially specifies SC/ST lists for a state or UT. Parliament subsequently includes or excludes entries by law. | Arts. 341, 342, 350B |
| Central and state SEBC lists | President specifies the Central List under Art. 342A, and Parliament can amend it. A state or UT can prepare and maintain its own list for its own purposes by law. | Art. 342A, 105th Amendment |

## 3. Parliament and state legislatures

| Recall prompt | Exact distinction | Authority |
|---|---|---|
| Who is part of Parliament? | President, Rajya Sabha and Lok Sabha. President is a component of Parliament and holds no seat in either House. | Arts. 59, 79 |
| Adjourn, prorogue, dissolve | The Chair adjourns a sitting, including sine die. President prorogues a House. Only Lok Sabha is subject to dissolution. Prorogation can occur without prior adjournment sine die. | Arts. 83, 85, House procedure · **PYQ 2024** |
| What lapses? | Prorogation itself does not lapse Bills. On LS dissolution, a Bill pending in LS or passed by LS and pending in RS lapses, subject to Art. 108(5). A Bill pending in RS and never passed by LS survives. A notified joint sitting can proceed despite later dissolution. | Arts. 107–108 · **PYQ 2016** |
| Speaker's two voting rules | While presiding, casting vote on a tie. During consideration of removal of the Speaker, the Speaker cannot preside, can speak, and can vote in the first instance only. | Arts. 96, 100 · **PYQ 2024** |
| Speaker tenure and removal | Speaker continues until just before the first meeting of the new Lok Sabha. Removal needs 14 days' notice and a majority of all the then members of the House. | Art. 94 |
| Money Bill | Art. 110 uses only listed matters and incidental matters. Introduced only in LS with President's recommendation. RS has 14 days to recommend changes. Speaker certifies. President cannot return it for reconsideration. | Arts. 109–111, 117 |
| Financial Bill under Art. 117(1) | Includes a matter in Art. 110(1)(a)–(f) and other provisions. Introduced only in LS with President's recommendation, subject to the tax-reduction amendment proviso. RS has ordinary legislative powers, and joint sitting can apply. | Arts. 108, 117(1) |
| Financial Bill under Art. 117(3) | Involves expenditure from Consolidated Fund of India. Can be introduced in either House. President's recommendation is required before that House passes the Bill. | Art. 117(3) |
| Joint sitting | For qualifying deadlocks on ordinary Bills and eligible Financial Bills. Money Bills and Art. 368 Bills are excluded. Lok Sabha Speaker normally presides. | Arts. 108, 118(4), Joint Sittings Rules |
| Annual Financial Statement | Constitution uses Annual Financial Statement. LS votes demands for grants. Charged expenditure can be discussed without a vote. Appropriation by law permits withdrawal from the Consolidated Fund. | Arts. 112–114 |
| Consolidated Fund, Public Account, Contingency Fund | Revenue, loans raised and loan repayments received go into Consolidated Fund. Other public moneys received by or on behalf of the government go into Public Account. Contingency Fund is an imprest for advances pending legislative authorisation. | Arts. 266–267 |
| Legislative Council's veto | For ordinary Assembly Bills, first delay up to three months, second up to one month. The Constitution provides no joint sitting of state Houses. For Money Bills, Council recommends within 14 days. | Arts. 197–199 |
| Create or abolish a State Legislative Council | Assembly first resolves by majority of total membership plus at least two-thirds present and voting. Parliament then legislates by ordinary law. | Art. 169 |
| MPs may speak or vote where? | Ministers and Attorney-General can speak and participate in either House, joint sittings and committees of which they are named members. Art. 88 itself confers no vote. Ministers vote on the basis of membership. | Art. 88 · **PYQ 2022** |
| Rajya Sabha special powers | Art. 249 resolution opens Parliament's State List power in the national interest. Art. 312 resolution permits Parliament to create an All India Service by law. Both need at least two-thirds of RS members present and voting. | Arts. 249, 312 |

## 4. Executive, elections and disqualification

| Recall prompt | Exact distinction | Authority |
|---|---|---|
| President vs Vice-President electoral college | President uses elected MPs and elected MLAs of states plus Delhi and Puducherry. Vice-President uses members of both Houses of Parliament, including nominated MPs, and excludes MLAs. Both use proportional representation by single transferable vote and secret ballot. | Arts. 54–55, 66 |
| President's impeachment vs VP's removal | Impeachment can start in either House for violation of the Constitution. Each House needs at least two-thirds of total membership at its relevant stage. VP removal starts in RS by majority of all then members and must be agreed to by LS. Both procedures require at least 14 days' notice. | Arts. 61, 67 |
| Advice to President | President can require reconsideration of ministerial advice once and must act on the advice tendered after reconsideration. | Art. 74(1) |
| Reconsidering a Bill | President can return a non-Money ordinary Bill once and cannot withhold assent after Parliament repasses it. President must assent to a duly passed Art. 368 Bill. Governor's options under Art. 200 and President's under Art. 201 involve a separate framework. | Arts. 111, 200–201, 368 |
| Governor's assent and delay | Under the Supreme Court's November 2025 Art. 143 opinion, there are no judicially prescribed general deadlines or deemed assent. Prolonged, unexplained and indefinite inaction by a Governor can invite a limited judicial direction to act. | Arts. 200–201, 2025 INSC 1333 |
| Ordinance trigger and expiry | President can promulgate unless both Houses are in session. Governor uses the parallel rule for the state legislature. Six weeks run from reassembly, using the later date if Houses reassemble separately. The ordinance has the force of an Act within legislative competence. It remains subject to fundamental rights and cannot amend the Constitution under Art. 368. | Arts. 13, 123, 213, 368 |
| Pardon powers | President covers court-martial sentences, offences within Union executive competence and all death sentences. Governor's Art. 161 power concerns offences within state executive competence. Art. 72(3) preserves state-law power to suspend, remit or commute a death sentence. | Arts. 72, 161 |
| Ministerial caps and non-members | Union Council of Ministers cap is 15% of LS strength. State cap is 15% of Assembly strength, with a minimum of 12. A minister who is not a member of the relevant legislature for six consecutive months ceases to be a minister. The Constitution does not classify ministers into four ranks. | Arts. 75, 164 · **PYQ 2022** |
| Constitutional disqualification vs defection | For Art. 102(1) disqualifications of sitting MPs, President decides according to ECI opinion. For Art. 191(1) of sitting MLAs/MLCs, Governor decides according to ECI opinion. Defection is decided by the relevant Chair or Speaker under the Tenth Schedule, subject to judicial review. If the question concerns the presiding officer, the House elects another member to decide. | Arts. 103, 192, Tenth Sch. para. 6, Kihoto Hollohan |
| Changing parties | Voluntarily giving up membership can be inferred from conduct. An independent member is disqualified on joining a party after election. A nominated member can join within six months of taking the seat. Merger exception requires at least two-thirds of the legislature party. The old one-third split exception was removed. | Tenth Sch. paras. 2, 4, 91st Amendment · **PYQ 2022** for nominated members |
| Defection decision deadline | The Tenth Schedule fixes no deadline. The Supreme Court has said the Speaker should ordinarily decide within three months, absent exceptional circumstances. | Tenth Sch. para. 6, Keisham Meghachandra Singh · **PYQ 2022** for the Schedule |
| RPA 1950 and RPA 1951 | 1950 Act principally covers allocation of seats and electoral rolls. 1951 Act covers conduct of elections, qualifications and disqualifications, election disputes and party registration. | RPA 1950 and 1951 |
| Party registration and recognition | Registration with ECI comes from s. 29A. National/state party recognition and reserved symbols come from the Election Symbols Order. | RPA 1951 s. 29A, Symbols Order 1968 |
| Election commissioners | ECI is constitutional. Under the 2023 Act, President appoints on recommendation of a committee of PM, Lok Sabha Opposition Leader and a Union Cabinet Minister nominated by PM. The statute is under challenge. The 2023 Anoop Baranwal formula with CJI applied until Parliament made a law. | Art. 324, 2023 Act ss. 4, 7, Anoop Baranwal, September 2026 proceedings |
| Removal of CEC and other ECs | CEC removal follows the manner and grounds applicable to a Supreme Court judge. Other ECs and regional commissioners can be removed only on CEC recommendation. | Art. 324(5) |
| Age 18, 25, 30, 35 | 18 for electoral-roll registration subject to law. 25 for LS/Assembly. 30 for RS/Legislative Council. 35 for President, VP and Governor. | Arts. 58, 66, 84, 157, 173, 326 |
| Vote share and multiple constituencies | LS and Assembly use first-past-the-post, so 50% of votes polled is unnecessary. The ordinary cap is two constituencies in the same election of the type covered by s. 33(7). | RPA 1951 s. 33(7), Conduct of Elections Rules 1961 r. 64 · **PYQ 2017, 2021** |

## 5. Federal powers, emergencies and amendment

| Recall prompt | Exact distinction | Authority |
|---|---|---|
| Who has residuary power? | Parliament, including residuary taxing power. GST is separately dealt with by Art. 246A. Parliament alone legislates for GST on inter-State supplies. | Arts. 246A, 248, Union List Entry 97 |
| Parliament on State List | Five distinct routes to remember are Rajya Sabha national-interest resolution, national emergency, request by two or more state legislatures, implementing international obligations, and exercise of state legislative power under President's Rule. | Arts. 249, 250, 252, 253, 356–357 |
| Art. 249 vs Art. 252 | Art. 249 resolution lasts up to a year at a time, with renewals possible. The law ceases to have effect to the extent of incompetency six months after the resolution ends. Art. 252 legislation starts from resolutions of at least two states. Other states may adopt it. Only Parliament can amend or repeal it under that article. | Arts. 249, 252 |
| Conflict on Concurrent List | A conflicting state law reserved for and receiving presidential assent prevails in that state, subject to Parliament's power to override it. | Art. 254 |
| National Emergency | War, external aggression or armed rebellion. Written decision of Union Cabinet is required. Parliamentary approval normally within one month, then renewal every six months. Each House uses a majority of total membership plus at least two-thirds present and voting. Special rules apply if LS is dissolved. | Art. 352 |
| President's Rule | Failure of constitutional machinery in a state. Can be proclaimed on the Governor's report or otherwise. Normally approved within two months and renewed every six months. Three-year outer limit, with additional conditions for continuation beyond one year. | Arts. 356–357 |
| Financial Emergency | Threat to financial stability or credit of India or any part. Normally approved within two months. The Constitution prescribes no periodic renewal. | Art. 360 |
| Art. 358 vs Art. 359 | Art. 19 restrictions are relaxed by Art. 358 only for emergency on grounds of war or external aggression, subject to the constitutional limits. Art. 359 involves a presidential order suspending access to courts to enforce specified Part III rights. Arts. 20 and 21 are excluded. | Arts. 358–359 |
| Altering state boundaries vs giving up territory | Art. 3 legislation requires President's recommendation and referral to the affected state legislature for views in applicable cases. The state's consent is unnecessary. Cession of Indian territory to a foreign country requires a constitutional amendment. | Arts. 3–4, Berubari advisory opinion |
| Art. 368 passage | Bill can start in either House. Each House must separately pass it by majority of total membership and at least two-thirds present and voting. No joint sitting. Initiation is in Parliament without prior presidential recommendation. The President must assent once the requirements are met. | Art. 368 · **PYQ 2022** |
| When do states ratify? | At least half of state legislatures for listed federal changes. Includes Arts. 54, 55, 73, 162, 241 and 279A, specified judiciary chapters, Centre–state legislative relations, Seventh Schedule lists, representation of states in Parliament, and Art. 368 itself. | Proviso to Art. 368(2) · **PYQ 2025** |
| Quorum and majority denominators | Parliamentary quorum is generally one-tenth, subject to law. Removal of the Speaker uses a majority of all then members. Art. 368 combines a majority of total membership with two-thirds present and voting. GST Council has a separate weighted vote. | Arts. 94, 100, 279A, 368 |
| Basic structure and Ninth Schedule | Basic-structure limitation comes from Supreme Court doctrine. Ninth Schedule laws inserted after 24 April 1973 can be tested under the I.R. Coelho framework. | Kesavananda Bharati, I.R. Coelho, Art. 31B |
| Delimitation freeze vs seat reservation for women | Arts. 82 and 170 refer to publication of relevant figures of the first census taken after 2026 for the relevant freeze. Under Art. 334A, women's reservation takes effect after a delimitation exercise for that purpose following publication of figures of the first census taken after commencement of the 106th Amendment Act. The Act commenced on 16 April 2026 under S.O. 1922(E). Actual seat reservation still depends on Art. 334A's triggers. The 131st Amendment Bill failed in Lok Sabha in April 2026. | Arts. 82, 170, 239AA, 330A, 332A, 334A, Ministry of Parliamentary Affairs |

## 6. Rights, duties, courts and citizenship

| Recall prompt | Exact distinction | Authority |
|---|---|---|
| Constitution's title, commencement and repeal | Art. 393 supplies the short title. Art. 394 gives 26 January 1950 as the general commencement date and names provisions that took effect immediately on adoption. Art. 395 repeals the Indian Independence Act 1947 and Government of India Act 1935 with the stated exception for the Abolition of Privy Council Jurisdiction Act 1949. | Arts. 393–395 · **PYQ 2026** |
| Meaning of law in Art. 13 | Includes ordinances, orders, bye-laws, rules, regulations, notifications and customs or usages having the force of law in India. Art. 13(4) excludes amendments under Art. 368 from Art. 13. Basic-structure review independently applies. | Arts. 13, 368 · **PYQ 2026** |
| Preamble | Part of the Constitution and amendable within basic-structure limits. The 42nd Amendment added Socialist, Secular and integrity. The Preamble guides interpretation and confers no independent power or enforceable right. | Kesavananda Bharati, 42nd Amendment |
| Fundamental rights for citizens vs persons | Art. 19 is for citizens. Arts. 14, 20 and 21 protect persons. Separate rights have their own wording and exceptions. Art. 16 concerns public employment for citizens. | Arts. 14, 16, 19–21 |
| Rights against private action | Classic examples are untouchability under Art. 17, Art. 23 prohibitions and Art. 24's bar on employment of a child below 14 in any factory, mine or other hazardous employment. Art. 15(2) also reaches specified forms of exclusion in public access. | Arts. 15(2), 17, 23–24 |
| Education right, directive and duty | Art. 21A covers free and compulsory education for ages 6–14. Art. 45 concerns early childhood care and education until six. Art. 51A(k) concerns the parent or guardian's duty to provide educational opportunities for ages 6–14. | Arts. 21A, 45, 51A(k), 86th Amendment |
| Fundamental duties | In Art. 51A, Part IVA. The 42nd Amendment added ten. The 86th added the education duty. The constitutional duties address citizens. Laws can give effect to them. | Art. 51A, 42nd and 86th Amendments |
| DPSPs and Fundamental Rights | DPSPs are non-justiciable and fundamental in governance. Art. 31C's limited protection concerns laws giving effect to Art. 39(b) or (c) against Arts. 14 and 19, subject to judicial scrutiny of the connection. | Arts. 37, 39, 31C, Minerva Mills, Property Owners Association |
| Right to property | Constitutional right under Art. 300A, outside Part III. Deprivation requires authority of law. | Art. 300A, 44th Amendment |
| Writ jurisdiction | Supreme Court under Art. 32 for Part III rights. High Courts under Art. 226 for Part III rights and other legal rights. HC territorial jurisdiction may rest on where the cause of action arises wholly or in part. | Arts. 32, 226 |
| Five writs | Habeas corpus tests detention and can reach private detention. Mandamus enforces public duty and can reach a private body performing that duty. Quo warranto tests entitlement to public office and does not require personal injury. Prohibition stops proceedings beyond jurisdiction. Certiorari quashes an offending decision or order. | Arts. 32, 226, Supreme Court case law · **PYQ 2022** for mandamus and quo warranto |
| SC vs HC judges | Retirement ages 65 and 62 respectively. President appoints both. Removal for proved misbehaviour or incapacity requires an address from each House in the same session by majority of total membership and at least two-thirds present and voting. | Arts. 124, 217–218 |
| Advisory opinion, review, complete justice | Art. 143 is a presidential reference. Art. 137 is Supreme Court review of its own judgments or orders. Art. 142 concerns complete justice in a pending cause or matter. | Arts. 137, 142–143 |
| SC original jurisdiction | Art. 131 covers specified Union–state and inter-state disputes involving a legal right, subject to constitutional exceptions. Election disputes of the President and VP go to SC under Art. 71. | Arts. 71, 131 |
| Constitutional permission vs actual tribunal | Arts. 323A and 323B authorise legislation on tribunals. CAT is established by statute, and NGT by the NGT Act, 2010. High Court judicial review over tribunal decisions is preserved under L. Chandra Kumar. | Arts. 323A–323B, Administrative Tribunals Act 1985, NGT Act 2010 |
| Citizenship at commencement vs today | Part II deals principally with citizenship at commencement and preserves Parliament's lawmaking power. Current acquisition and loss are governed by the Citizenship Act, 1955. OCI status gives no right to vote under that Act. | Arts. 5–11, Citizenship Act ss. 3–10, 7B |

## 7. Local government, special areas and schedules

| Recall prompt | Exact distinction | Authority |
|---|---|---|
| Panchayats vs municipalities | 73rd Amendment, Part IX, Eleventh Schedule with 29 subjects. 74th Amendment, Part IXA, Twelfth Schedule with 18 subjects. State laws may endow responsibilities. Listing a subject does not itself transfer it to every local body. | Arts. 243G, 243W, Eleventh and Twelfth Schedules |
| Gram Sabha vs Gram Panchayat | Gram Sabha is the registered electorate for the village within the panchayat area. Panchayat is the institution of rural self-government. | Arts. 243(b), 243(d), 243A |
| Intermediate panchayat | May be omitted where state population does not exceed 20 lakh. Exactly 20 lakh qualifies. | Art. 243B(2) · **PYQ 2025** |
| Panchayat minimum age and term | A person aged 21 or more cannot be disqualified merely for being under 25. The five-year term runs from the date appointed for first meeting. If dissolved, election is normally within six months. The constitutional exception applies if the remaining term is less than six months. The replacement serves the remainder. | Arts. 243E, 243F |
| Women and SC/ST in local bodies | At least one-third of directly elected seats are reserved for women, including reserved SC/ST women's seats. At least one-third of panchayat chairperson offices at each level are for women. In municipalities, chairperson reservation follows state law. States can provide for backward-class reservation. | Arts. 243D, 243T · **PYQ 2026** for SC/ST women |
| Municipal types | Nagar Panchayat for transitional area, Municipal Council for smaller urban area, Municipal Corporation for larger urban area. Industrial township exception is available under the proviso. | Art. 243Q |
| Ward, district and metropolitan committees | Wards Committees constitutionally required in municipalities with population of at least 3 lakh. DPC consolidates district panchayat and municipal plans. MPC prepares a draft plan for metropolitan area. Elected shares are at least four-fifths for DPC and two-thirds for MPC. | Arts. 243S, 243ZD–243ZE |
| Fifth vs Sixth Schedule | Fifth covers Scheduled Areas and Scheduled Tribes outside Assam, Meghalaya, Tripura and Mizoram. Sixth governs specified tribal areas in those four states through autonomous councils. The four states are not covered in their entirety by Sixth Schedule councils. | Art. 244, Fifth and Sixth Schedules · **PYQ 2026** |
| Scheduled Area designation | President declares Scheduled Areas by order. Governor reports to President annually or when required and may make specified regulations subject to presidential assent. Tribes Advisory Councils have a different role. | Fifth Sch. paras. 3–6 · **PYQ 2023** |
| PESA | The 1996 Act extends Part IX with modifications to Fifth Schedule Scheduled Areas. Gram Sabha approves local plans before implementation, identifies beneficiaries, and certifies use of relevant village panchayat funds. | Art. 243M(4)(b), PESA ss. 3–4 |
| Languages | Hindi in Devanagari is Union official language under Art. 343. English continues for specified official purposes under law. Eighth Schedule lists 22 languages and does not designate a national language. | Arts. 343–345, Eighth Sch., Official Languages Act 1963 |
| Schedule number swaps | Second concerns emoluments and related provisions for specified constitutional officeholders. Third contains specified oath forms. Fourth allocates RS seats. Seventh lists legislative subjects. Ninth is tied to Art. 31B. Tenth concerns defection. | Constitution, Second–Fourth and Seventh–Tenth Schedules |
| Where are the oaths? | President, VP and Governor have oath forms in the articles. Specified ministers, MPs/MLAs, judges and CAG have forms in the Third Schedule. | Arts. 60, 69, 159, Third Sch. |

## 8. Constitutional history and governance

| Recall prompt | Exact distinction | Authority |
|---|---|---|
| 1858 vs 1947 | Government of India Act 1858 transferred governance from the East India Company to the Crown. Indian Independence Act 1947 provided for two Dominions. | Named Acts |
| 1909, 1919 and 1935 | 1909 reforms introduced separate Muslim electorates. 1919 introduced provincial dyarchy. 1935 provided provincial autonomy and proposed dyarchy at the federal Centre, where the proposed federation never came into operation. | Indian Councils Act and regulations 1909, Government of India Acts 1919 and 1935 |
| Constituent Assembly timelines | Constitution adopted on 26 November 1949. Most provisions commenced on 26 January 1950. | Preamble, Art. 394 |
| RTI vs constitutional right to information | The RTI Act gives citizens a statutory request mechanism. The constitutional right to receive information arises in freedom-of-speech jurisprudence. The commissions are creatures of statute. | Art. 19(1)(a), RTI Act 2005 ss. 3, 12, 15 |
| Model Code vs election law | ECI's Model Code is an administrative code. Conduct covered by it can separately attract action under election or other laws, for instance the RPA's 48-hour restriction on specified campaigning. | ECI Model Code, RPA 1951 s. 126 |
| CBI and CVC | CBI was established by executive resolution and draws police powers from the Delhi Special Police Establishment Act, 1946. CVC is statutory. Under the DSPE Act, state consent governs extension of DSPE powers to areas in a state, subject to exceptions including constitutional-court orders. | DSPE Act ss. 5–6, CVC Act 2003, State of West Bengal v. Committee for Protection of Democratic Rights |
"""

def parse_markdown_to_vault():
    lines = RAW_POLITY_MARKDOWN.strip().split("\n")
    current_sec_num = 0
    current_sec_title = ""
    
    sections = []
    items = []
    
    item_idx = 1
    
    for line in lines:
        line_s = line.strip()
        if line_s.startswith("## "):
            # Example: ## 1. Constitution, parliamentary rules, law or convention?
            m = re.match(r"##\s*(\d+)\.\s*(.*)", line_s)
            if m:
                current_sec_num = int(m.group(1))
                current_sec_title = m.group(2).strip()
                sections.append({
                    "section_num": current_sec_num,
                    "title": current_sec_title
                })
        elif line_s.startswith("|") and not line_s.startswith("|---") and not "Recall prompt" in line_s and not "Group" in line_s:
            parts = [p.strip() for p in line_s.split("|")[1:-1]]
            if len(parts) >= 3:
                prompt = parts[0]
                distinction = parts[1]
                authority = parts[2]
                
                # Check for PYQ tag
                is_pyq = "PYQ" in authority
                pyq_years = []
                for ym in re.finditer(r"PYQ\s*(\d{4}(?:\s*,\s*\d{4})*)", authority):
                    yrs = [y.strip() for y in ym.group(1).split(",")]
                    pyq_years.extend(yrs)
                
                clean_auth = authority.replace("**", "")
                
                item = {
                    "id": f"polity-trap-{item_idx:03d}",
                    "subject": "Polity",
                    "section_num": current_sec_num,
                    "section_title": current_sec_title,
                    "prompt": prompt,
                    "distinction": distinction,
                    "authority": clean_auth,
                    "raw_authority": authority,
                    "is_pyq": is_pyq,
                    "pyq_years": pyq_years
                }
                items.append(item)
                item_idx += 1

    vault = {
        "metadata": {
            "title": "UPSC Prelims Confusion & Trap Matrix",
            "last_updated": "2026-11-25",
            "subjects": ["Polity", "Economy", "Environment", "SciTech", "History", "Geography", "IR"],
            "total_items": len(items)
        },
        "subjects": {
            "Polity": {
                "title": "Indian Polity & Governance",
                "subtitle": "The Confusion List: Source, Authority, Exception & Numerical Traps",
                "total_items": len(items),
                "pyq_count": len([it for it in items if it["is_pyq"]]),
                "sections": sections,
                "items": items
            },
            "Economy": {
                "title": "Indian Economy & Fiscal Architecture",
                "subtitle": "Banking, Monetary Transmission, Fiscal Metrics & Trade Boundaries",
                "total_items": 0,
                "pyq_count": 0,
                "sections": [],
                "items": []
            },
            "Environment": {
                "title": "Environment, Ecology & Climate Change",
                "subtitle": "Wildlife Schedules, Conventions, Red Lists & Protected Areas",
                "total_items": 0,
                "pyq_count": 0,
                "sections": [],
                "items": []
            },
            "SciTech": {
                "title": "Science, Technology & Innovation",
                "subtitle": "Frontier Missions, Biotechnology, Quantum & Deep-Tech Traps",
                "total_items": 0,
                "pyq_count": 0,
                "sections": [],
                "items": []
            },
            "Geography": {
                "title": "Geography & Resource Mapping",
                "subtitle": "Straits, River Basins, Mineral Belts & Tectonic Frontiers",
                "total_items": 0,
                "pyq_count": 0,
                "sections": [],
                "items": []
            },
            "History": {
                "title": "History, Art & Culture",
                "subtitle": "Architectural Dynasties, Inscriptions, Bhakti Traditions & Colonial Acts",
                "total_items": 0,
                "pyq_count": 0,
                "sections": [],
                "items": []
            },
            "IR": {
                "title": "International Relations & Treaties",
                "subtitle": "Maritime Chokepoints, Global Groupings & Multilateral Treaties",
                "total_items": 0,
                "pyq_count": 0,
                "sections": [],
                "items": []
            }
        }
    }
    
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        json.dump(vault, f, indent=2, ensure_ascii=False)
        
    print(f"Successfully generated {OUTPUT_PATH}")
    print(f"Total Polity Confusion Items: {len(items)} across {len(sections)} sections.")
    print(f"PYQ Items Tagged: {len([it for it in items if it['is_pyq']])}")

if __name__ == "__main__":
    parse_markdown_to_vault()
