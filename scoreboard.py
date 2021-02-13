from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(0, 300)
        self.update()

    def update(self):
        self.write(self.score, align='center', font=('comic Sans MS', 80, 'normal'))

    def point(self, brick):
        self.clear()
        if brick.pencolor() == 'yellow':
            self.score += 1
        elif brick.pencolor() == 'green':
            self.score += 3
        elif brick.pencolor() == 'orange':
            self.score += 5
        elif brick.pencolor() == 'red':
            self.score += 7
        self.update()