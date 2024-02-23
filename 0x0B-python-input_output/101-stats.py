#!/usr/bin/python3
""" A Module that reads stdin line by line """


def print_stats(total_size, status_count):
    """ A script that reads stdin line by line with with requested metrics"""
    print("File size: {}".format(total_size))
    for key in sorted(status_count):
        print("{}: {}".format(key, status_count[key]))


if __name__ == "__main__":
    import sys
    total_size = 0
    status_count = {}
    line_count = 0
    status_code = ['200', '301', '400', '401', '403', '404', '405', '500']

    try:
        for line in sys.stdin:
            if line_count == 10:
                print_stats(total_size, status_count)
                line_count = 1
            else:
                line_count += 1
            tokens = line.split()
            try:
                total_size += int(tokens[-1])
            except (IndexError, ValueError):
                pass
            try:
                if tokens[-2] in status_code:
                    if status_count.get(tokens[-2], -1) == -1:
                        status_count[tokens[-2]] = 1
                    else:
                        status_count[tokens[-2]] += 1
            except IndexError:
                pass
        print_stats(total_size, status_count)
    except KeyboardInterrupt:
        print_stats(total_size, status_count)
        raise
