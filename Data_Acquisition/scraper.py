from bs4 import BeautifulSoup
import requests
import csv

base_url = 'https://deleuze.cla.purdue.edu/seminars/leibniz-and-baroque/lecture-'
num_lectures = 5 

# Open a CSV file for writing
with open('paragraphs.csv', 'w', newline='', encoding='utf-8-sig') as csvfile:
    csv_writer = csv.writer(csvfile)
    
    for lecture_number in range(1, num_lectures + 1):
        url = f'{base_url}{lecture_number:02d}.html'
        response = requests.get(url)
        webpage_content = response.text
        soup = BeautifulSoup(webpage_content, 'html.parser')
        paragraph_tags = soup.find_all('p')
        
        for p_tag in paragraph_tags:
            # Write each paragraph as a row in the CSV
            csv_writer.writerow([p_tag.text])
