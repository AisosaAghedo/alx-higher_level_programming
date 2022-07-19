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

    def area(self):
        """ returns area of a square """
        return(self.__size ** 2)

    @property
    def size(self):
        """ To retrieve the size"""

        return (self.__size)

    @size.setter
    def size(self, value):
        """ to set value for size"""

        if type(value) is not int:
            raise (TypeError("size must be an integer"))
        elif value < 0:
            raise (ValueError("size must be >= 0"))
        else:
            self.__size = value

    def my_print(self):
        """  prints in stdout the square with the character # """

        if self.__size == 0:
            print()
        else:
            for rows in range(self.__size):
                print(self.__size * '#')
