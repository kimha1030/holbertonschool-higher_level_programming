#!/usr/bin/python3
"""Class size"""


class Square:
    """Class square that define un square with validation"""
    def __init__(self, size=0):
        """Class methods"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
