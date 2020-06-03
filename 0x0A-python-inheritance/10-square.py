#!/usr/bin/python3
"""Class BaseGeometry"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Method check size of square """

    def __init__(self, size):
        """Constructor Method"""
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
