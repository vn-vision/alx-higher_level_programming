#!/usr/bin/python3
""" Defines  inherited list class MyList """


class MyList(list):
    """ impplements the print function """
    def print_sorted(self):
        """ prints the list in sorted manner"""
        print(sorted(self))
