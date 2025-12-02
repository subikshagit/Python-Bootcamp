import random

black=r"""
.------..------..------.     .------..------.
|A.--. ||K.--. ||Q.--. |     |J.--. ||10--. |
| (\/) || :/\: || :(): |     | :(): || :/\: |
| :\/: || :\/: || ()() |     | ()() || :\/: |
| '--'A|| '--'K|| '--'Q|     | '--'J|| '--'10|
`------'`------'`------'     `------'`-------'
     ____  _            _            _    
    | __ )| | __ _  ___| | _____  __| |___ 
    |  _ \| |/ _` |/ __| |/ / _ \/ _` / __|
    | |_) | | (_| | (__|   <  __/ (_| \__ \
    |____/|_|\__,_|\___|_|\_\___|\__,_|___/

             BLACKJACK TIME!
"""


def deal_cards():
     choose = [11,2,3,4,5,6,7,8,9,10,10,10,10]
     card = random.choice(choose)
     return card

def calculate_score(cards):
     if sum(cards) == 21 and len(cards) == 2:
          return 0
     if 11 in cards and sum(cards) > 21:
          cards.remove(11)
          cards.append(1)
          
     return sum(cards)

def compare(user_score,computer_score):
     if user_score == computer_score:
          return "match draw👍"
     elif computer_score == 0:
          return "Lose opponent has a black jack 🤷‍♂️"

     elif user_score == 0 :
          return "Win with a black jack😍"

     elif user_score >21:
          return "you lose 🤷‍♂️"

     elif computer_score >21:
          return "opponent went over  you win!😍"
     
     elif user_score > computer_score:
          return "you win😍"
     
     else:
          return "you lose🤷‍♂️"

user_card = []
computer_card = []

for _ in range(2):
     user_card.append(deal_cards())
     computer_card.append(deal_cards())

     


n = input("Do you want play a Blackjack game? Type 'y' or 'n'")
if n == 'y':
     print(black)


     Game_over = True
     while(Game_over):

          user_score = calculate_score(user_card)
          computer_score = calculate_score(computer_card)

          print(f"your cards {user_card} and the current score is {user_score}")
          print(f"computer first card is {computer_card[0]}")

          if user_score == 0 or computer_score == 0 or user_score >21:
               Game_over = False

          else:
               should_continue = input("Type 'y' to continue with another card or pass")
               if should_continue == 'y':
                    user_card.append(deal_cards())
                    
               else:
                    
                    Game_over = False
     while computer_score != 0 and computer_score <17:
          computer_card.append(deal_cards())
          computer_score = calculate_score(computer_card)
print(compare(user_score,computer_score))