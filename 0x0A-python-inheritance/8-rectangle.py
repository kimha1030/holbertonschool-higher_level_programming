#!/usr/bin/python3
"""Class BaseGeometry"""


class BaseGeometry:
    """Method check value of name, age, distance"""
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """ Method check width and height of Class Rectangle """
    def __init__(self, width, height):
        BaseGeometry.__init__(self)
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
