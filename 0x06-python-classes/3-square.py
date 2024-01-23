#!/usr/bin/python3
""" a class Square that defines a square by 2-square.py) """


class Square:
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        res = self.__size * self.__size
        return res
