#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """
    This class represents a square.

    The Square class allows you to create and manipulate square objects with a specified size and position.

    Attributes:
        size (int): The size (side length) of the square.
        position (tuple): The position of the square represented as a tuple (x, y).
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a new Square instance with the given size and position.

        Args:
            size (int): The size (side length) of the square (default is 0).
            position (tuple): The position of the square as a tuple of two positive integers (default is (0, 0)).
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter for the size attribute.

        Args:
            value (int): The new size to set for the square.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        """
        Setter for the position attribute.

        Args:
            value (tuple): The new position to set for the square as a tuple of two positive integers.

        Raises:
            TypeError: If the value is not a tuple or is not of length 2, or if any element is not a positive integer.

        """
        if (
            not isinstance(value, tuple)
            or len(value) != 2
            or not all(isinstance(i, int) for i in value)
            or any(i < 0 for i in value)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Calculate and return the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Print the square to the standard output.
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)

    def __str__(self):
        """
        Convert the square to a string representation.

        Returns:
            str: A string representation of the square.
        """
        self.my_print()
        return ""

if __name__ == "__main__":
    my_square = Square(5, (0, 0))
    print(my_square)

    print("--")

    my_square = Square(5, (4, 1))
    print(my_square)
