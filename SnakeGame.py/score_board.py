
from turtle import Turtle
import os


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open(os.path.join(os.path.dirname(__file__), 'data.txt')) as data:
           self.highScore = int(data.read())
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.hideturtle()
        self.update_scoreboard()
        
    
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}  HighScore: {self.highScore}", align='center', font=("Arial", 24, "normal"))
        
    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.highScore:
            self.highScore = self.score
            with open(os.path.join(os.path.dirname(__file__), 'data.txt'),mode='w') as data:
               data.write(f"{self.highScore}")
        self.score = 0
        self.update_scoreboard()
