from turtle import Screen
from racket import Racket
from ball import Ball
from blocks import Block
from score import Score
from time import sleep
from math import hypot

# -------------------- COLLISIONS --------------------#
def wall_collision():
    global can_destroy

    # Collision with left or right wall
    if ball.xcor() <= -300 or ball.xcor() >= 280:
        ball.vertical_collision()
    # Collision with upper wall
    elif ball.ycor() >= 350:
        ball.horizontal_collision()
    # Game over
    elif ball.ycor() <= -350:
        message.update_layout('GAME OVER')
        return True
    can_destroy = True
    return False

def racket_collision():
    global can_destroy
    if ball.distance(racket) < dist_ball_racket and racket.ycor() <= ball.ycor() <= (racket.ycor() + 10):

        if ball.xcor() < racket.xcor() and ball.angle > 270 or ball.xcor() > racket.xcor() and ball.angle < 270:
            ball.angle -= 180
            ball.setheading(ball.angle)
        else:
            ball.horizontal_collision()

        can_destroy = True
        
def block_collision():
    global score, can_destroy

    for item in blocks.all_blocks:
        if ball.distance(item) <= dist_ball_block and\
                (item.ycor() - 10) <= ball.ycor() <= (item.ycor() + 10) and can_destroy:
            ball.horizontal_collision()
            item.reset()
            score += item.sp
            can_destroy = False
            return True
    return False

# -------------------- SCORE -------------------- #
def score_mark():
    if score > record:
        with open("./score.txt", "w") as f:
            f.write(str(score))
        show_record.update_layout(f"New Record: {score}")

    if score in [450, 900]:
        blocks.create_blocks()
    show_score.update_layout(f"Score: {score}")


with open("./score.txt") as file:
    record = int(file.readline())
score = 0

# -------------------- SCREEN SETUP -------------------- #
screen = Screen()
screen.setup(600, 700)
screen.title("Breakout Game")
screen.bgcolor("black")
screen.tracer(0)

# -------------------- GAME SETUP -------------------- #
racket = Racket()
ball = Ball()
blocks = Block()
show_score = Score(f"Score: {score}", -150, 320)
show_record = Score(f"Record: {record}", 130, 320)
message = Score('', 0, -50)

blocks.create_blocks()
dist_ball_block = round(hypot(blocks.width * 10, blocks.height * 10))
dist_ball_racket = round(hypot(racket.width * 10, racket.height * 10))
screen.update()

# -------------------- KEYS -------------------- #
screen.onkeypress(racket.move_left, "a")
screen.onkeypress(racket.move_left, "Left")
screen.onkeypress(racket.move_right, "d")
screen.onkeypress(racket.move_right, "Right")
screen.listen()

# -------------------- GAME LOOP -------------------- #
is_game_over = False
can_destroy = False
while not is_game_over:
    screen.update()
    sleep(ball.ball_speed)
    ball.move()

    racket_collision()
    if ball.ycor() >= 130:
        if block_collision():
            can_destroy = False
            score_mark()
            ball.ball_speed *= 0.9

    is_game_over = wall_collision()

screen.exitonclick()
