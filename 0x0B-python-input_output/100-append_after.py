#!/usr/bin/python3
"""Defines the append_after function"""


def append_after(filename="", search_string="", new_string=""):
    """Inserts a line of text after each line containing a
    specific string

    Args:
        search_string (str): the string to search for
        new_string (str): the string to insert
    """

    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    with open(filename, 'w', encoding='utf-8') as f:
        for line in lines:
            f.write(line)
            if line.find(search_string) != -1:
                f.write(new_string)
