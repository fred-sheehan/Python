from turtle import Turtle, Screen, colormode, onclick, penup
from random import random, randint, choice

tim = Turtle()
screen = Screen()

colormode(255)

tim.shape("turtle")
tim.width(2)
tim.speed(0)

def my_canvas():
    screen.setup(width=1600, height=800)
    screen.bgcolor("black")

def random_color():
    r = randint(40, 255)
    g = randint(40, 255)
    b = randint(40, 255)
    tim.color((r, g, b))

def spirograph():
    for _ in range(0, 36):
        random_color()
        tim.circle(100)
        tim.right(10)

my_canvas()
spirograph()
screen.exitonclick()
