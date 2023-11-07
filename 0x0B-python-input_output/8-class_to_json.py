#!/usr/bin/python3
"""
Module
"""

def class_to_json(obj):
    """
    Returns a dictionary representation of an object.

    This function checks if the object has an `__dict__` attribute.

    :param obj: The object for which to generate a dictionary representation.
    :return: A dictionary representation of the object.
    """
    dic = {}
    if hasattr(obj, "__dict__"):
        dic = obj.__dict__.copy()
    return dic
