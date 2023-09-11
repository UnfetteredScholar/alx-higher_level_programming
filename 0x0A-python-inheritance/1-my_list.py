#!/usr/bin/python3
"""Defines the MyList class"""

class MyList(list):
    """Custom list class definition"""

    def print_sorted(self):
        """Prints a sorted version of the list"""
        print(sorted(self))
