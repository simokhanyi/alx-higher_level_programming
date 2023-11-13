#!/usr/bin/python3
"""
Module that test rectangle
"""
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """
    Test cases for the Rectangle class in models/rectangle.py.
    """

    def test_rectangle_instance_creation(self):
        """
        Test creating instances of Rectangle and checking attributes.
        """
        r1 = Rectangle(10, 5)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 5)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)

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


if __name__ == '__main__':
    unittest.main()
