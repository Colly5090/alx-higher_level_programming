#!/usr/bin/python3
""" A Module that reads stdin line by line """


import sys

def print_stats(total_size, status_count):
    """ A script that reads stdin line by line with with requested metrics"""
    print("File size: {}".format(total_size))
    for status_code in sorted(status_count.keys()):
        print("{}: {}".format(status_code, status_count[status_code]))

total_size = 0
status_count = {}
line_count = 0

try:
    for line in sys.stdin:
        line_count += 1
        tokens = line.split()
        status_code = tokens[-2]
        file_size = int(tokens[-1])
        total_size += file_size
        status_count[status_code] = status_count.get(status_code, 0) + 1

        if line_count % 10 == 0:
            print_stats(total_size, status_count)
except KeyboardInterrupt:
    print_stats(total_size, status_count)
