#!/usr/bin/python3

def uppercase(str):
    for i in str:
        char = ord(i)
        if 'a' <= char <= 'z':
            string += chr(char - 32)
        else:
            string += char
    print('{}'.format(str))
