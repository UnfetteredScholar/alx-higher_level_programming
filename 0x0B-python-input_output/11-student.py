#!/usr/bin/python3
"""Defines the Student class"""


class Student:
    """The Student class"""

    def __init__(self, first_name, last_name, age):
        """Student class constructor"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Converts the class to a dictionary

        Args:
            attrs List[str]: list of attributes to return in dict

        Returns:
            Dictionary representation of object with specified attributes
        """
        if hasattr(self, "__dict__"):
            jdict = self.__dict__.copy()
            if attrs is list:
                keys = []
                for key in jdict.keys():
                    keys.append(key)
                for key in keys:
                    if key not in attrs:
                        del jdict[key]
            return jdict
        else:
            return {}

    def reload_from_json(self, json):
        """Reloads a Student object from a json dictionary

        Args:
            json (dict): the json dictionary
        """
        self.first_name = json['first_name']
        self.last_name = json['last_name']
        self.age = json['age']
