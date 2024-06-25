from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo
print(logo)
bide={}
bidding_finished =False
def highest_bidder(bidding_record):
  highest_bid = 0
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount> highest_bid:
      highest_bid = bid_amount
      winner =bidder
  print(f"the winner is {winner} with a bid of {highest_bid}")  

while not bidding_finished:
  name = input("what is your name?")
  bid =int(input("what is your bid?"))
  bide[name]=bid
  should_continue = input("are there any other bidders? type 'yes' or 'no'")
  if should_continue == "no":
    bidding_finished = True
    highest_bidder(bide)
  elif should_continue == "yes":
    clear()
