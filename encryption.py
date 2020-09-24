#!/bin/usr/python env

# program to encrypt messages
# start with set encryption
# eventually add multiple characters per input to be decoded


def caesar(text, rotation):
    result=''
    for i in range(len(text)):
        char=text[i]

    if char.isupper():
        result += chr((ord(char) + rotation-65) % 26 + 65)
    else:
        result += chr((ord(char) + rotation-97) % 26 + 97)
    return result




test1='DRAKE WAGNER IN THE HOUSE'
print(caesar(test1, 4))