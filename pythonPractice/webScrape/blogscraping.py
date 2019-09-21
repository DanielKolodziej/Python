import requests
from bs4 import BeautifulSoup
from csv import writer

response = requests.get('https://danielkolodziej.github.io/')

soup = BeautifulSoup(response.text, 'html.parser')

skills = soup.find_all(class_='skill-item')

# write to csv file
with open('skills.csv', 'w') as csv_file:
    csv_writer = writer(csv_file)
    headers = ['Title', 'Text']
    csv_writer.writerow(headers)

    for skill in skills:
        # print(skill)
        # .get_text().replace('\n', '')
        title = skill.find('h3').get_text()
        print(title)
        text = skill.find('p').get_text()
        print(text)
        csv_writer.writerow([title, text])
