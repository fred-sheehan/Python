from turtle import Turtle, Screen, colormode
from random import randint
import random
import time

# create a Screen object
my_screen = Screen()
# Set the screen title
my_screen.title("Turtle Graphics - Random Timmy")
# Set the screen background color - color name or hex value
my_screen.bgcolor("black")
# Set the screen size -  width and height in pixels
my_screen.setup(width=1650, height=1080)

# Create a turtle object
timmy = Turtle()
# Set the turtle shape ( arrow = default)
# "arrow", "turtle", "circle", "square", "triangle", "classic"
timmy.shape("square")

colors = ["red", "blue", "green", "yellow", "orange", "purple", "white", "pink", "brown", "cyan", "magenta", "grey", "black"]

# Set the turtle color mode to 255
colormode(255)
# timmy.pencolor(randint(0,255),randint(0,255),randint(0,255))
# timmy.fillcolor(randint(0,255),randint(0,255),randint(0,255))

def random_timmy():
    for _ in range(100):
        # speed =  0 - fastest, 1 - slow, 10 - fast, 6 - normal
        # timmy.speed(random.randint(1, 3))
        timmy.speed(0)
        # Set the turtle width to change randomly (in pixels)
        timmy.width(random.randint(1, 10))
        # Set the turtle to random color from list
        timmy.pencolor(randint(0,255),randint(0,255),randint(0,255))
        # put the pen down to draw
        timmy.pendown()
        # Set the turtle to random position
        timmy.goto(random.randint(-1650, 1650), random.randint(-1080, 1080))
        # put the pen up to stop drawing
        # timmy.penup()
        # Set the turtle to another random position
        timmy.goto(random.randint(-1650, 1650), random.randint(-1080, 1080))
        # wait for brief pause
        # time.sleep(0.05)

# Call the function to draw random timmy
random_timmy()
