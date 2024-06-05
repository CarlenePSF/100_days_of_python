"""
Functions with inputs
Arguments with parameters

defining functions

def main():
    # do something
    # Then do this
    # finally do that
"""

# Review:
# Create a function called greet().
# Write 3 print statements inside the function.
# Call the greet() function and run your code.


def greet():
    print("Hello World!")
    print("Hello Again")
    print("Bye!")


# Function that allows for input
def greet_with_name(name):
    print(f"Hello, {name}!")
    print("Hello Again")
    print("Bye!")


# Function with more than 1 input
def greet_with_name_location(name, location):
    print(f"Hello, {name}!")
    print(f"What is it that like in {location}?")


greet()
greet_with_name("Angela")
greet_with_name_location("Angela", "England")

# with kyeword arguments avoids change in parameters
greet_with_name_location(location="England", name="Angela")