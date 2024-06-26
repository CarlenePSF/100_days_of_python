# Todo 1- import and  add logos
# Todo 2 - print the information and ask the user for an input answer
# Todo 3 - If user is right, count one point, else end of the game print message

import random
import os
from art import logo, vs
from game_data import data


def clear():
    os.system('clear')


def choose_data():
    index = random.randint(0, len(data) - 1)
    return data[index]['name'], data[index]['description'], data[index]['country'], data[index]['follower_count']


def compare_coice(user_input, default, score):
    if user_input >= default:
        print("You're right! Current score:", score+1)
        return score + 1, False
    else:
        print(f"Sorry, that's wrong. Final Score:", score)
        return score, True


def play_higher_lower_game():
    print(logo)

    end_game = False
    user_score = 0

    while not end_game:
        name_a, description_a, country_a, num_followers_a = choose_data()
        name_b, description_b, country_b, num_followers_b = choose_data()

        print(f'Compare A: {name_a}, {description_a}, from {country_a}.')
        print(vs)
        print(f'Compare B:  {name_b}, {description_b}, from {country_b}.')
        user_guess = input('Who has more followers? Type "A" or "B": ').lower()

        if user_guess == 'a':
            user_score, end_game = compare_coice(num_followers_a, num_followers_b, user_score)
        else:
            user_score, end_game = compare_coice(num_followers_b, num_followers_a, user_score)


if __name__ == '__main__':
    play_higher_lower_game()
