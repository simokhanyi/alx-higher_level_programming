#!/usr/bin/python3
"""
Module that test square
"""
import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """
    Test cases for the Square class in models/square.py.
    """

    def test_square_instance_creation(self):
        """
        Test the creation of a Square instance and the initialization.
        """
        s1 = Square(5)
        self.assertEqual(s1.id, 2)

    def test_square_instance_creation(self):
        """
        Test creating instances of Square and checking attributes.
        """
        s1 = Square(5)
        self.assertEqual(s1.id, 1)
        self.assertEqual(s1.size, 5)
        self.assertEqual(s1.x, 0)
        self.assertEqual(s1.y, 0)

    def test_square_instance_with_attributes(self):
        """
        Test creating instance with specified attributes.
        """
        s = Square(3, 2, 1, 50)
        self.assertEqual(s.id, 50)
        self.assertEqual(s.size, 3)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 1)

    def test_square_area(self):
        """
        Test the area method of the Square class.
        """
        s = Square(4)
        self.assertEqual(s.area(), 16)

    def test_square_str_representation(self):
        """
        Test the __str__ method for the string representation of Square.
        """
        s = Square(2, 1, 3, 99)
        self.assertEqual(str(s), "[Square] (99) 1/3 - 2")

    def test_square_update_method(self):
        """
        Test the update method for updating attributes of Square.
        """
        s = Square(4, 2, 3, 10)
        s.update(89)
        self.assertTrue(str(s) == "[Square] (89) 2/3 - 4")
        s.update(89, 2)
        self.assertTrue(str(s) == "[Square] (89) 2/3 - 2")
        s.update(89, 2, 3)
        self.assertTrue(str(s) == "[Square] (89) 2/3 - 2")
        s.update(89, 2, 3, 4)
        self.assertTrue(str(s) == "[Square] (89) 4/3 - 2")


if __name__ == '__main__':
    unittest.main()
