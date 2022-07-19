#!/usr/bin/python3
""" defines class Square """


class Square:
    """ defines the class square"""

    def __init__(self, size=0):
        """ constructor of class 'Square' with the size """

        if type(size) is not int:
            raise (TypeError("size must be an integer"))
        elif size < 0:
            raise (ValueError("size must be >= 0"))
        else:
            self.__size = size
