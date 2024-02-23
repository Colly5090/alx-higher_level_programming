#!/usr/bin/python3
""" Module for add_inter """


def add_integer(a, b=98):
    """ Function that add two integers """
    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    elif type(b) not in (int, float):
        raise TypeError("b must be an integer")
    else:
        return int(a) + int(b)
