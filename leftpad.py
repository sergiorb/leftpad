# -*- coding: utf-8 -*-

import random

def leftpad(string, total_len=0, char=' '):
	"""
	Recieves a string. If it's shorter than the total_len, it's filled 
	with the char param from left to right.
	"""

	# Creates a list filled with the given char, where amount of chars
	# equals the difference between total length and string_length.
	# Then they are joined by none('') char and added to the original string.
	# This works because the function range takes the initial value as 0 by default.
	# For example, range(-100) equals range(0, -100), that produce an empy list because
	# the second parameter have to be greater than the first one.

	return ''.join([char for x in range(total_len - len(string))]) + string
		

def main():
	"""
	Test leftpad function.
	"""

	chars = ['#','&','@', '?',]

	for x in range(-10, 10):
		print leftpad('Ana', x, random.choice(chars))


if __name__ == '__main__':

	main()
