#!/usr/bin/python3
"""Class square"""


class Square:
    """Class square that define un square and modify property"""
    def __init__(self, size=0, position=(0, 0)):
        """constructor"""
        self.size = size
        self.position = position

    def area(self):
        """method return area of square"""
        return self.__size * self.__size

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
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @position.setter
    def position(self, value):
        """setter position"""
        if type(value) != tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value[0]) != int or type(value[1]) != int:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def my_print(self):
        """method print"""
        if self.__size == 0:
            print("\n")
            return
        else:
            for p in range(self.__position[1]):
                print("")
            for x in range(self.__size):
                for y in range(self.__position[0]):
                    print(" ", end="")
                for z in range(self.__size):
                    print("#", end="")
                print("")
