#!/bin/usr/python env

# program to encrypt messages
# start with set encryption
# eventually add multiple characters per input to be decoded
import string
string.ascii_lowercase[8]

sentence1='Hello there'
letters=string.ascii_lowercase
def encrypt_right(sentence,rotation):
    # sentence=input('Enter your message: ').lower()
    new_sentence=''
    for i in sentence: # ord('a') and ord('z') = 65 & 97
        num_digit = ord(i) + rotation
        new_sentence+=str((chr(num_digit)))
    print(new_sentence)
    return new_sentence

encrypt_right(sentence1,5)
