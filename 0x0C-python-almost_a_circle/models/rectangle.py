#!/usr/bin/python3
"""Class Base"""
from models.base import Base


class Rectangle(Base):
    """Method check width, height, x and y of Class Rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Method constructor"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Return protected width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Modifiy width as value"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Return protected height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Modifiy height as value"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """Return protected width"""
        return self.__x

    @x.setter
    def x(self, value):
        """Modifiy x as value"""
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """Return protected height"""
        return self.__y

    @y.setter
    def y(self, value):
        """Modifiy y as value"""
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """Return area"""
        area = self.__width * self.__height
        return area

    def display(self):
        """method print the rectangle"""
        if self.__x is None and self.__y is None:
            for i in range(1, self.__height):
                characters = "#" * self.__width
                print(characters)
        else:
            for es_up in range(self.__y):
                print("")
            for he_r in range(self.__height):
                for es_dw in range(self.__y):
                    print(" ", end="")
                for wi_r in range(self.__width):
                    print("#", end="")
                print("")

    def __str__(self):
        """method print with __str__"""
        message_str = "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height)
        return message_str

    def update(self, *args, **kwargs):
        """Method update arguments"""
        if args and args is not None:
            list_arg = ["id", "width", "height", "x", "y"]
            for x in range(len(list_arg)):
                if x < len(args):
                    setattr(self, list_arg[x], args[x])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Method: convert to dictionary"""
        list_attr = ["id", "width", "height", "x", "y"]
        new_Dict = {}
        for x in range(len(list_attr)):
            new_Dict[list_attr[x]] = getattr(self, list_attr[x])
        return new_Dict
