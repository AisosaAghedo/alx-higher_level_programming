#!/usr/bin/python3
""" a sub class """


class MyList(list):
    """ initialisation """
    def __init__(self):
        super().__init__()

    """  prints the list, but sorted (ascending sort)"""
    def print_sorted(self):
        print(sorted(self))
