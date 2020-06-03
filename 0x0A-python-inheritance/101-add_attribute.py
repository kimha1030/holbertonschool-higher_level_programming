#!/usr/bin/python3
"""Function that compares if obj is instance of class"""


def add_attribute(self, name, value):
    """Function: compares values of a class"""
    try:
        self.name == value
    except:
        raise TypeError("can't add new attribute")
