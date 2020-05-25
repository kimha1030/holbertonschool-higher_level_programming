#!/usr/bin/python3
"""Class Rectangle"""


class Rectangle:
    """Class rectangle that define a rectangle"""
    def __init__(self, width=0, height=0):
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.width = width
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.height = height

    def area(self):
        """Return area"""
        area = self.__width * self.__height
        return area

    def perimeter(self):
        """Return perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (2 * self.__width + 2 * self.__height)

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
        self.__width = value

    @height.setter
    def height(self, value):
        """Modifiy height as value"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def __str__(self):
        """method print with __str__"""
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            for i in range(self.__height):
                characters = "#" * self.__width
                print(characters)
        return characters
