import turtle
import random

screen = turtle.Screen()
screen.bgcolor("lightblue")
screen.title("Turtle Race!")

finish_line = 200
line = turtle.Turtle()
line.penup()
line.goto(finish_line, 100)
line.right(90)
line.pendown()
line.forward(200)
line.hideturtle()

colors = ["red", "green", "blue", "orange", "purple"]
start_y = -100

racers = []
for i in range(5):
    t = turtle.Turtle()
    t.color(colors[i])
    t.shape("turtle")
    t.penup()
    t.goto(-200, start_y + i * 50)
    t.pendown()
    racers.append(t)

winner = None
while not winner:
    for t in racers:
        move = random.randint(1, 5)
        t.forward(move)
        if t.xcor() >= finish_line:
            winner = t
            break

winner_name = winner.color()[0]
print(f"The winner is: {winner_name} turtle!")

turtle.done()
