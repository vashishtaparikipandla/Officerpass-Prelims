#!/usr/bin/env python3
"""
Builds Geography articles (ca-geo-01 to ca-geo-12: total 12 articles)
"""
import json
import os

BASE_DIR = '/Users/vashishtaparikipandla/Documents/OfficerPass'

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

geo_articles = [
    ("ca-geo-01", "2026-10-10", "Geography", "Western Disturbances Shifts & Polar Vortex Anomalies Affecting Rabi Crops", "IMD / Down to Earth", True, True,
     ["Western Disturbances (WDs) are extratropical cyclonic storms originating over the Mediterranean Sea, Caspian Sea, and Black Sea that bring non-monsoonal precipitation to north-west India.",
      "Climate change has induced northward shift in subtropical jet streams, leading to delayed, erratic winter rain and unseasonal March hailstorms damaging standing mustard and wheat.",
      "Precipitation from WDs is crucial for sustaining Himalayan snowpack feeding perennial rivers like Indus and Ganga during dry summer months."],
     "GS-1: Physical Geography, Indian Climatology, Western Disturbances, Subtropical Jet Stream, Rabi Agriculture.",
     [
         ("Western Disturbances that bring crucial winter rains to northwestern India originate over which water body?\n(a) Bay of Bengal\n(b) Mediterranean Sea and Black Sea\n(c) South China Sea\n(d) Red Sea",
          ["(a) Bay of Bengal", "(b) Mediterranean Sea and Black Sea", "(c) South China Sea", "(d) Red Sea"],
          "(b)", "Western Disturbances are extratropical low-pressure frontal systems that form over the Mediterranean, Caspian, and Black seas and are steered eastward by westerly jet streams."),
         ("Which high-altitude atmospheric wind system steers Western Disturbances towards the Indian subcontinent during winter?\n(a) Tropical Easterly Jet Stream\n(b) Sub-Tropical Westerly Jet Stream\n(c) Polar Easterlies\n(d) Trade Winds",
          ["(a) Tropical Easterly Jet Stream", "(b) Sub-Tropical Westerly Jet Stream", "(c) Polar Easterlies", "(d) Trade Winds"],
          "(b)", "The Sub-Tropical Westerly Jet Stream (STWJ), flowing at 9-12 km altitude, splits around the Tibetan Plateau with its southern branch steering WDs across Pakistan and North India."),
         ("What is the primary agricultural benefit of winter precipitation brought by Western Disturbances in Punjab and Haryana?\n(a) Sowing of Kharif rice crops\n(b) Sustaining the vegetative and grain-filling stages of Rabi wheat and mustard crops\n(c) Flowering of tea bushes in Nilgiris\n(d) Harvesting of jute in delta regions",
          ["(a) Sowing of Kharif rice crops", "(b) Sustaining the vegetative and grain-filling stages of Rabi wheat and mustard crops", "(c) Flowering of tea bushes in Nilgiris", "(d) Harvesting of jute in delta regions"],
          "(b)", "Light, steady winter showers and cold night temperatures associated with WDs are indispensable for optimum grain development in Rabi winter crops (wheat, barley, gram, mustard)."),
         ("When a Western Disturbance is approaching a region, what characteristic meteorological indicator is typically observed first?\n(a) Sudden sharp drop in night temperatures\n(b) Rise in night temperatures and appearance of high cirrus clouds\n(c) Severe dust storm without clouds\n(d) Immediate high atmospheric pressure",
          ["(a) Sudden sharp drop in night temperatures", "(b) Rise in night temperatures and appearance of high cirrus clouds", "(c) Severe dust storm without clouds\n", "(d) Immediate high atmospheric pressure"],
          "(b)", "An incoming WD pushes warm, moist air into the region, causing a characteristic rise in night (minimum) temperatures and cirrus/cirrostratus cloud cover ahead of the front."),
         ("Extratropical cyclones (Western Disturbances) differ fundamentally from Tropical cyclones because:\n(a) Extratropical cyclones have clear frontal systems (warm and cold fronts) and originate over land and sea alike\n(b) Extratropical cyclones only occur over warm tropical oceans with SST > 27°C\n(c) Extratropical cyclones rotate clockwise in the northern hemisphere\n(d) Extratropical cyclones have an eye with calm descending air",
          ["(a) Extratropical cyclones have clear frontal systems (warm and cold fronts) and originate over land and sea alike", "(b) Extratropical cyclones only occur over warm tropical oceans with SST > 27°C", "(c) Extratropical cyclones rotate clockwise in the northern hemisphere", "(d) Extratropical cyclones have an eye with calm descending air"],
          "(a)", "Extratropical cyclones are baroclinic systems powered by horizontal temperature gradients along distinct warm and cold fronts, unlike tropical cyclones driven by latent heat of condensation.")
     ]),

    ("ca-geo-02", "2026-09-18", "Geography", "Ken-Betwa River Interlinking Project & Panna Tiger Reserve Inundation", "NWDA / PIB", True, True,
     ["Ken-Betwa Link Project (KBLP) is the first project under the National Perspective Plan for interlinking of rivers, transferring surplus water from Ken to water-deficit Betwa basin.",
      "Both Ken and Betwa are non-peninsular right-bank tributaries of the Yamuna River originating in the Vindhyan Range of Madhya Pradesh.",
      "Daudhan Dam construction will submerge ~4,141 hectares of the core critical tiger habitat of Panna Tiger Reserve in Bundelkhand."],
     "GS-1: Drainage Systems, River Interlinking, Ken-Betwa, Bundelkhand Drought, Ecology vs Infrastructure.",
     [
         ("Both the Ken and Betwa rivers are tributaries of which major Indian river?\n(a) Ganga River\n(b) Yamuna River\n(c) Narmada River\n(d) Son River",
          ["(a) Ganga River", "(b) Yamuna River", "(c) Narmada River", "(d) Son River"],
          "(b)", "Both Ken and Betwa originate in the Vindhya range in Madhya Pradesh and flow north-northeast to join the Yamuna River (Betwa at Hamirpur, Ken at Chilla in Banda district, UP)."),
         ("Which National Park and Tiger Reserve will experience significant core habitat submergence due to the Daudhan dam of the Ken-Betwa Link Project?\n(a) Kanha Tiger Reserve\n(b) Bandhavgarh Tiger Reserve\n(c) Panna Tiger Reserve\n(d) Pench Tiger Reserve",
          ["(a) Kanha Tiger Reserve", "(b) Bandhavgarh Tiger Reserve", "(c) Panna Tiger Reserve", "(d) Pench Tiger Reserve"],
          "(c)", "The project's reservoir will inundate ~6,017 hectares of forest land, including ~4,141 hectares inside the core area of Panna Tiger Reserve, renowned for its tiger reintroduction success."),
         ("Which chronically drought-prone geographic region spanning Uttar Pradesh and Madhya Pradesh is the primary beneficiary of the Ken-Betwa link?\n(a) Marathwada\n(b) Bundelkhand\n(c) Saurashtra\n(d) Rayalaseema",
          ["(a) Marathwada", "(b) Bundelkhand", "(c) Saurashtra", "(d) Rayalaseema"],
          "(b)", "Bundelkhand (spanning 13 districts across MP and UP) suffers severe groundwater depletion, agrarian distress, and recurring drought, which KBLP aims to alleviate."),
         ("Which central agency under the Ministry of Jal Shakti is responsible for surveying and formulating river interlinking proposals under the National Perspective Plan?\n(a) Central Water Commission (CWC)\n(b) National Water Development Agency (NWDA)\n(c) Central Ground Water Board (CGWB)\n(d) Brahmaputra Board",
          ["(a) Central Water Commission (CWC)", "(b) National Water Development Agency (NWDA)", "(c) Central Ground Water Board (CGWB)", "(d) Brahmaputra Board"],
          "(b)", "The National Water Development Agency (NWDA) was established in 1982 to carry out feasibility studies and detailed project reports for interbasin water transfers."),
         ("The National Perspective Plan (NPP) for water resources development divides river interlinking into which two broad components?\n(a) Himalayan Rivers Development Component and Peninsular Rivers Development Component\n(b) Northern Plains Component and Coastal Component\n(c) Rainfed Component and Canal Component\n(d) East-Flowing Component and West-Flowing Component",
          ["(a) Himalayan Rivers Development Component and Peninsular Rivers Development Component", "(b) Northern Plains Component and Coastal Component", "(c) Rainfed Component and Canal Component", "(d) East-Flowing Component and West-Flowing Component"],
          "(a)", "The NPP formulated in 1980 comprises 30 links: 14 under the Himalayan Rivers Component and 16 under the Peninsular Rivers Component.")
     ]),

    ("ca-geo-03", "2026-08-20", "Geography", "Critical Minerals Mission & Lithium Exploration in Salal-Haimana (Reasi, J&K)", "Geological Survey of India / PIB", True, True,
     ["Geological Survey of India (GSI) established 5.9 million tonnes of inferred lithium resources (G4 stage) in the Salal-Haimana area of Reasi district, Jammu & Kashmir.",
      "Lithium in Salal-Haimana is embedded within bauxite/aluminous laterite formations of the Subathu geological group.",
      "Mines and Minerals (Development and Regulation) Amendment Act 2023 delisted six atomic minerals including Lithium, Beryllium, and Titanium, allowing commercial auction to private miners."],
     "GS-1 & GS-3: Mineral Resources, Lithium reserves, MMDR Act 2023, Critical Minerals, Energy Transition.",
     [
         ("The inferred 5.9 million tonnes lithium mineral deposit identified by GSI is located in which district of Jammu & Kashmir?\n(a) Baramulla\n(b) Reasi\n(c) Anantnag\n(d) Kupwara",
          ["(a) Baramulla\n", "(b) Reasi", "(c) Anantnag", "(d) Kupwara"],
          "(b)", "The deposit is situated in the Salal-Haimana area of Reasi district in the Jammu division, near the Chenab River and the Salal Hydroelectric Project."),
         ("In international geology, the 'Lithium Triangle' of South America that accounts for over half the world's brine lithium reserves comprises which three nations?\n(a) Brazil, Colombia, and Peru\n(b) Argentina, Bolivia, and Chile\n(c) Chile, Ecuador, and Venezuela\n(d) Mexico, Argentina, and Paraguay",
          ["(a) Brazil, Colombia, and Peru", "(b) Argentina, Bolivia, and Chile", "(c) Chile, Ecuador, and Venezuela", "(d) Mexico, Argentina, and Paraguay"],
          "(b)", "The Lithium Triangle spans the salt flats (salares) of the Atacama (Chile), Uyuni (Bolivia), and Hombre Muerto (Argentina)."),
         ("How does the geological occurrence of lithium in Jammu & Kashmir differ from deposits in South America and Western Australia?\n(a) J&K lithium is dissolved in volcanic geothermal geysers\n(b) J&K lithium is hosted in hard-rock bauxitic/clay aluminous formations rather than liquid salar brines or spodumene pegmatites\n(c) J&K lithium is pure metallic nuggets found on river beds\n(d) J&K lithium is extracted from sea ice",
          ["(a) J&K lithium is dissolved in volcanic geothermal geysers", "(b) J&K lithium is hosted in hard-rock bauxitic/clay aluminous formations rather than liquid salar brines or spodumene pegmatites", "(c) J&K lithium is pure metallic nuggets found on river beds", "(d) J&K lithium is extracted from sea ice"],
          "(b)", "While Australia mines spodumene pegmatite and South America pumps underground brine salars, the Reasi deposit is bound in aluminous lateritic/bauxite clays, requiring specialized hydrometallurgical processing."),
         ("What major reform was introduced by the MMDR Amendment Act 2023 regarding critical minerals in India?\n(a) Banned all private participation in mineral mining\n(b) Delisted six atomic minerals (including Lithium, Titanium, Niobium, Tantalum, Beryllium, Zirconium) to permit private exploration and commercial auction\n(c) Made mineral rights the exclusive monopoly of state governments\n(d) Fixed zero royalties on mineral exports",
          ["(a) Banned all private participation in mineral mining", "(b) Delisted six atomic minerals (including Lithium, Titanium, Niobium, Tantalum, Beryllium, Zirconium) to permit private exploration and commercial auction", "(c) Made mineral rights the exclusive monopoly of state governments", "(d) Fixed zero royalties on mineral exports"],
          "(b)", "The amendment removed these critical transition minerals from the restricted 'atomic minerals' list (Part B of First Schedule), enabling competitive commercial auction to private players."),
         ("Which joint-venture company set up by three Indian CPSEs (NALCO, HCL, MECL) is tasked with acquiring overseas critical mineral assets like lithium and cobalt?\n(a) Khanij Bidesh India Limited (KABIL)\n(b) Coal India Videsh\n(c) Mineral Exploration Corporation\n(d) Rare Earths Overseas Ltd",
          ["(a) Khanij Bidesh India Limited (KABIL)", "(b) Coal India Videsh", "(c) Mineral Exploration Corporation", "(d) Rare Earths Overseas Ltd"],
          "(a)", "KABIL (Khanij Bidesh India Ltd) was established under the Ministry of Mines to acquire brine and hard-rock exploration blocks abroad, signing agreements with Argentina's CAMYEN.")
     ]),

    ("ca-geo-04", "2026-07-16", "Geography", "ENSO Phase Transition: El Niño to La Niña & Indian Monsoon Teleconnections", "IMD / NOAA", True, True,
     ["The transition from a strong El Niño to ENSO-neutral and subsequent La Niña conditions significantly influences the spatial distribution of the Indian Summer Monsoon Rainfall (ISMR).",
      "La Niña features anomalous cooling of sea surface temperatures (SSTs) in the central and eastern equatorial Pacific, strengthening the Pacific Walker Circulation.",
      "Historically, La Niña is strongly correlated with above-normal southwest monsoon precipitation in India, but often prolongs extreme winter cold waves across north India."],
     "GS-1: Climatology, ENSO, Walker Circulation, Indian Monsoon Teleconnections, Indian Ocean Dipole.",
     [
         ("During a 'La Niña' event, what anomaly occurs in the equatorial Pacific Ocean?\n(a) Unusually warm sea surface temperatures in the eastern Pacific\n(b) Unusually cold sea surface temperatures in the central and eastern equatorial Pacific, with strong trade winds pushing warm water towards the western Pacific/Asia\n(c) Complete shutdown of global ocean thermohaline circulation\n(d) Sea level drops by 10 meters worldwide",
          ["(a) Unusually warm sea surface temperatures in the eastern Pacific", "(b) Unusually cold sea surface temperatures in the central and eastern equatorial Pacific, with strong trade winds pushing warm water towards the western Pacific/Asia", "(c) Complete shutdown of global ocean thermohaline circulation", "(d) Sea level drops by 10 meters worldwide"],
          "(b)", "La Niña represents the cold phase of ENSO: enhanced easterly trade winds pile up warm water in the western Pacific warm pool around Indonesia, while intense upwelling cools the eastern Pacific near Peru."),
         ("What is the general teleconnection impact of a developing 'La Niña' on the Indian Southwest Monsoon?\n(a) Severe widespread monsoon drought\n(b) Normal to above-normal monsoon rainfall and robust monsoon surge\n(c) Complete absence of rain in peninsular India\n(d) Delayed onset of monsoon by 6 months",
          ["(a) Severe widespread monsoon drought", "(b) Normal to above-normal monsoon rainfall and robust monsoon surge", "(c) Complete absence of rain in peninsular India", "(d) Delayed onset of monsoon by 6 months"],
          "(b)", "La Niña strengthens the ascending branch of the Walker circulation over the maritime continent, enhancing moisture convergence and favoring above-average southwest monsoon rainfall over India."),
         ("The Indian Ocean Dipole (IOD) involves anomalous sea surface temperature differences between which two oceanic regions?\n(a) Northern Arabian Sea and Southern Indian Ocean\n(b) Western tropical Indian Ocean (near African coast) and Eastern tropical Indian Ocean (near Sumatra, Indonesia)\n(c) Bay of Bengal and Gulf of Mannar\n(d) Red Sea and Persian Gulf",
          ["(a) Northern Arabian Sea and Southern Indian Ocean", "(b) Western tropical Indian Ocean (near African coast) and Eastern tropical Indian Ocean (near Sumatra, Indonesia)", "(c) Bay of Bengal and Gulf of Mannar", "(d) Red Sea and Persian Gulf"],
          "(b)", "The IOD (Indian Niño) measures the difference in SST between the western pole (Arabian Sea off East Africa) and eastern pole (eastern Indian Ocean south of Indonesia)."),
         ("A 'Positive Indian Ocean Dipole' (+IOD) generally has what effect on Indian monsoon rainfall?\n(a) Suppresses rainfall and triggers drought\n(b) Enhances rainfall over the Indian subcontinent, often counterbalancing the negative drying effect of an El Niño\n(c) Stops cyclone formation in the Arabian Sea\n(d) Causes freezing blizzards in summer",
          ["(a) Suppresses rainfall and triggers drought", "(b) Enhances rainfall over the Indian subcontinent, often counterbalancing the negative drying effect of an El Niño", "(c) Stops cyclone formation in the Arabian Sea", "(d) Causes freezing blizzards in summer"],
          "(b)", "A Positive IOD brings warm waters to the western Indian Ocean, increasing convection and rainfall over India, as demonstrated in 2019 and 1997 when it neutralized El Niño."),
         ("Which atmospheric pressure index compares surface air pressure between Tahiti in French Polynesia and Darwin in northern Australia?\n(a) North Atlantic Oscillation (NAO)\n(b) Southern Oscillation Index (SOI)\n(c) Madden-Julian Oscillation (MJO)\n(d) Arctic Oscillation (AO)",
          ["(a) North Atlantic Oscillation (NAO)", "(b) Southern Oscillation Index (SOI)", "(c) Madden-Julian Oscillation (MJO)", "(d) Arctic Oscillation (AO)"],
          "(b)", "The Southern Oscillation Index (SOI) measures sea level pressure difference between Tahiti and Darwin. Sustained positive SOI values indicate La Niña; sustained negative values indicate El Niño.")
     ]),

    ("ca-geo-05", "2026-06-22", "Geography", "Great Nicobar Island Development Project & Galathea Bay Mega-Port", "NITI Aayog / MoEFCC", True, True,
     ["The Rs 72,000 crore holistic development of Great Nicobar Island includes an International Container Transshipment Port (ICTP) at Galathea Bay, an airport, power plant, and township.",
      "Great Nicobar is the southernmost island of the Nicobar archipelago, situated barely 150 km from the tip of Sumatra (Indonesia) along the East-West international shipping lane.",
      "Environmental concerns center on the diversion of ~130 sq km of virgin primary rainforest, nesting beaches of the Giant Leatherback Turtle, and ancestral habitats of the Shompen and Nicobarese tribes."],
     "GS-1: Island Geography, Maritime Strategic Chokepoints, Biodiversity Hotspots, Leatherback Turtles, Shompen Tribe.",
     [
         ("What is the southernmost point of the Republic of India located on Great Nicobar Island?\n(a) Kanyakumari\n(b) Indira Point (formerly Pygmalion Point)\n(c) Kibithu\n(d) Sir Creek",
          ["(a) Kanyakumari\n", "(b) Indira Point (formerly Pygmalion Point)", "(c) Kibithu", "(d) Sir Creek"],
          "(b)", "Indira Point at 6°45' N latitude on Great Nicobar Island is the southernmost geographical point of the Indian Union (submerged by 4.25 meters during the 2004 Indian Ocean tsunami)."),
         ("Which oceanic water channel separates the Andaman Islands group from the Nicobar Islands group?\n(a) Duncan Passage\n(b) Ten Degree Channel\n(c) Nine Degree Channel\n(d) Six Degree Channel (Great Channel)",
          ["(a) Duncan Passage", "(b) Ten Degree Channel", "(c) Nine Degree Channel", "(d) Six Degree Channel (Great Channel)"],
          "(b)", "The Ten Degree Channel (150 km wide) lies along the 10° N parallel, separating Little Andaman to the north from Car Nicobar to the south."),
         ("The strategic water channel separating Great Nicobar Island from the Indonesian island of Sumatra is known as the:\n(a) Malacca Strait\n(b) Six Degree Channel (Great Channel)\n(c) Palk Strait\n(d) Sunda Strait",
          ["(a) Malacca Strait", "(b) Six Degree Channel (Great Channel)", "(c) Palk Strait", "(d) Sunda Strait"],
          "(b)", "The Six Degree Channel (Great Channel) is a vital global commercial shipping lane through which container traffic enters the Strait of Malacca from the Indian Ocean."),
         ("Galathea Bay on Great Nicobar Island is internationally renowned as the prime nesting habitat for which marine turtle species?\n(a) Olive Ridley Turtle\n(b) Giant Leatherback Turtle (Dermochelys coriacea)\n(c) Hawksbill Turtle\n(d) Loggerhead Turtle",
          ["(a) Olive Ridley Turtle", "(b) Giant Leatherback Turtle (Dermochelys coriacea)", "(c) Hawksbill Turtle", "(d) Loggerhead Turtle"],
          "(b)", "Galathea Bay is one of the most critical nesting sites in the northern Indian Ocean for the Giant Leatherback Turtle, the world's largest living marine turtle."),
         ("Which indigenous Particulary Vulnerable Tribal Group (PVTG), practicing hunting-gathering in interior dense rainforests, is indigenous to Great Nicobar Island?\n(a) Sentinelese\n(b) Jarawa\n(c) Shompen\n(d) Onge",
          ["(a) Sentinelese", "(b) Jarawa", "(c) Shompen", "(d) Onge"],
          "(c)", "The Shompen are an isolated, nomadic hunting-gathering PVTG indigenous to the interior rainforests of Great Nicobar Biosphere Reserve (Sentinelese, Jarawa, and Onge inhabit the Andaman islands).")
     ]),

    ("ca-geo-06", "2026-05-16", "Geography", "Tsangpo-Brahmaputra Medog Dam in Tibet & Downstream Riparian Hydrology", "MEA / The Hindu", True, True,
     ["China's planned 60-gigawatt mega-dam on the Great Bend (Yarlung Tsangpo Grand Canyon) near Medog in Tibet dwarfs the Three Gorges Dam in generating capacity.",
      "The Yarlung Tsangpo makes a sharp hairpin turn around Namcha Barwa before cutting through the Himalayas to enter Arunachal Pradesh as the Siang River.",
      "India has expedited plans for the 11-gigawatt Upper Siang multipurpose storage dam in Arunachal Pradesh to absorb flash-flood water releases and establish prior user water rights."],
     "GS-1: Transboundary Rivers, Drainage Pattern of Brahmaputra, Antecedent Drainage, Hydropolitics in South Asia.",
     [
         ("The Brahmaputra River originates in which glacier near Mount Kailash and Lake Manasarovar in Tibet?\n(a) Gangotri Glacier\n(b) Chemayungdung Glacier (Angsi Glacier)\n(c) Siachen Glacier\n(d) Zemu Glacier",
          ["(a) Gangotri Glacier", "(b) Chemayungdung Glacier (Angsi Glacier)", "(c) Siachen Glacier", "(d) Zemu Glacier"],
          "(b)", "The Yarlung Tsangpo originates in the Chemayungdung Glacier in the Kailash range in southwestern Tibet and flows eastward for ~1,700 km before entering India."),
         ("Around which prominent Himalayan mountain peak does the Yarlung Tsangpo make a dramatic hairpin bend (Great Bend) before entering Arunachal Pradesh?\n(a) Kanchenjunga\n(b) Nanga Parbat\n(c) Namcha Barwa\n(d) Nanda Devi",
          ["(a) Kanchenjunga", "(b) Nanga Parbat", "(c) Namcha Barwa", "(d) Nanda Devi"],
          "(c)", "The river cuts the deepest canyon in the world around the eastern Himalayan syntaxial anchor of Namcha Barwa (7,782 m), transforming into an antecedent gorge."),
         ("Match the name of the Brahmaputra River across its sequential geographic reaches:\n1. Tibet — A. Jamuna\n2. Arunachal Pradesh — B. Yarlung Tsangpo\n3. Assam Valley — C. Siang / Dihang\n4. Bangladesh — D. Brahmaputra\nSelect the correct matching:",
          ["(a) 1-B, 2-C, 3-D, 4-A", "(b) 1-A, 2-B, 3-C, 4-D", "(c) 1-C, 2-D, 3-B, 4-A", "(d) 1-B, 2-A, 3-C, 4-D"],
          "(a)", "In Tibet it is Yarlung Tsangpo; in Arunachal it is Siang/Dihang; after confluence with Dibang and Lohit near Sadiya it is Brahmaputra; in Bangladesh it is Jamuna (merging with Padma)."),
         ("In international river law, what legal doctrine gives a downstream riparian state protection based on utilizing river water before an upstream neighbor modifies it?\n(a) Harmon Doctrine (absolute territorial sovereignty)\n(b) Principle of Prior Appropriation ('first in time, first in right')\n(c) Res Communes\n(d) Terra Nullius",
          ["(a) Harmon Doctrine (absolute territorial sovereignty)", "(b) Principle of Prior Appropriation ('first in time, first in right')", "(c) Res Communes", "(d) Terra Nullius"],
          "(b)", "Prior Appropriation establishes that an established historic beneficial water user gains a protected legal standing against upstream interventions under customary international water law."),
         ("Which two major river tributaries meet the Siang River near Sadiya in Assam to formally create the Brahmaputra River?\n(a) Subansiri and Manas\n(b) Dibang and Lohit\n(c) Teesta and Torsa\n(d) Dhansiri and Kopili",
          ["(a) Subansiri and Manas", "(b) Dibang and Lohit", "(c) Teesta and Torsa", "(d) Dhansiri and Kopili"],
          "(b)", "The Dihang (Siang) enters the Assam plains where it is joined from the east by the Dibang (Sikang) and Lohit rivers, from which confluence onward the river is designated Brahmaputra.")
     ]),

    ("ca-geo-07", "2026-04-10", "Geography", "Joshimath Land Subsidence & Main Central Thrust (MCT) Tectonic Fragility", "ISRO / CBRI", False, True,
     ["Joshimath town in Chamoli district, Uttarakhand experienced widespread structural cracking and land subsidence, requiring emergency evacuations.",
      "Geologically, Joshimath is not built on solid bedrock but on an ancient unconsolidated landslide debris slope near the Main Central Thrust (MCT).",
      "Mishra Committee (1976) had explicitly warned against heavy civil construction, blasting, excavation of hill slopes, and deforestation around Joshimath."],
     "GS-1: Geomorphology, Himalayan Tectonics, Land Subsidence, Main Central Thrust, Disaster Vulnerability.",
     [
         ("The Main Central Thrust (MCT) in Himalayan geology separates which two major litho-tectonic mountain zones?\n(a) Shiwalik Hills and Lesser Himalayas\n(b) Lesser Himalayas (Himachal) and Greater Himalayas (Himadri)\n(c) Greater Himalayas and Tethys Himalayas\n(d) Indo-Gangetic Plains and Shiwaliks",
          ["(a) Shiwalik Hills and Lesser Himalayas", "(b) Lesser Himalayas (Himachal) and Greater Himalayas (Himadri)", "(c) Greater Himalayas and Tethys Himalayas", "(d) Indo-Gangetic Plains and Shiwaliks"],
          "(b)", "The MCT is a major ductile shear zone separating the low-grade metasedimentary rocks of the Lesser Himalayas from the high-grade crystalline metamorphic rocks of the Higher/Greater Himalayas."),
         ("What is the primary geological reason for the structural ground instability of Joshimath town?\n(a) It is located inside an active volcanic caldera\n(b) It is situated on thick, uncompacted morainic and ancient landslide debris with poor bearing capacity rather than solid in-situ bedrock\n(c) Mining of coal veins under the town\n(d) Rapid rise of the sea level",
          ["(a) It is located inside an active volcanic caldera", "(b) It is situated on thick, uncompacted morainic and ancient landslide debris with poor bearing capacity rather than solid in-situ bedrock", "(c) Mining of coal veins under the town", "(d) Rapid rise of the sea level"],
          "(b)", "Joshimath sits on a pile of loose glacial moraine and landslide rubble deposited centuries ago; lack of subsurface drainage saturates this material, causing gravitational creep and subsidence."),
         ("Which official committee in 1976 first cautioned that Joshimath was resting on a landslide deposit and advised a ban on heavy construction and blasting?\n(a) Kasturirangan Committee\n(b) M.C. Mishra Committee\n(c) Gadgil Commission\n(d) K. Radhakrishnan Committee",
          ["(a) Kasturirangan Committee", "(b) M.C. Mishra Committee", "(c) Gadgil Commission", "(d) K. Radhakrishnan Committee"],
          "(b)", "The 18-member Mishra Committee report in 1976 highlighted that Joshimath is a geological deposit, not solid rock, recommending strict regulation on stone quarrying and hill cutting."),
         ("Which river cuts the deep gorge at the toe of the Joshimath slope, leading to severe toe erosion and slope destabilization?\n(a) Alaknanda River and Dhauliganga confluence\n(b) Bhagirathi River\n(c) Mandakini River\n(d) Pindar River",
          ["(a) Alaknanda River and Dhauliganga confluence", "(b) Bhagirathi River", "(c) Mandakini River", "(d) Pindar River"],
          "(a)", "Joshimath overlooks the confluence of the Alaknanda and Dhauliganga rivers at Vishnuprayag. High-velocity river torrents scour the toe of the slope, pulling the hillside downward."),
         ("Under the Bureau of Indian Standards (BIS) seismic zonation map of India (IS 1893), in which seismic zone is the state of Uttarakhand predominantly located?\n(a) Zone II and III\n(b) Zone IV and Zone V (High to Very High Damage Risk)\n(c) Zone I\n(d) Completely aseismic zone",
          ["(a) Zone II and III", "(b) Zone IV and Zone V (High to Very High Damage Risk)", "(c) Zone I", "(d) Completely aseismic zone"],
          "(b)", "Chamoli district and Joshimath lie in Seismic Zone V, the highest risk zone in India, vulnerable to intense earthquake shaking from ongoing convergence of the Indian and Eurasian plates.")
     ]),

    ("ca-geo-08", "2026-03-29", "Geography", "Sundarbans Delta: Salinity Ingress, Mangrove Retreat & Tropical Cyclones", "ISRO / WWF", False, True,
     ["Sundarbans estuarine delta is experiencing accelerated saltwater intrusion driven by sea-level rise (4.4 mm/year vs 1.7 mm/year global average) and reduced upstream freshwater flow.",
      "Upstream diversion of the Ganga at Farakka Barrage has reduced sediment and freshwater discharge into the Hooghly-Bhagirathi distributaries.",
      "High salinity impairs regeneration of fresh-water loving Sundari trees (Heritiera fomes) and increases the intensity of cyclonic storm surges in the Bay of Bengal."],
     "GS-1: Estuarine Geomorphology, Delta Dynamics, Sea Level Rise, Salinization, Tropical Cyclones.",
     [
         ("The iconic mangrove tree species 'Sundari' (Heritiera fomes) that gives Sundarbans its name belongs to which ecological category?\n(a) Xerophyte\n(b) Freshwater-loving / moderate-salinity true mangrove species\n(c) Submerged hydrophyte\n(d) Epiphytic orchid",
          ["(a) Xerophyte", "(b) Freshwater-loving / moderate-salinity true mangrove species", "(c) Submerged hydrophyte\n", "(d) Epiphytic orchid"],
          "(b)", "Sundari (Heritiera fomes) thrives in low to moderate salinity brackish water; increasing sea salinity causes tip-dieback disease, leading to displacement by high-salinity tolerant Avicennia species."),
         ("What anthropogenic engineering structure in West Bengal regulates freshwater flow into the Bhagirathi-Hooghly river system upstream of the Sundarbans?\n(a) Tehri Dam\n(b) Farakka Barrage\n(c) Hirakud Dam\n(d) Durgapur Barrage",
          ["(a) Tehri Dam", "(b) Farakka Barrage", "(c) Hirakud Dam", "(d) Durgapur Barrage"],
          "(b)", "The Farakka Barrage was built in 1975 to divert 40,000 cusecs of water from the Ganga into the Hooghly to flush silt and keep Kolkata Port navigable, altering downstream estuarine salinity."),
         ("Why is the rate of relative sea-level rise in the Sundarbans delta significantly higher than the global mean sea-level rise?\n(a) Excessive underground magma cooling\n(b) Combination of global eustatic sea-level rise with natural compaction and tectonic subsidence of deltaic sediments\n(c) Inflow of Antarctic icebergs\n(d) High maritime shipping traffic",
          ["(a) Excessive underground magma cooling", "(b) Combination of global eustatic sea-level rise with natural compaction and tectonic subsidence of deltaic sediments", "(c) Inflow of Antarctic icebergs", "(d) High maritime shipping traffic"],
          "(b)", "The delta is undergoing natural subsidence (compaction of heavy alluvial sediments without sufficient replenishment by new silt) coupled with global climate-driven eustatic sea rise."),
         ("In tropical cyclone meteorology, which sector of a northward-moving tropical cyclone in the Bay of Bengal experiences the most destructive storm surge?\n(a) Left-rear quadrant\n(b) Right-forward quadrant\n(c) Left-forward quadrant\n(d) Center of the eye",
          ["(a) Left-rear quadrant\n", "(b) Right-forward quadrant", "(c) Left-forward quadrant", "(d) Center of the eye"],
          "(b)", "In the Northern Hemisphere, cyclonic winds rotate counterclockwise; in the right-forward quadrant, the rotational winds add to the forward translation speed of the cyclone, pushing water ashore."),
         ("Which island in the Indian Sundarbans was completely submerged due to sea-level rise and coastal erosion by 2006, creating some of India's first environmental refugees?\n(a) Sagar Island\n(b) Lohachara Island\n(c) Sandheads\n(d) Henry Island",
          ["(a) Sagar Island", "(b) Lohachara Island", "(c) Sandheads", "(d) Henry Island"],
          "(b)", "Lohachara Island in the Hooghly estuary was officially recorded as submerged in 2006, forcing thousands of residents to relocate to nearby Sagar Island.")
     ]),

    ("ca-geo-09", "2026-02-28", "Geography", "Beach Sand Minerals & Rare Earth Elements (REE): Monazite & IREL Architecture", "Department of Atomic Energy / PIB", False, True,
     ["Beach sand minerals (BSMs) along Indian coasts contain seven valuable heavy minerals: Ilmenite, Rutile, Leucoxene, Garnet, Zircon, Sillimanite, and Monazite.",
      "Monazite is an atomic mineral containing rare earth elements (Cerium, Lanthanum, Neodymium) and radioactive Thorium, regulated under the Atomic Energy Act 1962.",
      "Indian Rare Earths Limited (IREL), a CPSE under DAE, exercises exclusive public monopoly over the mining, processing, and refining of monazite."],
     "GS-1: Distribution of Minerals, Coastal Placers, Heavy Mineral Sands, Rare Earths, Atomic Minerals.",
     [
         ("Monazite sand deposits found along the coasts of Kerala and Tamil Nadu are a principal source of which radioactive nuclear fuel element?\n(a) Uranium-235\n(b) Thorium-232\n(c) Radium-226\n(d) Polonium-210",
          ["(a) Uranium-235", "(b) Thorium-232", "(c) Radium-226", "(d) Polonium-210"],
          "(b)", "Monazite is a phosphate mineral containing rare earths and 8-10% Thorium dioxide (ThO2), vital for Stage 3 of India's nuclear power program."),
         ("Which type of geological deposit accounts for the heavy mineral beach sand deposits of coastal India?\n(a) Magmatic hydrothermal veins\n(b) Placer deposits formed by mechanical concentration of dense weathered minerals by waves and tides\n(c) Deep sea hydrothermal vents\n(d) Sedimentary chemical evaporates",
          ["(a) Magmatic hydrothermal veins", "(b) Placer deposits formed by mechanical concentration of dense weathered minerals by waves and tides", "(c) Deep sea hydrothermal vents", "(d) Sedimentary chemical evaporates"],
          "(b)", "Beach sand minerals are littoral placer deposits: rivers carry weathered crystalline rocks from the Western and Eastern Ghats to the sea, where waves and longshore currents sort heavy minerals."),
         ("Which heavy mineral extracted from beach sand is the primary commercial ore used in the extraction of Titanium metal and white pigments?\n(a) Zircon\n(b) Ilmenite and Rutile\n(c) Sillimanite\n(d) Garnet",
          ["(a) Zircon", "(b) Ilmenite and Rutile", "(c) Sillimanite", "(d) Garnet"],
          "(b)", "Ilmenite (FeTiO3) and Rutile (TiO2) are the primary sources of Titanium metal and titanium dioxide pigment used in aerospace, paints, and defense."),
         ("Under Indian mining law, can private commercial companies mine and extract Monazite independently from beach sands?\n(a) Yes, open to 100% private mining since 2018\n(b) No, monazite mining is legally reserved exclusively for the Government of India through IREL\n(c) Only if partnered with foreign defense firms\n(d) State Governments can license it freely",
          ["(a) Yes, open to 100% private mining since 2018", "(b) No, monazite mining is legally reserved exclusively for the Government of India through IREL", "(c) Only if partnered with foreign defense firms", "(d) State Governments can license it freely"],
          "(b)", "Due to radioactive Thorium and strategic atomic significance, Monazite is classified as a prescribed substance under the Atomic Energy Act, mined exclusively by IREL (India) Ltd."),
         ("Which two Rare Earth Elements (REEs) are indispensable components in the manufacture of high-strength Neodymium-Iron-Boron (NdFeB) permanent magnets for electric vehicles and wind turbines?\n(a) Neodymium and Dysprosium\n(b) Helium and Argon\n(c) Calcium and Silicon\n(d) Zinc and Lead",
          ["(a) Neodymium and Dysprosium", "(b) Helium and Argon", "(c) Calcium and Silicon", "(d) Zinc and Lead"],
          "(a)", "Permanent magnets (NdFeB) require Neodymium for magnetic field strength and Dysprosium/Praseodymium to retain magnetism at high operating temperatures in EV motors.")
     ]),

    ("ca-geo-10", "2026-01-28", "Geography", "Major Maritime Straits & Global Shipping Chokepoints: Strategic Geography", "Ministry of Ports / IMO", True, True,
     ["Global maritime trade depends on critical narrow oceanic passages: Strait of Malacca, Strait of Hormuz, Bab-el-Mandeb, Turkish Straits (Bosporus and Dardanelles), and Panama Canal.",
      "Strait of Hormuz is the world's most critical petroleum chokepoint, handling ~21 million barrels/day (~21% of global petroleum liquids consumption).",
      "Bab-el-Mandeb connects the Red Sea to the Gulf of Aden; disruptions there force cargo ships around the Cape of Good Hope, adding 10-14 days transit time."],
     "GS-1: World Geography, Maritime Chokepoints, Strait of Hormuz, Bab-el-Mandeb, Global Shipping Corridors.",
     [
         ("The strategic Strait of Hormuz connects which two major bodies of water?\n(a) Red Sea and Gulf of Aden\n(b) Persian Gulf and Gulf of Oman (leading to the Arabian Sea)\n(c) Mediterranean Sea and Black Sea\n(d) South China Sea and Pacific Ocean",
          ["(a) Red Sea and Gulf of Aden", "(b) Persian Gulf and Gulf of Oman (leading to the Arabian Sea)", "(c) Mediterranean Sea and Black Sea", "(d) South China Sea and Pacific Ocean"],
          "(b)", "The Strait of Hormuz lies between Oman and Iran, connecting the Persian Gulf with the Gulf of Oman and the wider Indian Ocean."),
         ("Which two European / Asian waterways are separated by the Bosporus and Dardanelles straits (Turkish Straits)?\n(a) Black Sea and Sea of Marmara / Aegean Sea\n(b) Baltic Sea and North Sea\n(c) Red Sea and Dead Sea\n(d) Caspian Sea and Aral Sea",
          ["(a) Black Sea and Sea of Marmara / Aegean Sea", "(b) Baltic Sea and North Sea", "(c) Red Sea and Dead Sea", "(d) Caspian Sea and Aral Sea"],
          "(a)", "The Bosporus connects the Black Sea to the Sea of Marmara; the Dardanelles connects the Sea of Marmara to the Aegean Sea (Mediterranean), forming the boundary between Europe and Asia in Turkey."),
         ("Which 1936 international convention regulates maritime transit through the Turkish Straits (Bosporus and Dardanelles) during peacetime and wartime?\n(a) Montreux Convention\n(b) UNCLOS 1982\n(c) Treaty of Versailles\n(d) Geneva Convention",
          ["(a) Montreux Convention", "(b) UNCLOS 1982", "(c) Treaty of Versailles", "(d) Geneva Convention"],
          "(a)", "The Montreux Convention Regarding the Regime of the Straits gives Turkey control over the Turkish Straits and regulates transit of civilian cargo and naval warships."),
         ("The Strait of Gibraltar connects the Atlantic Ocean to the Mediterranean Sea and separates which two continents?\n(a) Asia and Africa\n(b) Europe (Spain) and Africa (Morocco)\n(c) North America and South America\n(d) Europe and Asia",
          ["(a) Asia and Africa", "(b) Europe (Spain) and Africa (Morocco)", "(c) North America and South America", "(d) Europe and Asia"],
          "(b)", "The Strait of Gibraltar is a 13-km wide maritime corridor separating the Iberian Peninsula of Spain in Europe from Morocco in North Africa."),
         ("What type of canal lock system is utilized by the Panama Canal to lift ships across the continental divide of the Isthmus of Panama?\n(a) Sea-level open canal like the Suez Canal\n(b) Gravity-fed freshwater lock system using Gatun Lake\n(c) Nuclear hydraulic pumps\n(d) Subterranean rail rollers",
          ["(a) Sea-level open canal like the Suez Canal", "(b) Gravity-fed freshwater lock system using Gatun Lake", "(c) Nuclear hydraulic pumps", "(d) Subterranean rail rollers"],
          "(b)", "Unlike the sea-level Suez Canal, the Panama Canal uses three sets of locks to lift vessels 26 meters above sea level to Gatun Lake and lower them on the other side.")
     ]),

    ("ca-geo-11", "2026-10-28", "Geography", "Western Ghats Ecologically Sensitive Area (ESA) Notification: Gadgil vs Kasturirangan", "MoEFCC / Down to Earth", True, True,
     ["MoEFCC re-issued the draft notification declaring 56,825 sq km across six states as Western Ghats Ecologically Sensitive Area (ESA).",
      "Western Ghats is one of the world's eight 'hottest hotspots' of biological diversity, older than the Himalayas, functioning as the water tower of peninsular India.",
      "Debate persists between the Madhav Gadgil Report (recommended 100% of Western Ghats as ecologically sensitive under 3 graded zones) and Kasturirangan Report (recommended protecting 37% as natural landscape)."],
     "GS-1: Western Ghats, Biodiversity Hotspots, Gadgil vs Kasturirangan, Ecologically Sensitive Areas, Wayanad Landslides.",
     [
         ("The Western Ghats mountain range spans across how many Indian States?\n(a) 4 States\n(b) 6 States (Gujarat, Maharashtra, Goa, Karnataka, Kerala, Tamil Nadu)\n(c) 8 States\n(d) 10 States",
          ["(a) 4 States", "(b) 6 States (Gujarat, Maharashtra, Goa, Karnataka, Kerala, Tamil Nadu)", "(c) 8 States", "(d) 10 States"],
          "(b)", "The 1,600 km Western Ghats mountain chain runs parallel to India's western coast across Gujarat, Maharashtra, Goa, Karnataka, Kerala, and Tamil Nadu."),
         ("What major proportion of the Western Ghats did the High-Level Working Group chaired by Dr. K. Kasturirangan recommend designating as an Ecologically Sensitive Area (ESA)?\n(a) 100% of the Western Ghats\n(b) Approximately 37% (classified as natural landscapes)\n(c) Only 10%\n(d) Zero percent",
          ["(a) 100% of the Western Ghats", "(b) Approximately 37% (classified as natural landscapes)", "(c) Only 10%", "(d) Zero percent"],
          "(b)", "Kasturirangan divided the Ghats into cultural landscape (63% with human settlements/plantations) and natural landscape (37% containing dense forests/protected areas), recommending ESA for the 37%."),
         ("The Western Ghats Ecology Expert Panel (WGEEP) that advocated bottom-up participatory environmental governance was headed by:\n(a) Prof. Madhav Gadgil\n(b) Dr. M.S. Swaminathan\n(c) Sunita Narain\n(d) Jairam Ramesh",
          ["(a) Prof. Madhav Gadgil", "(b) Dr. M.S. Swaminathan", "(c) Sunita Narain", "(d) Jairam Ramesh"],
          "(a)", "The Gadgil Commission (2011) recommended classifying the entire Western Ghats into three Ecologically Sensitive Zones (ESZ-1, ESZ-2, ESZ-3) with a complete ban on mining in ESZ-1."),
         ("What is the highest mountain peak in the Western Ghats and peninsular India?\n(a) Doddabetta\n(b) Anamudi\n(c) Kudremukh\n(d) Kalsubai",
          ["(a) Doddabetta\n", "(b) Anamudi", "(c) Kudremukh", "(d) Kalsubai"],
          "(b)", "Anamudi (2,695 meters) located in the Anamalai Hills of Eravikulam National Park in Kerala is the highest peak in peninsular India (Doddabetta is the highest peak in the Nilgiris at 2,637 m)."),
         ("Which prominent natural mountain pass in the Western Ghats breaks the continuous ridge between the Nilgiri Hills to the north and the Anamalai Hills to the south?\n(a) Thal Ghat\n(b) Bhor Ghat\n(c) Palghat Gap (Palakkad Gap)\n(d) Shencottah Gap",
          ["(a) Thal Ghat", "(b) Bhor Ghat", "(c) Palghat Gap (Palakkad Gap)", "(d) Shencottah Gap"],
          "(c)", "The 30-km wide Palghat Gap is a major tectonic shear discontinuity in the Western Ghats connecting Tamil Nadu (Coimbatore) with Kerala (Palakkad).")
     ]),

    ("ca-geo-12", "2026-09-22", "Geography", "Urban Heat Island (UHI) Effect & Microclimate Modification in Metros", "IMD / CSE", False, False,
     ["The Urban Heat Island (UHI) effect causes urbanized metropolitan cores to record temperatures 3°C to 7°C higher than surrounding rural peripheries.",
      "Driven by low-albedo concrete and asphalt pavements absorbing solar radiation, tall building canyons trapping heat, loss of vegetation evapotranspiration, and anthropogenic heat from ACs.",
      "Cool Roof policies, permeable pavements, reflective coatings, and blue-green infrastructure (urban waterbodies and parks) are essential adaptation measures."],
     "GS-1: Urban Climatology, Urban Heat Island Effect, Albedo, Cool Roofs, Microclimates.",
     [
         ("The Urban Heat Island (UHI) effect is primarily driven by which physical surface characteristic of modern cities?\n(a) Abundant natural vegetative cover\n(b) High prevalence of low-albedo impervious surfaces (asphalt and concrete) that absorb and re-radiate shortwave solar radiation as sensible heat\n(c) Excessive groundwater recharge\n(d) Absence of high-rise structures",
          ["(a) Abundant natural vegetative cover", "(b) High prevalence of low-albedo impervious surfaces (asphalt and concrete) that absorb and re-radiate shortwave solar radiation as sensible heat", "(c) Excessive groundwater recharge", "(d) Absence of high-rise structures"],
          "(b)", "Concrete and bitumen have low albedo (reflectivity) and high thermal mass, storing daytime solar energy and releasing it at night, preventing urban nocturnal cooling."),
         ("What is meant by the physical term 'Albedo'?\n(a) The thermal conductivity of electrical cables\n(b) The fraction of total incident solar radiation reflected by a surface without being absorbed\n(c) The rate of atmospheric chemical oxidation\n(d) The humidity level in tropical air",
          ["(a) The thermal conductivity of electrical cables", "(b) The fraction of total incident solar radiation reflected by a surface without being absorbed", "(c) The rate of atmospheric chemical oxidation", "(d) The humidity level in tropical air"],
          "(b)", "Albedo is dimensionless reflectivity (0 to 1). Fresh snow has high albedo (~0.8-0.9), while black asphalt has very low albedo (~0.05-0.10)."),
         ("How does the loss of urban vegetative canopy and wetlands intensify the Urban Heat Island phenomenon?\n(a) By reducing natural cooling caused by evapotranspiration\n(b) By increasing volcanic gas vents\n(c) By causing direct solar eclipse\n(d) By doubling wind velocity",
          ["(a) By reducing natural cooling caused by evapotranspiration", "(b) By increasing volcanic gas vents", "(c) By causing direct solar eclipse", "(d) By doubling wind velocity"],
          "(a)", "Trees and plants cool ambient air through evapotranspiration (converting sensible heat into latent heat of water vapor). Replacing green cover with concrete removes this natural evaporative cooling."),
         ("What do 'Cool Roofs' utilize to reduce building indoor temperatures and mitigate the urban heat island effect?\n(a) Thick layers of black bitumen tar\n(b) High Solar Reflectance Index (SRI) reflective paints, broken white tiles, or green vegetated roof gardens\n(c) Lead shielding\n(d) Continuous diesel-powered air blowers",
          ["(a) Thick layers of black bitumen tar", "(b) High Solar Reflectance Index (SRI) reflective paints, broken white tiles, or green vegetated roof gardens", "(c) Lead shielding", "(d) Continuous diesel-powered air blowers"],
          "(b)", "Cool roofs use materials with high solar reflectance (reflecting sunlight) and high thermal emittance (radiating absorbed heat), keeping building envelopes significantly cooler."),
         ("Which Indian state became the first in the country to launch an official, mandatory state-wide 'Cool Roof Policy' (2023-2028)?\n(a) Telangana\n(b) Kerala\n(c) Rajasthan\n(d) Maharashtra",
          ["(a) Telangana", "(b) Kerala", "(c) Rajasthan", "(d) Maharashtra"],
          "(a)", "Telangana launched India's first state Cool Roof Policy targeting 200 sq km of cool roofs in Hyderabad by 2030 to enhance thermal comfort and lower peak electricity loads.")
     ])
]

all_geo = [make_art(aid, dt, pil, tit, src, top, pt, sums, gs, qs) for aid, dt, pil, tit, src, top, pt, sums, gs, qs in geo_articles]
print(f"Total Geography articles: {len(all_geo)}")
assert len(all_geo) == 12, f"Expected 12, got {len(all_geo)}"

with open(os.path.join(BASE_DIR, 'data', 'ca_builders', 'geography.json'), 'w') as f:
    json.dump(all_geo, f, indent=2)

print("Saved geography.json successfully!")
