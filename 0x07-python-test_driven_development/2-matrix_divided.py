#!/usr/bin/python3
""" module to divide a list of list o integers or floats by a number(div)"""


def matrix_divided(matrix, div):
    """ This function returns a new list """

    new_m = [[] * i for i in range(len(matrix))]
    size = None
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for i in range(len(matrix)):
        if type(matrix[i]) is not list:
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")
        if size is None:
            size = len(matrix[i])
        elif size != len(matrix[i]):
            raise TypeError("Each row of the matrix must have the same size")
        for j in range(len(matrix[0])):
            if type(matrix[i][j]) != int and type(matrix[i][j]) != float:
                raise TypeError("matrix must be a matrix (list of lists) of\
 integers/floats")

            new_m[i].append(round(matrix[i][j] / div, 2))
    return new_m
