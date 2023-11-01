#!/usr/bin/python3
"""
This prints my name.
"""


def say_my_name(first_name, last_name=""):
    """
    Print a message with the first name and last name.

    :param first_name: The first name as a string.
    :param last_name: The last name as a string (default is an empty string).
    :raises TypeError: If first_name or last_name is not a string.
    """
    if not isinstance(first_name, str) or not isinstance(last_name, str):
        raise TypeError("first_name must be a string")

    if last_name:
        print(f"My name is {first_name} {last_name}")
    else:
        print(f"My name is {first_name}")


if __name__ == "__main__":
    say_my_name("John", "Smith")
    say_my_name("Walter", "White")
    say_my_name("Bob")

    try:
        say_my_name(12, "White")
    except Exception as e:
        print(e)
