import random

d = {
    0:"""
        _______
    ---'   ____)
        (_____)
        (_____)
        (____)
    ---.__(___)
    """,

    1:"""
            _______
        ---'    ____)
                ______)
                _______)
                _______)
        ---.__________)
        """,

    2:
        """
            _______
        ---'   ____)____
                ______)
            __________)
            (____)
        ---.__(___)
        """
}
user_count = 0
computer_count = 0
run = True
while(run):
    run += 1
    if run > 3:
        run = False
    print("what do you choose? type 0 for rock,1 for scissors and 2 for paper\n")
    user_choice =int(input())
    if 0 <= user_choice <= 2 :
        print(d[user_choice])

        computer_choice = random.randint(0,1)
        print(f"The computer choses {computer_choice}")
        print(d[computer_choice])

        if user_choice == computer_choice:
            print("match draw")
            user_count += 1
            computer_count += 1

        elif user_choice < computer_choice:

            if user_choice == 0 and computer_choice == 2:
                print("you win!")
                user_count += 1

            else:
                print("computer wins!")
                print("you lose")
                computer_count += 1

        elif user_choice > computer_choice:

            if computer_choice == 0 and user_choice == 2:
                print("computer wins!\n you lose?")
                computer_count += 1

            else:
                print("you win!\n computer lose!")
                user_count += 1
    
    else:
        print("you enter a invaid input")
