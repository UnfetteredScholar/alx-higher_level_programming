#!/usr/bin/python3
"""Defines the write_file function"""


def write_file(filename="", text=""):
    """Writes a stirng to a file"""

    with open(filename, 'w', encoding='utf-8') as f:
        chars = f.write(text)

    return chars
