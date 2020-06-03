#!/usr/bin/python3
"""Function that compares if is instance"""


def inherits_from(obj, a_class):
    """Function compares obj and a_class"""
    if isinstance(obj, a_class) and type(obj) != a_class:
        return True
    else:
        return False
