from turtle import Turtle, Screen, colormode
from random import random, randint

tim = Turtle()
screen = Screen()

colormode(255)

tim.shape("turtle")

def my_canvas():
    screen.setup(width=1600, height=800)
    screen.bgcolor("black")

def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)

def change_random_color():
    tim.color((randint(40, 255), randint(40, 255),randint(40, 255)))

my_canvas()
tim.setpos(-100, 150)
tim.color("red")

# change the highest number in range to draw
# different regular shapes
for shape_side_n in range(3, 15):
    draw_shape(shape_side_n)
    change_random_color()

screen.exitonclick()
