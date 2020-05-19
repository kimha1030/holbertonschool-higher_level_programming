#!/usr/bin/python3
"""Class size"""


class Square:
    """Class square that define un square and modify property"""
    def __init__(self, size=0):
        """Class methods"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Return area"""
        return self.__size * self.__size

    @property
    def size(self):
        """Return protected size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Modifiy size as value"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
