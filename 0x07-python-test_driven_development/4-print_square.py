#!/usr/bin/python3
""" A Module to print square """


def print_square(size):
    """ A Function that prints square with # """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    elif size < 0 and isinstance(size, float):
        raise TypeError("size must be an integer")
    else:
        for _ in range(size):
            print(size * "#")
