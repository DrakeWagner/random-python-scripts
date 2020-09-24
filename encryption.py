#!/bin/usr/python env

# program to encrypt messages
# start with set encryption
# eventually add multiple characters per input to be decoded
import string
string.ascii_lowercase[8]

sentence1='Hello there'
letters=string.ascii_lowercase
def letterrotate(sentence):
    # sentence=input('Enter your message: ').lower()
    new_sentence=''
    for i in sentence: # ord('a') and ord('z') = 65 & 97
        num_digit = ord(i) + 1
        new_sentence+=str((chr(num_digit)))
    print(new_sentence)
    return new_sentence

letterrotate(sentence1)


# def caesar(text, rotation):
#     result=''
#     for i in range(len(text)):
#         char=text[i]
        



#     if char.isupper():
#         result += chr((ord(char) + rotation-65) % 26 + 65)
#     else:
#         result += chr((ord(char) + rotation-97) % 26 + 97)
#     return result




# test1='DRAKE WAGNER IN THE HOUSE'
# print(caesar(test1, 4))