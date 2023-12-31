#!/usr/bin/python3
"""
Module that tests Base
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """
    Test cases for the Base class in base.py.
    """

    def test_base_creation(self):
        """
        Test the creation of a Base instance and the initialization.
        """
        dummy_instance = Base()
        self.assertEqual(dummy_instance.id, 1)

    def test_base_instance_with_id(self):
        """
        Test creating an instance with a specified ID.
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
        Test the create method for creating instances with all set.
        """
        dummy_instance = Base.create()
        self.assertEqual(dummy_instance.id, 1, "Default ID should be 1")

        # Additional test for create method with specified attributes
        attributes = {'id': 5}
        instance = Base.create(**attributes)
        self.assertEqual(instance.id, 5, "ID should be set to 5")


if __name__ == '__main__':
    unittest.main()
