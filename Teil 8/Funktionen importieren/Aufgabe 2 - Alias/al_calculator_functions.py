import math

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

def power(a, b):
    return a ** b

def sqrt(a):
    if a < 0:
        return "Error: Negative root"
    return math.sqrt(a)

def factorial(a):
    if a < 0:
        return "Error: Factorial of negative number"
    return math.factorial(a)
