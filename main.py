from turtle import Screen, Turtle
import time
from Snake import Snake
from Food import Food
from Wall import Wall

screen = Screen()
screen.setup(width=600, height=600)
# screen.bgpic('sun.gif')
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)
screen.listen()

game = True
snake = Snake()
food = Food()
wall = Wall()

speed = 0.11
score = 0

score_board = Turtle()
score_board.color("white")
score_board.penup()
score_board.goto(0, 250)
score_board.write(f'Score: {score}', align="center", font=("Arial", 24, "normal"))
score_board.hideturtle()

with open("high_score.txt", mode="r") as file:
    old_score = int(file.read())
hi_score = Turtle()
hi_score.color("white")
hi_score.penup()
hi_score.goto(0, -285)
hi_score.write(f'High Score: {old_score}', align="center", font=("Arial", 24, "normal"))
hi_score.hideturtle()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

def lost():
    loose = Turtle()
    loose.color("white")
    loose.penup()
    loose.goto(0, 0)
    loose.write(f'Game Over', align="center", font=("Arial", 24, "normal"))
    loose.hideturtle()

while game:
    screen.update()
    time.sleep(speed)
    snake.move()

    if snake.body[0].distance(food) < 15:
        snake.plus()
        food.refresh()
        speed -= 0.003
        score += 1
        score_board.clear()
        score_board.write(f'Score: {score}', align="center", font=("Arial", 24, "normal"))

    if snake.body[0].xcor() >= 285 or snake.body[0].xcor() <= -285:
        game = False
    if snake.body[0].ycor() >= 285 or snake.body[0].ycor() <= -285:
        game = False

    for i in range(2, len(snake.body)):
        if snake.body[0].distance(snake.body[i]) < 15:
            game = False

if old_score < score:
    with open("high_score.txt", "w") as file:
        file.write(f'{score}')
lost()

screen.exitonclick()

