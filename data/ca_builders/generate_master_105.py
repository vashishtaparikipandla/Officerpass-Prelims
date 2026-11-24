#!/usr/bin/env python3
"""
Comprehensive Master Generator for OfficerPass Current Affairs Database:
Generates 105 authentic, syllabus-aligned UPSC Prelims articles with 525 MCQs.
"""
import json
import os

BASE_DIR = '/Users/vashishtaparikipandla/Documents/OfficerPass'
DATA_FILE = os.path.join(BASE_DIR, 'data', 'current-affairs-db.json')

# 1. Load Polity (18 articles already verified)
with open(os.path.join(BASE_DIR, 'data', 'ca_builders', 'polity.json'), 'r') as f:
    polity_articles = json.load(f)

print(f"Loaded Polity: {len(polity_articles)} articles")

# 2. Load existing 11 articles to extract the other pillars
with open(DATA_FILE, 'r') as f:
    existing_all = json.load(f)

existing_by_id = {a['id']: a for a in existing_all}

# Master collector
master_articles = list(polity_articles) # 18 articles

# Helper to build article
def build_art(aid, dt, pillar, title, src, top100, pt365, sums, gs, qs):
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
        "id": aid,
        "date": dt,
        "pillar": pillar,
        "title": title,
        "source": src,
        "is_top100": top100,
        "is_pt365": pt365,
        "summary_points": sums,
        "gs_connection": gs,
        "mcqs": mcqs
    }

# ==================== ECONOMY (Need 18 total) ====================
# Existing: ca-eco-01 (SDF), ca-eco-02 (CBDC), ca-eco-03 (Carbon Market)
master_articles.append(existing_by_id['ca-eco-01'])
master_articles.append(existing_by_id['ca-eco-02'])
master_articles.append(existing_by_id['ca-eco-03'])

# Load eco 04-08 from partial
with open(os.path.join(BASE_DIR, 'data', 'ca_builders', 'economy_partial.json'), 'r') as f:
    eco_part = json.load(f)
for a in eco_part:
    if a['id'] not in [x['id'] for x in master_articles]:
        master_articles.append(a)

# Add ca-eco-09 through ca-eco-18 (10 more -> total 18)
eco_new = [
    ("ca-eco-09", "2026-09-08", "Economy", "GIFT City IFSC: Tax Incentives & Global Financial Centre Architecture", "IFSCA / The Hindu", True, True,
     ["GIFT City in Gujarat is India's first operational International Financial Services Centre (IFSC) under the IFSCA Act 2019.",
      "Units enjoy 100% tax exemption for 10 consecutive years out of 15 years, zero GST on transactions, and exemption from dividend distribution tax.",
      "Allows Indian entities to access foreign currency funding and permits trading in offshore equity derivatives and bullion."],
     "GS-3: Financial Markets, Foreign Investment, Capital Account Liberalization, Regulatory Arbitrage.",
     [
         ("Which statutory body regulates all financial products and institutions in International Financial Services Centres in India?\n(a) Reserve Bank of India\n(b) Securities and Exchange Board of India\n(c) International Financial Services Centres Authority (IFSCA)\n(d) Insurance Regulatory and Development Authority",
          ["(a) Reserve Bank of India", "(b) Securities and Exchange Board of India", "(c) International Financial Services Centres Authority (IFSCA)", "(d) Insurance Regulatory and Development Authority"],
          "(c)", "The IFSCA was established under the IFSCA Act 2019 as a unified regulator for banking, capital markets, and insurance in IFSCs."),
         ("What is the primary corporate tax incentive provided to units operating within an IFSC in India?\n(a) Complete tax exemption forever\n(b) 100% tax holiday for any 10 consecutive years out of a block of 15 years\n(c) 50% concession on corporate tax rates\n(d) Full exemption from import customs duties on raw materials only",
          ["(a) Complete tax exemption forever", "(b) 100% tax holiday for any 10 consecutive years out of a block of 15 years", "(c) 50% concession on corporate tax rates", "(d) Full exemption from import customs duties on raw materials only"],
          "(b)", "Under Section 80LA of the Income Tax Act, IFSC units are eligible for a 100% tax deduction for 10 consecutive years chosen out of 15 years."),
         ("The term 'Deemed Foreign Territory' in the context of GIFT City IFSC implies that:\n(a) Indian criminal laws do not apply\n(b) Transactions are treated as offshore foreign exchange transactions for exchange control purposes\n(c) Only foreign citizens can work in the jurisdiction\n(d) India does not possess territorial sovereignty over the zone",
          ["(a) Indian criminal laws do not apply", "(b) Transactions are treated as offshore foreign exchange transactions for exchange control purposes", "(c) Only foreign citizens can work in the jurisdiction", "(d) India does not possess territorial sovereignty over the zone"],
          "(b)", "Under FEMA, an IFSC is considered a non-resident zone / offshore financial center for foreign currency and cross-border transactions."),
         ("Which exchange in GIFT City launched trading in SGX Nifty derivatives, renaming it GIFT Nifty?\n(a) National Stock Exchange IFSC (NSE IX)\n(b) India INX (BSE subsidiary)\n(c) Multi Commodity Exchange\n(d) Metropolitan Stock Exchange",
          ["(a) National Stock Exchange IFSC (NSE IX)", "(b) India INX (BSE subsidiary)", "(c) Multi Commodity Exchange", "(d) Metropolitan Stock Exchange"],
          "(a)", "GIFT Nifty trades on NSE International Exchange (NSE IX) within GIFT City, repatriating offshore dollar trading from Singapore to India."),
         ("Can foreign universities set up branch campuses in GIFT City IFSC without complying with domestic UGC regulations?\n(a) Yes, IFSCA regulations allow top foreign universities to set up autonomous offshore campuses\n(b) No, full UGC approval is mandatory\n(c) Only universities from Commonwealth countries are permitted\n(d) Only if 50% seats are reserved for Indian state students",
          ["(a) Yes, IFSCA regulations allow top foreign universities to set up autonomous offshore campuses", "(b) No, full UGC approval is mandatory", "(c) Only universities from Commonwealth countries are permitted", "(d) Only if 50% seats are reserved for Indian state students"],
          "(a)", "IFSCA (Setting up and Operations of International Branch Campuses and Offshore Education Centres) Regulations permit foreign universities ranked in global top 500 to operate free of domestic UGC rules.")
     ]),

    ("ca-eco-10", "2026-08-04", "Economy", "Expected Credit Loss (ECL) Framework: Transition from Incurred Loss Model", "RBI Bulletin / Mint", True, True,
     ["RBI issued draft guidelines mandating Scheduled Commercial Banks to transition to the Expected Credit Loss (ECL) provisioning model.",
      "Replaces the legacy 'incurred loss' approach where banks provisioned only after an asset defaulted (NPA recognized).",
      "Classifies financial assets into three stages based on credit deterioration: Stage 1 (12-month ECL), Stage 2 & 3 (Lifetime ECL)."],
     "GS-3: Banking, NPA Management, Basel III Norms, Financial Systemic Stability.",
     [
         ("The Expected Credit Loss (ECL) framework differs from the traditional provisioning model primarily because:\n(a) It relies solely on government guarantees\n(b) It requires banks to estimate future credit defaults prospectively rather than waiting for an actual default to occur\n(c) It eliminates the concept of Non-Performing Assets completely\n(d) It applies only to retail personal loans",
          ["(a) It relies solely on government guarantees", "(b) It requires banks to estimate future credit defaults prospectively rather than waiting for an actual default to occur", "(c) It eliminates the concept of Non-Performing Assets completely", "(d) It applies only to retail personal loans"],
          "(b)", "ECL is forward-looking and requires provisioning based on economic cycles and early credit distress signals rather than post-facto default."),
         ("Under the ECL approach aligned with IFRS 9 / Ind AS 109, what does Stage 2 classification signify?\n(a) Zero risk of default\n(b) Significant increase in credit risk since initial recognition, requiring lifetime expected loss provisioning\n(c) Actual default / credit-impaired asset\n(d) Sovereign debt asset",
          ["(a) Zero risk of default", "(b) Significant increase in credit risk since initial recognition, requiring lifetime expected loss provisioning", "(c) Actual default / credit-impaired asset", "(d) Sovereign debt asset"],
          "(b)", "Stage 2 represents financial instruments with significant increase in credit risk since origination, requiring lifetime expected credit loss recognition."),
         ("Which international regulatory framework established the foundation for Expected Credit Loss provisioning following the 2008 global financial crisis?\n(a) Basel I\n(b) Basel II\n(c) Basel III\n(d) Bretton Woods Agreement",
          ["(a) Basel I", "(b) Basel II", "(c) Basel III", "(d) Bretton Woods Agreement"],
          "(c)", "The Basel Committee on Banking Supervision (BCBS) under Basel III reforms mandated ECL models to resolve the procyclicality of incurred loss models."),
         ("What is the standard regulatory criteria for an asset to be classified as a Non-Performing Asset (NPA) in Indian commercial banks?\n(a) Interest or principal overdue for more than 30 days\n(b) Interest or principal overdue for more than 60 days\n(c) Interest or principal overdue for more than 90 days\n(d) Overdue for more than 180 days",
          ["(a) Interest or principal overdue for more than 30 days", "(b) Interest or principal overdue for more than 60 days", "(c) Interest or principal overdue for more than 90 days", "(d) Overdue for more than 180 days"],
          "(c)", "Under RBI prudential norms, a loan asset is classified as an NPA if interest or installment of principal remains overdue for more than 90 days."),
         ("How does the transition to the ECL model initially impact a bank's capital adequacy ratio (CRAR)?\n(a) It dramatically increases CRAR\n(b) It leads to higher provisioning requirements, temporarily reducing common equity Tier-1 (CET1) capital\n(c) It has zero impact on capital\n(d) It forces the bank into prompt corrective action automatically",
          ["(a) It dramatically increases CRAR", "(b) It leads to higher provisioning requirements, temporarily reducing common equity Tier-1 (CET1) capital", "(c) It has zero impact on capital", "(d) It forces the bank into prompt corrective action automatically"],
          "(b)", "Transitioning to ECL requires higher upfront provisions, which eat into retained earnings and lower CET-1 capital, leading RBI to offer a glide path of up to 5 years.")
     ]),

    ("ca-eco-11", "2026-07-19", "Economy", "India's Foreign Exchange Reserves & Import Cover Milestone", "RBI / Economic Survey", False, True,
     ["India's forex reserves surpassed $700 billion milestone, consisting of Foreign Currency Assets (FCA), Gold, SDRs, and Reserve Tranche Position (RTP).",
      "Foreign Currency Assets constitute the largest component (over 85%), held in major global reserve currencies like USD, Euro, GBP, and Yen.",
      "Reserve Bank of India has actively diversified into physical gold purchases, increasing gold share in reserves to over 9%."],
     "GS-3: External Sector, Balance of Payments, Forex Management, RBI Balance Sheet, Currency Stability.",
     [
         ("Which of the following is NOT a component of India's Foreign Exchange Reserves?\n(a) Foreign Currency Assets (FCA)\n(b) Gold holdings of the RBI\n(c) Special Drawing Rights (SDR) with the IMF\n(d) Indian Corporate Rupee Bonds held by domestic mutual funds",
          ["(a) Foreign Currency Assets (FCA)", "(b) Gold holdings of the RBI", "(c) Special Drawing Rights (SDR) with the IMF", "(d) Indian Corporate Rupee Bonds held by domestic mutual funds"],
          "(d)", "Forex reserves comprise 4 components: Foreign Currency Assets, Gold, SDRs, and Reserve Position in the IMF (RTP)."),
         ("The 'Reserve Tranche Position' (RTP) in the International Monetary Fund refers to:\n(a) The gold deposited by developing nations as penalty\n(b) The portion of a member country's quota paid in reserve currencies that can be withdrawn on demand without conditionality\n(c) The emergency loan extended to member countries under Structural Adjustment Programs\n(d) The interest charged on SDR allocations",
          ["(a) The gold deposited by developing nations as penalty", "(b) The portion of a member country's quota paid in reserve currencies that can be withdrawn on demand without conditionality", "(c) The emergency loan extended to member countries under Structural Adjustment Programs", "(d) The interest charged on SDR allocations"],
          "(b)", "A member country's quota with the IMF includes the Reserve Tranche, which is an unconditional reserve asset that can be drawn without policy obligations."),
         ("What is the primary currency basket determining the value of the IMF's Special Drawing Rights (SDR)?\n(a) US Dollar, Euro, Chinese Renminbi, Japanese Yen, British Pound\n(b) US Dollar, Euro, Indian Rupee, Russian Rouble\n(c) US Dollar and Euro only\n(d) Gold, Silver, and Platinum bullion prices",
          ["(a) US Dollar, Euro, Chinese Renminbi, Japanese Yen, British Pound", "(b) US Dollar, Euro, Indian Rupee, Russian Rouble", "(c) US Dollar and Euro only", "(d) Gold, Silver, and Platinum bullion prices"],
          "(a)", "The SDR basket consists of five currencies: US Dollar, Euro, Chinese Yuan/Renminbi (added in 2016), Japanese Yen, and British Pound Sterling."),
         ("What is the economic concept of 'Import Cover' of forex reserves?\n(a) The custom duty levied on imported luxury items\n(b) The number of months of imports that can be sustained by a country's foreign currency reserves\n(c) The insurance policy covering marine transport shipments\n(d) The ratio of exports to total imports",
          ["(a) The custom duty levied on imported luxury items", "(b) The number of months of imports that can be sustained by a country's foreign currency reserves", "(c) The insurance policy covering marine transport shipments", "(d) The ratio of exports to total imports"],
          "(b)", "Import cover measures how many months a nation can finance its projected import bill using its foreign exchange reserves (safe benchmark is 8-10 months)."),
         ("When the RBI intervenes in the forex market by selling US Dollars to arrest Rupee depreciation, what happens to domestic banking liquidity?\n(a) Domestic liquidity expands\n(b) Domestic liquidity is sucked out (contracts)\n(c) Liquidity remains entirely unaffected\n(d) Commercial banks are mandated to reduce CRR",
          ["(a) Domestic liquidity expands", "(b) Domestic liquidity is sucked out (contracts)", "(c) Liquidity remains entirely unaffected", "(d) Commercial banks are mandated to reduce CRR"],
          "(b)", "Selling dollars absorbs Indian Rupees from the banking system, reducing domestic liquidity and prompting RBI to sterilize via open market purchases.")
     ]),

    ("ca-eco-12", "2026-06-08", "Economy", "Internationalisation of the Rupee: Special Rupee Vostro Accounts (SRVA)", "RBI / The Hindu", True, True,
     ["RBI introduced mechanisms allowing invoicing, payment, and settlement of international trade in Indian Rupees (INR) via Special Rupee Vostro Accounts (SRVA).",
      "A Vostro account is an account held by a foreign bank with an Indian bank in domestic currency (INR).",
      "Surplus INR balances in SRVA can be invested in Indian Government Securities (G-Secs), Treasury Bills, and local bank deposits."],
     "GS-3: External Trade, Currency Risk, De-dollarisation, Bilateral Trade Settlement, Capital Account Convertibility.",
     [
         ("In international banking transactions, what does a 'Vostro Account' literally mean in Latin?\n(a) Our account with you\n(b) Your account with us\n(c) Mutual escrow account\n(d) Sovereign foreign exchange account",
          ["(a) Our account with you", "(b) Your account with us", "(c) Mutual escrow account", "(d) Sovereign foreign exchange account"],
          "(b)", "Vostro means 'your account with us' (a foreign bank's account maintained at an Indian bank in INR). Nostro means 'our account with you' (an Indian bank's account maintained abroad in foreign currency)."),
         ("Under RBI's rupee trade settlement mechanism, how can a foreign exporter be paid for goods shipped to India?\n(a) Through physical currency notes only\n(b) Indian importer pays in INR, which is credited to the foreign bank's Special Rupee Vostro Account (SRVA) in India\n(c) Payment must be cleared through New York CHIPS system in USD\n(d) Via barter arrangement of gold bullion",
          ["(a) Through physical currency notes only", "(b) Indian importer pays in INR, which is credited to the foreign bank's Special Rupee Vostro Account (SRVA) in India", "(c) Payment must be cleared through New York CHIPS system in USD", "(d) Via barter arrangement of gold bullion"],
          "(b)", "The Indian importer pays in Indian Rupees, which is credited into the Special Vostro account of the correspondent bank of the partner country."),
         ("Which committee set up by the RBI provided the roadmap for Fuller Capital Account Convertibility (FCAC)?\n(a) Tarapore Committee\n(b) Urjit Patel Committee\n(c) Bimal Jalan Committee\n(d) Rangarajan Committee",
          ["(a) Tarapore Committee", "(b) Urjit Patel Committee", "(c) Bimal Jalan Committee", "(d) Rangarajan Committee"],
          "(a)", "The Tarapore Committees on Capital Account Convertibility (1997 and 2006) laid down preconditions including low fiscal deficit, low inflation, and robust banking health."),
         ("What is the primary strategic benefit of internationalising the Indian Rupee in foreign trade settlements?\n(a) Elimination of exchange rate volatility and dependency on the US Dollar clearing system\n(b) Complete isolation from global inflation trends\n(c) Guaranteed surplus on the current account\n(d) Exemption from WTO tariff bindings",
          ["(a) Elimination of exchange rate volatility and dependency on the US Dollar clearing system", "(b) Complete isolation from global inflation trends", "(c) Guaranteed surplus on the current account", "(d) Exemption from WTO tariff bindings"],
          "(a)", "Invoicing in INR protects domestic traders against dollar exchange risks and mitigates vulnerabilities arising from unilateral Western sanctions on SWIFT."),
         ("Under the RBI Rupee settlement framework, surplus balances in SRVA accounts can be deployed into:\n(a) Speculative real estate investments\n(b) Government Treasury Bills and G-Secs\n(c) Cryptocurrency tokens\n(d) Unregulated peer-to-peer lending",
          ["(a) Speculative real estate investments", "(b) Government Treasury Bills and G-Secs", "(c) Cryptocurrency tokens", "(d) Unregulated peer-to-peer lending"],
          "(b)", "RBI allows foreign banks to invest surplus rupee funds in Indian Government securities, treasury bills, and bank deposits to earn yield.")
     ]),

    ("ca-eco-13", "2026-05-18", "Economy", "Current Account Deficit (CAD) Dynamics & Services Export Resilience", "Ministry of Commerce / RBI", False, True,
     ["India's Current Account Deficit (CAD) moderated to sustainable levels under 1.5% of GDP despite merchandise trade deficits exceeding $240 billion.",
      "Resilience is driven by record surplus in services exports ($160B+ surplus) spanning IT software, business consulting, and Global Capability Centres (GCCs).",
      "Remittance inflows exceeded $120 billion, with India retaining its position as the world's largest recipient of overseas remittances."],
     "GS-3: Balance of Payments, Current vs Capital Account, Services Exports, Inward Remittances, Global Capability Centres.",
     [
         ("Which of the following items is included in the Current Account of India's Balance of Payments?\n1. Merchandise trade (exports and imports)\n2. Software services receipts\n3. Remittances by non-resident Indians\n4. Foreign Direct Investment (FDI)\nSelect the correct answer:",
          ["(a) 1, 2 and 3 only", "(b) 1 and 4 only", "(c) 2, 3 and 4 only", "(d) 1, 2, 3 and 4"],
          "(a)", "FDI, FPI, and external commercial borrowings belong to the Capital Account. Trade in goods, services, income, and unilateral transfers (remittances) form the Current Account."),
         ("In balance of payments accounting, 'Invisibles' comprise:\n(a) Smuggled contraband goods\n(b) Services, transfers (remittances/grants), and factor income (interest/dividends)\n(c) Defense capital expenditure\n(d) Trade conducted through darknet platforms",
          ["(a) Smuggled contraband goods", "(b) Services, transfers (remittances/grants), and factor income (interest/dividends)", "(c) Defense capital expenditure", "(d) Trade conducted through darknet platforms"],
          "(b)", "Invisibles in the current account consist of non-merchandise transactions: services (IT, travel, transport), transfers (gifts, remittances), and income flows."),
         ("According to the World Bank's Migration and Development Brief, which country is the world's top recipient of external remittances?\n(a) China\n(b) Mexico\n(c) India\n(d) Philippines",
          ["(a) China", "(b) Mexico", "(c) India", "(d) Philippines"],
          "(c)", "India is the world's largest recipient of remittances, surpassing $120 billion annually, with substantial flows from North America, UK, and the Gulf."),
         ("A country running a persistent Current Account Deficit must finance it through:\n(a) An equivalent surplus on its Capital Account or drawing down forex reserves\n(b) Printing fiat currency exclusively\n(c) Imposing domestic export bans\n(d) Increasing domestic statutory minimum wages",
          ["(a) An equivalent surplus on its Capital Account or drawing down forex reserves", "(b) Printing fiat currency exclusively", "(c) Imposing domestic export bans", "(d) Increasing domestic statutory minimum wages"],
          "(a)", "By BoP identity (Current Account + Capital Account + Changes in Reserves = 0), a CAD must be financed by capital inflows (FDI/FPI/loans) or by drawing down reserves."),
         ("The phenomenon of 'Twin Deficits' in macroeconomics refers to the simultaneous existence of:\n(a) Trade Deficit and Revenue Deficit\n(b) High Fiscal Deficit and high Current Account Deficit\n(c) Primary Deficit and Monetised Deficit\n(d) Capital Account Deficit and Liquidity Deficit",
          ["(a) Trade Deficit and Revenue Deficit", "(b) High Fiscal Deficit and high Current Account Deficit", "(c) Primary Deficit and Monetised Deficit", "(d) Capital Account Deficit and Liquidity Deficit"],
          "(b)", "The Twin Deficit hypothesis posits that high government fiscal deficits drive up consumption and imports, spilling over into a wide Current Account Deficit.")
     ]),

    ("ca-eco-14", "2026-04-28", "Economy", "Minimum Support Price (MSP) Formulas: Swaminathan Commission & C2 vs A2+FL", "Ministry of Agriculture / Indian Express", True, True,
     ["Government fixes MSP for 22 mandated agricultural crops and Fair & Remunerative Price (FRP) for sugarcane based on CACP recommendations.",
      "Existing MSP formula guarantees at least 50% profit over 'A2+FL' cost (all paid-out expenses plus imputed value of family labour).",
      "Farmers' demand centers on statutory guarantee of MSP calculated on 'C2' cost (comprehensive cost including rental value of owned land and interest on capital)."],
     "GS-3: Agriculture, Pricing Policy, CACP, Swaminathan Committee, Farm Income & Subsidies.",
     [
         ("Which statutory/advisory body recommends the Minimum Support Prices (MSP) to the Central Government?\n(a) NITI Aayog\n(b) Commission for Agricultural Costs and Prices (CACP)\n(c) National Farmers Commission\n(d) Food Corporation of India",
          ["(a) NITI Aayog", "(b) Commission for Agricultural Costs and Prices (CACP)", "(c) National Farmers Commission", "(d) Food Corporation of India"],
          "(b)", "The Commission for Agricultural Costs and Prices (CACP), an attached office of the Ministry of Agriculture, recommends MSPs. The Cabinet Committee on Economic Affairs (CCEA) approves them."),
         ("In agricultural cost terminology used by CACP, what does 'A2+FL' cost include?\n(a) Only seeds and chemical fertilizers\n(b) All paid-out costs on inputs, hired labor, fuels, irrigation plus the imputed value of unpaid family labor\n(c) Comprehensive cost including rental value of owned land and interest on owned capital\n(d) Only the market transportation charges to mandis",
          ["(a) Only seeds and chemical fertilizers", "(b) All paid-out costs on inputs, hired labor, fuels, irrigation plus the imputed value of unpaid family labor", "(c) Comprehensive cost including rental value of owned land and interest on owned capital", "(d) Only the market transportation charges to mandis"],
          "(b)", "Cost A2 covers all paid-out expenses incurred by the farmer. A2+FL adds the imputed value of family labor. C2 is comprehensive cost (A2+FL + land rent + capital interest)."),
         ("The National Commission on Farmers chaired by Prof. M.S. Swaminathan recommended that MSP should be at least:\n(a) 25% above A2 cost\n(b) 50% above the weighted average Cost of Production (C2)\n(c) Equal to international benchmark market prices\n(d) 100% above input expenditure",
          ["(a) 25% above A2 cost", "(b) 50% above the weighted average Cost of Production (C2)", "(c) Equal to international benchmark market prices", "(d) 100% above input expenditure"],
          "(b)", "The Swaminathan Commission report (2006) famously recommended fixing MSP at least 50% more than the comprehensive cost of production (C2)."),
         ("For sugarcane, instead of MSP, the Central Government announces:\n(a) Minimum Export Price (MEP)\n(b) Fair and Remunerative Price (FRP)\n(c) Statutory Maximum Retail Price\n(d) Procurement Buffer Price",
          ["(a) Minimum Export Price (MEP)", "(b) Fair and Remunerative Price (FRP)", "(c) Statutory Maximum Retail Price", "(d) Procurement Buffer Price"],
          "(b)", "Under the Sugarcane (Control) Order 1966, the Union Government fixes the Fair and Remunerative Price (FRP) that sugar mills are legally obligated to pay cane growers."),
         ("How many agricultural crops are covered under the formal Minimum Support Price (MSP) announcements each year?\n(a) 15 crops\n(b) 22 mandated crops (plus FRP for sugarcane)\n(c) 50 crops\n(d) All agricultural commodities grown in India",
          ["(a) 15 crops", "(b) 22 mandated crops (plus FRP for sugarcane)", "(c) 50 crops", "(d) All agricultural commodities grown in India"],
          "(b)", "CACP recommends MSPs for 22 mandated crops (7 cereals, 5 pulses, 7 oilseeds, 3 commercial crops) plus FRP for sugarcane.")
     ]),

    ("ca-eco-15", "2026-03-12", "Economy", "National Monetisation Pipeline (NMP) & Capital Expenditure (Capex) Strategy", "NITI Aayog / MoF", False, True,
     ["National Monetisation Pipeline (NMP) seeks to monetize core infrastructure assets worth Rs 6 lakh crore without transferring ownership (lease/concession models).",
      "Top sectors comprise Roads (NHAI InvITs), Railways, Power Transmission (PowerGrid InvIT), and Oil & Gas pipelines.",
      "Proceeds are recycled directly to finance new greenfield infrastructure under the National Infrastructure Pipeline (NIP)."],
     "GS-3: Infrastructure Financing, Public-Private Partnerships (PPP), InvITs and REITs, Asset Monetisation.",
     [
         ("The core operational philosophy behind the National Monetisation Pipeline (NMP) is:\n(a) Outright sale and privatization of state-owned land assets\n(b) Leasing brownfield, de-risked revenue-generating public infrastructure assets to private operators while retaining public ownership\n(c) Shutting down non-profitable public enterprises\n(d) Sovereign borrowing from foreign commercial banks",
          ["(a) Outright sale and privatization of state-owned land assets", "(b) Leasing brownfield, de-risked revenue-generating public infrastructure assets to private operators while retaining public ownership", "(c) Shutting down non-profitable public enterprises", "(d) Sovereign borrowing from foreign commercial banks"],
          "(b)", "NMP emphasizes monetisation of rights, not ownership. Public assets remain government property and return to the state at the end of concession periods."),
         ("Which two sectors account for more than 50% of the total target value under the National Monetisation Pipeline?\n(a) Telecom and Civil Aviation\n(b) Roads and Railways\n(c) Power and Mining\n(d) Ports and Warehousing",
          ["(a) Telecom and Civil Aviation", "(b) Roads and Railways", "(c) Power and Mining", "(d) Ports and Warehousing"],
          "(b)", "Roads (27%) and Railways (25%) constitute the bulk of the NMP asset base, followed by Power (15%) and Oil/Gas pipelines (8%)."),
         ("What financial vehicle enables retail and institutional investors to pool funds and invest directly in income-generating infrastructure projects?\n(a) Infrastructure Investment Trusts (InvITs)\n(b) Credit Default Swaps (CDS)\n(c) Participatory Notes (P-Notes)\n(d) Masala Bonds",
          ["(a) Infrastructure Investment Trusts (InvITs)", "(b) Credit Default Swaps (CDS)", "(c) Participatory Notes (P-Notes)", "(d) Masala Bonds"],
          "(a)", "InvITs are mutual fund-like collective investment vehicles regulated by SEBI that own operational infrastructure assets and pass regular cash flows as dividends/interest."),
         ("What is the crucial difference between greenfield and brownfield infrastructure investments?\n(a) Greenfield involves high environmental risk, while brownfield involves low environmental risk\n(b) Greenfield involves building entirely new assets from scratch; brownfield involves expanding or monetizing existing operating assets\n(c) Greenfield applies only to agriculture; brownfield applies to heavy manufacturing\n(d) Brownfield is exclusively financed by foreign equity",
          ["(a) Greenfield involves high environmental risk, while brownfield involves low environmental risk", "(b) Greenfield involves building entirely new assets from scratch; brownfield involves expanding or monetizing existing operating assets", "(c) Greenfield applies only to agriculture; brownfield applies to heavy manufacturing", "(d) Brownfield is exclusively financed by foreign equity"],
          "(b)", "Greenfield projects carry land acquisition and construction execution risks; brownfield assets are already built, de-risked, and generating operating cash flows."),
         ("Which government portal acts as the single-window digital mapping platform integrating multi-modal infrastructure planning across ministries?\n(a) PM Gati Shakti National Master Plan\n(b) PRAGATI Portal\n(c) DARPAN Dashboard\n(d) UMANG Platform",
          ["(a) PM Gati Shakti National Master Plan", "(b) PRAGATI Portal", "(c) DARPAN Dashboard", "(d) UMANG Platform"],
          "(a)", "PM Gati Shakti uses GIS-based spatial planning by Bhaskaracharya National Institute for Space Applications and Geo-informatics (BISAG-N) to coordinate infrastructure projects.")
     ]),

    ("ca-eco-16", "2026-02-14", "Economy", "SEBI's Regulatory Framework for ESG Ratings & Mutual Fund Greenwashing", "SEBI / Livemint", True, False,
     ["SEBI mandated that Environmental, Social, and Governance (ESG) Rating Providers (ERPs) must be registered under SEBI (Credit Rating Agencies) Regulations.",
      "Introduced 'Core ESG Rating' based on assured parameters under the Business Responsibility and Sustainability Report (BRSR Core).",
      "Requires ESG mutual fund schemes to invest at least 65% of their AUM in companies reporting comprehensive BRSR Core assurance."],
     "GS-3: Financial Markets, Sustainable Investing, Greenwashing Prevention, Corporate Governance, SEBI Regulations.",
     [
         ("The term 'Greenwashing' in corporate finance and investment funds refers to:\n(a) Promoting biological cleaning of wastewater\n(b) Deceptively presenting products, policies, or investments as environmentally friendly when they are not\n(c) Planting trees on industrial premises\n(d) Zero-tariff trade on agricultural goods",
          ["(a) Promoting biological cleaning of wastewater", "(b) Deceptively presenting products, policies, or investments as environmentally friendly when they are not", "(c) Planting trees on industrial premises", "(d) Zero-tariff trade on agricultural goods"],
          "(b)", "Greenwashing involves making misleading or unsubstantiated claims regarding the environmental credentials of a company, bond, or fund."),
         ("What is the mandatory sustainability reporting framework for top 1000 listed entities by market capitalization in India?\n(a) Corporate Social Responsibility (CSR) Filing\n(b) Business Responsibility and Sustainability Report (BRSR)\n(c) Kyoto Protocol National Disclosure\n(d) ISO 14001 Environmental Audit",
          ["(a) Corporate Social Responsibility (CSR) Filing", "(b) Business Responsibility and Sustainability Report (BRSR)", "(c) Kyoto Protocol National Disclosure", "(d) ISO 14001 Environmental Audit"],
          "(b)", "SEBI mandated the Business Responsibility and Sustainability Report (BRSR) to replace the older Business Responsibility Report (BRR) for ESG disclosures."),
         ("Under SEBI regulations, ESG Mutual Fund schemes in India are permitted to launch strategies under which of the following categories?\n1. Exclusion strategies\n2. Integration strategies\n3. Impact investing\n4. Transition or transition-related strategies\nSelect the correct answer:",
          ["(a) 1 and 2 only", "(b) 3 and 4 only", "(c) 1, 2, 3 and 4", "(d) 2 and 4 only"],
          "(c)", "SEBI permits 6 defined ESG strategies: Exclusion, Integration, Best-in-class, Positive Screening, Impact Investing, and Sustainable/Transition."),
         ("Under Section 135 of the Companies Act 2013, what percentage of average net profits must qualifying companies spend on CSR activities?\n(a) 1%\n(b) 2%\n(c) 3%\n(d) 5%",
          ["(a) 1%", "(b) 2%", "(c) 3%", "(d) 5%"],
          "(b)", "Qualifying companies (net worth Rs 500 cr+, turnover Rs 1000 cr+, or net profit Rs 5 cr+) must spend at least 2% of average net profits of preceding three years on CSR."),
         ("Who regulates ESG Rating Providers (ERPs) in Indian financial markets?\n(a) Ministry of Environment, Forest and Climate Change\n(b) Securities and Exchange Board of India (SEBI)\n(c) Reserve Bank of India\n(d) Bureau of Energy Efficiency",
          ["(a) Ministry of Environment, Forest and Climate Change", "(b) Securities and Exchange Board of India (SEBI)", "(c) Reserve Bank of India", "(d) Bureau of Energy Efficiency"],
          "(b)", "SEBI amended the Credit Rating Agencies Regulations in 2023 to bring ESG Rating Providers under formal statutory licensing and oversight.")
     ]),

    ("ca-eco-17", "2026-01-24", "Economy", "Central Bank Monetary Policy Transmission & Bank Lending Benchmarks", "RBI Bulletin", False, True,
     ["External Benchmark Lending Rate (EBLR) framework links floating rate loans for retail and MSMEs to external benchmarks like the Repo Rate or T-Bill yields.",
      "Replaced the Marginal Cost of Funds based Lending Rate (MCLR) system to ensure faster, symmetrical monetary policy transmission.",
      "RBI observed that lending rates adjust faster during repo rate hiking cycles than deposit rates, prompting scrutiny of NIM spreads."],
     "GS-3: Monetary Policy, Banking Sector Reforms, Repo Rate, Transmission Mechanism, MCLR vs EBLR.",
     [
         ("Which external benchmark is most widely adopted by Indian commercial banks for floating-rate personal and housing loans under RBI norms?\n(a) US Federal Reserve Funds Rate\n(b) RBI's Policy Repo Rate\n(c) 10-year Indian Sovereign Bond Yield\n(d) State Bank of India Base Rate",
          ["(a) US Federal Reserve Funds Rate", "(b) RBI's Policy Repo Rate", "(c) 10-year Indian Sovereign Bond Yield", "(d) State Bank of India Base Rate"],
          "(b)", "Most banks adopt the RBI Repo Rate as the external benchmark under the mandatory EBLR framework introduced in October 2019."),
         ("The Marginal Cost of Funds based Lending Rate (MCLR) was introduced by RBI primarily to replace which older system?\n(a) Prime Lending Rate (BPLR) and Base Rate system\n(b) Reverse Repo Corridor\n(c) Statutory Liquidity Ratio\n(d) Cash Reserve Ratio",
          ["(a) Prime Lending Rate (BPLR) and Base Rate system", "(b) Reverse Repo Corridor", "(c) Statutory Liquidity Ratio", "(d) Cash Reserve Ratio"],
          "(a)", "MCLR was introduced in 2016 to replace the opaque Base Rate system, tying minimum lending rates to marginal funding costs of banks."),
         ("What does the 'Net Interest Margin' (NIM) of a commercial bank represent?\n(a) The total fee income earned from digital payment transactions\n(b) The difference between interest income earned on loans and interest paid on deposits relative to total interest-earning assets\n(c) The ratio of gross NPAs to net advances\n(d) The statutory tax paid by public sector banks",
          ["(a) The total fee income earned from digital payment transactions", "(b) The difference between interest income earned on loans and interest paid on deposits relative to total interest-earning assets", "(c) The ratio of gross NPAs to net advances", "(d) The statutory tax paid by public sector banks"],
          "(b)", "NIM is a core profitability metric: (Interest Income - Interest Expended) / Total Interest-Earning Assets."),
         ("In monetary economics, 'Liquidity Trap' refers to a situation where:\n(a) Banks have zero deposits to lend\n(b) Interest rates are so low that people prefer holding cash, making monetary policy ineffective in stimulating investment\n(c) RBI refuses to lend to the Central Government\n(d) Inflation reaches hyperinflation levels above 100%",
          ["(a) Banks have zero deposits to lend", "(b) Interest rates are so low that people prefer holding cash, making monetary policy ineffective in stimulating investment", "(c) RBI refuses to lend to the Central Government", "(d) Inflation reaches hyperinflation levels above 100%"],
          "(b)", "Keynesian liquidity trap occurs when monetary easing fails because interest rates near zero cause cash demand to become infinitely elastic."),
         ("Which statutory committee determines the policy repo rate under Section 45ZB of the RBI Act 1934?\n(a) Board for Financial Supervision\n(b) Monetary Policy Committee (MPC)\n(c) Financial Stability and Development Council\n(d) Central Board of the RBI",
          ["(a) Board for Financial Supervision", "(b) Monetary Policy Committee (MPC)", "(c) Financial Stability and Development Council", "(d) Central Board of the RBI"],
          "(b)", "The 6-member Monetary Policy Committee (3 internal RBI officials, 3 external government-appointed experts) sets the repo rate to achieve the 4% (+/- 2%) inflation target.")
     ]),

    ("ca-eco-18", "2026-10-30", "Economy", "Direct Benefit Transfer (DBT) & JAM Trinity: 10-Year Macroeconomic Audit", "DBT Mission / World Bank", True, True,
     ["Direct Benefit Transfer (DBT) cumulative transfers crossed Rs 38 lakh crore, eliminating over Rs 3 lakh crore in ghost beneficiaries and leakages.",
      "Enabled by the JAM Trinity (Jan Dhan accounts, Aadhaar digital identity, Mobile connectivity) and the Aadhaar Payment Bridge System (APBS).",
      "Covers 310+ schemes across 53 ministries, with major welfare programs including PM-KISAN, PAHAL (LPG), and MGNREGA wages."],
     "GS-3: Financial Inclusion, Welfare Delivery, Subsidy Reforms, Public Finance Management, Anti-Poverty Interventions.",
     [
         ("The core technological backbone facilitating wage and welfare payments under the Direct Benefit Transfer (DBT) is:\n(a) SWIFT Messaging System\n(b) Aadhaar Payment Bridge System (APBS) managed by NPCI\n(c) Real Time Gross Settlement (RTGS)\n(d) Hawala Clearance Network",
          ["(a) SWIFT Messaging System", "(b) Aadhaar Payment Bridge System (APBS) managed by NPCI", "(c) Real Time Gross Settlement (RTGS)", "(d) Hawala Clearance Network"],
          "(b)", "NPCI's Aadhaar Payment Bridge System routes subsidies directly into beneficiary bank accounts using the Aadhaar number as a central financial address."),
         ("Under the Pradhan Mantri Jan Dhan Yojana (PMJDY), what is the key insurance feature provided on RuPay debit cards?\n(a) Comprehensive crop insurance\n(b) Accidental death and disability insurance cover of up to Rs 2 lakh\n(c) Fire insurance for residential premises\n(d) Health insurance for international travel",
          ["(a) Comprehensive crop insurance", "(b) Accidental death and disability insurance cover of up to Rs 2 lakh", "(c) Fire insurance for residential premises", "(d) Health insurance for international travel"],
          "(b)", "PMJDY account holders receive a RuPay debit card with inbuilt accidental insurance cover (raised from Rs 1 lakh to Rs 2 lakh for accounts opened after Aug 2018)."),
         ("Which scheme was recognized by Guinness World Records as the world's largest direct cash transfer program?\n(a) PM-KISAN\n(b) PAHAL (DBTL) scheme for LPG subsidies\n(c) Ayushman Bharat PM-JAY\n(d) PM Awas Yojana",
          ["(a) PM-KISAN", "(b) PAHAL (DBTL) scheme for LPG subsidies", "(c) Ayushman Bharat PM-JAY", "(d) PM Awas Yojana"],
          "(b)", "PAHAL (Pratyaksh Hanstantrit Labh) for LPG cylinder subsidies was verified by Guinness World Records as the largest cash transfer program."),
         ("What is the primary statutory basis under which government can mandate Aadhaar authentication for receipt of state subsidies?\n(a) Section 7 of the Aadhaar Act 2016\n(b) Article 370 of the Constitution\n(c) Section 144 of the CrPC\n(d) Information Technology Act 2000",
          ["(a) Section 7 of the Aadhaar Act 2016", "(b) Article 370 of the Constitution", "(c) Section 144 of the CrPC", "(d) Information Technology Act 2000"],
          "(a)", "Section 7 of the Aadhaar Act allows the Central or State government to require Aadhaar authentication for benefits funded out of the Consolidated Fund of India."),
         ("Which government IT platform integrates all financial flows and accounting of welfare schemes from the Centre to the end vendor?\n(a) Public Financial Management System (PFMS)\n(b) Government e-Marketplace (GeM)\n(c) PRAGATI Platform\n(d) MCA21 Portal",
          ["(a) Public Financial Management System (PFMS)", "(b) Government e-Marketplace (GeM)", "(c) PRAGATI Platform", "(d) MCA21 Portal"],
          "(a)", "PFMS administered by the Controller General of Accounts (CGA) tracks real-time expenditure and integrates banking gateways for DBT disbursement.")
     ])
]

for aid, dt, pil, tit, src, top, pt, sums, gs, qs in eco_new:
    master_articles.append(build_art(aid, dt, pil, tit, src, top, pt, sums, gs, qs))

print(f"Total Economy articles now in master: {len([a for a in master_articles if a['pillar'] == 'Economy'])}")

# Write progress to a check file
with open(os.path.join(BASE_DIR, 'data', 'ca_builders', 'master_progress.json'), 'w') as f:
    json.dump(master_articles, f, indent=2)
print("Saved master progress with Polity (18) and Economy (18)!")
