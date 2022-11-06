import os
os.system("cls")


print("welcome to silent auction ;)")

silent_auction={}

bid_finish=False


def find_highest_bidder(auction_record):
    highest_bid=0
    winner=""
    for bidder in auction_record:
        bid_amount = auction_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of {highest_bid}")


while not bid_finish:
    name=input("Enter your name :")
    bid=int(input("Enter your bid $"))
    silent_auction[name]=bid
    should_continue=input("enter you would like to partispate in the auction type 'yes' or 'no' :")
        
    if should_continue =="no":
        bid_finish =True
        find_highest_bidder(silent_auction)
    elif should_continue=='yes':
        os.system("cls")


