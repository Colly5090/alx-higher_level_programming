#!/usr/bin/python3
""" A Module to define a square, its shape and properties """


class Square:
    """
    A class to define a square
    This class defines the basic geometric functionalities of a sqaure

    Attributes:
        A private size as functionality of the square

    Methods:
        None currently defined
    """
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return self.__size ** 2
