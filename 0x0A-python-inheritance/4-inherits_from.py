#!/usr/bin/python3
""" A Module that returns True or False"""


def inherits_from(obj, a_class):
    """
    Check if obj is an instance of a class that inherited
    (directly or indirectly)
    from the specified class a_class. """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
