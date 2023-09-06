from turtle import Turtle

class Score(Turtle):
    def __init__(self, text, pos_x, pos_y):
        super().__init__()

        # Style
        self.hideturtle()
        self.penup()
        self.color("white")
        # Position
        self.goto(pos_x, pos_y)
        # Text
        self.update_layout(text)

    def update_layout(self, text):
        """ Change turtle text """
        font_name = "Arial"
        font_size = 18
        font_kind = "bold"
        font = (font_name, font_size, font_kind)
        self.clear()
        self.write(f"{text}", False, "center", font)
