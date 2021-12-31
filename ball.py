from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.x = 1

    def move(self):

            newX = self.xcor() + self.x_move
            newY = self.ycor() + self.y_move
            self.goto(newX, newY)

    def bounce(self):
        self.y_move *= -1

    def bounce_paddle(self):
        self.x_move *= -1

    def new_game(self):
        self.home()
        self.x = 1
        self.bounce()
        self.bounce_paddle()

    def speedup(self):
        self.x += 2
        self.speed(self.x)
        print(self.speed())
