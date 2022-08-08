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

    def update(self, *args, **kwargs):
        """ update args and kwargs arguments """
        if len(args) > 0:
            for i in args:
                if len(args) == 1:
                    self.id = args[0]
                elif len(args) == 2:
                    self.id, self.width = args
                elif len(args) == 3:
                    self.id, self.width, self.height = args
                elif len(args) == 4:
                    self.id, self.width, self.height, self.x = args
                elif len(args) == 5:
                    self.id, self.width, self.height, self.x, self.y = args

        else:
            for key in kwargs:
                if key == 'id':
                    self.id = kwargs[key]
                elif key == 'width':
                    self.width = kwargs[key]
                elif key == 'height':
                    self.height = kwargs[key]
                elif key == 'x':
                    self.x = kwargs[key]
                elif key == 'y':
                    self.y = kwargs[key]

    def to_dictionary(self):
        """ return dict representation """
        New_dict = {'id': self.id, 'width': self.width,
                    'height': self.height, 'x': self.x, 'y': self.y}
        return New_dict
