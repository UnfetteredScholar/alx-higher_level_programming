#!/usr/bin/python3
"""Defines the from_json_string function"""
import json


def from_json_string(my_str):
    """Converts a json string to an object"""

    return json.loads(my_str)
