#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix is not None:
        for row in matrix:
            for i, num in enumerate(row):
                print("{:d}".format(num))
                if i < len(row) - 1:
                    print(" ")
