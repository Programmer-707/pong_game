from turtle import Turtle

class Paddle():

    def __init__(self, xcor, ycor):
        self.padle = Turtle("square")
        self.padle.color("white")
        self.padle.penup()
        self.padle.shapesize(stretch_wid=5, stretch_len=1)
        self.padle.goto(xcor, ycor)

    def up(self):
        newY=self.padle.ycor()+20
        X=self.padle.xcor()
        self.padle.goto(X, newY)

    def down(self):
        newY = self.padle.ycor() - 20
        X = self.padle.xcor()
        self.padle.goto(X, newY)

    def position_p(self):
        return self.padle.pos()