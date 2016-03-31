# -*- coding: utf-8 -*-

import random

def leftpad(string, total_len=0, char=' '):
	"""
	Recieves a string. If it's shorter than the gien total_len, it's filled 
	with the char param from left to right.
	"""

	to_add = total_len - len(string)

	if to_add > 0:
		char_string = ''
		for x in range(to_add):
			char_string = char_string+char
		string = char_string + string

	return string

def main():
	"""
	Test leftpad function.
	"""

	chars = ['#','&','@', '?',]

	for x in range(10):
		print leftpad('Ana', x, random.choice(chars))


if __name__ == '__main__':
	main()