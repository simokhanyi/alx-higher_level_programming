#!/usr/bin/python3
"""
Module with Square
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    This class defines a square based on size and inherits from Rectangle.

    Attributes:
        size (int): Size of the square.
        x (int): X-coordinate of the square.
        y (int): Y-coordinate of the square.
        id (int): Identifier of the square.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes a Square instance.

        Args:
            size (int): Size of the square.
            x (int, optional): X-coordinate of the square (default is 0).
            y (int, optional): Y-coordinate of the square (default is 0).
            id (int, optional): Identifier of the square (default is None).
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter method for size."""
        return self.width

    @size.setter
    def size(self, value):
        """Setter method for size."""
        self.width = value
        self.height = value

    def __str__(self):
        """
        Returns a string representation of the Square instance.

        Returns:
            str: String representation of the Square.
        """
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width
        )

    def to_dictionary(self):
        """
        Returns the dictionary representation of the Square.

        Returns:
            dict: Dictionary containing id, size, x, and y.
        """
        return {
            'id': self.id,
            'size': self.width,
            'x': self.x,
            'y': self.y
        }

    def to_csv(self):
        return [self.id, self.size, self.x, self.y]

    @classmethod
    def create_from_csv(cls, row):
        return cls(*map(int, row))
