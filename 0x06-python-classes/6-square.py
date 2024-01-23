#!/usr/bin/python3
""" Defines a square based on 5-square.py, uses property
to update and access private attributes
"""


class Square:

	def __init__(self, size=0, position=(0, 0)):
		"""Creates new instances of square.

		Args:
		    __size (int): size of the square (1 side).
		    __position (tuple): position of the square.
		"""
		self.__size = size
		self.__position = position

	""" the property getter and setter for size """
	@property
	def size(self):
		"""Returns the size of a square
		"""
		return self.__size

	@size.setter
	def size(self, value):
		"""Property setter for size.

		Args:
		value (int): size of a square (1 side).

		Raises:
		TypeError: size must be an integer.
		ValueError: size must be >= 0.
		"""
		if not isinstance(value, int):
			raise TypeError("size must be an integer")
		elif value < 0:
			raise ValueError("size must be >= 0")
		self.__size = value

	""" the property getter and setter for position-tuple"""
	@property
	def position(self):
		""" Return position """
		return self.__position

	@position.setter
	def position(self, value):
		"""Property setter for position.

		Args:
		    value (tuple): position of the square.

		Raises:
		    TypeError: position must be a tuple of 2 positive integers
		"""
		if not isinstance(value, tuple) or len(value) != 2:
			raise TypeError("position must be a tuple of 2 positive integers")
		if not isinstance(value[0], int) or not isinstance(value[1], int):
			raise TypeError("position must be a tuple of 2 positive integers")
		if value[0] < 0 or value[1] < 0:
			raise TypeError("position must be a tuple of 2 positive integers")

		self.__position = value

	""" function to calculate the area of the square """
	def area(self):
		"""Calculates the area of square.

		Returns: the current square area.
		"""
		res = self.__size ** 2
		return res

	""" my_print function """
	def my_print(self):

		""" prints in stdout """
		if self.__size == 0:
			print()
		else:
			for i in range(self.__position[1]):
				print()
			for i in range(self.__size):
				print(' ' * self.__position[0] + '#' * self.__size)
