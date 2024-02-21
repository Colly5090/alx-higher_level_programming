#!/usr/bin/python3
""" A module that represents an object into JSON """


import json


def from_json_string(my_str):
    """ A function that represents an object in json string """
    return json.loads(my_str)
