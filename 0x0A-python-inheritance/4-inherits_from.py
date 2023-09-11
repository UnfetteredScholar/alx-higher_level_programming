#!/usr/bin/python3
"""Defines the inherits_from python"""


def inherits_from(obj, a_class):
    """Checks if an object inherits from a class

    Args:
        obj: the object
        a_class: the class

    Returns:
        True if the object inherits form the class else False
    """
    return issubclass(obj, a_class)
