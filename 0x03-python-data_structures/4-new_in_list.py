#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    cpy = None
    if my_list is not None:
        cpy = [x for x in my_list]
        if 0 <= idx < len(my_list):
            cpy[idx] = element
    return cpy
