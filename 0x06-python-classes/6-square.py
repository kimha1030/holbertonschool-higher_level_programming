#!/usr/bin/python3
"""Class square"""


class Square:
    """Class square that define un square and modify property"""
    def __init__(self, size=0, position=(0, 0)):
        """constructor"""
        self.size = size
        self.__position = position

    def area(self):
        """method return area of square"""
        return self.__size * self.__size

    def my_print(self):
        """method print"""
        if self.__size == 0:
            print(end="\n")
            return
        else:
            for x in range(self.__position[1]):
                print(sep="")
            for y in range(self.__size):
                for a in range(self.__position[0]):
                    print(" ", end="")
                for b in range(self.__size):
                    print("#", end="")
                print(sep="")

    @property
    def size(self):
        """method return self.size"""
        return self.__size

    @property
    def position(self):
        """method return self position"""
        return self.__position

    @size.setter
    def size(self, value):
        """setter size"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @position.setter
    def position(self, value):
        """setter position"""
        if type(value) != tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[0]) != int and type(value[1] != int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 and value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position
