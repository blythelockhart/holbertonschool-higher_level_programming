#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list is None:
        return None
    keep = my_list[0]
    for i in my_list:
        if i > keep:
            keep = i
    return keep
