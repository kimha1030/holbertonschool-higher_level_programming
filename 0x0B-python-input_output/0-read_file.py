#!/usr/bin/python3
"""Function that allows read a file"""


def read_file(filename=""):
    """Function: read a file"""
    with open(filename, encoding="UTF-8") as my_file:
        read_text = my_file.read()
        print(read_text)
    my_file.closed
