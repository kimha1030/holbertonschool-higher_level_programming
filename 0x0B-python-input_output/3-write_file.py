#!/usr/bin/python3
"""Function that allows read a number of lines of file"""


def write_file(filename="", text=""):
    """Function: read a number of lines of file"""
    with open(filename, "w", encoding="UTF-8",) as my_file:
        return(my_file.write(text))
    my_file.closed
