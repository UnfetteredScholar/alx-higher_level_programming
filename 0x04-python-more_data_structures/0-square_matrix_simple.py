#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    res = []
    if matrix is not None and matrix != []:
        for row in matrix:
            res.append(list(map(lambda x: x**2, row)))
    return res
