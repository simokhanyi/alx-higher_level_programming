#!/usr/bin/python3
"""
Module
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

    def to_json(self):
        """
        Return a dictionary representation of the Student object.

        :return: A dictionary containing the attributes of the Student object.
        """
        return self.__dict__.copy()
