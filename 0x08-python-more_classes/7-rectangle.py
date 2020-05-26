#!/usr/bin/python3
"""Class Rectangle"""


class Rectangle:
    """Class rectangle that define a rectangle"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Method constructor"""
        Rectangle.number_of_instances += 1
        self.width = width
        self.height = height

    def area(self):
        """Return area"""
        Rectangle.number_of_instances += 1
        area = self.__width * self.__height
        return area

    def perimeter(self):
        """Return perimeter"""
        Rectangle.number_of_instances += 1
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
        res = ""
        if self.__width == 0 or self.__height == 0:
            return res
        else:
            for row in range(1, self.__height):
                res = res + "\n"
                for col in range(1, self.__width):
                    res = res + Rectangle.print_symbol
            return res

    def __repr__(self):
        """method print with __repr__"""
        message_repr = "Rectangle({}, {})".format(self.__width, self.__height)
        return message_repr

    def __del__(self):
        """method for delete instances"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
