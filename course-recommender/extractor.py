import re
import json

def extract_angled_bracket_items(input_filepath, output_filepath):

    try:
        with open(input_filepath, 'r') as infile:
            text = infile.read()
    except FileNotFoundError:
        print(f"Error: Input file not found at '{input_filepath}'")
        return

    bracket_pattern = r'<([^>]+)>'
    extracted_items = re.findall(bracket_pattern, text)

    try:
        with open(output_filepath, 'w') as outfile:
            json.dump(extracted_items, outfile, indent=4)
        print(f"Extracted items saved to '{output_filepath}'")
    except IOError:
        print(f"Error: Could not write to output file '{output_filepath}'")


if __name__ == "__main__":
    input_file = "response.txt"
    output_file = "skills.json"

    extract_angled_bracket_items(input_file, output_file)
