from turtle import Turtle

STARTING_POSITION = (0, -180)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 180

class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def go_up(self):
        self.forward(MOVE_DISTANCE)

    def crossed_the_road(self, ycor):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False
