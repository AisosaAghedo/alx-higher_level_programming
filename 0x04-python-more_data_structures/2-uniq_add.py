#!/usr/bin/python3
def uniq_add(my_list=[]):
    result = list(set(my_list))
    sum = 0
    for i in result:
        sum = sum + i
    return(sum)
