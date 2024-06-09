import os
from art import logo

print(logo)


def clear_screen():
    os.system('clear')


def find_highest_bidder(bidding_record):
    winner = ""
    highest_bidder = 0
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bidder:
            highest_bidder = bid_amount
            winner = bidder

    print(f'The winner is {winner} with a bid of ${highest_bidder}')


continue_bids = True
bids = {}

while continue_bids:
    name = input("What is your name? ")
    price = input("What is your bid? $")
    bids[name] = float(price)

    add_bids = input("Are there any other users who want to bid? [Y/N] ")

    if add_bids == 'Y':
        clear_screen()
    else:
        continue_bids = False
        find_highest_bidder(bids)
