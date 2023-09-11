#!/usr/bin/python3
"""Defines the lookup function"""


def lookup(obj):
    """Gets the list of available attributes and methods for an
    object.

    Args:
        obj: an object instance

    Returns:
        A list of available methods and attributes
    """
    return dir(obj)
