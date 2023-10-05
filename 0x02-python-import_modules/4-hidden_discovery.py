#!/usr/bin/python3
import marshal

# Load the compiled module
with open("hidden_4.pyc", "rb") as file:
    code = marshal.load(file)

# Extract and print names that do not start with '__'
names = [name for name in code.co_names if not name.startswith('__')]
names.sort()  # Sort the names alphabetically
for name in names:
    print(name)
