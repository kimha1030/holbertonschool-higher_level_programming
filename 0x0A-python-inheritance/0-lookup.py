#!/usr/bin/python3
"""Function that print the attributes of object"""


def lookup(obj):
    """Function that return the available attributes"""
    list_o = []
    list_o = getattr(obj)
    return list_o
