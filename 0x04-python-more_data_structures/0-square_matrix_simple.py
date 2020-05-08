#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new = []
    for r in range(len(matrix)):
        sub = []
        for c in range(len(matrix[0])):
            x = (matrix[r][c]) * (matrix[r][c])
            sub.append(x)
        new.append(sub)
    return new
