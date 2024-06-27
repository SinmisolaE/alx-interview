#!/usr/bin/python3

""" function that returns a list of lists of integers representing
     Pasccal's triangle of n
"""


def pascal_triangle(n):
    """ implementation of Pascal's triangle where n is
      an integer and must be greater than 0
    """

    triangle = []

    if (n <= 0):
        return []

    for col in range(n):
        row = [None for x in range(col + 1)]
        row[0] = 1
        row[-1] = 1

        for row_idx in range(1, col):
            row[row_idx] = (
                triangle[col - 1][row_idx - 1] +
                triangle[col - 1][row_idx]
            )

        triangle.append(row)

    return triangle
