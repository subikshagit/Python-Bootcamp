from turtle import Turtle

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]  

    def create_snake(self):
        pos_list = [(0, 0), (-20, 0), (-40, 0)]
        for i in range(3):
            self.add_segment(pos_list[i])

    def add_segment(self, position):
        tim = Turtle("square")
        tim.shape('square')
        tim.penup()
        tim.goto(position)
        tim.color('white')
        self.segments.append(tim)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for i in range(len(self.segments)-1,0,-1):
            new_x = self.segments[i-1].xcor()
            new_y = self.segments[i-1].ycor()
            self.segments[i].goto(new_x, new_y)
        self.segments[0].forward(20) 
    

    def reset(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]  


    def control_snake(self, direction):
        if direction == "up":
            if self.head.heading() != 270:  
                self.head.setheading(90)
        elif direction == "down":
            if self.head.heading() != 90:
                self.head.setheading(270)
        elif direction == "left":
            if self.head.heading() != 0:
                self.head.setheading(180)
        elif direction == "right":
            if self.head.heading() != 180:
                self.head.setheading(0)