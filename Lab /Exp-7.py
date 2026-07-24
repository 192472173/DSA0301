from nltk.stem import PorterStemmer
from nltk.stem import LancasterStemmer
from nltk.stem import SnowballStemmer

porter = PorterStemmer()
lancaster = LancasterStemmer()
snowball = SnowballStemmer("english")

words = ["running", "studies", "happiness", "relational", "playing"]

print("Word\t\tPorter\t\tLancaster\tSnowball")

for word in words:
    print(f"{word}\t\t{porter.stem(word)}\t\t{lancaster.stem(word)}\t\t{snowball.stem(word)}")
