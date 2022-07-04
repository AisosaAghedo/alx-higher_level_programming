#!/usr/bin/python3
def max_integer(my_list=[]):
    maxi = my_list[0]
    i =  0
    length = len(my_list)
    if length == 0:
        return(None)
    else:
        while i < length:
            maxi = maxi[i]
            i = i + 1
    return(maxi)
