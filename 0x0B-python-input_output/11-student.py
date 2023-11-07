#!/usr/bin/python3
""" 
Student class with JSON methods
"""


class Student:
    """ Class definition for Student """

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
        Return a dictionary representation of the Student instance based on specified attributes.

        :param attrs: Optional list of attributes to include in the dictionary.
        :type attrs: list
        :return: A dictionary containing the specified attributes of the Student instance.
        :rtype: dict
        """
        if not isinstance(attrs, list) or \
           not all(isinstance(i, str) for i in attrs):
            dic = self.__dict__.copy()
        else:
            dic = {i: self.__dict__[i] for i in attrs if i in self.__dict__}
        return dic

    def reload_from_json(self, json):
        """
        Replace attributes of the Student instance with values from a dictionary.

        :param json: A dictionary with attribute-value pairs to update the Student instance.
        :type json: dict
        """
        for i in json:
            self.__dict__[i] = json[i]
