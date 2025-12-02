def adventure_game():
    playing = True
    current_location = "start"  # Initial location

    while playing:
        if current_location == "start":
            print("You find yourself at the entrance of a dark cave.")
            choice = input("Do you go 'inside' or 'run away'? ").lower()
            if choice == "inside":
                current_location = "cave"
            elif choice == "run away":
                print("You run away to safety. Game over.")
                playing = False
            else:
                print("Invalid choice. Try again.")

        elif current_location == "cave":
            print("You are in a dimly lit cave. You see two paths.")
            choice = input("Do you go 'left' or 'right'? ").lower()
            if choice == "left":
                current_location = "treasure"
            elif choice == "right":
                current_location = "monster"
            else:
                print("Invalid choice. Try again.")

        elif current_location == "treasure":
            print("You found the treasure! You win!")
            playing = False

        elif current_location == "monster":
            print("A monster attacks you! Game over.")
            playing = False

        else:
            print("Error: Invalid location.")
            playing = False

    print("Thank you for playing!")

adventure_game()