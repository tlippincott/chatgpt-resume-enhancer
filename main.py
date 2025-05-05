import requests
import json
from pathlib import Path

# Path to main.py
base_path = Path(__file__).parent

# Input and output file paths
input_file = base_path / 'chatgpt-resume-enhancer' / 'input-files' / 'test-input.txt'
output_file = base_path / 'chatgpt-resume-enhancer' / 'output-files' / 'test-output.txt'

# Test API endpoint (for now)
api_url = 'https://jsonplaceholder.typicode.com/posts/1'

# Optional headers (will use with ChatGPT)
headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer YOUR_API_KEY_HERE'
}

# Read the text from the input file
with open(input_file, 'r', encoding='utf-8') as file:
    text_data = file.read()

print(text_data)

# Prepare JSON payload
payload = {
    'text': text_data
}

# Send the request
# response = requests.post(api_url, headers=headers, json=payload)
response = requests.get(api_url)

# Save the response text to the output file
with open(output_file, 'w', encoding='utf-8') as file:
    file.write(response.text)

print(f"Response saved to {output_file}")
