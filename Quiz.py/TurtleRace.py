from turtle import Turtle, Screen
import random
s = Screen()
s.setup(width=500, height=400)
textInput = s.textinput(title="Your Bet", prompt="Which turtle will win? Enter a color:")
print(textInput)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_pos = [-70, -40, -10, 20, 50, 80]
for_pos = random.randint(1,100)
all_turtle = []

is_on = False
for i in range(6):
    tim1 = Turtle(shape="turtle")    
    tim1.color(colors[i])
    tim1.penup()
    tim1.goto(-230,y_pos[i])
    all_turtle.append(tim1)
if textInput :
    is_on = True
while is_on:
    for turtle in all_turtle:
        if turtle.xcor() > 230:
            is_on = False
            winning_color = turtle.pencolor()
            if winning_color == textInput:
                print(f"You've won! The {winning_color} turtle is the winner!") 
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

s.exitonclick()