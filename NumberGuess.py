import random
num_pic = r"""
  _   _                 _                        _____                      
 | \ | |               | |                      / ____|                     
 |  \| | ___  _   _  __| | ___  _ __ ___   ___ | |  __  __ _ _ __ ___   ___ 
 | . ` |/ _ \| | | |/ _` |/ _ \| '_ ` _ \ / _ \| | |_ |/ _` | '_ ` _ \ / _ \
 | |\  | (_) | |_| | (_| | (_) | | | | | |  __/| |__| | (_| | | | | | |  __/
 |_| \_|\___/ \__,_|\__,_|\___/|_| |_| |_|\___| \_____|\__,_|_| |_| |_|\___|
                                                                            

"""
is_over =True
answer =random.randint(1,10000)
def guess_number(level,easy,hard):
        global is_over
        global answer
        while(is_over):
            if difficult == "easy":
                print(f"you have a {easy} attemps remaining guess")
                easy -= 1
            else:
                print(f"you have a {hard} attemps remaining")
                hard -= 1
            
            guess = int(input("Make a guess:" ))
            if guess == answer:
                print(f"yeah..! you got it! The answer was {answer}")
                is_over = False
            elif guess < answer:
                print("Too low \n guess again!")
            elif guess >answer:
                print("Too high")
            else:
                print("you enter a invalid input? please checkit out")
                is_over = False

print(num_pic)
print ("Welcome to the Number guessig Game!😍")
print ('I am thinking the number between 1 to 100.')
difficult = input("choose the difficulty level. Type ' hard' or ' easy' ").lower()
easy = 10
hard = 5
guess_number(difficult,easy,hard)
