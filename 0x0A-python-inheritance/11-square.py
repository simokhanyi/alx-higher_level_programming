#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle
"""
module with class BaseGeometry
"""


class Square(Rectangle):
    """
    A class that represents a square, inheriting from Rectangle.
    """

    def __init__(self, size):
        """
        Initialize a Square instance with a size.

        Args:
            size (int): The size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than or equal to 0.
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """
        Return a string representation of the square.

        Returns:
            str: A string describing the square.
        """
        return "[Square] {}/{}".format(self.__size, self.__size)

# Test the code


if __name__ == '__main__':
    s = Square(13)
    print(s)
    print(s.area())
