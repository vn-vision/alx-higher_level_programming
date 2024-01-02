#!/usr/bin/python3

# chr()-converts the Unicode for ASCII back to characters
# ord()-gets the UNICODE for each character in ASCII
for letter in range(97, 123):
    if chr(letter) != 'q' and chr(letter) != 'e':
        print("{}".format(chr(letter)), end="")
