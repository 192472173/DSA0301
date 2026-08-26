import re

expression = input("Enter logical expression: ")

pattern = r'([A-Za-z]+)\((.*?)\)'

match = re.match(pattern, expression)

if match:
    print("Predicate:", match.group(1))
    print("Arguments:", match.group(2))
else:
    print("Invalid Expression")
