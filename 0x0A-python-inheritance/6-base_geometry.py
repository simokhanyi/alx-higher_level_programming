#!/usr/bin/python3
"""
Module with class BaseGeometry
"""


class BaseGeometry:
    """
    A class that represents a basic geometry object.
    """

    def area(self):
        """
        Calculate the area of the geometry object.

        Raises:
            Exception: This method is not implemented.
        """
        raise Exception("area() is not implemented")

# Test the code


if __name__ == '__main__':
    bg = BaseGeometry()

    try:
        print(bg.area())
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))
