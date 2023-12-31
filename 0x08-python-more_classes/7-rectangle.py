#!/usr/bin/python3
"""7-rectangle.
"""


class Rectangle:
    """
    A class that defines a rectangle and provides methods to manipulate it.

    Attributes:
        number_of_instances (int): A class attribute that keeps tracks.
        print_symbol (str): A class attribute representing the symbol used.

    Methods:
        __init__(self, width=0, height=0): Initializes a new Rectangl.
        width (property): Retrieves the width of the rectangle.
        width (setter): Sets the width of the rectangle and validates it.
        height (property): Retrieves the height of the rectangle.
        height (setter): Sets the height of the rectangle and validates it.
        area(self): Calculates and returns the area of the rectangle.
        perimeter(self): Calculates and returns the perimeter of the rectangle.
        __str__(self): Returns a string representation of the rectangle.
        __repr__(self): Returns a string representation of a rectangle object.
        __del__(self): Prints a message when instance of Rectangle is deleted.

    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initializes a new Rectangle instance with the given width and height.

        Args:
            width (int, optional): The width of the rectangle. Defaults to 0.
            height (int, optional): The height of the rectangle. Defaults to 0.
        """
        self.__w = width
        self.__h = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """
        Retrieves the width of the rectangle.

        Returns:
            int: The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the width of the rectangle and validates it.

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
        self.__w = value

    @property
    def height(self):
        """
        Retrieves the height of the rectangle.

        Returns:
            int: The height of the rectangle.
        """
        return self.__h

    @height.setter
    def height(self, value):
        """
        Sets the height of the rectangle and validates it.

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
        self.__h = value

    def area(self):
        """
        Calculates and returns the area of the rectangle.

        Returns:
            int: The area of the rectangle (width * height).
        """
        return self.__w * self.__h

    def perimeter(self):
        """
        Calculates and returns the perimeter of the rectangle.

        Returns:
            int: The perimeter of the rectangle (2 * (width + height)).
        """
        if self.__w == 0 or self.__h == 0:
            return 0
        return 2 * (self.__w + self.__h)

    def __str__(self):
        """
        Returns a string representation of the rectangle.

        Returns:
            str: A string representing the rectangle using print_symbol.
        """
        if self.__w == 0 or self.__h == 0:
            return ""
        symbol_line = str(self.print_symbol) * self.__w
        return '\n'.join([symbol_line for _ in range(self.__h)])

    def __repr__(self):
        """
        Returns a string representation of the rectangle object.

        Returns:
            str: A string representing the rectangle object.
        """
        return f"{self.__class__.__name__}({self.__w}, {self.__h})"

    def __del__(self):
        """
        Prints a message when an instance of Rectangle is deleted.
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
