#!/usr/bin/python3
"""9-rectangle.
"""


class Rectangle:
    """
    Rectangle class represents a geometric rectangle.

    Attributes:
        number_of_instances (int): A class attribute to count instances .
        print_symbol (str): The symbol used for string of rectangles.

    Args:
        width (int, optional): The width of the rectangle (default is 0).
        height (int, optional): The height of the rectangle (default is 0).

    Methods:
        __init__(self, width=0, height=0): Initializes a Rectangle instance.
        width (property): Getter for the width attribute.
        width (setter): Setter for the width attribute.
        height (property): Getter for the height attribute.
        height (setter): Setter for the height attribute.
        area(self): Calculates the area of the rectangle.
        perimeter(self): Calculates the perimeter of the rectangle.
        _draw_rectangle(self): Helper method to draw the rectangle.
        __str__(self): Returns a string representation of the rectangle.
        __repr__(self): Returns a string representation to recreate instance.
        __del__(self): Destructor that gets called when an instance is deleted.
        bigger_or_equal(rect_1, rect_2): Compares two rectangles.
        square(cls, size=0): Creates a square with equal sides.

    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """
        Initializes a new Rectangle instance.

        Args:
            width (int, optional): The width of the rectangle (default is 0).
            height (int, optional): The height of the rectangle (default is 0).
        """
        type(self).number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Getter for the width attribute.

        Returns:
            int: The width of the rectangle.
        """
        return self.__width

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
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """
        Getter for the height attribute.

        Returns:
            int: The height of the rectangle.
        """
        return self.__height

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
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """
        Calculates and returns the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculates and returns the perimeter of the rectangle.

        Returns:
            int: The perimeter of the rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

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

    def __str__(self):
        """
        Returns a string representation of the rectangle.

        Returns:
            str: A string containing the rectangle's representation.
        """
        return self._draw_rectangle()

    def __repr__(self):
        """
        Returns a string representation to recreate an instance.

        Returns:
            str: A string representation that can be used to create instance.
        """
        return f"{self.__class__.__name__}({self.__width}, {self.__height})"

    def __del__(self):
        """
        Destructor method that gets called when an instance is deleted.
        """
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Compares two rectangles and returns the larger one.

        Args:
            rect_1 (Rectangle): The first rectangle for comparison.
            rect_2 (Rectangle): The second rectangle for comparison.

        Raises:
            TypeError: If rect_1 or rect_2 is not an instance of Rectangle.

        Returns:
            Rectangle: The larger or equal rectangle.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        return rect_1 if rect_1.area() >= rect_2.area() else rect_2

    @classmethod
    def square(cls, size=0):
        """
        Creates a square with equal sides.

        Args:
            size (int): Length of the sides of the square, defaults to 0.

        Returns:
            Rectangle: A new instance of the class with equal sides.
        """
        return cls(size, size)
