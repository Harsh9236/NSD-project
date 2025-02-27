import json
import requests
import os

def send_json_and_prompt_to_openrouter(json_file_path, prompt, api_key, model_name):

    try:
        with open(json_file_path, 'r') as f:
            json_data = json.load(f)
    except FileNotFoundError:
        print(f"Error: JSON file not found at {json_file_path}")
        return None
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON format in {json_file_path}")
        return None

    api_url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": model_name,
        "messages": [
            {"role": "user", "content": f"{prompt}\n\nJSON Data:\n{json.dumps(json_data)}"}
        ]
    }

    try:
        response = requests.post(api_url, headers=headers, json=payload)
        response.raise_for_status()
        response_json = response.json()

        if 'choices' in response_json and response_json['choices']:
            output_text = response_json['choices'][0]['message']['content']
            return output_text
        else:
            print("Error: No 'choices' found in the API response or choices list is empty.")
            print("API Response:", response_json)
            return None

    except requests.exceptions.RequestException as e:
        print(f"API request error: {e}")
        print(f"Response content (if available): {e.response.content if e.response else 'No response content'}")
        return None

def save_output_to_file(output_text, output_file_path="output.txt"):

    try:
        with open(output_file_path, 'w') as f:
            f.write(output_text)
        print(f"Output saved to: {output_file_path}")
    except Exception as e:
        print(f"Error saving output to file: {e}")


if __name__ == "__main__":
    api_key = "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"
    json_file_path = "resume.json"
    prompt = "Analyze the resume and extract skills that the person possesses. Enclose the skills within angled brackets. Example <React>, <Python>, <AWS>, <Django>, <Git>"
    output_file_path = "response.txt"
    model_name = "google/gemini-2.0-flash-exp:free"

    output = send_json_and_prompt_to_openrouter(json_file_path, prompt, api_key, model_name)

    if output:
        save_output_to_file(output, output_file_path)
    else:
        print("Failed to get output from the model.")
