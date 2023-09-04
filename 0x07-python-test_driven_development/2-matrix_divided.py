#!/usr/bin/python3
""" Defines the divie matrix function"""


def matrix_divided(matrix, div):
    """divides all elements of a matrix by an int

    Args:
    matrix (list): a 2D matrix of int or float
    div (float): number to divide the matrix by

    Returns:
    list of lists: 2D matrix with elements divides

    Raises:
    TypeError: if matrix is not list of lists of floats or integers.
    TypeError: If rows are not the same size
    TypeError: If div is not a number
    ZeroDivisionError: if div is 0
    """

    if type(div) is not int and type(div) is not float:
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')

    if type(matrix) is not list:
        raise TypeError(
                'matrix must be a matrix (list of lists) of integers/floats')
    if len(matrix) == 0:
        return []

    for row in matrix:
        if type(row) is not list:
            raise TypeError(
                    'matrix must be a matrix (list of lists) of \
integers/floats')
        if len(matrix[0]) != len(row):
            raise TypeError('Each row of the matrix must have the same size')
        for num in row:
            if (type(num) is int or type(num) is float) is not True:
                raise TypeError(
                        'matrix must be a matrix (list of lists) of \
integers/floats')

    res = []
    for row in matrix:
        r = []
        for num in row:
            r.append(round(num / div, 2))
        res.append(r)

    return res
