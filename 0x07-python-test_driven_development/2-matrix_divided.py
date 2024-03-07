#!/usr/bin/python3
""" A Module that divides a matrix """


def matrix_divided(matrix, div):
    """ A Function that divides each elements of a matrix """
    if (not isinstance(matrix, list) or
        not all(isinstance(row, list) for row in matrix) or
        not all(all(isinstance(elem, (int, float)) for elem in row)
                for row in matrix)):
        raise TypeError(
             "matrix must be a matrix (list of lists) of integers/floats")

    if any(len(row) != len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = [[round(elem / div, 2) for elem in row]for row in matrix]
    return new_matrix
