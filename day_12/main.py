"""
Scope: local vs global scope

enemies = 1


def increase_enemies():
    enemies_local = 2
    print(f"Enemies inside function: {enemies_local}")


increase_enemies()

print(f"Enemies outside function: {enemies}")

# Global scope
player_health = 100


# Local scope
def drink_potion():
    potion_strength = 5
    print(f"Player health: {player_health}")  # global
    print(f"Potion strength: {potion_strength}")


drink_potion()
# print(potion_strength)  # NameError: name 'potion_strength' is not defined


# Local scope
def game():
    def drink_potion_2():
        potion_strength = 5
        print(f"Player health: {player_health}")
        print(f"Potion strength: {potion_strength}")
    drink_potion_2()


drink_potion_2()


# Modify global scope
# bad practice to name global and local variables with same names

enemies = 1


def increase_enemies_global():
    global enemies  # to modify something global with in the local scope - BAD PRACTICE
    enemies += 1
    print(f"enemies inside function: {enemies}")


def increase_enemies_with_return():
    print(f"enemies inside function: {enemies}")
    return enemies + 1


print(f"enemies outside function: {enemies}")

increase_enemies_global()

enemies = increase_enemies_with_return()

print(f"enemies outside function: {enemies}")
"""

# Python constants and Global scope
# Global scopes

PI = 3.14159  # will never modify along code - capital letters
URL = "https://www.google.com/search?q="


