#!/usr/bin/python3
def no_c(my_string):
    new = ''.join(ch for ch in my_string if ch != 'c' and ch != 'C')
    return new
