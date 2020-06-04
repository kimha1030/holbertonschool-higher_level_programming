#!/usr/bin/python3
"""Function that adds a new string in text file"""


def append_after(filename="", search_string="", new_string=""):
    """Function: adds a new string in text file"""
    with open(filename, "a", encoding="UTF-8",) as my_file:
        if my_file.read() == search_string:
            my_file.write(new_string)
        return(my_file)
    my_file.closed
