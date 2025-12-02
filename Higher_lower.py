print(
  '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\
                         `'-------'`
                       .-------------.
                   jgs/_______________\ '''
 )

def highest_bidder(bids):
    higher = 0
    winner = ""
    for i in bids:
        bid_amount = bids[i]
        if bid_amount > higher:
            higher = bid_amount
            winner = i
    print(f"the winner is {winner} and the highest bidder is {higher}")


dictionary = {}
auction_continue= True
while auction_continue:
    name = input("What is your name?\n")
    bid = int(input("what is your bid?"))
    dictionary[name] = bid 
    should_continue = input("Are you have any other bids? if you should continue 'yes' else 'no'")

    if should_continue == 'yes':
        print("\n"*100)
    elif should_continue == 'no':
        auction_continue = False
    
print(dictionary)
highest_bidder(dictionary)
print(max(dictionary, key = dictionary.get))
