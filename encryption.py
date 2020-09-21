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
    return result
