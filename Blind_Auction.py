logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''


from replit import clear
print(logo)

print("Welcome to the secret auction program")

auction = {
    
}

while True:
    name = input("What is your name: ")
    bid = input("What's your bid: $")

    auction[name] = int(bid)
    more = input("Are there any other bidder's: ").lower()
    if more == "yes":
        clear()
        continue
        
    elif more == "no":
        clear()
        break

highest_bid = 0
for bidder in auction:
    bid_amount = auction[bidder]
    if bid_amount > highest_bid: 
        highest_bid = bid_amount
    winner = bidder
print(f"The winner is {winner} with a bid of ${highest_bid}")
