from turtle import Turtle
WIDTH = 3
HEIGHT = 1
COLUMNS = 600 // WIDTH
ROWS = 5
COLORS = ["red", "blue", "green", "yellow", "purple", "pink", "brown", "white", "black"]

class Block(Turtle):
    def __init__(self):
        super().__init__()

        self.all_blocks = []
        self.width = WIDTH
        self.height = HEIGHT

    def create_blocks(self):
        """ Create blocks in five rows and ten columns, each row have a different color """
        block_xcor = -300 + (20*WIDTH // 2)
        block_ycor = 250 - (20*HEIGHT // 2)
        points = 5

        for row in range(ROWS):
            color = COLORS[row]
            points -= 1
            for col in range(COLUMNS):
                new_block = Turtle("square")
                new_block.penup()
                new_block.color("black", color)
                new_block.shapesize(stretch_len=WIDTH, stretch_wid=HEIGHT)
                new_block.goto(block_xcor, block_ycor)
                new_block.sp = 5 + points

                self.all_blocks.append(new_block)
                block_xcor += 20*WIDTH
            block_xcor = -300 + (20 * WIDTH // 2)
            block_ycor -= 20*HEIGHT
