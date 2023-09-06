import spacy


with open('first_five_lectures_rough.txt', 'r') as f:
    text = f.read()
    lectures = text.split('LECTURE ')[1:]
    

lecture_1 = lectures[0]
lecture_2 = lectures[1]
nlp = spacy.load("en_core_web_lg")
doc = nlp(lecture_2)

sentences = list(doc.sents)


sentence = sentences[:4] 
print(sentence)

for sen in sentence:
    ents = list(sen.ents)
    for ent in ents:
        print(ent.text)
        print(ent.label_)






