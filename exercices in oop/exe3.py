"""
3. Write a Python program to create a calculator class. Include methods for basic arithmetic operations.
"""

class Calculator:
    def __init__(self, a):
        self.number = a

    def add(self, b):
        return self.number + b
    def subtract(self, b):
        return self.number - b
    def multiply(self, b):
        return self.number * b
    def divide(self, b):
        return self.number / b


number_1 = Calculator(int(input("enter a number: ")))
number_2 = int(input("enter another number: "))

print(number_1.add(number_2))
print(number_1.subtract(number_2))
print(number_1.multiply(number_2))
print(number_1.divide(number_2))

