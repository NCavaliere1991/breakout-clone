from turtle import Turtle


class Bricks(Turtle):
    def __init__(self):
        super().__init__()
        self.brick_list = []

    def make_bricks(self):
        x, y = -280, 250
        for i in range(8):
            for j in range(14):
                brick = Turtle()
                brick.shape('square')
                brick.shapesize(stretch_len=1.84, stretch_wid=1)
                brick.penup()
                brick.goto(x, y)
                if i <= 1:
                    brick.color('red')
                elif 1 < i <= 3:
                    brick.color('orange')
                elif 3 < i <= 5:
                    brick.color('green')
                elif 5 < i <= 7:
                    brick.color('yellow')
                self.brick_list.append(brick)
                x += 42.5
            x -= 595
            y -= 25
