from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from ScoreBoard import ScorBoard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

paddle1=Paddle(350, 0)
paddle2=Paddle(-350, 0)
ball = Ball()
score_board = ScorBoard()

screen.listen()
screen.onkeypress(paddle1.up, "Up")
screen.onkeypress(paddle1.down, "Down")
screen.onkeypress(paddle2.up, "w")
screen.onkeypress(paddle2.down, "s")
x = 0.1
while True:
    if x < 0:
        x = 0
    time.sleep(x)
    screen.update()
    ball.move()

# detect collision of ball hitting the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

#detect collision with paddle
    if (ball.distance(paddle1.position_p()) < 50 and ball.xcor() > 320) or (ball.distance(paddle2.position_p()) < 50 and
                                                                            ball.xcor() < -320):
        ball.bounce_paddle()
        x -= 0.004

    # detect when ball goes out in right side
    if ball.xcor() > 380:
        score_board.l_score += 1
        x=0.1
        ball.new_game()
        score_board.showScore()

    # detect when ball goes out in left side
    if ball.xcor() < -380:
        score_board.r_score += 1
        x=0.1
        ball.new_game()
        score_board.showScore()








screen.exitonclick()