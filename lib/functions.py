#!/usr/bin/env python3

def greet_programmer():
    print("Hello, programmer!")

def greet(name):
    print("Hello, " + name + "!")

def greet_with_default(name="programmer"):
    if name is None:
        print("Hello, programmer!")
    else:
        print("Hello, " + name + "!")

def add(num1, num2):
    return num1 + num2

def halve(number):
    return number / 2