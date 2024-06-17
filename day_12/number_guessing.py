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


def check_answer(user_guess, computer_guess, turns):
    if user_guess < computer_guess:
        print("Too low.")
        return turns - 1
    elif user_guess > computer_guess:
        print("Too high.")
        return turns - 1
    if user_guess == computer_guess:
        print(f"You got it right! The aswer was {computer_guess}")



def play_game():
    print(logo)

    print("Welcome to the game of Number Guessing!")
    print("I'm thinking of a number between 1 and 100.")
    answer = randint(1, 100)
    print(f"The correct answer is {answer}")

    turns = level_of_difficulty()
    guess = 0

    while guess != answer:
        print(f"You have {turns} attempts to guess the number.")
        guess = int(input("Make a guess: "))
        turns = check_answer(guess, answer, turns)

        if turns == 0:
            print("You've run out of guesses, you lose.")
            return
        elif guess != answer:
            print("Guess again.")


if __name__ == "__main__":
    play_game()
