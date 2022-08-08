#!/usr/bin/python3
""" sub class square that inherits from sub class Rectangle"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """ Class constructor """
    def __init__(self, size, x=0, y=0, id=None):
        """ super method """
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """ string method """
        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(self.id,
                                                         self.x,
                                                         self.y,
                                                         self.size)

    """ retrieves the size """
    @property
    def size(self):
        return self.width

    """ sets the size """
    @size.setter
    def size(self, value):
        self.height = value
        self.width = value

    def update(self, *args, **kwargs):
        """ update with args and kwargs """
        if len(args) > 0:
            for i in args:
                if len(args) == 1:
                    self.id = args[0]
                elif len(args) == 2:
                    self.id, self.size = args
                elif len(args) == 3:
                    self.id, self.size, self.x = args
                elif len(args) == 4:
                    self.id, self.size, self.x, self.y = args

        else:
            for key in kwargs:
                if key == 'id':
                    self.id = kwargs[key]
                elif key == 'size':
                    self.size = kwargs[key]
                elif key == 'x':
                    self.x = kwargs[key]
                elif key == 'y':
                    self.y = kwargs[key]

    def to_dictionary(self):
        """ returns a dictionary"""
        New_dict = {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}
        return New_dict
