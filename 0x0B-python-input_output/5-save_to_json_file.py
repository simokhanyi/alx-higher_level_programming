#!/usr/bin/python3
import json
"""
Module
"""


def save_to_json_file(my_obj, filename):
    """Writes an object to a text file, using a JSON representation."""
    with open(filename, "w") as f:
        json.dump(my_obj, f)
