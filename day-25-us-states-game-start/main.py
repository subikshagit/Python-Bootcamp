import pandas as pd
import numpy as np
import turtle 

screen = turtle.Screen()
screen.title("US States Game!")
img = "blank_states_img.gif"
screen.addshape(img)
turtle.shape(img)


data = pd.read_csv("50_states.csv")
all_states = data.state.to_list()

while len(all_states) > 0:

    answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?").title()
    print(answer_state)

    if answer_state == 'Exit':
        break
    elif answer_state in all_states:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)


    screen.mainloop()