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

    @classmethod
    def square(cls, size=0):
        """Class method for return a new Rectangle instance"""
        return Rectangle(size, size)

    def bigger_or_equal(rect_1, rect_2):
        """Method that compares area two rectangles"""
        r1 = isinstance(rect_1, Rectangle)
        if r1 is False:
            raise TypeError("rect_1 must be an instance of Rectangle")
        r2 = isinstance(rect_2, Rectangle)
        if r2 is False:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() > rect_2.area():
            return rect_1
        elif rect_2.area() > rect_1.area():
            return rect_2
        else:
            return rect_1

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
        line = ""
        if self.__width == 0 or self.__height == 0:
            return line
        else:
            for row in range(self.__height):
                line = line + "\n"
                for col in range(self.__width):
                    line = line + str(self.print_symbol)
            rectangles = line[1:]
            return rectangles

    def __repr__(self):
        """method print with __repr__"""
        message_repr = "Rectangle({}, {})".format(self.__width, self.__height)
        return message_repr

    def __del__(self):
        """method for delete instances"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
