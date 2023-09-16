#!/usr/bin/python3

from flag import FLAG

encoded = ''

for i in FLAG:
	encoded += str(ord(i)) + " "

print(encoded)
