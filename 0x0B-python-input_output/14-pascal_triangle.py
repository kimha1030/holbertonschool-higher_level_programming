#!/usr/bin/python3
"""Function that prints a Pascal Triangle"""


def pascal_triangle(n):
    """Function: Pascal Triangle"""
    triangle = [[1]]
    for r in range(1, n):
        val_r = [1]
        for c in range (1, r):
            val_r.append(triangle[r-1][c-1] + triangle[r-1][c])
        val_end = 1
        val_r.append(val_end)
        triangle.append(val_r)
    return(triangle)