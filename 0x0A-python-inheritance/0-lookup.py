#!/usr/bin/python3
"""
Module with the method lookpu
"""


def lookup(obj):
    """
    Return the list of available attributes and methods of an object.

    Args:
        obj: The object to look up attributes and methods for.

    Returns:
        A list containing the names of attributes and methods.
    """
    return dir(obj)


class MyClass1(object):
    pass


class MyClass2(object):
    my_attr1 = 3

    def my_meth(self):
        pass


print(lookup(MyClass1))
print(lookup(MyClass2))
print(lookup(int))
