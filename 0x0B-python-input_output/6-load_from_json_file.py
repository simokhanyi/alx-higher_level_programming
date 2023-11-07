#!/usr/bin/python3
import json
"""
Module
"""


def load_from_json_file(filename):
    """
    Reads a JSON file and creates an object from it.

    :param filename: The name of the JSON file to read and parse.
    :type filename: str
    :return: The Python object created from the JSON data in the file.
    """
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)


if __name__ == "__main__":
    filename = "my_list.json"
    my_list = load_from_json_file(filename)
    print(my_list)
    print(type(my_list))

    filename = "my_dict.json"
    my_dict = load_from_json_file(filename)
    print(my_dict)
    print(type(my_dict))

    try:
        filename = "my_set_doesnt_exist.json"
        my_set = load_from_json_file(filename)
        print(my_set)
        print(type(my_set))
    except FileNotFoundError as e:
        print("[{}] {}".format(e.__class__.__name__, e))

    try:
        filename = "my_fake.json"
        my_fake = load_from_json_file(filename)
        print(my_fake)
        print(type(my_fake))
    except ValueError as e:
        print("[{}] {}".format(e.__class__.__name__, e))
