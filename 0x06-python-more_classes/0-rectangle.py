#!/usr/bin/python3
"""Writing a class that defines a rectangle by width and height"""


class Rectangle():
	def __init__(self, width=0, height=0):
		"""Initialize weight and height attributes"""
		self.width = width
		self.height = height

		if width is not type(int):
			raise TypeError("width must be an integer")
		if height is not type(int):
			raise TypeError("height must be an integer")
		if width <= 0:
			raise ValueError("width must be >= 0")
	pass
