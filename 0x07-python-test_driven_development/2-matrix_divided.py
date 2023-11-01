#!/usr/bin/python3
"""Defines a function that divides all elements of a matrix.

Attributes:
    matrix_divided: divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix by a given number.

    Args:
        matrix (list): A list of lists of integers or floats.
        div (int/float): The number to divide all elements by.

    Raises:
        TypeError: If matrix is not a list of lists of integers or floats.
        TypeError: If each row of the matrix doesn't have the same size.
        TypeError: If an element of any list is not an integer or float.
        TypeError: If div is not an integer or a float.
        ZeroDivisionError: If div is equal to 0.

    Returns:
        list of lists: The new matrix with elements divided by div, rounded.
    """
    if not isinstance(div, (int, float)) or div == 0:
    raise (TypeError("div must be a number")
           if not isinstance(div, (int, float))
           else ZeroDivisionError("division by zero"))

    if not all(len(row) == len(matrix[0]) for row in matrix[1:]):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = [[round(val / div, 2) for val in row] for row in matrix]
    return new_matrix
