#!/usr/bin/python3
"""Defines a Class Square"""


class Square:
    """Square class

    Attributes:
        __size (int): the size of the square
        __position (tuple): tuple representing the position of the square
    """

    def __init__(self, size=0, position=(0, 0)):
        """Initializes a Square object
            Args:
                size (int): the size of the square
                position (tuple): the position of the square

            Raises:
                TypeError: If size is not an int or position
                is not tuple of two positive integers
                ValueError: If size < 0
        """
        if type(size) is not int:
            raise TypeError('size must be an integer')
        else:
            if size < 0:
                raise ValueError('size must be >= 0')
            else:
                self.__size = size

        if (type(position) is not tuple or len(position) != 2 or
            type(position[0]) is not int or type(position[1]) is not int or
                position[0] < 0 or position[1] < 0):
            raise TypeError('position must be a tuple of 2 positive integers')
        else:
            self.__position = position

    def area(self):
        """Gets the area of the square

        Returns:
            The area of the square
        """

        return self.__size**2

    @property
    def size(self):
        """Gets or Sets the size of the Square object

        Raises:
            TypeError: if size is not an int
            ValueError: if size < 0
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

    @property
    def position(self):
        """Gets or Sets the position of the Square object

        Raises:
            TypeError: if position is not a tupe of 2 positive integers
        """

        return self.__position

    @position.setter
    def position(self, position):
        if (type(position) is not tuple or len(position) != 2 or
            type(position[0]) is not int or type(position[1]) is not int or
                position[0] < 0 or position[1] < 0):
            raise TypeError('position must be a tuple of 2 positive integers')
        else:
            self.__position = position

    def my_print(self):
        """Prints the square using #
            Position is indicated using spaces
        """

        if self.__size == 0:
            print()
            return
        for y in range(self.__position[1]):
            print()
        for i in range(self.__size):
            line = ' ' * self.__position[0] + '#'*self.__size
            print(line)
