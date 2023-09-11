#!/usr/bin/python3
"""Defines the is_kind_of_class function"""


def is_kind_of_class(obj, a_class):
    """Checks if ab object is an instance of a class or its derived
    classes

    Args:
        obj: the object
        a_class: the class

    Returns:
        True if obj is an instance of a_class or its derivative
    """
    return isinstance(obj, a_class)
