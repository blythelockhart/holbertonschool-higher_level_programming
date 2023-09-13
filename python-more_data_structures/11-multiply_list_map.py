#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    new_l = []
    for i in my_list:
        new_l.append(i * number)
    return new_l
