#!/usr/bin/python3
"""Function that compares if obj is instance of class"""


def is_kind_of_class(obj, a_class):
    """Function: compares obj and class"""
    if isinstance(obj, a_class):
        return True
    else:
        return False
