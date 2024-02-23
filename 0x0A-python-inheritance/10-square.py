#!/usr/bin/python3
""" A Module that inherits a class """

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ A class that inherits a subclass rectangle from BaseGeometry """
    def __init__(self, size):
        super().integer_validator("size", size)
        self.__size = size

    def area(self):
        return self.__size ** 2
