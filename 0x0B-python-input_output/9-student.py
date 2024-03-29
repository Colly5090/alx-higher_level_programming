#!/usr/bin/python3
""" A Module that defines a class of student """


class Student:
    """
    A Class of Student that retrieves student attributes and
    instance in dictionary representation
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ Return the dictionary representation of this Student instance """
        return self.__dict__
