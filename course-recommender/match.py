import json
import re

def process_text_to_words(text):

    text = text.lower()
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    words = set(text.split())
    return words

def find_matching_ids(file1_path, file2_path):

    try:
        with open(file1_path, 'r') as f1, open(file2_path, 'r') as f2:
            skill_categories = json.load(f1)
            entries = json.load(f2)
    except FileNotFoundError:
        return {"error": "One or both of the input files were not found."}
    except json.JSONDecodeError:
        return {"error": "Error decoding JSON from one or both of the files. Please ensure they are valid JSON."}

    category_word_sets = [process_text_to_words(category) for category in skill_categories]
    matching_ids = []

    for entry in entries:
        if 'ID' not in entry or 'skills' not in entry:
            print(f"Warning: Entry missing 'ID' or 'skills' key: {entry}")
            continue # Skip this entry if it's malformed

        entry_id = entry['ID']
        entry_skills = entry['skills']
        entry_skill_word_sets = [process_text_to_words(skill) for skill in entry_skills]

        for entry_skill_words in entry_skill_word_sets:
            for category_words in category_word_sets:
                if entry_skill_words.intersection(category_words):
                    matching_ids.append(entry_id)
                    return_ids = list(set(matching_ids))

    return list(set(matching_ids))

if __name__ == "__main__":
    file1_path = "skills.json"
    file2_path = "courses.json"

    result_ids = find_matching_ids(file1_path, file2_path)

    if "error" in result_ids:
        print(f"Error: {result_ids['error']}")
    else:
        output_data = result_ids
        with open('recommendations.json', 'w') as outfile:
            json.dump(output_data, outfile, indent=2)
        print("Matching IDs written to recommendations.json")
