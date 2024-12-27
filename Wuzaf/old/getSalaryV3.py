import json
from bs4 import BeautifulSoup
import re

# Load the HTML file
with open('salaryPage.html', 'r', encoding='utf-8') as file:
    content = file.read()

# Parse the HTML content
soup = BeautifulSoup(content, 'html.parser')

# Find all script tags
script_tags = soup.find_all('script')

# Extract the JSON part
jsonPart = script_tags[0].text.split('Wuzzuf.initialStoreState = ')[-1].split('Wuzzuf.serverRenderedURL = ')[0].strip()
# Remove the last semicolon
jsonPart = jsonPart.rstrip(';')  # This ensures the semicolon is removed

try:
    # Parse the JSON string
    data = json.loads(jsonPart)

    # Navigate to the salary information
    if 'salary' in data:
        salary_details = data['salary']
        print('Salary Details:', salary_details)
    else:
        print('Salary information not found in the JSON.')
except json.JSONDecodeError as e:
    print('Error parsing JSON:', e)
