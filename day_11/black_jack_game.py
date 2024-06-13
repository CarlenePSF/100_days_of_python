import random
import os
from art import logo


def clear():
    os.system('clear')


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


def calculate_score(hand):
    if len(hand) == 2 and sum(hand) == 21:
        return 0
    if 11 in hand and sum(hand) > 21:
        hand.remove(11)
        hand.append(1)
    return sum(hand)


def compare_score(player_score, opponent_score):
    if player_score == opponent_score:
        return "Draw."
    elif opponent_score == 0:
        return "Lose, opponent has a Blackjack."
    elif player_score == 0:
        return "Win with a Blackjack!"
    elif player_score > 21:
        return "You went over. You lose!"
    elif opponent_score > 21:
        return "Opponent went over. You win!"
    elif player_score > opponent_score:
        return "You win!"
    else:
        return "You lose!"


def play_game():
    print(logo)

    user_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(user_cards, computer_cards)

        print(f"Your cards: {user_cards}, and your score {user_score}.")
        print(f"Computer's firts card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal.lower() == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare_score(user_score, computer_score))


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    clear()
    play_game()
