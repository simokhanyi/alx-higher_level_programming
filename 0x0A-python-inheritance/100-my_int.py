class MyInt(int):
    """
    A class that represents an integer with inverted == and != operators.
    """

    def __eq__(self, other):
        """
        Check if the integer is not equal to another integer.

        Args:
            other (int): The integer to compare with.

        Returns:
            bool: True if not equal, False if equal.
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Check if the integer is equal to another integer.

        Args:
            other (int): The integer to compare with.

        Returns:
            bool: True if equal, False if not equal.
        """
        return super().__eq__(other)

# Test the code


if __name__ == '__main__':
    my_i = MyInt(3)
    print(my_i)
    print(my_i == 3)
    print(my_i != 3)
