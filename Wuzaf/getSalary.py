

from bs4 import BeautifulSoup
import json
from pprint import pprint

with open("salaryPage.html", "r", encoding='utf-8') as inFile:
    salaryPage = inFile.read()



if 'Competitive salary and benefits Payment in USD' in salaryPage:
    print('found the salary\n')
else:
    print('salary not found')


jsonPart = salaryPage.split('Wuzzuf.initialStoreState = ')[1].strip()

jsonPart = jsonPart.split('Wuzzuf.serverRenderedURL = ')[0].strip()[:-1]

salaryJsonObject = json.loads(jsonPart)

salaryDicts = salaryJsonObject['entities']['job']['collection']

for key in salaryDicts:
    pprint(salaryDicts[key]['attributes']['salary'])
    break

# print(salaryJsonObject)