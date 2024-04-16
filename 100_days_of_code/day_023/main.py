import time

from turtle import Screen
from player import Player

from car_manager import CarManager
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=500, height=400)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()
scoreboard.update_scoreboard()
screen.listen()
screen.onkey(player.go_up, "Up")
level_up = 0
game_is_on = True

while game_is_on:
    time.sleep(0.1)
    car_manager.create_car()
    car_manager.move_cars()
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

        if player.crossed_the_road(180):
            level_up += 1
            scoreboard.level_up = level_up
            scoreboard.update_scoreboard()
            player.goto(0, -180)

    screen.update()

screen.exitonclick()
