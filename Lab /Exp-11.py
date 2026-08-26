# Simple Top-Down Parser (Recursive Descent Parser)

# Grammar:
# S -> a A
# A -> b A | c

class TopDownParser:
    def __init__(self, string):
        self.string = string
        self.index = 0

    # Parse S -> a A
    def S(self):
        if self.match('a'):
            return self.A()
        return False

    # Parse A -> b A | c
    def A(self):
        if self.match('b'):
            return self.A()
        elif self.match('c'):
            return True
        return False

    # Match current character
    def match(self, symbol):
        if self.index < len(self.string) and self.string[self.index] == symbol:
            self.index += 1
            return True
        return False

    # Start parsing
    def parse(self):
        if self.S() and self.index == len(self.string):
            return "String Accepted"
        else:
            return "String Rejected"


# Main Program
input_string = input("Enter the input string: ")

parser = TopDownParser(input_string)
print(parser.parse())
