# Blind bid auction program
from auction_gavel_logo import logo
import os

def clear():
    os.system('cls||clear')

clear()
print("Welcome to the secret auction program.")
print(logo)

bids = {}
finished_bidding = False

def find_highest_bid(bidding_record):
    # bidding_record = {"name": bid, "name": bid}
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}.")

while not finished_bidding:
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $"))
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'.\n ").lower()
    if should_continue == "no":
        finished_bidding = True
        find_highest_bid(bids)
    elif should_continue == "yes":
        clear()
