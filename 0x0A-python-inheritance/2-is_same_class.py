#!/usr/bin/python3
"""Function that shows if type obj is equal to class"""


def is_same_class(obj, a_class):
    """Function: compares obj and class"""
    if type(obj) is a_class:
        return True
    else:
        return False
