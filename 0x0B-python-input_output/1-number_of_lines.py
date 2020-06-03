#!/usr/bin/python3
"""Function that count the number of lines of file"""


def number_of_lines(filename=""):
    """Function: count number of lines of file"""
    nb_line = 0
    with open(filename, "r") as my_file:
        for line in my_file:
            nb_line = nb_line + 1
    return (nb_line)
