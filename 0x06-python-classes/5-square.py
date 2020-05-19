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
        """return area"""
        return self.__size * self.__size

    def my_print(self):
        """print square"""
        if self.__size == 0:
            print(end="\n")
        else:
            for i in range(self.__size):
                for i in range(self.__size):
                    print("#", end="")
                print(end="\n")

    @property
    def size(self):
        """return size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Conditions value"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
