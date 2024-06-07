"""
# Dictionary


programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
    "Loop": "The action of doing something over and over again."
}

# print the complete dictionary
print(programming_dictionary)

# print itens by key
print(programming_dictionary["Bug"])
print(programming_dictionary["Function"])
print(programming_dictionary["Loop"])

# adding itens to the dictionary

programming_dictionary["Dictionary"] = (
    "Dictionaries are used to store data values in 'key:value' pairs."
    "A dictionary is a collection which is ordered*, changeable and do not allow duplicates.")

# print(programming_dictionary)
# print(programming_dictionary["Dictionary"])

# empty dictionary
empty_dictionary = {}

# Wipe an existing dictionary - to clear out users inputs
# programming_dictionary = {}
# print(programming_dictionary)

# Editing an item in a dictionary
# programming_dictionary["Bug"] = "A moth in your computer."

# print(programming_dictionary)

# loop through dictionary

for key in programming_dictionary:
    # print keys
    print(key)
    print(programming_dictionary[key])
"""

# Nesting dictionary in a dictionary

travel_log = {
    "France": {
        "cities_visited": ["Paris", "Bordeaux", "Toulouse"],
        "total_visits": 1,
    },
    "Netherlands": {
        "cities_visited": ["Amsterdam", "Utrecht", "Dalfsen", "Zwolle"],
        "total_visits": 2,
    }
}
print(travel_log["France"])
print(travel_log["France"]["cities_visited"])
print(travel_log["France"]["total_visits"])


# a dictionary inside a list
travel_log = [
    {"Country": "France",
     "cities_visited": ["Paris", "Bordeaux", "Toulouse"],
     "total_visits": 1,
     },
    {"Country": "Netherlands",
     "cities_visited": ["Amsterdam", "Utrecht", "Dalfsen", "Zwolle"],
     "total_visits": 2,
     }
]

print(travel_log[0]["Country"])
print(travel_log[0]["cities_visited"])
print(travel_log[0]["total_visits"])
