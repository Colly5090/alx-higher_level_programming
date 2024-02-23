#!/usr/bin/python3
""" A Module that inherit from a class """

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ A Class that inherit from the basegeometry class """
    def __init__(self, width, height):
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height
