#!/usr/bin/python3
"""
Module
"""


import sys
import json


def save_to_json_file(my_obj, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(my_obj, file)

def load_from_json_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return json.load(file)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        return []


if __name__ == "__main__":
    try:
        json_list = load_from_json_file('add_item.json')
    except FileNotFoundError:
        json_list = []

    for i in range(1, len(sys.argv)):
        json_list.append(sys.argv[i])
    save_to_json_file(json_list, "add_item.json")
