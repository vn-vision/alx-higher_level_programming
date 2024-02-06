#!/usr/bin/python3
""" Class MyInt"""


class MyInt(int):
    """ it inherits from int """

    def __eq__(self, other):
        """ Override the == operator """
        return super().__ne__(other)

    def __ne__(self, other):
        """ override the != operator """

        return super().__eq__(other)
