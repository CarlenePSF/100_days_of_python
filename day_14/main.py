# Todo 1- import and  add logos
# Todo 2 - print the information and ask the user for an input answer
# Todo 3 - If user is right, count one point, else end of the game print message

import random
from art import logo, vs
from game_data import data

print(logo)

end_game = False
score = 0

while not end_game:
    index_a = random.randint(0, len(data) - 1)
    index_b = random.randint(0, len(data) - 1)

    name_a = data[index_a]['name']
    description_a = data[index_a]['description']
    country_a = data[index_a]['country']
    num_followers_a = data[index_a]['follower_count']

    name_b = data[index_b]['name']
    description_b = data[index_b]['description']
    country_b = data[index_b]['country']
    num_followers_b = data[index_b]['follower_count']

    print(f'Compare A: {name_a}, {description_a}, from {country_a}.')
    print(vs)
    print(f'Compare B:  {name_b}, {description_b}, from {country_b}.')
    user_guess = input('Who has more followers? Type "A" or "B": ').lower()

    if user_guess == 'a':
        if num_followers_a >= num_followers_b:
            score += 1
            print("You're right! Current score:", score)
        else:
            end_game = True
            print(f"Sorry, that's wrong. Final Score:", score)
    else:
        if num_followers_b >= num_followers_a:
            score += 1
            print("You're right! Current score:", score)
        else:
            end_game = True
            print(f"Sorry, that's wrong. Final Score:", score)
