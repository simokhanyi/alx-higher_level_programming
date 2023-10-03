#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number > 0:
    print("The {} is positive".format(number))
elif number == 0:
    print("The {} is zero".format(number))
else:
    print("The {} is negative".format(number))
