#!/usr/bin/python3
"""Defines the save_to_json_file function"""
import json


def save_to_json_file(my_obj, filename):
    """Saves a json string to the specified file"""

    json.dump(my_obj, open(filename, 'w', encoding='utf-8'))
