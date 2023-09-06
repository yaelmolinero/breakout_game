from turtle import Turtle
from random import choice
MOVE_DISTANCE = 10

class Ball(Turtle):
    def __init__(self):
        super().__init__()

        # Style
        self.shape("circle")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        # Movement
        self.ball_speed = 0.01
        self.angle = choice([220, 230, 240, 310, 320, 330])
        self.setheading(self.angle)

    def move(self):
        self.forward(MOVE_DISTANCE)

    def vertical_collision(self):
        """ Calculate the reflection angle """
        if 0 < self.angle < 180:
            self.angle = 180 - self.angle
        elif 180 < self.angle < 360:
            self.angle = 540 - self.angle
        elif self.angle == 0:
            self.angle = 25
        self.setheading(self.angle)

    def horizontal_collision(self):
        """ Calculate the reflection angle """
        self.angle = 360 - self.angle
        self.setheading(self.angle)
