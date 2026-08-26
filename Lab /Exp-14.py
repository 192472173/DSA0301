# Subject-Verb Agreement Checker

grammar = {
    "I": "am",
    "You": "are",
    "We": "are",
    "They": "are",
    "He": "is",
    "She": "is",
    "It": "is"
}

sentence = input("Enter sentence: ").split()

if len(sentence) >= 2:
    subject = sentence[0]
    verb = sentence[1]

    if subject in grammar and grammar[subject] == verb:
        print("Sentence is grammatically correct.")
    else:
        print("Subject-Verb Agreement Error.")
else:
    print("Invalid sentence.")
