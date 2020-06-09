#!/usr/bin/python3
"""Class Base"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Method check width, height, x and y of Class Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """Method constructor"""
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """Method print with __str__"""
        message_str = "(Square) ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.size)
        return message_str

    @property
    def size(self):
        """Return protected width"""
        return self.width

    @size.setter
    def size(self, value):
        """Modify the value of width or height as size"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Method: update arguments"""
        list_arg = ["id", "size", "x", "y"]
        if args and args is not None:
            for x in range(len(list_arg)):
                if x < len(args):
                    setattr(self, list_arg[x], args[x])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Method: convert to dictionary"""
        list_attr = ["id", "size", "x", "y"]
        new_Dict = {}
        for x in range(len(list_attr)):
            new_Dict[list_attr[x]] = getattr(self, list_attr[x])
        return new_Dict
