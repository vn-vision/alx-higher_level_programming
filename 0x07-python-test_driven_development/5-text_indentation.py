#!/usr/bin/python3
''' text indentation '''


def text_indentation(text):
    """Print text with 2 new lines after '.', '?', and ':'"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    delimiters = ['.', '?', ':']
    current_line = ""

    for char in text:
        current_line += char
        if char in delimiters:
            print(current_line.strip())
            print()  # Print two new lines
            current_line = ""

    if current_line:
        print(current_line.strip())
