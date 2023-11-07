#!/usr/bin/python3
"""
Module that reads text files
"""


def read_file(filename=""):
    """
    Reads a text file (UTF8) and prints its contents to stdout.

    :param filename: The name of file to be read (default is an empty string).
    :type filename: str
    """
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            print(line, end='')


if __name__ == "__main__":
    read_file("my_file_0.txt")
