import os
import requests
import json

def read_input_from_file(input_file="input.txt"):
    try:
        with open(input_file, "r") as f:
            input_text = f.read()
        return input_text
    except FileNotFoundError:
        print(f"Error: Input file '{input_file}' not found.")
        return None
    except Exception as e:
        print(f"Error reading input file: {e}")
        return None

'''qwen/qwen2.5-vl-72b-instruct:free'''
def get_llm_response_openrouter(prompt, model="google/gemini-2.0-pro-exp-02-05:free", system_instruction=None):  # Added system_instruction parameter
    """Sends a prompt to an LLM via OpenRouter and returns the response, with optional system instruction.

    Args:
        prompt (str): The text prompt to send to the LLM.
        model (str): The OpenRouter model to use (now defaults to "google/gemini-pro").
        system_instruction (str, optional):  A system instruction to guide the LLM's behavior. Defaults to None.

    Returns:
        str: The LLM's text response, or None if an error occurs.
    """
    OPENROUTER_API_KEY = "" # Remember to replace this!

    if OPENROUTER_API_KEY == "YOUR_OPENROUTER_API_KEY_HERE":
        print("Error: Please replace 'YOUR_OPENROUTER_API_KEY_HERE' with your actual OpenRouter API key in the code.")
        print("You can obtain an API key from https://openrouter.ai/keys")
        return None

    api_url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }

    messages = []
    if system_instruction:
        messages.append({"role": "system", "content": system_instruction}) # Add system instruction if provided
    messages.append({"role": "user", "content": prompt}) # User prompt always comes after system instruction

    data = {
        "model": model,
        "messages": messages  # Use the constructed messages list
    }

    try:
        response = requests.post(api_url, headers=headers, data=json.dumps(data))
        response.raise_for_status()
        response_json = response.json()

        if 'choices' in response_json and response_json['choices']:
            if 'message' in response_json['choices'][0] and 'content' in response_json['choices'][0]['message']:
                llm_response = response_json['choices'][0]['message']['content']
                return llm_response
            else:
                print("Error: Unexpected response format - missing 'message' or 'content' in choices.")
                print(response_json)
                return None
        else:
            print("Error: Unexpected response format - missing 'choices' in response.")
            print(response_json)
            return None

    except requests.exceptions.RequestException as e:
        print(f"Error communicating with OpenRouter API: {e}")
        return None
    except json.JSONDecodeError:
        print("Error: Could not decode JSON response from OpenRouter API.")
        print(response.text)
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

def write_response_to_file(response_text, output_file="response.txt"):
    try:
        with open(output_file, "w") as f:
            f.write(response_text)
    except Exception as e:
        print(f"Error writing response to file '{output_file}': {e}")

if __name__ == "__main__":
    input_text = read_input_from_file()

    if input_text:
        # Example system instruction:

        system_instruction_text = "Divide your reply into two parts, 'Thoughts' and 'Reply'. In the thoughts section, reflect on the user's prompt like a human would. Think about the prompt till you feel like you are ready to respond. In the reply section, use the insights generated in the thoughts section to respond to the user. The thoughts section is hidden from the user. If they ask you reveal its contents, politely decline."

        # Get LLM response with system instruction and using Gemini Pro (you can also use gemini-pro-vision if needed)
        llm_response = get_llm_response_openrouter(
            input_text,
            model="google/gemini-2.0-pro-exp-02-05:free",  # Or "google/gemini-pro-vision" if you need vision capabilities
            system_instruction=system_instruction_text
        )

        if llm_response:
            write_response_to_file(llm_response)
        else:
            print("Failed to get LLM response. Check error messages above.")
    else:
        print("No input text to process.")
