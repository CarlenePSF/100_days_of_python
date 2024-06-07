"""
You are going to write a program that adds to a travel_log.
You can see a travel_log which is a List that contains 2 Dictionaries.
Your job is to create a function that can add new countries to this list.

Write a function that will work with the following line of code
on line 21 to add the entry for Brazil to the travel_log.

add_new_country("Brazil", 5, ["São Paulo", "Rio de Janeiro"])

DO NOT modify the travel_log directly. The goal is to create a function that modifies it.

- Example Input
Brazil
5
["São Paulo", "Rio de Janeiro"]

- Example Output
I've been to Brazil 5 times.
My favourite city was São Paulo.

"""
# TODO: Write the function that will allow new countries
# to be added to the travel_log.


def add_new_country(name, times_visits, cities_visited):
    add_dict = {
        "country": name,
        "visits": times_visits,
        "cities": cities_visited
    }
    travel_log.append(add_dict)


travel_log = [
  {
    "country": "France",
    "visits": 12,
    "cities": ["Paris", "Lille", "Dijon"]
  },
  {
    "country": "Germany",
    "visits": 5,
    "cities": ["Berlin", "Hamburg", "Stuttgart"]
  },
]


add = True


while add:
    country = input("Add country name: ")
    visits = int(input("Number of visits: "))
    list_of_cities = eval(input("Which cities did you visited: "))

    add_new_country(country, visits, list_of_cities)
    print(f"I've been to {travel_log[-1]['country']} {travel_log[-1]['visits']} times.")
    print(f"My favourite city was {travel_log[-1]['cities'][0]}.")

    to_continue = input("Would you like to add another country? [Y/N]")
    if to_continue == "N":
        add = False
