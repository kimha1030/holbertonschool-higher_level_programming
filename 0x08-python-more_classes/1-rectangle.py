#!/usr/bin/python3
"""Class Rectangle"""


class Rectangle:
    """Class rectangle that define a rectangle"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """Return protected width"""
        return self.__width

    @property
    def height(self):
        """Return protected height"""
        return self.__height

    @width.setter
    def width(self, value):
        """Modifiy width as value"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @height.setter
    def height(self, value):
        """Modifiy height as value"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
