import requests
import json

# Input and output file paths
input_file = 'input.txt'
output_file = 'response.txt'

# Replace with your actual test API endpoint
api_url = 'https://example.com/api/analyze'  # Change to your real API URL

# Optional headers — include API key or other auth as needed
headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer YOUR_API_KEY_HERE'  # Replace with your key
}

# Read the text from the input file
with open(input_file, 'r', encoding='utf-8') as file:
    text_data = file.read()

# Prepare JSON payload
payload = {
    'text': text_data
}

# Send the request
response = requests.post(api_url, headers=headers, json=payload)

# Save the response text to the output file
with open(output_file, 'w', encoding='utf-8') as file:
    file.write(response.text)

print(f"Response saved to {output_file}")
