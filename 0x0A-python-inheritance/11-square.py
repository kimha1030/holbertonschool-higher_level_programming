#!/usr/bin/python3
"""Class BaseGeometry"""
Rectangle = __import__('10-square').Rectangle


class Square(Rectangle):
    """ Method check size of square """
    def __init__(self, size):
        """Method constructor"""
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Return area"""
        area = self.__size * self.__size
        return area

    def __str__(self):
        """Method print with __str__"""
        msge = "[Square] {:d}/{:d}".format(self.__size, self.__size)
        return (msge)
