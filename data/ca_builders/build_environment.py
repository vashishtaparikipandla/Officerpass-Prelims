#!/usr/bin/env python3
"""
Builds Environment & Ecology articles (ca-env-01 to ca-env-16: total 16 articles)
"""
import json
import os

BASE_DIR = '/Users/vashishtaparikipandla/Documents/OfficerPass'
with open(os.path.join(BASE_DIR, 'data', 'current-affairs-db.json')) as f:
    existing = json.load(f)

env1_2 = [a for a in existing if a['pillar'] == 'Environment']

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

env_new = [
    ("ca-env-03", "2026-10-12", "Environment", "Loss and Damage Fund Operationalisation at COP28 / COP29", "UNFCCC / Down to Earth", True, True,
     ["The Loss and Damage Fund was officially launched to assist developing nations particularly vulnerable to adverse effects of climate change.",
      "The World Bank acts as interim financial trustee and host of the Fund for an initial period of four years.",
      "Rooted in the principle of Common But Differentiated Responsibilities and Respective Capabilities (CBDR-RC) under UNFCCC."],
     "GS-3: Climate Change Treaties, COP Negotiations, Climate Justice, Loss & Damage, CBDR-RC.",
     [
         ("The Loss and Damage Fund for climate-vulnerable developing countries was operationalized at which UNFCCC COP summit?\n(a) COP21 Paris\n(b) COP26 Glasgow\n(c) COP27 Sharm el-Sheikh / COP28 Dubai\n(d) COP15 Copenhagen",
          ["(a) COP21 Paris", "(b) COP26 Glasgow", "(c) COP27 Sharm el-Sheikh / COP28 Dubai", "(d) COP15 Copenhagen"],
          "(c)", "The agreement to establish the Fund was struck at COP27 (2022) in Sharm el-Sheikh and operationalized with funding pledges at COP28 (2023) in Dubai."),
         ("Which international financial institution was selected to host the Loss and Damage Fund on an interim basis for 4 years?\n(a) Asian Development Bank\n(b) World Bank\n(c) New Development Bank\n(d) International Monetary Fund",
          ["(a) Asian Development Bank", "(b) World Bank", "(c) New Development Bank", "(d) International Monetary Fund"],
          "(b)", "The World Bank was designated as the interim trustee and host secretariat for a 4-year term despite initial concerns from developing nations regarding overhead costs."),
         ("What is the core distinction between 'Climate Adaptation' and 'Loss and Damage'?\n(a) Adaptation refers to cutting emissions; Loss and Damage refers to carbon sinks\n(b) Adaptation involves adjustments to anticipate climate impacts; Loss and Damage deals with unavoidable residual climate damages that cannot be adapted to\n(c) There is no distinction in UNFCCC terminology\n(d) Adaptation applies only to developed nations",
          ["(a) Adaptation refers to cutting emissions; Loss and Damage refers to carbon sinks", "(b) Adaptation involves adjustments to anticipate climate impacts; Loss and Damage deals with unavoidable residual climate damages that cannot be adapted to", "(c) There is no distinction in UNFCCC terminology", "(d) Adaptation applies only to developed nations"],
          "(b)", "Mitigation curbs emissions; adaptation builds resilience against future impacts; loss and damage covers residual, irreversible harms (sea level rise, desertification, extreme cyclones)."),
         ("The Warsaw International Mechanism (WIM) established in 2013 under COP19 primarily addresses:\n(a) Nuclear non-proliferation\n(b) Loss and damage associated with climate change impacts in developing countries\n(c) Maritime piracy in the Baltic Sea\n(d) Carbon trading in forestry offsets",
          ["(a) Nuclear non-proliferation", "(b) Loss and damage associated with climate change impacts in developing countries", "(c) Maritime piracy in the Baltic Sea", "(d) Carbon trading in forestry offsets"],
          "(b)", "The WIM was created at COP19 in Warsaw to promote approaches to address loss and damage associated with extreme events and slow-onset events in vulnerable developing nations."),
         ("Are financial contributions to the Loss and Damage Fund legally binding on developed nations under the Paris Agreement?\n(a) Yes, mandatory annual contributions based on GDP quotas\n(b) No, contributions are voluntary and non-compensatory (without legal liability)\n(c) Enforced via UN Security Council sanctions\n(d) Deducted automatically from IMF SDR allocations",
          ["(a) Yes, mandatory annual contributions based on GDP quotas", "(b) No, contributions are voluntary and non-compensatory (without legal liability)", "(c) Enforced via UN Security Council sanctions", "(d) Deducted automatically from IMF SDR allocations"],
          "(b)", "Paragraph 51 of the COP21 Paris Decision explicitly notes that Article 8 does not involve or provide a basis for any liability or compensation, making contributions voluntary.")
     ]),

    ("ca-env-04", "2026-09-05", "Environment", "India's Ramsar Sites Network & Montreux Record Conservation Status", "MoEFCC / PIB", True, True,
     ["India expanded its network of Ramsar Wetlands of International Importance, taking the national total to 85+ sites across states.",
      "The Montreux Record is a register of wetland sites on the Ramsar List where changes in ecological character have occurred, are occurring, or are likely to occur.",
      "Currently, only two Indian wetlands are listed on the Montreux Record: Keoladeo National Park (Rajasthan) and Loktak Lake (Manipur)."],
     "GS-3: Biodiversity, Wetlands Conservation, Ramsar Convention 1971, Montreux Record, Aquatic Ecology.",
     [
         ("Which of the following wetlands in India are currently placed on the Montreux Record?\n1. Chilika Lake (Odisha)\n2. Keoladeo National Park (Rajasthan)\n3. Loktak Lake (Manipur)\nSelect the correct answer using the code below:",
          ["(a) 1 and 2 only", "(b) 2 and 3 only", "(c) 1 and 3 only", "(d) 1, 2 and 3"],
          "(b)", "Chilika Lake was successfully removed from the Montreux Record in 2002 after ecological restoration. Only Keoladeo and Loktak Lake remain on the record."),
         ("What is the primary characteristic feature of Loktak Lake in Manipur?\n(a) Hot volcanic sulfur springs\n(b) Floating vegetative biomass islands known as 'Phumdis'\n(c) Subterranean limestone caves\n(d) Hyper-saline salt flats",
          ["(a) Hot volcanic sulfur springs", "(b) Floating vegetative biomass islands known as 'Phumdis'", "(c) Subterranean limestone caves", "(d) Hyper-saline salt flats"],
          "(b)", "Loktak Lake is famous for its Phumdis (heterogeneous floating masses of vegetation, soil, and organic matter) and hosts Keibul Lamjao, the world's only floating national park."),
         ("Under the Ramsar Convention, which was the first wetland site designated from India in 1981?\n(a) Sundarbans\n(b) Chilika Lake and Keoladeo National Park\n(c) Wular Lake\n(d) Vembanad-Kol wetland",
          ["(a) Sundarbans", "(b) Chilika Lake and Keoladeo National Park", "(c) Wular Lake", "(d) Vembanad-Kol wetland"],
          "(b)", "Chilika Lake (Odisha) and Keoladeo National Park (Rajasthan) were the first two wetlands in India to be designated as Ramsar sites in 1981."),
         ("Which state in India possesses the highest number of Ramsar designated wetlands?\n(a) Uttar Pradesh\n(b) Tamil Nadu\n(c) Kerala\n(d) Odisha",
          ["(a) Uttar Pradesh", "(b) Tamil Nadu", "(c) Kerala", "(d) Odisha"],
          "(b)", "Tamil Nadu leads all Indian states with the largest number of designated Ramsar wetlands (16+ sites), followed closely by Uttar Pradesh."),
         ("What is the theme of World Wetlands Day celebrated annually on February 2nd?\n(a) Commemorates the adoption of the Ramsar Convention in 1971 in Ramsar, Iran\n(b) Marks the signing of the Stockholm Declaration\n(c) Commemorates the Rio Earth Summit\n(d) Celebrates the establishment of the Central Wetland Regulatory Authority",
          ["(a) Commemorates the adoption of the Ramsar Convention in 1971 in Ramsar, Iran", "(b) Marks the signing of the Stockholm Declaration", "(c) Commemorates the Rio Earth Summit", "(d) Celebrates the establishment of the Central Wetland Regulatory Authority"],
          "(a)", "World Wetlands Day marks the date of adoption of the Convention on Wetlands on February 2, 1971 in the Iranian city of Ramsar on the shores of the Caspian Sea.")
     ]),

    ("ca-env-05", "2026-08-16", "Environment", "Project Cheetah at Kuno National Park & Gandhi Sagar Sanctuary Expansion", "NTCA / PIB", True, True,
     ["Cheetah reintroduction under Action Plan for Introduction of Cheetah in India aims to establish free-ranging metapopulation of Asiatic/African cheetahs.",
      "Gandhi Sagar Wildlife Sanctuary (Madhya Pradesh) and Nauradehi Sanctuary prepared as second and third habitats to mitigate carrying capacity pressure at Kuno.",
      "Asiatic Cheetah (Acinonyx jubatus venaticus) is critically endangered with surviving wild populations restricted entirely to Iran."],
     "GS-3: Wildlife Conservation, In-situ Conservation, Species Reintroduction, NTCA, WPA 1972.",
     [
         ("The cheetah was declared officially extinct in India in which year?\n(a) 1947\n(b) 1952\n(c) 1972\n(d) 1985",
          ["(a) 1947", "(b) 1952", "(c) 1972", "(d) 1985"],
          "(b)", "The cheetah was officially declared extinct in India in 1952 following the shooting of the last recorded three Asiatic cheetahs in Korea (Chhattisgarh) in 1947."),
         ("Which wildlife sanctuary in Madhya Pradesh has been developed as the second home for translocated African cheetahs after Kuno National Park?\n(a) Gandhi Sagar Wildlife Sanctuary\n(b) Bandhavgarh National Park\n(c) Kanha National Park\n(d) Satpura Tiger Reserve",
          ["(a) Gandhi Sagar Wildlife Sanctuary", "(b) Bandhavgarh National Park", "(c) Kanha National Park", "(d) Satpura Tiger Reserve"],
          "(a)", "Gandhi Sagar Wildlife Sanctuary in Mandsaur/Neemuch districts of MP has been developed with predator-proof enclosures as the second cheetah site."),
         ("Consider the following statements regarding the Cheetah:\n1. The Asiatic Cheetah is classified as 'Critically Endangered' on the IUCN Red List.\n2. The African Cheetah translocated to India is classified as 'Vulnerable'.\n3. Cheetahs are solitary animals and never form coalitions.\nWhich of the statements given above is/are correct?",
          ["(a) 1 and 2 only", "(b) 2 and 3 only", "(c) 1 and 3 only", "(d) 1, 2 and 3"],
          "(a)", "Statement 3 is incorrect. Male cheetahs often form permanent social groups called 'coalitions' (usually brothers) to defend territory."),
         ("Which statutory body under the Ministry of Environment is the nodal implementing agency for Project Cheetah?\n(a) Wildlife Institute of India (WII)\n(b) National Tiger Conservation Authority (NTCA)\n(c) Central Zoo Authority (CZA)\n(d) Animal Welfare Board of India",
          ["(a) Wildlife Institute of India (WII)", "(b) National Tiger Conservation Authority (NTCA)", "(c) Central Zoo Authority (CZA)", "(d) Animal Welfare Board of India"],
          "(b)", "The NTCA (constituted under the Wildlife Protection Act 1972) is the nodal statutory authority overseeing Project Tiger and Project Cheetah."),
         ("Which river flows through Kuno National Park, serving as its primary lifeline?\n(a) Chambal River\n(b) Kuno River\n(c) Betwa River\n(d) Ken River",
          ["(a) Chambal River", "(b) Kuno River", "(c) Betwa River", "(d) Ken River"],
          "(b)", "The Kuno River, a major tributary of the Chambal River, flows north-south through the middle of Kuno National Park.")
     ]),

    ("ca-env-06", "2026-07-11", "Environment", "Great Indian Bustard (GIB) Conservation & SC Overhead Power Line Mandate", "The Hindu / Down to Earth", True, True,
     ["Supreme Court modified its blanket undergrounding order in MK Ranjitsinh (2024), balancing biodiversity with India's international climate commitments.",
      "Expert committee constituted to demarcate priority and potential GIB habitats across Rajasthan (Thar Desert) and Gujarat (Kutch).",
      "GIB (Ardeotis nigriceps) is Critically Endangered, listed under Schedule I of WPA 1972 and Appendix I of CMS and CITES, with poor frontal vision causing collisions with power lines."],
     "GS-3: Endangered Species, Renewable Energy vs Wildlife Conflict, Ecological Jurisprudence, WPA 1972.",
     [
         ("The Great Indian Bustard (Ardeotis nigriceps) is the state bird of which Indian state?\n(a) Gujarat\n(b) Rajasthan\n(c) Madhya Pradesh\n(d) Maharashtra",
          ["(a) Gujarat", "(b) Rajasthan", "(c) Madhya Pradesh", "(d) Maharashtra"],
          "(b)", "The Great Indian Bustard (locally known as Godawan) is the official state bird of Rajasthan."),
         ("What physiological limitation makes the Great Indian Bustard uniquely vulnerable to fatal collisions with overhead electric transmission lines?\n(a) Heavy body weight combined with narrow frontal binocular field of vision\n(b) Complete nocturnal blindness\n(c) Attraction to electromagnetic radiation\n(d) Inability to fly above 10 feet",
          ["(a) Heavy body weight combined with narrow frontal binocular field of vision", "(b) Complete nocturnal blindness", "(c) Attraction to electromagnetic radiation", "(d) Inability to fly above 10 feet"],
          "(a)", "GIBs are heavy fliers with poor frontal vision; they scan downwards while foraging, making it impossible to detect thin overhead power cables until too close to maneuver."),
         ("What mechanical device is installed on power transmission cables to alert and divert approaching bustards?\n(a) Bird diverters / reflective flappers\n(b) High-decibel acoustic sirens\n(c) Infrared laser fences\n(d) Magnetic repellers",
          ["(a) Bird diverters / reflective flappers", "(b) High-decibel acoustic sirens", "(c) Infrared laser fences", "(d) Magnetic repellers"],
          "(b)", "Firefly bird flight diverters are reflective, glow-in-the-dark discs installed on cables that spin in the wind and warn birds from a distance."),
         ("What is the conservation status of the Great Indian Bustard on the IUCN Red List of Threatened Species?\n(a) Vulnerable\n(b) Endangered\n(c) Critically Endangered\n(d) Extinct in the Wild",
          ["(a) Vulnerable", "(b) Endangered", "(c) Critically Endangered", "(d) Extinct in the Wild"],
          "(c)", "The Great Indian Bustard is classified as 'Critically Endangered' with fewer than 150 mature individuals surviving in the wild, primarily in Thar Desert."),
         ("Which National Park in Rajasthan is the premier sanctuary protecting the core breeding population of GIB?\n(a) Ranthambore National Park\n(b) Desert National Park (Jaisalmer/Barmer)\n(c) Keoladeo Ghana National Park\n(d) Sariska National Park",
          ["(a) Ranthambore National Park", "(b) Desert National Park (Jaisalmer/Barmer)", "(c) Keoladeo Ghana National Park", "(d) Sariska National Park"],
          "(b)", "Desert National Park spanning Jaisalmer and Barmer contains the primary breeding enclosure and conservation breeding center for the GIB.")
     ]),

    ("ca-env-07", "2026-06-25", "Environment", "Glacial Lake Outburst Floods (GLOF) Vulnerability in the Himalayas", "NDMA / ISRO", True, True,
     ["South Lhonak glacial lake breach in Sikkim triggered catastrophic flash floods downstream along the Teesta River basin.",
      "GLOF occurs when water dammed by loose moraine or ice suddenly breaches due to avalanche, seismic activity, or intense rainfall.",
      "National Disaster Management Authority (NDMA) identified 188 high-risk glacial lakes across the Indian Himalayan Region for early warning sensor installation."],
     "GS-3: Disaster Management, Climate Change, Glaciology, Himalayan Ecology, Teesta Basin Floods.",
     [
         ("A Glacial Lake Outburst Flood (GLOF) is caused primarily by the sudden breach of:\n(a) Reinforced concrete dam walls\n(b) Natural moraine dams formed of loose rock, boulders, and ice debris\n(c) Underground karst aquifers\n(d) Man-made reservoir spillways",
          ["(a) Reinforced concrete dam walls", "(b) Natural moraine dams formed of loose rock, boulders, and ice debris", "(c) Underground karst aquifers", "(d) Man-made reservoir spillways"],
          "(b)", "Glacial lakes are impounded by unstable terminal or lateral moraines consisting of unconsolidated glacial till, gravel, and ice that fail easily under hydrostatic pressure."),
         ("The catastrophic GLOF disaster of October 2023 in Sikkim occurred at which high-altitude glacial lake?\n(a) Tsomgo Lake\n(b) Gurudongmar Lake\n(c) South Lhonak Lake\n(d) Khecheopalri Lake",
          ["(a) Tsomgo Lake", "(b) Gurudongmar Lake", "(c) South Lhonak Lake", "(d) Khecheopalri Lake"],
          "(c)", "The South Lhonak lake at ~5,200m in North Sikkim breached, washing away the Chungthang dam (Teesta-III hydro project) and causing massive downstream casualties."),
         ("Which major river basin in eastern India was devastated by the South Lhonak glacial lake breach?\n(a) Brahmaputra River\n(b) Teesta River\n(c) Manas River\n(d) Subansiri River",
          ["(a) Brahmaputra River", "(b) Teesta River", "(c) Manas River", "(d) Subansiri River"],
          "(b)", "The Teesta River basin (a major right-bank tributary of the Brahmaputra) was severely flooded, destroying infrastructure across Sikkim and northern West Bengal."),
         ("Which scientific engineering method is used to mitigate the risk of GLOF in vulnerable glacial lakes?\n(a) Siphoning and controlled pumping of lake water to lower lake depth and hydrostatic pressure\n(b) Chemical freezing of the moraine dam\n(c) Detonating dynamite in the moraine wall\n(d) Dumping plastic boulders in the lake",
          ["(a) Siphoning and controlled pumping of lake water to lower lake depth and hydrostatic pressure", "(b) Chemical freezing of the moraine dam", "(c) Detonating dynamite in the moraine wall", "(d) Dumping plastic boulders in the lake"],
          "(a)", "Controlled siphoning through HDPE pipes, spillway excavation, and structural drainage channels lower the water level, reducing bursting potential."),
         ("Under the Sendai Framework for Disaster Risk Reduction (2015-2030), what is Priority 1?\n(a) Investing in disaster risk reduction for resilience\n(b) Understanding disaster risk\n(c) Strengthening disaster risk governance\n(d) Enhancing disaster preparedness for effective response",
          ["(a) Investing in disaster risk reduction for resilience", "(b) Understanding disaster risk", "(c) Strengthening disaster risk governance", "(d) Enhancing disaster preparedness for effective response"],
          "(b)", "Priority 1 of the Sendai Framework is 'Understanding disaster risk' (including risk mapping and hazard assessment of glaciated basins).")
     ]),

    ("ca-env-08", "2026-05-12", "Environment", "Wildlife Protection Amendment Act 2022: Rationalization of Schedules", "MoEFCC / PRS", True, True,
     ["The Amendment reduced the number of schedules from six to four, streamlining regulatory compliance and aligning with CITES appendices.",
      "Schedule I provides the highest level of protection to endangered animal species; Schedule II protects species requiring lesser protection; Schedule III lists protected plants; Schedule IV lists species protected under CITES.",
      "Abolished Schedule V (which historically listed 'vermin' species like fruit bats, mice, and crows), empowering Central Government to declare specific animals as vermin by notification."],
     "GS-3: Environmental Law, Wildlife Conservation, CITES, Schedules Rationalization, Invasive Species.",
     [
         ("How many schedules does the Wildlife (Protection) Act, 1972 contain following the 2022 Amendment?\n(a) Six schedules\n(b) Four schedules\n(c) Three schedules\n(d) Five schedules",
          ["(a) Six schedules", "(b) Four schedules", "(c) Three schedules", "(d) Five schedules"],
          "(b)", "The 2022 amendment rationalized the older 6 schedules into 4 schedules: Schedule I (highest protection animals), Schedule II (other animals), Schedule III (plants), Schedule IV (CITES specimens)."),
         ("Under the amended Wildlife (Protection) Act, which schedule was omitted entirely?\n(a) Schedule I\n(b) Schedule III\n(c) Schedule V (Vermin Schedule)\n(d) Schedule VI",
          ["(a) Schedule I", "(b) Schedule III", "(c) Schedule V (Vermin Schedule)", "(d) Schedule VI"],
          "(c)", "The older Schedule V for vermin was omitted completely. The Central Government now declares vermin for specified areas and periods via notification under Section 62."),
         ("Which international wildlife convention was explicitly operationalized into domestic Indian law through Schedule IV of the 2022 Amendment?\n(a) Bonn Convention (CMS)\n(b) Convention on International Trade in Endangered Species of Wild Fauna and Flora (CITES)\n(c) Ramsar Convention\n(d) Convention on Biological Diversity (CBD)",
          ["(a) Bonn Convention (CMS)", "(b) Convention on International Trade in Endangered Species of Wild Fauna and Flora (CITES)", "(c) Ramsar Convention", "(d) Convention on Biological Diversity (CBD)"],
          "(b)", "Schedule IV incorporates specimens listed in Appendices I, II, and III of CITES, designating a Management Authority and Scientific Authority in India."),
         ("Under Section 43 of the amended Act, can live captive Asian Elephants be transferred or transported?\n(a) Completely banned under all circumstances\n(b) Permitted for religious or any other purpose under conditions prescribed by the Central Government\n(c) Allowed for commercial circus sales freely\n(d) Only permitted through international auction",
          ["(a) Completely banned under all circumstances", "(b) Permitted for religious or any other purpose under conditions prescribed by the Central Government", "(c) Allowed for commercial circus sales freely", "(d) Only permitted through international auction"],
          "(b)", "Section 43 was amended to provide an exception allowing transfer of captive elephants for religious or other purposes as prescribed by the Centre."),
         ("Which authority is established under the Act to advise the Central Government on policies and programs for conservation of wildlife?\n(a) National Board for Wildlife (NBWL)\n(b) Animal Welfare Council\n(c) Biodiversity Authority of India\n(d) Central Pollution Control Board",
          ["(a) National Board for Wildlife (NBWL)", "(b) Animal Welfare Council", "(c) Biodiversity Authority of India", "(d) Central Pollution Control Board"],
          "(a)", "The National Board for Wildlife (NBWL) is chaired by the Prime Minister and serves as the apex statutory advisory body under Section 5A of the Act.")
     ]),

    ("ca-env-09", "2026-04-18", "Environment", "Forest (Conservation) Amendment Act 2023 & Godavarman Jurisprudence", "MoEFCC / The Hindu", True, True,
     ["Act renamed the legislation as Van (Sanrakshan Evam Samvardhan) Adhiniyam, restricting applicability to notified forest lands and government records.",
      "Narrowed the broad definition of 'forest' established by the Supreme Court in the landmark 1996 T.N. Godavarman Thirumulpad case (dictionary meaning of forest).",
      "Exempts forest land within 100 km of international borders from prior forest clearance for strategic national security infrastructure."],
     "GS-3: Forest Conservation, Environmental Governance, Godavarman Precedent, Strategic Border Infrastructure, Tribal Rights.",
     [
         ("The landmark 1996 Supreme Court ruling in T.N. Godavarman Thirumulpad v. Union of India held that the Forest (Conservation) Act applies to:\n(a) Only reserved forests notified by State Governments\n(b) All forests irrespective of ownership or classification, applying the dictionary meaning of 'forest'\n(c) Only national parks and wildlife sanctuaries\n(d) Private plantations exceeding 1000 hectares",
          ["(a) Only reserved forests notified by State Governments", "(b) All forests irrespective of ownership or classification, applying the dictionary meaning of 'forest'", "(c) Only national parks and wildlife sanctuaries", "(d) Private plantations exceeding 1000 hectares"],
          "(b)", "The Godavarman ruling established that 'forest' must be understood according to its dictionary meaning, covering any area recorded as forest in government records regardless of ownership."),
         ("What major exemption was introduced under the Forest Conservation Amendment Act 2023 for linear infrastructure projects?\n(a) Complete exemption for all private real estate builders\n(b) Exemption for strategic linear projects of national importance within 100 km of international borders or LAC\n(c) Exemption for all mining within tiger reserves\n(d) Exemption for thermal power plants",
          ["(a) Complete exemption for all private real estate builders", "(b) Exemption for strategic linear projects of national importance within 100 km of international borders or LAC", "(c) Exemption for all mining within tiger reserves", "(d) Exemption for thermal power plants"],
          "(b)", "Section 1A exempts strategic security infrastructure (roads, bridges, defense installations) within 100 km of international borders from prior central forest clearance."),
         ("In February 2024, what interim order did the Supreme Court pass regarding the amended Forest Act?\n(a) Fully struck down the entire Act as unconstitutional\n(b) Directed that the broad Godavarman dictionary definition of 'forest' shall continue to apply until state expert committees identify deemed forests\n(c) Permitted unrestricted commercial logging in border states\n(d) Transferred forest jurisdiction to district collectors permanently",
          ["(a) Fully struck down the entire Act as unconstitutional", "(b) Directed that the broad Godavarman dictionary definition of 'forest' shall continue to apply until state expert committees identify deemed forests", "(c) Permitted unrestricted commercial logging in border states", "(d) Transferred forest jurisdiction to district collectors permanently"],
          "(b)", "The Supreme Court mandated that states must adhere to the 1996 Godavarman dictionary definition of forests to protect over 1.97 lakh sq km of unclassed/deemed forests."),
         ("What is the primary function of the Compensatory Afforestation Fund Management and Planning Authority (CAMPA)?\n(a) To auction timber from sacred groves\n(b) To manage funds deposited by user agencies towards compensatory afforestation when forest land is diverted for non-forest purposes\n(c) To conduct tiger census surveys\n(d) To issue international carbon certificates",
          ["(a) To auction timber from sacred groves", "(b) To manage funds deposited by user agencies towards compensatory afforestation when forest land is diverted for non-forest purposes", "(c) To conduct tiger census surveys", "(d) To issue international carbon certificates"],
          "(b)", "Under the Compensatory Afforestation Fund Act 2016, CAMPA holds funds for Net Present Value (NPV) and afforestation when forest land is diverted."),
         ("Under the Scheduled Tribes and Other Traditional Forest Dwellers (Recognition of Forest Rights) Act 2006, who is the authority to initiate the process for determining forest rights?\n(a) Forest Range Officer\n(b) Gram Sabha\n(c) District Magistrate\n(d) Sub-Divisional Committee",
          ["(a) Forest Range Officer", "(b) Gram Sabha", "(c) District Magistrate", "(d) Sub-Divisional Committee"],
          "(b)", "Under FRA 2006, the Gram Sabha is the statutory authority to initiate the process for determining the nature and extent of individual and community forest rights.")
     ]),

    ("ca-env-10", "2026-03-24", "Environment", "National Green Hydrogen Mission: SIGHT Program & Carbon Offsetting", "MNRE / PIB", True, True,
     ["National Green Hydrogen Mission targets producing at least 5 Million Metric Tonnes (MMT) of green hydrogen per annum by 2030.",
      "Strategic Interventions for Green Hydrogen Transition (SIGHT) program provides direct financial incentives for domestic electrolyser manufacturing and green hydrogen production.",
      "Mandates that green hydrogen must be produced through water electrolysis powered entirely by renewable energy or biomass gasification."],
     "GS-3: Renewable Energy, Decarbonisation, Green Hydrogen, SIGHT Scheme, Energy Transition.",
     [
         ("Green Hydrogen is defined as hydrogen gas produced through which process?\n(a) Steam Methane Reforming (SMR) using natural gas\n(b) Electrolysis of water powered entirely by renewable energy sources\n(c) Coal gasification without carbon capture\n(d) Fractional distillation of crude petroleum",
          ["(a) Steam Methane Reforming (SMR) using natural gas", "(b) Electrolysis of water powered entirely by renewable energy sources", "(c) Coal gasification without carbon capture", "(d) Fractional distillation of crude petroleum"],
          "(b)", "Green hydrogen is split from water via electrolysis using renewable electricity (solar/wind). Grey uses fossil gas without CCS; Blue uses fossil gas with CCS; Black/Brown uses coal."),
         ("What is the annual production target set for Green Hydrogen under India's National Green Hydrogen Mission by 2030?\n(a) 1 MMT\n(b) 5 MMT\n(c) 15 MMT\n(d) 25 MMT",
          ["(a) 1 MMT", "(b) 5 MMT", "(c) 15 MMT", "(d) 25 MMT"],
          "(b)", "The Mission targets at least 5 Million Metric Tonnes (MMT) per annum of green hydrogen capacity by 2030, saving Rs 1 lakh crore in fossil fuel imports."),
         ("Under the SIGHT program, financial incentives are provided for:\n(a) Domestic manufacturing of electrolysers and production of green hydrogen\n(b) Purchasing imported petrol vehicles\n(c) Constructing thermal coal boilers\n(d) Subsidizing urea fertilizer imports",
          ["(a) Domestic manufacturing of electrolysers and production of green hydrogen", "(b) Purchasing imported petrol vehicles", "(c) Constructing thermal coal boilers", "(d) Subsidizing urea fertilizer imports"],
          "(a)", "Strategic Interventions for Green Hydrogen Transition (SIGHT) has two financial incentive sub-programs: Component I (Electrolyser manufacturing) and Component II (Green Hydrogen production)."),
         ("Which of the following heavy industrial sectors is considered a 'hard-to-abate' sector where green hydrogen is essential for decarbonization?\n1. Primary Steel manufacturing\n2. Ammonia / Fertilizer synthesis\n3. Oil Refining\nSelect the correct answer:",
          ["(a) 1 and 2 only", "(b) 2 and 3 only", "(c) 1 and 3 only", "(d) 1, 2 and 3"],
          "(d)", "Steel (replacing metallurgical coking coal with direct reduced iron via H2), fertilizers (green ammonia replacing gas-derived hydrogen), and oil refineries are prime hard-to-abate sectors."),
         ("What is the only by-product generated when green hydrogen is combusted or utilized in a fuel cell?\n(a) Carbon dioxide\n(b) Sulfur dioxide\n(c) Pure Water (H2O)\n(d) Nitrous oxide",
          ["(a) Carbon dioxide", "(b) Sulfur dioxide", "(c) Pure Water (H2O)", "(d) Nitrous oxide"],
          "(c)", "The combustion or fuel cell reaction of hydrogen with atmospheric oxygen produces only water vapor (2H2 + O2 -> 2H2O), with zero greenhouse gas emissions.")
     ]),

    ("ca-env-11", "2026-02-19", "Environment", "Extended Producer Responsibility (EPR) & Plastic Waste Management Rules", "CPCB / PIB", False, True,
     ["Plastic Waste Management Rules mandate Extended Producer Responsibility (EPR) for Producers, Importers, and Brand Owners (PIBOs).",
      "Categorizes plastics into four distinct regimes: Category I (Rigid plastics), Category II (Flexible single/multi-layer), Category III (Multi-layered packaging), and Category IV (Compostable plastics).",
      "Imposes strict bans on identified single-use plastic (SUP) items having low utility and high littering potential."],
     "GS-3: Waste Management, Circular Economy, Plastic Pollution, EPR Framework, Central Pollution Control Board.",
     [
         ("The concept of 'Extended Producer Responsibility' (EPR) holds manufacturers responsible for:\n(a) The medical expenses of their retail customers\n(b) The post-consumer environmental end-of-life management of products they introduce into the market\n(c) The market pricing of competitor brands\n(d) Paying customs duties on exported finished products",
          ["(a) The medical expenses of their retail customers", "(b) The post-consumer environmental end-of-life management of products they introduce into the market", "(c) The market pricing of competitor brands", "(d) Paying customs duties on exported finished products"],
          "(b)", "EPR makes producers, importers, and brand-owners legally and financially responsible for collecting, recycling, and safely disposing of post-consumer plastic waste."),
         ("Which central agency manages the centralized online portal for EPR registration and certificate trading for plastic waste in India?\n(a) National Biodiversity Authority\n(b) Central Pollution Control Board (CPCB)\n(c) NITI Aayog\n(d) Bureau of Indian Standards (BIS)",
          ["(a) National Biodiversity Authority", "(b) Central Pollution Control Board (CPCB)", "(c) NITI Aayog", "(d) Bureau of Indian Standards (BIS)"],
          "(b)", "The Central Pollution Control Board (CPCB) operates the centralized EPR portal where producers register, report recycling, and trade EPR certificates."),
         ("Under the Plastic Waste Management Rules, what minimum thickness was mandated for carry bags made of virgin or recycled plastic?\n(a) 50 microns\n(b) 75 microns\n(c) 120 microns\n(d) 200 microns",
          ["(a) 50 microns", "(b) 75 microns", "(c) 120 microns", "(d) 200 microns"],
          "(c)", "The rules increased the minimum thickness of plastic carry bags from 50 to 75 microns, and subsequently to 120 microns to encourage reusability and collection viability."),
         ("What distinguishes 'Oxo-degradable' plastics from genuinely 'Biodegradable' plastics?\n(a) Oxo-degradable plastics completely convert into organic humus\n(b) Oxo-degradable plastics merely fragment into microplastics under heat and UV light rather than being assimilated by microorganisms\n(c) Oxo-degradable plastics are made exclusively from corn starch\n(d) Oxo-degradable plastics are legally certified compostable in India",
          ["(a) Oxo-degradable plastics completely convert into organic humus", "(b) Oxo-degradable plastics merely fragment into microplastics under heat and UV light rather than being assimilated by microorganisms", "(c) Oxo-degradable plastics are made exclusively from corn starch", "(d) Oxo-degradable plastics are legally certified compostable in India"],
          "(b)", "Oxo-degradable plastics contain additives that accelerate mechanical fragmentation into persistent, toxic microplastics, leading to a nationwide ban in India."),
         ("In waste hierarchy and circular economy principles, what is the most preferred environmental option?\n(a) Landfill disposal\n(b) Incineration with energy recovery\n(c) Recycling\n(d) Prevention / Reduction at source",
          ["(a) Landfill disposal", "(b) Incineration with energy recovery", "(c) Recycling", "(d) Prevention / Reduction at source"],
          "(d)", "The waste management hierarchy ranks: 1. Prevention/Reduction, 2. Reuse, 3. Recycling, 4. Recovery (energy), and 5. Disposal (least favored).")
     ]),

    ("ca-env-12", "2026-01-16", "Environment", "Global Biofuels Alliance (GBA) & Ethanol Blending (E20) Target", "MoPNG / PIB", True, True,
     ["Global Biofuels Alliance (GBA) launched during India's G20 Presidency alongside USA and Brazil (representing 85% of global ethanol production).",
      "India advanced its national target to achieve 20% ethanol blending in petrol (E20) from 2030 to 2025-26.",
      "Promotes 2G (Second Generation) ethanol produced from agricultural residues (paddy straw, sugarcane bagasse) to avoid food-versus-fuel conflict."],
     "GS-3: Biofuels, Energy Security, Ethanol Blending Program, G20 Outcomes, Sustainable Agriculture.",
     [
         ("Which three countries were the primary founding initiators of the Global Biofuels Alliance (GBA) launched at the G20 New Delhi Summit?\n(a) India, Brazil, and the United States\n(b) India, Russia, and China\n(c) India, Germany, and France\n(d) Brazil, Argentina, and South Africa",
          ["(a) India, Brazil, and the United States", "(b) India, Russia, and China", "(c) India, Germany, and France", "(d) Brazil, Argentina, and South Africa"],
          "(a)", "India, the US, and Brazil are the three leading biofuel producers and consumers, driving the launch of the Global Biofuels Alliance in September 2023."),
         ("What is the raw material distinction between 1G and 2G Bioethanol?\n(a) 1G uses sugarcane/food grains; 2G uses non-food lignocellulosic biomass and agricultural crop residues\n(b) 1G is made from algae; 2G is made from animal fat\n(c) 1G is blended with diesel; 2G is blended with aviation fuel\n(d) 1G is synthetic; 2G is natural",
          ["(a) 1G uses sugarcane/food grains; 2G uses non-food lignocellulosic biomass and agricultural crop residues", "(b) 1G is made from algae; 2G is made from animal fat", "(c) 1G is blended with diesel; 2G is blended with aviation fuel", "(d) 1G is synthetic; 2G is natural"],
          "(a)", "First generation (1G) biofuels use food crops (sugarcane juice, corn, broken rice); second generation (2G) uses inedible agricultural residues like rice straw and bagasse."),
         ("India's National Policy on Biofuels set the accelerated deadline for achieving 20% ethanol blending in petrol (E20) as:\n(a) 2030\n(b) 2025-26\n(c) 2035\n(d) 2040",
          ["(a) 2030", "(b) 2025-26", "(c) 2035", "(d) 2040"],
          "(b)", "The Union Cabinet amended the National Biofuels Policy, advancing the E20 blending target from the initial 2030 deadline to ethanol supply year 2025-26."),
         ("Under the SATAT (Sustainable Alternative Towards Affordable Transportation) initiative, the government promotes:\n(a) Electric bullet trains\n(b) Compressed Bio-Gas (CBG) plants using municipal and agricultural biomass\n(c) Nuclear powered coastal ferries\n(d) Hydrogen fuel cell drones",
          ["(a) Electric bullet trains", "(b) Compressed Bio-Gas (CBG) plants using municipal and agricultural biomass", "(c) Nuclear powered coastal ferries", "(d) Hydrogen fuel cell drones"],
          "(b)", "SATAT encourages setting up Compressed Bio-Gas (CBG) production plants from agricultural residue, cattle dung, and municipal solid waste as commercial automotive fuel."),
         ("Third-generation (3G) biofuels are derived primarily from which biomass feedstock?\n(a) Genetically engineered algae and cyanobacteria\n(b) Used cooking oil\n(c) Jatropha seeds\n(d) Timber sawdust",
          ["(a) Genetically engineered algae and cyanobacteria", "(b) Used cooking oil", "(c) Jatropha seeds", "(d) Timber sawdust"],
          "(a)", "Third-generation (3G) biofuels utilize microalgae and aquatic biomass cultivated on non-arable land without competing with food or freshwater resources.")
     ]),

    ("ca-env-13", "2026-10-25", "Environment", "Mangrove Alliance for Climate (MAC) & MISHTI Scheme Implementation", "MoEFCC / PIB", False, True,
     ["India joined the Mangrove Alliance for Climate (MAC) led by UAE and Indonesia at COP27 to accelerate conservation of coastal blue carbon ecosystems.",
      "Mangrove Initiative for Shoreline Habitats & Tangible Incomes (MISHTI) aims at comprehensively restoring mangrove cover across 540 sq km over 11 states and UTs.",
      "Mangroves store up to four times more carbon per hectare than terrestrial tropical rainforests, acting as natural storm-surge buffers."],
     "GS-3: Mangrove Ecology, Blue Carbon, Coastal Protection, MISHTI Scheme, Blue Economy.",
     [
         ("Which two countries spearheaded the launch of the Mangrove Alliance for Climate (MAC) at UNFCCC COP27?\n(a) United Arab Emirates and Indonesia\n(b) India and Bangladesh\n(c) Australia and Japan\n(d) Brazil and Colombia",
          ["(a) United Arab Emirates and Indonesia", "(b) India and Bangladesh", "(c) Australia and Japan", "(d) Brazil and Colombia"],
          "(a)", "The UAE and Indonesia launched the Mangrove Alliance for Climate (MAC) at COP27 in Egypt, which India joined as an active partner."),
         ("What is the primary objective of the MISHTI scheme announced in the Union Budget?\n(a) Developing inland aquaculture ponds for tiger prawns\n(b) Intensive afforestation and restoration of mangrove ecosystems along India's coastline and salt pans\n(c) Deep sea exploratory fishing licenses\n(d) Construction of concrete seawalls along beaches",
          ["(a) Developing inland aquaculture ponds for tiger prawns", "(b) Intensive afforestation and restoration of mangrove ecosystems along India's coastline and salt pans", "(c) Deep sea exploratory fishing licenses", "(d) Construction of concrete seawalls along beaches"],
          "(b)", "MISHTI (Mangrove Initiative for Shoreline Habitats & Tangible Incomes) facilitates mangrove plantation along the coast and on salt pan lands through convergence of CAMPA and MGNREGS."),
         ("In environmental economics, 'Blue Carbon' specifically refers to carbon captured and stored by:\n(a) Oceanic phytoplankton in polar ice\n(b) Coastal and marine vegetated ecosystems including mangroves, tidal marshes, and seagrass meadows\n(c) Carbon stored in deep ocean trenches\n(d) Liquid carbon dioxide injected into subsea oil reservoirs",
          ["(a) Oceanic phytoplankton in polar ice", "(b) Coastal and marine vegetated ecosystems including mangroves, tidal marshes, and seagrass meadows", "(c) Carbon stored in deep ocean trenches", "(d) Liquid carbon dioxide injected into subsea oil reservoirs"],
          "(b)", "Blue carbon is the carbon sequestered by coastal marine ecosystems: mangroves, salt marshes, and seagrasses, which lock carbon in sediment for centuries."),
         ("Which specialized anatomical adaptations enable mangrove species like Rhizophora to thrive in waterlogged, saline tidal soils?\n1. Pneumatophores (blind breathing roots)\n2. Viviparous germination\n3. Salt-secreting foliage glands\nSelect the correct answer:",
          ["(a) 1 and 2 only", "(b) 2 and 3 only", "(c) 1 and 3 only", "(d) 1, 2 and 3"],
          "(d)", "Mangroves feature pneumatophores to absorb atmospheric oxygen in anoxic mud, vivipary (seeds germinate while still attached to the tree), and ultra-filtration/salt exclusion."),
         ("Which delta in India contains the world's single largest contiguous block of halophytic mangrove forest?\n(a) Godavari Delta\n(b) Sundarbans Delta\n(c) Pichavaram Delta\n(d) Bhitarkanika Delta",
          ["(a) Godavari Delta", "(b) Sundarbans Delta", "(c) Pichavaram Delta", "(d) Bhitarkanika Delta"],
          "(b)", "The Sundarbans delta spanning India and Bangladesh is the world's largest contiguous mangrove forest, hosting the Royal Bengal Tiger and designated a UNESCO World Heritage site.")
     ]),

    ("ca-env-14", "2026-09-28", "Environment", "Blue Economy Policy & Coastal Regulation Zone (CRZ) Norms", "MoES / PIB", False, True,
     ["India's Blue Economy contributes ~4% to GDP, encompassing marine fisheries, maritime shipping, offshore renewables, coastal tourism, and biotechnology.",
      "CRZ Notification classifies coastal stretches into four zones: CRZ-I (Ecologically sensitive), CRZ-II (Urban built-up), CRZ-III (Rural coastal), and CRZ-IV (Water area up to 12 nautical miles).",
      "Deep Ocean Mission approved with Rs 4,077 crore outlay by Ministry of Earth Sciences for deep-sea mining of polymetallic nodules and ocean climate advisory services."],
     "GS-3: Marine Resources, Blue Economy, CRZ Classification, Deep Ocean Mission, Coastal Governance.",
     [
         ("Under the Coastal Regulation Zone (CRZ) Notification, which zone comprises Ecologically Sensitive Areas (ESAs) such as mangroves, corals, and turtle nesting grounds?\n(a) CRZ-I A\n(b) CRZ-II\n(c) CRZ-III A\n(d) CRZ-IV",
          ["(a) CRZ-I A", "(b) CRZ-II", "(c) CRZ-III A", "(d) CRZ-IV"],
          "(a)", "CRZ-I A covers environmentally sensitive areas (mangroves, corals, sand dunes, national parks). CRZ-I B covers the intertidal zone between Low Tide Line (LTL) and High Tide Line (HTL)."),
         ("Which of the following activities is strictly prohibited in the No Development Zone (NDZ) of rural coastal areas under CRZ-III?\n(a) Traditional fishing by local communities\n(b) Setting up of new commercial industrial plants and disposal of untreated effluents\n(c) Rainwater harvesting structures\n(d) Construction of temporary shacks during tourist season",
          ["(a) Traditional fishing by local communities", "(b) Setting up of new commercial industrial plants and disposal of untreated effluents", "(c) Rainwater harvesting structures", "(d) Construction of temporary shacks during tourist season"],
          "(b)", "Industrial units, hazardous waste disposal, and heavy polluting establishments are strictly prohibited in the NDZ of CRZ-III areas."),
         ("The international eco-label 'Blue Flag' awarded to Indian beaches like Golden Beach (Odisha) and Radhanagar (Andaman) is managed by:\n(a) UNESCO\n(b) Foundation for Environmental Education (FEE), Denmark\n(c) United Nations Environment Programme (UNEP)\n(d) International Maritime Organization (IMO)",
          ["(a) UNESCO", "(b) Foundation for Environmental Education (FEE), Denmark", "(c) United Nations Environment Programme (UNEP)", "(d) International Maritime Organization (IMO)"],
          "(b)", "Blue Flag certification is awarded by the non-profit Foundation for Environmental Education (FEE) based on 33 stringent environmental, bathing water, and safety criteria."),
         ("Under the UN Convention on the Law of the Sea (UNCLOS), an Exclusive Economic Zone (EEZ) extends up to how many nautical miles from the baseline?\n(a) 12 nautical miles\n(b) 24 nautical miles\n(c) 200 nautical miles\n(d) 350 nautical miles",
          ["(a) 12 nautical miles", "(b) 24 nautical miles", "(c) 200 nautical miles", "(d) 350 nautical miles"],
          "(c)", "Territorial waters extend to 12 nautical miles; Contiguous Zone to 24 nm; Exclusive Economic Zone (EEZ) extends up to 200 nautical miles from the territorial baseline."),
         ("Which mission under the Ministry of Earth Sciences includes the development of the manned submersible vehicle 'MATSYA 6000'?\n(a) Sagarmanthan Mission\n(b) Deep Ocean Mission\n(c) Project Mausam\n(d) Samudra Setu",
          ["(a) Sagarmanthan Mission", "(b) Deep Ocean Mission", "(c) Project Mausam", "(d) Samudra Setu"],
          "(b)", "Under the Deep Ocean Mission, the National Institute of Ocean Technology (NIOT) developed MATSYA 6000, designed to carry 3 humans to a depth of 6,000 meters in the Indian Ocean.")
     ]),

    ("ca-env-15", "2026-08-30", "Environment", "Miyawaki Method of Urban Afforestation & Air Pollution Mitigation", "MoEFCC / CPCB", False, False,
     ["The Miyawaki technique, pioneered by Japanese botanist Akira Miyawaki, creates multi-layered, native miniature urban forests in compact spaces.",
      "Involves planting native species densely (30 times denser than conventional monoculture) with growth rates 10 times faster, becoming self-sustaining in 3 years.",
      "Adopted by municipal corporations under the National Clean Air Programme (NCAP) as green acoustic and dust-trapping barriers in cities."],
     "GS-3: Urban Ecology, Afforestation Techniques, National Clean Air Programme, Biodiversity in Cities.",
     [
         ("The Miyawaki method of urban forestry is best described as:\n(a) Creating monoculture eucalyptus plantations for commercial paper pulp\n(b) Developing dense, multi-layered micro-forests using exclusively native species in small urban pockets\n(c) Genetically modifying bamboo for rapid carbon absorption\n(d) Subsidizing chemical fertilizers in city gardens",
          ["(a) Creating monoculture eucalyptus plantations for commercial paper pulp", "(b) Developing dense, multi-layered micro-forests using exclusively native species in small urban pockets", "(c) Genetically modifying bamboo for rapid carbon absorption", "(d) Subsidizing chemical fertilizers in city gardens"],
          "(b)", "Miyawaki forests replicate natural ecological succession by planting diverse local native species (canopy, tree, sub-tree, and shrub layers) at very high density."),
         ("Compared to conventional plantation forestry, Miyawaki forests typically grow:\n(a) At the same rate\n(b) 10 times faster and 30 times denser\n(c) Slower due to root competition\n(d) Only in sub-zero alpine conditions",
          ["(a) At the same rate", "(b) 10 times faster and 30 times denser", "(c) Slower due to root competition", "(d) Only in sub-zero alpine conditions"],
          "(b)", "Close spacing forces saplings to shoot upwards rapidly for sunlight, achieving self-sustaining mature canopy cover within 2-3 years instead of 20-30 years."),
         ("Which national program in India launched in 2019 targets 20-40% reduction in PM2.5 and PM10 concentrations across non-attainment cities?\n(a) National Clean Air Programme (NCAP)\n(b) Green India Mission\n(c) Smart Cities Mission\n(d) AMRUT",
          ["(a) National Clean Air Programme (NCAP)\n(b) Green India Mission\n(c) Smart Cities Mission\n(d) AMRUT"],
          "(a)", "The National Clean Air Programme (NCAP) targets 131 non-attainment cities that persistently fail to meet the National Ambient Air Quality Standards (NAAQS)."),
         ("Which of the following is considered a primary reason why non-native exotic tree species like Eucalyptus and Conocarpus are discouraged in urban forestry?\n(a) They produce excessive edible fruits\n(b) Deep root water depletion, allelopathic suppression of native flora, and pollen allergies\n(c) Inability to survive Indian summer heat\n(d) Their leaves attract locust swarms",
          ["(a) They produce excessive edible fruits\n(b) Deep root water depletion, allelopathic suppression of native flora, and pollen allergies\n(c) Inability to survive Indian summer heat\n(d) Their leaves attract locust swarms"],
          "(b)", "Exotics like Conocarpus and Eucalyptus rapidly deplete urban water tables, damage underground civic sewer infrastructure, and trigger severe respiratory pollen allergies."),
         ("In ecological science, the process where plants absorb and neutralize atmospheric particulate matter on their leaf cuticles is known as:\n(a) Eutrophication\n(b) Phyto-remediation and particulate deposition\n(c) Biomagnification\n(d) Acidification",
          ["(a) Eutrophication", "(b) Phyto-remediation and particulate deposition", "(c) Biomagnification", "(d) Acidification"],
          "(b)", "Vegetative green belts capture airborne dust and PM2.5 on hairy or waxy leaf surfaces, mitigating urban particulate pollution via phytoremediation.")
     ]),

    ("ca-env-16", "2026-07-08", "Environment", "Coral Reef Bleaching: Fourth Global Mass Bleaching Event & Lakshadweep Crisis", "NOAA / CMFRI", True, True,
     ["NOAA confirmed the fourth global mass coral bleaching event on record, impacting reefs across Atlantic, Pacific, and Indian Ocean basins.",
      "Coral bleaching is triggered when elevated sea surface temperatures force corals to expel symbiotic algae (zooxanthellae) living in their tissues.",
      "Severe bleaching confirmed across Lakshadweep atolls and Gulf of Mannar, threatening marine food security and natural breakwaters."],
     "GS-3: Marine Ecosystems, Coral Bleaching, Ocean Warming, Symbiosis, Coastal Resilience.",
     [
         ("Coral bleaching occurs primarily due to the breakdown of the symbiotic relationship between corals and:\n(a) Cyanobacteria\n(b) Microscopic photosynthetic algae called Zooxanthellae\n(c) Marine nematodes\n(d) Sponges",
          ["(a) Cyanobacteria", "(b) Microscopic photosynthetic algae called Zooxanthellae", "(c) Marine nematodes", "(d) Sponges"],
          "(b)", "Thermal stress causes corals to expel their photosynthetic endosymbionts (zooxanthellae of genus Symbiodinium), stripping corals of their color and primary nutrient source."),
         ("Which of the following marine regions in India possesses coral reefs?\n1. Andaman and Nicobar Islands\n2. Lakshadweep Islands\n3. Gulf of Kutch\n4. Gulf of Mannar\nSelect the correct answer:",
          ["(a) 1 and 2 only", "(b) 3 and 4 only", "(c) 1, 2 and 4 only", "(d) 1, 2, 3 and 4"],
          "(d)", "India has four major coral reef regions: Andaman & Nicobar (fringing/barrier), Lakshadweep (atolls), Gulf of Mannar (fringing), and Gulf of Kutch (patchy fringing)."),
         ("What chemical compound constitutes the primary structural skeleton secreted by hard reef-building (hermatypic) corals?\n(a) Calcium Carbonate (CaCO3)\n(b) Silicon Dioxide (SiO2)\n(c) Sodium Chloride (NaCl)\n(d) Magnesium Sulfate (MgSO4)",
          ["(a) Calcium Carbonate (CaCO3)", "(b) Silicon Dioxide (SiO2)", "(c) Sodium Chloride (NaCl)", "(d) Magnesium Sulfate (MgSO4)"],
          "(a)", "Hermatypic corals extract calcium and carbonate ions from seawater to build aragonite skeletons (calcium carbonate, CaCO3)."),
         ("How does Ocean Acidification caused by anthropogenic CO2 absorption impair coral reefs?\n(a) It causes water temperatures to drop below freezing\n(b) It lowers ocean pH and reduces the availability of carbonate ions needed for calcification\n(c) It turns coral polyps into predatory jellyfish\n(d) It causes marine salinity to double",
          ["(a) It causes water temperatures to drop below freezing", "(b) It lowers ocean pH and reduces the availability of carbonate ions needed for calcification", "(c) It turns coral polyps into predatory jellyfish", "(d) It causes marine salinity to double"],
          "(b)", "Dissolved CO2 forms carbonic acid, lowering seawater pH and reacting with carbonate ions, which dissolves existing coral skeletons and impedes new calcification."),
         ("The phenomenon of 'Coral Gardening' or 'Biorock' technology refers to:\n(a) Injecting dye into bleached corals\n(b) Using low-voltage electrical currents passed through submerged steel structures to accelerate calcium carbonate precipitation and coral growth\n(c) Dredging sea beds to bury dead corals\n(d) Spraying sunscreen on coastal reefs",
          ["(a) Injecting dye into bleached corals", "(b) Using low-voltage electrical currents passed through submerged steel structures to accelerate calcium carbonate precipitation and coral growth", "(c) Dredging sea beds to bury dead corals", "(d) Spraying sunscreen on coastal reefs"],
          "(b)", "Biorock (mineral accretion technology) uses low-voltage DC electric current in seawater to precipitate calcium carbonate onto steel frames, speeding up coral healing by up to 5 times.")
     ])
]

all_env = env1_2 + [make_art(aid, dt, pil, tit, src, top, pt, sums, gs, qs) for aid, dt, pil, tit, src, top, pt, sums, gs, qs in env_new]
print(f"Total Environment articles: {len(all_env)}")
assert len(all_env) == 16, f"Expected 16, got {len(all_env)}"

with open(os.path.join(BASE_DIR, 'data', 'ca_builders', 'environment.json'), 'w') as f:
    json.dump(all_env, f, indent=2)

print("Saved environment.json successfully!")
