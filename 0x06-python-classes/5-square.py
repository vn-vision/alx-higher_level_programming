#!/usr/bin/python3

""" defines a square based on 4-square.py,
uses property to update and access private attributes """


class Square:
	"""
	Class that defines properties of square by: (based on 4-square.py).

	Attributes:
	size: size of a square (1 side).
	"""
	def __init__(self, size=0):
		"""Creates new instances of square.

		Args:
		    size: size of the square (1 side).
		"""
		if not isinstance(size, int):
			raise TypeError("size must be an integer")
		elif size < 0:
			raise ValueError("size must be >= 0")
		else:
			self.__size = size

	@property
	def size(self):
		""" Return the size """
		return self.__size

	@size.setter
	def size(self, value):
		"""Property setter for size.

		Args:
		    value (int): size of a square (1 side).

		Raises:
		    TypeError: size must be an integer
		    ValueError: size must be >= 0
		"""
		if not isinstance(value, int):
			raise TypeError("size must be an integer")
		elif value < 0:
			raise ValueError("size must be >= 0")
		self.__size = value

	def area(self):
		"""Calculates the area of square.

		Returns: the current square area.
		"""
		res = self.__size ** 2
		return res

	def my_print(self):
	""" my_print function - prints the square in '#' """
		if self.__size == 0:
			print()
		else:
			for i in range(self.__size):
				print('#' * self.__size)
