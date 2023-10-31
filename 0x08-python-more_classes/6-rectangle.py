#!/usr/bin/python3
"""
Rectangle Class

This module defines the `Rectangle` class.

Attributes:
    number_of_instances (int): A class attribute that keeps tracks.
    print_symbol: The symbol used for string representation of rectangles.

Methods:
    __init__(self, width=0, height=0): Initializes a Rectangle instance.
    width (property): Getter for the width attribute.
    width (setter): Setter for the width attribute.
    height (property): Getter for the height attribute.
    height (setter): Setter for the height attribute.
    area(self): Calculates the area of the rectangle.
    perimeter(self): Calculates the perimeter of the rectangle.
    __str__(self): Returns a string representation of the rectangle.
    __repr__(self): Returns a string representation to recreate a new instance.
    __del__(self): Destructor that gets called when an instance is deleted.
"""


class Rectangle:
    # Class attribute to keep track of the number of instances
    number_of_instances = 0
    # The symbol used for string representation of rectangles
    p = "#"

    def __init__(self, width=0, height=0):
        """
        Initializes a new Rectangle instance.

        Args:
            width (int, optional): The width of the rectangle (default is 0).
            height (int, optional): The height of the rectangle (default is 0).
        """
        self.__w = width
        self.__h = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """
        Getter for the width attribute.

        Returns:
            int: The width of the rectangle.
        """
        return self.__w

    @width.setter
    def width(self, value):
        """
        Setter for the width attribute.

        Args:
            value (int): The new width value.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__w = value

    @property
    def height(self):
        """
        Getter for the height attribute.

        Returns:
            int: The height of the rectangle.
        """
        return self.__h

    @height.setter
    def height(self, value):
        """
        Setter for the height attribute.

        Args:
            value (int): The new height value.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__h = value

    def area(self):
        """
        Calculates the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.__w * self.__h

    def perimeter(self):
        """
        Calculates the perimeter of the rectangle.

        Returns:
            int: The perimeter of the rectangle.
        """
        if self.__w == 0 or self.__h == 0:
            return 0
        return 2 * (self.__w + self.__h)

    def __str__(self):
        """
        Returns a string representation of the rectangle.

        Returns:
            str: A string containing the rectangle's representation.
        """
        if self.__w == 0 or self.__h == 0:
            return ""
        return '\n'.join([str(self.p) * self.__w for _ in range(self.__h)]

    def __repr__(self):
        """
        Returns a string representation to recreate a new instance.

        Returns:
            str: A string representation that can be used to create a instance.
        """
        return f"{self.__class__.__name__}({self.__w}, {self.__h})"

    def __del__(self):
        """
        Destructor method that gets called when an instance is deleted.
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
