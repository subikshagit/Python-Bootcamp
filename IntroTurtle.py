from turtle import Turtle

t = Turtle()
is_True = True
c=0
while is_True:
    for i in ('red','green','pink','black'):
        t.color(i)
        t.pendown()
        t.dot()
        t.filling()
        t.forward(100)
        t.right(100)
        t.begin_fill()
        t.stamp()

        c+=1
        if c == 20:
            is_True = False