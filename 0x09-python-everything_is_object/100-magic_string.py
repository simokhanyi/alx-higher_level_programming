#!/usr/bin/python3
"""pythonic
"""


def magic_string():
    """
    Generate a "BestSchool" string with increasing "BestSchool, " parts.

    Returns:
        str: A string with "BestSchool, " repeated a number of times based
        on the number of function calls.

    Example:
        For the first call, it returns "BestSchool".
        For the second call, it returns "BestSchool, BestSchool".
        For the third call, it returns "BestSchool, BestSchool, BestSchool".
    """
    magic_string.counter = getattr(magic_string, "counter", -1) + 1
    return "BestSchool, " * magic_string.counter + "BestSchool"
