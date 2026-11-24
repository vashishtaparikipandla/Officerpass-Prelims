#!/usr/bin/env python3
"""
Builds Science & Technology articles (ca-sci-01 to ca-sci-15: total 15 articles)
"""
import json
import os

BASE_DIR = '/Users/vashishtaparikipandla/Documents/OfficerPass'
with open(os.path.join(BASE_DIR, 'data', 'current-affairs-db.json')) as f:
    existing = json.load(f)

sci1_2 = [a for a in existing if a['pillar'] == 'SciTech']

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

sci_new = [
    ("ca-sci-03", "2026-10-22", "SciTech", "Gaganyaan Mission: Crew Escape System & Vyommitra Humanoid Trials", "ISRO / PIB", True, True,
     ["Gaganyaan is India's first human spaceflight mission aiming to launch a 3-member crew into a 400 km Low Earth Orbit (LEO) for a 3-day mission.",
      "The Launch Vehicle Mark-3 (LVM3) is human-rated as the launch vehicle, equipped with a Crew Escape System (CES) for emergency aborts.",
      "ISRO designed 'Vyommitra', a female spacefaring humanoid robot to monitor life-support systems and module parameters during uncrewed test flights."],
     "GS-3: Space Technology, Human Spaceflight, ISRO Missions, Launch Vehicle Mark-3, Robotics.",
     [
         ("Which launch vehicle has been human-rated by ISRO to launch the Gaganyaan crew module into orbit?\n(a) PSLV-XL\n(b) GSLV Mk II\n(c) Launch Vehicle Mark-3 (LVM3 / GSLV Mk III)\n(d) Small Satellite Launch Vehicle (SSLV)",
          ["(a) PSLV-XL", "(b) GSLV Mk II", "(c) Launch Vehicle Mark-3 (LVM3 / GSLV Mk III)", "(d) Small Satellite Launch Vehicle (SSLV)"],
          "(c)", "The heavy-lift LVM3 rocket was re-engineered and human-rated with redundant avionics and safety margins as the HLVM3 for Gaganyaan."),
         ("What is the primary function of ISRO's female humanoid robot 'Vyommitra' in the Gaganyaan program?\n(a) To pilot the spacecraft without ground control\n(b) To simulate human physiological responses and monitor environmental control and life-support systems (ECLSS) during uncrewed flights\n(c) To conduct spacewalks outside the crew module\n(d) To repair external heat shield tiles",
          ["(a) To pilot the spacecraft without ground control", "(b) To simulate human physiological responses and monitor environmental control and life-support systems (ECLSS) during uncrewed flights", "(c) To conduct spacewalks outside the crew module", "(d) To repair external heat shield tiles"],
          "(b)", "Vyommitra is a half-humanoid robot designed to operate switch panels, monitor ECLSS parameters, read cabin pressure, and test communications before astronaut flights."),
         ("At what altitude and orbital inclination will the Gaganyaan crew module orbit the Earth?\n(a) Geostationary Orbit at 36,000 km\n(b) Low Earth Orbit (LEO) at ~400 km\n(c) Sun-Synchronous Polar Orbit at 800 km\n(d) Lagrange Point L1 at 1.5 million km",
          ["(a) Geostationary Orbit at 36,000 km", "(b) Low Earth Orbit (LEO) at ~400 km", "(c) Sun-Synchronous Polar Orbit at 800 km", "(d) Lagrange Point L1 at 1.5 million km"],
          "(b)", "Gaganyaan will insert a 3-member crew into a 400 km circular Low Earth Orbit (LEO) for a 3-day mission before de-orbiting for splashdown."),
         ("Where is the designated landing recovery zone for the Gaganyaan crew module following atmospheric re-entry?\n(a) Thar Desert sand dunes\n(b) Bay of Bengal or Arabian Sea waters off the Indian coast\n(c) Lake Chilika\n(d) Rann of Kutch",
          ["(a) Thar Desert sand dunes", "(b) Bay of Bengal or Arabian Sea waters off the Indian coast", "(c) Lake Chilika", "(d) Rann of Kutch"],
          "(b)", "The crew module will parachute into the Arabian Sea / Bay of Bengal with recovery operations coordinated by the Indian Navy and Coast Guard."),
         ("What specialized training institute in Bengaluru conducts human engineering, space medicine, and astronaut fitness for the Indian Air Force test pilots selected for Gaganyaan?\n(a) Institute of Aerospace Medicine (IAM)\n(b) National Institute of Mental Health (NIMHANS)\n(c) Defence Bioengineering and Electromedical Laboratory (DEBEL)\n(d) Vikram Sarabhai Space Centre",
          ["(a) Institute of Aerospace Medicine (IAM)", "(b) National Institute of Mental Health (NIMHANS)", "(c) Defence Bioengineering and Electromedical Laboratory (DEBEL)", "(d) Vikram Sarabhai Space Centre"],
          "(a)", "The Indian Air Force's Institute of Aerospace Medicine (IAM) in Bengaluru is the premier agency for aeromedical evaluation and astronaut conditioning.")
     ]),

    ("ca-sci-04", "2026-09-15", "SciTech", "BioE3 Policy: Biotechnology for Economy, Environment & Employment", "DBT / PIB", True, True,
     ["Cabinet approved the BioE3 (Biotechnology for Economy, Environment and Employment) Policy driven by the Department of Biotechnology (DBT).",
      "Focuses on High-Performance Biomanufacturing across 6 thematic sectors including bio-based chemicals, smart proteins, precision biotherapeutics, and carbon capture.",
      "Establishes Bio-enablers Hubs and Biofoundries to bridge the gap between laboratory synthesis and commercial industrial scale fermentation."],
     "GS-3: Biotechnology, Biomanufacturing, Industrial Policy, Circular Bioeconomy, Department of Biotechnology.",
     [
         ("The 'BioE3' Policy recently approved by the Union Cabinet stands for:\n(a) Biotechnology for Ecology, Energy, and Education\n(b) Biotechnology for Economy, Environment, and Employment\n(c) Biofuels, Electronics, and Electric Engineering\n(d) Biodiversity, Ecosystems, and Economic Evaluation",
          ["(a) Biotechnology for Ecology, Energy, and Education", "(b) Biotechnology for Economy, Environment, and Employment", "(c) Biofuels, Electronics, and Electric Engineering", "(d) Biodiversity, Ecosystems, and Economic Evaluation"],
          "(b)", "BioE3 stands for Biotechnology for Economy, Environment, and Employment, aiming to foster a high-performance biomanufacturing ecosystem."),
         ("What is the primary role of 'Biofoundries' in the context of the BioE3 policy?\n(a) Mining heavy metals from microbial deposits\n(b) Automated facilities that design, build, and test engineered biological systems at industrial scale using synthetic biology\n(c) Recycling agricultural organic compost\n(d) Breeding genetically modified cattle",
          ["(a) Mining heavy metals from microbial deposits", "(b) Automated facilities that design, build, and test engineered biological systems at industrial scale using synthetic biology", "(c) Recycling agricultural organic compost", "(d) Breeding genetically modified cattle"],
          "(b)", "Biofoundries integrate robotics, high-throughput screening, and machine learning to accelerate Design-Build-Test-Learn cycles in synthetic biology."),
         ("Which of the following is considered a 'Smart Protein' under modern biotechnology classification?\n1. Plant-based meat alternatives\n2. Fermentation-derived cellular protein\n3. Cultivated / cell-based meat grown in bioreactors\nSelect the correct answer:",
          ["(a) 1 only", "(b) 1 and 2 only", "(c) 2 and 3 only", "(d) 1, 2 and 3"],
          "(d)", "Smart proteins encompass plant-based alternatives, microbial fermentation biomass, and cultivated meat grown from animal cell cultures without livestock slaughter."),
         ("Under the BioE3 policy, which public sector entity under the DBT acts as the interface for funding biomanufacturing startups and commercial translation?\n(a) Biotechnology Industry Research Assistance Council (BIRAC)\n(b) Council of Scientific and Industrial Research (CSIR)\n(c) Indian Council of Medical Research (ICMR)\n(d) Technology Development Board (TDB)",
          ["(a) Biotechnology Industry Research Assistance Council (BIRAC)", "(b) Council of Scientific and Industrial Research (CSIR)", "(c) Indian Council of Medical Research (ICMR)", "(d) Technology Development Board (TDB)"],
          "(a)", "BIRAC (a Section 8 not-for-profit enterprise of DBT) manages biotech incubation, seed funding, and commercial translational partnerships in India."),
         ("How does biomanufacturing contribute to industrial decarbonization compared to traditional petrochemical manufacturing?\n(a) It replaces fossil feedstocks with biological raw materials using enzymes and microbes at lower temperatures and pressures\n(b) It consumes nuclear energy directly\n(c) It turns all carbon emissions into liquid hydrogen\n(d) It completely eliminates the need for water",
          ["(a) It replaces fossil feedstocks with biological raw materials using enzymes and microbes at lower temperatures and pressures", "(b) It consumes nuclear energy directly", "(c) It turns all carbon emissions into liquid hydrogen", "(d) It completely eliminates the need for water"],
          "(a)", "Biomanufacturing uses engineered microorganisms and biocatalysts to produce plastics, enzymes, and chemicals under mild conditions, reducing carbon footprints by up to 80%.")
     ]),

    ("ca-sci-05", "2026-08-18", "SciTech", "National Quantum Mission (NQM): Quantum Computing & Quantum Communication Hubs", "DST / PIB", True, True,
     ["Approved with a budget outlay of Rs 6,003 crore over 2023-2031, implemented by the Department of Science and Technology (DST).",
      "Targets developing intermediate scale quantum computers with 50-1000 physical qubits across superconducting and photonic platforms.",
      "Aims to achieve secure Quantum Key Distribution (QKD) over ground stations up to 2,000 km and inter-city satellite-based quantum communications."],
     "GS-3: Quantum Computing, Cryptography, QKD, National Quantum Mission, Department of Science & Technology.",
     [
         ("The fundamental unit of information in a quantum computer is called a:\n(a) Byte\n(b) Qubit (Quantum Bit)\n(c) Transistor\n(d) Nanobit",
          ["(a) Byte", "(b) Qubit (Quantum Bit)", "(c) Transistor", "(d) Nanobit"],
          "(b)", "While classical computers use binary bits (0 or 1), quantum computers utilize qubits which can exist as 0, 1, or both simultaneously due to superposition."),
         ("Which two fundamental principles of quantum mechanics give quantum computers their exponential computational power over classical computers?\n(a) Superposition and Quantum Entanglement\n(b) Newton's third law and Brownian motion\n(c) Thermal convection and radiation\n(d) Photoelectric effect and Compton scattering",
          ["(a) Superposition and Quantum Entanglement", "(b) Newton's third law and Brownian motion", "(c) Thermal convection and radiation", "(d) Photoelectric effect and Compton scattering"],
          "(a)", "Superposition allows qubits to process multiple combinations simultaneously; Entanglement links qubits so the state of one instantly influences another regardless of distance."),
         ("What is the primary technological capability of Quantum Key Distribution (QKD)?\n(a) Instantaneous transmission of physical objects across space\n(b) Unconditionally secure communication where any eavesdropping attempt disturbs the quantum state and is immediately detected\n(c) Mining cryptocurrency at zero electrical cost\n(d) Replacing wireless radio towers",
          ["(a) Instantaneous transmission of physical objects across space", "(b) Unconditionally secure communication where any eavesdropping attempt disturbs the quantum state and is immediately detected\n", "(c) Mining cryptocurrency at zero electrical cost", "(d) Replacing wireless radio towers"],
          "(b)", "QKD uses photons to transmit encryption keys. By Heisenberg's Uncertainty Principle, any interception alters photon quantum states, exposing the interception."),
         ("Under the National Quantum Mission, how many Thematic Hubs (T-Hubs) are being established across India?\n(a) Two\n(b) Four\n(c) Eight\n(d) Twelve",
          ["(a) Two", "(b) Four", "(c) Eight", "(d) Twelve"],
          "(b)", "The Mission establishes four T-Hubs: Quantum Computing, Quantum Communication, Quantum Sensing & Metrology, and Quantum Materials & Devices."),
         ("Why do many current superconducting quantum computers require dilution refrigerators cooled close to Absolute Zero (-273.15°C)?\n(a) To prevent laser melting of the chassis\n(b) To eliminate thermal noise and preserve quantum coherence of qubits\n(c) To conduct chemical photosynthesis\n(d) To freeze digital malware",
          ["(a) To prevent laser melting of the chassis", "(b) To eliminate thermal noise and preserve quantum coherence of qubits", "(c) To conduct chemical photosynthesis", "(d) To freeze digital malware"],
          "(b)", "Thermal vibrations destroy delicate quantum states (decoherence). Superconducting qubits require millikelvin temperatures near absolute zero to maintain superposition.")
     ]),

    ("ca-sci-06", "2026-07-28", "SciTech", "India Semiconductor Mission (ISM): Dholera Commercial Fab & OSAT Ecosystem", "MeitY / PIB", True, True,
     ["India Semiconductor Mission (ISM) provides 50% fiscal support on a pari-passu basis for setting up silicon semiconductor fabs and display fabs.",
      "First commercial semiconductor fabrication facility approved at Dholera, Gujarat (Tata Electronics in partnership with PSMC Taiwan).",
      "Focuses on developing the full semiconductor value chain: Silicon Fabs, Compound Semiconductors, Outsourced Semiconductor Assembly and Test (OSAT), and ATMP."],
     "GS-3: Semiconductors, Microelectronics, ISM, Supply Chain Resilience, Electronics Manufacturing.",
     [
         ("Under the modified Semicon India program, what percentage of the project cost is provided as fiscal support by the Central Government on a pari-passu basis?\n(a) 25%\n(b) 50%\n(c) 75%\n(d) 100%",
          ["(a) 25%", "(b) 50%", "(c) 75%", "(d) 100%"],
          "(b)", "The Union Cabinet streamlined the incentive to a uniform 50% fiscal support of project cost across all technology nodes for silicon fabs, display fabs, and OSAT facilities."),
         ("India's first commercial semiconductor fabrication facility has been established at which location?\n(a) Sriperumbudur, Tamil Nadu\n(b) Dholera, Gujarat\n(c) Noida, Uttar Pradesh\n(d) Whitefield, Bengaluru",
          ["(a) Sriperumbudur, Tamil Nadu", "(b) Dholera, Gujarat", "(c) Noida, Uttar Pradesh", "(d) Whitefield, Bengaluru"],
          "(b)", "Tata Electronics partnering with Taiwan's Powerchip Semiconductor Manufacturing Corp (PSMC) established India's first commercial mega-fab at Dholera Smart City, Gujarat."),
         ("In semiconductor manufacturing terminology, what does 'OSAT' stand for?\n(a) Open Source Automated Technology\n(b) Outsourced Semiconductor Assembly and Test\n(c) Optical Silicon Architecture Transport\n(d) Overhead Silicon Alignment Tool",
          ["(a) Open Source Automated Technology", "(b) Outsourced Semiconductor Assembly and Test", "(c) Optical Silicon Architecture Transport", "(d) Overhead Silicon Alignment Tool"],
          "(b)", "OSAT (Outsourced Semiconductor Assembly and Test) companies take fabricated silicon wafers, dice them into individual chips, package them, and test their performance."),
         ("What chemical element is the overwhelmingly predominant raw semiconductor material used in modern integrated circuits (ICs)?\n(a) Germanium\n(b) Silicon\n(c) Gallium\n(d) Copper",
          ["(a) Germanium", "(b) Silicon", "(c) Gallium", "(d) Copper"],
          "(b)", "Silicon is the foundation of modern microelectronics due to its natural abundance (derived from silica sand), stable oxide (SiO2), and favorable bandgap."),
         ("Which government research laboratory in Chandigarh has historically maintained India's premier public semiconductor fabrication facility?\n(a) Semi-Conductor Laboratory (SCL)\n(b) National Physical Laboratory\n(c) CSIR-CEERI Pilani\n(d) DRDO SSPL",
          ["(a) Semi-Conductor Laboratory (SCL)", "(b) National Physical Laboratory", "(c) CSIR-CEERI Pilani", "(d) DRDO SSPL"],
          "(a)", "Semi-Conductor Laboratory (SCL) in Mohali, Punjab (near Chandigarh) is an autonomous body under MeitY producing specialized chips for space and defense missions.")
     ]),

    ("ca-sci-07", "2026-06-18", "SciTech", "Generative AI Governance, MeitY Advisory & Deepfake Regulation", "MeitY / Indian Express", True, False,
     ["MeitY issued advisories under the Information Technology (Intermediary Guidelines and Digital Media Ethics Code) Rules, 2021 regarding AI deepfakes.",
      "Mandates that social media intermediaries must remove synthetic misinformation and non-consensual deepfakes within 24 to 36 hours of notification.",
      "Requires platforms to label AI-generated synthetic content with visible watermarks and metadata to prevent voter manipulation and digital fraud."],
     "GS-3: Artificial Intelligence, Deepfakes, Cyber Security, IT Rules 2021, Algorithmic Bias.",
     [
         ("The technology enabling the creation of hyper-realistic synthetic media, commonly known as 'Deepfakes', is primarily based on:\n(a) Generative Adversarial Networks (GANs) and Diffusion Models\n(b) Classical Relational Database Management Systems\n(c) Blockchain Proof of Work\n(d) Linear regression algorithms",
          ["(a) Generative Adversarial Networks (GANs) and Diffusion Models", "(b) Classical Relational Database Management Systems", "(c) Blockchain Proof of Work", "(d) Linear regression algorithms"],
          "(a)", "Deepfakes utilize Generative Adversarial Networks (GANs)—consisting of a generator pitted against a discriminator network—to create synthetic faces, voices, and videos."),
         ("Under the Information Technology (Intermediary Guidelines) Rules, 2021, what is the maximum statutory timeline for an intermediary to take down non-consensual explicit deepfakes?\n(a) 24 hours\n(b) 36 hours\n(c) 72 hours\n(d) 7 days",
          ["(a) 24 hours", "(b) 36 hours", "(c) 72 hours", "(d) 7 days"],
          "(a)", "Under Rule 3(2)(b), intermediaries must remove or disable access to content exposing the private area of an individual or depicting impersonation/nudity within 24 hours."),
         ("Which section of the Information Technology Act, 2000 provides 'Safe Harbour' protection to online intermediaries from liability for third-party user content?\n(a) Section 66A\n(b) Section 69A\n(c) Section 79\n(d) Section 43A",
          ["(a) Section 66A", "(b) Section 69A", "(c) Section 79", "(d) Section 43A"],
          "(c)", "Section 79 provides conditional safe harbour to intermediaries, provided they observe due diligence and comply with government takedown notices under the IT Rules."),
         ("The European Union's landmark legislation establishing a comprehensive, risk-based framework for regulating artificial intelligence is the:\n(a) EU Artificial Intelligence Act\n(b) Digital Services Act\n(c) GDPR 2.0\n(d) Turing Compliance Directive",
          ["(a) EU Artificial Intelligence Act", "(b) Digital Services Act", "(c) GDPR 2.0", "(d) Turing Compliance Directive"],
          "(a)", "The EU AI Act classifies AI systems by risk (Unacceptable, High, Limited, Minimal) and bans cognitive behavioral manipulation and untargeted facial scraping."),
         ("What digital mechanism is embedded into image and video files to cryptographically prove provenance and authenticity?\n(a) C2PA (Coalition for Content Provenance and Authenticity) digital watermarking\n(b) QR codes on physical packaging\n(c) Magnetic tape strip\n(d) IP address geotagging",
          ["(a) C2PA (Coalition for Content Provenance and Authenticity) digital watermarking", "(b) QR codes on physical packaging", "(c) Magnetic tape strip", "(d) IP address geotagging"],
          "(a)", "C2PA standards attach tamper-evident cryptographic metadata (Content Credentials) to media files, indicating whether generative AI tools were used during creation.")
     ]),

    ("ca-sci-08", "2026-05-24", "SciTech", "Prototype Fast Breeder Reactor (PFBR) Kalpakkam & Core Loading Milestone", "DAE / PIB", True, True,
     ["Core loading commenced at the 500 MWe Prototype Fast Breeder Reactor (PFBR) at Kalpakkam, Tamil Nadu, marking entry into Stage 2 of India's Nuclear Program.",
      "PFBR uses Mixed Oxide (MOX) fuel of Uranium-238 and Plutonium-239 with liquid sodium as coolant, operating without a neutron moderator.",
      "Called a 'breeder' because it produces more fissile material (Pu-239) than it consumes, paving the way for Stage 3 Thorium-232 utilization."],
     "GS-3: Nuclear Energy, Homi Bhabha Three-Stage Program, PFBR Kalpakkam, Thorium Utilization, DAE.",
     [
         ("The commencement of core loading at the Prototype Fast Breeder Reactor (PFBR) at Kalpakkam signifies India's transition to which stage of its nuclear power program?\n(a) Stage 1\n(b) Stage 2\n(c) Stage 3\n(d) Stage 4",
          ["(a) Stage 1", "(b) Stage 2", "(c) Stage 3", "(d) Stage 4"],
          "(b)", "India's 3-Stage Program formulated by Dr. Homi Bhabha: Stage 1 (PHWRs using natural uranium), Stage 2 (Fast Breeder Reactors using plutonium), Stage 3 (Thorium-based Advanced Heavy Water Reactors)."),
         ("What coolant material is utilized in the Prototype Fast Breeder Reactor at Kalpakkam?\n(a) Heavy Water (D2O)\n(b) Light Water (H2O)\n(c) Liquid Sodium\n(d) Pressurized Carbon Dioxide gas",
          ["(a) Heavy Water (D2O)", "(b) Light Water (H2O)", "(c) Liquid Sodium", "(d) Pressurized Carbon Dioxide gas"],
          "(c)", "Fast breeder reactors require fast neutrons (un-moderated) to breed fuel. Liquid sodium has excellent thermal conductivity without moderating (slowing down) neutrons."),
         ("Why is a reactor called a 'Breeder Reactor'?\n(a) It breeds microorganisms in cooling ponds\n(b) It produces more fissile material than it consumes in the fission chain reaction\n(c) It can operate without any nuclear fuel\n(d) It operates only on solar panels",
          ["(a) It breeds microorganisms in cooling ponds", "(b) It produces more fissile material than it consumes in the fission chain reaction", "(c) It can operate without any nuclear fuel", "(d) It operates only on solar panels"],
          "(b)", "Fast neutrons convert fertile Uranium-238 into fissile Plutonium-239 at a breeding ratio greater than 1, yielding more fissile fuel than consumed."),
         ("Which abundant mineral found in the beach sands of Kerala, Tamil Nadu, and Odisha is the key to Stage 3 of India's nuclear program?\n(a) Bauxite\n(b) Monazite (Thorium-232)\n(c) Hematite\n(d) Ilmenite",
          ["(a) Bauxite", "(b) Monazite (Thorium-232)", "(c) Hematite", "(d) Ilmenite"],
          "(b)", "India possesses ~25% of the world's Thorium reserves in monazite beach sands. Stage 2 breeders produce the fissile U-233 seed required to fuel Stage 3 Thorium reactors."),
         ("Which public sector enterprise under the Department of Atomic Energy (DAE) was incorporated to build and operate fast breeder reactors in India?\n(a) Nuclear Power Corporation of India Limited (NPCIL)\n(b) Bharatiya Nabhikiya Vidyut Nigam Limited (BHAVINI)\n(c) Uranium Corporation of India Limited (UCIL)\n(d) Heavy Water Board (HWB)",
          ["(a) Nuclear Power Corporation of India Limited (NPCIL)", "(b) Bharatiya Nabhikiya Vidyut Nigam Limited (BHAVINI)", "(c) Uranium Corporation of India Limited (UCIL)", "(d) Heavy Water Board (HWB)"],
          "(b)", "BHAVINI is the dedicated PSU set up in 2003 under DAE specifically to construct, commission, and operate the commercial fast breeder reactor fleet.")
     ]),

    ("ca-sci-09", "2026-04-14", "SciTech", "CRISPR-Cas9 Sickle Cell Disease Gene Therapy: Casgevy Regulatory Approvals", "Nature / WHO", True, True,
     ["Casgevy (exagamglogene autotemcel) became the world's first licensed therapy utilizing CRISPR-Cas9 genome editing technology for Sickle Cell Disease and Beta-Thalassemia.",
      "CRISPR-Cas9 acts as molecular scissors, cutting specific DNA sequences to reactivate production of fetal hemoglobin (HbF).",
      "India launched the National Sickle Cell Anemia Elimination Mission 2047, focusing on screening 7 crore tribal citizens across 17 high-prevalence states."],
     "GS-3: Biotechnology, Gene Editing, CRISPR-Cas9, Sickle Cell Mission, Public Health in Tribal Areas.",
     [
         ("The CRISPR-Cas9 system was originally discovered as an adaptive immune defense mechanism in:\n(a) Human white blood cells\n(b) Bacteria and archaea against invading viral bacteriophages\n(c) Flowering angiosperms\n(d) Marine cnidarians",
          ["(a) Human white blood cells", "(b) Bacteria and archaea against invading viral bacteriophages", "(c) Flowering angiosperms", "(d) Marine cnidarians"],
          "(b)", "CRISPR (Clustered Regularly Interspaced Short Palindromic Repeats) is a natural bacterial immune system that memorizes and snips viral DNA using Cas endonuclease enzymes."),
         ("In the CRISPR-Cas9 complex, what is the specific role of the 'Guide RNA' (gRNA)?\n(a) To supply electrical energy to the enzyme\n(b) To recognize and guide the Cas9 cutting enzyme to the exact complementary target DNA sequence\n(c) To synthesize blood platelets\n(d) To coat the cell membrane against radiation",
          ["(a) To supply electrical energy to the enzyme", "(b) To recognize and guide the Cas9 cutting enzyme to the exact complementary target DNA sequence", "(c) To synthesize blood platelets", "(d) To coat the cell membrane against radiation"],
          "(b)", "The guide RNA is a synthetic RNA sequence matching the target gene, ensuring that Cas9 cleaves exclusively at the targeted genomic site."),
         ("Sickle Cell Anemia is caused by a single point mutation in the beta-globin gene on chromosome 11, where glutamic acid is substituted by:\n(a) Lysine\n(b) Valine\n(c) Alanine\n(d) Tryptophan",
          ["(a) Lysine", "(b) Valine", "(c) Alanine", "(d) Tryptophan"],
          "(b)", "A single nucleotide substitution (GAG -> GTG) replaces hydrophilic glutamic acid with hydrophobic valine at position 6, causing hemoglobin molecules to polymerize into sickle shapes under low oxygen."),
         ("What target year has the Government of India set under the National Sickle Cell Anemia Elimination Mission?\n(a) 2030\n(b) 2035\n(c) 2047\n(d) 2050",
          ["(a) 2030", "(b) 2035", "(c) 2047", "(d) 2050"],
          "(c)", "The Mission launched by the Prime Minister in 2023 aims to eliminate sickle cell disease as a public health problem by 2047 through pre-marital counseling and screening."),
         ("Which scientists were awarded the Nobel Prize in Chemistry in 2020 for the development of the CRISPR-Cas9 method for genome editing?\n(a) Jennifer Doudna and Emmanuelle Charpentier\n(b) James Watson and Francis Crick\n(c) Katalin Kariko and Drew Weissman\n(d) Svante Paabo and Shinya Yamanaka",
          ["(a) Jennifer Doudna and Emmanuelle Charpentier", "(b) James Watson and Francis Crick", "(c) Katalin Kariko and Drew Weissman", "(d) Svante Paabo and Shinya Yamanaka"],
          "(a)", "Emmanuelle Charpentier and Jennifer A. Doudna were jointly awarded the 2020 Chemistry Nobel Prize for discovering and reprogramming the CRISPR-Cas9 genetic scissors.")
     ]),

    ("ca-sci-10", "2026-03-08", "SciTech", "Indigenous CAR-T Cell Therapy (NexCAR19): Cancer Immunotherapy Breakthrough", "CDSCO / PIB", True, True,
     ["Central Drugs Standard Control Organisation (CDSCO) approved NexCAR19 (Actalycabtagene autoleucel), India's first indigenously developed CAR-T cell therapy.",
      "Jointly developed by IIT Bombay, Tata Memorial Centre, and ImmunoACT, reducing treatment costs from ~$400,000 abroad to ~$40,000 in India.",
      "Engineers a patient's own T-cells with a Chimeric Antigen Receptor (CAR) targeting the CD19 protein found on malignant B-cell leukemia and lymphoma."],
     "GS-3: Biotechnology, Cancer Immunotherapy, CAR-T Technology, Affordable Healthcare, CDSCO Approvals.",
     [
         ("What does 'CAR-T' cell therapy stand for in modern oncological medicine?\n(a) Chemotherapy Assisted Radiation Therapy\n(b) Chimeric Antigen Receptor T-cell therapy\n(c) Cellular Autoimmune Regulated Transfer\n(d) Cytotoxic Antibody Release Treatment",
          ["(a) Chemotherapy Assisted Radiation Therapy", "(b) Chimeric Antigen Receptor T-cell therapy", "(c) Cellular Autoimmune Regulated Transfer", "(d) Cytotoxic Antibody Release Treatment"],
          "(b)", "CAR-T stands for Chimeric Antigen Receptor T-cell therapy, a type of autologous cellular immunotherapy."),
         ("How does CAR-T therapy work inside a patient's body?\n(a) It poisons cancerous cells using heavy radiation seeds\n(b) It extracts the patient's own T-lymphocytes, genetically reprograms them to express synthetic receptors targeting cancer proteins, and re-infuses them\n(c) It replaces all blood with donor blood\n(d) It acts as a preventative bacterial vaccine",
          ["(a) It poisons cancerous cells using heavy radiation seeds", "(b) It extracts the patient's own T-lymphocytes, genetically reprograms them to express synthetic receptors targeting cancer proteins, and re-infuses them", "(c) It replaces all blood with donor blood", "(d) It acts as a preventative bacterial vaccine"],
          "(b)", "T-cells (the body's immune soldiers) are drawn from patient blood, genetically modified via viral vectors to express CAR receptors recognizing cancer antigens (like CD19), multiplied, and infused back."),
         ("India's first commercially approved CAR-T therapy developed by IIT Bombay and Tata Memorial Centre is marketed under the name:\n(a) NexCAR19\n(b) Kymriah\n(c) Yescarta\n(d) Covaxin",
          ["(a) NexCAR19", "(b) Kymriah", "(c) Yescarta", "(d) Covaxin"],
          "(a)", "NexCAR19 is India's first indigenous CAR-T cell therapy, designed specifically with a humanized antibody construct to minimize inflammatory cytokine release syndrome."),
         ("T-cells and B-cells are specialized sub-types of which white blood cell classification?\n(a) Monocytes\n(b) Neutrophils\n(c) Lymphocytes\n(d) Eosinophils",
          ["(a) Monocytes", "(b) Neutrophils", "(c) Lymphocytes\n", "(d) Eosinophils"],
          "(c)", "T-cells (maturing in the Thymus) and B-cells (maturing in Bone marrow) are the two primary cellular components of the adaptive immune system (lymphocytes)."),
         ("Which statutory authority headed by the Drugs Controller General of India (DCGI) is responsible for approving new drugs and clinical trials in India?\n(a) Central Drugs Standard Control Organisation (CDSCO)\n(b) Indian Council of Medical Research (ICMR)\n(c) National Health Authority (NHA)\n(d) Pharmacopoeia Commission",
          ["(a) Central Drugs Standard Control Organisation (CDSCO)", "(b) Indian Council of Medical Research (ICMR)", "(c) National Health Authority (NHA)", "(d) Pharmacopoeia Commission"],
          "(a)", "The CDSCO under the Ministry of Health and Family Welfare is the national regulatory authority for drugs, medical devices, and clinical trials under the Drugs and Cosmetics Act 1940.")
     ]),

    ("ca-sci-11", "2026-02-05", "SciTech", "Square Kilometre Array (SKA) Observatory: India's Full Member Ratification", "DST / The Hindu", False, True,
     ["Government of India formally ratified membership in the Square Kilometre Array Observatory (SKAO), joining the world's largest radio telescope consortium.",
      "Comprises thousands of radio antennas co-located in remote desert locations: SKA-Low in Western Australia and SKA-Mid in South Africa's Karoo region.",
      "India's primary scientific and engineering contribution centers on designing and building the Telescope Manager software architecture led by NCRA-TIFR Pune."],
     "GS-3: Astronomy, Radio Telescopes, International Scientific Megaprojects, SKAO, Giant Metrewave Radio Telescope.",
     [
         ("The Square Kilometre Array (SKA) is designed to be the world's largest facility for which branch of astronomy?\n(a) Optical astronomy\n(b) Radio astronomy\n(c) X-ray astronomy\n(d) Gravitational wave interferometry",
          ["(a) Optical astronomy", "(b) Radio astronomy", "(c) X-ray astronomy", "(d) Gravitational wave interferometry"],
          "(b)", "SKA will be the world's largest radio telescope, operating across radio frequencies from 50 MHz to 15 GHz to probe the early Universe and Cosmic Dawn."),
         ("In which two countries are the physical antenna arrays of the Square Kilometre Array located?\n(a) India and Chile\n(b) Australia and South Africa\n(c) United States and Canada\n(d) China and Argentina",
          ["(a) India and Chile", "(b) Australia and South Africa", "(c) United States and Canada", "(d) China and Argentina"],
          "(b)", "SKA-Low (low frequency dipoles) is located at Murchison in Western Australia; SKA-Mid (dish antennas) is located in the Karoo desert of South Africa."),
         ("Which premier Indian astrophysics research institute headquartered in Pune leads India's institutional participation in the SKA project?\n(a) Indian Institute of Astrophysics (IIA)\n(b) National Centre for Radio Astrophysics (NCRA-TIFR)\n(c) Inter-University Centre for Astronomy and Astrophysics (IUCAA)\n(d) Physical Research Laboratory (PRL)",
          ["(a) Indian Institute of Astrophysics (IIA)", "(b) National Centre for Radio Astrophysics (NCRA-TIFR)", "(c) Inter-University Centre for Astronomy and Astrophysics (IUCAA)", "(d) Physical Research Laboratory (PRL)"],
          "(b)", "NCRA-TIFR, which operates the world-renowned Giant Metrewave Radio Telescope (GMRT) at Khodad near Pune, coordinates India's software and technical role in SKA."),
         ("Radio waves differ from visible light waves in the electromagnetic spectrum primarily because they have:\n(a) Shorter wavelengths and higher frequencies\n(b) Longer wavelengths and lower frequencies\n(c) Zero velocity in vacuum\n(d) Only particulate mass",
          ["(a) Shorter wavelengths and higher frequencies", "(b) Longer wavelengths and lower frequencies", "(c) Zero velocity in vacuum", "(d) Only particulate mass"],
          "(b)", "Radio waves sit at the lowest frequency, longest wavelength end of the electromagnetic spectrum, allowing them to penetrate cosmic dust clouds unhindered."),
         ("Where is the international global headquarters of the Square Kilometre Array Observatory (SKAO) located?\n(a) Jodrell Bank, United Kingdom\n(b) Geneva, Switzerland\n(c) Paris, France\n(d) Washington D.C., USA",
          ["(a) Jodrell Bank, United Kingdom", "(b) Geneva, Switzerland", "(c) Paris, France", "(d) Washington D.C., USA"],
          "(a)", "SKAO is an intergovernmental organization established by treaty, with its central headquarters located at Jodrell Bank Observatory near Manchester, UK.")
     ]),

    ("ca-sci-12", "2026-01-12", "SciTech", "Indian Space Policy 2023: IN-SPACe & Private Non-Government Entities (NGEs)", "ISRO / PIB", True, True,
     ["Indian Space Policy 2023 created an institutional separation of roles: ISRO (R&D and advanced exploration), IN-SPACe (authorization and promotion of private space sector), and NSIL (commercialization).",
      "Indian National Space Promotion and Authorization Centre (IN-SPACe) serves as a single-window autonomous agency under Department of Space for private entities.",
      "NewSpace India Limited (NSIL) acts as the commercial arm, responsible for owning and operating commercial operational launch vehicles and satellites."],
     "GS-3: Space Technology, Privatization of Space, IN-SPACe, NSIL, Commercial Space Missions.",
     [
         ("Under the Indian Space Policy 2023, which entity is the single-window regulatory agency for authorizing and promoting private space activities?\n(a) ISRO\n(b) IN-SPACe (Indian National Space Promotion and Authorization Centre)\n(c) Antrix Corporation\n(d) Telecom Regulatory Authority of India",
          ["(a) ISRO", "(b) IN-SPACe (Indian National Space Promotion and Authorization Centre)", "(c) Antrix Corporation", "(d) Telecom Regulatory Authority of India"],
          "(b)", "IN-SPACe is an autonomous single-window nodal agency under the Department of Space that authorizes, promotes, and handholds Non-Government Entities (NGEs)."),
         ("What is the primary statutory mandate of NewSpace India Limited (NSIL)?\n(a) Pure scientific research into black holes\n(b) Commercializing space technologies, building rockets via industry consortia, and operating commercial satellite assets\n(c) Regulating private drone flights\n(d) Managing the Indian Air Force radar network",
          ["(a) Pure scientific research into black holes", "(b) Commercializing space technologies, building rockets via industry consortia, and operating commercial satellite assets", "(c) Regulating private drone flights", "(d) Managing the Indian Air Force radar network"],
          "(b)", "NSIL is a wholly-owned Government of India CPSE under Department of Space tasked with commercial exploitation of space R&D, manufacturing LVM3/PSLV via industry, and satellite transponder leasing."),
         ("India's first privately developed sub-orbital rocket, launched by Skyroot Aerospace from Sriharikota in 2022, was named:\n(a) Vikram-S\n(b) Agnibaan\n(c) Rohini-200\n(d) Dhruva-1",
          ["(a) Vikram-S", "(b) Agnibaan", "(c) Rohini-200", "(d) Dhruva-1"],
          "(a)", "Vikram-S (named after Dr. Vikram Sarabhai) was India's first privately built rocket launched under Mission Prarambh by Skyroot Aerospace."),
         ("Which startup successfully test-fired Agnibaan SOrTeD, featuring the world's first single-piece 3D-printed semi-cryogenic engine (Agnilet)?\n(a) Pixxel\n(b) Agnikul Cosmos\n(c) Bellatrix Aerospace\n(d) Dhruva Space",
          ["(a) Pixxel", "(b) Agnikul Cosmos", "(c) Bellatrix Aerospace", "(d) Dhruva Space"],
          "(b)", "Agnikul Cosmos launched Agnibaan Sub-Orbital Technology Demonstrator from India's first private launchpad (Dhanush) at Sriharikota, using a 3D-printed engine running on liquid oxygen and aviation kerosene."),
         ("Under the 1967 UN Outer Space Treaty, who bears international responsibility for national activities in outer space carried out by non-governmental entities?\n(a) The private corporation exclusively\n(b) The appropriate State Party to the Treaty (the sovereign country)\n(c) The United Nations Security Council\n(d) The International Telecommunication Union",
          ["(a) The private corporation exclusively", "(b) The appropriate State Party to the Treaty (the sovereign country)", "(c) The United Nations Security Council", "(d) The International Telecommunication Union"],
          "(b)", "Article VI of the Outer Space Treaty makes sovereign states internationally liable for activities of their private commercial entities in space, necessitating domestic licensing regimes like IN-SPACe.")
     ]),

    ("ca-sci-13", "2026-10-01", "SciTech", "Small Modular Reactors (SMRs) & Nuclear Energy Renaissance", "DAE / Livemint", True, True,
     ["Small Modular Reactors (SMRs) are nuclear fission reactors with power capacity up to 300 MWe per unit (about one-third of traditional reactors).",
      "Designed with modular prefabricated systems that can be factory-manufactured, shipped by truck or rail, and assembled on site.",
      "Government is exploring private sector participation and leasing Bharat Small Reactors (BSRs) based on 220 MWe Pressurised Heavy Water Reactor (PHWR) designs to power captive industrial units."],
     "GS-3: Nuclear Power, SMRs, Decarbonization, Clean Energy, Industrial Captive Power.",
     [
         ("By standard International Atomic Energy Agency (IAEA) classification, Small Modular Reactors (SMRs) have a power generation capacity of up to:\n(a) 50 MWe\n(b) 300 MWe\n(c) 1,000 MWe\n(d) 5,000 MWe",
          ["(a) 50 MWe", "(b) 300 MWe", "(c) 1,000 MWe", "(d) 5,000 MWe"],
          "(b)", "The IAEA defines Small Modular Reactors (SMRs) as advanced nuclear reactors producing up to 300 MWe per module, combining modular factory construction with passive safety features."),
         ("What is the major safety advantage of SMRs over large-scale gigawatt-class nuclear reactors?\n(a) Zero radioactive waste generation\n(b) Passive safety systems relying on gravity, natural circulation, and convection that do not require external power or human action to shut down safely\n(c) Use of common table salt as core fuel\n(d) They cannot be damaged by seismic earthquakes",
          ["(a) Zero radioactive waste generation", "(b) Passive safety systems relying on gravity, natural circulation, and convection that do not require external power or human action to shut down safely", "(c) Use of common table salt as core fuel", "(d) They cannot be damaged by seismic earthquakes"],
          "(b)", "Passive safety mechanisms operate on fundamental physical principles (gravity feed, natural convection) without needing active electrical pumps or operator intervention during accidents."),
         ("Under the Atomic Energy Act 1962, can private corporations in India currently build and operate nuclear power plants independently?\n(a) Yes, 100% private ownership is permitted\n(b) No, nuclear power generation remains restricted to Central Government entities or joint ventures with at least 51% government majority equity\n(c) Private sector is allowed only in solar energy\n(d) State Governments possess sole authority",
          ["(a) Yes, 100% private ownership is permitted", "(b) No, nuclear power generation remains restricted to Central Government entities or joint ventures with at least 51% government majority equity", "(c) Private sector is allowed only in solar energy", "(d) State Governments possess sole authority"],
          "(b)", "Section 3 of the Atomic Energy Act reserves nuclear power to the Central Government (via NPCIL/BHAVINI). Joint ventures require majority central equity, though amendments are under consideration for captive SMRs."),
         ("What is the nuclear fuel type utilized in India's indigenous fleet of 220 MWe and 700 MWe Pressurised Heavy Water Reactors (PHWRs)?\n(a) Enriched Uranium-235 (20% enrichment)\n(b) Natural Uranium dioxide (UO2) without enrichment\n(c) Pure Plutonium-239 metal\n(d) Thorium-232 oxide only",
          ["(a) Enriched Uranium-235 (20% enrichment)", "(b) Natural Uranium dioxide (UO2) without enrichment", "(c) Pure Plutonium-239 metal\n", "(d) Thorium-232 oxide only"],
          "(b)", "India's PHWRs use natural uranium (0.7% U-235) because Heavy Water (D2O) has low neutron absorption, eliminating the need for costly uranium enrichment."),
         ("In nuclear non-proliferation agreements, the Civil Liability for Nuclear Damage Act (CLNDA) 2010 in India contains a contentious clause in:\n(a) Section 17(b) providing right of recourse against equipment suppliers in case of defective components\n(b) Section 5 prohibiting foreign inspections\n(c) Section 10 transferring liability to consumers\n(d) Section 25 exempting all plant operators",
          ["(a) Section 17(b) providing right of recourse against equipment suppliers in case of defective components", "(b) Section 5 prohibiting foreign inspections", "(c) Section 10 transferring liability to consumers", "(d) Section 25 exempting all plant operators"],
          "(a)", "Section 17(b) allows plant operators to seek damages from foreign equipment vendors if accidents result from defective equipment, contrasting with international conventions where liability is channeled exclusively to the operator.")
     ]),

    ("ca-sci-14", "2026-09-02", "SciTech", "Dark Sky Reserve at Hanle, Ladakh & Astrotourism Development", "IIA / DST", False, True,
     ["India's first Dark Sky Reserve established at Hanle in Eastern Ladakh as the Department of Science and Technology's Indian Astronomical Observatory (IAO).",
      "Hanle was chosen for high altitude (4,500 m), dry arid atmosphere, clear sub-zero nights, and near-zero artificial light pollution.",
      "Hosts the 2-meter optical-infrared Himalayan Chandra Telescope (HCT) and the Major Atmospheric Cerenkov Experiment (MACE) gamma-ray telescope."],
     "GS-3: Astronomy, Light Pollution, Indian Astronomical Observatory, MACE Telescope, Ladakh Development.",
     [
         ("India's first designated Dark Sky Reserve has been notified in which location?\n(a) Spiti Valley, Himachal Pradesh\n(b) Hanle, Eastern Ladakh\n(c) Mount Abu, Rajasthan\n(d) Kodaikanal, Tamil Nadu",
          ["(a) Spiti Valley, Himachal Pradesh\n", "(b) Hanle, Eastern Ladakh", "(c) Mount Abu, Rajasthan", "(d) Kodaikanal, Tamil Nadu"],
          "(b)", "The Hanle Dark Sky Reserve was created around the Indian Astronomical Observatory in Changthang Wildlife Sanctuary, Eastern Ladakh."),
         ("Why is Hanle in Ladakh an ideal geographic location for optical, infrared, and gamma-ray astronomy?\n(a) High atmospheric humidity\n(b) High altitude (4,500m), low precipitation, cloudless skies, minimal atmospheric attenuation, and absence of light pollution\n(c) Proximity to the equator\n(d) Presence of deep underground volcanic caves",
          ["(a) High atmospheric humidity", "(b) High altitude (4,500m), low precipitation, cloudless skies, minimal atmospheric attenuation, and absence of light pollution", "(c) Proximity to the equator", "(d) Presence of deep underground volcanic caves"],
          "(b)", "High altitude cold desert conditions provide a dry, thin atmosphere that absorbs minimal starlight and infrared radiation, offering pristine seeing conditions."),
         ("The MACE (Major Atmospheric Cerenkov Experiment) telescope located at Hanle is designed to detect:\n(a) Subterranean seismic vibrations\n(b) Very high-energy cosmic Gamma rays via atmospheric Cherenkov flashes\n(c) Low-frequency FM radio broadcasts\n(d) Solar neutrino emissions exclusively",
          ["(a) Subterranean seismic vibrations", "(b) Very high-energy cosmic Gamma rays via atmospheric Cherenkov flashes", "(c) Low-frequency FM radio broadcasts", "(d) Solar neutrino emissions exclusively"],
          "(b)", "MACE is the world's second-largest gamma-ray telescope, built by BARC to observe Cherenkov radiation generated when cosmic gamma rays collide with the upper atmosphere."),
         ("What is the primary objective of creating a 'Dark Sky Reserve'?\n(a) To enforce complete daytime blackouts\n(b) To protect the nocturnal environment and night sky from artificial light pollution through regulated lighting ordinances\n(c) To conduct military camouflage exercises\n(d) To study subterranean troglobites",
          ["(a) To enforce complete daytime blackouts", "(b) To protect the nocturnal environment and night sky from artificial light pollution through regulated lighting ordinances", "(c) To conduct military camouflage exercises", "(d) To study subterranean troglobites"],
          "(b)", "Dark sky reserves designate buffer zones where public outdoor lighting is shielded and controlled to minimize skyglow and preserve astronomical observation."),
         ("Which premier research institute operates the Himalayan Chandra Telescope (HCT) remotely via satellite link from Hosakote near Bengaluru?\n(a) Tata Institute of Fundamental Research\n(b) Indian Institute of Astrophysics (IIA)\n(c) Physical Research Laboratory\n(d) Raman Research Institute",
          ["(a) Tata Institute of Fundamental Research", "(b) Indian Institute of Astrophysics (IIA)", "(c) Physical Research Laboratory", "(d) Raman Research Institute"],
          "(b)", "The Indian Institute of Astrophysics (IIA) in Bengaluru controls the 2-meter optical telescope at Hanle remotely via dedicated INSAT satellite communication link.")
     ]),

    ("ca-sci-15", "2026-08-01", "SciTech", "Polymetallic Nodules & International Seabed Authority (ISA) Deep Sea Exploration", "MoES / PIB", True, True,
     ["India holds exploration contracts from the International Seabed Authority (ISA) for Polymetallic Nodules in the Central Indian Ocean Basin (CIOB) and Polymetallic Sulphides in Central/Southwest Indian Ridges.",
      "Polymetallic nodules (potato-sized rocks on abyssal plains at 4,000-6,000m) are rich in critical transition metals: Nickel, Cobalt, Copper, and Manganese.",
      "UNCLOS declared the international seabed area and its mineral resources as the 'Common Heritage of Mankind' managed by the Kingston-based ISA."],
     "GS-3: Deep Sea Minerals, Critical Raw Materials, UNCLOS, International Seabed Authority, Maritime Geopolitics.",
     [
         ("Polymetallic nodules resting on the abyssal plains of the ocean floor are predominantly composed of which metal by weight?\n(a) Gold\n(b) Manganese (along with Iron oxides)\n(c) Uranium\n(d) Platinum",
          ["(a) Gold", "(b) Manganese (along with Iron oxides)", "(c) Uranium", "(d) Platinum"],
          "(b)", "Also known as manganese nodules, they typically consist of ~28% Manganese, ~6% Iron, ~1.3% Nickel, ~1.1% Copper, and ~0.25% Cobalt."),
         ("Which international organization established under UNCLOS regulates all mineral-related activities in the international seabed area beyond national jurisdiction?\n(a) International Maritime Organization (IMO)\n(b) International Seabed Authority (ISA)\n(c) United Nations Environment Programme (UNEP)\n(d) International Whaling Commission",
          ["(a) International Maritime Organization (IMO)", "(b) International Seabed Authority (ISA)", "(c) United Nations Environment Programme (UNEP)", "(d) International Whaling Commission"],
          "(b)", "The International Seabed Authority (headquartered in Kingston, Jamaica) was established under UNCLOS 1982 to organize and control exploration and exploitation of seabed minerals."),
         ("Where is India's allocated 75,000 sq km exploration site for polymetallic nodules located?\n(a) Bay of Bengal continental shelf\n(b) Central Indian Ocean Basin (CIOB)\n(c) Arabian Sea Lakshadweep Ridge\n(d) Andaman Sea Submarine Trench",
          ["(a) Bay of Bengal continental shelf", "(b) Central Indian Ocean Basin (CIOB)", "(c) Arabian Sea Lakshadweep Ridge", "(d) Andaman Sea Submarine Trench"],
          "(b)", "India was the first 'Pioneer Investor' registered in 1987, receiving an exploration site in the Central Indian Ocean Basin located ~2,000 km south of Kanyakumari at 4,000-6,000 m depths."),
         ("What is the primary ecological concern associated with commercial deep-sea mining using seafloor crawlers?\n(a) Overfishing of coastal sardines\n(b) Destruction of fragile benthic ecosystems, destruction of biogenic nodule habitats, and sediment plumes suffocating mid-water organisms\n(c) Heating up of surface tropical water\n(d) Triggering tsunamis",
          ["(a) Overfishing of coastal sardines", "(b) Destruction of fragile benthic ecosystems, destruction of biogenic nodule habitats, and sediment plumes suffocating mid-water organisms", "(c) Heating up of surface tropical water", "(d) Triggering tsunamis"],
          "(b)", "Deep-sea benthic fauna rely on hard nodule substrates formed over millions of years. Crawler machinery destroys these ecosystems and generates underwater sediment plumes."),
         ("Under Part XI of UNCLOS, mineral resources in the international seabed Area are legally designated as:\n(a) Res Nullius (property of whoever claims it first)\n(b) The Common Heritage of Mankind\n(c) Exclusive property of the G7 nations\n(d) Sovereign property of coastal states",
          ["(a) Res Nullius (property of whoever claims it first)", "(b) The Common Heritage of Mankind", "(c) Exclusive property of the G7 nations", "(d) Sovereign property of coastal states"],
          "(b)", "Article 136 of UNCLOS states: 'The Area and its resources are the common heritage of mankind', requiring equitable sharing of financial and economic benefits.")
     ])
]

all_sci = sci1_2 + [make_art(aid, dt, pil, tit, src, top, pt, sums, gs, qs) for aid, dt, pil, tit, src, top, pt, sums, gs, qs in sci_new]
print(f"Total SciTech articles: {len(all_sci)}")
assert len(all_sci) == 15, f"Expected 15, got {len(all_sci)}"

with open(os.path.join(BASE_DIR, 'data', 'ca_builders', 'scitech.json'), 'w') as f:
    json.dump(all_sci, f, indent=2)

print("Saved scitech.json successfully!")
