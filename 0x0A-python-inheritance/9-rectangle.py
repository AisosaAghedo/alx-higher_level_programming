#!/usr/bin/python3
"""
class BaseGeometry and subclass Rectangle
"""


class BaseGeometry:
    """A class with public instance methods"""
    def area(self):
        """raises an exception """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validator """
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """ subclass rectangle"""
    def __init__(self, width, height):
        """instantiation """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """returns area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """informal string representation of the rectangle"""
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
