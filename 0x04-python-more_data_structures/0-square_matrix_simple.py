#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    length = len(matrix)
    new_list = [[] * i for i in range(length)]
    
    i = 0
    while i < length:
        new_list[i] = list(map((lambda x: x * x),matrix[i] ))
        i = i + 1
    return(new_list)

