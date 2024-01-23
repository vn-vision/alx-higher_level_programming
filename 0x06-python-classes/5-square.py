#!/usr/bin/python3

""" defines a square based on 4-square.py,
uses property to update and access private attributes """


class Square:
	""" Class square and it's attributes """
	
	def __init__(self, size=0):
		""" private instance size """
		
		if not isinstance(size, int):
			raise TypeError("size must be an integer")
		elif size < 0:
			raise ValueError("size must be >= 0")
		self.__size = size
		
	@property
	def size(self):
		""" the property getter and setter for size """
		return self.__size

	@size.setter
	def size(self, value):
		""" the setter for the private instance """
		
		if not isinstance(value, int):
			raise TypeError("size must be an integer")
		elif value < 0:
			raise ValueError("size must be >= 0")
		self.__size = value

	def area(self):
		""" public function to calculate the area of the square """
		res = self.__size ** 2
		return res

	def my_print(self):
	""" my_print function - prints the square in '#' """
		if self.__size == 0:
			print()
		else:
			for i in range(self.__size):
				print('#' * self.__size)
