#!/usr/bin/python3
""" A module that for JSON representation of an object """


import json


def to_json_string(my_obj):
    """ A function that returns JSON representation of an onject """
    return json.dumps(my_obj)
