#!/usr/bin/python3
import py_compile
import marshal

# Compile the .pyc file (if not already compiled)
py_compile.compile("hidden_4.py")

# Load the compiled module
with open("hidden_4.pyc", "rb") as file:
    code = marshal.load(file)

# Filter and print names that do not start with '__' in alphabetical order
names = sorted(name for name in code.co_names if not name.startswith('__'))
for name in names:
    print(name)
