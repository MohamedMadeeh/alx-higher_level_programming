#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    t = []
    for x in matrix:
        t.append(list(map(lambda x: x**2, x)))
    return (t)
