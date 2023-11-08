#!/usr/bin/python3
import json
"""
Module
"""


def to_json_string(my_obj):
    """
    Return the JSON representation of an object as a string.

    :param my_obj: The object to be converted to a JSON string.
    :return: The JSON representation of the object.
    """
    return json.dumps(my_obj)
