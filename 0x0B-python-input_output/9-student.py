#!/usr/bin/python3
"""
a class student
"""


class Student:
    """ instantiation """
    def __init__(self, first_name, last_name, age):
        """ publicinstance attributes """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ public method """
        return self.__dict__
