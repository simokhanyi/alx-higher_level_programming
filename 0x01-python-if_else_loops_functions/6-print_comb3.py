#!/usr/bin/python3
# 6-print_comb3.py

for first_digit in range(10):
    for second_digit in range(first_digit + 1, 10):
        print(format"{first_digit}{second_digit}", end=', ')
        
# Print a newline character to end the last line
print()
