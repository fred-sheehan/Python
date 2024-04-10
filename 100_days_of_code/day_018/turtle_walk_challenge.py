from turtle import Turtle, Screen, colormode, onclick
from random import random, randint, choice

tim = Turtle()
screen = Screen()

colormode(255)

tim.shape("turtle")
tim.width(10)
tim.speed(0)

def my_canvas():
    screen.setup(width=1600, height=900)
    screen.bgcolor("black")

def random_color():
    r = randint(40, 255)
    g = randint(40, 255)
    b = randint(40, 255)
    tim.color((r, g, b))

def random_walk():
    for _ in range(0, 300):
        random_color()
        tim.setheading(choice([0, 90, 180, 270]))
        tim.forward(50)

my_canvas()
random_walk()
screen.exitonclick()
