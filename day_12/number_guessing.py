"""
Number guessing
"""
from art import logo
from random import randint, seed

# seed(25)

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


def level_of_difficulty():
    level = input("Choose a difficulty level, easy/hard: ").lower()
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


def check_answer(user_guess, computer_guess, attempts):
    if user_guess < computer_guess:
        print("Your guess is too low.")
        return attempts - 1
    elif user_guess > computer_guess:
        print("Your guess is too high.")
        return attempts - 1
    if user_guess == computer_guess:
        print(f"You got it right! The aswer was {computer_guess}")
        return None


def play_game():
    print(logo)
    print("Welcome to the game of Number Guessing!")
    print("I'm thinking of a number between 1 and 100.")
    number_guess = randint(1, 100)
    print(f"Psst, the correct answer is {number_guess}")

    turns = level_of_difficulty()

    while turns > 0:
        print(f"You have {turns} attempts to guess the number.")
        guess = int(input("Make a guess: "))
        turns = check_answer(guess, number_guess, turns)
        if turns == 0:
            print(f"You are out of attempts.")
            print("You lose the game!")
        elif turns is None:
            break
        else:
            print("Guess again.")


if __name__ == "__main__":
    play_game()
