#!/usr/bin/python3
# 8-uppercase.py

def uppercase(input_str):
    """Print a string in uppercase."""
    for char in input_str:
        if 'a' <= char <= 'z':
            # Convert lowercase letters to uppercase by shifting ASCII value
            uppercase_char = chr(ord(char) - 32)
            print("{}".format(uppercase_char), end="")
        else:
            print("{}".format(char), end="")
        print("")
