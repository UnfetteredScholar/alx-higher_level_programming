#!/usr/bin/python3
"""Defines the say_my_name function"""


def say_my_name(first_name, last_name=""):
    """Prints the names passed to the function in stdout

    Args:
        first_name (str): the first name
        last_name (str): the last name

    Raises:
        TypeError: If either arg is not a str
    """

    if type(first_name) is not str:
        raise TypeError('first_name must be a string')
    if type(last_name) is not str:
        raise TypeError('last_name must be a string')
    print("My name is {} {}".format(first_name, last_name))
