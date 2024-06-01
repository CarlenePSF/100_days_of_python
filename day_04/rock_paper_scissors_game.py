import random

print("Welcome to rock paper scissors!")

player_choice = input("Player choice: rock, paper, scissors? ")
computer_choice = random.choice(["rock", "paper", "scissors"])

if player_choice == computer_choice:
    print("It's a tie!")
if player_choice == "rock" and computer_choice == "scissors":
    print(f"Computer choice is {computer_choice}. You win!")
if player_choice == "rock" and computer_choice == "paper":
    print(f"Computer choice is {computer_choice}. You lose!")
if player_choice == "paper" and computer_choice == "rock":
    print(f"Computer choice is {computer_choice}. You win!")
if player_choice == "paper" and computer_choice == "scissors":
    print(f"Computer choice is {computer_choice}.You lose!")
if player_choice == "scissors" and computer_choice == "paper":
    print(f"Computer choice is {computer_choice}.You win!")
if player_choice == "scissors" and computer_choice == "rock":
    print(f"Computer choice is {computer_choice}.You lose!")
