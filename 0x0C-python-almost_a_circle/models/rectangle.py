#!/usr/bin/python3
""" A sub class Rectangle """
from models.base import Base


class Rectangle(Base):
    """ constructor """
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    """ retrieves private attribute x """
    @property
    def x(self):
        return self.__x

    """ sets private attribute x """
    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    """ retrieves private attribute y """
    @property
    def y(self):
        return self.__y

    """ sets private attribute y """
    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")

        self.__y = value

    """ retrieves private attribute width"""
    @property
    def width(self):
        return self.__width

    """ sets private attribute width """
    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

        self.__width = value

    """ retrieves private attribute height """
    @property
    def height(self):
        return self.__height

    """ sets private attribute y """
    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    def area(self):
        """ returns area of a rectangle """
        return self.__width * self.__height

    def display(self):
        """print to stdout"""
        [print("") for y in range(self.__y)]
        for i in range(self.__height):
            [print(" ", end="") for x in range(self.__x)]
            [print("#", end="") for w in range(self.__width)]
            print("")

    def __str__(self):
        """ __str__ representation of the rectangle"""
        return "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".format(self.id,
                                                                 self.__x,
                                                                 self.__y,
                                                                 self.__width,
                                                                 self.__height)


