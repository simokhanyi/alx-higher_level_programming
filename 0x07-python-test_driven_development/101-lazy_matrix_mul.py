#!/usr/bin/python3
"""Defines a function that multiplies 2 matrices by using the module NumPy.

Attributes:
    m_a (matrix)
    m_b (matrix)
"""


import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies two matrices using NumPy.

    Args:
        m_a (list of lists): The first matrix to be multiplied.
        m_b (list of lists): The second matrix to be multiplied.

    Returns:
        numpy.ndarray: The resulting matrix after multiplication.

    Raises:
        ValueError: If m_a or m_b is empty or if the matrices cannot be
        multiplied due to dimension mismatch.
    """

    # Convert input matrices to NumPy arrays
    a = np.array(m_a)
    b = np.array(m_b)

    # Check if matrices can be multiplied
    if a.shape[1] != b.shape[0]:
        raise ValueError("m_a and m_b can't be multiplied")

    # Perform matrix multiplication using NumPy
    result = np.dot(a, b)

    return result
