#!/usr/bin/python3
def uppercase(str):
    for char in str:
        if ord(i) >= 97 and ord(i) <= 122:
            char = chr(ord(i) - 32)
        print("{}".format(char), end='')
    print()
