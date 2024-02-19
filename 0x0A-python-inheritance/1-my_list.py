#!/usr/bin/python3
""" A Module that inherits MyList from list """


class MyList(list):
    """
    A Class that inherits from list

    Attribute:
        None Currently defined
    Method:
        None Currently defined

    """
    def print_sorted(self):
        print(sorted(self))
