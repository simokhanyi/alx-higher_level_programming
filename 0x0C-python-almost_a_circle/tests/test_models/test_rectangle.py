#!/usr/bin/python3
"""
Module that tests Rectangle
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from random import randrange
from contextlib import redirect_stdout
import io


class TestRectangle(unittest.TestCase):
    """
    Test cases for the Rectangle class in rectangle.py.
    """

    def test_rectangle_instance_creation(self):
        """
        Test the creation of a Rectangle instance and the initialization.
        """
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 1)

    def test_rectangle_instance_with_attributes(self):
        """
        Test creating instance with specified attributes.
        """
        r = Rectangle(5, 3, 2, 1, 50)
        self.assertEqual(r.id, 50)
        self.assertEqual(r.width, 5)
        self.assertEqual(r.height, 3)
        self.assertEqual(r.x, 2)
        self.assertEqual(r.y, 1)

    def test_rectangle_area(self):
        """
        Test the area method of the Rectangle class.
        """
        r = Rectangle(7, 4)
        self.assertEqual(r.area(), 28)

    def test_rectangle_str_representation(self):
        """
        Test the __str__ method for the string representation of Rectangle.
        """
        r = Rectangle(3, 8, 2, 1, 99)
        self.assertEqual(str(r), "[Rectangle] (99) 2/1 - 3/8")

    def test_rectangle_update_method(self):
        """
        Test the update method for updating attributes of Rectangle.
        """
        r = Rectangle(4, 6, 1, 2, 10)
        r.update(89)
        self.assertEqual(str(r), "[Rectangle] (89) 1/2 - 4/6")
        r.update(89, 2)
        self.assertEqual(str(r), "[Rectangle] (89) 1/2 - 2/6")
        r.update(89, 2, 3)
        self.assertEqual(str(r), "[Rectangle] (89) 1/2 - 2/3")
        r.update(89, 2, 3, 4)
        self.assertEqual(str(r), "[Rectangle] (89) 4/2 - 2/3")
        r.update(89, 2, 3, 4, 5)
        self.assertEqual(str(r), "[Rectangle] (89) 4/5 - 2/3")

    def test_rectangle_to_dictionary(self):
        """
        Test the to_dictionary method for Rectangle.
        """
        r = Rectangle(4, 6, 1, 2, 10)
        r_dictionary = r.to_dictionary()
        expected_dict = {
            'id': 10,
            'width': 4,
            'height': 6,
            'x': 1,
            'y': 2
        }
        self.assertDictEqual(r_dictionary, expected_dict)


if __name__ == '__main__':
    unittest.main()
