import turtle
from turtle import Turtle

STEPS = 20

class Snake:
    def __init__(self):
        self.body = []
        self.create()

    def create(self):
        for i in range(3):
            part = Turtle("square")
            if i == 0:
                part.color("#d580ff")
            else:
                part.color("#ff1aff")
            part.penup()
            part.goto(-10 + (-20 * i), 10)
            self.body.append(part)

    def move(self):
        for seg in range(len(self.body) - 1, 0, -1):
            newx = self.body[seg - 1].xcor()
            newy = self.body[seg - 1].ycor()
            self.body[seg].goto(newx, newy)
        self.body[0].forward(STEPS)

    def up(self):
        if self.body[0].heading() == 0:
            self.body[0].left(90)
        if self.body[0].heading() == 180:
            self.body[0].right(90)

    def down(self):
        if self.body[0].heading() == 0:
            self.body[0].right(90)
        if self.body[0].heading() == 180:
            self.body[0].left(90)

    def right(self):
        if self.body[0].heading() == 90:
            self.body[0].right(90)
        if self.body[0].heading() == 270:
            self.body[0].left(90)

    def left(self):
        if self.body[0].heading() == 90:
            self.body[0].left(90)
        if self.body[0].heading() == 270:
            self.body[0].right(90)

    def plus(self):
        part = Turtle("square")
        part.penup()
        part.setpos(self.body[-1].xcor(), self.body[-1].ycor())
        part.color("#ff1aff")
        self.body.append(part)