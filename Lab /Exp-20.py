from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

documents = [
    "Natural language processing",
    "Machine learning and AI",
    "Python programming language"
]

query = input("Enter search query: ")

vectorizer = TfidfVectorizer()

tfidf = vectorizer.fit_transform(documents + [query])

similarity = cosine_similarity(tfidf[-1], tfidf[:-1])

best = similarity.argmax()

print("Most Relevant Document:")
print(documents[best])
