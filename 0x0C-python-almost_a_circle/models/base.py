#!/usr/bin/python3
"""
Module with base
"""
import json
import csv
import turtle


class Base:
    """
    Base class for managing id attribute in future classes.

    Attributes:
    - __nb_objects (int): Private class attribute to keep track of objects.
    - id (int): Public instance attribute representing the unique identifier.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Constructor for Base class.

        Args:
        - id (int, optional): Assigns public instance attribute id with value.
          Otherwise, increments __nb_objects and assigns the new value to id.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def draw(list_rectangles, list_squares):
        """
        Draws all the Rectangles and Squares using Turtle graphics.

        Args:
        - list_rectangles (list): List of Rectangle instances.
        - list_squares (list): List of Square instances.

        Returns:
        - None
        """
        turtle.clear()
        turtle.speed(2)
        turtle.hideturtle()

        for rect in list_rectangles:
            turtle.penup()
            turtle.goto(rect.x, rect.y)
            turtle.pendown()
            turtle.forward(rect.width)
            turtle.right(90)
            turtle.forward(rect.height)
            turtle.right(90)
            turtle.forward(rect.width)
            turtle.right(90)
            turtle.forward(rect.height)
            turtle.right(90)

        for square in list_squares:
            turtle.penup()
            turtle.goto(square.x, square.y)
            turtle.pendown()
            turtle.forward(square.size)
            turtle.right(90)
            turtle.forward(square.size)
            turtle.right(90)
            turtle.forward(square.size)
            turtle.right(90)
            turtle.forward(square.size)
            turtle.right(90)

        turtle.exitonclick()

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns the JSON string representation of list_dictionaries.

        Args:
        - list_dictionaries (list): List of dictionaries to be represented.

        Returns:
        - str: JSON string representation of list_dictionaries.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes the JSON string representation of list_objs to a file.

        Args:
        - list_objs (list): List of instances inheriting from Base.

        Returns:
        - None
        """
        filename = f"{cls.__name__}.json"
        self.id = id if id is not None else Base.__nb_objects + 1
        with open(filename, "w") as file:
            file.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """
        Returns the list of the JSON string representation json_string.

        Args:
        - json_string (str): String representing a list of dictionaries.

        Returns:
        - list: List represented by json_string.
        """
        if json_string is None or json_string == '':
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Returns an instance with all attributes already set.

        Args:
        - **dictionary: Double pointer to a dictionary.

        Returns:
        - cls: Instance with all attributes set.
        """
        if cls.__name__ == "Rectangle":
            dummy_instance = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy_instance = cls(1)
        else:
            return None

        dummy_instance.update(**dictionary)
        return dummy_instance

    @classmethod
    def create(cls, **dictionary):
        """
        Returns an instance with all attributes already set.

        Args:
        - **dictionary: Double pointer to a dictionary.

        Returns:
        - cls: Instance with all attributes set.
        """
        if cls.__name__ == "Rectangle":
            dummy_instance = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy_instance = cls(1)
        else:
            return None

        dummy_instance.update(**dictionary)
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """
        Returns a list of instances.

        If the file doesn’t exist, return an empty list.
        Otherwise, return a list of instances.

        Returns:
        - list: List of instances.
        """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as file:
                json_string = file.read()
                list_of_dicts = cls.from_json_string(json_string)
                return [cls.create(**d) for d in list_of_dicts]
        except FileNotFoundError:
            return []

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns the JSON string representation of list_dictionaries.

        Args:
        - list_dictionaries (list): List of dictionaries to be represented.

        Returns:
        - str: JSON string representation of list_dictionaries.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Serializes a list of objects to a CSV file.

        Args:
        - list_objs (list): List of instances inheriting from Base.

        Returns:
        - None
        """
        filename = f"{cls.__name__}.csv"
        with open(filename, "w", newline='') as file:
            writer = csv.writer(file)
            for obj in list_objs:
                writer.writerow(obj.to_csv())

    @classmethod
    def load_from_file_csv(cls):
        """
        Deserializes a list of objects from a CSV file.

        Returns:
        - list: List of instances.
        """
        filename = f"{cls.__name__}.csv"
        try:
            with open(filename, "r", newline='') as file:
                reader = csv.reader(file)
                return [cls.create_from_csv(row) for row in reader]
        except FileNotFoundError:
            return []

    def to_csv(self):
        """
        Returns a list with the object attributes in CSV format.

        Returns:
        - list: List with object attributes in CSV format.
        """
        raise NotImplementedError("to_csv must be implemented in subclasses")

    @classmethod
    def create_from_csv(cls, row):
        """
        Creates an instance from a CSV row.

        Args:
        - row (list): List with object attributes in CSV format.

        Returns:
        - cls: Instance created from CSV row.
        """
        raise NotImplementedError("create_from_csv must be implemented")
