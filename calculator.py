print(
  '''       _            _       _             
          | |          | |     | |            
  ___ __ _| | ___ _   _| | __ _| |_ ___  _ __ 
 / __/ _` | |/ __| | | | |/ _` | __/ _ \| '__|
| (_| (_| | | (__| |_| | | (_| | || (_) | |   
 \___\__,_|_|\___|\__,_|_|\__,_|\__\___/|_|   
                                    '''
 )
print(
    '''
    ____________________
    |  _________________  |
    | | JO           0. | |
    | |_________________| |
    |  ___ ___ ___   ___  |
    | | 7 | 8 | 9 | | + | |
    | |___|___|___| |___| |
    | | 4 | 5 | 6 | | - | |
    | |___|___|___| |___| |
    | | 1 | 2 | 3 | | x | |
    | |___|___|___| |___| |
    | | . | 0 | = | | / | |
    | |___|___|___| |___| |
    |_____________________|
'''
)
first_number = eval(input("what is the first number?: "))
is_continue = True
while is_continue:
    print("+" "\n" "-" "\n" "*" "\n" "/" "\n" )
    operation = input("pick an operation:")
    num2 = eval(input("What is the second number?: "))
    if operation == '+':
        result = first_number + num2 
    elif operation == '-':
        result = first_number - num2
    elif operation == "*":
        result = first_number * num2
    elif operation == "/":
        result = first_number / num2
    else:
        print("you enter a invalid operation")
    print(f"{first_number} {operation} {num2} = ",result)

    should_continue = input("Type 'y' to continue with the result ,or Type 'n' to start a  new calculation\n")
    if should_continue == 'y':
        first_number = result
    elif should_continue =='n':
        is_continue = False
    else:
        print("invalid input")