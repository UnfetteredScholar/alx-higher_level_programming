#!/usr/bin/python3
"""Defines is_same_class function"""


def is_same_class(obj, a_class):
    """Checks if an object is an instance of a class

    Args:
        obj: the object to be checked
        a_class: the class to be checked against

    Returns:
        True if obj is an instance of a_class
    """
    return (type(obj) is a_class)
