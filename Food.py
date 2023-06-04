
from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()

        self.shape("circle")
        self.shapesize(1/2, 1/2)
        self.color("yellow")
        self.speed("fastest")
        self.penup()
        self.refresh()

    def refresh(self):
        self.penup()
        self.goto(random.randint(-280, 280), random.randint(-280, 280))
