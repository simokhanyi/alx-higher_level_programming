#!/usr/bin/python3
"""Defines a class Square"""

class Square:
    """
    This class represents a square with a given size and position.

    Attributes:
        size (int): The size of the square.
        position (tuple): The position of the square.
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a new Square instance with the given size and position.

        Args:
            size (int): The size (side length) of the square (default is 0).
            position (tuple): The position of the square (default is (0, 0)).

        Raises:
            TypeError: If the size is not an integer or if the position is not a tuple of two positive integers.
            ValueError: If the size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

        if (
            not isinstance(position, tuple)
            or len(position) != 2
            or not all(isinstance(i, int) for i in position)
            or any(i < 0 for i in position)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

    def area(self):
        """
        Calculates and returns the area of the square.

        Returns:
            int: The area of the square (size^2).
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints a textual representation of the square using '#' characters.
        If the size is 0, it prints an empty line, and the position is used to add leading spaces.
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
