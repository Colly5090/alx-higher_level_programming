#!/usr/bin/python3
""" A module that add attributes """


def add_attribute(object, attr_name, value):
    """
    A Function that adds attribute to an object
    """
    if hasattr(object, '__dict__') or isinstance(object, type):
        setattr(object, attr_name, value)
    else:
        raise TypeError("can't add new attribute")
