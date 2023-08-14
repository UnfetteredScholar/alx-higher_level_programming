#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix != [[]]:
        for row in matrix:
            for i, num in enumerate(row):
                print("{:d}".format(num), end='')
                if i < len(row) - 1:
                    print(" ", end='')
                else:
                    print("")
matrix = [
    [1],
    [4],
    [7]
]

print_matrix_integer()
