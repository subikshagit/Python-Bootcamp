from turtle import Screen,Turtle
from paddle import Paddle
from balll import Ball
import time
from score import Score

screen = Screen()
screen.bgcolor("black") 
screen.setup(width=800, height=600)
screen.title("Pong Game")  
screen.tracer(0)

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))

balll = Ball()
score = Score()
screen.listen()

screen.onkey(r_paddle.go_up, "Up" )
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w" )
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(balll.move_speed)
    screen.update()
    balll.move()


    #detect the collision with the wall 
    if balll.ycor() > 280 or balll.ycor() < -280:
        #bounce 
        balll.bounce_y()

    #detect the collision with the paddle 
    if balll.distance(r_paddle) < 50 and balll.xcor() > 320 or balll.distance(l_paddle) < 50 and balll.xcor() < -320:
        balll.bounce_x()


    #x misses
    if balll.xcor() > 380:
        balll.reset_pos()
        score.l_point()

    if balll.xcor() < -380:
        balll.reset_pos()
        score.r_point()
        

screen.exitonclick()


