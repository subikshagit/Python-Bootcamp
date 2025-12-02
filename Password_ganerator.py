import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbol = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+','[', ']', '{', '}', '\\', '|', ';', ':', '\'', '"', ',', '.', '<', '>', '/', '?', '`', '~']

print("Welcome to my password Generator!")

print("how many letters do you want to add?")
letter_count = int(input())

print("how many numbers do you want to add?")
numbers_count = int(input())

print("how many symbols do you want to add?")
symbols_count = int (input())


password =[]

for j in range(letter_count):
    password.append(random.choice(letters))

for k in range(numbers_count):
    password.append(random.choice(numbers))

for l in range(symbols_count):
    password.append(random.choice(symbol))

random.shuffle(password)
print(*password,sep='')