#!/usr/bin/python3

class Square:
    """
    This class represents a square with a given size.

    Attributes:
        size (int): The size of the square.

    Methods:
        __init__(self, size=0): Initializes a new Square instance with the given size.
        area(self): Calculates and returns the area of the square.
    """
    def __init__(self, size=0):
        """
        Initializes a new Square instance with the given size.

        Args:
            size (int): The size (side length) of the square (default is 0).

        Raises:
            TypeError: If the size is not an integer.
            ValueError: If the size is less than 0.

        Returns:
            None
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Calculates and returns the area of the square.

        Returns:
            int: The area of the square (size^2).
        """
        return self.__size ** 2
