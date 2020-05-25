#!/usr/bin/python3
"""Module to find the product o f two matrix
"""


def matrix_mul(m_a, m_b):
    """Function to find the product of two matrix
    """
    msg1 = "m_a should contain only integers or floats"
    msg2 = "m_b should contain only integers or floats"
    msg3 = "each row of m_a must be of the same size"
    msg4 = "each row of m_b must be of the same size"
    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")
    if len(m_a) == 0:
        raise ValueError("m_a can't be empty")
    if len(m_b) == 0:
        raise ValueError("m_b can't be empty")
    for row in m_a:
        if type(row) != list:
            raise TypeError("m_a must be a list of lists")
        if len(row) == 0:
            raise TypeError("m_a can't be empty")
        if len(row) != len(m_a[0]):
            raise TypeError(msg3)
        for c in row:
            if type(c) not in (float, int):
                raise TypeError(msg1)
    for row in m_b:
        if type(row) != list:
            raise TypeError("m_b must be a list of lists")
        if len(row) == 0:
            raise TypeError("m_b can't be empty")
        if len(row) != len(m_b[0]):
            raise TypeError(msg4)
        for c in row:
            if type(c) not in (float, int):
                raise TypeError(msg2)
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    matrix = []
    p_row = []
    product = 0
    for rowA in range(len(m_a)):
        for colB in range(len(m_b[0])):
            for rowB in range(len(m_b)):
                product = product + m_a[rowA][rowB] * m_b[rowB][colB]
            p_row.append(product)
            product = 0
        matrix.append(p_row)
        p_row = []
    return matrix
