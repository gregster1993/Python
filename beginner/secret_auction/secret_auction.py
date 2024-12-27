from art import logo

print(logo)

#import art
#print(art.logo)

bids = {}
bidding_finished = False

def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""

    max(bidding_record)

    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            winner = bidder
            highest_bid = bid_amount
    print(f"The winner is {winner} with a bid of ${highest_bid}")

while not bidding_finished:
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $"))
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'yes or no'. \n").lower()
    if should_continue == "no":
        bidding_finished = True
        find_highest_bidder(bids)
    else:
        print("\n" * 100)