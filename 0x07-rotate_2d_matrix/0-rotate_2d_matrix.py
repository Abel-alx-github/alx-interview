#!/usr/bin/python3


""" function that rotate 2-d matrix in-place"""


def rotate_2d_matrix(matrix):
    """
    Rotates a 2D matrix 90 degrees clockwise in-place.
    Args:
        matrix: An n x n 2D matrix.
    """
    len_row = len(matrix)

    for i in range(len_row):
        for j in range(i, len_row):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse each row of the transposed matrix
    for row in matrix:
        row.reverse()
