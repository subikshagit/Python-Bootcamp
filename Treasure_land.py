print('''
      *******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************''')
print("Wecome to the Treasure Island.")
print("our mission is to find a treasure.")

direction = input(f"You're at a cross road.where do you want to go?\n  Type {"left"} or {"right"} \n")
if direction == "right":
    print("you fell to a hole! Game over")

elif direction == "left":
    option = input("you want to swim or wait \n     Type swim or wait\n").lower()

    if option == "swim":
        print("you fell to the sea.Game over!")

    elif option == "wait":
        ask = input("Which door you want?\n Type red blue or yellow\n").lower()

        if ask == "red" or ask == "blue":
            print("Sorry game over!")

        elif ask == "yellow":
            print("wow! you won the Game!")

        else:
            print("you enter the invalid input.please check")

    else:
        print("you enter the invalid input please check!")
        
else:
    print("you enter a invalid input so please enter the valid input and check the error:")