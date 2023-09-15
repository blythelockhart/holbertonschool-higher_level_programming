#!/usr/bin/python3
dict_c = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
}
def roman_to_int(roman_string):
    num = 0
    prev_value = 0
    for char in roman_string[::-1]:
        value = roman_dict[char]
        if value > prev_value:
            num += value
        else:
            num -= value
        prev_value = value
    return num
