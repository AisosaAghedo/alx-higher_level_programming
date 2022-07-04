#!/usr/bin/python3
def max_integer(my_list=[]):
    i =  0
    maxi = 0
    length = len(my_list)
    if length == 0:
        return(None)


    while i < length:
        if my_list[i] > maxi:
            maxi = my_list[i]
        i = i + 1
    return(maxi)
