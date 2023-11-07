#!/usr/bin/python3
"""
Module that writes string file.txt
"""


def append_write(filename="", text=""):
    """
    Appends a string to the end of a text file (UTF8).

    :param filename: The name of file to append to (default an empty string).
    :type filename: str
    :param text: The text to be appended to the file (default an empty string).
    :type text: str
    :return: The number of characters added to the file.
    :rtype: int
    """
    with open(filename, 'a', encoding='utf-8') as file:
        return file.write(text)


if __name__ == "__main__":
    nb_characters_added = append_write("file_append.txt", "This School is so cool!\n")
    print(nb_characters_added)
