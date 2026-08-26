# Simple Earley Parser for Context-Free Grammar

from collections import defaultdict

# Grammar:
# S -> A B
# A -> a
# B -> b

grammar = {
    "S": [["A", "B"]],
    "A": [["a"]],
    "B": [["b"]]
}

class State:
    def __init__(self, lhs, rhs, dot, start):
        self.lhs = lhs
        self.rhs = rhs
        self.dot = dot
        self.start = start

    def __eq__(self, other):
        return (self.lhs == other.lhs and
                self.rhs == other.rhs and
                self.dot == other.dot and
                self.start == other.start)

    def __hash__(self):
        return hash((self.lhs, tuple(self.rhs), self.dot, self.start))

    def __repr__(self):
        return f"{self.lhs} -> {' '.join(self.rhs[:self.dot])} • {' '.join(self.rhs[self.dot:])}, {self.start}"

def earley_parse(words):
    n = len(words)
    chart = [set() for _ in range(n + 1)]

    # Initial state
    chart[0].add(State("GAMMA", ["S"], 0, 0))

    for i in range(n + 1):
        changed = True
        while changed:
            changed = False
            for state in list(chart[i]):

                # Predictor
                if state.dot < len(state.rhs):
                    symbol = state.rhs[state.dot]
                    if symbol in grammar:
                        for production in grammar[symbol]:
                            new_state = State(symbol, production, 0, i)
                            if new_state not in chart[i]:
                                chart[i].add(new_state)
                                changed = True

                # Scanner
                elif i < n:
                    pass

                # Completer
                if state.dot == len(state.rhs):
                    for old_state in list(chart[state.start]):
                        if (old_state.dot < len(old_state.rhs) and
                                old_state.rhs[old_state.dot] == state.lhs):
                            new_state = State(old_state.lhs,
                                              old_state.rhs,
                                              old_state.dot + 1,
                                              old_state.start)
                            if new_state not in chart[i]:
                                chart[i].add(new_state)
                                changed = True

        # Scanner Step
        if i < n:
            for state in list(chart[i]):
                if state.dot < len(state.rhs):
                    symbol = state.rhs[state.dot]
                    if symbol == words[i]:
                        chart[i + 1].add(
                            State(state.lhs, state.rhs, state.dot + 1, state.start)
                        )

    final_state = State("GAMMA", ["S"], 1, 0)

    if final_state in chart[n]:
        print("String Accepted")
    else:
        print("String Rejected")


# Main Program
input_string = input("Enter the input string: ")
tokens = list(input_string)

earley_parse(tokens)
