#!/usr/bin/python3
"""Defines the load_from_json_file function"""
import json


def load_from_json_file(filename):
    """Creates an object from a json file"""

    with open(filename, 'r', encoding='utf-8') as f:
        json_string = f.read()
        return json.loads(json_string)
