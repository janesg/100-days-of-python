import os
import platform

print("Welcome to the Secret Auction for a mystery item!")

bids = []
bids_finished = False
largest_bid = 0.0
highest_bidder = {}

while not bids_finished:
    name = input("Enter you name : ")
    bid = float(input("Enter your bid : "))

    bids.append({
        "name": name,
        "bid": bid
    })

    bids_finished = bool(input("Are there more users that want to bid ? (y)es or (n)o :").lower().startswith("n"))
    os.system("cls" if platform.system() == 'Windows' else "clear")

for bid in bids:
    if bid["bid"] > largest_bid:
        largest_bid = bid["bid"]
        winning_bid = bid

print(f"The auction for the mysterious item was won by {winning_bid["name"]} with a bid of {winning_bid["bid"]}")
