text = input("Enter text: ")

sentences = text.split('.')

noun = ""

for sentence in sentences:
    words = sentence.split()

    for word in words:
        if word.istitle():
            noun = word

        if word.lower() in ["he", "she", "him", "her"]:
            print(word, "refers to", noun)
