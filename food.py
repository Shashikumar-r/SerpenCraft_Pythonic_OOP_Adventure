import random
from turtle import Turtle
from random import randint

# TODO 4 :- creating food and collision of food and snake

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5,stretch_len=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        self.goto(randint(-280,280),randint(-280,280))
