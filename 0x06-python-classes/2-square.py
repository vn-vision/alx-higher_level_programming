#!/usr/bin/python3
""" this module is a continuation of 1-square.py """


class Square:
	""" Class defines properties of square
	
	Attributes:
		size: size of square
	"""

	def __init__(self, size=0):
		""" Creates new instances of square.
		
		Args:
			size: size of square side
		"""
		if not isinstance(size, int):
			raise TypeError("size must be an integer")
		elif size < 0:
			raise ValueError("size must be >= 0")
		else:
			self.__size = size
