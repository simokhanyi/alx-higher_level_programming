#!/usr/bin/python3
"""
function that multiplies 2 matrices
"""


def matrix_mul(m_a, m_b):
    """
    Multiplies two matrices.

    Args:
        m_a (list of lists): The first matrix to be multiplied.
        m_b (list of lists): The second matrix to be multiplied.

    Returns:
        list of lists: The resulting matrix after multiplication.

    Raises:
        TypeError: If m_a or m_b is not a list, not a list of lists, or
        contains elements other than integers or floats.
        ValueError: If m_a or m_b is empty or if the matrices cannot be
        multiplied due to dimension mismatch.

    The function takes two matrices m_a and m_b as input and validates them
    according to the specified requirements. It then performs matrix
    multiplication if the matrices are valid and returns the result as a new
    matrix.
    """

    # Validate input matrix m_a
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not m_a or any(
            not all(isinstance(val, (int, float)) for val in row)
            for row in m_a):
        raise ValueError("m_a can't be empty and should contain only numbers")
    if any(len(row) != len(m_a[0]) for row in m_a[1:]):
        raise TypeError("Each row of m_a must be of the same size")

    # Validate input matrix m_b
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")
    if not m_b or any(
            not all(isinstance(val, (int, float)) for val in row)
            for row in m_b):
        raise ValueError("m_b can't be empty and should contain only numbers")
    if any(len(row) != len(m_b[0]) for row in m_b[1:]):
        raise TypeError("Each row of m_b must be of the same size")

    # Check if matrices can be multiplied
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    # Perform matrix multiplication
    result = []
    for i in range(len(m_a)):
        row = []
        for j in range(len(m_b[0])):
            total = sum(m_a[i][k] * m_b[k][j] for k in range(len(m_a[0])))
            row.append(total)
        result.append(row)

    return result
