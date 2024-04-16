#!/usr/bin/python3
""" A Module that two new line after a text """


def text_indentation(text):
    """ A Function that prints newline after encountering . ? /"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    new_str = text
    for delimeter in ".?:":
        new_str = new_str.replace(delimeter, delimeter + "\n\n")

    lines = new_str.split('\n')
    for line in lines:
        print(line.strip())
