#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    num = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    final_integers = 0
    roman_value = 0

    for char in reversed(num):
        value = num.get(char, 0)
        if value < roman_value:
            final_integers -= value
        else:
            final_integers += value
        roman_value = value

    return final_integers
