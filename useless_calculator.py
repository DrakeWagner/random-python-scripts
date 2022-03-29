#!/usr/bin/env python

def get_1():
    return 1
def get_2():
    return 2
def get_3():
    return 3
def get_4():
    return 4
def get_5():
    return 5
def get_6():
    return 6
def get_7():
    return 7
def get_8():
    return 8
def get_9():
    return 9
def get_0():
    return 0

def add(num1, num2):
    return num1 + num2
def subtract(num1, num2):
    return num1 - num2
def multiply(num1, num2):
    return num1 * num2
def divide(num1, num2):
    return num1 / num2

def calculate():
    i = input('Enter single digit, operator, and second digit:  ')
    num1 = i.split()[0][0]
    op = i.split()[0][1]
    num2 = i.split()[0][2]

calculate()