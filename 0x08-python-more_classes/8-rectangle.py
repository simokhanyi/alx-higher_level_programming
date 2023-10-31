#!/usr/bin/python3
"""8-rectangle
"""


class Rectangle:
    """
    Rectangle class represents a geometric rectangle.

    Attributes:
        number_of_instances (int): A class attribute of rectangles.
        print_symbol: The symbol used for string representation of rectangles.

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
        __str__(self): Returns a string representation of the rectangle.
        __repr__(self): Returns a string representation to recreate instance.
        __del__(self): Destructor that gets called when an instance is deleted.
        bigger_or_equal(rect_1, rect_2): Compares two rectangles.

    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initializes a new Rectangle instance.

        Args:
            width (int, optional): The width of the rectangle (default is 0).
            height (int, optional): The height of the rectangle (default is 0).
        """
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

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
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
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
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Calculates the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculates the perimeter of the rectangle.

        Returns:
            int: The perimeter of the rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2

    def __str__(self):
        """
        Returns a string representation of the rectangle.

        Returns:
            str: A string containing the rectangle's representation.
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        symbol_line = str(self.print_symbol) * self.__width
        return '\n'.join([symbol_line for _ in range(self.__height)]

    def __repr__(self):
        """
        Returns a string representation to recreate a new instance.

        Returns:
            str: A string representation that can be used to create instance.
        """
        return f"{self.__class__.__name__}({self.__width}, {self.__height})"

        def __del__(self):
        """
        Destructor method that gets called when an instance is deleted.
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

        @ staticmethod
        def bigger_or_equal(rect_1, rect_2):
        """
        Compares two rectangles.

        Args:
            rect_1 (Rectangle): The first rectangle for comparison.
            rect_2 (Rectangle): The second rectangle for comparison.

        Returns:
            Rectangle: The larger or equal rectangle.

        Raises:
            TypeError: If rect_1 or rect_2 is not an instance of Rectangle.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2
