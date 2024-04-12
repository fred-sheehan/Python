from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()

    def centreline(self):
        self.width(2)
        self.hideturtle()
        self.goto(0, 300)
        self.setheading(270)
        for _ in range(30):
            self.pendown()
            self.forward(5)
            self.penup()
            self.forward(15)

    def update_score(self, l_score, r_score):
        self.clear()
        self.goto(-100, 230)
        self.write(f"{l_score}", align="center", font=("Courier", 60, "normal"))
        self.goto(100, 230)
        self.write(f"{r_score}", align="center", font=("Courier", 60, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Courier", 60, "normal"))
