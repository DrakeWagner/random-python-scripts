#!/bin/usr/python env
import string
letters=string.ascii_lowercase

# Special cryptography code for Drake and Arushi

def encrypt(sentence,rotation):
    # sentence=input('Enter your message: ').lower()
    new_sentence=''
    sentence=sentence.lower()
    for i in sentence: # ord('a') and ord('z') = 65 & 97
        num_digit = ord(i) + rotation
        new_sentence+=str((chr(num_digit)))
    print(new_sentence)
    return new_sentence

def encrypt_interactive():
    sentence=input('Enter your message: ').lower()
    rotation=int(input('How many rotations: '))
    new_sentence=''
    for i in sentence: # ord('a') and ord('z') = 65 & 97
        num_digit = ord(i) + rotation
        new_sentence+=str((chr(num_digit)))
    print('Your encrypted message is: ',new_sentence, '\n\
Your rotation code is: ', rotation, sep='')
    return new_sentence

def decrypt(sentence,rotation):
    new_sentence=''
    for i in sentence:
        num_digit = ord(i) - rotation
        new_sentence+=str((chr(num_digit)))
    print(new_sentence)

def decrypt_interactive():
    sentence=input('Enter the message to decrypt: ').lower()
    rotation=int(input('How many rotations: '))
    new_sentence=''
    for i in sentence:
        num_digit = ord(i) - rotation
        new_sentence+=str((chr(num_digit)))
    print('Your decrypted message is: ', new_sentence, sep='')

def interface():
    choice=input('Encrypt or Decode <E or D>: ').lower()
    print(choice)
    if choice == ('e' or 'encrypt'):
        encrypt_interactive()
        interface()
    elif choice == ('d' or 'decrypt'):
        decrypt_interactive()
        interface()
    elif choice == ('q' or 'quit'):
        import sys
        sys.exit(0)

interface()