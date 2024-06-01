"""
Coin toss program
"""
import random

randon_number = random.randint(0, 1)

if randon_number == 0:
    print("Tails")
else:
    print("Heads")
