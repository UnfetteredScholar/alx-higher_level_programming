#!/usr/bin/python3
def roman_to_int(roman_string):
    values = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
            '_': 0  # Used to denote end of string
            }
    res = 0
    if roman_string is None or type(roman_string) is not str or roman_string == "":
        return 0

    roman = roman_string + '_'
    for i in range(0, len(roman_string)):
        if values[roman[i]] < values[roman[i + 1]]:
            res -= values[roman[i]]
        else:
            res += values[roman[i]]
    return res
