#!/usr/bin/python3
import json
"""
Module that writes string file.txt
"""


def from_json_string(my_str):
    """Returns a Python object represented by a JSON string."""
    return json.loads(my_str)
