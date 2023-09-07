#!/usr/bin/python3

def uppercase(s):
    string = ""
    for char in s:
        if 'a' <= char <= 'z':
            string += chr(ord(char) - 32)
        else:
            string += char
    print(string)
