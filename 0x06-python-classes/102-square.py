#!/usr/bin/python3

class Square:
    """
    This class represents a square and provides methods for comparing squares based on their areas.

    Attributes:
        size (float or int): The size (side length) of the square.

    Methods:
        area(): Calculate and return the area of the square.
    """

    def __init__(self, size=0):
        """
        Initializes a new Square instance with the given size.

        Args:
            size (float or int): The size (side length) of the square (default is 0).

        Raises:
            TypeError: If the size is not a number (float or int).
            ValueError: If the size is less than 0.

        Returns:
            None
        """
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter for the size attribute.

        Args:
            value (float or int): The new size to set for the square.

        Raises:
            TypeError: If the value is not a number (float or int).
            ValueError: If the value is less than 0.

        Returns:
            None
        """
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculate and return the area of the square.

        Args:
            None

        Returns:
            float or int: The area of the square.
        """
        return self.__size * self.__size

    def __eq__(self, other):
        """
        Compare two squares for equality based on their areas.

        Args:
            other (Square): The other square to compare to.

        Returns:
            bool: True if the areas of the two squares are equal, False otherwise.
        """
        return self.area() == other.area()

    def __ne__(self, other):
        """
        Compare two squares for inequality based on their areas.

        Args:
            other (Square): The other square to compare to.

        Returns:
            bool: True if the areas of the two squares are not equal, False otherwise.
        """
        return self.area() != other.area()

    def __lt__(self, other):
        """
        Compare two squares to determine if one has a smaller area than the other.

        Args:
            other (Square): The other square to compare to.

        Returns:
            bool: True if the area of the square is less than the area of the other square, False otherwise.
        """
        return self.area() < other.area()

    def __le__(self, other):
        """
        Compare two squares to determine if one has a smaller or equal area to the other.

        Args:
            other (Square): The other square to compare to.

        Returns:
            bool: True if the area of the square is less than or equal to the area of the other square, False otherwise.
        """
        return self.area() <= other.area()

    def __gt__(self, other):
        """
        Compare two squares to determine if one has a larger area than the other.

        Args:
            other (Square): The other square to compare to.

        Returns:
            bool: True if the area of the square is greater than the area of the other square, False otherwise.
        """
        return self.area() > other.area()

    def __ge__(self, other):
        """
        Compare two squares to determine if one has a larger or equal area to the other.

        Args:
            other (Square): The other square to compare to.

        Returns:
            bool: True if the area of the square is greater than or equal to the area of the other square, False otherwise.
        """
        return self.area() >= other.area()

if __name__ == "__main__":
    s_5 = Square(5)
    s_6 = Square(6)

    if s_5 < s_6:
        print("Square 5 < Square 6")
    if s_5 <= s_6:
        print("Square 5 <= Square 6")
    if s_5 == s_6:
        print("Square 5 == Square 6")
    if s_5 != s_6:
        print("Square 5 != Square 6")
    if s_5 > s_6:
        print("Square 5 > Square 6")
    if s_5 >= s_6:
        print("Square 5 >= Square 6")
