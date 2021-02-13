from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color('gray')
        self.penup()
        self.shape('circle')
        self.goto(0, 0)
        self.x_move = 3
        self.y_move = -3
        self.speed(0)
        self.shapesize(stretch_wid=.5)

    def move(self):
        self.setx(self.xcor() + self.x_move)
        self.sety(self.ycor() + self.y_move)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def reset(self):
        self.goto(0, 0)
        self.move_speed = .1
        self.move()