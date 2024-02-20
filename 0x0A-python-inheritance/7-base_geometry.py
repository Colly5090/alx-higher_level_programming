#!/usr/bin/python3
""" A Module that defines an empty class """


class BaseGeometry(object):
    """ An Empty class defined with no attributes and methods """
    pass

    def area(self):
        """ Raise an exception area is not implemented """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Validates that the 'value' is an integer greater than 0 """
        if not isinstance(value, int) or isinstance(value, bool):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
