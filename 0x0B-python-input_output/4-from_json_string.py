#!/usr/bin/python3
import json
"""
Module that writes string file.txt
"""


def from_json_string(my_str):
    """
    Return an object represented by a JSON string.

    :param my_str: The JSON string to be converted into an object.
    :return: The Python data structure (object) represented by the JSON string.
    """
    return json.loads(my_str)
