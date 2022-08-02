#!/usr/bin/python3
"""
A function that returns a list of lists of integers
representing the Pascal’s triangle of n
"""

def pascal_triangle(n):
    """
    returns a list of list of integers
    """
    if n <= 0:
        return []

    new_list = [[1]]
    while len(new_list) != n:
        triangle = new_list[-1]
        temp = [1]
        for i in range(len(tringle) - 1):
            temp.append(triangle[i] + triangle[i + 1])
        temp.append(1)
        new_list.append(temp)
    return new_list
