#!/usr/bin/python3
"""Defines the find_peak function"""


def find_peak(list_of_integers):
    """
    Finds a peak in a list of unsorted integers

    Args:
        list_of_integers (List[int]): List of integers
        to search

    Returns:
        The peak found or None if list is empty
    """

    n = len(list_of_integers)
    if n == 0:
        return None
    left = 0
    right = n - 1

    while left != right:
        mid = int(left + (right - left) / 2)

        if (mid == 0 or
            list_of_integers[mid - 1] <=
            list_of_integers[mid]) and\
            (mid == n - 1 or
           list_of_integers[mid + 1] <=
           list_of_integers[mid]):
            return list_of_integers[mid]
        elif (list_of_integers[mid - 1] >
                list_of_integers[mid] >
                list_of_integers[mid + 1]):
            right = mid - 1
        else:
            left = mid + 1

    return list_of_integers[left]
