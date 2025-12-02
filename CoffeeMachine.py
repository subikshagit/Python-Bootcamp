MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
resourses = {
    "water" : 300,
    "milk" : 200,
    "coffee":100,
}


def is_sufficient(ingre):
    for item in ingre:
        if ingre[item] >= resourses[item]:
            print(f"Sorry there is not enough for the {item}")
            return False
    return True



def process_coins():
    print("please insert the coins!")
    total = int(input("how many quaters?" ))*0.25
    total += int(input("how many dimes?" ))*0.1
    total += int(input("how many nickel?" ))*0.05
    total += int(input("how many pennie?" ))*0.01
    return total



    
def payment(pay,money):
    if money >= pay:
        global profit
        profit += money
        return True
    else:
        print("your money is not sufficient for the payment!")
        return False


def make_coffee(choice,ingredient,change):
    for item in ingredient:
        resourses[item] -= ingredient[item]
    print(f"your coffeee {choice} is readyyyy...just taste it!☕🍵")
    print(f"Here is the change... for youuu{change}")

is_True = True
profit = 0
while is_True:
    choice = input("what would you like? (expresso/latte/cappuciano)?").lower()

    if choice == 'off':
        is_True = False

    elif choice == 'report':
       print(f"water : {resourses['water']}ml")
       print(f"milk : {resourses['milk']}ml")
       print(f"coffee :{resourses['coffee']}g")
       print("money =${profit}")


    else:
        drink = MENU[choice]
        if is_sufficient(drink['ingredients']):
            pay = process_coins()
            if payment(pay,drink["cost"]):
                change = round(pay-drink["cost"],2)
                make_coffee(choice,drink['ingredients'],change)
               