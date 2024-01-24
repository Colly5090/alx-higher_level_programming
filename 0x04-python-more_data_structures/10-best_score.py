#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None

    highest_score = None
    highest_key = None

    for key, value in a_dictionary.items():
        if highest_score is None or value > highest_score:
            highest_score = value
            highest_key = key
    return highest_key
