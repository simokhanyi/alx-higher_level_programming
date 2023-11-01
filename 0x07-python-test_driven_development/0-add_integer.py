#!/usr/bin/python3
"""
This is the addition module.
it adds 2 integers
a and b must be first casted
"""


def add_integer(a, b=98):
    """
    Add two integers or floating-point numbers and return their sum.

    :param a: The first integer or floating-point number.
    :param b: The second integer or floating-point number (default is 98).
    :return: The sum of 'a' and 'b' as an integer.
    """
    if type(a) not in (int, float) or type(b) not in (int, float):
        raise TypeError("a must be an integer or b must be an integer")
    a = int(a)
    b = int(b)
    return a + b


if __name__ == "__main__":
    print(add_integer(1, 2))
    print(add_integer(100, -2))
    print(add_integer(2))
    print(add_integer(100.3, -2))
    try:
        print(add_integer(4, "School"))
    except Exception as e:
        print(e)
    try:
        print(add_integer(None))
    except Exception as e:
        print(e)
