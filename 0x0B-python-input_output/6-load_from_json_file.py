#!/usr/bin/python3
""" A module that creates an object from a json file """


import json


def load_from_json_file(filename):
    """ A Function that loads an object from a JSOm file """
    with open(filename, 'r', encoding='utf-8') as file:
        json.load(file)
