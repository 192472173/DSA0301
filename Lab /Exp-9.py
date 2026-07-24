import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
ps = PorterStemmer()
with open("sample.txt", "r") as file:
    text = file.read()
print("Original Text:")
print(text)
words = word_tokenize(text)

print("\nOriginal Words:")
print(words)
stemmed_words = [ps.stem(word) for word in words]

print("\nStemmed Words:")
print(stemmed_words)
print("\nComparison:")
print("-" * 30)
print("Original\t\tStemmed")
print("-" * 30)

for original, stemmed in zip(words, stemmed_words):
    print(f"{original}\t\t{stemmed}")
