import time
from turtle import Screen   
from snake import Snake
from food import Food
from score_board import ScoreBoard

s = Screen()
s.bgcolor(0, 0, 0)
s.setup(width=600, height=600)
s.title("Snake Game")
s.tracer(0)  # Turn off the screen updates for performance

snake= Snake()
food = Food()
score_board = ScoreBoard()

s.listen()
s.onkey(lambda:snake.control_snake("up"), "Up")
s.onkey(lambda:snake.control_snake("down"), "Down")
s.onkey(lambda:snake.control_snake("left"), "Left")
s.onkey(lambda:snake.control_snake("right"), "Right")


game_is_on = True
while game_is_on:
    s.update()  
    time.sleep(0.1)  
    snake.move()  
    
    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score_board.increase_score()
    # Detect collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        score_board.reset()
        snake.reset()

    # Detect collision with tail
    for segment in snake.segments:
        if segment != snake.head:
            if snake.head.distance(segment) < 10:
                score_board.reset()
                snake.reset()

        
s.exitonclick()  # Wait for a click to close the window
