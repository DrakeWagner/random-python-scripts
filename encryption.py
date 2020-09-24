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
    sentence=sentence.lower()
    for i in sentence: # ord('a') and ord('z') = 65 & 97
        num_digit = ord(i) + rotation
        new_sentence+=str((chr(num_digit)))
    print(new_sentence)
    return new_sentence

def encrypt_right_interactive():
    sentence=input('Enter your message: ').lower()
    rotation=int(input('How many rotations: '))
    new_sentence=''
    for i in sentence: # ord('a') and ord('z') = 65 & 97
        num_digit = ord(i) + rotation
        new_sentence+=str((chr(num_digit)))
    print(new_sentence)
    return new_sentence

def decrypt(sentence,rotation):
    new_sentence=''
    for i in sentence:
        num_digit = ord(i) - rotation
        new_sentence+=str((chr(num_digit)))
    print(new_sentence)


# encrypt_right(sentence1,5)
# encrypt_right_interactive()
decrypt('mjqqt%ymjwj', 5)
