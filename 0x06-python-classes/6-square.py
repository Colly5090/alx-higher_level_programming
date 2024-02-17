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
    def __init__(self, size=0, position=(0, 0)):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        if not (isinstance(position, tuple) and len(position) == 2 and
        all(isinstance(item, int) and item > 0 for item in position)):
            raise TypeError("position must be a tuple of 2 positive integers")
        
        self.__size = size
        self.__position = position

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
    
    @property
    def position(self):
        return self.__position
    
    @position.setter
    def position(self, value):
        if not (isinstance(value, tuple) and len(value) == 2 and
        all(isinstance(item, int) and item > 0 for item in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if self.__size == 0:
            print()
            return
        
        for _ in range(self.__position[1]):
            print("")
        
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
