#!/usr/bin/python3
""" a class Square that defines a square by 2-square.py) """


class Square:
	""" class defines square properties
	Attributes:
		size: side of a square
	"""
	
	def __init__(self, size=0):
		""" creates new instance for square

		Args:
			size: side of a square
		"""

		self.__size = size

		if not isinstance(size, int):
			raise TypeError("size must be an integer")
		elif size < 0:
			raise ValueError("size must be >= 0")
		else:
			self.__size = size

	def area(self):
		""" calculates the area of square

		Returns: the area
		"""

		res = self.__size ** 2
		return res
