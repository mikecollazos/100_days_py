import os
from auction_art import logo


def find_highest_bidder(bids):
    highest_bid = 0
    winner = ""
    for bidder in bids:
        bid_amount = bids[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The Winner is {winner} with a bid of ${highest_bid}")
    


other_users = True
bids = {}
while other_users:
    os.system('cls' if os.name == 'nt' else 'clear')
    print(logo)
    name =      input("what is your name? :   ")
    bid_price = int(input("what is your bid?  :   "))
    bids[name] = bid_price
    other_bidders = input("Are there other bidder? yes/no : \n")
    #print(bids.values())
    if other_bidders.lower() == "no":
        find_highest_bidder(bids)
        # largest_value = max(bids.values())
        # largest_key = max(bids, key=bids.get)
        #print(f"The winning bid is {largest_value} and comes from {largest_key}")
        other_users=False
    

print(bids)