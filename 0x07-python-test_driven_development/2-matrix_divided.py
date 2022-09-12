#!/usr/bin/python3
""" divide a matrix by div"""


def matrix_divided(matrix, div):
    """ much error checking, then maths"""

    for row in matrix:
        for val in row:
            val_type = type(val)
            if val_type is not int and val_type is not float:
                raise TypeError("matrix must be a matrix (list of lists) \
of integers/floats")

    matrix_row_size = len(matrix[0])
    for row in matrix:
        if len(row) != matrix_row_size:
            raise TypeError("Each row of the matrix must have the same size")

    div_type = type(div)
    if div_type is not int and div_type is not float:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    for row in matrix:
        new_matrix.append([round(val/div, 2) for val in row])
    return new_matrix
