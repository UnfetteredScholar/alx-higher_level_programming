#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    index = -1
    count = 0

    while index + 1 < x:
        try:
            index += 1
            print("{:d}".format(my_list[index]), end="")
        except (TypeError, ValueError):
            continue
        else:
            count += 1
    print()
    return count
