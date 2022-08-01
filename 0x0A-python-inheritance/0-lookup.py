#!/usr/bin/python3
""" function to list list of attributes of obj """


def lookup(obj):
    """ returns a list of available attributes and methods of an object"""
    return(dir(obj))
