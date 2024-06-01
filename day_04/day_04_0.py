"""
Randomisation and Python lists
https://www.khanacademy.org/computing/computer-science/cryptography/crypt/v/random-vs-pseudorandom-number-generators

https://docs.python.org/3/tutorial/controlflow.html
-------------

import random

random.seed()

print(random.random())  # generates a random number between 0 and 1
print(random.randint(0, 10))  # generates a integer random number in a given interval

# expand the range generating random number between 0 and (4.99999...) 5 - not included.
print(random.random() * 5)
"""
# Python lists - data structure That belongs to the same category or data type

states_of_america = [
    "Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut",
    "Massachusetts", "Maryland", "South Carolina", "New Hampshire",
    "Virginia", "New Jersey", "North Carolina", "Rhode Island", "Vermont",
    "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi",
    "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan",
    "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota",
    "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado",
    "North Dakota", "South Dakota", "Montana", "Washington", "Idaho",
    "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska",
    "Hawaii"]

# # change a single item by indexing
# states_of_america[1] = "Pencilvania"
# print(states_of_america[1])
# print(states_of_america)
#
# # add an item at the end of the list
# states_of_america.append("AngelaLand")
# print(states_of_america)
#
# # extending the list
# states_of_america.extend(["Brasil", "Mexico"])
# print(states_of_america)

# print(states_of_america[50])  # IndexError: list index out of range
# print(states_of_america)


dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples",
               "Grapes", "Peaches", "Cherries", "Pears", "Tomatoes",
               "Celery", "Potatoes"]
print(dirty_dozen)
# nested list
fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears",]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirty_dozen = [fruits, vegetables]
print(dirty_dozen)

print(dirty_dozen[0])
print(dirty_dozen[1])

print(dirty_dozen[1][1])