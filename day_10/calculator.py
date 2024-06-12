import os
from art import logo


def clear_screen():
    os.system('clear')


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calculator():
    print(logo)

    num1 = float(input("Enter first number: "))
    for key in operations:
        print(key)
    should_continue = True

    while should_continue:
        symbol_operation = input("Enter a symbol operation from above: ")
        operation = operations[symbol_operation]
        num2 = float(input("Enter the next number: "))
        result = operation(num1, num2)

        print(f"{num1} {symbol_operation} {num2} = {result}")

        if input(f"Type 'y' to continue calculation with {result}, or type 'n' to start a new calculation: ") == "y":
            num1 = result
        else:
            should_continue = False


run_calculator = True
while run_calculator:
    calculator()
    if input("Clear (y/n)? ").lower() == "y":
        clear_screen()
    else:
        run_calculator = False
