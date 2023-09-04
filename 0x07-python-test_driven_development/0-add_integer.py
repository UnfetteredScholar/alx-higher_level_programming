#!/usr/bin/python3
"""Defines the add_integer function"""


def add_integer(a, b=98):
    """Adds two integers

    Args:
        a (int): the first integer
        b (int): the second integer

    Returns:
        int: the sum of the two integers

    Raises:
        TypeError: if a or b are not int or float
    """

    if (type(a) is int or type(a) is float) is not True:
        raise TypeError("a must be an integer")
    if (type(b) is int or type(b) is float) is not True:
        raise TypeError("b must be an integer")

    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)

    return a + b
