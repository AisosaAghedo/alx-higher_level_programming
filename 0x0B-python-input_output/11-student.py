#!/usr/bin/python3
"""
Class Student
"""


class Student:
    """ instantiation """
    def __init__(self, first_name, last_name, age):
        """ publicinstance attributes """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ public method """
        new_dict = {}
        if attrs is None:
            return self.__dict__
        else:
            for key in self.__dict__:
                if key in attrs:
                    new_dict[key] = self.__dict__[key]

            return new_dict

    def reload_from_json(self, json):
        """
        public method that replaces all attributes
        of the Student instance
        """
        for key in self.__dict__:
            if key in json:
                self.__dict__[key] = json[key]

        return self.__dict__
