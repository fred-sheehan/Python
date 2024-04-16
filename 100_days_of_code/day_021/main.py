# Pong Game
import time

from turtle import Screen
from scoreboard import Scoreboard
from paddle import Paddle
from ball import Ball


screen = Screen()
screen.setup(width=900, height=600)
screen.title("Pong Game")
screen.bgcolor("black")
screen.tracer(0)

scoreboard = Scoreboard()
scoreboard.update_score(0, 0)
scoreboard.centreline()

l_paddle = Paddle((-410, 0))
r_paddle = Paddle((410, 0))

ball = Ball()

screen.listen()
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

l_score = 0
r_score = 0
game_is_on = True

while game_is_on:
    scoreboard.centreline()
    time.sleep(0.05)
    screen.update()
    ball.move()

    # collisions with walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # collisions with paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 380 or ball.distance(l_paddle) < 50 and ball.xcor() < -380:
        ball.bounce_x()

    # ball out of bounds left
    if ball.xcor() > 460:
        l_score += 1
        ball.reset_position()

    # ball out of bounds right
    if ball.xcor() < -460:
        r_score += 1
        ball.reset_position()

    scoreboard.update_score(l_score, r_score)

    if l_score == 10 or r_score == 10:
        game_is_on = False
        scoreboard.game_over()


# close turtle screen
screen.exitonclick()
