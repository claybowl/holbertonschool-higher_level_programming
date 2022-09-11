#!/usr/bin/python3
"""
function that divides all elements of a matrix

"""


def matrix_divided(matrix, div):
    """
    this function divides all elements of matrix
    """

    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) " +
                        "of integers/floats")

    if not isinstance(div, (float, int)):
        raise TypeError("div must be an number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    len_rows = []
    for row in matrix:
        len_rows.append(len(row))
    if not all(elem == len_rows[0] for elem in len_rows):
        raise TypeError("Each row of the matrix must have the same size")

    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")

    if type(matrix) is NoneType:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = [[round(x / div, 2) for x in row] for row in matrix]

    return new_matrix
