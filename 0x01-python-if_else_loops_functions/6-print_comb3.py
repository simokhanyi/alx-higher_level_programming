#!/usr/bin/python3
# 6-print_comb3.py

# Iterate through the first digit
for first_digit in range(0, 10):
    # Iterate through the second digit, starting from the next one
    for second_digit in range(first_digit + 1, 10):
        # Check if it's the last combination
        if first_digit == 8 and second_digit == 9:
            print("{}{}".format(first_digit, second_digit))
        else:
            print("{}{}".format(first_digit, second_digit), end=", ")

