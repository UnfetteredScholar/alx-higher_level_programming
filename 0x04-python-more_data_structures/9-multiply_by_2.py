#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    res = {}

    for key in a_dictionary.keys():
        res[key] = 2 * a_dictionary[key]
    return res
