#!/usr/bin/python3
""" The module 4-print_square takes one argument, which is the size"""


def print_square(size):
    """ this function prints  a square with the character # """

    i = 0
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if type(size) == float and size < 0:
        raise TypeError("size must be an integer")
    while i < size:
        print("#" * size)
        i = i + 1
