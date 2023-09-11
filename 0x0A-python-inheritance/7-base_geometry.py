#!/usr/bin/python3
"""Defines the BaseGeomety class"""


class BaseGeometry:
    """The BaseGeometry class definition"""

    def area(self):
        """Raises exception not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates if the variable value is an integer
        and is greater than 0"""

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
