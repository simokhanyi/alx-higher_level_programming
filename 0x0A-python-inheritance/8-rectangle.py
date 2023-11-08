#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""
Module with class Rectangle
"""


class Rectangle(BaseGeometry):
    """ Class representing a rectangle """

    def __init__(self, width, height):
        """ Constructor """
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)

    def area(self):
        """ Calculate the area of the rectangle """
        return self.__width * self.__height

    def __str__(self):
        """ Return a string representation of the rectangle """
        return f"[Rectangle] {self.__width}/{self.__height}"
