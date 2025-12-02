print("Welcome to the Tip calculator!")
print("what was the total bill?")

bill = eval(input())
print(f"${bill}")

print("how much tip would you like to  give ?10,12,15?")
tip = int(input())
print(tip)

print("how many people to split the bill?")
split = int(input())
print(split)

total_bill = (bill *(tip/100)+bill)


print(f"Each persoon should pay:${round((total_bill/split),2)}")
