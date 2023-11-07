#!/usr/bin/python3
"""
Pascals_triangle
"""


def pascal_triangle(n):
    """
    Generate Pascal's triangle up to n rows.

    :param n: The number of rows to generate in Pascal's triangle.
    :type n: int
    :return: A list of lists representing Pascal's triangle.
    :rtype: list
    """
    if n <= 0:
        return []

    triangle = [[1]]
    while len(triangle) < n:
        row = [1]
        prev_row = triangle[-1]
        for i in range(1, len(prev_row)):
            row.append(prev_row[i - 1] + prev_row[i])
        row.append(1)
        triangle.append(row)

    return triangle
