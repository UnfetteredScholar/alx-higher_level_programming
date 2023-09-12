#!/usr/bin/python3
"""Defines the Student class"""


class Student:
    """The Student class"""

    def __init__(self, first_name, last_name, age):
        """Student class constructor"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Converts the class to a dictionary"""
        if hasattr(self, "__dict__"):
            return self.__dict__.copy()
        else:
            return {}
