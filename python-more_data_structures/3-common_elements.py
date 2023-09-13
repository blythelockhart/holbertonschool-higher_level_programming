#!/usr/bin/python3
def common_elements(set_1, set_2):
    new_s = []
    for i in set_1:
        for j in set_2:
            if i == j:
                new_s.append(i)
    return new_s
