import spacy
import json

with open('Data_Cleaning/20_lectures_1.3.txt', 'r', encoding='utf-8-sig') as file:
    text = file.read()

nlp = spacy.load('en_core_web_sm')
nlp.max_length = 1700000
doc = nlp(text)

master_list = []
for sentence in doc.sents:
    token_list = []
    for token in sentence:
        if not token.is_alpha:
            pass
        elif token.is_stop:
            pass
        else:
            token_list.append(token.lemma_)
    master_list.append(token_list)

json_data = json.dumps(master_list, ensure_ascii=False, indent=4)
with open('20_lectures.json', 'w') as json_file:
    json_file.write(json_data)
