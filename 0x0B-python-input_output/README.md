# PYTHON INPUT / OUTPUT

This directory contains the different methods for Writing, Reading and deleting
from a file.

The standard output file can be referenced as { sys.stdout }

open() - returns a file object, used with two positional arguments and one keyword argument
read() - opens a file for reading
readline() - reads a single line from the file
write() - writes into a file

f = open('Workfile', 'w', encoding="utf-8")

    workfile - the file to open
    w - write, if existing file it will be removed
    r - read,
    a - appending,
    r+ - both reading and writing
    encoding - the modern de-facto standard

using `with` keyword when dealing with file objects, properly closes the file.
Else, you should call f.close()
