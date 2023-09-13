#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    dict_c = a_dictionary.copy()
    for i in a_dictionary:
        dict_c[i] = a_dictionary[i] * 2
    return dict_c
