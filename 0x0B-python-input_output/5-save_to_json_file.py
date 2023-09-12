#!/usr/bin/python3
"""Defines the save_to_json_file function"""
import json


def save_to_json_file(my_obj, filename):
    """Saves a json string to the specified file"""

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(json.dumps(my_obj))
