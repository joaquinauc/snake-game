import random
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food.
    if snake.head_of_snake.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect collision with wall.
    if snake.head_of_snake.xcor() > 280 or snake.head_of_snake.xcor() < -280 or snake.head_of_snake.ycor() > 280 or snake.head_of_snake.ycor() < -280:
        scoreboard.reset_highscore()
        snake.reset()

    # Detect collision with tail.
    for segment in snake.segments[1:]:  # Slicing the head of the snake.
        if snake.head_of_snake.distance(segment) < 15:
            scoreboard.reset_highscore()
            snake.reset()


screen.exitonclick()
