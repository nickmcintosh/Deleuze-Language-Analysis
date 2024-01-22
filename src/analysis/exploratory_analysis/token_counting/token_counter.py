import spacy
import csv
from collections import defaultdict


nlp = spacy.load('en_core_web_sm')

text = open('Data_Cleaning/DLGE_v1.3.txt', 'r', encoding='utf-8-sig').read()
text = text.lower()

doc = nlp(text)
lemmatized_token_counts = defaultdict(int)

for token in doc:
    if not token.is_alpha:
        pass
    elif token.is_stop:
        pass
    else:
        token_lemma = token.lemma_
        lemmatized_token_counts[token_lemma] += 1


sorted_token_counts = dict(
    sorted(lemmatized_token_counts.items(), key=lambda item: item[1], reverse=True))


csv_file_path = 'word_counts.csv'
with open(csv_file_path, mode='w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['WORD', 'COUNT'])
    for token, count in sorted_token_counts.items():
        writer.writerow([token, count])

print(f'Data saved to {csv_file_path}')
