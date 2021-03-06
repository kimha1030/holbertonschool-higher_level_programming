#!/usr/bin/python3
"""ClassParent: Base"""
import json
import os.path


class Base:
    """Class Base that define the private attribute"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """Function: convert to obj json from str"""
        if not list_dictionaries and list_dictionaries is None:
            new_list = "[]"
        else:
            new_list = json.dumps(list_dictionaries)
        return new_list

    @classmethod
    def save_to_file(cls, list_objs):
        """Method for save obj json as file"""
        files = cls.__name__+".json"
        if list_objs is None:
            new_list = []
            with open(files, "w", encoding="UTF-8") as new_file:
                data = cls.to_json_string(new_list)
                new_file.write(data)
        else:
            with open(files, "w", encoding="UTF-8") as new_file:
                new_list = []
                for x in list_objs:
                    new_list.append(x.to_dictionary())
                data = cls.to_json_string(new_list)
                new_file.write(data)

    def from_json_string(json_string):
        """Function: convert from obj json to string"""
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return(json.loads(json_string))

    @classmethod
    def create(cls, **dictionary):
        """Method of class for create a dictionary"""
        if cls.__name__ == "Rectangle":
            value = cls(1, 1)
            value.update(**dictionary)
            return value
        if cls.__name__ == "Square":
            value = cls(1)
            value.update(**dictionary)
            return value

    @classmethod
    def load_from_file(cls):
        """Method of class for load from a file"""
        files = cls.__name__+".json"
        if os.path.isfile(files):
            with open(files, "r", encoding="UTF-8") as data_file:
                read_file = data_file.read()
                value = cls.from_json_string(read_file)
                new_list = []
                for x in value:
                    new_list.append(cls.create(**x))
                return new_list
        else:
            list_empty = []
            return list_empty
