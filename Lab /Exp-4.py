from nltk.stem import PorterStemmer
ps = PorterStemmer()
words = ["relational", "conditional", "running", "studies", "happiness"]
print("Step-by-Step Porter Stemming")
for word in words:
    print(word, " --> ", ps.stem(word))
