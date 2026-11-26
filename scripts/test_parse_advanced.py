#!/usr/bin/env python3
import json
import re
import os

SOURCE_FILE = "/Users/vashishtaparikipandla/.gemini/antigravity/brain/3ec99952-3403-46c4-aae5-1b72abc5478b/.user_uploaded/media_1795577702518_82ea755a.md"
TARGET_JSON = "/Users/vashishtaparikipandla/Documents/OfficerPass/data/upsc-traps-vault.json"

SECTION_MAP = {
    "A1. Practice, precedent or general procedure": (9, "A1. Practice, Precedent & General Procedure"),
    "A2. Where a familiar expression hides a different legal source": (10, "A2. Familiar Expressions with Different Legal Sources"),
    "B1. President, Vice-President, Governor and councils of ministers": (11, "B1. President, VP, Governor & Councils of Ministers"),
    "B2. Presiding officers, MPs and MLAs": (12, "B2. Presiding Officers, MPs & MLAs"),
    "B3. Attorney-General, Advocate-General, CAG and audit": (13, "B3. Attorney-General, Advocate-General, CAG & Audit"),
    "B4. Supreme Court, High Courts and subordinate judiciary": (14, "B4. Supreme Court, High Courts & Subordinate Judiciary"),
    "B5. Election commissions, public service commissions and elections": (15, "B5. Election & Public Service Commissions"),
    "B6. Finance Commission, GST Council and federal institutions": (16, "B6. Finance Commission, GST Council & Federal Institutions"),
    "B7. SC, ST, SEBC, languages and minority institutions": (17, "B7. SC, ST, SEBC, Languages & Minority Institutions"),
    "B8. Local government offices and committees": (18, "B8. Local Government Offices & Committees"),
    "B9. Statutory and executive bodies that commonly appear beside constitutional ones": (19, "B9. Statutory & Executive Bodies Beside Constitutional Ones"),
    "C1. Criminal justice and public order": (20, "C1. Criminal Justice & Public Order (BNS, BNSS, BSA)"),
    "C2. Forces and command or ministry matching": (21, "C2. Armed Forces, CAPFs & Command/Ministry"),
    "C3. Investigating agencies, ministries and parent laws": (22, "C3. Investigating Agencies, Ministries & Parent Laws"),
    "C4. Rights, regulators and current-law crossovers": (23, "C4. Rights, Regulators & Current-Law Crossovers"),
    "What the past questions changed": (24, "D. UPSC Examiner Blueprint — What Past Questions Changed (2012–2026)")
}

def parse_advanced_traps():
    with open(SOURCE_FILE, "r", encoding="utf-8") as f:
        lines = f.readlines()

    current_section_num = None
    current_section_title = None
    in_table = False
    header_seen = False

    parsed_items = []
    sections_added = []
    seen_sec_nums = set()

    for line in lines:
        stripped = line.strip()

        # Check section header
        if stripped.startswith("### "):
            header_text = stripped[4:].strip()
            for key, (s_num, s_title) in SECTION_MAP.items():
                if key.lower() in header_text.lower():
                    current_section_num = s_num
                    current_section_title = s_title
                    if s_num not in seen_sec_nums:
                        seen_sec_nums.add(s_num)
                        sections_added.append({
                            "section_num": s_num,
                            "title": s_title
                        })
                    break
            in_table = False
            header_seen = False
            continue

        if current_section_num is None:
            continue

        # Parse table lines
        if stripped.startswith("|"):
            parts = [p.strip() for p in stripped.split("|")]
            # parts has empty string at index 0 and -1 if starts and ends with |
            if parts and parts[0] == "":
                parts = parts[1:]
            if parts and parts[-1] == "":
                parts = parts[:-1]

            if not parts or all(re.match(r"^:?-+:?$", p) for p in parts):
                # separator row
                continue

            # Check if this is the header row
            p_lower = [p.lower() for p in parts]
            if "item" in p_lower or "expression" in p_lower or "office and cue" in p_lower or "body and cue" in p_lower or "fact to recall" in p_lower or "institution" in p_lower or "agency or law" in p_lower or "subject" in p_lower or "past question" in p_lower:
                header_seen = True
                continue

            # Data row
            if len(parts) >= 2:
                prompt = parts[0]
                distinction = parts[1]
                if len(parts) >= 3:
                    raw_auth = parts[2]
                else:
                    raw_auth = "UPSC Examiner Trap Construction Pattern"

                # Clean authority
                auth = re.sub(r"\*\*([^*]+)\*\*", r"\1", raw_auth)

                # PYQ detection
                is_pyq = False
                pyq_years = []

                combined_text = f"{prompt} {distinction} {raw_auth}"
                if "PYQ" in combined_text or current_section_num == 24:
                    is_pyq = True

                # Find years
                found_years = re.findall(r"\b(20\d{2})\b", combined_text)
                if is_pyq and found_years:
                    for y in found_years:
                        if y not in pyq_years:
                            pyq_years.append(y)

                parsed_items.append({
                    "section_num": current_section_num,
                    "section_title": current_section_title,
                    "prompt": prompt,
                    "distinction": distinction,
                    "authority": auth,
                    "raw_authority": raw_auth,
                    "is_pyq": is_pyq,
                    "pyq_years": pyq_years
                })

    return sections_added, parsed_items

if __name__ == "__main__":
    sections, items = parse_advanced_traps()
    print(f"Parsed {len(sections)} sections, {len(items)} items.")
    for s in sections:
        sec_items = [i for i in items if i["section_num"] == s["section_num"]]
        pyqs = [i for i in sec_items if i["is_pyq"]]
        print(f"  Section {s['section_num']}: {s['title']} -> {len(sec_items)} items ({len(pyqs)} PYQs)")
