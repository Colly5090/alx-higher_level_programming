#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dict = {}

    for key, value in a_dictionary.items:
        new_dict[key] = value * 2
        result = '\
                '.join([f'{key}: {value}' for key, value in new_dict.items()])
    return result_str
