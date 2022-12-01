#!/usr/bin/python3

if __name__ == "__main__":
    """Print the count and list of args on different line"""
    import sys

    len = len(sys.argv) - 1
    if len == 0:
        print("0 arguments.")
    elif len == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format((len)))
    for i in range(1, len + 1):
        print("{}: {}".format(i, sys.argv[i]))
