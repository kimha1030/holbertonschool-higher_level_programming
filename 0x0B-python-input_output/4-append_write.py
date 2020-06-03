#!/usr/bin/python3
"""Function that allows read a number of lines of file"""


def append_write(filename="", text=""):
    """Function: read a number of lines of file"""
    with open(filename, "a", encoding="UTF-8",) as my_file:
        return(my_file.write(text))
    my_file.closed
