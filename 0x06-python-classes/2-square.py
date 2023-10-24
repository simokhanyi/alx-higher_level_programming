#!/usr/bin/python3
"""Defines a class Square"""

class Square:
    """
    This class represents a square with a given size.

    Attributes:
        The size of the square.
    """
    def __init__(self, size=0):
        """
        Initializes a new Square instance with the given size.

        Args:
            The size (side length) of the square (default is 0).
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
