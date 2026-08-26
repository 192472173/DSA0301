# Generate a Parse Tree using Context-Free Grammar (CFG)

import nltk
from nltk import CFG
from nltk.parse import ChartParser

# Define the CFG grammar
grammar = CFG.fromstring("""
S  -> NP VP
NP -> Det N
VP -> V NP
Det -> 'the'
N -> 'cat' | 'dog'
V -> 'chased' | 'saw'
""")

# Create the parser
parser = ChartParser(grammar)

# Input sentence
sentence = input("Enter the sentence: ").lower().split()

# Parse the sentence
try:
    trees = list(parser.parse(sentence))

    if trees:
        print("Parse Tree:")
        for tree in trees:
            print(tree)
            tree.pretty_print()   # Displays the parse tree
    else:
        print("Sentence cannot be parsed.")
except ValueError:
    print("Invalid sentence!")
