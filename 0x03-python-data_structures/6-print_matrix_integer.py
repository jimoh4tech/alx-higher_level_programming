#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for mat in matrix:
        ln = len(mat)
        for i in range(ln):
            print("{:d}".format(mat[i]), end=' ' if i != (ln - 1) else '')
        print()
