"""
Step 3
"""

import random

word_list = ["aardvark", "baboon", "camel"]
# word_list = ["amor"]
chosen_word = random.choice(word_list)

# Testing code
print(f'Pssst, the solution is {chosen_word}.')

display = []
word_length = len(chosen_word)
for _ in range(word_length):
    display += "_"


while "".join(display) != chosen_word:

    guess = input("Guess a letter: ").lower()

    # check guess letter
    for position in range(word_length):  # iterate through the index
        letter = chosen_word[position]
        # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter
    print(display)
