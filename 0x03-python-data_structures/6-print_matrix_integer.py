#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for mat in matrix:
        l = len(mat)
        for i in range(l):
            print("{:d}".format(mat[i]), end=' ' if i != (l - 1) else '')
        print()
