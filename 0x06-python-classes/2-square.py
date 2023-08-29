#!/usr/bin/python3
"""Defines a Class Square"""


class Square:
    """Square class"""

    def __init__(self, size):
        """Initializes a Square object
            Args:
                size (int): the size of the square

            Raises:
                TypeError: If size is not an int
                ValueError: If size < 0
        """
        if type(size) is not int:
            raise TypeError('size must be an integer')
        else:
            if size < 0:
                raise ValueError('size must be >= 0')
            else:
                self.__size = size
