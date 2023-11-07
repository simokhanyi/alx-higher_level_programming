#!/usr/bin/python3
"""
Module that writes string file.txt
"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file (UTF8) and returns the number of characters.

    :param filename: The name of the file to write to (default an empty string.
    :type filename: str
    :param text: The text to be written to the file (default an empty string).
    :type text: str
    :return: The number of characters in the file after writing.
    :rtype: int
    """
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(text)
    with open(filename, 'r', encoding='utf-8') as file:
        return len(file.read())


if __name__ == "__main__":
    nb_characters = write_file("my_first_file.txt", "This School is so cool!\n")
    print(nb_characters)
