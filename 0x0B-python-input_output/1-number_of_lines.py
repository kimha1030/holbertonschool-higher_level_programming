#!/usr/bin/python3
"""Function that count the number of lines of file"""


def number_of_lines(filename=""):
    """Function: count number of lines of file"""
    nb_line = 0
    for line in open(filename):
        nb_line = nb_line + 1
    return (nb_line)
