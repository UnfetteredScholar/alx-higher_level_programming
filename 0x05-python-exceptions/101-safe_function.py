#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    res = None
    try:
        res = fct(*args)
    except Exception as ex:
        print("Error: {}".format(ex), file=sys.stderr)
    return res
