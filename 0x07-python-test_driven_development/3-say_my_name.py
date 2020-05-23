#!/usr/bin/python3
"""Module to print a full name
"""


def say_my_name(first_name, last_name=""):
    """Function that allows print full name
    """
    if type(first_name) != str:
        raise TypeError("first_name must be a string")
    if type(last_name) != str:
        raise TypeError("last_name must be a string")
    print("my name is {:s} {:s}".format(first_name, last_name, end=""))
