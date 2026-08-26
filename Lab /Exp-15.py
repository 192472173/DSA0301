 import nltk
from nltk import PCFG
from nltk.parse import ViterbiParser

# Define the Probabilistic Context-Free Grammar (PCFG)
grammar = PCFG.fromstring("""
S -> NP VP [1.0]

NP -> Det N [0.6]
NP -> 'John' [0.4]

VP -> V NP [0.7]
VP -> V [0.3]

Det -> 'the' [0.6]
Det -> 'a' [0.4]

N -> 'dog' [0.5]
N -> 'cat' [0.5]

V -> 'sees' [0.6]
V -> 'runs' [0.4]
""")

# Create the parser
parser = ViterbiParser(grammar)

# Input sentence
sentence = "John sees the dog".split()

print("Input Sentence:", " ".join(sentence))
print("\nMost Probable Parse Tree:\n")

# Parse and display the result
for tree in parser.parse(sentence):
    print(tree)
    print("\nProbability:", tree.prob())
