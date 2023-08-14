#!/usr/bin/python3
def no_c(my_string):
    res = ""
    if my_string is not None:
        for char in my_string:
            if char != 'c' and char != 'C':
               res = res + char
    return res
