from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("dodger blue")
        self.penup()
        self.shapesize(stretch_len=3, stretch_wid=1)
        self.goto(position)

    def go_right(self):
        if self.xcor() < 260:
            self.goto(self.xcor() + 20, self.ycor())

    def go_left(self):
        if self.xcor() > -261:
            self.goto(self.xcor() - 20, self.ycor())