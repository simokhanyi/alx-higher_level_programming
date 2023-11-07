#!/usr/bin/python3
"""
Student class definition
"""

class Student:

    def __init__(self, first_name, last_name, age):
        """
        Initialize a Student object.

        :param first_name: The first name of the student.
        :param last_name: The last name of the student.
        :param age: The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Return a dictionary representation of the Student instance.

        :param attrs: Optional list of attributes to include in dictionary.
        :type attrs: list
        :return: A dictionary containing the specified attributes of thStudent.
        :rtype: dict
        """
        if (isinstance(attrs, list) and
                all(isinstance(x, str) for x in attrs)):
            return {x: getattr(self, x) for x in attrs if hasattr(self, x)}
        return self.__dict__
