#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    keys = []
    if a_dictionary is not None and a_dictionary != {}:
        for key in a_dictionary.keys():
            if a_dictionary[key] == value:
                keys.append(key)
        for key in keys:
            del a_dictionary[key]
    return a_dictionary
