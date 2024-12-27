import json
from bs4 import BeautifulSoup
from pprint import pprint

# Load the HTML file
with open('salaryPage.html', 'r', encoding='utf-8') as file:
    content = file.read()

# Parse the HTML content
soup = BeautifulSoup(content, 'html.parser')

# Find all script tags
script_tags = soup.find_all('script')

jsonPart = script_tags[0].text.split('Wuzzuf.initialStoreState = ')[-1].split('Wuzzuf.serverRenderedURL = ')[0].strip()
# print(jsonPart)
jsonPart = jsonPart.rstrip(';')  # This ensures the semicolon is removed
# print(jsonPart)


try:
    # Parse the JSON string
    data = json.loads(jsonPart)

    entities = data['entities']['job']['collection']

    for entity in entities:
        salary_details = entities[entity]['attributes']['salary']
        print(salary_details)
        break
    # Navigate to the salary information
    # if 'salary' in data:
    #     salary_details = data['salary']
    #     print('Salary Details:', salary_details)
    # else:
    #     print('Salary information not found in the JSON.')
except json.JSONDecodeError as e:
    print('Error parsing JSON:', e)

