#!/usr/bin/python3
"""Writing a class that defines a 
rectangle by width and height
"""


class Rectangle():
	"""Rectangle class defined by width and height."""
	
	def __init__(self, width=0, height=0):
		"""Initialize weight and height attributes"""
		self.width = width
		self.height = height

		if width is not type(int):
			raise TypeError("width must be an integer")
		if height is not type(int):
			raise TypeError("height must be an integer")
		if width < 0:
			raise ValueError("width must be >= 0")
	
	@property
	def width(self):
		"""Retrieves the width of a Rectangle instance"""
		return self.__width
	
	@width.setter
	def width(self, value):
		"""Sets the width of a rectangle instance"""
		self.__width = value

	@property
	def height(self, value):
		"""Retrieves the height of Rectangle instance"""
		return self.__height
	
	@height.setter
	def height(self, value):
		"""Sets the height of a Rectangle instance"""
		self.__height = value