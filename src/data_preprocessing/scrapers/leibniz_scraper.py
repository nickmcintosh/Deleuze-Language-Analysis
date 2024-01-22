from bs4 import BeautifulSoup
import requests


base_url = 'https://deleuze.cla.purdue.edu/lecture/lecture-'

url_endings = ['01-7/', '02-8/', '03-5/',
               '04-6/', '05-6/', '06-6/',
               '07-6/', '08-5/', '09-5/',
               '10-5/', '11-5/', '12-5/',
               '13-6/', '14-4/', '15-4/',
               '16-4/', '17-4/', '18-4/',
               '19-4/', '20-4/']

with open('twenty_lectures.txt', 'w', encoding='utf-8-sig') as txtfile:
    for ending in url_endings:
        url = f'{base_url}{ending}'
        response = requests.get(url)
        webpage_content = response.text
        soup = BeautifulSoup(webpage_content, 'html.parser')
        english_content = soup.find('section', id='content-en')
        paragraphs = english_content.find_all('p')

        for i, paragraph in enumerate(paragraphs):
            if i == 4 or i > 5:
                txtfile.write(paragraph.get_text())
                txtfile.write('\n')
