#!/usr/bin/python3
""" A Module to append a string in a text file """


def append_after(filename="", search_string="", new_string=""):
    """
    A Function that inserts a line of text
    to a file with a specific string
    """
    with open(filename, "r") as file:
        lines = file.readlines()

    with open(filename, 'w') as file:
        for line in lines:
            file.write(line)
            if search_string in line:
                file.write(new_string)
