# factorial
print("Please enter the number you want a factorial")
fact_num = int(input())
fact = 1
for i in range(1,fact_num+1):
    fact *= i
print(f"The factorial of the {fact_num} is {fact}.")