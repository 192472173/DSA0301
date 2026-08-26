import spacy

nlp = spacy.load("en_core_web_sm")

text = input("Enter sentence: ")

doc = nlp(text)

print("Noun Phrases:")

for chunk in doc.noun_chunks:
    print(chunk.text)
