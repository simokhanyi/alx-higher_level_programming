#!/usr/bin/python3
"""
Module with class BaseGeometry
"""


class BaseGeometry:
    """ Class with basic geometry methods """

    def area(self):
        """ Calculate the area (not implemented in BaseGeometry) """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Validate that a value is a positive integer """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
