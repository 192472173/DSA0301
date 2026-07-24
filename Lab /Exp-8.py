from nltk.stem import PorterStemmer

ps = PorterStemmer()

words = [
    "university",
    "universe",
    "studies",
    "studying",
    "organization",
    "organizational"
]

print("Original\t\tStem")

for word in words:
    print(f"{word}\t\t{ps.stem(word)}")
