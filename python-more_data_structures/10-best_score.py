#!/usr/bin/python3
def best_score(a_dictionary):
    best_s = max(a_dictionary, key=a_dictionary.get)
    return best_s
