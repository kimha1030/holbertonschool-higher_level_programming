#!/usr/bin/python3
"""Module to divides a matrix by div
"""


def matrix_divided(matrix, div):
    """ Function that allows divides the matrix by div
    """
    msg1 = "matrix must be a matrix (list of lists) of integers/floats"
    msg2 = "Each row of the matrix must have the same size"
    if matrix == None and div == None:
        raise TypeError(msg1)
    else:
        if type(div) not in (float, int):
            raise TypeError("div must be a number")
        if div == 0:
            raise ZeroDivisionError("division by zero")
        if type(matrix) is not list:
            raise TypeError(msg1)
        x = []
        for row in matrix:
            if type(row) != list:
                raise TypeError(msg1)
            if len(row) == 0:
                raise TypeError(msg1)
            if len(row) != len(matrix[0]):
                raise TypeError(msg2)
            for c in row:
                if type(c) not in (float, int):
                    raise TypeError(msg1)
        x = [[round(c/div, 2) for c in row] for row in matrix]
        return (x)