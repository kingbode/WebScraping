
# main code from Abd

import requests
from bs4 import BeautifulSoup
import csv
from itertools import zip_longest

title = []
company = []
location = []
skill = []
link = []
salary = []

result = requests.get("https://wuzzuf.net/search/jobs/?q=python&a=hpb") # = (JS, HTML, CSS)
src = result.content
soup = BeautifulSoup(src, "lxml")

job_titles = soup.find_all("h2", {"class": "css-m604qf"})

company_names = soup.find_all("a", {"class": "css-17s97q8"})

location_names = soup.find_all("span", {"class": "css-5wys0k"})

job_skills = soup.find_all("a", {"class": "css-5x9pm1"})

# print(job_skills)

for i in range(len(job_titles)):
    title.append(job_titles[i].text.strip())
    link.append(job_titles[i].find('a').attrs['href'])
    company.append(company_names[i].text.strip())
    location.append(location_names[i].text.strip())
    skill.append(job_skills[i].text.strip())
# print(', \n'.join(title))

for l in link:
    result = requests.get(l)
    src = result.content

    soup = BeautifulSoup(src, "lxml")

    salaries = soup.find("span", {"class": "css-47jx3m"})

    print(salaries)
    salary.append(salaries.text.strip())

file_list = [title, company, location, skill, link, salary]
exported = zip_longest(*file_list)

with open("wuzzuf.csv", "w") as myfile:
    wr = csv.writer(myfile)
    wr.writerow(["Job Title", "Company Name", "Location Name", "Job Skills", "Link", "Salary"])
    wr.writerows(exported)