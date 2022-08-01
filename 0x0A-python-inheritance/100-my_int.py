#!/usr/bin/python3
"""
class int and subclass Myint
"""


class MyInt(int):
    """ inherits from class int """

    def __eq__(self, value):
        if (self - value == 0):
            return False
        else:

            return True

    def __ne__(self, value):
        if self - value != 0:
            return False
        else:
            return True
