#!/usr/bin/python3
"""
Module with Rectangle
"""
from models.base import Base


class Rectangle(Base):
    """
    This class represents a rectangle.

    Attributes:
        width (int): Width of the rectangle.
        height (int): Height of the rectangle.
        x (int): X-coordinate of the rectangle.
        y (int): Y-coordinate of the rectangle.
        id (int): Identifier of the rectangle.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes a Rectangle instance.

        Args:
            width (int): Width of the rectangle.
            height (int): Height of the rectangle.
            x (int, optional): X-coordinate of the rectangle (default is 0).
            y (int, optional): Y-coordinate of the rectangle (default is 0).
            id (int, optional): Identifier of the rectangle (default is None).
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @staticmethod
    def save_to_file_csv(list_objs):
        # Implement the method to save objects to CSV file
        pass

    @classmethod
    def load_from_file_csv(cls):
        # Implement the method to load objects from CSV file
        pass

    def area(self):
        """Calculate the area of the rectangle."""
        return self.width * self.height

    def display(self):
        """Display the rectangle with '#' characters."""
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """
        Returns a string representation of the Rectangle instance.

        Returns:
            str: String representation of the Rectangle.
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height
        )

    def update(self, *args, **kwargs):
        """Update the attributes of the Rectangle."""
        attr_names = ['id', 'width', 'height', 'x', 'y']
        if args:
            for i, arg in enumerate(args):
                setattr(self, attr_names[i], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
        Returns the dictionary representation of the Rectangle.

        Returns:
            dict: Dictionary containing id, width, height, x, and y.
        """
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }

    def to_csv(self):
        """Returns rectangle attributes as a list for CSV."""
        return [self.id, self.width, self.height, self.x, self.y]

    @classmethod
    def create_from_csv(cls, row):
        """Creates a Rectangle instance from CSV row data."""
        return cls(*map(int, row))
