#!/usr/bin/python3
"""
function that divides all elements of a matrix

"""


def matrix_divided(matrix, div):
    """
    this function divides all elements of matrix
    """

    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) \
                        of integers/floats")

    div_type = type(div)
    if div_type is not int and div_type is not float:
        raise TypeError("div must be a number")

    len_rows = []
    for row in matrix:
        len_rows.append(len(row))
    if not all(elem == len_rows[0] for elem in len_rows):
        raise TypeError("Each row of the matrix must have the same size")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    for row in matrix:
        new_matrix.append([round(val/div, 2) for val in row])

    return new_matrix
