#!/usr/bin/python3
"""Defines the append write function"""


def append_write(filename="", text=""):
    """Appends a string to a file"""

    with open(filename, 'a', encoding='utf-8') as f:
        chars = f.write(text)
    return chars
