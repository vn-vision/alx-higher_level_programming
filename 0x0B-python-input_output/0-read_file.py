#!/usr/bin/python3
""" function reads a text file in encoding=utf8 """


def read_file(filename=""):
    f = with open(filename, 'r', encoding='utf-8')
    f.read()
