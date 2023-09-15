#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    ct = 0
    for x in range(x):
        try:
            if type(my_list[x]) == int:
                print('{:d}'.format(my_list[x]), end="")
                ct += 1
        except (IndexError, TypeError):
            break
    print()
    return ct
