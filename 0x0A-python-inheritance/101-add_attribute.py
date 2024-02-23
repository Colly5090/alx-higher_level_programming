#!/usr/bin/python3

def add_att(object, attr_name, value):
    """
    A function that adds an attribute to an object
    if not raise an exception
    """
    if hasattr(object, __dict__):
        setattr(object, attr_name, value)
    else:
        raise TypeError("can't add new attribute")
