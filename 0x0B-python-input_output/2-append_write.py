#!/usr/bin/python3
""" A module that appneds a string to a text file """


def append_write(filename="", text=""):
    """
    A function that appends a string at the end of a text file
    and returns the number of characters added
    """
    with open(filename, 'a', encoding='utf-8') as file:
        numb_char = file.write(text)
    return numb_char
