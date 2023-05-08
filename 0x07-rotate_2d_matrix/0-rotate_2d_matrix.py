#!/usr/bin/python3
"""rotates a matrix"""
from copy import deepcopy


def rotate_2d_matrix(matrix):
    """rotates a 2d matrix by 90 degrees clockwise
    """
    size = len(matrix)
    inc = [i for i in range(size)]
    dec = [i for i in range(size - 1, -1, -1)]
    matrix_copy = deepcopy(matrix)

    for i in range(3):
        for j, k in zip(inc, dec):
            print([j, i], [i, k])
            matrix[i][k] = matrix_copy[j][i]

    print(matrix_copy)
