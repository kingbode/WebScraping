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

print(script_tags[0].text)

# Find the JSON starting point using regex
match = re.search(r'Wuzzuf\.initialStoreState\s*=\s*(\{.*?\});', script_tags[0].text, re.DOTALL)

# Look for the script containing the salary data
for script in script_tags:
    if 'salary' in script.string or '':
        try:
            # Attempt to parse the JSON-like data
            salary_data = json.loads(script.string)
            # Check for salary information
            if 'salary' in salary_data:
                salary_details = salary_data['salary']
                print('Salary Details:', salary_details)
                break
        except (TypeError, json.JSONDecodeError):
            continue

# If salary data is not found
else:
    print('Salary information not found.')
