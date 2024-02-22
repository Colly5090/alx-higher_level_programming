#!/usr/bin/python3
""" A Module that add arguments to a file """


import json
import sys


def save_to_json_file(my_obj, filename):
    """
    A function that writes object to a text file using JSON
    representation
    """
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(my_obj, file)

def load_from_json_file(filename):
    """ A Function that loads an object from a JSON file """
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)
    
args = sys.argv[1:]
filename = "add_item.json"

try:
    items = load_from_json_file(filename)
except FileNotFoundError:
    items = []

items.extend(args)
save_to_json_file(items, filename)