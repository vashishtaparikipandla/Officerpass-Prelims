import json
import os

with open('data/curriculum-180.json', 'r') as f:
    curriculum = json.load(f)

with open('micro-topics/microtopics-db.json', 'r') as f:
    db = json.load(f)

csat_catalog = db.get('CSAT_MicroTopics', [])
print(f"Loaded {len(csat_catalog)} CSAT microtopics from catalog.")

# Helper to find or assign CSAT microtopic for each day
def get_csat_for_day(day_num):
    # Mapping logic across 180 days
    if 1 <= day_num <= 3:
        cat_item = csat_catalog[0] # Unit digit
    elif 4 <= day_num <= 6:
        cat_item = csat_catalog[1] # Remainder theorem
    elif day_num == 7:
        cat_item = csat_catalog[0] # Mock Day 1 Consolidation
    elif 8 <= day_num <= 10:
        cat_item = csat_catalog[2] # Divisibility rules
    elif 11 <= day_num <= 13:
        cat_item = csat_catalog[3] # Factors & multiples
    elif day_num == 14:
        cat_item = csat_catalog[4] # Trailing zeroes
    elif 15 <= day_num <= 18:
        cat_item = csat_catalog[5] # Percentages ₹100
    elif 19 <= day_num <= 21:
        cat_item = csat_catalog[6] # Successive percentage
    elif 22 <= day_num <= 25:
        cat_item = csat_catalog[7] # Profit and Loss
    elif 26 <= day_num <= 28:
        cat_item = csat_catalog[8] # Averages seesaw
    elif 29 <= day_num <= 32:
        cat_item = csat_catalog[9] # Ratio, Mixture & Alligation
    elif 33 <= day_num <= 35:
        cat_item = csat_catalog[10] # Time & Work LCM
    elif 36 <= day_num <= 38:
        cat_item = csat_catalog[11] # Pipes & Cisterns
    elif 39 <= day_num <= 42:
        cat_item = csat_catalog[12] # Speed, Time & Distance
    elif 43 <= day_num <= 46:
        cat_item = csat_catalog[13] # Trains relative speed
    elif 47 <= day_num <= 49:
        cat_item = csat_catalog[14] # Boats & Streams
    elif 50 <= day_num <= 54:
        cat_item = csat_catalog[15] # Permutations & Combinations
    elif 55 <= day_num <= 58:
        cat_item = csat_catalog[16] # Probability
    elif 59 <= day_num <= 62:
        cat_item = csat_catalog[17] # Clocks
    elif 63 <= day_num <= 66:
        cat_item = csat_catalog[18] # Calendar
    elif 67 <= day_num <= 70:
        cat_item = csat_catalog[19] # Cubes & Dice
    elif 71 <= day_num <= 75:
        cat_item = csat_catalog[20] # Blood Relations
    elif 76 <= day_num <= 80:
        cat_item = csat_catalog[21] # Direction Sense
    elif 81 <= day_num <= 87:
        cat_item = csat_catalog[22] # Syllogisms
    elif 88 <= day_num <= 95:
        cat_item = csat_catalog[23] # Seating & Puzzles
    elif 96 <= day_num <= 105:
        cat_item = csat_catalog[24] # Reading Comprehension Sherlocking
    elif 106 <= day_num <= 125:
        # Phase 2: RC Intensive Sherlocking across domains
        cat_item = csat_catalog[24]
    elif 126 <= day_num <= 140:
        # Phase 2: High-Yield Quant & Reasoning Speed Review
        idx = (day_num - 126) % (len(csat_catalog) - 1)
        cat_item = csat_catalog[idx]
    else: # Phase 3: Days 141 to 180 (Full Mock Simulations)
        idx = (day_num - 141) % len(csat_catalog)
        cat_item = csat_catalog[idx]

    sub_items = [
        {"id": f"csat__d{day_num}_s{i}", "text": item["text"]}
        for i, item in enumerate(cat_item["sub_items"])
    ]

    return {
        "id": f"csat-d{day_num}",
        "topic_id": cat_item["id"],
        "title": cat_item["topic"],
        "ungist_ref": cat_item["core_sources"],
        "prob": cat_item["prob"],
        "keywords": cat_item.get("keywords", ""),
        "sub_items": sub_items
    }

for day_obj in curriculum:
    day_num = day_obj["day"]
    csat_data = get_csat_for_day(day_num)
    day_obj["csat_micro_topic"] = csat_data
    if "session_evening" in day_obj:
        day_obj["session_evening"]["csat_topic"] = csat_data["title"]
        day_obj["session_evening"]["csat_ungist_ref"] = csat_data["ungist_ref"]
        day_obj["session_evening"]["csat_prob"] = csat_data["prob"]

with open('data/curriculum-180.json', 'w') as f:
    json.dump(curriculum, f, indent=2)

print("Successfully updated all 180 days in data/curriculum-180.json with day-specific CSAT micro-topics!")
