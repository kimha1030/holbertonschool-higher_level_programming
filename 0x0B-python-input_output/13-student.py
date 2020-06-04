#!/usr/bin/python3
"""Class Student"""


class Student:
    """Class Student"""

    def __init__(self, first_name, last_name, age):
        """Constructor"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Function: returns the dictionary with the property of class"""
        if type(attrs) == list:
            for s in attrs:
                if type(s) is not str:
                    return(self.__dict__)
            new_dict = {}
            for key, value in self.__dict__.items():
                for k in attrs:
                    if k == key:
                        new_dict[key] = value
            return(new_dict)
        else:
            return(self.__dict__)

    def reload_from_json(self, json):
        for key, value in json.items():
            setattr(self, key, value)
