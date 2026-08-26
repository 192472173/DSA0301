from nltk.wsd import lesk

sentence = input("Enter sentence: ").split()

word = input("Word to disambiguate: ")

sense = lesk(sentence, word)

print("Sense:", sense)
print("Meaning:", sense.definition())
