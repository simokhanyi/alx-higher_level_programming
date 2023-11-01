#!/usr/bin/python3
"""
This prints square size.
"""


def print_square(size):
    """
    Print a square of a given size using the '#' character.

    :param size: The size length of the square as an integer.
    :raises TypeError: If size is not an integer or a float and less than 0.
    :raises ValueError: If size is less than 0.
    """
    if not isinstance(size, int) or (isinstance(size, float) and size < 0):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)


if __name__ == "__main__":
    print_square(4)
    print("")
    print_square(10)
    print("")
    print_square(0)
    print("")
    print_square(1)
    print("")

    try:
        print_square(-1)
    except Exception as e:
        print(e)
    print("")
