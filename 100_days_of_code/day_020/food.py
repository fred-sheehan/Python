from random import randint


class Food:


    def __init__(self):
        self.food = []
        self.create_food()

    def create_food(self):
        x = randint(-280, 280)
        y = randint(-280, 280)
        self.food.append((x, y))

    def get_food(self):
        return self.food
