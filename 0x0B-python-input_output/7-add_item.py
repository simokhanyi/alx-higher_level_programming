#!/usr/bin/python3
"""
Module
"""


import sys
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file


def add_and_save_items_to_file(args):
    """
    Adds command-line arguments to Python list and saves it to a file as JSON.

    :param args: A list of command-line arguments.
    """
    try:
        # Load existing data from the file, if it exists
        existing_data = load_from_json_file("add_item.json")
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        existing_data = []

    # Add the new arguments to the list
    existing_data.extend(args)

    # Save the updated list to the file
    save_to_json_file(existing_data, "add_item.json")


if __name__ == "__main__":
    # Get command-line arguments excluding the script name
    args = sys.argv[1:]

    # Add and save the arguments to the file
    add_and_save_items_to_file(args)
