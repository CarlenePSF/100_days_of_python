"""
Debugging
"""

"""
# Describe Problem
def my_function():
    for i in range(1, 20):  # Range is not right-included
        # print(i)
        if i == 20:  # This block is never executed because the condition is never satisfied
            print("You got it")
"""


# def my_function():
#     """
#     Refactoring the function above
#     :return:
#     """
#     for i in range(1, 21):  # Include 20
#         # print(i)  # Print to check the values
#         if i == 20:  # This block is never executed because the condition is never satisfied
#             print("You got it")
#
#
# my_function()

"""
#  Reproduce the Bug
It will print the element from the index generetaded by rand module but the interval is incorrect, 
because collections in python are indexed starting from 0. The error message: IndexError: list index out of range

The solution is define an interval from 0 to 5
"""
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# # dice_num = randint(1, 6)
# dice_num = randint(0, 5)
# print(dice_num)
# print(dice_imgs[dice_num])

"""
# Play Computer
"""
# year = int(input("What's your year of birth?"))
# if 1980 < year < 1994:
#     print("You are a millenial.")
# elif year >= 1994:  # To include the eyar 1994 use >=
#     print("You are a Gen Z.")

"""
# Fix the Errors

age = input("How old are you?")
if age > 18:
print("You can drive at age {age}.")
"""

# age = int(input("How old are you?"))
# if age > 18:
#     print(f"You can drive at age {age}.")


"""
# Print is Your Friend
the bug is in using == when asking the user an input
"""

# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page = int(input("Number of words per page: "))
#
# total_words = pages * word_per_page
# print(total_words)

"""
# Use a Debugger
"""


def mutate(a_list):
    b_list = []
    for item in a_list:
        new_item = item * 2
        b_list.append(new_item)  # Identation
    print(b_list)


mutate([1, 2, 3, 5, 8, 13])
