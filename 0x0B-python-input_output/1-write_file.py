#!/usr/bin/python3
""" A Module that writes a string to a text file """


def write_file(filename="", text=""):
    """
    A function to write a string to a UTF8 text file and return
    number of characters
    """
    with open(filename, 'w', encoding='utf-8') as file:
        numb_chars = file.write(text)
    return numb_chars
