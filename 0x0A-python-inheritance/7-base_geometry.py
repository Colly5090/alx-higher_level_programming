#!/usr/bin/python3
""" A Module that defines an empty class """


class BaseGeometry:
    """ An Empty class defined with no attributes and methods """

    def area(self):
        """ Raise an exception area is not implemented """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Validates that the 'value' is an integer greater than 0 """
        if not isinstance(value, int):
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
