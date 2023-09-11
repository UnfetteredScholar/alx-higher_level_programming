#!/usr/bin/python3
"""Defines the Square class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class"""
    def __init__(self, size):
        """Square class constructor"""
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """Gets the area of a square"""
        return (self.__size**2)

    def __str__(self):
        """informal string representation of the rectangle"""
        return "[Square] {:d}/{:d}".format(self.__size, self.__size)
