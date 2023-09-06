from turtle import Turtle
INITIAL_HEIGHT = -300
MOVE_DISTANCE = 30

class Racket(Turtle):
    def __init__(self):
        super().__init__()

        # Style
        self.shape("square")
        self.color("#1D8348")
        self.penup()
        self.setheading(0)
        self.width = 3
        self.height = 1
        self.shapesize(stretch_len=3, stretch_wid=1)
        # Initial position
        self.goto(0, INITIAL_HEIGHT)

    def move_left(self):
        """ Move the racket to the left """
        if self.xcor() >= -260:
            self.back(MOVE_DISTANCE)

    def move_right(self):
        """ Move the racket to the right """
        if self.xcor() <= 240:
            self.forward(MOVE_DISTANCE)
