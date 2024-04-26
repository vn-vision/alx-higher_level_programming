#!/usr/bin/python3
''' this script finds a peak in a list of unsorted integers '''


def find_peak(list_of_integers):
    ''' this takes a list of ints as a parameter '''
    peak = []
    length = len(list_of_integers)

    i = 1

    if length < 3:
        return None

    if all(x == list_of_integers[0] for x in list_of_integers):
        return [list_of_integers[0]]

    while i < length - 1:
        try:
            a = list_of_integers[i - 1]
            b = list_of_integers[i]
            c = list_of_integers[i + 1]
            if b > a and b > c:
                peak.append(b)
        except IndexError:
            pass
        i = i + 1
    return peak
