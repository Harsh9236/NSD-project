def extract_bracketed_text(input_filepath="response.txt", output_filepath="score.txt"):
    """
    Extracts text stored within angled brackets from input.txt and saves it to output.txt.

    Args:
        input_filepath (str, optional): Path to the input file. Defaults to "input.txt".
        output_filepath (str, optional): Path to the output file. Defaults to "output.txt".
    """

    try:
        with open(input_filepath, 'r') as infile, open(output_filepath, 'w') as outfile:
            text = infile.read()  # Read the entire input file content
            extracted_texts = []
            current_bracketed_text = ""
            inside_brackets = False

            for char in text:
                if char == '<':
                    inside_brackets = True
                    current_bracketed_text = ""  # Start a new bracketed text
                elif char == '>':
                    inside_brackets = False
                    if current_bracketed_text: # Avoid adding empty strings if <> is encountered
                        extracted_texts.append(current_bracketed_text)
                elif inside_brackets:
                    current_bracketed_text += char

            for extracted_text in extracted_texts:
                outfile.write(extracted_text + '\n') # Write each extracted text to a new line

    except FileNotFoundError:
        print(f"Error: Input file '{input_filepath}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    extract_bracketed_text()
