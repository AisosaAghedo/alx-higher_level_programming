#!/usr/bin/python3
""" A class that defines a rectangle with private instance
attributes width and height
"""


class Rectangle:
    """ representation of class Rectangle """

    def __init__(self, width=0, height=0):
        """ instantiation of class Rectangle """
        self.height = height
        self.width = width

    @property
    def width(self):
        """ retrieves the private instance attribute width """
        return self.__width

    @width.setter
    def width(self, value):
        """sets the private instance attribute width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ retrieves the private instance attribute height """
        return self.__height

    @height.setter
    def height(self, value):
        """ sets the private instance attribute height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ returns area of a rectangle """
        return self.__height * self.__width

    def perimeter(self):
        """ returns the perimeter of a rectangle """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (2 * self.__width) + (2 * self.__height)

    def __str__(self):
        """ string representation """
        string = ""
        i = 0
        if self.__width != 0 and self.__height != 0:
            while i < self.__height:
                print("#" * self.__width)
                i = i + 1
        return string
