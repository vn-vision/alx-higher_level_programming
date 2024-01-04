#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    n = len(sys.argv)
    i = 1

    if (n < 2):
        print("0 arguments.")
    elif (n == 2):
        print("1 argument:")
        print("1: {}".format(sys.argv[1]))
    else:
        print("{} arguments:".format((n - 1)))
        while (i < n):
            print("{}: {}".format(i, sys.argv[i]))
            i += 1
