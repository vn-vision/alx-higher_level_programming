#!/usr/bin/python3

import sys
def safe_print_integer_err(value):
	while True:
		try:
			print("{:d}".format(value))
			return True
		except ValueError as ve:
			print("Exception: {}".format(ve), file=sys.stderr)
			return False
