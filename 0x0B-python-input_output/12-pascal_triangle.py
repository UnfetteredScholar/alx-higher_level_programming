#!/usr/bin/python3
"""Defines the pascal_triangle function"""


def pascal_triangle(n):
    """returns a list of lists of integers
    representing the Pascal’s triangle of n

    Args:
        n (int): the number of rows
    """
    rows = [[1]]

    if n <= 0:
        return []
    elif n == 1:
        return rows

    for i in range(1, n):
        row = [1]
        for j in range(1, len(rows[-1])):
            row.append(rows[-1][j] + rows[-1][j - 1])
        row.append(1)
        rows.append(row)

    return rows
