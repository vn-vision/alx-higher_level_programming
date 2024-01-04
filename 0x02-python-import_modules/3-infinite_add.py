#!/usr/bin/python3

def infnit_add():

    import sys

    n = len(sys.argv)
    i = 1
    results = 0

    while (i < n):
        results += int(sys.argv[i])
        i += 1

    print(results)


if __name__ == "__main__":
    infnit_add()
