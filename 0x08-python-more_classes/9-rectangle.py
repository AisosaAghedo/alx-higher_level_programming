#!/usr/bin/python3
""" A class that defines a rectangle with private instance
attributes width and height
"""


class Rectangle:
    """ representation of class Rectangle """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ instantiation of class Rectangle """
        self.height = height
        self.width = width
        Rectangle.number_of_instances = Rectangle.number_of_instances + 1

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
        if self.__width != 0 and self.__height != 0:
            string += "\n".join(str(self.print_symbol) * self.__width
                                for j in range(self.__height))
        return string

    def __repr__(self):
        """ returns a string representation of the rectangle """
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        Rectangle.number_of_instances = Rectangle.number_of_instances - 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area == rect_2.area:
            return rect_1


    @classmethod
    def square(cls, size=0):
        """ reurns a  new rectangle instance """
        return cls(size, size)

my_square = Rectangle.square(5)
print("Area: {} - Perimeter: {}".format(my_square.area(), my_square.perimeter()))
print(my_square)

