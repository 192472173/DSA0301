text = input("Enter paragraph: ")

sentences = text.split('.')

if len(sentences) > 2:
    print("Text appears coherent.")
else:
    print("Short text. Coherence cannot be determined.")
