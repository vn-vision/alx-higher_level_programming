#!/usr/bin/python3
""" defines a square based on 3-square.py,
uses property to update and access private attributes """


class Square:

	def __init__(self, size=0):
		if not isinstance(size, int):
			raise TypeError("size must be an integer")
		elif size < 0:
			raise ValueError("size must be >= 0")
		self.__size = size

	@property
	def size(self):
		return self.__size

	@size.setter
	def size(self, value):
		if not isinstance(value, int):
			raise TypeError("size must be an integer")
		elif value < 0:
			raise ValueError("size must be >= 0")
		self.__size = value

	def area(self):
		return (self.size ** 2)
