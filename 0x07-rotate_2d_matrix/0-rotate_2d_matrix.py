#!/usr/bin/python3
"""rotates a matrix"""


def rotate_2d_matrix(matrix = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]):
    """rotates a 2d matrix by 90 degrees clockwise
    """
    size = len(matrix)
    inc = [i for i in range(size)]
    dec = [i for i in range(size - 1, -1, -1)]
    matrix_copy = []
    for i in matrix:
        temp = []
        for j in i:
            temp.append(j)
        matrix_copy.append(temp)


    for i in range(size):
        for j, k in zip(inc, dec):
            matrix[i][k] = matrix_copy[j][i]

rotate_2d_matrix()