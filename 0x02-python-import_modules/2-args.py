#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    total_args = len(sys.argv[1:]) #couting total number of args excluding script name from 1

    if total_args > 1:
        print(f"{total_args} arguments:")
        for index, item in enumerate(sys.argv[1:], start=1):
            print(f"{index}: {item}")
    elif total_args == 1:
        print(f"1 argument:")
        print(f"1: {sys.argv[1]}")
    else:
        print("0 arguments.)
