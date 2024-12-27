

import requests
from bs4 import BeautifulSoup
import csv
from itertools import zip_longest


def getSalary(url):

    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'max-age=0',
        'if-none-match': 'W/"41862-+S5C3tWB8iYF6QjsfqIBrI66bO0"',
        'priority': 'u=0, i',
        'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        src = response.text
        soup = BeautifulSoup(src, "html.parser")
        # with open("salaryPage.html", "w", encoding='utf-8' ) as page:
        #     page.write(src)

        jobSalary = soup.find_all("script")
        return jobSalary

    return None


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

    jobSalary = getSalary(l)

    if jobSalary:
        print(jobSalary)
        salary.append(jobSalary.text.strip())
    else:
        salary.append('Not mentioned')

file_list = [title, company, location, skill, link, salary]
exported = zip_longest(*file_list)

with open("wuzzuf.csv", "w") as myfile:
    wr = csv.writer(myfile)
    wr.writerow(["Job Title", "Company Name", "Location Name", "Job Skills", "Link", "Salary"])
    wr.writerows(exported)