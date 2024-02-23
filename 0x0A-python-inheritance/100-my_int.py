#!/usr/bin/python3
""" A module that defines class """


class MyInt(int):
    """ A class that define == and != in an inverted form """
    def __eq__(self, other):
        return not super().__eq__(other)

    def __ne__(self, other):
        return not super().__ne__(other)
