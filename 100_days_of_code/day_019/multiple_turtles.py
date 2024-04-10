from turtle import Turtle, Screen
from random import random, randint
from tkinter import messagebox

screen = Screen()
screen.setup(width=600, height=350)
screen.bgcolor("black")

screen.title("Turtle races - Place your bets!   red,  orange,  yellow,  green,  blue,  purple")

is_race_on = False

user_bet = screen.textinput(title="Which turtle will win the race?", prompt=" Enter a color: ")

color_list = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-75, -45, -15, 15, 45, 75]
all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(color_list[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-270, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        rand_distance = randint(0, 10)
        turtle.forward(rand_distance)

        if turtle.xcor() > 270:
            winning_color = turtle.pencolor()
            is_race_on = False

            if winning_color == user_bet:
                messagebox.showinfo(title="Race over!", message="You won! The " + winning_color + " turtle came first.")
            else:
                messagebox.showinfo(title="Race over!", message="You Lost! The winning turtle was the " + winning_color + " turtle.")


screen.exitonclick()
