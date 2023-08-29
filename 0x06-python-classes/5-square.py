#!/usr/bin/python3
"""Defines a Class Square"""


class Square:
    """Square class

    Attributes:
        __size (int): the size of the square
    """

    def __init__(self, size=0):
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

    def area(self):
        """Gets the area of the square

        Returns:
            The area of the square
        """

        return self.__size**2

    @property
    def size(self):
        """Gets or Sets the size of the Square object
        """

        return self.__size

    @size.setter
    def size(self, size):
        if type(size) is not int:
            raise TypeError('size must be an integer')
        else:
            if size < 0:
                raise ValueError('size must be >= 0')
            else:
                self.__size = size

    def my_print(self):
        """Prints the square using #
        """

        if self.__size == 0:
            print()
            return
        for i in range(self.__size):
            print('#'*self.__size)
