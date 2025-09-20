# create_unicode_mapping.py
# FIRST STEP: Create Unicode mapping for Sinhala characters
# Place this file in project-root/ and run it first

import json
import os
from pathlib import Path


def create_unicode_mapping():
    """Create Unicode mapping from class numbers to Sinhala characters"""

    # Your 454 Sinhala characters (in order from class 1 to 454)
    sinhala_classes = [
        "අ", "ආ", "ඇ", "ඈ", "ඉ", "ඊ", "උ", "එ", "ඒ", "ඔ", "ඕ",
        "ක", "කා", "කැ", "කෑ", "කි", "කී", "කු", "කූ", "ක්", "කෝ", "ක්‍ර", "ක්‍රි", "ක්‍රී",
        "ග", "ගා", "ගැ", "ගෑ", "ගි", "ගී", "ගු", "ගූ", "ග්", "ගෝ", "ග්‍ර", "ග්‍රි", "ග්‍රී",
        "ච", "චා", "චැ", "චෑ", "චි", "චී", "චු", "චූ", "ච්", "චෝ", "ච්‍ර", "ච්‍ර්", "ච්‍රී",
        "ජ", "ජා", "ජැ", "ජෑ", "ජි", "ජී", "ජු", "ජූ", "ජ්", "ජෝ", "ජ්‍ර", "ජ්‍රි", "ජ්‍රී",
        "ට", "ටා", "ටැ", "ටෑ", "ටි", "ටී", "ටු", "ටූ", "ට්", "ටෝ", "ට්‍ර", "ට්‍ර්", "ට්‍රි",
        "ඩ", "ඩා", "ඩැ", "ඩෑ", "ඩි", "ඩී", "ඩු", "ඩූ", "ඩ්", "ඩෝ", "ඩ්‍ර", "ඩ්‍ර්", "ඩ්‍රි",
        "ණ", "ණා", "ණි",
        "ත", "තා", "ති", "තී", "තු", "තූ", "ත්", "තෝ", "ත්‍ර", "ත්‍රා", "ත්‍රි", "ත්‍රී",
        "ද ", "දා", "දැ", "දෑ", "දි", "දී", "දු", "දූ", "ද්", "දෝ", "ද්‍ර", "ද්‍රෝ", "ද්‍රා", "ද්‍රි", "ද්‍රී",
        "න", "නා", "නැ", "නෑ", "නි", "නී", "නු", "නූ", "න්", "නෝ", "න්‍ර", "න්‍රා", "න්‍රි", "න්‍රී",
        "ප", "පා", "පැ", "පෑ", "පි", "පී", "පු", "පූ", "ප්", "ප්‍රෝ", "පෝ", "ප්‍ර", "ප්‍රා", "ප්‍රි", "ප්‍රී",
        "බ", "බා", "බැ", "බෑ", "බි", "බී", "බු", "බූ", "බ්", "බ්‍රෝ", "බ්‍ර", "බ්‍රා", "බ්‍රි", "බ්‍රී", "බ්‍රෝ",
        "ම", "මා", "මැ", "මෑ", "මි", "මී", "මු", "මූ", "ම්", "මෝ", "ම්‍ර", "ම්‍රා", "ම්‍රි", "ම්‍රී", "ම්‍රෝ",
        "ය", "යා", "යැ", "යෑ", "යි", "යී", "යු", "යූ", "ෝ", "ය්", "hda",
        "ර", "රා", "රැ", "රැ", "රු", "රූ", "රි", "රී",
        "ල", "ලා", "ලැ", "ලෑ", "ලි", "ලී", "ලු", "ලූ", "ල්", ",da",
        "ව", "වා", "වැ", "වෑ", "වි", "වී", "වු", "වූ", "ව්", "jda", "ව්‍ර", "ව්‍රා", "ව්‍රැ", "ව්‍රෑ", "j%da",
        "ශ", "ශා", "ශැ", "ශෑ", "ශි", "ශී", "ශු", "ශූ", "ශ්", "Yda", "ශ්‍ර", "ශ්‍රා", "ශ්‍රැ", "ශ්‍රෑ", "ශ්‍රි", "ශ්‍රී",
        "Y%da",
        "ෂ", "ෂා", "ෂැ", "ෂෑ", "ෂි", "ෂී", "ෂු", "ෂූ", "ෂ්", "Ida",
        "ස", "සා", "සැ", "සෑ", "සි", "සී", "සු", "සූ", "ida", "ස්‍ර", "ස්‍රා", "ස්‍රි", "ස්‍රී", "ස්",
        "හ", "හා", "හැ", "හෑ", "හි", "හී", "හු", "හූ", "හ්", "yda",
        "ළ", "ළා", "ළැ", "ළෑ", "ළි", "ළී",
        "ළූ", "ළූ",
        "ෆ", "ෆා", "ෆැ", "ෆෑ", "ෆි", "ෆී", "ෆූ", "ෆූ", "ෆ්‍ර", "ෆ්‍රි", "ෆ්‍රී", "ෆ්‍රැ", "ෆ්‍රෑ", "ෆ්", "*da",
        "ක්‍රා", "ක්‍රැ", "ක්‍රෑ", "l%da", ".%da",
        "ඛ", "ඛා", "ඛි", "ඛී", "ඛ්",
        "ඝ", "ඝා", "ඝැ", "ඝෑ", "ඝි", "ඝී", "ඝු", "ඝූ", ">da", "ඝ්", "ඝ්‍ර", "ඝ්‍රා", "ඝ්‍රි", "ඝ්‍රී",
        "ඳ", "ඳා", "ඳැ", "ෑ", "ඳෑ", "ඳි", "ඳී", "ඳු", "ඳූ", "|da ", " ඳ්",
        "ඟ", "ඟා", "ඟැ", " ඟෑ", " ඟි", "ඟී", " ඟු", " ඟූ", "Õda", "ඟ්",
        "ඬ", "ැ", "ඬා", " ඬැ", "ඬෑ", " ඬි", "ඬී", " ඬු", "ඬූ", "ඬda ", " ඬ්",
        "ඹ", "ඹා", " ඹැ", " ඹෑ", " ඹි", "ඹී", " ඹු", "ඹූ", "Uda", "ඹ්",
        "භ", "භා", "භැ", "භෑ", "භි", "භී", "භු", "භූ", "Nda", "භ්",
        "ධ", "ධා", "ධැ", "ධෑ", ",ධි", ",ධී", ",ධු", ",ධූ", "ධෝ", "ධ්",
        "ඨ", "ඨා", "ඨැ", "ඨි", "ඨී", "ඨු", "ඨූ", "ඨ්", "ඪ", "ඪා", "ඪි", "Vda",
        "ඵ", "ඵා", "ඵු", "ඵි", "Mda", "ඵ් ", "ථ", "ථා", "ථැ", "ථ්", "ා", "ෟ", "ණැ", "ණෑ", "ෘ", "ණී", "ණු", "ණූ",
        "Kda", "ණ්", "ඥ", "ඥා", "{da", "ඤ", "ඤා", "ඤු", "[da", "ඤ්", "ඣ", "ඣා", "ඣු", "COda",
        "ඣ්", "ඦ", "ඦා", "ඦැ", "ඦෑ", "ඦි", "ඦු", "ඦූ", "ඦෝ",
        "ඦ්", "ඡ", "ඡා", "ඡැ", "ඡෑ", "ඡි", "ඡේ", "තැ", "තෑ", "ත්‍රැ", "ත්‍රෑ", ";%da",
        "ළු", "ෲ", "HQ", "ff", "f", "H", "Hq"
    ]

    def categorize_character(char):
        """Categorize each Sinhala character"""
        char = char.strip()

        # Independent vowels
        if char in ["අ", "ආ", "ඇ", "ඈ", "ඉ", "ඊ", "උ", "එ", "ඒ", "ඔ", "ඕ"]:
            return "independent_vowel"

        # Base consonants (single characters)
        elif char in ["ක", "ග", "ච", "ජ", "ට", "ඩ", "ණ", "ත", "ද", "න", "ප", "බ", "ම", "ය", "ර", "ල", "ව", "ශ", "ෂ",
                      "ස", "හ", "ළ", "ෆ", "ඛ", "ඝ", "ඳ", "ඟ", "ඬ", "ඹ", "භ", "ධ", "ඨ", "ඪ", "ඵ", "ථ", "ඥ", "ඤ", "ඣ",
                      "ඦ", "ඡ"]:
            return "base_consonant"

        # Consonant + vowel combinations
        elif any(vowel in char for vowel in ["ා", "ැ", "ෑ", "ි", "ී", "ු", "ූ", "ෝ", "ේ", "ො"]):
            return "consonant_vowel_combination"

        # Consonant + ර combinations
        elif "්‍ර" in char:
            return "consonant_r_combination"

        # Consonant clusters (with halanta ්)
        elif "්" in char and len(char) > 1:
            return "consonant_cluster"

        # Encoded/special characters
        elif any(marker in char for marker in ["da", "HQ", "ff", "f", "H", "Hq"]):
            return "encoded_character"

        # Other vowel signs
        elif char in ["ා", "ැ", "ෑ", "ි", "ී", "ු", "ූ", "ෝ", "ේ", "ො", "ෘ", "ෟ", "ෲ"]:
            return "vowel_sign"

        else:
            return "other"

    # Create the mapping structure
    unicode_mapping = {
        "dataset_info": {
            "total_classes": len(sinhala_classes),
            "dataset_name": "Sinhala Letter 454",
            "source": "https://www.kaggle.com/datasets/sathiralamal/sinhala-letter-454",
            "description": "Sinhala handwritten character recognition dataset",
            "created_by": "Group 2025-Y2-S1-MLB-B8G1-04",
            "team_members": [
                "IT24102111 - Thiqa Zibrij A.G",
                "IT24102160 - Gangamini A.H.A.",
                "IT24102051 - Madhushan P.S.A.D.Y",
                "IT24102031 - Disanayaka K.G.G.S",
                "IT24102090 - Bandara D M R M",
                "IT24102032 - Thilina N.A.D.I.D"
            ]
        },
        "class_to_unicode": {},
        "unicode_to_class": {},
        "category_distribution": {}
    }

    # Build the mappings
    category_counts = {}

    for i, char in enumerate(sinhala_classes, 1):  # Start from class 1
        class_id = str(i)
        char_clean = char.strip()
        category = categorize_character(char_clean)

        # Count categories
        category_counts[category] = category_counts.get(category, 0) + 1

        # Create character info
        char_info = {
            "unicode": char_clean,
            "category": category,
            "class_id": i,
            "index": i - 1  # 0-based index for programming
        }

        # Add to mappings
        unicode_mapping["class_to_unicode"][class_id] = char_info
        unicode_mapping["unicode_to_class"][char_clean] = i

    # Add category distribution
    unicode_mapping["category_distribution"] = category_counts

    return unicode_mapping


def save_mapping():
    """Save the Unicode mapping to JSON file"""

    # Create directory structure
    base_path = Path(".")
    mapping_dir = base_path / "data" / "mappings"
    mapping_dir.mkdir(parents=True, exist_ok=True)

    # Generate mapping
    mapping = create_unicode_mapping()

    # Save to file
    output_file = mapping_dir / "unicode_mapping.json"
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(mapping, f, indent=2, ensure_ascii=False)

    print("=" * 60)
    print("UNICODE MAPPING CREATED SUCCESSFULLY!")
    print("=" * 60)
    print(f"📄 File saved: {output_file}")
    print(f"📊 Total classes: {mapping['dataset_info']['total_classes']}")
    print("\n📈 Category Distribution:")
    for category, count in mapping['category_distribution'].items():
        print(f"   {category}: {count}")

    print("\n✅ Examples:")
    for i in [1, 12, 25, 100, 200, 454]:
        if str(i) in mapping['class_to_unicode']:
            char_info = mapping['class_to_unicode'][str(i)]
            print(f"   Class {i}: '{char_info['unicode']}' ({char_info['category']})")

    print(f"\n🎯 Ready for preprocessing! Each member can now use this mapping.")
    print("=" * 60)

    return output_file


if __name__ == "__main__":
    save_mapping()