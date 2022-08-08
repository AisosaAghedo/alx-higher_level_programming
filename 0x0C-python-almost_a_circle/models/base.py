#!/usr/bin/python3
""" A class named base """
from json import dumps
from json import loads


class Base:
    """ private class attribute """
    __nb_objects = 0

    def __init__(self, id=None):
        """ constructor """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    """static method that returns JSON string"""
    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or len(list_dictionaries) == []:
            return '[]'
        else:
            return dumps(list_dictionaries)

    """ class method that writes json repr to file """
    @classmethod
    def save_to_file(cls, list_objs):
        filename = cls.__name__ + ".json"
        with open(filename, "w") as f:
            if list_objs is None:
                f.write("[]")
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                f.write(Base.to_json_string(list_dicts))

    """ static method that returns the list of the JSON string repr"""
    @staticmethod
    def from_json_string(json_string):
        new_list = '[]'
        if json_string is None:
            return new_list
        elif len(json_string) == 0:
            return new_list
        else:
            new_list = loads(json_string)
            return new_list

    """ class method that returns the instance with all atrributes set"""
    @classmethod
    def create(cls, **dictionary):
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new_dict = cls(1, 1)
            else:
                new_dict = cls(1)
            new_dict.update(**dictionary)
            return new_dict

    """class method that returns a list of all instances """
    @classmethod
    def load_from_file(cls):
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r") as f:
                list_dicts = Base.from_json_string(f.read())
                return [cls.create(**dict) for dict in list_dicts]
        except IOError:
            return []
