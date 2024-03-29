#!/usr/bin/python3
""" A Module that handles file input and output"""


def read_file(filename=""):
    """ A funtion that reads a UTF8 text files and print to stdout """
    with open(filename, 'r', encoding='utf-8') as file:
        print(file.read(), end='')
