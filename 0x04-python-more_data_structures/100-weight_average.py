#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list is None or my_list == []:
        return 0
    product_sum = 0
    weight_sum = 0
    for pair in my_list:
        product_sum += (pair[0] * pair[1])
        weight_sum += pair[1]

    return (product_sum / weight_sum)
