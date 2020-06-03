#!/usr/bin/python3
"""Function that allows read a number of lines of file"""


def read_lines(filename="", nb_lines=0):
    """Function: read a number of lines of file"""
    line_file = 0
    for line in open(filename):
        line_file = line_file + 1
    with open(filename, encoding="UTF-8") as my_file:
        if nb_lines <= 0 or nb_lines >= line_file:
            print(my_file.read(), end="")
        else:
            for i, line in enumerate(my_file):
                if i != nb_lines:
                    print(line, end='')
                else:
                    break
    my_file.closed
