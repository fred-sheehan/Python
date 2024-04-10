from turtle import Turtle, Screen, colormode
from random import randint

t = Turtle()
colormode(255)
t.speed(0)
t.width(1)

my_screen = Screen()
my_screen.title("Random Color Spiral")
my_screen.bgcolor("black")
my_screen.setup(width=1600, height=900)


def draw_spiral(starting_radius, loops):
    for i in range(0, loops):
        t.pencolor(randint(0,255),randint(0,255),randint(0,255))
        t.circle(starting_radius + i, 60)

draw_spiral(5, 500)
