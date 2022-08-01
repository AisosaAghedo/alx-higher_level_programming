#!/usr/bin/python3
""" function that adds a new attribute to an object if it’s possible """


def add_attribute(obj, name, value):
    """ raises a a TypeError if new attribute can't be added """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    else:
        setattr(obj, name, value)
