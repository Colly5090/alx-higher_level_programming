#!/usr/bin/python3
""" A module that defines class """


class MyInt(int):
    """ A class that define == and != in an inverted form """
    def __eq__(self, other):
        return self.__ne__(self, other)

    def __ne__(self, other):
        return self.__eq__(self, other)
