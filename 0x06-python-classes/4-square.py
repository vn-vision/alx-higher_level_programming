#!/usr/bin/python3
""" Defines a square based on 3-square.py,
uses property to update and access private attributes """


class Square:
	""" Class defines 3-square.py

	Attributes:
		size: side of a square
	"""

	def __init__(self, size=0):
		""" Create new square instance.

		Args:
			size: size of the square
		"""

		if not isinstance(size, int):
			raise TypeError("size must be an integer")
		elif size < 0:
			raise ValueError("size must be >= 0")
		else:
			self.__size = size

	@property
	def size(self):
		""" Returns the set size """
		return self.__size

	@size.setter
	def size(self, value):
		""" Manipulates the private instance

		Args:
			value: the value to add

		Raises:
			TypeError if not int
			ValueError if not positive
		"""

		if not isinstance(value, int):
			raise TypeError("size must be an integer")
		elif value < 0:
			raise ValueError("size must be >= 0")
		self.__size = value

	def area(self):
		""" Calculates the area

		Returns: the area
		"""

		return (self.size ** 2)
