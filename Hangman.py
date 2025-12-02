import random

hangman_stages = [
''' 
+--+
|  |
 O |
/|\|
/ \|
   |
=====
''',
''' 
+--+
|  |
 O |
/|\|
/  |
   |
=====
''',
''' 
+--+
|  |
 O |
/|\|
   |
   |
=====
''',
''' 
+--+
|  |
 O |
/| |
   |
   |
=====
''',
''' 
+--+
|  |
 O |
 | |
   |
   |
=====
''',
''' 
+--+
|  |
 O |
   |
   |
   |
=====
''',
''' 
+--+
|  |
   |
   |
   |
   |
=====
'''
]


print(
    '''                                           
        | |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
        | '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
        | | | | (_| | | | | (_| | | | | | | (_| | | | |
        |_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                            __/ |                      
                            |___/                       
''')

lives = 0
my_list=['apple', 'banana', 'cat', 'dog', 'elephant', 'flower', 'grape', 'house', 'ice', 'jungle',
 'kite', 'lemon', 'moon', 'notebook', 'orange', 'pencil', 'queen', 'rain', 'sun', 'tree',
 'umbrella', 'violin', 'whale', 'xylophone', 'yarn', 'zebra']

guess_word = random.choice(my_list)
print(guess_word)

word =''
for i in range(len(guess_word)):
    word += '_'
print("Word to guess:",word)

lives = 6
game_over = True
correct_letter = []

while game_over:

    display=''
    guess_letter = input("guess a letter:\n")

    for i in guess_word:
        if i == guess_letter:
            display += guess_letter
            correct_letter.append(guess_letter)

        elif i in correct_letter:
            display += i

        else:
            display += '_'
            
    print(display)
    
    if guess_letter not in guess_word:
        lives -= 1
        print(hangman_stages[lives])

        if lives == 0:
            game_over = False
            print("you lose!")
            
    if '_' not in display:
        game_over = False
        print("you win!")



    