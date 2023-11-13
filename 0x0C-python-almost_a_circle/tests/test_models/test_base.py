#!/usr/bin/python3
"""
Module that test base
"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """
    Test cases for the Base class in models/base.py.
    """

    def test_base_instance_creation(self):
        """
        Test creating instances of Base and checking unique ID are assigned.
        """
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)

    def test_base_instance_with_id(self):
        """
        Test creating instance with a specified id.
        """
        b = Base(100)
        self.assertEqual(b.id, 100)

    def test_to_json_string(self):
        """
        Test the to_json_string method for converting a list of dictionaries.
        """
        # Test with an empty list
        json_string = Base.to_json_string([])
        self.assertEqual(json_string, "[]")

        # Test with a list containing a dictionary
        json_string = Base.to_json_string([{'id': 1, 'name': 'test'}])
        self.assertEqual(json_string, '[{"id": 1, "name": "test"}]')

    def test_from_json_string(self):
        """
        Test the from_json_string method for converting a JSON string.
        """
        # Test with an empty string
        list_of_dicts = Base.from_json_string("")
        self.assertEqual(list_of_dicts, [])

        # Test with a JSON string containing a dictionary
        json_string = '[{"id": 1, "name": "test"}]'
        list_of_dicts = Base.from_json_string(json_string)
        self.assertEqual(list_of_dicts, [{'id': 1, 'name': 'test'}])

    def test_create_instance(self):
        """
        Test the create method for creating instance with all attributes set.
        """
        dummy_instance = Base.create(id=1)
        self.assertEqual(dummy_instance.id, 1)


if __name__ == '__main__':
    unittest.main()
