#!/usr/bin/python3
""" defines a square based on 5-square.py, uses property
to update and access private attributes """


class Square:

	def __init__(self, size=0, position=(0, 0)):
		""" private instance size, size of the square """
		if not isinstance(size, int):
			raise TypeError("size must be an integer")
		elif size < 0:
			raise ValueError("size must be >= 0")
		self.__size = size

		""" private instance position, type tuple """
		if not isinstance(position, tuple) or len(position) != 2:
			raise TypeError("position must be a tuple of 2 positive integers")

		self.__position = position

	""" the property getter and setter for size """
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

	""" the property getter and setter for position-tuple"""
	@property
	def position(self):
		return self.__position

	@position.setter
	def position(self, value):
		if not isinstance(value, tuple) or len(value) != 2:
			raise TypeError("position must be a tuple of 2 positive integers")

		self.__position = position

	""" function to calculate the area of the square """
	def area(self):
		res = self.__size ** 2
		return res

	""" my_print function """
	def my_print(self):
		if self.__size == 0:
			print()
		else:
			for i in range(self.__position[1]):
				print()
			for i in range(self.__size):
				print(' ' * self.__position[0] + '#' * self.__size)
