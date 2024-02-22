#!/usr/bin/python3
""" A Module for data structure of JSON """


def class_to_json(obj):
    """ A function that returns dictionary description of a JSON """
    return obj.__dict__
