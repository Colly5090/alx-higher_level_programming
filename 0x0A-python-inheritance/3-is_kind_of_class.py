#!/usr/bin/python3
""" A Module that check object is an instance of a class """


def is_kind_of_class(obj, a_class):
    """
    A Function that checks if an object is an
    instance of a class or a subclass
    """
    return isinstance(obj, a_class)
