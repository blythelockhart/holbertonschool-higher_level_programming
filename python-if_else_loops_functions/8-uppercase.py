#!/usr/bin/python3

def uppercase(str):
    string = ""
    for i in str:
        char = ord(i)
        if 97 <= char <= 122:
            string += chr(char - 32)
        else:
            string += i
    print('{}'.format(string))
