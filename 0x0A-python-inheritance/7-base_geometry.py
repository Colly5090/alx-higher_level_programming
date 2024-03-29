#!/usr/bin/python3
""" A Module that defines an empty class """


class BaseGeometry:
    """ An Empty class defined with no attributes and methods """

    def area(self):
        """ Raise an exception area is not implemented """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Validates that the 'value' is an integer greater than 0 """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
