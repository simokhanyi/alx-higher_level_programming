#!/usr/bin/python3
"""3-rectangle
"""


class Rectangle:
    """
    This class defines a Rectangle object with width and height attributes.

    Attributes:
        width (int): The width of the rectangle. Defaults 0 if not specified.
        height (int): The height of the rectangle. Defaults 0 if not specified.

    Methods:
        __init__(self, width=0, height=0): Initializes a new Rectangle.
        width (property): Retrieves the width of the rectangle.
        width (setter): Sets the width of the rectangle and validates it.
        height (property): Retrieves the height of the rectangle.
        height (setter): Sets the height of the rectangle and validates it.
        area(self): Calculates and returns the area of the rectangle.
        perimeter(self): Calculates and returns the perimeter of the rectangle.
        __str__(self): Returns a string representation of the rectangle.
        __repr__(self): Returns a string representation of rectangle object.
    """
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """
        Retrieve the width of the rectangle.

        Returns:
            int: The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Set the width of the rectangle and validate it.

        Args:
            value (int): The new width value.

        Raises:
            TypeError: If the width is not an integer.
            ValueError: If the width is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Retrieve the height of the rectangle.

        Returns:
            int: The height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Set the height of the rectangle and validate it.

        Args:
            value (int): The new height value.

        Raises:
            TypeError: If the height is not an integer.
            ValueError: If the height is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Calculate and return the area of the rectangle.

        Returns:
            int: The area of the rectangle (width * height).
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculate and return the perimeter of the rectangle.

        Returns:
            int: The perimeter of the rectangle (2 * (width + height)).
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        Return a string representation of the rectangle using '#' characters.

        Returns:
            str: A string representing the rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        return '\n'.join(['#' * self.__width for _ in range(self.__height)])

    def __repr__(self):
        """
        Return a string representation of the rectangle object.

        Returns:
            str: A string representing the rectangle object.
        """
        return f"<{self.__class__.__name__} object at {id(self):#x}>"
