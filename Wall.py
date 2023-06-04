
from turtle import Turtle

CORDINATES = [(-295, 0), (295, 0), (0, 295), (0, -295)]

class Wall:
    def __init__(self):
        self.create()

    def create(self):
        for i in range (4):
            wall = Turtle()
            wall.shape("square")
            if i < 2:
                wall.shapesize(60, 1)
            else:
                wall.shapesize(1, 60)
            wall.color("red")
            wall.speed("fastest")
            wall.penup()
            wall.goto(CORDINATES[i][0], CORDINATES[i][1])
