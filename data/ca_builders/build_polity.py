#!/usr/bin/env python3
import json

with open('/Users/vashishtaparikipandla/Documents/OfficerPass/data/current-affairs-db.json') as f:
    d = json.load(f)

pol1_3 = [a for a in d if a['pillar'] == 'Polity']

# Import from create_full_ca_database
import create_full_ca_database as m1
batch1 = m1.polity_batch

# Define ca-pol-12 cleanly
p12 = {
    "id": "ca-pol-12",
    "date": "2026-04-12",
    "pillar": "Polity",
    "title": "Delimitation of Parliamentary Constituencies: Constitutional Bar until Post-2026",
    "source": "The Hindu / PIB",
    "is_top100": True,
    "is_pt365": True,
    "summary_points": [
        "Article 82 and Article 170(3) provide for readjustment of Lok Sabha and Assembly seats after each census.",
        "The 84th Constitutional Amendment Act 2001 froze the total number of Lok Sabha seats based on the 1971 Census until the first census taken after the year 2026.",
        "The 87th Amendment 2003 permitted intra-state rationalization of constituency boundaries based on 2001 Census data without changing total state seats."
    ],
    "gs_connection": "GS-2: Representation of People, Federalism, North-South Demography Divergence, 84th Amendment.",
    "mcqs": [
        {
            "id": "ca-pol-12-q1",
            "q": "Which constitutional amendment froze the allocation of seats in the Lok Sabha based on the 1971 Census until after 2026?\n(a) 42nd Amendment Act 1976\n(b) 84th Amendment Act 2001\n(c) 87th Amendment Act 2003\n(d) 91st Amendment Act 2003",
            "options": ["(a) 42nd Amendment Act 1976", "(b) 84th Amendment Act 2001", "(c) 87th Amendment Act 2003", "(d) 91st Amendment Act 2003"],
            "answer": "(b)",
            "explanation": "The 84th Amendment Act 2001 extended the 42nd Amendment freeze for another 25 years (until the first census taken after 2026)."
        },
        {
            "id": "ca-pol-12-q2",
            "q": "Under Article 82, who is empowered to establish a Delimitation Commission for boundary readjustment?\n(a) Supreme Court\n(b) Parliament by law\n(c) Election Commission of India independently\n(d) President in his sole discretion",
            "options": ["(a) Supreme Court", "(b) Parliament by law", "(c) Election Commission of India independently", "(d) President in his sole discretion"],
            "answer": "(b)",
            "explanation": "Article 82 provides that Parliament may by law determine the authority and manner of delimitation."
        },
        {
            "id": "ca-pol-12-q3",
            "q": "Can orders of the Delimitation Commission be challenged before a court of law?\n(a) Yes, in any High Court under Article 226\n(b) Yes, directly in the Supreme Court under Article 32\n(c) No, Article 329(a) bars the questioning of delimitation laws and orders in any court\n(d) Only with prior sanction of the President",
            "options": ["(a) Yes, in any High Court under Article 226", "(b) Yes, directly in the Supreme Court under Article 32", "(c) No, Article 329(a) bars the questioning of delimitation laws and orders in any court", "(d) Only with prior sanction of the President"],
            "answer": "(c)",
            "explanation": "Article 329(a) bars court interference in electoral matters regarding delimitation and allotment of seats."
        },
        {
            "id": "ca-pol-12-q4",
            "q": "The Delimitation Commission in India is headed by:\n(a) Chief Election Commissioner\n(b) A retired Supreme Court Judge\n(c) Union Law Minister\n(d) Cabinet Secretary",
            "options": ["(a) Chief Election Commissioner", "(b) A retired Supreme Court Judge", "(c) Union Law Minister", "(d) Cabinet Secretary"],
            "answer": "(b)",
            "explanation": "The Delimitation Commission is headed by a retired Supreme Court judge, alongside the CEC and respective State Election Commissioners."
        },
        {
            "id": "ca-pol-12-q5",
            "q": "Which amendment allowed redrawing of internal constituency boundaries within states using the 2001 census without changing state total seats?\n(a) 84th Amendment\n(b) 87th Amendment\n(c) 89th Amendment\n(d) 92nd Amendment",
            "options": ["(a) 84th Amendment", "(b) 87th Amendment", "(c) 89th Amendment", "(d) 92nd Amendment"],
            "answer": "(b)",
            "explanation": "The 87th Amendment Act 2003 substituted 2001 census for 1991 census for intra-state constituency rationalization."
        }
    ]
}

all_pol = pol1_3 + batch1 + [p12]
all_pol.sort(key=lambda x: int(x['id'].split('-')[-1]))

print(f"Total Polity articles: {len(all_pol)}")
assert len(all_pol) == 18, f"Expected 18, got {len(all_pol)}"

with open('/Users/vashishtaparikipandla/Documents/OfficerPass/data/ca_builders/polity.json', 'w') as f:
    json.dump(all_pol, f, indent=2)

print("Saved polity.json successfully!")
