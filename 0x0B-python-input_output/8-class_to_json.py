#!/usr/bin/python3
"""Defines the class_to_json function"""


def class_to_json(obj):
    """Creates a dictionary description from a json serialization
    of an object"""

    if hasattr(obj, "__dict__"):
        return obj.__dict__.copy()
    else:
        return {}
